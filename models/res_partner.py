from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_hotel_customer = fields.Boolean('Is Hotel Customer', default=False)
    hotel_customer_id = fields.One2many('hotel.customer', 'partner_id', string='Hotel Customer Profile')
    hotel_reservation_ids = fields.One2many('hotel.reservation', 'partner_id', string='Hotel Reservations')
    hotel_reservation_count = fields.Integer('Reservations', compute='_compute_hotel_reservation_count')
    
    @api.depends('hotel_reservation_ids')
    def _compute_hotel_reservation_count(self):
        for record in self:
            record.hotel_reservation_count = len(record.hotel_reservation_ids)
    
    def action_view_hotel_reservations(self):
        self.ensure_one()
        return {
            'name': 'Hotel Reservations',
            'type': 'ir.actions.act_window',
            'res_model': 'hotel.reservation',
            'view_mode': 'tree,form,calendar',
            'domain': [('partner_id', '=', self.id)],
            'context': {'default_partner_id': self.id},
        }

