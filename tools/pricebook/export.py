import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_pricebook_export_tools"]


def register_pricebook_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_export_categories(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for pricebook categories.

        Mirrors Export_Categories.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/export/categories"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for pricebook categories."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_export_equipment(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for pricebook equipment.

        Mirrors Export_Equipment.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/export/equipment"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for pricebook equipment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_export_materials(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for pricebook materials.

        Mirrors Export_Materials.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/export/materials"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for pricebook materials."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_export_services(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for pricebook services.

        Mirrors Export_Services.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/export/services"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for pricebook services."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


