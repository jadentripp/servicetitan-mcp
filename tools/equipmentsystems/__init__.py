from typing import Any

from .export import register_equipmentsystems_export_tools
from .installedequipment import register_installed_equipment_tools

__all__ = ["register_equipmentsystems_tools"]


def register_equipmentsystems_tools(mcp: Any) -> None:
    """Register Equipment Systems tools with the MCP server instance."""
    register_equipmentsystems_export_tools(mcp)
    register_installed_equipment_tools(mcp)



