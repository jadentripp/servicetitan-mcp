import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_jobplanningandmanagement_project_substatuses_tools"]


def register_jobplanningandmanagement_project_substatuses_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_project_substatuses_get_list(
        tenant: int,
        name: Optional[str] = None,
        status_id: Optional[int] = None,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of project sub statuses. Mirrors ProjectSubStatuses_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-substatuses"

        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        if status_id is not None:
            params["statusId"] = status_id
        if ids:
            params["ids"] = ids
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project sub statuses."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_project_substatuses_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single project sub status by ID. Mirrors ProjectSubStatuses_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-substatuses/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch project sub status by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


