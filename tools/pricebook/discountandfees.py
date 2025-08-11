import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_pricebook_discounts_and_fees_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_pricebook_discounts_and_fees_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_discounts_and_fees_create(
        tenant: int,
        type: str,
        code: str,
        description: str,
        amount_type: str,
        amount: float,
        display_name: Optional[str] = None,
        limit: Optional[float] = None,
        taxable: Optional[bool] = None,
        categories: Optional[Sequence[int]] = None,
        hours: Optional[float] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        account: Optional[str] = None,
        intacct_gl_group_account: Optional[str] = None,
        cross_sale_group: Optional[str] = None,
        active: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        pays_commission: Optional[bool] = None,
        exclude_from_payroll: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a discount or fee in the pricebook.

        Mirrors DiscountAndFees_Create.
        - type: Discount|Fee
        - amount_type: Percentage|Fixed
        """

        mapped_type = _normalize_enum(type, {"Discount", "Fee"})
        if not mapped_type:
            return "Invalid 'type'. Use one of: Discount, Fee."
        mapped_amount_type = _normalize_enum(amount_type, {"Percentage", "Fixed"})
        if not mapped_amount_type:
            return "Invalid 'amount_type'. Use one of: Percentage, Fixed."

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/discounts-and-fees"

        body: dict[str, Any] = {
            "type": mapped_type,
            "code": code,
            "description": description,
            "amountType": mapped_amount_type,
            "amount": float(amount),
        }
        if display_name is not None:
            body["displayName"] = display_name
        if limit is not None:
            body["limit"] = float(limit)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if categories is not None:
            body["categories"] = list(categories)
        if hours is not None:
            body["hours"] = float(hours)
        if assets is not None:
            body["assets"] = list(assets)
        if account is not None:
            body["account"] = account
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if active is not None:
            body["active"] = bool(active)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if exclude_from_payroll is not None:
            body["excludeFromPayroll"] = bool(exclude_from_payroll)
        if external_data is not None:
            body["externalData"] = external_data
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create discount/fee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_discounts_and_fees_get_list(
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
        """Get a paginated list of discounts and fees.

        Mirrors DiscountAndFees_GetList.
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/discounts-and-fees"

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
            return "Unable to fetch discounts and fees."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_discounts_and_fees_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a discount/fee by ID.

        Mirrors DiscountAndFees_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/discounts-and-fees/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch discount/fee by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_discounts_and_fees_update(
        tenant: int,
        id: int,
        type: Optional[str] = None,
        code: Optional[str] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        amount_type: Optional[str] = None,
        amount: Optional[float] = None,
        intacct_gl_group_account: Optional[str] = None,
        limit: Optional[float] = None,
        taxable: Optional[bool] = None,
        categories: Optional[Sequence[int]] = None,
        hours: Optional[float] = None,
        assets: Optional[Sequence[dict[str, Any]]] = None,
        account: Optional[str] = None,
        cross_sale_group: Optional[str] = None,
        active: Optional[bool] = None,
        bonus: Optional[float] = None,
        commission_bonus: Optional[float] = None,
        pays_commission: Optional[bool] = None,
        exclude_from_payroll: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        budget_cost_code: Optional[str] = None,
        budget_cost_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing discount/fee.

        Mirrors DiscountAndFees_Update.
        - type (optional): Discount|Fee
        - amount_type (optional): Percentage|Fixed
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/discounts-and-fees/{id}"

        body: dict[str, Any] = {}
        if type is not None:
            mapped_type = _normalize_enum(type, {"Discount", "Fee"})
            if not mapped_type:
                return "Invalid 'type'. Use one of: Discount, Fee."
            body["type"] = mapped_type
        if code is not None:
            body["code"] = code
        if display_name is not None:
            body["displayName"] = display_name
        if description is not None:
            body["description"] = description
        if amount_type is not None:
            mapped_amount_type = _normalize_enum(amount_type, {"Percentage", "Fixed"})
            if not mapped_amount_type:
                return "Invalid 'amount_type'. Use one of: Percentage, Fixed."
            body["amountType"] = mapped_amount_type
        if amount is not None:
            body["amount"] = float(amount)
        if intacct_gl_group_account is not None:
            body["intacctGlGroupAccount"] = intacct_gl_group_account
        if limit is not None:
            body["limit"] = float(limit)
        if taxable is not None:
            body["taxable"] = bool(taxable)
        if categories is not None:
            body["categories"] = list(categories)
        if hours is not None:
            body["hours"] = float(hours)
        if assets is not None:
            body["assets"] = list(assets)
        if account is not None:
            body["account"] = account
        if cross_sale_group is not None:
            body["crossSaleGroup"] = cross_sale_group
        if active is not None:
            body["active"] = bool(active)
        if bonus is not None:
            body["bonus"] = float(bonus)
        if commission_bonus is not None:
            body["commissionBonus"] = float(commission_bonus)
        if pays_commission is not None:
            body["paysCommission"] = bool(pays_commission)
        if exclude_from_payroll is not None:
            body["excludeFromPayroll"] = bool(exclude_from_payroll)
        if external_data is not None:
            body["externalData"] = external_data
        if budget_cost_code is not None:
            body["budgetCostCode"] = budget_cost_code
        if budget_cost_type is not None:
            body["budgetCostType"] = budget_cost_type

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update discount/fee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_discounts_and_fees_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a discount/fee by ID.

        Mirrors DiscountAndFees_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/discounts-and-fees/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete discount/fee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


