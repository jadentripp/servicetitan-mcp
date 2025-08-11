import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_crm_export_tools"]


def register_crm_export_tools(mcp: Any) -> None:
    """Register CRM export tools (bookings, etc.)."""

    @mcp.tool()
    async def crm_export_bookings(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export bookings from ServiceTitan CRM API.

        Mirrors ExportBookings_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/bookings"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM bookings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_export_customers(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export customers from ServiceTitan CRM API.

        Mirrors ExportCustomers_GetCustomers.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/customers"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM customers."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_export_customer_contacts(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export customer contacts from ServiceTitan CRM API.

        Mirrors ExportContacts_CustomersContacts.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/customers/contacts"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM customer contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_export_leads(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export leads from ServiceTitan CRM API.

        Mirrors ExportLeads_Leads.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/leads"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM leads."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_export_locations(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export locations from ServiceTitan CRM API.

        Mirrors ExportLocations_Locations.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/locations"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM locations."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_export_location_contacts(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export location contacts from ServiceTitan CRM API.

        Mirrors ExportContacts_LocationsContacts.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/export/locations/contacts"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for CRM location contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



