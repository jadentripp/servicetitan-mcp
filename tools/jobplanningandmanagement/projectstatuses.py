import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_jobplanningandmanagement_project_statuses_tools"]


def register_jobplanningandmanagement_project_statuses_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_project_statuses_get_list(
        tenant: int,
        name: Optional[str] = None,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of project statuses. Mirrors ProjectStatuses_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-statuses"

        params: dict[str, Any] = {}
        if name:
            params["name"] = name
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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project statuses."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_project_statuses_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single project status by ID. Mirrors ProjectStatuses_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-statuses/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch project status by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


