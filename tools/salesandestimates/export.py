import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_sales_estimates_export_tools"]


def register_sales_estimates_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def sales_estimates_export(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for estimates. Mirrors EstimatesExport_Estimates."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/export"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to export estimates."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



