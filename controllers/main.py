from odoo import http
from odoo.http import request


class HotelWebsite(http.Controller):
    
    @http.route(['/hotel'], type='http', auth='public', website=True)
    def hotel_home(self, **kwargs):
        """Hotel website home page"""
        room_types = request.env['hotel.room.type'].sudo().search([('active', '=', True)])
        return request.render('hotel_management.hotel_home', {
            'room_types': room_types,
        })
    
    @http.route(['/hotel/rooms'], type='http', auth='public', website=True)
    def hotel_rooms(self, **kwargs):
        """Display available room types"""
        room_types = request.env['hotel.room.type'].sudo().search([('active', '=', True)])
        return request.render('hotel_management.hotel_rooms', {
            'room_types': room_types,
        })
    
    @http.route(['/hotel/room/<int:room_type_id>'], type='http', auth='public', website=True)
    def hotel_room_detail(self, room_type_id, **kwargs):
        """Display room type details"""
        room_type = request.env['hotel.room.type'].sudo().browse(room_type_id)
        if not room_type.exists():
            return request.not_found()
        
        return request.render('hotel_management.hotel_room_detail', {
            'room_type': room_type,
        })
    
    @http.route(['/hotel/booking'], type='http', auth='public', website=True)
    def hotel_booking(self, **kwargs):
        """Booking form"""
        room_types = request.env['hotel.room.type'].sudo().search([('active', '=', True)])
        return request.render('hotel_management.hotel_booking_form', {
            'room_types': room_types,
        })
    
    @http.route(['/hotel/check_availability'], type='json', auth='public')
    def check_availability(self, room_type_id, check_in, check_out, **kwargs):
        """Check room availability via AJAX"""
        room_type = request.env['hotel.room.type'].sudo().browse(int(room_type_id))
        if not room_type.exists():
            return {'error': 'Room type not found'}
        
        # Find available rooms
        available_rooms = request.env['hotel.room'].sudo().search([
            ('room_type_id', '=', room_type.id),
            ('state', 'in', ['available', 'reserved']),
        ])
        
        available = []
        for room in available_rooms:
            if room.check_availability(check_in, check_out):
                available.append({
                    'id': room.id,
                    'name': room.name,
                    'room_number': room.room_number,
                })
        
        return {
            'available': len(available) > 0,
            'rooms': available,
            'count': len(available),
        }

