from typing import Any

from .export import register_memberships_export_tools
from .customermemberships import register_memberships_customer_memberships_tools
from .invoicetemplates import register_memberships_invoice_templates_tools
from .locationrecurringserviceevents import register_memberships_location_recurring_service_events_tools
from .locationrecurringservices import register_memberships_location_recurring_services_tools
from .membershiptypes import register_memberships_membership_types_tools

__all__ = ["register_memberships_tools"]


def register_memberships_tools(mcp: Any) -> None:
    """Register Memberships-related tools with the MCP server instance."""
    register_memberships_export_tools(mcp)
    register_memberships_customer_memberships_tools(mcp)
    register_memberships_invoice_templates_tools(mcp)
    register_memberships_location_recurring_service_events_tools(mcp)
    register_memberships_location_recurring_services_tools(mcp)
    register_memberships_membership_types_tools(mcp)


