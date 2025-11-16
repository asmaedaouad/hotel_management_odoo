from odoo import models, fields


class HotelMealType(models.Model):
    _name = 'hotel.meal.type'
    _description = 'Hotel Meal Type'
    _order = 'sequence, name'

    name = fields.Char('Meal Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=10)
    description = fields.Text('Description', translate=True)
    image = fields.Image('Image', max_width=512, max_height=512)
    
    # Pricing
    price = fields.Float('Price', required=True, default=0.0)
    currency_id = fields.Many2one('res.currency', string='Currency',
                                   default=lambda self: self.env.company.currency_id)
    
    # Meal Category
    category = fields.Selection([
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('beverage', 'Beverage'),
    ], string='Category', required=True)
    
    # Availability
    available_from = fields.Float('Available From (Hour)', default=0.0)
    available_to = fields.Float('Available To (Hour)', default=24.0)
    
    # Dietary Information
    vegetarian = fields.Boolean('Vegetarian')
    vegan = fields.Boolean('Vegan')
    gluten_free = fields.Boolean('Gluten Free')
    halal = fields.Boolean('Halal')
    
    active = fields.Boolean('Active', default=True)
    
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Meal name must be unique!'),
    ]

