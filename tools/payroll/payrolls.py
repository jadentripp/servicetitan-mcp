import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_payrolls_tools"]


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


def register_payroll_payrolls_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_payrolls_get_employee_payrolls(
        tenant: int,
        employee: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        started_on_or_after: Optional[str] = None,
        ended_on_or_before: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        approved_on_or_after: Optional[str] = None,
        status: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of employee payrolls.

        Mirrors Payrolls_GetEmployeePayrolls.
        - status: Pending|Expired|Approved|Paid|Locked
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/employees/{employee}/payrolls"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if started_on_or_after:
            params["startedOnOrAfter"] = started_on_or_after
        if ended_on_or_before:
            params["endedOnOrBefore"] = ended_on_or_before
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if approved_on_or_after:
            params["approvedOnOrAfter"] = approved_on_or_after
        if status is not None:
            mapped_status = _normalize_enum(
                status, {"Pending", "Expired", "Approved", "Paid", "Locked"}
            )
            if not mapped_status:
                return "Invalid 'status'. Use one of: Pending, Expired, Approved, Paid, Locked."
            params["status"] = mapped_status
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch employee payrolls."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payrolls_get_list(
        tenant: int,
        employee_type: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        started_on_or_after: Optional[str] = None,
        ended_on_or_before: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        approved_on_or_after: Optional[str] = None,
        status: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of payrolls.

        Mirrors Payrolls_GetList.
        - employee_type: Technician|Employee
        - status: Pending|Expired|Approved|Paid|Locked
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/payrolls"

        params: dict[str, Any] = {}
        if employee_type is not None:
            mapped_type = _normalize_enum(employee_type, {"Technician", "Employee"})
            if not mapped_type:
                return "Invalid 'employee_type'. Use one of: Technician, Employee."
            params["employeeType"] = mapped_type
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if started_on_or_after:
            params["startedOnOrAfter"] = started_on_or_after
        if ended_on_or_before:
            params["endedOnOrBefore"] = ended_on_or_before
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if approved_on_or_after:
            params["approvedOnOrAfter"] = approved_on_or_after
        if status is not None:
            mapped_status = _normalize_enum(
                status, {"Pending", "Expired", "Approved", "Paid", "Locked"}
            )
            if not mapped_status:
                return "Invalid 'status'. Use one of: Pending, Expired, Approved, Paid, Locked."
            params["status"] = mapped_status
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch payrolls."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payrolls_get_technician_payrolls(
        tenant: int,
        technician: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        started_on_or_after: Optional[str] = None,
        ended_on_or_before: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        approved_on_or_after: Optional[str] = None,
        status: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of technician payrolls.

        Mirrors Payrolls_GetTechnicianPayrolls.
        - status: Pending|Expired|Approved|Paid|Locked
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/technicians/{technician}/payrolls"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if started_on_or_after:
            params["startedOnOrAfter"] = started_on_or_after
        if ended_on_or_before:
            params["endedOnOrBefore"] = ended_on_or_before
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if approved_on_or_after:
            params["approvedOnOrAfter"] = approved_on_or_after
        if status is not None:
            mapped_status = _normalize_enum(
                status, {"Pending", "Expired", "Approved", "Paid", "Locked"}
            )
            if not mapped_status:
                return "Invalid 'status'. Use one of: Pending, Expired, Approved, Paid, Locked."
            params["status"] = mapped_status
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch technician payrolls."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


