from typing import Any

from .export import register_crm_export_tools
from .bookingprovidertags import register_crm_booking_provider_tags_tools
from .bookings import register_crm_bookings_tools
from .bulktags import register_crm_bulk_tags_tools
from .contactmethods import register_crm_contact_methods_tools
from .contactpreferences import register_crm_contact_preferences_tools
from .contacts import register_crm_contacts_tools
from .customers import register_crm_customers_tools
from .leads import register_crm_leads_tools
from .locations import register_crm_locations_tools

__all__ = ["register_crm_tools"]


def register_crm_tools(mcp: Any) -> None:
    """Register CRM-related tools with the provided MCP server instance."""
    register_crm_export_tools(mcp)
    register_crm_booking_provider_tags_tools(mcp)
    register_crm_bookings_tools(mcp)
    register_crm_bulk_tags_tools(mcp)
    register_crm_contact_methods_tools(mcp)
    register_crm_contact_preferences_tools(mcp)
    register_crm_contacts_tools(mcp)
    register_crm_customers_tools(mcp)
    register_crm_leads_tools(mcp)
    register_crm_locations_tools(mcp)


