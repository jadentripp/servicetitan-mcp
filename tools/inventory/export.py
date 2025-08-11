import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_inventory_export_tools"]


def register_inventory_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_export_adjustments(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for inventory adjustments.

        Mirrors Export_Adjustments.
        - from_token: continuation token or starting date string (e.g., 2020-01-01)
        - include_recent_changes: if True, recent changes may repeat across requests
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/export/adjustments"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for Inventory adjustments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_export_purchase_orders(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for purchase orders.

        Mirrors Export_PurchaseOrders.
        - from_token: continuation token or starting date string (e.g., 2020-01-01)
        - include_recent_changes: if True, recent changes may repeat across requests
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/export/purchase-orders"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for Inventory purchase orders."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_export_returns(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for returns.

        Mirrors Export_Returns.
        - from_token: continuation token or starting date string (e.g., 2020-01-01)
        - include_recent_changes: if True, recent changes may repeat across requests
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/export/returns"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for Inventory returns."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_export_transfers(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for transfers.

        Mirrors Export_Transfers.
        - from_token: continuation token or starting date string (e.g., 2020-01-01)
        - include_recent_changes: if True, recent changes may repeat across requests
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/export/transfers"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for Inventory transfers."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


