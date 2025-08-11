import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_schedulingpro_scheduler_tools"]


def register_schedulingpro_scheduler_tools(mcp: Any) -> None:
    @mcp.tool()
    async def schedulingpro_get_schedulers(
        tenant: int,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a list of schedulers.

        Mirrors Scheduler_Schedulers.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/schedulingpro/v2/tenant/{tenant}/schedulers"

        params: dict[str, Any] = {}
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch schedulers."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def schedulingpro_get_scheduler_performance(
        tenant: int,
        id: str,
        session_created_on_or_after: str,
        session_created_before: str,
        environment: str = "production",
    ) -> str:
        """Provides performance data for scheduler.

        Mirrors Scheduler_SchedulerPerformance.
        Required times are RFC3339 date-time strings (UTC).
        """

        if not id:
            return "'id' is required."
        if not session_created_on_or_after or not session_created_before:
            return "Both 'session_created_on_or_after' and 'session_created_before' are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/schedulingpro/v2/tenant/{tenant}/schedulers/{id}/performance"

        params = {
            "sessionCreatedOnOrAfter": session_created_on_or_after,
            "sessionCreatedBefore": session_created_before,
        }

        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch scheduler performance."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def schedulingpro_get_scheduler_sessions(
        tenant: int,
        id: str,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of sessions for scheduler.

        Mirrors Scheduler_SchedulerSessions.
        """

        if not id:
            return "'id' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/schedulingpro/v2/tenant/{tenant}/schedulers/{id}/sessions"

        params: dict[str, Any] = {}
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch scheduler sessions."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


