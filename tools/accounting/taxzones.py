import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_tax_zones_tools"]


def register_tax_zones_tools(mcp: Any) -> None:
    @mcp.tool()
    async def tax_zones_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of tax zones and their rates."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/tax-zones"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if active is not None:
            params["active"] = active
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch tax zones."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


