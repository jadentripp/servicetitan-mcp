import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_settings_tag_types_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_settings_tag_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def settings_tag_types_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of tag types. Mirrors TagTypes_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/tag-types"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch tag types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



