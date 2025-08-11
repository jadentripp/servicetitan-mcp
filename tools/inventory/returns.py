import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_returns_tools"]


def register_inventory_returns_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_returns_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        number: Optional[str] = None,
        reference_number: Optional[str] = None,
        job_id: Optional[int] = None,
        purchase_order_id: Optional[int] = None,
        batch_id: Optional[int] = None,
        vendor_ids: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        inventory_location_ids: Optional[str] = None,
        sync_statuses: Optional[str] = None,
        custom_fields_fields: Optional[dict[str, str]] = None,
        custom_fields_operator: Optional[str] = None,
        return_date_on_or_after: Optional[str] = None,
        return_date_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of returns with filters.

        Mirrors Returns_GetList.
        - active: one of "True", "Any", "False" (case-insensitive).
        - custom_fields_operator: one of "And", "Or" (case-insensitive).
        - CSV filters (ids, vendor_ids, etc.) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/returns"

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
        if reference_number:
            params["referenceNumber"] = reference_number
        if job_id is not None:
            params["jobId"] = job_id
        if purchase_order_id is not None:
            params["purchaseOrderId"] = purchase_order_id
        if batch_id is not None:
            params["batchId"] = batch_id
        if vendor_ids:
            params["vendorIds"] = vendor_ids
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if inventory_location_ids:
            params["inventoryLocationIds"] = inventory_location_ids
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

        if return_date_on_or_after:
            params["returnDateOnOrAfter"] = return_date_on_or_after
        if return_date_before:
            params["returnDateBefore"] = return_date_before
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

        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch returns."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_returns_create_return(
        tenant: int,
        vendor_id: int,
        return_type_id: int,
        business_unit_id: int,
        inventory_location_id: int,
        return_date: str,
        tax: float,
        shipping: float,
        restocking_fee: float,
        items: Optional[Sequence[dict[str, Any]]] = None,
        job_id: Optional[int] = None,
        purchase_order_id: Optional[int] = None,
        reference_number: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new return. Mirrors Returns_CreateReturn."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/returns"

        body: dict[str, Any] = {
            "vendorId": vendor_id,
            "returnTypeId": return_type_id,
            "businessUnitId": business_unit_id,
            "inventoryLocationId": inventory_location_id,
            "returnDate": return_date,
            "tax": tax,
            "shipping": shipping,
            "restockingFee": restocking_fee,
        }

        if items is not None:
            body["items"] = list(items)
        if job_id is not None:
            body["jobId"] = job_id
        if purchase_order_id is not None:
            body["purchaseOrderId"] = purchase_order_id
        if reference_number is not None:
            body["referenceNumber"] = reference_number
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create return."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_returns_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Batch update custom fields on returns. Mirrors Returns_UpdateCustomFields."""

        if not operations:
            return "No operations provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/returns/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update return custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_returns_update(
        tenant: int,
        id: int,
        return_type_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        reference_number: Optional[str] = None,
        inventory_location_id: Optional[int] = None,
        return_date: Optional[str] = None,
        memo: Optional[str] = None,
        tax: Optional[float] = None,
        shipping: Optional[float] = None,
        restocking_fee: Optional[float] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        external_data_patch_mode: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update a return. Mirrors Returns_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/returns/{id}"

        body: dict[str, Any] = {}
        if return_type_id is not None:
            body["returnTypeId"] = return_type_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if reference_number is not None:
            body["referenceNumber"] = reference_number
        if inventory_location_id is not None:
            body["inventoryLocationId"] = inventory_location_id
        if return_date is not None:
            body["returnDate"] = return_date
        if memo is not None:
            body["memo"] = memo
        if tax is not None:
            body["tax"] = tax
        if shipping is not None:
            body["shipping"] = shipping
        if restocking_fee is not None:
            body["restockingFee"] = restocking_fee
        if items is not None:
            body["items"] = list(items)

        external_data: dict[str, Any] = {}
        if external_data_patch_mode is not None:
            mode_norm = str(external_data_patch_mode).strip().lower()
            if mode_norm in {"replace", "merge"}:
                external_data["patchMode"] = {"replace": "Replace", "merge": "Merge"}[mode_norm]
            else:
                return "Invalid 'external_data_patch_mode'. Use one of: Replace, Merge."

        if external_data_application_guid is not None:
            external_data["applicationGuid"] = external_data_application_guid
        if external_data_items is not None:
            external_data["externalData"] = list(external_data_items)
        if external_data:
            body["externalData"] = external_data

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update return."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_returns_cancel(
        tenant: int,
        id: int,
        canceled_reason: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Cancel a return. Mirrors Returns_Cancel.

        canceled_reason: one of NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled (case-insensitive)
        """

        allowed = {"NotRequired", "Duplicate", "Accidental", "VendorIssue", "Other", "JobCanceled"}
        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/returns/{id}/cancellation"

        body: dict[str, Any] = {}
        if canceled_reason is not None:
            lower_map = {a.lower(): a for a in allowed}
            mapped = lower_map.get(str(canceled_reason).strip().lower())
            if mapped is None:
                return "Invalid 'canceled_reason'. Use one of: NotRequired, Duplicate, Accidental, VendorIssue, Other, JobCanceled."
            body["canceledReason"] = mapped

        data = await make_st_post(url, json_body=(body or None))
        if not data:
            return "Unable to cancel return."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


