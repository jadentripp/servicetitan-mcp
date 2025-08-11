from typing import Any

from .export import register_inventory_export_tools
from .adjustments import register_inventory_adjustments_tools
from .purchaseorders import register_inventory_purchase_orders_tools
from .purchaseordersmarkup import register_inventory_purchase_order_markups_tools
from .purchaseordertypes import register_inventory_purchase_order_types_tools
from .receipts import register_inventory_receipts_tools
from .returns import register_inventory_returns_tools
from .returntypes import register_inventory_return_types_tools
from .transfers import register_inventory_transfers_tools
from .trucks import register_inventory_trucks_tools
from .vendors import register_inventory_vendors_tools
from .warehouses import register_inventory_warehouses_tools

__all__ = ["register_inventory_tools"]


def register_inventory_tools(mcp: Any) -> None:
    """Register Inventory-related tools with the MCP server instance."""
    register_inventory_export_tools(mcp)
    register_inventory_adjustments_tools(mcp)
    register_inventory_purchase_orders_tools(mcp)
    register_inventory_purchase_order_markups_tools(mcp)
    register_inventory_purchase_order_types_tools(mcp)
    register_inventory_receipts_tools(mcp)
    register_inventory_returns_tools(mcp)
    register_inventory_return_types_tools(mcp)
    register_inventory_transfers_tools(mcp)
    register_inventory_trucks_tools(mcp)
    register_inventory_vendors_tools(mcp)
    register_inventory_warehouses_tools(mcp)


