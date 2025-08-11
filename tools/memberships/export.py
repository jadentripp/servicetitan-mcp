import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_memberships_export_tools"]


def register_memberships_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_export_invoice_templates(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for invoice templates (Memberships).

        Mirrors Export_InvoiceTemplates.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/invoice-templates"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for invoice templates."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_membership_status_changes(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for customer membership status changes.

        Mirrors Export_MembershipStatusChanges.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/membership-status-changes"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for membership status changes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_membership_types(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for membership types.

        Mirrors Export_MembershipTypes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/membership-types"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for membership types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_memberships(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for customer memberships.

        Mirrors Export_Memberships.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/memberships"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for memberships."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_location_recurring_service_events(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for recurring service events.

        Mirrors Export_LocationRecurringServiceEvents.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/recurring-service-events"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for recurring service events."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_recurring_service_types(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for recurring service types.

        Mirrors Export_RecurringServiceTypes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/recurring-service-types"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for recurring service types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_export_location_recurring_services(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for recurring services.

        Mirrors Export_LocationRecurringServices.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/export/recurring-services"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for recurring services."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


