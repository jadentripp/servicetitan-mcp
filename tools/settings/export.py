import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_settings_export_tools"]


def register_settings_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def settings_export_business_units(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for business units. Mirrors Export_BusinessUnits."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/export/business-units"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to export business units."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_export_employees(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for employees. Mirrors Export_Employees."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/export/employees"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to export employees."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_export_tag_types(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for tag types. Mirrors Export_TagTypes."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/export/tag-types"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to export tag types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_export_technicians(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for technicians. Mirrors Export_Technicians."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/export/technicians"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to export technicians."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



