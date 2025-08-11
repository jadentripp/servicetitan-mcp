import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_patch,
    make_st_delete,
)

__all__ = ["register_pricebook_services_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_pricebook_services_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_services_create(
        tenant: int,
        code: str,
        description: str,
        display_name: Optional[str] = None,
        warranty: Optional[dict[str, Any]] = None,
        categories: Optional[Sequence[int]] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        taxable: Optional[bool] = None,
        account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        hours: Optional[float] = None,
        is_labor: Optional[bool] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        active: Optional[bool] = None,
        cross_sale_group: Optional[str] = None,
        pays_commission: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        external_data: Optional[dict[str, Any]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        service_materials: Optional[Sequence[dict[str, Any]]] = None,
        service_equipment: Optional[Sequence[dict[str, Any]]] = None,
        recommendations: Optional[Sequence[int]] = None,
        upgrades: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new service (Services_Create)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/services"

        body: dict[str, Any] = {
            "code": code,
            "description": description,
        }
        if display_name is not None:
            body["displayName"] = display_name
        if warranty is not None:
            body["warranty"] = warranty
        if categories is not None:
            body["categories"] = list(categories)
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if account is not None:
            body["account"] = account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if hours is not None:
            body["hours"] = float(hours)
        if is_labor is not None:
            body["isLabor"] = bool(is_labor)
        if assets is not None:
            body["assets"] = list(assets)
        if active is not None:
            body["active"] = bool(active)
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if external_data is not None:
            body["externalData"] = external_data
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type
        if service_materials is not None:
            body["serviceMaterials"] = list(service_materials)
        if service_equipment is not None:
            body["serviceEquipment"] = list(service_equipment)
        if recommendations is not None:
            body["recommendations"] = list(recommendations)
        if upgrades is not None:
            body["upgrades"] = list(upgrades)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create service."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_services_get_list(
        tenant: int,
        calculate_prices: bool = False,
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
        """Get list of services (Services_GetList)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/services"

        params: dict[str, Any] = {}
        if calculate_prices:
            params["calculatePrices"] = True
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
            return "Unable to fetch services."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_services_get(
        tenant: int,
        id: int,
        calculate_prices: bool = False,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a service by ID (Services_Get)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/services/{id}"

        params: dict[str, Any] = {}
        if calculate_prices:
            params["calculatePrices"] = True
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch service by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_services_update(
        tenant: int,
        id: int,
        code: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        warranty: Optional[dict[str, Any]] = None,
        categories: Optional[Sequence[int]] = None,
        price: Optional[float] = None,
        member_price: Optional[float] = None,
        add_on_price: Optional[float] = None,
        add_on_member_price: Optional[float] = None,
        taxable: Optional[bool] = None,
        account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        hours: Optional[float] = None,
        is_labor: Optional[bool] = None,
        recommendations: Optional[Sequence[int]] = None,
        upgrades: Optional[Sequence[int]] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        service_materials: Optional[Sequence[dict[str, Any]]] = None,
        service_equipment: Optional[Sequence[dict[str, Any]]] = None,
        active: Optional[bool] = None,
        cross_sale_group: Optional[str] = None,
        pays_commission: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        external_data: Optional[dict[str, Any]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing service (Services_Update)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/services/{id}"

        body: dict[str, Any] = {}
        if code is not None:
            body["code"] = code
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description
        if warranty is not None:
            body["warranty"] = warranty
        if categories is not None:
            body["categories"] = list(categories)
        if price is not None:
            body["price"] = float(price)
        if member_price is not None:
            body["memberPrice"] = float(member_price)
        if add_on_price is not None:
            body["addOnPrice"] = float(add_on_price)
        if add_on_member_price is not None:
            body["addOnMemberPrice"] = float(add_on_member_price)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if account is not None:
            body["account"] = account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if hours is not None:
            body["hours"] = float(hours)
        if is_labor is not None:
            body["isLabor"] = bool(is_labor)
        if recommendations is not None:
            body["recommendations"] = list(recommendations)
        if upgrades is not None:
            body["upgrades"] = list(upgrades)
        if assets is not None:
            body["assets"] = list(assets)
        if service_materials is not None:
            body["serviceMaterials"] = list(service_materials)
        if service_equipment is not None:
            body["serviceEquipment"] = list(service_equipment)
        if active is not None:
            body["active"] = bool(active)
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if external_data is not None:
            body["externalData"] = external_data
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update service."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_services_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a service by ID (Services_Delete)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/services/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete service."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


