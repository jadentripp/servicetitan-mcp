from typing import Any

from .estimates import register_sales_estimates_tools
from .export import register_sales_estimates_export_tools

__all__ = ["register_salesandestimates_tools"]


def register_salesandestimates_tools(mcp: Any) -> None:
    """Register Sales & Estimates related tools with the MCP server instance."""
    register_sales_estimates_tools(mcp)
    register_sales_estimates_export_tools(mcp)



