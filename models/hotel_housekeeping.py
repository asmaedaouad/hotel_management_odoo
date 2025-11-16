from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HotelHousekeeping(models.Model):
    _name = 'hotel.housekeeping'
    _description = 'Hotel Housekeeping'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, scheduled_date, id'

    name = fields.Char('Task Number', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    room_id = fields.Many2one('hotel.room', string='Room', required=True, tracking=True)
    room_number = fields.Char('Room Number', related='room_id.room_number', store=True)
    floor = fields.Integer('Floor', related='room_id.floor', store=True)
    
    task_type = fields.Selection([
        ('cleaning', 'Regular Cleaning'),
        ('deep_cleaning', 'Deep Cleaning'),
        ('maintenance', 'Maintenance'),
        ('inspection', 'Inspection'),
        ('turndown', 'Turndown Service'),
    ], string='Task Type', required=True, default='cleaning', tracking=True)
    
    scheduled_date = fields.Date('Scheduled Date', required=True, default=fields.Date.today, tracking=True)
    scheduled_time = fields.Float('Scheduled Time', help='Time in 24-hour format (e.g., 14.5 for 2:30 PM)')
    
    assigned_to = fields.Many2one('res.users', string='Assigned To', tracking=True)
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1', tracking=True)
    
    state = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='pending', required=True, tracking=True)
    
    start_time = fields.Datetime('Start Time', readonly=True)
    end_time = fields.Datetime('End Time', readonly=True)
    duration = fields.Float('Duration (hours)', compute='_compute_duration', store=True)
    
    notes = fields.Text('Notes')
    checklist_ids = fields.One2many('hotel.housekeeping.checklist', 'housekeeping_id', string='Checklist')
    
    reservation_id = fields.Many2one('hotel.reservation', string='Related Reservation')
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.housekeeping') or _('New')
        return super().create(vals)
    
    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                delta = record.end_time - record.start_time
                record.duration = delta.total_seconds() / 3600
            else:
                record.duration = 0.0
    
    def action_start(self):
        self.write({
            'state': 'in_progress',
            'start_time': fields.Datetime.now(),
        })
    
    def action_complete(self):
        self.write({
            'state': 'completed',
            'end_time': fields.Datetime.now(),
        })
        # Update room status
        if self.task_type == 'cleaning':
            self.room_id.write({'state': 'available'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})


class HotelHousekeepingChecklist(models.Model):
    _name = 'hotel.housekeeping.checklist'
    _description = 'Housekeeping Checklist Item'
    _order = 'sequence, id'

    housekeeping_id = fields.Many2one('hotel.housekeeping', string='Housekeeping Task', required=True, ondelete='cascade')
    sequence = fields.Integer('Sequence', default=10)
    name = fields.Char('Task', required=True)
    completed = fields.Boolean('Completed', default=False)
    notes = fields.Char('Notes')

