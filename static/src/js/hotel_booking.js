/** @odoo-module **/

// Hotel booking website JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Booking form validation and AJAX handling
    const bookingForm = document.getElementById('hotel_booking_form');
    
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            // Add custom validation here
            console.log('Booking form submitted');
        });
    }
});

