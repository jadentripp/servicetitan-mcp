import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_patch,
    make_st_delete,
)

__all__ = ["register_crm_bookings_tools"]


def register_crm_bookings_tools(mcp: Any) -> None:
    """Register CRM Booking Provider bookings tools."""

    @mcp.tool()
    async def crm_booking_provider_bookings_get_list(
        tenant: int,
        booking_provider: int,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        external_id: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of bookings for a booking provider.

        Mirrors Bookings_GetList2.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings"

        params: dict[str, Any] = {}
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
        if external_id:
            params["externalId"] = external_id
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch bookings for booking provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_get(
        tenant: int,
        booking_provider: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a booking by ID for a booking provider.

        Mirrors Bookings_GetForProvider.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch booking for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_create(
        tenant: int,
        booking_provider: int,
        source: str,
        name: str,
        summary: str,
        is_first_time_client: bool,
        external_id: str,
        address: Optional[dict[str, Any]] = None,
        contacts: Optional[Sequence[dict[str, Any]]] = None,
        customer_type: Optional[str] = None,
        start: Optional[str] = None,
        campaign_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        priority: Optional[str] = None,
        uploaded_images: Optional[Sequence[str]] = None,
        is_send_confirmation_email: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a booking for a booking provider.

        Mirrors Bookings_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings"

        body: dict[str, Any] = {
            "source": source,
            "name": name,
            "summary": summary,
            "isFirstTimeClient": is_first_time_client,
            "externalId": external_id,
        }
        if address is not None:
            body["address"] = address
        if contacts is not None:
            body["contacts"] = list(contacts)
        if customer_type is not None:
            body["customerType"] = customer_type
        if start is not None:
            body["start"] = start
        if campaign_id is not None:
            body["campaignId"] = campaign_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if job_type_id is not None:
            body["jobTypeId"] = job_type_id
        if priority is not None:
            body["priority"] = priority
        if uploaded_images is not None:
            body["uploadedImages"] = list(uploaded_images)
        if is_send_confirmation_email is not None:
            body["isSendConfirmationEmail"] = is_send_confirmation_email

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create booking for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_update(
        tenant: int,
        booking_provider: int,
        id: int,
        source: Optional[str] = None,
        name: Optional[str] = None,
        address: Optional[dict[str, Any]] = None,
        customer_type: Optional[str] = None,
        start: Optional[str] = None,
        summary: Optional[str] = None,
        campaign_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        priority: Optional[str] = None,
        is_first_time_client: Optional[bool] = None,
        uploaded_images: Optional[Sequence[str]] = None,
        external_id: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update a booking for a booking provider.

        Mirrors Bookings_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}"

        body: dict[str, Any] = {}
        if source is not None:
            body["source"] = source
        if name is not None:
            body["name"] = name
        if address is not None:
            body["address"] = address
        if customer_type is not None:
            body["customerType"] = customer_type
        if start is not None:
            body["start"] = start
        if summary is not None:
            body["summary"] = summary
        if campaign_id is not None:
            body["campaignId"] = campaign_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if job_type_id is not None:
            body["jobTypeId"] = job_type_id
        if priority is not None:
            body["priority"] = priority
        if is_first_time_client is not None:
            body["isFirstTimeClient"] = is_first_time_client
        if uploaded_images is not None:
            body["uploadedImages"] = list(uploaded_images)
        if external_id is not None:
            body["externalId"] = external_id

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update booking for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_get_contacts(
        tenant: int,
        booking_provider: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of contacts for a booking for a booking provider.

        Mirrors Bookings_GetContactList2.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}/contacts"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch booking contacts for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_create_contact(
        tenant: int,
        booking_provider: int,
        id: int,
        type: str,
        value: str,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a contact on the specified booking for a booking provider.

        Mirrors Bookings_CreateContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}/contacts"

        body: dict[str, Any] = {"type": type, "value": value}
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create booking contact for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_update_contact(
        tenant: int,
        booking_provider: int,
        id: int,
        contact_id: int,
        type: Optional[str] = None,
        value: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update a single booking contact for a booking provider.

        Mirrors Bookings_UpdateBookingContact.
        """

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}/contacts/{contact_id}"
        )

        body: dict[str, Any] = {}
        if type is not None:
            body["type"] = type
        if value is not None:
            body["value"] = value
        if memo is not None:
            body["memo"] = memo

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update booking contact for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_booking_provider_bookings_delete_contact(
        tenant: int,
        booking_provider: int,
        id: int,
        contact_id: int,
        environment: str = "production",
    ) -> str:
        """Remove a contact from a booking for a booking provider.

        Mirrors Bookings_DeleteContact.
        """

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/crm/v2/tenant/{tenant}/booking-provider/{booking_provider}/bookings/{id}/contacts/{contact_id}"
        )

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete booking contact for provider."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_bookings_get_list(
        tenant: int,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        external_id: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of bookings (tenant-wide).

        Mirrors Bookings_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/bookings"

        params: dict[str, Any] = {}
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
        if external_id:
            params["externalId"] = external_id
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch bookings."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_bookings_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a booking by ID (tenant-wide).

        Mirrors Bookings_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/bookings/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch booking."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_bookings_get_contacts(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of contacts for a booking (tenant-wide).

        Mirrors Bookings_GetContactList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/bookings/{id}/contacts"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch booking contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


