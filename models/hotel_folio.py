from odoo import models, fields, api, _


class HotelFolio(models.Model):
    _name = 'hotel.folio'
    _description = 'Hotel Folio (Guest Bill)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    name = fields.Char('Folio Number', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    reservation_id = fields.Many2one('hotel.reservation', string='Reservation', required=True, tracking=True)
    customer_id = fields.Many2one('hotel.customer', string='Customer',
                                   related='reservation_id.customer_id', store=True)
    room_id = fields.Many2one('hotel.room', string='Room',
                              related='reservation_id.room_id', store=True)
    
    date = fields.Date('Date', default=fields.Date.today, required=True)
    
    # Folio Lines
    line_ids = fields.One2many('hotel.folio.line', 'folio_id', string='Folio Lines')
    
    # Amounts
    subtotal = fields.Monetary('Subtotal', compute='_compute_amounts', store=True)
    tax_amount = fields.Monetary('Tax', compute='_compute_amounts', store=True)
    total_amount = fields.Monetary('Total', compute='_compute_amounts', store=True)
    amount_paid = fields.Monetary('Amount Paid', default=0.0)
    amount_due = fields.Monetary('Amount Due', compute='_compute_amount_due', store=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    notes = fields.Text('Notes')
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.folio') or _('New')
        return super().create(vals)
    
    @api.depends('line_ids', 'line_ids.subtotal', 'line_ids.tax_amount')
    def _compute_amounts(self):
        for record in self:
            record.subtotal = sum(record.line_ids.mapped('subtotal'))
            record.tax_amount = sum(record.line_ids.mapped('tax_amount'))
            record.total_amount = record.subtotal + record.tax_amount
    
    @api.depends('total_amount', 'amount_paid')
    def _compute_amount_due(self):
        for record in self:
            record.amount_due = record.total_amount - record.amount_paid
    
    def action_confirm(self):
        self.write({'state': 'open'})
    
    def action_mark_paid(self):
        self.write({
            'state': 'paid',
            'amount_paid': self.total_amount,
        })
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})


class HotelFolioLine(models.Model):
    _name = 'hotel.folio.line'
    _description = 'Hotel Folio Line'
    _order = 'folio_id, sequence, id'

    folio_id = fields.Many2one('hotel.folio', string='Folio', required=True, ondelete='cascade')
    sequence = fields.Integer('Sequence', default=10)
    
    date = fields.Date('Date', default=fields.Date.today, required=True)
    description = fields.Char('Description', required=True)
    
    product_id = fields.Many2one('product.product', string='Product')
    
    quantity = fields.Float('Quantity', default=1.0, required=True)
    price_unit = fields.Monetary('Unit Price', required=True)
    
    subtotal = fields.Monetary('Subtotal', compute='_compute_amounts', store=True)
    tax_rate = fields.Float('Tax Rate (%)', default=10.0)
    tax_amount = fields.Monetary('Tax Amount', compute='_compute_amounts', store=True)
    total = fields.Monetary('Total', compute='_compute_amounts', store=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   related='folio_id.currency_id', store=True)
    
    @api.depends('quantity', 'price_unit', 'tax_rate')
    def _compute_amounts(self):
        for record in self:
            record.subtotal = record.quantity * record.price_unit
            record.tax_amount = record.subtotal * (record.tax_rate / 100)
            record.total = record.subtotal + record.tax_amount

