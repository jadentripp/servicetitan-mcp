import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_serviceagreements_export_tools"]


def register_serviceagreements_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def service_agreements_export_service_agreements(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for service agreements (Export_ServiceAgreements)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/service-agreements/v2/tenant/{tenant}/export/service-agreements"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for service agreements."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


