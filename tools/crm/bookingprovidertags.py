import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_crm_booking_provider_tags_tools"]


def register_crm_booking_provider_tags_tools(mcp: Any) -> None:
    """Register CRM Booking Provider Tags tools."""

    @mcp.tool()
    async def crm_booking_provider_tags_get_list(
        tenant: int,
        name: Optional[str] = None,
        ids: Optional[str] = None,
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
        """Gets a paginated list of booking provider tags.

        Mirrors BookingProviderTags_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider-tags"

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
            return "Unable to fetch booking provider tags."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_tags_create(
        tenant: int,
        tag_name: str,
        description: str,
        environment: str = "production",
    ) -> str:
        """Create a booking provider tag.

        Mirrors BookingProviderTags_Create.
        """

        if not tag_name or not description:
            return "Both tag_name and description are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider-tags"

        body = {
            "tagName": tag_name,
            "description": description,
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create booking provider tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_tags_update(
        tenant: int,
        id: int,
        tag_name: Optional[str] = None,
        description: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update a booking provider tag by ID.

        Mirrors BookingProviderTags_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider-tags/{id}"

        body: dict[str, Any] = {}
        if tag_name is not None:
            body["tagName"] = tag_name
        if description is not None:
            body["description"] = description

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update booking provider tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_tags_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single booking provider tag by ID.

        Mirrors BookingProviderTags_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider-tags/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch booking provider tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


