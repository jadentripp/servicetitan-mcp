import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_vendors_tools"]


def register_inventory_vendors_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_vendors_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
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
        """Get a paginated list of vendors. Mirrors Vendors_GetList.

        - active: one of "True", "Any", "False" (case-insensitive).
        - CSV filters (ids) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/vendors"

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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch vendors."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_vendors_create(
        tenant: int,
        name: str,
        active: bool,
        is_truck_replenishment: bool,
        tax_rate: float,
        restricted_mobile_creation: bool,
        address: dict[str, Any],
        memo: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        fax: Optional[str] = None,
        delivery_option: Optional[str] = None,
        vendor_quickbooks_item: Optional[str] = None,
        payment_term_id: Optional[int] = None,
        remittance_vendor_id: Optional[int] = None,
        external_data: Optional[dict[str, Any]] = None,
        tags: Optional[Sequence[dict[str, Any]]] = None,
        vendor_contacts: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new vendor. Mirrors Vendors_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/vendors"

        body: dict[str, Any] = {
            "name": name,
            "active": bool(active),
            "isTruckReplenishment": bool(is_truck_replenishment),
            "taxRate": tax_rate,
            "restrictedMobileCreation": bool(restricted_mobile_creation),
            "address": address,
        }
        if memo is not None:
            body["memo"] = memo
        if first_name is not None:
            body["firstName"] = first_name
        if last_name is not None:
            body["lastName"] = last_name
        if phone is not None:
            body["phone"] = phone
        if email is not None:
            body["email"] = email
        if fax is not None:
            body["fax"] = fax
        if delivery_option is not None:
            body["deliveryOption"] = delivery_option
        if vendor_quickbooks_item is not None:
            body["vendorQuickbooksItem"] = vendor_quickbooks_item
        if payment_term_id is not None:
            body["paymentTermId"] = payment_term_id
        if remittance_vendor_id is not None:
            body["remittanceVendorId"] = remittance_vendor_id
        if external_data is not None:
            body["externalData"] = external_data
        if tags is not None:
            body["tags"] = list(tags)
        if vendor_contacts is not None:
            body["vendorContacts"] = list(vendor_contacts)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create vendor."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_vendors_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        active: Optional[bool] = None,
        memo: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        fax: Optional[str] = None,
        is_truck_replenishment: Optional[bool] = None,
        delivery_option: Optional[str] = None,
        tax_rate: Optional[float] = None,
        restricted_mobile_creation: Optional[bool] = None,
        vendor_quickbooks_item: Optional[str] = None,
        payment_term_id: Optional[int] = None,
        remittance_vendor_id: Optional[int] = None,
        address: Optional[dict[str, Any]] = None,
        tags: Optional[Sequence[dict[str, Any]]] = None,
        vendor_contacts: Optional[Sequence[dict[str, Any]]] = None,
        external_data_patch_mode: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing vendor. Mirrors Vendors_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/vendors/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if active is not None:
            body["active"] = bool(active)
        if memo is not None:
            body["memo"] = memo
        if first_name is not None:
            body["firstName"] = first_name
        if last_name is not None:
            body["lastName"] = last_name
        if phone is not None:
            body["phone"] = phone
        if email is not None:
            body["email"] = email
        if fax is not None:
            body["fax"] = fax
        if is_truck_replenishment is not None:
            body["isTruckReplenishment"] = bool(is_truck_replenishment)
        if delivery_option is not None:
            body["deliveryOption"] = delivery_option
        if tax_rate is not None:
            body["taxRate"] = tax_rate
        if restricted_mobile_creation is not None:
            body["restrictedMobileCreation"] = bool(restricted_mobile_creation)
        if vendor_quickbooks_item is not None:
            body["vendorQuickbooksItem"] = vendor_quickbooks_item
        if payment_term_id is not None:
            body["paymentTermId"] = payment_term_id
        if remittance_vendor_id is not None:
            body["remittanceVendorId"] = remittance_vendor_id
        if address is not None:
            body["address"] = address
        if tags is not None:
            body["tags"] = list(tags)
        if vendor_contacts is not None:
            body["vendorContacts"] = list(vendor_contacts)

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
            return "Unable to update vendor."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_vendors_get_by_id(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get vendor by ID. Mirrors Vendors_GetById."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/vendors/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch vendor by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


