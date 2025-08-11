import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_put

__all__ = ["register_payroll_payroll_settings_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_payroll_payroll_settings_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_payroll_settings_update_employee(
        tenant: int,
        employee: int,
        hourly_rate: float,
        external_payroll_id: Optional[str] = None,
        manager_id: Optional[int] = None,
        hire_date: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Updates the employee payroll settings.

        Mirrors PayrollSettings_UpdateEmployeePayrollSettings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/employees/{employee}/payroll-settings"

        body: dict[str, Any] = {
            "hourlyRate": float(hourly_rate),
        }
        if external_payroll_id is not None:
            body["externalPayrollId"] = external_payroll_id
        if manager_id is not None:
            body["managerId"] = int(manager_id)
        if hire_date is not None:
            body["hireDate"] = hire_date

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update employee payroll settings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payroll_settings_get_employee(
        tenant: int,
        employee: int,
        environment: str = "production",
    ) -> str:
        """Gets the employee payroll settings.

        Mirrors PayrollSettings_GetEmployeePayrollSettings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/employees/{employee}/payroll-settings"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch employee payroll settings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payroll_settings_get_list(
        tenant: int,
        employee_type: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets the payroll settings list.

        Mirrors PayrollSettings_GetPayrollSettingsList.
        - employee_type: Technician|Employee
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/payroll-settings"

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
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if active is not None:
            normalized_active = str(active).strip().lower()
            if normalized_active in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized_active]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch payroll settings list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payroll_settings_update_technician(
        tenant: int,
        technician: int,
        hourly_rate: float,
        external_payroll_id: Optional[str] = None,
        manager_id: Optional[int] = None,
        hire_date: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Updates the technician payroll settings.

        Mirrors PayrollSettings_UpdateTechnicianPayrollSettings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/technicians/{technician}/payroll-settings"

        body: dict[str, Any] = {
            "hourlyRate": float(hourly_rate),
        }
        if external_payroll_id is not None:
            body["externalPayrollId"] = external_payroll_id
        if manager_id is not None:
            body["managerId"] = int(manager_id)
        if hire_date is not None:
            body["hireDate"] = hire_date

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update technician payroll settings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_payroll_settings_get_technician(
        tenant: int,
        technician: int,
        environment: str = "production",
    ) -> str:
        """Gets the technician payroll settings.

        Mirrors PayrollSettings_GetTechnicianPayrollSettings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/technicians/{technician}/payroll-settings"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch technician payroll settings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


