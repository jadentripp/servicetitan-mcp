import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_return_types_tools"]


def register_inventory_return_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_return_types_create(
        tenant: int,
        name: str,
        automatically_receive_vendor_credit: bool,
        include_in_sales_tax: bool,
        is_default: bool,
        is_default_for_consignment: bool,
        environment: str = "production",
    ) -> str:
        """Create a new Return Type. Mirrors ReturnTypes_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/return-types"

        body = {
            "name": name,
            "automaticallyReceiveVendorCredit": bool(automatically_receive_vendor_credit),
            "includeInSalesTax": bool(include_in_sales_tax),
            "isDefault": bool(is_default),
            "isDefaultForConsignment": bool(is_default_for_consignment),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create return type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_return_types_update(
        tenant: int,
        id: int,
        active: Optional[bool] = None,
        name: Optional[str] = None,
        automatically_receive_vendor_credit: Optional[bool] = None,
        include_in_sales_tax: Optional[bool] = None,
        is_default: Optional[bool] = None,
        is_default_for_consignment: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing Return Type. Mirrors ReturnTypes_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/return-types/{id}"

        body: dict[str, Any] = {"id": id}
        if active is not None:
            body["active"] = bool(active)
        if name is not None:
            body["name"] = name
        if automatically_receive_vendor_credit is not None:
            body["automaticallyReceiveVendorCredit"] = bool(automatically_receive_vendor_credit)
        if include_in_sales_tax is not None:
            body["includeInSalesTax"] = bool(include_in_sales_tax)
        if is_default is not None:
            body["isDefault"] = bool(is_default)
        if is_default_for_consignment is not None:
            body["isDefaultForConsignment"] = bool(is_default_for_consignment)

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update return type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_return_types_get_list(
        tenant: int,
        active_only: bool,
        name: Optional[str] = None,
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
        """Get a paginated list of Return Types. Mirrors ReturnTypes_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/return-types"

        params: dict[str, Any] = {"activeOnly": bool(active_only)}
        if name:
            params["name"] = name
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

        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch return types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


