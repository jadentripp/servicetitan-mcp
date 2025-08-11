from typing import Any

from .export import register_payroll_export_tools
from .activitycodes import register_payroll_activity_codes_tools
from .grosspayitems import register_payroll_gross_pay_items_tools
from .jobsplits import register_payroll_job_splits_tools
from .locationlabortype import register_payroll_location_labor_type_tools
from .payrolladjustments import register_payroll_payroll_adjustments_tools
from .payrolladjustments_get import register_payroll_payroll_adjustments_get_tools
from .payrolls import register_payroll_payrolls_tools
from .payrollsettings import register_payroll_payroll_settings_tools
from .timesheetcodes import register_payroll_timesheet_codes_tools
from .timesheets import register_payroll_timesheets_tools

__all__ = ["register_payroll_tools"]


def register_payroll_tools(mcp: Any) -> None:
    """Register Payroll-related tools with the MCP server instance."""
    register_payroll_export_tools(mcp)
    register_payroll_activity_codes_tools(mcp)
    register_payroll_gross_pay_items_tools(mcp)
    register_payroll_job_splits_tools(mcp)
    register_payroll_location_labor_type_tools(mcp)
    register_payroll_payroll_adjustments_tools(mcp)
    register_payroll_payroll_adjustments_get_tools(mcp)
    register_payroll_payrolls_tools(mcp)
    register_payroll_payroll_settings_tools(mcp)
    register_payroll_timesheet_codes_tools(mcp)
    register_payroll_timesheets_tools(mcp)


