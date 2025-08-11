import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_payments_tools"]


def register_payments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payments_get_list(
        tenant: int,
        ids: Optional[str] = None,
        applied_to_invoice_ids: Optional[str] = None,
        applied_to_reference_number: Optional[str] = None,
        statuses: Optional[str] = None,
        paid_on_after: Optional[str] = None,
        paid_on_before: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        batch_number: Optional[int] = None,
        batch_id: Optional[int] = None,
        transaction_type: Optional[str] = None,
        customer_id: Optional[int] = None,
        total_greater: Optional[float] = None,
        total_less: Optional[float] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        custom_field_fields: Optional[dict[str, str]] = None,
        custom_field_operator: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of payments with filters."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payments"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if applied_to_invoice_ids:
            params["appliedToInvoiceIds"] = applied_to_invoice_ids
        if applied_to_reference_number:
            params["appliedToReferenceNumber"] = applied_to_reference_number
        if statuses:
            params["statuses"] = statuses
        if paid_on_after:
            params["paidOnAfter"] = paid_on_after
        if paid_on_before:
            params["paidOnBefore"] = paid_on_before
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if batch_number is not None:
            params["batchNumber"] = batch_number
        if batch_id is not None:
            params["batchId"] = batch_id
        if transaction_type:
            params["transactionType"] = transaction_type
        if customer_id is not None:
            params["customerId"] = customer_id
        if total_greater is not None:
            params["totalGreater"] = total_greater
        if total_less is not None:
            params["totalLess"] = total_less
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if custom_field_fields:
            params["customField.Fields"] = json.dumps(custom_field_fields)
        if custom_field_operator:
            params["customField.Operator"] = custom_field_operator
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch payments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payments_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Update custom fields for specified payments."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payments/custom-fields"

        body = {"operations": list(operations)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update payment custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payments_get_custom_field_types(
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
        """Get payment custom field types (paginated)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payments/custom-fields"

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
            return "Unable to fetch payment custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payments_update_status(
        tenant: int,
        status: str,
        payment_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Batch update payment status."""

        if not payment_ids:
            return "No payment IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payments/status"

        body = {"status": status, "paymentIds": [int(pid) for pid in payment_ids]}
        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update payment status."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payments_update(
        tenant: int,
        id: int,
        type_id: int,
        splits: Sequence[dict[str, Any]],
        active: Optional[bool] = None,
        memo: Optional[str] = None,
        paid_on: Optional[str] = None,
        auth_code: Optional[str] = None,
        check_number: Optional[str] = None,
        export_id: Optional[str] = None,
        status: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Patch update a payment."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/payments/{id}"

        body: dict[str, Any] = {
            "typeId": type_id,
            "splits": list(splits),
        }
        if active is not None:
            body["active"] = active
        if memo is not None:
            body["memo"] = memo
        if paid_on is not None:
            body["paidOn"] = paid_on
        if auth_code is not None:
            body["authCode"] = auth_code
        if check_number is not None:
            body["checkNumber"] = check_number
        if export_id is not None:
            body["exportId"] = export_id
        if status is not None:
            body["status"] = status

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update payment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


