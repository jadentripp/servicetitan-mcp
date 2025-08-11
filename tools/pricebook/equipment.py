import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_pricebook_equipment_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_pricebook_equipment_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_equipment_create(
        tenant: int,
        code: str,
        description: str,
        display_name: Optional[str] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        active: Optional[bool] = None,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        manufacturer_warranty: Optional[dict[str, Any]] = None,
        service_provider_warranty: Optional[dict[str, Any]] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        categories: Optional[Sequence[int]] = None,
        primary_vendor: Optional[dict[str, Any]] = None,
        other_vendors: Optional[Sequence[dict[str, Any]]] = None,
        account: Optional[str] = None,
        cost_of_sale_account: Optional[str] = None,
        asset_account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        cross_sale_group: Optional[str] = None,
        pays_commission: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        hours: Optional[float] = None,
        taxable: Optional[bool] = None,
        cost: Optional[float] = None,
        unit_of_measure: Optional[str] = None,
        is_inventory: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        equipment_materials: Optional[Sequence[dict[str, Any]]] = None,
        recommendations: Optional[Sequence[dict[str, Any]]] = None,
        upgrades: Optional[Sequence[int]] = None,
        is_configurable_equipment: Optional[bool] = None,
        variation_equipment: Optional[Sequence[int]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        dimensions: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new equipment SKU.

        Mirrors Equipment_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/equipment"

        body: dict[str, Any] = {
            "code": code,
            "description": description,
        }
        if display_name is not None:
            body["displayName"] = display_name
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if active is not None:
            body["active"] = bool(active)
        if manufacturer is not None:
            body["manufacturer"] = manufacturer
        if model is not None:
            body["model"] = model
        if manufacturer_warranty is not None:
            body["manufacturerWarranty"] = manufacturer_warranty
        if service_provider_warranty is not None:
            body["serviceProviderWarranty"] = service_provider_warranty
        if assets is not None:
            body["assets"] = list(assets)
        if categories is not None:
            body["categories"] = list(categories)
        if primary_vendor is not None:
            body["primaryVendor"] = primary_vendor
        if other_vendors is not None:
            body["otherVendors"] = list(other_vendors)
        if account is not None:
            body["account"] = account
        if cost_of_sale_account is not None:
            body["costOfSaleAccount"] = cost_of_sale_account
        if asset_account is not None:
            body["assetAccount"] = asset_account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if hours is not None:
            body["hours"] = float(hours)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if cost is not None:
            body["cost"] = float(cost)
        if unit_of_measure is not None:
            body["unitOfMeasure"] = unit_of_measure
        if is_inventory is not None:
            body["isInventory"] = bool(is_inventory)
        if external_data is not None:
            body["externalData"] = external_data
        if equipment_materials is not None:
            body["equipmentMaterials"] = list(equipment_materials)
        if recommendations is not None:
            body["recommendations"] = list(recommendations)
        if upgrades is not None:
            body["upgrades"] = list(upgrades)
        if is_configurable_equipment is not None:
            body["isConfigurableEquipment"] = bool(is_configurable_equipment)
        if variation_equipment is not None:
            body["variationEquipment"] = list(variation_equipment)
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type
        if dimensions is not None:
            body["dimensions"] = dimensions

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_equipment_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of equipment.

        Mirrors Equipment_GetList.
        - active: True|Any|False
        - ids: CSV up to 50
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/equipment"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort
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
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch equipment list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_equipment_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get equipment by ID.

        Mirrors Equipment_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/equipment/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch equipment by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_equipment_update(
        tenant: int,
        id: int,
        code: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        active: Optional[bool] = None,
        manufacturer: Optional[str] = None,
        model: Optional[str] = None,
        manufacturer_warranty: Optional[dict[str, Any]] = None,
        service_provider_warranty: Optional[dict[str, Any]] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        recommendations: Optional[Sequence[dict[str, Any]]] = None,
        upgrades: Optional[Sequence[int]] = None,
        equipment_materials: Optional[Sequence[dict[str, Any]]] = None,
        categories: Optional[Sequence[int]] = None,
        primary_vendor: Optional[dict[str, Any]] = None,
        other_vendors: Optional[Sequence[dict[str, Any]]] = None,
        account: Optional[str] = None,
        cost_of_sale_account: Optional[str] = None,
        asset_account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        cross_sale_group: Optional[str] = None,
        pays_commission: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        hours: Optional[float] = None,
        taxable: Optional[bool] = None,
        cost: Optional[float] = None,
        unit_of_measure: Optional[str] = None,
        is_inventory: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        is_configurable_equipment: Optional[bool] = None,
        variation_equipment: Optional[Sequence[int]] = None,
        dimensions: Optional[dict[str, Any]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing equipment SKU.

        Mirrors Equipment_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/equipment/{id}"

        body: dict[str, Any] = {}
        if code is not None:
            body["code"] = code
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if active is not None:
            body["active"] = bool(active)
        if manufacturer is not None:
            body["manufacturer"] = manufacturer
        if model is not None:
            body["model"] = model
        if manufacturer_warranty is not None:
            body["manufacturerWarranty"] = manufacturer_warranty
        if service_provider_warranty is not None:
            body["serviceProviderWarranty"] = service_provider_warranty
        if assets is not None:
            body["assets"] = list(assets)
        if recommendations is not None:
            body["recommendations"] = list(recommendations)
        if upgrades is not None:
            body["upgrades"] = list(upgrades)
        if equipment_materials is not None:
            body["equipmentMaterials"] = list(equipment_materials)
        if categories is not None:
            body["categories"] = list(categories)
        if primary_vendor is not None:
            body["primaryVendor"] = primary_vendor
        if other_vendors is not None:
            body["otherVendors"] = list(other_vendors)
        if account is not None:
            body["account"] = account
        if cost_of_sale_account is not None:
            body["costOfSaleAccount"] = cost_of_sale_account
        if asset_account is not None:
            body["assetAccount"] = asset_account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if hours is not None:
            body["hours"] = float(hours)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if cost is not None:
            body["cost"] = float(cost)
        if unit_of_measure is not None:
            body["unitOfMeasure"] = unit_of_measure
        if is_inventory is not None:
            body["isInventory"] = bool(is_inventory)
        if external_data is not None:
            body["externalData"] = external_data
        if is_configurable_equipment is not None:
            body["isConfigurableEquipment"] = bool(is_configurable_equipment)
        if variation_equipment is not None:
            body["variationEquipment"] = list(variation_equipment)
        if dimensions is not None:
            body["dimensions"] = dimensions
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_equipment_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete equipment by ID.

        Mirrors Equipment_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/equipment/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


