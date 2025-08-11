import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_marketing_campaigns_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_marketing_campaigns_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketing_campaigns_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        ids: Optional[str] = None,
        name: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        campaign_phone_number: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of campaigns.

        Mirrors Campaigns_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/campaigns"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if active is not None:
            mapped = _normalize_tristate(active)
            if mapped == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped
        if ids:
            params["ids"] = ids
        if name:
            params["name"] = name
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if campaign_phone_number:
            params["campaignPhoneNumber"] = campaign_phone_number
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch campaigns."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaigns_create(
        tenant: int,
        name: str,
        business_unit_id: int,
        category_id: int,
        active: bool,
        dnis: Optional[str] = None,
        is_default_campaign: Optional[bool] = None,
        source: Optional[str] = None,
        medium: Optional[str] = None,
        other_source: Optional[str] = None,
        other_medium: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Creates a new campaign.

        Mirrors Campaigns_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/campaigns"

        body: dict[str, Any] = {
            "name": name,
            "businessUnitId": int(business_unit_id),
            "categoryId": int(category_id),
            "active": bool(active),
        }
        if dnis is not None:
            body["dnis"] = dnis
        if is_default_campaign is not None:
            body["isDefaultCampaign"] = bool(is_default_campaign)
        if source is not None:
            body["source"] = source
        if medium is not None:
            body["medium"] = medium
        if other_source is not None:
            body["otherSource"] = other_source
        if other_medium is not None:
            body["otherMedium"] = other_medium

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create campaign."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaigns_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        category_id: Optional[int] = None,
        active: Optional[bool] = None,
        dnis: Optional[str] = None,
        is_default_campaign: Optional[bool] = None,
        source: Optional[str] = None,
        medium: Optional[str] = None,
        other_source: Optional[str] = None,
        other_medium: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Updates a campaign by ID (patch).

        Mirrors Campaigns_Update.
        """

        if (
            name is None
            and business_unit_id is None
            and category_id is None
            and active is None
            and dnis is None
            and is_default_campaign is None
            and source is None
            and medium is None
            and other_source is None
            and other_medium is None
        ):
            return "Provide at least one field to update."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/campaigns/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if business_unit_id is not None:
            body["businessUnitId"] = int(business_unit_id)
        if category_id is not None:
            body["categoryId"] = int(category_id)
        if active is not None:
            body["active"] = bool(active)
        if dnis is not None:
            body["dnis"] = dnis
        if is_default_campaign is not None:
            body["isDefaultCampaign"] = bool(is_default_campaign)
        if source is not None:
            body["source"] = source
        if medium is not None:
            body["medium"] = medium
        if other_source is not None:
            body["otherSource"] = other_source
        if other_medium is not None:
            body["otherMedium"] = other_medium

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update campaign."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaigns_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a campaign by ID.

        Mirrors Campaigns_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/campaigns/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch campaign by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_campaigns_get_costs(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        year: Optional[int] = None,
        month: Optional[int] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of campaign costs for a campaign.

        Mirrors Campaigns_GetCosts.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/campaigns/{id}/costs"

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
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch campaign costs for campaign."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


