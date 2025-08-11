from typing import Any

from .campaigncategories import register_marketing_campaign_categories_tools
from .campaigncosts import register_marketing_campaign_costs_tools
from .campaigns import register_marketing_campaigns_tools
from .suppressions import register_marketing_suppressions_tools

__all__ = ["register_marketing_tools"]


def register_marketing_tools(mcp: Any) -> None:
    """Register Marketing-related tools with the MCP server instance."""
    register_marketing_campaign_categories_tools(mcp)
    register_marketing_campaign_costs_tools(mcp)
    register_marketing_campaigns_tools(mcp)
    register_marketing_suppressions_tools(mcp)


