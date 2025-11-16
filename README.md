# 🏨 Hotel Management Module for Odoo 17

[![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue.svg)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-green.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)

A comprehensive, professional-grade hotel management system for Odoo 17 that handles all aspects of hotel operations including room management, reservations, housekeeping, meal services, and tourist transport.

## ✨ Features

### 🏢 Core Operations
- **Room Management** - Complete room inventory with types, amenities, and real-time status tracking
- **Reservation System** - Full booking workflow with automatic pricing and conflict detection
- **Customer Management** - Detailed guest profiles with history and preferences
- **Housekeeping** - Task management with priority system and quality checklists
- **Folio/Billing** - Professional guest billing with line-by-line charge tracking

### 🍽️ Services
- **Meal Management** - Room service and restaurant orders with dietary information
- **Transport Services** - Tourist vehicle booking and management

### ⚙️ Configuration
- **Dynamic Pricing Rules** - Seasonal pricing, weekend rates, and special offers
- **Room Types** - Flexible room categorization with custom amenities
- **Meal Types** - Complete menu configuration

## 📊 Module Statistics

- **12 Models** - Complete data structure
- **50+ Views** - Tree, Form, Kanban, Calendar views
- **15 Menu Items** - Well-organized navigation
- **3 Professional Reports** - Reservation vouchers, folios, occupancy
- **Automated Workflows** - Checkout → Housekeeping → Available

## 🚀 Installation

### Prerequisites
- Odoo 17.0
- Python 3.10+
- PostgreSQL 12+

### Quick Install

1. **Clone the repository**
```bash
git clone https://github.com/asmaedaouad/hotel_management_odoo.git
cd hotel_management_odoo
```

2. **Copy to Odoo addons directory**
```bash
cp -r hotel_management /path/to/odoo/addons/
```

3. **Restart Odoo**
```bash
sudo systemctl restart odoo
# or
./odoo-bin -c odoo.conf
```

4. **Install the module**
- Go to Apps menu in Odoo
- Update Apps List
- Search for "Hotel Management"
- Click Install

## 📚 Documentation

- **[Installation Guide](INSTALLATION.md)** - Detailed installation instructions
- **[Quick Start](QUICK_START.md)** - Get started in 5 minutes
- **[User Guide](USER_GUIDE.md)** - Complete usage documentation
- **[What's New](WHATS_NEW.md)** - Latest features and improvements

## 🎯 Key Features Explained

### Housekeeping Management
- Automatic task creation after guest checkout
- Priority-based task assignment
- Quality control checklists
- Time tracking and performance monitoring
- Kanban board for visual management

### Dynamic Pricing
- Seasonal rate adjustments
- Weekend/weekday pricing
- Special offers and discounts
- Automatic price calculation on reservations
- Priority-based rule application

### Guest Folio System
- Complete billing management
- Multiple charge types (room, meals, services)
- Automatic tax calculation
- Payment tracking
- Professional printable bills

## 🔄 Workflows

```
Guest Checkout → Housekeeping Task Created → Task Completed → Room Available
Reservation Created → Pricing Rules Applied → Price Calculated → Booking Confirmed
```



## 🛠️ Technical Details

### Dependencies
- `base` - Odoo base module
- `web` - Web interface
- `mail` - Messaging and activities
- `portal` - Customer portal
- `website` - Website integration

### Models
- `hotel.room.type` - Room categories
- `hotel.room` - Room inventory
- `hotel.customer` - Guest profiles
- `hotel.reservation` - Bookings
- `hotel.housekeeping` - Cleaning tasks
- `hotel.pricing.rule` - Dynamic pricing
- `hotel.folio` - Guest billing
- `hotel.meal.type` - Menu items
- `hotel.meal.order` - Meal orders
- `hotel.transport` - Vehicle bookings
- And more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the LGPL-3 License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Asmae Daouad**
- GitHub: [@asmaedaouad](https://github.com/asmaedaouad)

## 🙏 Acknowledgments

- Odoo Community for the amazing framework
- All contributors and testers

## 📞 Support

For support, please open an issue in the GitHub repository or contact the author.

---

**Made with ❤️ for the hospitality industry**

