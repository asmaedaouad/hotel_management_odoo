from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'room_number'

    name = fields.Char('Room Name', compute='_compute_name', store=True)
    room_number = fields.Char('Room Number', required=True, tracking=True)
    room_type_id = fields.Many2one('hotel.room.type', string='Room Type', required=True, tracking=True)
    floor = fields.Integer('Floor', tracking=True)
    
    # Status
    state = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
        ('cleaning', 'Cleaning'),
        ('reserved', 'Reserved'),
    ], string='Status', default='available', required=True, tracking=True)
    
    # Additional info
    description = fields.Html('Description')
    notes = fields.Text('Internal Notes')
    image = fields.Image('Room Image', max_width=1024, max_height=1024)
    
    # Amenities (inherited from room type + additional)
    amenity_ids = fields.Many2many('hotel.amenity', string='Additional Amenities',
                                    help='Amenities specific to this room, in addition to room type amenities')
    
    # Reservations
    reservation_ids = fields.One2many('hotel.reservation', 'room_id', string='Reservations')
    current_reservation_id = fields.Many2one('hotel.reservation', string='Current Reservation',
                                              compute='_compute_current_reservation', store=False)
    
    # Computed fields
    is_available = fields.Boolean('Is Available', compute='_compute_is_available', store=False)
    capacity = fields.Integer('Capacity', related='room_type_id.capacity', store=True)
    base_price = fields.Float('Base Price', related='room_type_id.base_price', store=True)
    
    active = fields.Boolean('Active', default=True)
    
    _sql_constraints = [
        ('room_number_unique', 'unique(room_number)', 'Room number must be unique!'),
    ]
    
    @api.depends('room_number', 'room_type_id')
    def _compute_name(self):
        for record in self:
            if record.room_type_id:
                record.name = f"{record.room_type_id.name} - {record.room_number}"
            else:
                record.name = record.room_number or 'New Room'
    
    @api.depends('state')
    def _compute_is_available(self):
        for record in self:
            record.is_available = record.state == 'available'
    
    def _compute_current_reservation(self):
        today = fields.Date.today()
        for record in self:
            current = self.env['hotel.reservation'].search([
                ('room_id', '=', record.id),
                ('state', 'in', ['confirmed', 'checked_in']),
                ('check_in_date', '<=', today),
                ('check_out_date', '>=', today),
            ], limit=1)
            record.current_reservation_id = current.id if current else False
    
    def action_set_available(self):
        self.write({'state': 'available'})
    
    def action_set_maintenance(self):
        self.write({'state': 'maintenance'})
    
    def action_set_cleaning(self):
        self.write({'state': 'cleaning'})
    
    def action_view_reservations(self):
        self.ensure_one()
        return {
            'name': 'Reservations',
            'type': 'ir.actions.act_window',
            'res_model': 'hotel.reservation',
            'view_mode': 'tree,form,calendar',
            'domain': [('room_id', '=', self.id)],
            'context': {'default_room_id': self.id},
        }
    
    def check_availability(self, check_in, check_out):
        """Check if room is available for given dates"""
        self.ensure_one()
        if self.state not in ['available', 'reserved']:
            return False
        
        conflicting = self.env['hotel.reservation'].search([
            ('room_id', '=', self.id),
            ('state', 'in', ['confirmed', 'checked_in']),
            '|',
            '&', ('check_in_date', '<=', check_in), ('check_out_date', '>', check_in),
            '&', ('check_in_date', '<', check_out), ('check_out_date', '>=', check_out),
        ])
        return not bool(conflicting)

