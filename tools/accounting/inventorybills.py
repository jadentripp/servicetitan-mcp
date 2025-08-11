import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_inventory_bills_tools"]


def register_inventory_bills_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_bills_get_list(
        tenant: int,
        ids: Optional[str] = None,
        batch_id: Optional[int] = None,
        batch_number: Optional[int] = None,
        bill_number: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        custom_field_fields: Optional[dict[str, str]] = None,
        custom_field_operator: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        job_number: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        purchase_order_types: Optional[str] = None,
        sync_statuses: Optional[str] = None,
        min_cost: Optional[float] = None,
        max_cost: Optional[float] = None,
        bill_type: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a filtered list of inventory bills."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/inventory-bills"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if batch_id is not None:
            params["batchId"] = batch_id
        if batch_number is not None:
            params["batchNumber"] = batch_number
        if bill_number:
            params["billNumber"] = bill_number
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if custom_field_fields:
            params["customField.Fields"] = json.dumps(custom_field_fields)
        if custom_field_operator:
            params["customField.Operator"] = custom_field_operator
        if date_from:
            params["dateFrom"] = date_from
        if date_to:
            params["dateTo"] = date_to
        if job_number:
            params["jobNumber"] = job_number
        if purchase_order_number:
            params["purchaseOrderNumber"] = purchase_order_number
        if purchase_order_types:
            params["purchaseOrderTypes"] = purchase_order_types
        if sync_statuses:
            params["syncStatuses"] = sync_statuses
        if min_cost is not None:
            params["minCost"] = min_cost
        if max_cost is not None:
            params["maxCost"] = max_cost
        if bill_type:
            params["billType"] = bill_type
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch inventory bills."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_bills_get_custom_field_types(
        tenant: int,
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
        """Get inventory bill custom field types."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/inventory-bills/custom-fields"

        params: dict[str, Any] = {}
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
            return "Unable to fetch inventory bill custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_bills_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Update custom fields on inventory bills.

        The `operations` argument should be a sequence of objects with keys:
        - objectId: int
        - customFields: list of { name: str, value: str }
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/inventory-bills/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update inventory bill custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_bills_mark_as_exported(
        tenant: int,
        inventory_bill_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Mark inventory bills as exported by ID."""

        if not inventory_bill_ids:
            return "No inventory bill IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/inventory-bills/markasexported"

        body = {"inventoryBillIds": [int(bill_id) for bill_id in inventory_bill_ids]}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark inventory bills as exported."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_bills_get_list_paginated(
        tenant: int,
        ids: Optional[str] = None,
        batch_id: Optional[int] = None,
        batch_number: Optional[int] = None,
        bill_number: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        custom_field_fields: Optional[dict[str, str]] = None,
        custom_field_operator: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        job_number: Optional[str] = None,
        purchase_order_number: Optional[str] = None,
        purchase_order_types: Optional[str] = None,
        sync_statuses: Optional[str] = None,
        min_cost: Optional[float] = None,
        max_cost: Optional[float] = None,
        bill_type: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a filtered, paginated list of inventory bills."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/inventory-bills/paginated"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if batch_id is not None:
            params["batchId"] = batch_id
        if batch_number is not None:
            params["batchNumber"] = batch_number
        if bill_number:
            params["billNumber"] = bill_number
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if custom_field_fields:
            params["customField.Fields"] = json.dumps(custom_field_fields)
        if custom_field_operator:
            params["customField.Operator"] = custom_field_operator
        if date_from:
            params["dateFrom"] = date_from
        if date_to:
            params["dateTo"] = date_to
        if job_number:
            params["jobNumber"] = job_number
        if purchase_order_number:
            params["purchaseOrderNumber"] = purchase_order_number
        if purchase_order_types:
            params["purchaseOrderTypes"] = purchase_order_types
        if sync_statuses:
            params["syncStatuses"] = sync_statuses
        if min_cost is not None:
            params["minCost"] = min_cost
        if max_cost is not None:
            params["maxCost"] = max_cost
        if bill_type:
            params["billType"] = bill_type
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch paginated inventory bills."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


