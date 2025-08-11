import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_invoices_tools"]


def register_invoices_tools(mcp: Any) -> None:
    @mcp.tool()
    async def invoices_get_list(
        tenant: int,
        ids: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        statuses: Optional[Sequence[str]] = None,
        batch_id: Optional[int] = None,
        batch_number: Optional[int] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        custom_field_fields: Optional[dict[str, str]] = None,
        custom_field_operator: Optional[str] = None,
        include_total: bool = False,
        job_id: Optional[int] = None,
        job_number: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        invoiced_on_or_after: Optional[str] = None,
        invoiced_on_before: Optional[str] = None,
        adjustment_to_id: Optional[int] = None,
        number: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        total_greater: Optional[float] = None,
        total_less: Optional[float] = None,
        balance_filter_balance: Optional[float] = None,
        balance_filter_comparer: Optional[str] = None,
        due_date_before: Optional[str] = None,
        due_date_on_or_after: Optional[str] = None,
        order_by: Optional[str] = None,
        order_by_direction: Optional[str] = None,
        review_statuses: Optional[Sequence[str]] = None,
        assigned_to_ids: Optional[Sequence[int]] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Retrieve a paginated list of invoices with rich filters."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if statuses:
            params["statuses"] = list(statuses)
        if batch_id is not None:
            params["batchId"] = batch_id
        if batch_number is not None:
            params["batchNumber"] = batch_number
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if custom_field_fields:
            params["customField.Fields"] = json.dumps(custom_field_fields)
        if custom_field_operator:
            params["customField.Operator"] = custom_field_operator
        if include_total:
            params["includeTotal"] = True
        if job_id is not None:
            params["jobId"] = job_id
        if job_number:
            params["jobNumber"] = job_number
        if business_unit_id is not None:
            params["businessUnitId"] = business_unit_id
        if customer_id is not None:
            params["customerId"] = customer_id
        if invoiced_on_or_after:
            params["invoicedOnOrAfter"] = invoiced_on_or_after
        if invoiced_on_before:
            params["invoicedOnBefore"] = invoiced_on_before
        if adjustment_to_id is not None:
            params["adjustmentToId"] = adjustment_to_id
        if number:
            params["number"] = number
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if total_greater is not None:
            params["totalGreater"] = total_greater
        if total_less is not None:
            params["totalLess"] = total_less
        if balance_filter_balance is not None:
            params["balanceFilter.Balance"] = balance_filter_balance
        if balance_filter_comparer:
            params["balanceFilter.Comparer"] = balance_filter_comparer
        if due_date_before:
            params["dueDateBefore"] = due_date_before
        if due_date_on_or_after:
            params["dueDateOnOrAfter"] = due_date_on_or_after
        if order_by:
            params["orderBy"] = order_by
        if order_by_direction:
            params["orderByDirection"] = order_by_direction
        if review_statuses:
            params["reviewStatuses"] = list(review_statuses)
        if assigned_to_ids:
            params["assignedToIds"] = list(assigned_to_ids)
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch invoices."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_mark_as_exported(
        tenant: int,
        invoices: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Mark invoices as exported.

        invoices: list of { invoiceId: int, externalId?: str, externalMessage?: str }
        """

        if not invoices:
            return "No invoices provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/markasexported"

        body = [
            {
                "invoiceId": int(item.get("invoiceId")),
                **({"externalId": item["externalId"]} if item.get("externalId") is not None else {}),
                **({"externalMessage": item["externalMessage"]} if item.get("externalMessage") is not None else {}),
            }
            for item in invoices
            if "invoiceId" in item
        ]

        if not body:
            return "No valid invoice objects provided."

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark invoices as exported."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_update_invoice(
        tenant: int,
        id: int,
        number: Optional[str] = None,
        type_id: Optional[int] = None,
        invoiced_on: Optional[str] = None,
        subtotal: Optional[float] = None,
        tax: Optional[float] = None,
        summary: Optional[str] = None,
        royalty_status: Optional[str] = None,
        royalty_date: Optional[str] = None,
        royalty_sent_on: Optional[str] = None,
        royalty_memo: Optional[str] = None,
        export_id: Optional[str] = None,
        review_status: Optional[str] = None,
        assigned_to_id: Optional[int] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        due_date: Optional[str] = None,
        payments: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update invoice fields, items, due date, or payments."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/{id}"

        body: dict[str, Any] = {}
        if number is not None:
            body["number"] = number
        if type_id is not None:
            body["typeId"] = type_id
        if invoiced_on is not None:
            body["invoicedOn"] = invoiced_on
        if subtotal is not None:
            body["subtotal"] = subtotal
        if tax is not None:
            body["tax"] = tax
        if summary is not None:
            body["summary"] = summary
        if royalty_status is not None:
            body["royaltyStatus"] = royalty_status
        if royalty_date is not None:
            body["royaltyDate"] = royalty_date
        if royalty_sent_on is not None:
            body["royaltySentOn"] = royalty_sent_on
        if royalty_memo is not None:
            body["royaltyMemo"] = royalty_memo
        if export_id is not None:
            body["exportId"] = export_id
        if review_status is not None:
            body["reviewStatus"] = review_status
        if assigned_to_id is not None:
            body["assignedToId"] = assigned_to_id
        if items is not None:
            body["items"] = list(items)
        if due_date is not None:
            body["dueDate"] = due_date
        if payments is not None:
            body["payments"] = list(payments)

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update invoice."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_create_adjustment_invoice(
        tenant: int,
        adjustment_to_id: int,
        number: Optional[str] = None,
        type_id: Optional[int] = None,
        invoiced_on: Optional[str] = None,
        subtotal: Optional[float] = None,
        tax: Optional[float] = None,
        summary: Optional[str] = None,
        royalty_status: Optional[str] = None,
        royalty_date: Optional[str] = None,
        royalty_sent_on: Optional[str] = None,
        royalty_memo: Optional[str] = None,
        export_id: Optional[str] = None,
        review_status: Optional[str] = None,
        assigned_to_id: Optional[int] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Create an adjustment invoice targeting an existing invoice."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices"

        body: dict[str, Any] = {"adjustmentToId": adjustment_to_id}
        if number is not None:
            body["number"] = number
        if type_id is not None:
            body["typeId"] = type_id
        if invoiced_on is not None:
            body["invoicedOn"] = invoiced_on
        if subtotal is not None:
            body["subtotal"] = subtotal
        if tax is not None:
            body["tax"] = tax
        if summary is not None:
            body["summary"] = summary
        if royalty_status is not None:
            body["royaltyStatus"] = royalty_status
        if royalty_date is not None:
            body["royaltyDate"] = royalty_date
        if royalty_sent_on is not None:
            body["royaltySentOn"] = royalty_sent_on
        if royalty_memo is not None:
            body["royaltyMemo"] = royalty_memo
        if export_id is not None:
            body["exportId"] = export_id
        if review_status is not None:
            body["reviewStatus"] = review_status
        if assigned_to_id is not None:
            body["assignedToId"] = assigned_to_id
        if items is not None:
            body["items"] = list(items)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create adjustment invoice."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Update custom fields for invoices by object ID."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update invoice custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_get_custom_field_types(
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
        """Get invoice custom field types (paginated)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/custom-fields"

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
            return "Unable to fetch invoice custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_update_invoice_items(
        tenant: int,
        invoice_id: int,
        items: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Update invoice items for a specific invoice.

        The `items` payload should be a list of InvoiceItemUpdateRequest objects.
        """

        if not items:
            return "No items provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/{invoice_id}/items"

        body = list(items)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update invoice items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def invoices_delete_invoice_item(
        tenant: int,
        invoice_id: int,
        item_id: int,
        environment: str = "production",
    ) -> str:
        """Delete a single invoice item by ID."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/invoices/{invoice_id}/items/{item_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete invoice item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


