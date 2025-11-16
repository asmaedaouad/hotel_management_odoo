# Hotel Management - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Install the Module (2 minutes)

1. **Restart Odoo**
   ```bash
   cd odoo-docker
   docker-compose restart web
   ```

2. **Update Apps List**
   - Login to Odoo as Administrator
   - Go to **Apps**
   - Click **Update Apps List** (activate Developer Mode if needed: Settings → Activate Developer Mode)
   - Click **Update**

3. **Install Module**
   - Search for "Hotel Management"
   - Click **Install**
   - Wait for installation to complete

### Step 2: Quick Configuration (3 minutes)

The module comes with demo data pre-loaded. You can start using it immediately or customize:

#### Option A: Use Demo Data (Fastest)
The module includes:
- ✅ 3 Room Types (Standard, Deluxe, Suite)
- ✅ 4 Rooms (101, 102, 201, 301)
- ✅ 15 Amenities (WiFi, AC, TV, etc.)
- ✅ 3 Meal Types

**You can start creating reservations right away!**

#### Option B: Customize (Recommended)

1. **Review Room Types**
   - Go to: **Hotel Management → Configuration → Room Types**
   - Modify prices and amenities as needed

2. **Add Your Rooms**
   - Go to: **Hotel Management → Operations → Rooms**
   - Click **Create** and add your actual rooms

3. **Configure Meals**
   - Go to: **Hotel Management → Configuration → Meal Types**
   - Add your restaurant menu items

### Step 3: Create Your First Reservation

1. **Go to Reservations**
   - Click: **Hotel Management → Operations → Reservations**
   - Click **Create**

2. **Fill in Details**
   - **Customer**: Click "Create and Edit" to add a new customer
     - Enter name, email, phone
     - Save
   - **Room**: Select from available rooms (e.g., "Standard Room - 101")
   - **Check-in Date**: Select arrival date
   - **Check-out Date**: Select departure date
   - **Adults**: Enter number of adults (default: 1)
   - **Children**: Enter number of children (default: 0)

3. **Confirm Reservation**
   - Review the automatically calculated price
   - Click **Confirm** button
   - The room status will change to "Reserved"

4. **Check In Guest**
   - When guest arrives, click **Check In** button
   - Room status changes to "Occupied"

5. **Check Out Guest**
   - When guest leaves, click **Check Out** button
   - Room status changes to "Cleaning"

### Step 4: Try Other Features

#### Create a Meal Order
1. Go to: **Hotel Management → Services → Meal Orders**
2. Click **Create**
3. Select the reservation
4. Add meal items in "Order Lines" tab
5. Click **Confirm**

#### Book Transport Service
1. Go to: **Hotel Management → Services → Transport**
2. Click **Create**
3. Select customer and vehicle
4. Enter pickup/dropoff details
5. Click **Confirm**

## 📊 Understanding the Dashboard

Access: **Hotel Management → Dashboard**

The dashboard shows:
- Current occupancy rate
- Today's check-ins and check-outs
- Pending reservations
- Revenue statistics

## 👥 User Roles

Assign roles to your staff:

1. Go to: **Settings → Users & Companies → Users**
2. Edit a user
3. In "Hotel Management" section, assign:
   - **Hotel User**: For basic staff (view only)
   - **Hotel Receptionist**: For front desk (manage reservations)
   - **Hotel Manager**: For managers (full access)

## 📱 Common Tasks

### Check Room Availability
1. Go to: **Hotel Management → Operations → Rooms**
2. Use filters to see available rooms
3. Or use Calendar view in Reservations to see bookings

### View Customer History
1. Go to: **Hotel Management → Operations → Customers**
2. Open a customer record
3. Click "Reservations" smart button to see all bookings

### Print Reservation Voucher
1. Open a reservation
2. Click **Print** → **Reservation Voucher**

### Cancel a Reservation
1. Open the reservation
2. Click **Cancel** button
3. Room status returns to "Available"

## 🔧 Troubleshooting

### Can't see the module?
- Make sure you restarted Odoo
- Update the apps list
- Check you're logged in as Administrator

### Room shows as unavailable?
- Check room status in Rooms list
- If "Maintenance" or "Cleaning", click the room and use "Set Available" button

### Can't create reservation?
- Make sure you have at least one room created
- Check that dates are valid (check-out > check-in)
- Verify room is available for those dates

## 📚 Next Steps

1. **Remove Demo Data** (if needed)
   - Go to each configuration menu
   - Delete demo records
   - Create your own

2. **Add More Rooms**
   - Create all your actual rooms
   - Assign correct room types
   - Set floor numbers

3. **Train Your Staff**
   - Show them how to create reservations
   - Demonstrate check-in/check-out process
   - Explain meal and transport booking

4. **Customize Pricing**
   - Adjust room type prices
   - Set seasonal rates (future feature)
   - Configure meal prices

## 🎯 Tips for Success

- ✅ Always confirm reservations (don't leave them in Draft)
- ✅ Check in guests on arrival (updates room status)
- ✅ Check out guests on departure (triggers cleaning)
- ✅ Use special requests field for customer preferences
- ✅ Track VIP customers for special treatment
- ✅ Review occupancy reports regularly

## 📞 Need Help?

- Check the **README.md** for detailed documentation
- Review **INSTALLATION.md** for installation issues
- See **MODULE_SUMMARY.md** for technical details

## 🎉 You're Ready!

Your hotel management system is now set up and ready to use. Start taking reservations and managing your hotel operations efficiently!

---

**Happy Hoteling! 🏨**

