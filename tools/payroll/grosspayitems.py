import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_payroll_gross_pay_items_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_payroll_gross_pay_items_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_gross_pay_items_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        employee_type: Optional[str] = None,
        employee_id: Optional[int] = None,
        payroll_ids: Optional[str] = None,
        date_on_or_after: Optional[str] = None,
        date_on_or_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_on_or_before: Optional[str] = None,
        modified_before: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of gross pay items.

        Mirrors GrossPayItems_GetList.
        - employee_type: Technician | Employee
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/gross-pay-items"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if employee_type is not None:
            mapped = _normalize_enum(employee_type, {"Technician", "Employee"})
            if not mapped:
                return "Invalid 'employee_type'. Use one of: Technician, Employee."
            params["employeeType"] = mapped
        if employee_id is not None:
            params["employeeId"] = int(employee_id)
        if payroll_ids:
            params["payrollIds"] = payroll_ids
        if date_on_or_after:
            params["dateOnOrAfter"] = date_on_or_after
        if date_on_or_before:
            params["dateOnOrBefore"] = date_on_or_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_on_or_before:
            params["modifiedOnOrBefore"] = modified_on_or_before
        if modified_before:
            params["modifiedBefore"] = modified_before
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch gross pay items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_gross_pay_items_create(
        tenant: int,
        payroll_id: int,
        amount: float,
        activity_code_id: int,
        date: str,
        invoice_id: Optional[int] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Creates a new gross pay item.

        Mirrors GrossPayItems_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/gross-pay-items"

        body: dict[str, Any] = {
            "payrollId": int(payroll_id),
            "amount": float(amount),
            "activityCodeId": int(activity_code_id),
            "date": date,
        }
        if invoice_id is not None:
            body["invoiceId"] = int(invoice_id)
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create gross pay item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_gross_pay_items_update(
        tenant: int,
        id: int,
        payroll_id: int,
        amount: float,
        activity_code_id: int,
        date: str,
        invoice_id: Optional[int] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Updates a gross pay item by ID.

        Mirrors GrossPayItems_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/gross-pay-items/{id}"

        body: dict[str, Any] = {
            "payrollId": int(payroll_id),
            "amount": float(amount),
            "activityCodeId": int(activity_code_id),
            "date": date,
        }
        if invoice_id is not None:
            body["invoiceId"] = int(invoice_id)
        if memo is not None:
            body["memo"] = memo

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update gross pay item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_gross_pay_items_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Deletes a gross pay item by ID.

        Mirrors GrossPayItems_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/gross-pay-items/{id}"

        data = await make_st_delete(url)
        if not data:
            return "Unable to delete gross pay item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


