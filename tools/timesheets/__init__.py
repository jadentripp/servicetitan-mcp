from typing import Any

from .export import register_timesheets_export_tools
from .activities import register_timesheets_activities_tools
from .activitycategories import register_timesheets_activity_categories_tools
from .activitytypes import register_timesheets_activity_types_tools

__all__ = ["register_timesheets_tools"]


def register_timesheets_tools(mcp: Any) -> None:
    """Register Timesheets tools with the MCP server instance."""
    register_timesheets_export_tools(mcp)
    register_timesheets_activities_tools(mcp)
    register_timesheets_activity_categories_tools(mcp)
    register_timesheets_activity_types_tools(mcp)


