from typing import Any

from .export import register_serviceagreements_export_tools
from .serviceagreements import register_serviceagreements_service_agreements_tools

__all__ = ["register_serviceagreements_tools"]


def register_serviceagreements_tools(mcp: Any) -> None:
    """Register Service Agreements tools with the MCP server instance."""
    register_serviceagreements_export_tools(mcp)
    register_serviceagreements_service_agreements_tools(mcp)


