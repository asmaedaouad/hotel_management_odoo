from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HotelTransport(models.Model):
    _name = 'hotel.transport'
    _description = 'Hotel Transport Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'booking_date desc, id desc'

    name = fields.Char('Booking Number', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    # Booking Information
    reservation_id = fields.Many2one('hotel.reservation', string='Reservation')
    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True)
    
    # Vehicle Information
    vehicle_name = fields.Char('Vehicle', required=True, tracking=True, help='Vehicle name or plate number')
    driver_id = fields.Many2one('res.partner', string='Driver', tracking=True)
    
    # Trip Details
    booking_date = fields.Datetime('Booking Date', default=fields.Datetime.now, required=True)
    pickup_date = fields.Datetime('Pickup Date/Time', required=True, tracking=True)
    return_date = fields.Datetime('Return Date/Time', tracking=True)
    
    pickup_location = fields.Char('Pickup Location', required=True)
    dropoff_location = fields.Char('Drop-off Location', required=True)
    
    # Trip Type
    trip_type = fields.Selection([
        ('airport_pickup', 'Airport Pickup'),
        ('airport_dropoff', 'Airport Drop-off'),
        ('city_tour', 'City Tour'),
        ('excursion', 'Excursion'),
        ('transfer', 'Transfer'),
        ('hourly', 'Hourly Rental'),
    ], string='Trip Type', required=True, default='transfer')
    
    # Passengers
    passengers = fields.Integer('Number of Passengers', default=1, required=True)
    
    # Pricing
    distance = fields.Float('Distance (km)')
    duration = fields.Float('Duration (hours)')
    price = fields.Monetary('Price', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    # Additional Information
    special_requests = fields.Text('Special Requests')
    notes = fields.Text('Internal Notes')
    
    # Flight Information (for airport transfers)
    flight_number = fields.Char('Flight Number')
    flight_time = fields.Datetime('Flight Time')
    
    active = fields.Boolean('Active', default=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.transport') or _('New')
        return super().create(vals)
    
    # Uncomment if using Fleet module
    # @api.constrains('passengers', 'vehicle_id')
    # def _check_passenger_capacity(self):
    #     for record in self:
    #         if record.vehicle_id and record.vehicle_id.seats:
    #             if record.passengers > record.vehicle_id.seats:
    #                 raise ValidationError(
    #                     _('Number of passengers (%s) exceeds vehicle capacity (%s).') %
    #                     (record.passengers, record.vehicle_id.seats)
    #                 )
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_complete(self):
        self.write({'state': 'completed'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})


# Uncomment this class if you have the Fleet module installed
# class FleetVehicle(models.Model):
#     _inherit = 'fleet.vehicle'
#
#     # Add hotel-specific fields to fleet vehicles
#     available_for_hotel = fields.Boolean('Available for Hotel Service', default=True)
#     hourly_rate = fields.Float('Hourly Rate')
#     daily_rate = fields.Float('Daily Rate')
#     price_per_km = fields.Float('Price per KM')
#
#     transport_booking_ids = fields.One2many('hotel.transport', 'vehicle_id', string='Transport Bookings')
#     transport_count = fields.Integer('Transport Bookings', compute='_compute_transport_count')
#
#     @api.depends('transport_booking_ids')
#     def _compute_transport_count(self):
#         for record in self:
#             record.transport_count = len(record.transport_booking_ids)
#
#     def action_view_transport_bookings(self):
#         self.ensure_one()
#         return {
#             'name': 'Transport Bookings',
#             'type': 'ir.actions.act_window',
#             'res_model': 'hotel.transport',
#             'view_mode': 'tree,form,calendar',
#             'domain': [('vehicle_id', '=', self.id)],
#             'context': {'default_vehicle_id': self.id},
#         }
