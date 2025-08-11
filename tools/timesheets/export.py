import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_timesheets_export_tools"]


def register_timesheets_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def timesheets_export_activities(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export activities (Export_Activities)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/timesheets/v2/tenant/{tenant}/export/activities"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for activities."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def timesheets_export_activity_categories(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export activity categories (Export_ActivityCategories)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/timesheets/v2/tenant/{tenant}/export/activity-categories"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for activity categories."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def timesheets_export_activity_types(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export activity types (Export_ActivityTypes)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/timesheets/v2/tenant/{tenant}/export/activity-types"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for activity types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


