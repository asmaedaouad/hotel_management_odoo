from odoo import models, fields, api


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char('Full Name', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Related Partner', ondelete='cascade')
    
    # Contact Information
    email = fields.Char('Email', tracking=True)
    phone = fields.Char('Phone', tracking=True)
    mobile = fields.Char('Mobile', tracking=True)
    
    # Personal Information
    date_of_birth = fields.Date('Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    nationality = fields.Many2one('res.country', string='Nationality')
    
    # Identification
    id_type = fields.Selection([
        ('passport', 'Passport'),
        ('id_card', 'ID Card'),
        ('driving_license', 'Driving License'),
    ], string='ID Type')
    id_number = fields.Char('ID Number')
    id_expiry_date = fields.Date('ID Expiry Date')
    
    # Address
    street = fields.Char('Street')
    street2 = fields.Char('Street 2')
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', string='State')
    zip = fields.Char('ZIP')
    country_id = fields.Many2one('res.country', string='Country')
    
    # Customer Info
    customer_type = fields.Selection([
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('travel_agency', 'Travel Agency'),
    ], string='Customer Type', default='individual', required=True)
    
    company_name = fields.Char('Company Name')
    vip = fields.Boolean('VIP Customer', default=False)
    
    # Statistics
    reservation_ids = fields.One2many('hotel.reservation', 'customer_id', string='Reservations')
    reservation_count = fields.Integer('Total Reservations', compute='_compute_reservation_count', store=True)
    total_spent = fields.Monetary('Total Spent', compute='_compute_total_spent', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    # Preferences
    special_requests = fields.Text('Special Requests')
    notes = fields.Text('Internal Notes')
    
    active = fields.Boolean('Active', default=True)
    
    @api.depends('reservation_ids')
    def _compute_reservation_count(self):
        for record in self:
            record.reservation_count = len(record.reservation_ids)
    
    @api.depends('reservation_ids', 'reservation_ids.total_amount')
    def _compute_total_spent(self):
        for record in self:
            record.total_spent = sum(record.reservation_ids.filtered(
                lambda r: r.state in ['confirmed', 'checked_in', 'checked_out']
            ).mapped('total_amount'))
    
    @api.model
    def create(self, vals):
        # Create related partner if not exists
        if not vals.get('partner_id') and vals.get('name'):
            partner = self.env['res.partner'].create({
                'name': vals['name'],
                'email': vals.get('email'),
                'phone': vals.get('phone'),
                'mobile': vals.get('mobile'),
                'street': vals.get('street'),
                'street2': vals.get('street2'),
                'city': vals.get('city'),
                'state_id': vals.get('state_id'),
                'zip': vals.get('zip'),
                'country_id': vals.get('country_id'),
            })
            vals['partner_id'] = partner.id
        return super().create(vals)
    
    def action_view_reservations(self):
        self.ensure_one()
        return {
            'name': 'Customer Reservations',
            'type': 'ir.actions.act_window',
            'res_model': 'hotel.reservation',
            'view_mode': 'tree,form,calendar',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id},
        }

