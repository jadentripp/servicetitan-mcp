import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_adjustments_tools"]


def register_inventory_adjustments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_adjustments_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        number: Optional[str] = None,
        reference_number: Optional[str] = None,
        batch_id: Optional[int] = None,
        invoice_ids: Optional[str] = None,
        inventory_location_ids: Optional[str] = None,
        adjustment_types: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        sync_statuses: Optional[str] = None,
        custom_fields_fields: Optional[dict[str, str]] = None,
        custom_fields_operator: Optional[str] = None,
        date_on_or_after: Optional[str] = None,
        date_before: Optional[str] = None,
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
        """Get a paginated list of inventory adjustments with filters.

        Mirrors Adjustments_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        - custom_fields_operator: one of "And", "Or" (case-insensitive).
        - CSV filters (ids, invoice_ids, etc.) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/adjustments"

        params: dict[str, Any] = {}

        if ids:
            params["ids"] = ids

        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values
        if number:
            params["number"] = number
        if reference_number:
            params["referenceNumber"] = reference_number
        if batch_id is not None:
            params["batchId"] = batch_id
        if invoice_ids:
            params["invoiceIds"] = invoice_ids
        if inventory_location_ids:
            params["inventoryLocationIds"] = inventory_location_ids
        if adjustment_types:
            params["adjustmentTypes"] = adjustment_types
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if sync_statuses:
            params["syncStatuses"] = sync_statuses

        if custom_fields_fields:
            # Pass object as JSON string per existing conventions
            params["customFields.Fields"] = json.dumps(custom_fields_fields)
        if custom_fields_operator is not None:
            op_norm = str(custom_fields_operator).strip().lower()
            if op_norm in {"and", "or"}:
                params["customFields.Operator"] = {"and": "And", "or": "Or"}[op_norm]
            else:
                return "Invalid 'custom_fields_operator'. Use one of: And, Or."

        if date_on_or_after:
            params["dateOnOrAfter"] = date_on_or_after
        if date_before:
            params["dateBefore"] = date_before
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
            return "Unable to fetch inventory adjustments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_adjustments_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Batch update custom fields on adjustments.

        operations: list of { objectId: int, customFields: [{ name: str, value: str }] }
        Mirrors Adjustments_UpdateCustomFields.
        """

        if not operations:
            return "No operations provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/adjustments/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update adjustment custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_adjustments_update(
        tenant: int,
        id: int,
        external_data_patch_mode: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing adjustment (external data).

        Mirrors Adjustments_Update.
        Provide any of: external_data_patch_mode (Replace|Merge),
        external_data_application_guid (guid), external_data_items (list of {key,value}).
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/adjustments/{id}"

        body: dict[str, Any] = {}

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
            return "Unable to update inventory adjustment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


