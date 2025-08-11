from typing import Any

from .callreasons import register_jobbooking_call_reasons_tools

__all__ = ["register_jobbooking_tools"]


def register_jobbooking_tools(mcp: Any) -> None:
    """Register JobBooking-related tools with the MCP server instance."""
    register_jobbooking_call_reasons_tools(mcp)


