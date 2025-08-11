import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_payroll_payroll_adjustments_tools"]


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


def register_payroll_payroll_adjustments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_payroll_adjustments_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        employee_ids: Optional[str] = None,
        posted_on_or_after: Optional[str] = None,
        posted_on_or_before: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of payroll adjustments.

        Mirrors PayrollAdjustments_GetList.
        - active: one of "True", "Any", "False".
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/payroll-adjustments"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if employee_ids:
            params["employeeIds"] = employee_ids
        if posted_on_or_after:
            params["postedOnOrAfter"] = posted_on_or_after
        if posted_on_or_before:
            params["postedOnOrBefore"] = posted_on_or_before
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
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
            return "Unable to fetch payroll adjustments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payroll_adjustments_create(
        tenant: int,
        employee_type: str,
        employee_id: int,
        posted_on: str,
        amount: Optional[float] = None,
        memo: Optional[str] = None,
        activity_code_id: Optional[int] = None,
        invoice_id: Optional[int] = None,
        hours: Optional[float] = None,
        rate: Optional[float] = None,
        environment: str = "production",
    ) -> str:
        """Creates a new payroll adjustment.

        Mirrors PayrollAdjustments_Create.
        """

        mapped_type = _normalize_enum(employee_type, {"Technician", "Employee"})
        if not mapped_type:
            return "Invalid 'employee_type'. Use one of: Technician, Employee."

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/payroll-adjustments"

        body: dict[str, Any] = {
            "employeeType": mapped_type,
            "employeeId": int(employee_id),
            "postedOn": posted_on,
        }
        if amount is not None:
            body["amount"] = float(amount)
        if memo is not None:
            body["memo"] = memo
        if activity_code_id is not None:
            body["activityCodeId"] = int(activity_code_id)
        if invoice_id is not None:
            body["invoiceId"] = int(invoice_id)
        if hours is not None:
            body["hours"] = float(hours)
        if rate is not None:
            body["rate"] = float(rate)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create payroll adjustment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


