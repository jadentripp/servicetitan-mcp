import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_jobplanningandmanagement_project_types_reference_tools"]


def register_jobplanningandmanagement_project_types_reference_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_project_types_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of project types. Mirrors ProjectTypes_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-types"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_project_types_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a project type by ID. Mirrors ProjectTypes_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/project-types/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch project type by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


