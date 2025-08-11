import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_reporting_dynamic_value_sets_tools"]


def register_reporting_dynamic_value_sets_tools(mcp: Any) -> None:
    @mcp.tool()
    async def reporting_get_dynamic_value_set(
        tenant: int,
        dynamic_set_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """List values for a given dynamic value set (key and display name).

        Mirrors DynamicValueSets_GetDynamicSet.
        """

        if not dynamic_set_id:
            return "'dynamic_set_id' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/reporting/v2/tenant/{tenant}/dynamic-value-sets/{dynamic_set_id}"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch dynamic value set."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


