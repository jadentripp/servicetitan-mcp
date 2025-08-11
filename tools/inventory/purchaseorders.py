import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_purchase_orders_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    key = v.lower()
    return lower_map.get(key, v)


def register_inventory_purchase_orders_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_purchase_orders_get_list(
        tenant: int,
        ids: Optional[str] = None,
        status: Optional[str] = None,
        number: Optional[str] = None,
        job_id: Optional[int] = None,
        job_ids: Optional[str] = None,
        technician_id: Optional[int] = None,
        project_id: Optional[int] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        date_on_or_after: Optional[str] = None,
        date_before: Optional[str] = None,
        sent_on_or_after: Optional[str] = None,
        sent_before: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a list of purchase orders (paginated) with filters.

        Mirrors PurchaseOrders_GetList.
        - status: one of Pending, Sent, PartiallyReceived, Received, Exported, Canceled (case-insensitive)
        - CSV filters (ids, job_ids) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if status:
            normalized = _normalize_enum(
                status,
                {"Pending", "Sent", "PartiallyReceived", "Received", "Exported", "Canceled"},
            )
            params["status"] = normalized
        if number:
            params["number"] = number
        if job_id is not None:
            params["jobId"] = job_id
        if job_ids:
            params["jobIds"] = job_ids
        if technician_id is not None:
            params["technicianId"] = technician_id
        if project_id is not None:
            params["projectId"] = project_id
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if date_on_or_after:
            params["dateOnOrAfter"] = date_on_or_after
        if date_before:
            params["dateBefore"] = date_before
        if sent_on_or_after:
            params["sentOnOrAfter"] = sent_on_or_after
        if sent_before:
            params["sentBefore"] = sent_before
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
            return "Unable to fetch purchase orders."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_create(
        tenant: int,
        vendor_id: int,
        type_id: int,
        business_unit_id: int,
        inventory_location_id: int,
        ship_to: dict[str, Any],
        impacts_technician_payroll: bool,
        date: str,
        required_on: str,
        tax: float,
        shipping: float,
        items: Sequence[dict[str, Any]],
        job_id: Optional[int] = None,
        technician_id: Optional[int] = None,
        project_id: Optional[int] = None,
        vendor_invoice_number: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new purchase order.

        Mirrors PurchaseOrders_Create.
        Provide `ship_to` as CreateAddressRequest and `items` as list of CreatePurchaseOrderItemRequest.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders"

        body: dict[str, Any] = {
            "vendorId": vendor_id,
            "typeId": type_id,
            "businessUnitId": business_unit_id,
            "inventoryLocationId": inventory_location_id,
            "shipTo": ship_to,
            "impactsTechnicianPayroll": bool(impacts_technician_payroll),
            "date": date,
            "requiredOn": required_on,
            "tax": tax,
            "shipping": shipping,
            "items": list(items),
        }

        if job_id is not None:
            body["jobId"] = job_id
        if technician_id is not None:
            body["technicianId"] = technician_id
        if project_id is not None:
            body["projectId"] = project_id
        if vendor_invoice_number is not None:
            body["vendorInvoiceNumber"] = vendor_invoice_number
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create purchase order."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_get_by_id(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single purchase order by ID. Mirrors PurchaseOrders_GetById."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch purchase order by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_update(
        tenant: int,
        id: int,
        vendor_id: Optional[int] = None,
        type_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        inventory_location_id: Optional[int] = None,
        job_id: Optional[int] = None,
        technician_id: Optional[int] = None,
        project_id: Optional[int] = None,
        ship_to: Optional[dict[str, Any]] = None,
        vendor_invoice_number: Optional[str] = None,
        impacts_technician_payroll: Optional[bool] = None,
        memo: Optional[str] = None,
        date: Optional[str] = None,
        required_on: Optional[str] = None,
        tax: Optional[float] = None,
        shipping: Optional[float] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing purchase order. Mirrors PurchaseOrders_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/{id}"

        body: dict[str, Any] = {}
        if vendor_id is not None:
            body["vendorId"] = vendor_id
        if type_id is not None:
            body["typeId"] = type_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if inventory_location_id is not None:
            body["inventoryLocationId"] = inventory_location_id
        if job_id is not None:
            body["jobId"] = job_id
        if technician_id is not None:
            body["technicianId"] = technician_id
        if project_id is not None:
            body["projectId"] = project_id
        if ship_to is not None:
            body["shipTo"] = ship_to
        if vendor_invoice_number is not None:
            body["vendorInvoiceNumber"] = vendor_invoice_number
        if impacts_technician_payroll is not None:
            body["impactsTechnicianPayroll"] = bool(impacts_technician_payroll)
        if memo is not None:
            body["memo"] = memo
        if date is not None:
            body["date"] = date
        if required_on is not None:
            body["requiredOn"] = required_on
        if tax is not None:
            body["tax"] = tax
        if shipping is not None:
            body["shipping"] = shipping
        if items is not None:
            body["items"] = list(items)

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update purchase order."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_get_requests(
        tenant: int,
        ids: Optional[str] = None,
        request_status: Optional[str] = None,
        request_number: Optional[str] = None,
        job_id: Optional[int] = None,
        job_ids: Optional[str] = None,
        technician_id: Optional[int] = None,
        project_id: Optional[int] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        date_on_or_after: Optional[str] = None,
        date_before: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a list of purchase order requests (paginated).

        Mirrors PurchaseOrders_GetRequests.
        - request_status: one of PendingApproval, Approved, Rejected (case-insensitive)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/requests"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if request_status:
            normalized = _normalize_enum(request_status, {"PendingApproval", "Approved", "Rejected"})
            params["requestStatus"] = normalized
        if request_number:
            params["requestNumber"] = request_number
        if job_id is not None:
            params["jobId"] = job_id
        if job_ids:
            params["jobIds"] = job_ids
        if technician_id is not None:
            params["technicianId"] = technician_id
        if project_id is not None:
            params["projectId"] = project_id
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if date_on_or_after:
            params["dateOnOrAfter"] = date_on_or_after
        if date_before:
            params["dateBefore"] = date_before
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
            return "Unable to fetch purchase order requests."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_approve_request(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Approve a purchase order request. Mirrors PurchaseOrders_ApproveRequest."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/requests/{id}/approve"

        data = await make_st_post(url)
        if not data:
            return "Unable to approve purchase order request."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_reject_request(
        tenant: int,
        id: int,
        rejection_reason: str,
        environment: str = "production",
    ) -> str:
        """Reject a purchase order request with a reason.

        rejection_reason: one of CostTooHigh, WrongVendor, Other (case-insensitive)
        Mirrors PurchaseOrders_RejectRequest.
        """

        allowed = {"CostTooHigh", "WrongVendor", "Other"}
        normalized = _normalize_enum(rejection_reason, allowed)
        if normalized not in allowed:
            return "Invalid 'rejection_reason'. Use one of: CostTooHigh, WrongVendor, Other."

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/requests/{id}/reject"

        body = {"rejectionReason": normalized}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to reject purchase order request."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_orders_cancel(
        tenant: int,
        id: int,
        canceled_reason: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Cancel a purchase order. Mirrors PurchaseOrders_Cancel.

        canceled_reason: one of NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled (case-insensitive)
        """

        allowed = {"NotRequired", "Duplicate", "Accidental", "VendorIssue", "Other", "JobCanceled"}
        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-orders/{id}/cancellation"

        body: dict[str, Any] = {}
        if canceled_reason is not None:
            normalized = _normalize_enum(canceled_reason, allowed)
            if normalized not in allowed:
                return "Invalid 'canceled_reason'. Use one of: NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled."
            body["canceledReason"] = normalized

        data = await make_st_post(url, json_body=(body or None))
        if not data:
            return "Unable to cancel purchase order."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


