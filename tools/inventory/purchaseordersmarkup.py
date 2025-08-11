import json
from typing import Any, Optional

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_put,
    make_st_delete,
)

__all__ = ["register_inventory_purchase_order_markups_tools"]


def register_inventory_purchase_order_markups_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_purchase_order_markups_get_list(
        tenant: int,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of purchase order markups.

        Mirrors PurchaseOrdersMarkup_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-markups"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
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
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch purchase order markups."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_markups_create(
        tenant: int,
        from_amount: float,
        to_amount: float,
        percent: float,
        environment: str = "production",
    ) -> str:
        """Create a new purchase order markup. Mirrors PurchaseOrdersMarkup_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-markups"

        body = {
            "from": from_amount,
            "to": to_amount,
            "percent": percent,
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create purchase order markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_markups_update(
        tenant: int,
        id: int,
        from_amount: float,
        to_amount: float,
        percent: float,
        environment: str = "production",
    ) -> str:
        """Update an existing purchase order markup. Mirrors PurchaseOrdersMarkup_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-markups/{id}"

        body = {
            "from": from_amount,
            "to": to_amount,
            "percent": percent,
        }

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update purchase order markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_markups_get_by_id(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single purchase order markup by ID. Mirrors PurchaseOrdersMarkup_GetById."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-markups/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch purchase order markup by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_markups_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete an existing purchase order markup. Mirrors PurchaseOrdersMarkup_Delete."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-markups/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete purchase order markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


