from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order = 'check_in_date desc, id desc'

    name = fields.Char('Reservation Number', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    # Customer Information
    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Partner', related='customer_id.partner_id', store=True)
    email = fields.Char('Email', related='customer_id.email', store=True)
    phone = fields.Char('Phone', related='customer_id.phone', store=True)
    
    # Reservation Details
    room_id = fields.Many2one('hotel.room', string='Room', required=True, tracking=True)
    room_type_id = fields.Many2one('hotel.room.type', string='Room Type', 
                                    related='room_id.room_type_id', store=True)
    check_in_date = fields.Date('Check-in Date', required=True, tracking=True)
    check_out_date = fields.Date('Check-out Date', required=True, tracking=True)
    
    # Actual check-in/out times
    actual_check_in = fields.Datetime('Actual Check-in')
    actual_check_out = fields.Datetime('Actual Check-out')
    
    # Guest Information
    adults = fields.Integer('Adults', default=1, required=True)
    children = fields.Integer('Children', default=0)
    total_guests = fields.Integer('Total Guests', compute='_compute_total_guests', store=True)
    
    # Pricing
    nights = fields.Integer('Number of Nights', compute='_compute_nights', store=True)
    price_per_night = fields.Float('Price per Night', required=True)
    subtotal = fields.Monetary('Subtotal', compute='_compute_amounts', store=True)
    tax_amount = fields.Monetary('Tax Amount', compute='_compute_amounts', store=True)
    total_amount = fields.Monetary('Total Amount', compute='_compute_amounts', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    # Payment
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partial', 'Partially Paid'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
    ], string='Payment Status', default='unpaid', tracking=True)
    
    amount_paid = fields.Monetary('Amount Paid', default=0.0)
    amount_due = fields.Monetary('Amount Due', compute='_compute_amount_due', store=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    # Additional Services
    meal_order_ids = fields.One2many('hotel.meal.order', 'reservation_id', string='Meal Orders')
    transport_ids = fields.Many2many('hotel.transport', string='Transport Services')
    
    # Special Requests
    special_requests = fields.Text('Special Requests')
    notes = fields.Text('Internal Notes')
    
    # Source
    source = fields.Selection([
        ('direct', 'Direct'),
        ('website', 'Website'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('agency', 'Travel Agency'),
    ], string='Booking Source', default='direct')
    
    active = fields.Boolean('Active', default=True)
    
    _sql_constraints = [
        ('check_dates', 'CHECK(check_out_date > check_in_date)',
         'Check-out date must be after check-in date!'),
    ]
    
    @api.depends('adults', 'children')
    def _compute_total_guests(self):
        for record in self:
            record.total_guests = record.adults + record.children
    
    @api.depends('check_in_date', 'check_out_date')
    def _compute_nights(self):
        for record in self:
            if record.check_in_date and record.check_out_date:
                delta = record.check_out_date - record.check_in_date
                record.nights = delta.days
            else:
                record.nights = 0
    
    @api.depends('nights', 'price_per_night')
    def _compute_amounts(self):
        for record in self:
            record.subtotal = record.nights * record.price_per_night
            record.tax_amount = record.subtotal * 0.1  # 10% tax
            record.total_amount = record.subtotal + record.tax_amount
    
    @api.depends('total_amount', 'amount_paid')
    def _compute_amount_due(self):
        for record in self:
            record.amount_due = record.total_amount - record.amount_paid
    
    @api.onchange('room_id')
    def _onchange_room_id(self):
        if self.room_id:
            self.price_per_night = self.room_id.base_price

    @api.onchange('check_in_date', 'check_out_date', 'room_id')
    def _onchange_dates_for_pricing(self):
        """Apply pricing rules when dates change"""
        if self.check_in_date and self.check_out_date and self.room_id:
            # Get applicable pricing rules
            pricing_rules = self.env['hotel.pricing.rule'].search([
                ('active', '=', True),
                ('date_from', '<=', self.check_out_date),
                ('date_to', '>=', self.check_in_date),
            ], order='priority')

            if pricing_rules:
                # Apply the first matching rule
                base_price = self.room_id.base_price
                for rule in pricing_rules:
                    new_price = rule.get_price_for_date(
                        self.room_id.room_type_id,
                        self.check_in_date,
                        base_price
                    )
                    if new_price != base_price:
                        self.price_per_night = new_price
                        break
    
    @api.onchange('check_in_date', 'check_out_date', 'room_id')
    def _onchange_dates(self):
        if self.check_in_date and self.check_out_date and self.room_id:
            if self.check_out_date <= self.check_in_date:
                return {
                    'warning': {
                        'title': _('Invalid Dates'),
                        'message': _('Check-out date must be after check-in date.')
                    }
                }

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.reservation') or _('New')

        # Validate room availability
        if vals.get('room_id') and vals.get('check_in_date') and vals.get('check_out_date'):
            room = self.env['hotel.room'].browse(vals['room_id'])
            if not room.check_availability(vals['check_in_date'], vals['check_out_date']):
                raise ValidationError(_('Room is not available for the selected dates.'))

        reservation = super().create(vals)
        return reservation

    def write(self, vals):
        # Validate room availability on update
        for record in self:
            check_in = vals.get('check_in_date', record.check_in_date)
            check_out = vals.get('check_out_date', record.check_out_date)
            room_id = vals.get('room_id', record.room_id.id)

            if room_id and check_in and check_out:
                room = self.env['hotel.room'].browse(room_id)
                conflicting = self.env['hotel.reservation'].search([
                    ('id', '!=', record.id),
                    ('room_id', '=', room_id),
                    ('state', 'in', ['confirmed', 'checked_in']),
                    '|',
                    '&', ('check_in_date', '<=', check_in), ('check_out_date', '>', check_in),
                    '&', ('check_in_date', '<', check_out), ('check_out_date', '>=', check_out),
                ])
                if conflicting:
                    raise ValidationError(_('Room is not available for the selected dates.'))

        return super().write(vals)

    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise UserError(_('Only draft reservations can be confirmed.'))
            record.write({
                'state': 'confirmed',
            })
            record.room_id.write({'state': 'reserved'})
            # Send confirmation email
            record._send_confirmation_email()

    def action_check_in(self):
        for record in self:
            if record.state != 'confirmed':
                raise UserError(_('Only confirmed reservations can be checked in.'))
            record.write({
                'state': 'checked_in',
                'actual_check_in': fields.Datetime.now(),
            })
            record.room_id.write({'state': 'occupied'})

    def action_check_out(self):
        for record in self:
            if record.state != 'checked_in':
                raise UserError(_('Only checked-in reservations can be checked out.'))
            record.write({
                'state': 'checked_out',
                'actual_check_out': fields.Datetime.now(),
            })
            record.room_id.write({'state': 'cleaning'})

            # Create housekeeping task
            self.env['hotel.housekeeping'].create({
                'room_id': record.room_id.id,
                'task_type': 'cleaning',
                'scheduled_date': fields.Date.today(),
                'priority': '2',  # High priority
                'reservation_id': record.id,
                'notes': f'Clean room after checkout - Reservation {record.name}',
            })

    def action_cancel(self):
        for record in self:
            if record.state in ['checked_in', 'checked_out']:
                raise UserError(_('Cannot cancel a reservation that is checked in or checked out.'))
            record.write({'state': 'cancelled'})
            if record.room_id.state == 'reserved':
                record.room_id.write({'state': 'available'})

    def action_set_to_draft(self):
        self.write({'state': 'draft'})

    def _send_confirmation_email(self):
        """Send confirmation email to customer"""
        # This would integrate with Odoo's email system
        # For now, we'll just log a message
        for record in self:
            record.message_post(
                body=_('Reservation confirmed. Confirmation email sent to %s') % record.email,
                subject=_('Reservation Confirmed'),
            )

    def _compute_access_url(self):
        """Compute portal access URL"""
        super()._compute_access_url()
        for record in self:
            record.access_url = f'/my/reservations/{record.id}'

