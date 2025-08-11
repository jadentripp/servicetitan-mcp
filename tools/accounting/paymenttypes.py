import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payment_types_tools"]


def register_payment_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payment_types_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of payment types."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payment-types"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if active is not None:
            params["active"] = active
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
            return "Unable to fetch payment types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payment_types_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a payment type by ID."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payment-types/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch payment type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


