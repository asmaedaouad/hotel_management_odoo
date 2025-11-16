from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HotelPricingRule(models.Model):
    _name = 'hotel.pricing.rule'
    _description = 'Hotel Pricing Rule'
    _order = 'priority, date_from'

    name = fields.Char('Rule Name', required=True)
    active = fields.Boolean('Active', default=True)
    priority = fields.Integer('Priority', default=10, help='Lower number = higher priority')
    
    # Applicability
    room_type_ids = fields.Many2many('hotel.room.type', string='Room Types',
                                      help='Leave empty to apply to all room types')
    
    # Date Range
    date_from = fields.Date('Valid From', required=True)
    date_to = fields.Date('Valid To', required=True)
    
    # Days of Week
    apply_on_monday = fields.Boolean('Monday', default=True)
    apply_on_tuesday = fields.Boolean('Tuesday', default=True)
    apply_on_wednesday = fields.Boolean('Wednesday', default=True)
    apply_on_thursday = fields.Boolean('Thursday', default=True)
    apply_on_friday = fields.Boolean('Friday', default=True)
    apply_on_saturday = fields.Boolean('Saturday', default=True)
    apply_on_sunday = fields.Boolean('Sunday', default=True)
    
    # Pricing
    price_type = fields.Selection([
        ('fixed', 'Fixed Price'),
        ('percentage', 'Percentage Adjustment'),
        ('amount', 'Amount Adjustment'),
    ], string='Price Type', required=True, default='percentage')
    
    fixed_price = fields.Float('Fixed Price')
    percentage = fields.Float('Percentage (%)', help='Positive for increase, negative for discount')
    amount = fields.Float('Amount', help='Positive for increase, negative for discount')
    
    # Minimum Stay
    min_stay = fields.Integer('Minimum Stay (nights)', default=1)
    
    # Description
    description = fields.Text('Description')
    
    _sql_constraints = [
        ('check_dates', 'CHECK(date_to >= date_from)',
         'End date must be after start date!'),
    ]
    
    @api.constrains('percentage')
    def _check_percentage(self):
        for record in self:
            if record.price_type == 'percentage' and record.percentage < -100:
                raise ValidationError(_('Percentage discount cannot be more than 100%'))
    
    def get_price_for_date(self, room_type, date, base_price):
        """Calculate price for a specific date and room type"""
        self.ensure_one()
        
        # Check if rule applies to this room type
        if self.room_type_ids and room_type not in self.room_type_ids:
            return base_price
        
        # Check if date is in range
        if not (self.date_from <= date <= self.date_to):
            return base_price
        
        # Check day of week
        weekday = date.weekday()  # 0 = Monday, 6 = Sunday
        day_applies = [
            self.apply_on_monday,
            self.apply_on_tuesday,
            self.apply_on_wednesday,
            self.apply_on_thursday,
            self.apply_on_friday,
            self.apply_on_saturday,
            self.apply_on_sunday,
        ][weekday]
        
        if not day_applies:
            return base_price
        
        # Calculate price
        if self.price_type == 'fixed':
            return self.fixed_price
        elif self.price_type == 'percentage':
            return base_price * (1 + self.percentage / 100)
        elif self.price_type == 'amount':
            return base_price + self.amount
        
        return base_price

