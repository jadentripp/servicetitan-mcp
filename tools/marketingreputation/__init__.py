from typing import Any

from .reviews import register_marketingreputation_reviews_tools

__all__ = ["register_marketingreputation_tools"]


def register_marketingreputation_tools(mcp: Any) -> None:
    """Register Marketing Reputation-related tools with the MCP server instance."""
    register_marketingreputation_reviews_tools(mcp)


