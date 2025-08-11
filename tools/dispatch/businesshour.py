import json
from typing import Any, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_dispatch_business_hour_tools"]


def register_dispatch_business_hour_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_business_hours(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Get the business hours.

        Mirrors BusinessHour_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/business-hours"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch business hours."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_business_hours(
        tenant: int,
        weekdays: Sequence[dict[str, int]],
        saturday: Sequence[dict[str, int]],
        sunday: Sequence[dict[str, int]],
        environment: str = "production",
    ) -> str:
        """Create business hours.

        Mirrors BusinessHour_Create.
        Each time range dict must include integer keys: fromHour, toHour.
        """

        if not weekdays:
            return "'weekdays' must contain at least one time range."
        if not saturday:
            return "'saturday' must contain at least one time range."
        if not sunday:
            return "'sunday' must contain at least one time range."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/business-hours"

        body = {
            "weekdays": list(weekdays),
            "saturday": list(saturday),
            "sunday": list(sunday),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create business hours."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


