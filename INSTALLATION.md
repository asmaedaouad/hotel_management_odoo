# Hotel Management Module - Installation Guide

## Prerequisites

- Odoo 17 installed and running
- Access to Odoo with administrator privileges
- Fleet module installed (for transport services)

## Installation Steps

### 1. Module is Already in Place

The module is located at: `odoo-docker/ehsah_addons/hotel_management/`

### 2. Restart Odoo

Restart your Odoo instance to detect the new module:

```bash
# If using Docker Compose
docker-compose restart web
```

### 3. Update Apps List

1. Log in to Odoo as Administrator
2. Go to **Apps** menu
3. Click on **Update Apps List** (you may need to activate Developer Mode first)
4. Click **Update** in the confirmation dialog

### 4. Install the Module

1. In the Apps menu, search for "Hotel Management"
2. Click **Install** on the Hotel Management module
3. Wait for the installation to complete

### 5. Verify Installation

After installation, you should see a new menu item "Hotel Management" in the main menu.

## Post-Installation Configuration

### Step 1: Configure Room Types

1. Go to **Hotel Management → Configuration → Room Types**
2. Review the demo room types (Standard, Deluxe, Suite)
3. Modify or create new room types as needed
4. Set appropriate pricing for each room type

### Step 2: Review Amenities

1. Go to **Hotel Management → Configuration → Amenities**
2. Review the pre-loaded amenities
3. Add any additional amenities specific to your hotel

### Step 3: Create Rooms

1. Go to **Hotel Management → Operations → Rooms**
2. Review the demo rooms (101, 102, 201, 301)
3. Create additional rooms:
   - Enter room number
   - Select room type
   - Set floor number
   - Add any room-specific amenities

### Step 4: Configure Meal Types

1. Go to **Hotel Management → Configuration → Meal Types**
2. Review the demo meal types
3. Add your hotel's menu items with pricing

### Step 5: Setup Transport Fleet (Optional)

If you want to use the transport services feature:

1. Go to **Fleet → Vehicles**
2. Add your vehicles
3. Check "Available for Hotel Service"
4. Set hourly rate, daily rate, and price per km

### Step 6: Configure User Access

1. Go to **Settings → Users & Companies → Users**
2. For each user, assign appropriate hotel management groups:
   - **Hotel User**: Can view and create reservations
   - **Hotel Receptionist**: Can manage reservations and check-ins
   - **Hotel Manager**: Full access to all features

## Testing the Module

### Create a Test Reservation

1. Go to **Hotel Management → Operations → Reservations**
2. Click **Create**
3. Create or select a customer
4. Select a room
5. Set check-in and check-out dates
6. Enter guest information
7. Click **Confirm**
8. Try checking in and checking out

### Create a Test Meal Order

1. Go to **Hotel Management → Services → Meal Orders**
2. Click **Create**
3. Select a reservation
4. Add meal items
5. Confirm the order

### Create a Test Transport Booking

1. Go to **Hotel Management → Services → Transport**
2. Click **Create**
3. Select a customer
4. Choose a vehicle
5. Set pickup details
6. Confirm the booking

## Troubleshooting

### Module Not Appearing in Apps List

- Make sure you've restarted Odoo
- Update the apps list
- Check that the module is in the correct addons path

### Installation Errors

- Check Odoo logs for specific error messages
- Ensure all dependencies are installed (base, web, mail, portal, website, fleet)
- Verify file permissions

### Access Issues

- Make sure users have the correct security groups assigned
- Check that record rules are properly configured

## Next Steps

After successful installation and configuration:

1. Remove or modify demo data as needed
2. Start creating real customer records
3. Begin taking reservations
4. Train staff on using the system

## Support

For issues or questions, refer to the README.md file or contact the module developer.

