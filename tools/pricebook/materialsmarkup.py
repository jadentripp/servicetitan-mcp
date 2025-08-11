import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_put

__all__ = ["register_pricebook_materials_markup_tools"]


def register_pricebook_materials_markup_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_materials_markup_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Get materials markup collection (MaterialsMarkup_GetList)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materialsmarkup"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch materials markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_markup_create(
        tenant: int,
        id: int,
        from_amount: float,
        to_amount: float,
        percent: float,
        environment: str = "production",
    ) -> str:
        """Create materials markup item (MaterialsMarkup_Create)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materialsmarkup"

        body: dict[str, Any] = {
            "id": int(id),
            "from": float(from_amount),
            "to": float(to_amount),
            "percent": float(percent),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create materials markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_markup_update(
        tenant: int,
        id: int,
        from_amount: float,
        to_amount: float,
        percent: float,
        environment: str = "production",
    ) -> str:
        """Update materials markup item (MaterialsMarkup_Update)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materialsmarkup/{id}"

        body: dict[str, Any] = {
            "id": int(id),
            "from": float(from_amount),
            "to": float(to_amount),
            "percent": float(percent),
        }

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update materials markup."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_materials_markup_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get materials markup item by ID (MaterialsMarkup_Get)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/materialsmarkup/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch materials markup by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


