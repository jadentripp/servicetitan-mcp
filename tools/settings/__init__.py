from typing import Any

from .export import register_settings_export_tools
from .businessunits import register_settings_business_units_tools
from .employees import register_settings_employees_tools
from .technicians import register_settings_technicians_tools
from .tagtypes import register_settings_tag_types_tools
from .userroles import register_settings_user_roles_tools

__all__ = ["register_settings_tools"]


def register_settings_tools(mcp: Any) -> None:
    """Register Settings-related tools with the MCP server instance."""
    register_settings_export_tools(mcp)
    register_settings_business_units_tools(mcp)
    register_settings_employees_tools(mcp)
    register_settings_technicians_tools(mcp)
    register_settings_tag_types_tools(mcp)
    register_settings_user_roles_tools(mcp)



