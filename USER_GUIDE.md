# Hotel Management - Complete User Guide

## 📚 Table of Contents
1. [Getting Started](#getting-started)
2. [Daily Operations](#daily-operations)
3. [Configuration](#configuration)
4. [Reports](#reports)
5. [Best Practices](#best-practices)

---

## 🚀 Getting Started

### First Time Setup

1. **Login to Odoo** as Administrator
2. **Go to Hotel Management** menu
3. **Configure Room Types** (Configuration → Room Types)
4. **Add Rooms** (Operations → Rooms)
5. **Setup Pricing Rules** (Configuration → Pricing Rules)
6. **Configure Meal Types** (Configuration → Meal Types)

---

## 📅 Daily Operations

### Morning Routine (Front Desk)

#### 1. Check Today's Arrivals
```
Hotel Management → Operations → Reservations
Filter: "Today Check-in"
```
- Review all check-ins for today
- Prepare welcome packages
- Verify room readiness

#### 2. Check Today's Departures
```
Filter: "Today Check-out"
```
- Prepare final bills
- Schedule checkout times
- Coordinate with housekeeping

#### 3. Review Housekeeping Tasks
```
Hotel Management → Operations → Housekeeping
```
- Check pending tasks
- Assign priorities
- Monitor progress

---

### Check-In Process

1. **Find Reservation**
   - Go to: Operations → Reservations
   - Search by customer name or reservation number

2. **Verify Details**
   - Check guest information
   - Confirm room type
   - Review special requests

3. **Check In Guest**
   - Click "Check In" button
   - Room status automatically changes to "Occupied"
   - Give room key to guest

4. **Create Folio** (Optional)
   - Go to: Operations → Folios/Bills
   - Create new folio
   - Link to reservation
   - Add room charges

---

### Check-Out Process

1. **Prepare Final Bill**
   - Open guest's folio
   - Add any additional charges (minibar, phone, etc.)
   - Review total amount

2. **Process Payment**
   - Collect payment from guest
   - Mark folio as "Paid"
   - Print receipt

3. **Check Out Guest**
   - Go to reservation
   - Click "Check Out" button
   - Room status changes to "Cleaning"
   - Housekeeping task automatically created

4. **Return Deposit** (if applicable)

---

### Housekeeping Operations

#### For Housekeeping Staff

1. **View Your Tasks**
   ```
   Hotel Management → Operations → Housekeeping
   Filter by: Assigned to Me
   ```

2. **Start a Task**
   - Open task
   - Click "Start" button
   - Start time is recorded

3. **Complete Checklist**
   - Check off each item as completed
   - Add notes if needed

4. **Finish Task**
   - Click "Complete" button
   - End time is recorded
   - Room status changes to "Available"

#### For Housekeeping Supervisor

1. **Assign Tasks**
   - Create new tasks
   - Assign to staff members
   - Set priorities

2. **Monitor Progress**
   - Use Kanban view
   - Check task durations
   - Identify bottlenecks

---

## ⚙️ Configuration

### Setting Up Pricing Rules

#### Example 1: Weekend Premium (+20%)
```
Name: Weekend Premium
Date From: 2024-01-01
Date To: 2024-12-31
Days: Saturday, Sunday only
Price Type: Percentage
Percentage: 20
```

#### Example 2: Summer Season (Fixed Price)
```
Name: Summer High Season
Date From: 2024-06-01
Date To: 2024-08-31
Days: All days
Price Type: Fixed Price
Fixed Price: 200.00
Room Types: Deluxe, Suite
```

#### Example 3: Early Bird Discount (-15%)
```
Name: Early Bird Discount
Date From: 2024-01-01
Date To: 2024-12-31
Days: Monday to Thursday
Price Type: Percentage
Percentage: -15
Minimum Stay: 3 nights
```

---

### Managing Room Types

1. **Create Room Type**
   - Name: e.g., "Deluxe Ocean View"
   - Code: e.g., "DOV"
   - Capacity: Number of guests
   - Base Price: Standard nightly rate
   - Bed Type: Select from dropdown
   - Size: Room size in m²

2. **Add Amenities**
   - Select from existing amenities
   - Or create new ones

3. **Add Description**
   - Write attractive description
   - Upload room photo

---

### Creating Meal Types

1. **Basic Information**
   - Name: e.g., "Continental Breakfast"
   - Category: Breakfast/Lunch/Dinner/Snack/Beverage
   - Price: Set price

2. **Availability**
   - Available From: e.g., 6:00 AM
   - Available To: e.g., 11:00 AM

3. **Dietary Info**
   - Check: Vegetarian, Vegan, Gluten-free, Halal
   - Helps guests with dietary restrictions

---

## 📊 Reports

### Reservation Voucher
- **When**: After confirming reservation
- **How**: Open reservation → Print → Reservation Voucher
- **Use**: Give to guest as confirmation

### Guest Folio
- **When**: At checkout
- **How**: Open folio → Print → Guest Folio
- **Use**: Final bill for guest

### Occupancy Report
- **When**: End of day/week/month
- **How**: Hotel Management → Reports → Occupancy
- **Use**: Track hotel performance

---

## 💡 Best Practices

### For Managers

1. **Review Pricing Rules Monthly**
   - Adjust based on demand
   - Create special offers
   - Monitor competition

2. **Monitor Housekeeping Performance**
   - Check average task duration
   - Identify training needs
   - Reward efficient staff

3. **Analyze Occupancy Trends**
   - Identify peak seasons
   - Plan staffing accordingly
   - Optimize pricing

### For Receptionists

1. **Always Confirm Reservations**
   - Don't leave in Draft status
   - Send confirmation to guest
   - Note special requests

2. **Keep Folios Updated**
   - Add charges daily
   - Don't wait until checkout
   - Avoid billing disputes

3. **Communicate with Housekeeping**
   - Report room issues
   - Coordinate early check-ins
   - Plan late checkouts

### For Housekeeping

1. **Start Tasks Promptly**
   - Click "Start" when beginning
   - Helps track efficiency
   - Improves scheduling

2. **Complete Checklists**
   - Don't skip items
   - Ensures quality
   - Reduces complaints

3. **Report Issues Immediately**
   - Use notes field
   - Create maintenance tasks
   - Prevent bigger problems

---

## 🆘 Common Issues & Solutions

### Issue: Room shows as unavailable but it's empty
**Solution**: Check room status → Click "Set Available"

### Issue: Pricing rule not applying
**Solution**: Check date range, days of week, and priority

### Issue: Can't check in guest
**Solution**: Make sure reservation is "Confirmed" first

### Issue: Housekeeping task not appearing
**Solution**: Check if checkout was completed properly

---

## 📞 Quick Reference

### Keyboard Shortcuts
- **Ctrl + K**: Quick search
- **Ctrl + Alt + H**: Go to home
- **F5**: Refresh page

### Status Colors
- 🟢 Green: Available/Completed/Paid
- 🔵 Blue: Reserved/In Progress/Open
- 🟡 Yellow: Cleaning/Pending
- 🔴 Red: Maintenance/Urgent/Cancelled

---

## 🎓 Training Checklist

### For New Receptionists
- [ ] Create a test reservation
- [ ] Check in a guest
- [ ] Create a folio
- [ ] Add charges to folio
- [ ] Check out a guest
- [ ] Print reports

### For New Housekeeping Staff
- [ ] View assigned tasks
- [ ] Start a task
- [ ] Complete checklist
- [ ] Finish a task
- [ ] Report an issue

### For Managers
- [ ] Create pricing rule
- [ ] Add new room type
- [ ] Assign user permissions
- [ ] Generate reports
- [ ] Monitor operations

---

**Need Help?** Check the README.md or IMPROVEMENTS_SUMMARY.md files!

