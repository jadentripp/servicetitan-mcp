from typing import Any

from .dynamicvaluesets import register_reporting_dynamic_value_sets_tools
from .reportcategories import register_reporting_report_categories_tools
from .reportcategoryreports import register_reporting_report_category_reports_tools

__all__ = ["register_reporting_tools"]


def register_reporting_tools(mcp: Any) -> None:
    """Register Reporting-related tools with the provided MCP server instance."""
    register_reporting_dynamic_value_sets_tools(mcp)
    register_reporting_report_categories_tools(mcp)
    register_reporting_report_category_reports_tools(mcp)


