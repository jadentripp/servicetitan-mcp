import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_memberships_location_recurring_service_events_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_memberships_location_recurring_service_events_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_location_recurring_service_events_get_list(
        tenant: int,
        ids: Optional[str] = None,
        location_id: Optional[int] = None,
        job_id: Optional[int] = None,
        status: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of recurring service events.

        Mirrors LocationRecurringServiceEvents_GetList.
        - status (follow-up): NotAttempted, Unreachable, Contacted, Won, Dismissed
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-service-events"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if location_id is not None:
            params["locationId"] = int(location_id)
        if job_id is not None:
            params["jobId"] = int(job_id)
        if status is not None:
            mapped = _normalize_enum(status, {"NotAttempted", "Unreachable", "Contacted", "Won", "Dismissed"})
            if not mapped:
                return "Invalid 'status'. Use one of: NotAttempted, Unreachable, Contacted, Won, Dismissed."
            params["status"] = mapped
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch recurring service events."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_location_recurring_service_events_mark_complete(
        tenant: int,
        id: int,
        job_id: int,
        environment: str = "production",
    ) -> str:
        """Marks a recurring service event as complete.

        Mirrors LocationRecurringServiceEvents_MarkComplete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-service-events/{id}/mark-complete"

        body = {"jobId": int(job_id)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark recurring service event complete."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_location_recurring_service_events_mark_incomplete(
        tenant: int,
        id: int,
        job_id: int,
        environment: str = "production",
    ) -> str:
        """Marks a recurring service event as incomplete.

        Mirrors LocationRecurringServiceEvents_MarkIncomplete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-service-events/{id}/mark-incomplete"

        body = {"jobId": int(job_id)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark recurring service event incomplete."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


