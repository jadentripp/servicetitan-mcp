import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_post

__all__ = ["register_dispatch_capacity_tools"]


def register_dispatch_capacity_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_capacity(
        tenant: int,
        starts_on_or_after: str,
        ends_on_or_before: str,
        business_unit_ids: Optional[Sequence[int]] = None,
        job_type_id: Optional[int] = None,
        skill_based_availability: bool = True,
        environment: str = "production",
    ) -> str:
        """Get capacity/availability for a time window.

        Mirrors Capacity_GetList.
        Required: starts_on_or_after, ends_on_or_before, skill_based_availability.
        """

        if not starts_on_or_after:
            return "'starts_on_or_after' is required."
        if not ends_on_or_before:
            return "'ends_on_or_before' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/capacity"

        body: dict[str, Any] = {
            "startsOnOrAfter": starts_on_or_after,
            "endsOnOrBefore": ends_on_or_before,
            "skillBasedAvailability": bool(skill_based_availability),
        }
        if business_unit_ids:
            body["businessUnitIds"] = list(business_unit_ids)
        if job_type_id is not None:
            body["jobTypeId"] = int(job_type_id)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to fetch capacity."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


