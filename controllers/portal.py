from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class HotelPortal(CustomerPortal):
    
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'reservation_count' in counters:
            values['reservation_count'] = request.env['hotel.reservation'].search_count([])
        return values
    
    @http.route(['/my/reservations', '/my/reservations/page/<int:page>'], type='http', auth='user', website=True)
    def portal_my_reservations(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        """Display customer's hotel reservations"""
        values = self._prepare_portal_layout_values()
        HotelReservation = request.env['hotel.reservation']
        
        domain = []
        
        searchbar_sortings = {
            'date': {'label': 'Check-in Date', 'order': 'check_in_date desc'},
            'name': {'label': 'Reference', 'order': 'name'},
            'state': {'label': 'Status', 'order': 'state'},
        }
        
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        
        # Count for pager
        reservation_count = HotelReservation.search_count(domain)
        
        # Pager
        pager = portal_pager(
            url="/my/reservations",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=reservation_count,
            page=page,
            step=self._items_per_page
        )
        
        # Content
        reservations = HotelReservation.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        
        values.update({
            'date': date_begin,
            'reservations': reservations,
            'page_name': 'reservation',
            'pager': pager,
            'default_url': '/my/reservations',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("hotel_management.portal_my_reservations", values)
    
    @http.route(['/my/reservations/<int:reservation_id>'], type='http', auth='user', website=True)
    def portal_reservation_detail(self, reservation_id, **kw):
        """Display reservation details"""
        reservation = request.env['hotel.reservation'].browse(reservation_id)
        
        if not reservation.exists():
            return request.not_found()
        
        values = {
            'reservation': reservation,
            'page_name': 'reservation',
        }
        return request.render("hotel_management.portal_reservation_detail", values)

