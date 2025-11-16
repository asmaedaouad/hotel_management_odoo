from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HotelMealOrder(models.Model):
    _name = 'hotel.meal.order'
    _description = 'Hotel Meal Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'order_date desc, id desc'

    name = fields.Char('Order Number', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    # Order Information
    reservation_id = fields.Many2one('hotel.reservation', string='Reservation', required=True)
    customer_id = fields.Many2one('hotel.customer', string='Customer',
                                   related='reservation_id.customer_id', store=True)
    room_id = fields.Many2one('hotel.room', string='Room',
                              related='reservation_id.room_id', store=True)
    
    # Order Details
    order_date = fields.Datetime('Order Date', default=fields.Datetime.now, required=True)
    delivery_date = fields.Datetime('Delivery Date', required=True)
    delivery_location = fields.Selection([
        ('room', 'Room Service'),
        ('restaurant', 'Restaurant'),
        ('poolside', 'Poolside'),
        ('garden', 'Garden'),
    ], string='Delivery Location', default='room', required=True)
    
    # Order Lines
    order_line_ids = fields.One2many('hotel.meal.order.line', 'order_id', string='Order Lines')
    
    # Pricing
    subtotal = fields.Monetary('Subtotal', compute='_compute_amounts', store=True)
    service_charge = fields.Monetary('Service Charge', compute='_compute_amounts', store=True)
    tax_amount = fields.Monetary('Tax Amount', compute='_compute_amounts', store=True)
    total_amount = fields.Monetary('Total Amount', compute='_compute_amounts', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    # Special Instructions
    special_instructions = fields.Text('Special Instructions')
    notes = fields.Text('Internal Notes')
    
    @api.depends('order_line_ids', 'order_line_ids.subtotal')
    def _compute_amounts(self):
        for record in self:
            record.subtotal = sum(record.order_line_ids.mapped('subtotal'))
            record.service_charge = record.subtotal * 0.05  # 5% service charge
            record.tax_amount = (record.subtotal + record.service_charge) * 0.1  # 10% tax
            record.total_amount = record.subtotal + record.service_charge + record.tax_amount
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.meal.order') or _('New')
        return super().create(vals)
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_prepare(self):
        self.write({'state': 'preparing'})
    
    def action_ready(self):
        self.write({'state': 'ready'})
    
    def action_deliver(self):
        self.write({'state': 'delivered'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})


class HotelMealOrderLine(models.Model):
    _name = 'hotel.meal.order.line'
    _description = 'Hotel Meal Order Line'
    _order = 'order_id, sequence, id'

    order_id = fields.Many2one('hotel.meal.order', string='Order', required=True, ondelete='cascade')
    sequence = fields.Integer('Sequence', default=10)
    
    meal_type_id = fields.Many2one('hotel.meal.type', string='Meal', required=True)
    description = fields.Text('Description')
    
    quantity = fields.Integer('Quantity', default=1, required=True)
    price_unit = fields.Float('Unit Price', required=True)
    subtotal = fields.Monetary('Subtotal', compute='_compute_subtotal', store=True)
    
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   related='order_id.currency_id', store=True)
    
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.quantity * record.price_unit
    
    @api.onchange('meal_type_id')
    def _onchange_meal_type_id(self):
        if self.meal_type_id:
            self.price_unit = self.meal_type_id.price
            self.description = self.meal_type_id.description

