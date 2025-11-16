# Hotel Management Module for Odoo 17

A comprehensive hotel management system for Odoo 17 that handles all aspects of hotel operations.

## Features

### 1. Room Management
- **Room Types**: Define different types of rooms (Standard, Deluxe, Suite, etc.)
- **Room Configuration**: Manage individual rooms with floor numbers, amenities, and status
- **Amenities**: Track room amenities (WiFi, AC, TV, Mini Bar, etc.)
- **Room Status**: Available, Occupied, Reserved, Maintenance, Cleaning

### 2. Reservation Management
- **Online Reservations**: Accept reservations from multiple sources (Direct, Website, Phone, Email, Agency)
- **Booking Workflow**: Draft → Confirmed → Checked In → Checked Out
- **Guest Information**: Track adults, children, and special requests
- **Pricing**: Automatic calculation of nights, taxes, and total amounts
- **Payment Tracking**: Monitor payment status (Unpaid, Partial, Paid, Refunded)
- **Calendar View**: Visual representation of reservations

### 3. Customer Management
- **Customer Profiles**: Store detailed customer information
- **Customer Types**: Individual, Corporate, Travel Agency
- **Identification**: Track ID type, number, and expiry
- **VIP Customers**: Mark and track VIP guests
- **Statistics**: View total reservations and spending per customer
- **Preferences**: Store special requests and preferences

### 4. Meal Management
- **Meal Types**: Define breakfast, lunch, dinner, snacks, and beverages
- **Dietary Information**: Track vegetarian, vegan, gluten-free, halal options
- **Meal Orders**: Room service and restaurant orders
- **Order Workflow**: Draft → Confirmed → Preparing → Ready → Delivered
- **Pricing**: Automatic calculation with service charges and taxes

### 5. Transport Services
- **Fleet Integration**: Uses Odoo's Fleet module for vehicle management
- **Trip Types**: Airport pickup/dropoff, city tours, excursions, transfers, hourly rentals
- **Booking Management**: Track pickup/dropoff locations, dates, and times
- **Driver Assignment**: Assign drivers to transport bookings
- **Flight Information**: Track flight details for airport transfers
- **Pricing**: Distance and duration-based pricing

### 6. Security & Access Control
- **User Groups**:
  - Hotel User: View and create reservations
  - Hotel Receptionist: Manage reservations and check-ins/outs
  - Hotel Manager: Full access to all features
- **Record Rules**: Data access based on user roles

### 7. Reporting
- **Reservation Voucher**: Printable reservation confirmation
- **Occupancy Reports**: Track room occupancy rates
- **Revenue Reports**: Monitor hotel revenue

## Installation

1. Copy the `hotel_management` folder to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Hotel Management" module

## Configuration

### Initial Setup

1. **Configure Room Types**:
   - Go to Hotel Management → Configuration → Room Types
   - Create room types (Standard, Deluxe, Suite, etc.)
   - Set pricing, capacity, and amenities

2. **Add Amenities**:
   - Go to Hotel Management → Configuration → Amenities
   - Default amenities are pre-loaded (WiFi, AC, TV, etc.)

3. **Create Rooms**:
   - Go to Hotel Management → Operations → Rooms
   - Add individual rooms with room numbers and types

4. **Configure Meal Types**:
   - Go to Hotel Management → Configuration → Meal Types
   - Define available meals and beverages

5. **Setup Fleet Vehicles** (for transport services):
   - Go to Fleet → Vehicles
   - Add vehicles and mark them as "Available for Hotel Service"

## Usage

### Creating a Reservation

1. Go to Hotel Management → Operations → Reservations
2. Click "Create"
3. Select or create a customer
4. Choose a room and dates
5. Enter guest information
6. Confirm the reservation
7. Check in the guest on arrival
8. Check out on departure

### Managing Meal Orders

1. Go to Hotel Management → Services → Meal Orders
2. Create a new order linked to a reservation
3. Add meal items
4. Confirm and track the order through preparation and delivery

### Booking Transport

1. Go to Hotel Management → Services → Transport
2. Create a new booking
3. Select customer, vehicle, and trip details
4. Confirm and track the booking

## Technical Details

### Models

- `hotel.room.type`: Room type configuration
- `hotel.amenity`: Room amenities
- `hotel.room`: Individual rooms
- `hotel.customer`: Customer information
- `hotel.reservation`: Reservations and bookings
- `hotel.meal.type`: Meal configuration
- `hotel.meal.order`: Meal orders
- `hotel.meal.order.line`: Meal order lines
- `hotel.transport`: Transport bookings

### Dependencies

- base
- web
- mail
- portal
- website
- fleet

## Future Enhancements (Client Portal)

The next phase will include:
- Customer portal for online bookings
- Room availability search
- Online payment integration
- Booking confirmation emails
- Customer dashboard

## Support

For issues or questions, please contact the module author.

## License

LGPL-3

## Author

Asmae

