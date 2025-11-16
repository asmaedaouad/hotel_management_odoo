# Installation Guide

## Prerequisites

- Odoo 17.0
- Python 3.10+
- PostgreSQL 12+

## Installation

### 1. Clone or Download

```bash
git clone https://github.com/asmaedaouad/hotel_management_odoo.git
```

### 2. Copy to Addons Directory

```bash
cp -r hotel_management /path/to/odoo/addons/
```

### 3. Restart Odoo

```bash
sudo systemctl restart odoo
# or
./odoo-bin -c odoo.conf
```

### 4. Install Module

1. Go to **Apps** menu in Odoo
2. Click **Update Apps List**
3. Search for "Hotel Management"
4. Click **Install**

## Configuration

### Initial Setup

1. **Room Types**: Configuration → Room Types
2. **Amenities**: Configuration → Amenities
3. **Rooms**: Operations → Rooms
4. **Pricing Rules**: Configuration → Pricing Rules
5. **Meal Types**: Configuration → Meal Types

### User Permissions

Assign users to appropriate groups:
- **Hotel User**: View and create reservations
- **Hotel Receptionist**: Manage reservations and operations
- **Hotel Manager**: Full access

## Troubleshooting

**Module not appearing?**
- Restart Odoo
- Update apps list
- Check addons path

**Installation errors?**
- Check Odoo logs
- Verify dependencies
- Check file permissions

## Support

For issues, please open an issue on GitHub.

