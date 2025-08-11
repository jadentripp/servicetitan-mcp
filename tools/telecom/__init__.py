from typing import Any

from .export import register_telecom_export_tools
from .calls import register_telecom_calls_tools

__all__ = ["register_telecom_tools"]


def register_telecom_tools(mcp: Any) -> None:
    """Register Telecom-related tools with the MCP server instance."""
    register_telecom_export_tools(mcp)
    register_telecom_calls_tools(mcp)



