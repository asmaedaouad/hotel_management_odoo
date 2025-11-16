from odoo import models, fields


class HotelAmenity(models.Model):
    _name = 'hotel.amenity'
    _description = 'Hotel Amenity'
    _order = 'name'

    name = fields.Char('Amenity Name', required=True, translate=True)
    description = fields.Text('Description', translate=True)
    icon = fields.Char('Icon Class', help='Font Awesome icon class (e.g., fa-wifi)')
    active = fields.Boolean('Active', default=True)
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Amenity name must be unique!'),
    ]

