from typing import Any

from .technicianrating import register_customer_interactions_technician_rating_tools

__all__ = ["register_customer_interactions_tools"]


def register_customer_interactions_tools(mcp: Any) -> None:
    """Register Customer Interactions-related tools with the MCP server instance."""
    register_customer_interactions_technician_rating_tools(mcp)



