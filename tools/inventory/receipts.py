import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_inventory_receipts_tools"]


def register_inventory_receipts_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_receipts_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        number: Optional[str] = None,
        vendor_invoice_number: Optional[str] = None,
        bill_id: Optional[int] = None,
        batch_id: Optional[int] = None,
        vendor_ids: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        inventory_location_ids: Optional[str] = None,
        purchase_order_ids: Optional[str] = None,
        sync_statuses: Optional[str] = None,
        custom_fields_fields: Optional[dict[str, str]] = None,
        custom_fields_operator: Optional[str] = None,
        received_on_or_after: Optional[str] = None,
        received_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of receipts with filters.

        Mirrors Receipts_GetList.
        - active: one of "True", "Any", "False" (case-insensitive).
        - custom_fields_operator: one of "And", "Or" (case-insensitive).
        - CSV filters (ids, vendor_ids, etc.) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/receipts"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids

        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        if number:
            params["number"] = number
        if vendor_invoice_number:
            params["vendorInvoiceNumber"] = vendor_invoice_number
        if bill_id is not None:
            params["billId"] = bill_id
        if batch_id is not None:
            params["batchId"] = batch_id
        if vendor_ids:
            params["vendorIds"] = vendor_ids
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if inventory_location_ids:
            params["inventoryLocationIds"] = inventory_location_ids
        if purchase_order_ids:
            params["purchaseOrderIds"] = purchase_order_ids
        if sync_statuses:
            params["syncStatuses"] = sync_statuses

        if custom_fields_fields:
            params["customFields.Fields"] = json.dumps(custom_fields_fields)
        if custom_fields_operator is not None:
            op_norm = str(custom_fields_operator).strip().lower()
            if op_norm in {"and", "or"}:
                params["customFields.Operator"] = {"and": "And", "or": "Or"}[op_norm]
            else:
                return "Invalid 'custom_fields_operator'. Use one of: And, Or."

        if received_on_or_after:
            params["receivedOnOrAfter"] = received_on_or_after
        if received_before:
            params["receivedBefore"] = received_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
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
            return "Unable to fetch receipts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_receipts_create_receipt(
        tenant: int,
        purchase_order_id: int,
        date_received: str,
        tax: float,
        shipping: float,
        items: Sequence[dict[str, Any]],
        vendor_document_number: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a receipt for a purchase order. Mirrors Receipts_CreateReceipt."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/receipts"

        body: dict[str, Any] = {
            "purchaseOrderId": purchase_order_id,
            "dateReceived": date_received,
            "tax": tax,
            "shipping": shipping,
            "items": list(items),
        }
        if vendor_document_number is not None:
            body["vendorDocumentNumber"] = vendor_document_number
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create receipt."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_receipts_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Batch update custom fields on receipts. Mirrors Receipts_UpdateCustomFields."""

        if not operations:
            return "No operations provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/receipts/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update receipt custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_receipts_cancel_receipts(
        tenant: int,
        id: int,
        query_id: Optional[int] = None,
        canceled_reason: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Cancel a receipt. Mirrors Receipts_CancelReceipts.

        canceled_reason: one of NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled (case-insensitive)
        """

        allowed = {"NotRequired", "Duplicate", "Accidental", "VendorIssue", "Other", "JobCanceled"}
        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/receipts/{id}/cancellation"

        params: dict[str, Any] = {}
        if query_id is not None:
            params["id"] = int(query_id)

        body: dict[str, Any] = {}
        if canceled_reason is not None:
            normalized = str(canceled_reason).strip()
            # Normalize case-insensitive to API enums
            lower_map = {a.lower(): a for a in allowed}
            mapped = lower_map.get(normalized.lower())
            if mapped is None:
                return "Invalid 'canceled_reason'. Use one of: NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled."
            body["canceledReason"] = mapped

        data = await make_st_post(url, json_body=(body or None), params=(params or None))
        if not data:
            return "Unable to cancel receipt."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


