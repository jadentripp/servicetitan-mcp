import json
from typing import Any

from ..utils import get_base_url, make_st_request

__all__ = ["register_marketingads_capacity_awareness_warning_tools"]


def register_marketingads_capacity_awareness_warning_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingads_capacity_awareness_warning_get(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Returns all capacity awareness warnings.

        Mirrors CapacityAwarenessWarning_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingads/v2/tenant/{tenant}/capacity-warnings"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch capacity awareness warnings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


