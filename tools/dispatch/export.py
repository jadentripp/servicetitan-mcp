import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_dispatch_export_tools"]


def register_dispatch_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_export_appointment_assignments(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Export feed for appointment assignments.

        Mirrors Export_AppointmentAssignments.

        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/export/appointment-assignments"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                # Preserve original casing expected by API: True/Any/False
                mapped = {"true": "True", "any": "Any", "false": "False"}[normalized]
                params["active"] = mapped
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for Dispatch appointment assignments." 

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



