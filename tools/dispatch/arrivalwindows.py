import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_put

__all__ = ["register_dispatch_arrival_windows_tools"]


def register_dispatch_arrival_windows_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_arrival_windows(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """List arrival windows (paginated) with optional filters.

        Mirrors ArrivalWindows_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, only active returned by default.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch arrival windows."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_arrival_window(
        tenant: int,
        start: str,
        duration: str,
        business_unit_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Create a new arrival window.

        Mirrors ArrivalWindows_Create.
        """

        if not start:
            return "'start' is required."
        if not duration:
            return "'duration' is required."
        if not business_unit_ids:
            return "'business_unit_ids' must contain at least one ID."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows"

        body = {
            "start": start,
            "duration": duration,
            "businessUnitIds": list(business_unit_ids),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create arrival window."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_update_arrival_window(
        tenant: int,
        id: int,
        start: str,
        duration: str,
        business_unit_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Update an existing arrival window by ID.

        Mirrors ArrivalWindows_Update.
        """

        if not start:
            return "'start' is required."
        if not duration:
            return "'duration' is required."
        if not business_unit_ids:
            return "'business_unit_ids' must contain at least one ID."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows/{id}"

        body = {
            "start": start,
            "duration": duration,
            "businessUnitIds": list(business_unit_ids),
        }

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update arrival window."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_arrival_window(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single arrival window by ID.

        Mirrors ArrivalWindows_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch arrival window."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_set_arrival_window_activated(
        tenant: int,
        id: int,
        is_active: bool,
        environment: str = "production",
    ) -> str:
        """Set the active status of an arrival window.

        Mirrors ArrivalWindows_Activated.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows/{id}/activated"

        body = {"isActive": bool(is_active)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to set arrival window active status."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_arrival_window_configuration(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Get arrival window configuration.

        Mirrors ArrivalWindows_GetConfiguration.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows/configuration"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch arrival window configuration."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_update_arrival_window_configuration(
        tenant: int,
        configuration: str,
        environment: str = "production",
    ) -> str:
        """Update arrival window configuration.

        Mirrors ArrivalWindows_UpdatedConfiguration.
        configuration: one of "StartTimeOfArrivalWindow" or "EndTimeOfArrivalWindow".
        """

        allowed = {"starttimeofarrivalwindow", "endtimeofarrivalwindow"}
        if configuration.strip().lower() not in allowed:
            return "Invalid configuration. Use StartTimeOfArrivalWindow or EndTimeOfArrivalWindow."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/arrival-windows/configuration"

        # Preserve exact casing expected by API
        normalized_map = {
            "starttimeofarrivalwindow": "StartTimeOfArrivalWindow",
            "endtimeofarrivalwindow": "EndTimeOfArrivalWindow",
        }
        body = {"configuration": normalized_map[configuration.strip().lower()]}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update arrival window configuration."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


