import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_transfers_tools"]


def register_inventory_transfers_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_transfers_get_list(
        tenant: int,
        ids: Optional[str] = None,
        statuses: Optional[str] = None,
        number: Optional[str] = None,
        reference_number: Optional[str] = None,
        batch_id: Optional[int] = None,
        transfer_type_ids: Optional[str] = None,
        from_location_ids: Optional[str] = None,
        to_location_ids: Optional[str] = None,
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
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of inventory transfers with filters.

        Mirrors Transfers_GetList.
        - custom_fields_operator: one of "And", "Or" (case-insensitive)
        - CSV filters (ids, statuses, transfer_type_ids, from_location_ids, to_location_ids, sync_statuses) are comma-separated strings
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/transfers"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if statuses:
            params["statuses"] = statuses
        if number:
            params["number"] = number
        if reference_number:
            params["referenceNumber"] = reference_number
        if batch_id is not None:
            params["batchId"] = batch_id
        if transfer_type_ids:
            params["transferTypeIds"] = transfer_type_ids
        if from_location_ids:
            params["fromLocationIds"] = from_location_ids
        if to_location_ids:
            params["toLocationIds"] = to_location_ids
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

        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch transfers."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_transfers_update_custom_fields(
        tenant: int,
        operations: Sequence[dict[str, Any]],
        environment: str = "production",
    ) -> str:
        """Batch update custom fields on transfers. Mirrors Transfers_UpdateCustomFields."""

        if not operations:
            return "No operations provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/transfers/custom-fields"

        body = {"operations": list(operations)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update transfer custom fields."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_transfers_update(
        tenant: int,
        id: int,
        external_data_patch_mode: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update transfer external data. Mirrors Transfers_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/transfers/{id}"

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
            return "Unable to update transfer."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


