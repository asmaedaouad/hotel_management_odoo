{
    'name': 'Hotel Management',
    'version': '17.0.1.0.0',
    'summary': 'Complete Hotel Management System',
    'description': """
        Hotel Management Module
        =======================
        Features:
        - Room Management (types, amenities, availability)
        - Online Reservations
        - Meal Management
        - Tourist Transport Fleet Management
        - Customer Portal
        - Reporting and Analytics
    """,
    'author': 'Asmae',
    'category': 'Services/Hotel',
    'depends': ['base', 'web', 'mail', 'portal', 'website'],
    'data': [
        # Security
        'security/hotel_security.xml',
        'security/ir.model.access.csv',

        # Data
        'data/hotel_data.xml',
        'data/room_amenities_data.xml',
        'data/default_permissions.xml',

        # Views - Configuration
        'views/hotel_room_type_views.xml',
        'views/hotel_amenity_views.xml',
        'views/hotel_meal_type_views.xml',
        'views/hotel_pricing_rule_views.xml',

        # Views - Operations
        'views/hotel_room_views.xml',
        'views/hotel_reservation_views.xml',
        'views/hotel_customer_views.xml',
        'views/hotel_housekeeping_views.xml',
        'views/hotel_folio_views.xml',

        # Views - Services
        'views/hotel_meal_order_views.xml',
        'views/hotel_transport_views.xml',

        # Views - Dashboard
        'views/hotel_dashboard_views.xml',

        # Menus
        'views/hotel_menus.xml',

        # Reports
        'reports/hotel_reservation_report.xml',
        'reports/hotel_folio_report.xml',
        'reports/hotel_occupancy_report.xml',
    ],
    'demo': [
        'demo/hotel_demo.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'hotel_management/static/src/css/hotel_dashboard.css',
    #         'hotel_management/static/src/js/hotel_dashboard.js',
    #     ],
    #     'web.assets_frontend': [
    #         'hotel_management/static/src/css/hotel_website.css',
    #         'hotel_management/static/src/js/hotel_booking.js',
    #     ],
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

