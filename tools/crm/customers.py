import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_patch,
    make_st_delete,
)

__all__ = ["register_crm_customers_tools"]


def register_crm_customers_tools(mcp: Any) -> None:
    """Register CRM Customers tools."""

    @mcp.tool()
    async def crm_customers_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        exclude_accounting_changes_from_modified_date_range: bool = False,
        name: Optional[str] = None,
        street: Optional[str] = None,
        unit: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        country: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        phone: Optional[str] = None,
        active: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of customers with filters.

        Mirrors Customers_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort
        if ids:
            params["ids"] = ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if exclude_accounting_changes_from_modified_date_range:
            params["excludeAccountingChangesFromModifiedDateRange"] = True
        if name:
            params["name"] = name
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
        if phone:
            params["phone"] = phone
        if active is not None:
            params["active"] = active
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch customers."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_create(
        tenant: int,
        name: str,
        address: dict[str, Any],
        locations: Sequence[dict[str, Any]],
        type: Optional[str] = None,
        do_not_mail: Optional[bool] = None,
        do_not_service: Optional[bool] = None,
        contacts: Optional[Sequence[dict[str, Any]]] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new customer.

        Mirrors Customers_Create.
        """

        if not name or not address or not locations:
            return "name, address, and locations are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers"

        body: dict[str, Any] = {
            "name": name,
            "address": address,
            "locations": list(locations),
        }
        if type is not None:
            body["type"] = type
        if do_not_mail is not None:
            body["doNotMail"] = do_not_mail
        if do_not_service is not None:
            body["doNotService"] = do_not_service
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
            return "Unable to create customer."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_get_modified_contacts_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        customer_ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get modified customer contacts within a date range or by customer IDs.

        Mirrors Customers_GetModifiedContactsList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/contacts"

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
        if customer_ids:
            params["customerIds"] = customer_ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch modified customer contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_get_custom_field_types(
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
        """Get customer custom field types (paginated).

        Mirrors Customers_GetCustomFieldTypes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/custom-fields"

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
            return "Unable to fetch customer custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        type: Optional[str] = None,
        address: Optional[dict[str, Any]] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        external_data: Optional[dict[str, Any]] = None,
        do_not_mail: Optional[bool] = None,
        do_not_service: Optional[bool] = None,
        active: Optional[bool] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Update a customer (PATCH).

        Mirrors Customers_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if type is not None:
            body["type"] = type
        if address is not None:
            body["address"] = address
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if external_data is not None:
            body["externalData"] = external_data
        if do_not_mail is not None:
            body["doNotMail"] = do_not_mail
        if do_not_service is not None:
            body["doNotService"] = do_not_service
        if active is not None:
            body["active"] = active
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update customer."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a customer by ID.

        Mirrors Customers_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch customer."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_get_contact_list(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get contacts for a customer (paginated).

        Mirrors Customers_GetContactList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/contacts"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch customer contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_create_contact(
        tenant: int,
        id: int,
        type: str,
        value: str,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a contact for a customer.

        Mirrors Customers_CreateContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/contacts"

        body: dict[str, Any] = {"type": type, "value": value}
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create customer contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_update_contact(
        tenant: int,
        id: int,
        contact_id: int,
        type: Optional[str] = None,
        value: Optional[str] = None,
        memo: Optional[str] = None,
        preferences: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update a customer contact (PATCH).

        Mirrors Customers_UpdateContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/contacts/{contact_id}"

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
            return "Unable to update customer contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_delete_contact(
        tenant: int,
        id: int,
        contact_id: int,
        environment: str = "production",
    ) -> str:
        """Delete a customer contact.

        Mirrors Customers_DeleteContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/contacts/{contact_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete customer contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_get_notes(
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
        """Get notes for a customer (paginated).

        Mirrors Customers_GetNotes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/notes"

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
            return "Unable to fetch customer notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_create_note(
        tenant: int,
        id: int,
        text: str,
        pin_to_top: Optional[bool] = None,
        add_to_locations: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a new note for a customer.

        Mirrors Customers_CreateNote.
        """

        if not text:
            return "text is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/notes"

        body: dict[str, Any] = {"text": text}
        if pin_to_top is not None:
            body["pinToTop"] = pin_to_top
        if add_to_locations is not None:
            body["addToLocations"] = add_to_locations

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create customer note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_delete_note(
        tenant: int,
        id: int,
        note_id: int,
        environment: str = "production",
    ) -> str:
        """Delete a customer note.

        Mirrors Customers_DeleteNote.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/notes/{note_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete customer note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_delete_tag(
        tenant: int,
        id: int,
        tag_type_id: int,
        environment: str = "production",
    ) -> str:
        """Remove a tag from a customer.

        Mirrors Customers_DeleteTag.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/tags/{tag_type_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete customer tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_customers_create_tag(
        tenant: int,
        id: int,
        tag_type_id: int,
        environment: str = "production",
    ) -> str:
        """Add a tag to a customer.

        Mirrors Customers_CreateTag.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/customers/{id}/tags/{tag_type_id}"

        data = await make_st_post(url)
        if not data:
            return "Unable to create customer tag."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


