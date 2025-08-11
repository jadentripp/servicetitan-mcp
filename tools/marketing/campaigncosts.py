import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_marketing_campaign_costs_tools"]


def register_marketing_campaign_costs_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketing_campaign_costs_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        year: Optional[int] = None,
        month: Optional[int] = None,
        campaign_id: Optional[int] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of campaign costs.

        Mirrors CampaignCosts_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/costs"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if year is not None:
            params["year"] = year
        if month is not None:
            params["month"] = month
        if campaign_id is not None:
            params["campaignId"] = int(campaign_id)
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch campaign costs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_costs_create(
        tenant: int,
        campaign_id: int,
        year: int,
        month: int,
        daily_cost: float,
        environment: str = "production",
    ) -> str:
        """Creates a new campaign cost.

        Mirrors CampaignCosts_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/costs"

        body = {
            "campaignId": int(campaign_id),
            "year": int(year),
            "month": int(month),
            "dailyCost": float(daily_cost),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create campaign cost."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_costs_update(
        tenant: int,
        id: int,
        daily_cost: float,
        environment: str = "production",
    ) -> str:
        """Updates a campaign cost by ID (patch).

        Mirrors CampaignCosts_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/costs/{id}"

        body = {"dailyCost": float(daily_cost)}

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update campaign cost."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaign_costs_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a campaign cost by ID.

        Mirrors CampaignCosts_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/costs/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch campaign cost by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


