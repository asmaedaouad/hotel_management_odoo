from odoo import models, fields, api


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Hotel Room Type'
    _order = 'sequence, name'

    name = fields.Char('Room Type', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=10)
    code = fields.Char('Code', required=True)
    capacity = fields.Integer('Capacity (Persons)', required=True, default=1)
    description = fields.Html('Description', translate=True)
    image = fields.Image('Image', max_width=1024, max_height=1024)
    
    # Pricing
    base_price = fields.Float('Base Price per Night', required=True, default=0.0)
    currency_id = fields.Many2one('res.currency', string='Currency', 
                                   default=lambda self: self.env.company.currency_id)
    
    # Amenities
    amenity_ids = fields.Many2many('hotel.amenity', string='Amenities')
    
    # Room count
    room_count = fields.Integer('Number of Rooms', compute='_compute_room_count', store=True)
    room_ids = fields.One2many('hotel.room', 'room_type_id', string='Rooms')
    
    # Additional info
    size = fields.Float('Size (m²)')
    bed_type = fields.Selection([
        ('single', 'Single Bed'),
        ('double', 'Double Bed'),
        ('twin', 'Twin Beds'),
        ('queen', 'Queen Bed'),
        ('king', 'King Bed'),
        ('suite', 'Suite'),
    ], string='Bed Type')
    
    active = fields.Boolean('Active', default=True)
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Room type code must be unique!'),
    ]
    
    @api.depends('room_ids')
    def _compute_room_count(self):
        for record in self:
            record.room_count = len(record.room_ids)
    
    def action_view_rooms(self):
        self.ensure_one()
        return {
            'name': 'Rooms',
            'type': 'ir.actions.act_window',
            'res_model': 'hotel.room',
            'view_mode': 'tree,form',
            'domain': [('room_type_id', '=', self.id)],
            'context': {'default_room_type_id': self.id},
        }

