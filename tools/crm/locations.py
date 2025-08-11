import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_crm_locations_tools"]


def register_crm_locations_tools(mcp: Any) -> None:
    """Register CRM Locations tools."""

    @mcp.tool()
    async def crm_locations_get_list(
        tenant: int,
        ids: Optional[str] = None,
        name: Optional[str] = None,
        customer_id: Optional[int] = None,
        street: Optional[str] = None,
        unit: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        country: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        active: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of locations with filters.

        Mirrors Locations_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if name:
            params["name"] = name
        if customer_id is not None:
            params["customerId"] = customer_id
        if street:
            params["street"] = street
        if unit:
            params["unit"] = unit
        if city:
            params["city"] = city
        if state:
            params["state"] = state
        if zip:
            params["zip"] = zip
        if country:
            params["country"] = country
        if latitude is not None:
            params["latitude"] = latitude
        if longitude is not None:
            params["longitude"] = longitude
        if active is not None:
            params["active"] = active
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
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch locations."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_create(
        tenant: int,
        name: str,
        address: dict[str, Any],
        customer_id: int,
        contacts: Optional[Sequence[dict[str, Any]]] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new location.

        Mirrors Locations_Create.
        """

        if not name or not address or not customer_id:
            return "name, address, and customer_id are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations"

        body: dict[str, Any] = {"name": name, "address": address, "customerId": customer_id}
        if contacts is not None:
            body["contacts"] = list(contacts)
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if external_data is not None:
            body["externalData"] = external_data

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create location."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_get_locations_contacts_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        location_ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get contacts across locations filtered by date ranges or IDs.

        Mirrors Locations_GetLocationsContactsList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/contacts"

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
        if location_ids:
            params["locationIds"] = location_ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch locations contacts list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_get_custom_field_types(
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
        """Get location custom field types (paginated).

        Mirrors Locations_GetCustomFieldTypes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/custom-fields"

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
            return "Unable to fetch location custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_update(
        tenant: int,
        id: int,
        customer_id: Optional[int] = None,
        name: Optional[str] = None,
        address: Optional[dict[str, Any]] = None,
        active: Optional[bool] = None,
        tax_zone_id: Optional[int] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update a location (PATCH).

        Mirrors Locations_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}"

        body: dict[str, Any] = {}
        if customer_id is not None:
            body["customerId"] = customer_id
        if name is not None:
            body["name"] = name
        if address is not None:
            body["address"] = address
        if active is not None:
            body["active"] = active
        if tax_zone_id is not None:
            body["taxZoneId"] = tax_zone_id
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if external_data is not None:
            body["externalData"] = external_data

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update location."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a location by ID.

        Mirrors Locations_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch location."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_get_contact_list(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get contacts for a location (paginated).

        Mirrors Locations_GetContactList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/contacts"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch location contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_create_contact(
        tenant: int,
        id: int,
        type: str,
        value: str,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a contact for a location.

        Mirrors Locations_CreateContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/contacts"

        body: dict[str, Any] = {"type": type, "value": value}
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create location contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_update_contact(
        tenant: int,
        id: int,
        contact_id: int,
        type: Optional[str] = None,
        value: Optional[str] = None,
        memo: Optional[str] = None,
        preferences: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update a location contact (PATCH).

        Mirrors Locations_UpdateContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/contacts/{contact_id}"

        body: dict[str, Any] = {}
        if type is not None:
            body["type"] = type
        if value is not None:
            body["value"] = value
        if memo is not None:
            body["memo"] = memo
        if preferences is not None:
            body["preferences"] = preferences

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update location contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_delete_contact(
        tenant: int,
        id: int,
        contact_id: int,
        environment: str = "production",
    ) -> str:
        """Delete a location contact.

        Mirrors Locations_DeleteContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/contacts/{contact_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete location contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_get_notes(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get notes for a location (paginated).

        Mirrors Locations_GetNotes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/notes"

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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch location notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_create_note(
        tenant: int,
        id: int,
        text: str,
        pin_to_top: Optional[bool] = None,
        add_to_customer: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a note on a location.

        Mirrors Locations_CreateNote.
        """

        if not text:
            return "text is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/notes"

        body: dict[str, Any] = {"text": text}
        if pin_to_top is not None:
            body["pinToTop"] = pin_to_top
        if add_to_customer is not None:
            body["addToCustomer"] = add_to_customer

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create location note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_delete_note(
        tenant: int,
        id: int,
        note_id: int,
        environment: str = "production",
    ) -> str:
        """Delete a location note.

        Mirrors Locations_DeleteNote.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/notes/{note_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete location note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_delete_tag(
        tenant: int,
        id: int,
        tag_type_id: int,
        environment: str = "production",
    ) -> str:
        """Remove a tag from a location.

        Mirrors Locations_DeleteTag.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/tags/{tag_type_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete location tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_locations_create_tag(
        tenant: int,
        id: int,
        tag_type_id: int,
        environment: str = "production",
    ) -> str:
        """Add a tag to a location.

        Mirrors Locations_CreateTag.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/locations/{id}/tags/{tag_type_id}"

        data = await make_st_post(url)
        if not data:
            return "Unable to create location tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


