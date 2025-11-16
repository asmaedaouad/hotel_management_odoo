/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class HotelDashboard extends Component {
    static template = "hotel_management.Dashboard";
}

registry.category("actions").add("hotel_management.dashboard", HotelDashboard);

