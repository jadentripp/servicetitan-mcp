import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_delete

__all__ = ["register_dispatch_team_tools"]


def register_dispatch_team_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_teams(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        include_inactive: Optional[bool] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of teams with filters.

        Mirrors Team_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/teams"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if include_inactive is not None:
            params["includeInactive"] = bool(include_inactive)
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch teams."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_team(
        tenant: int,
        active: bool,
        name: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new team.

        Mirrors Team_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/teams"

        body: dict[str, Any] = {"active": bool(active)}
        if name is not None:
            body["name"] = name

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create team."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_team(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a specific team by ID.

        Mirrors Team_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/teams/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch team."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_delete_team(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a team by ID.

        Mirrors Team_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/teams/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete team."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


