from typing import Any

from .clientsidedata import register_taskmanagement_client_side_data_tools
from .tasks import register_taskmanagement_tasks_tools

__all__ = ["register_taskmanagement_tools"]


def register_taskmanagement_tools(mcp: Any) -> None:
    """Register Task Management tools with the MCP server instance."""
    register_taskmanagement_client_side_data_tools(mcp)
    register_taskmanagement_tasks_tools(mcp)


