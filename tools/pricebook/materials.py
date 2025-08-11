import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_patch,
    make_st_delete,
)

__all__ = ["register_pricebook_materials_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_pricebook_materials_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_materials_get_list(
        tenant: int,
        is_other_direct_cost: Optional[bool] = None,
        cost_type_ids: Optional[str] = None,
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
        """List materials with filters and pagination.

        Mirrors Materials_GetList.
        - active: True|Any|False
        - ids, cost_type_ids: CSV strings
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials"

        params: dict[str, Any] = {}
        if is_other_direct_cost is not None:
            params["isOtherDirectCost"] = bool(is_other_direct_cost)
        if cost_type_ids:
            params["costTypeIds"] = cost_type_ids
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
            return "Unable to fetch materials."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_create(
        tenant: int,
        code: str,
        description: str,
        display_name: Optional[str] = None,
        cost: Optional[float] = None,
        active: Optional[bool] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        hours: Optional[float] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        pays_commission: Optional[bool] = None,
        deduct_as_job_cost: Optional[bool] = None,
        unit_of_measure: Optional[str] = None,
        is_inventory: Optional[bool] = None,
        account: Optional[str] = None,
        cost_of_sale_account: Optional[str] = None,
        asset_account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        taxable: Optional[bool] = None,
        primary_vendor: Optional[dict[str, Any]] = None,
        other_vendors: Optional[Sequence[dict[str, Any]]] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        categories: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        is_configurable_material: Optional[bool] = None,
        chargeable_by_default: Optional[bool] = None,
        variation_materials: Optional[Sequence[int]] = None,
        is_other_direct_cost: Optional[bool] = None,
        cost_type_id: Optional[int] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new material SKU.

        Mirrors Materials_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials"

        body: dict[str, Any] = {
            "code": code,
            "description": description,
        }
        if display_name is not None:
            body["displayName"] = display_name
        if cost is not None:
            body["cost"] = float(cost)
        if active is not None:
            body["active"] = bool(active)
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if hours is not None:
            body["hours"] = float(hours)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if deduct_as_job_cost is not None:
            body["deductAsJobCost"] = bool(deduct_as_job_cost)
        if unit_of_measure is not None:
            body["unitOfMeasure"] = unit_of_measure
        if is_inventory is not None:
            body["isInventory"] = bool(is_inventory)
        if account is not None:
            body["account"] = account
        if cost_of_sale_account is not None:
            body["costOfSaleAccount"] = cost_of_sale_account
        if asset_account is not None:
            body["assetAccount"] = asset_account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if primary_vendor is not None:
            body["primaryVendor"] = primary_vendor
        if other_vendors is not None:
            body["otherVendors"] = list(other_vendors)
        if assets is not None:
            body["assets"] = list(assets)
        if categories is not None:
            body["categories"] = list(categories)
        if external_data is not None:
            body["externalData"] = external_data
        if is_configurable_material is not None:
            body["isConfigurableMaterial"] = bool(is_configurable_material)
        if chargeable_by_default is not None:
            body["chargeableByDefault"] = bool(chargeable_by_default)
        if variation_materials is not None:
            body["variationMaterials"] = list(variation_materials)
        if is_other_direct_cost is not None:
            body["isOtherDirectCost"] = bool(is_other_direct_cost)
        if cost_type_id is not None:
            body["costTypeId"] = int(cost_type_id)
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create material."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_get_cost_types(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Get material cost types.

        Mirrors Materials_GetCostTypes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials/costtypes"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch material cost types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a material by ID.

        Mirrors Materials_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch material by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_update(
        tenant: int,
        id: int,
        code: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        cost: Optional[float] = None,
        active: Optional[bool] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        hours: Optional[float] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        pays_commission: Optional[bool] = None,
        deduct_as_job_cost: Optional[bool] = None,
        unit_of_measure: Optional[str] = None,
        is_inventory: Optional[bool] = None,
        account: Optional[str] = None,
        cost_of_sale_account: Optional[str] = None,
        asset_account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        taxable: Optional[bool] = None,
        primary_vendor: Optional[dict[str, Any]] = None,
        other_vendors: Optional[Sequence[dict[str, Any]]] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        categories: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        is_configurable_material: Optional[bool] = None,
        chargeable_by_default: Optional[bool] = None,
        variation_materials: Optional[Sequence[int]] = None,
        cost_type_id: Optional[int] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing material SKU.

        Mirrors Materials_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials/{id}"

        body: dict[str, Any] = {}
        if code is not None:
            body["code"] = code
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description
        if cost is not None:
            body["cost"] = float(cost)
        if active is not None:
            body["active"] = bool(active)
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if hours is not None:
            body["hours"] = float(hours)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if deduct_as_job_cost is not None:
            body["deductAsJobCost"] = bool(deduct_as_job_cost)
        if unit_of_measure is not None:
            body["unitOfMeasure"] = unit_of_measure
        if is_inventory is not None:
            body["isInventory"] = bool(is_inventory)
        if account is not None:
            body["account"] = account
        if cost_of_sale_account is not None:
            body["costOfSaleAccount"] = cost_of_sale_account
        if asset_account is not None:
            body["assetAccount"] = asset_account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if primary_vendor is not None:
            body["primaryVendor"] = primary_vendor
        if other_vendors is not None:
            body["otherVendors"] = list(other_vendors)
        if assets is not None:
            body["assets"] = list(assets)
        if categories is not None:
            body["categories"] = list(categories)
        if external_data is not None:
            body["externalData"] = external_data
        if is_configurable_material is not None:
            body["isConfigurableMaterial"] = bool(is_configurable_material)
        if chargeable_by_default is not None:
            body["chargeableByDefault"] = bool(chargeable_by_default)
        if variation_materials is not None:
            body["variationMaterials"] = list(variation_materials)
        if cost_type_id is not None:
            body["costTypeId"] = int(cost_type_id)
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update material."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a material by ID.

        Mirrors Materials_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materials/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete material."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


