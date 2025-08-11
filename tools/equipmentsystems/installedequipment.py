import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_installed_equipment_tools"]


def register_installed_equipment_tools(mcp: Any) -> None:
    @mcp.tool()
    async def equipmentsystems_get_installed_equipment(
        tenant: int,
        location_ids: Optional[str] = None,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of installed equipment with filters.

        Mirrors InstalledEquipment_GetList.
        - active: one of "True", "Any", "False" (case-insensitive)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/equipmentsystems/v2/tenant/{tenant}/installed-equipment"

        params: dict[str, Any] = {}
        if location_ids:
            params["locationIds"] = location_ids
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
        if active is not None:
            a = str(active).strip().lower()
            if a in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[a]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch installed equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def equipmentsystems_create_installed_equipment(
        tenant: int,
        location_id: int,
        name: Optional[str] = None,
        installed_on: Optional[str] = None,
        actual_replacement_date: Optional[str] = None,
        serial_number: Optional[str] = None,
        barcode_id: Optional[str] = None,
        memo: Optional[str] = None,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        cost: Optional[float] = None,
        manufacturer_warranty_start: Optional[str] = None,
        manufacturer_warranty_end: Optional[str] = None,
        service_provider_warranty_start: Optional[str] = None,
        service_provider_warranty_end: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        attachments: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Create installed equipment.

        Mirrors InstalledEquipment_Create.
        """

        if not location_id:
            return "'location_id' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/equipmentsystems/v2/tenant/{tenant}/installed-equipment"

        body: dict[str, Any] = {"locationId": int(location_id)}
        if name is not None:
            body["name"] = name
        if installed_on is not None:
            body["installedOn"] = installed_on
        if actual_replacement_date is not None:
            body["actualReplacementDate"] = actual_replacement_date
        if serial_number is not None:
            body["serialNumber"] = serial_number
        if barcode_id is not None:
            body["barcodeId"] = barcode_id
        if memo is not None:
            body["memo"] = memo
        if manufacturer is not None:
            body["manufacturer"] = manufacturer
        if model is not None:
            body["model"] = model
        if cost is not None:
            body["cost"] = float(cost)
        if manufacturer_warranty_start is not None:
            body["manufacturerWarrantyStart"] = manufacturer_warranty_start
        if manufacturer_warranty_end is not None:
            body["manufacturerWarrantyEnd"] = manufacturer_warranty_end
        if service_provider_warranty_start is not None:
            body["serviceProviderWarrantyStart"] = service_provider_warranty_start
        if service_provider_warranty_end is not None:
            body["serviceProviderWarrantyEnd"] = service_provider_warranty_end
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if attachments is not None:
            body["attachments"] = list(attachments)
        if tag_type_ids is not None:
            body["tagTypeIds"] = [int(x) for x in tag_type_ids]

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create installed equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def equipmentsystems_update_installed_equipment(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        installed_on: Optional[str] = None,
        actual_replacement_date: Optional[str] = None,
        serial_number: Optional[str] = None,
        barcode_id: Optional[str] = None,
        memo: Optional[str] = None,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        cost: Optional[float] = None,
        manufacturer_warranty_start: Optional[str] = None,
        manufacturer_warranty_end: Optional[str] = None,
        service_provider_warranty_start: Optional[str] = None,
        service_provider_warranty_end: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        attachments: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Update installed equipment.

        Mirrors InstalledEquipment_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/equipmentsystems/v2/tenant/{tenant}/installed-equipment/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if installed_on is not None:
            body["installedOn"] = installed_on
        if actual_replacement_date is not None:
            body["actualReplacementDate"] = actual_replacement_date
        if serial_number is not None:
            body["serialNumber"] = serial_number
        if barcode_id is not None:
            body["barcodeId"] = barcode_id
        if memo is not None:
            body["memo"] = memo
        if manufacturer is not None:
            body["manufacturer"] = manufacturer
        if model is not None:
            body["model"] = model
        if cost is not None:
            body["cost"] = float(cost)
        if manufacturer_warranty_start is not None:
            body["manufacturerWarrantyStart"] = manufacturer_warranty_start
        if manufacturer_warranty_end is not None:
            body["manufacturerWarrantyEnd"] = manufacturer_warranty_end
        if service_provider_warranty_start is not None:
            body["serviceProviderWarrantyStart"] = service_provider_warranty_start
        if service_provider_warranty_end is not None:
            body["serviceProviderWarrantyEnd"] = service_provider_warranty_end
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if attachments is not None:
            body["attachments"] = list(attachments)
        if tag_type_ids is not None:
            body["tagTypeIds"] = [int(x) for x in tag_type_ids]

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update installed equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


