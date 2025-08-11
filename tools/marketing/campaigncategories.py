import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_marketing_campaign_categories_tools"]


def register_marketing_campaign_categories_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketing_campaign_categories_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of campaign categories.

        Mirrors CampaignCategories_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/categories"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
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
            return "Unable to fetch campaign categories."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_categories_create(
        tenant: int,
        name: str,
        environment: str = "production",
    ) -> str:
        """Creates a new campaign category.

        Mirrors CampaignCategories_Create.
        """

        if not name:
            return "'name' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/categories"

        body = {"name": name}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create campaign category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_categories_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        active: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Updates a campaign category by ID (patch).

        Mirrors CampaignCategories_Update.
        """

        if name is None and active is None:
            return "Provide at least one field to update: name, active."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/categories/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if active is not None:
            body["active"] = bool(active)

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update campaign category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_categories_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a campaign category by ID.

        Mirrors CampaignCategories_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/categories/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch campaign category by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


