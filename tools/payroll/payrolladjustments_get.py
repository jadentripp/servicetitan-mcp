import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_payroll_adjustments_get_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_payroll_payroll_adjustments_get_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_payroll_adjustments_get(
        tenant: int,
        id: int,
        employee_type: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a payroll adjustment by ID.

        Mirrors PayrollAdjustments_Get.
        """

        params: dict[str, Any] = {}
        if employee_type is not None:
            mapped = _normalize_enum(employee_type, {"Technician", "Employee"})
            if not mapped:
                return "Invalid 'employee_type'. Use one of: Technician, Employee."
            params["employeeType"] = mapped

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/payroll-adjustments/{id}"

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch payroll adjustment by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


