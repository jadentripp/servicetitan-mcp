import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_equipmentsystems_export_tools"]


def register_equipmentsystems_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def equipmentsystems_export_installed_equipment(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for installed equipment.

        Mirrors Export_ExportInstalledEquipment.
        - from_token: continuation token or starting date string (e.g., 2020-01-01)
        - include_recent_changes: if True, recent changes may repeat across requests
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/equipmentsystems/v2/tenant/{tenant}/export/installed-equipment"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for installed equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


