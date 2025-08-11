from typing import Any

from .router import register_schedulingpro_router_tools
from .scheduler import register_schedulingpro_scheduler_tools

__all__ = ["register_schedulingpro_tools"]


def register_schedulingpro_tools(mcp: Any) -> None:
    """Register SchedulingPro-related tools with the provided MCP server instance."""
    register_schedulingpro_router_tools(mcp)
    register_schedulingpro_scheduler_tools(mcp)


