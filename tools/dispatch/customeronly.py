import json
from typing import Any, Sequence

from ..utils import get_base_url, make_st_post

__all__ = ["register_dispatch_customer_only_tools"]


def register_dispatch_customer_only_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_create_gps_pings(
        tenant: int,
        gps_provider: str,
        pings: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Create GPS pings for a given provider.

        Mirrors Gps_Create.
        Provide a list of GPS ping objects conforming to GpsPingCreateRequest.
        """

        if not gps_provider:
            return "'gps_provider' is required."
        if not pings:
            return "'pings' must contain at least one GPS ping object."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/gps-provider/{gps_provider}/gps-pings"

        body = list(pings)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create GPS pings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


