import json
from typing import Any, Optional

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_patch,
    make_st_put,
    make_st_delete,
)

__all__ = ["register_crm_contacts_tools"]


def register_crm_contacts_tools(mcp: Any) -> None:
    """Register CRM Contacts tools."""

    @mcp.tool()
    async def crm_contacts_get_list(
        tenant: int,
        name: Optional[str] = None,
        title: Optional[str] = None,
        reference_id: Optional[str] = None,
        is_archived: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of contacts.

        Mirrors Contacts_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts"

        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        if title:
            params["title"] = title
        if reference_id:
            params["referenceId"] = reference_id
        if is_archived is not None:
            params["isArchived"] = is_archived
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch contacts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_create(
        tenant: int,
        name: Optional[str] = None,
        title: Optional[str] = None,
        reference_id: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new contact.

        Mirrors Contacts_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if title is not None:
            body["title"] = title
        if reference_id is not None:
            body["referenceId"] = reference_id

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_search_contact_methods(
        tenant: int,
        contact_id: Optional[str] = None,
        reference_id: Optional[str] = None,
        type: Optional[str] = None,
        value: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Search contact methods across contacts.

        Mirrors Contacts_SearchContactMethods.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/contact-methods"

        params: dict[str, Any] = {}
        if contact_id:
            params["contactId"] = contact_id
        if reference_id:
            params["referenceId"] = reference_id
        if type:
            params["type"] = type
        if value:
            params["value"] = value
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to search contact methods."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_get_preference_metadata_list(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Get list of contact preference metadata types.

        Mirrors Contacts_GetPreferenceMetadataList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/preferences"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch contact preference metadata."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_get_by_relationship_id(
        tenant: int,
        relationship_id: int,
        name: Optional[str] = None,
        title: Optional[str] = None,
        reference_id: Optional[str] = None,
        is_archived: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get contacts by relationship ID.

        Mirrors Contacts_GetByRelationshipId.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/relationships/{relationship_id}"

        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        if title:
            params["title"] = title
        if reference_id:
            params["referenceId"] = reference_id
        if is_archived is not None:
            params["isArchived"] = is_archived
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch contacts by relationship id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_get_relationship_list(
        tenant: int,
        contact_id: str,
        related_entity_id: Optional[int] = None,
        type_slug: Optional[str] = None,
        type_name: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a list of contact relationships.

        Mirrors Contacts_GetContactRelationshipList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/relationships"

        params: dict[str, Any] = {}
        if related_entity_id is not None:
            params["relatedEntityId"] = related_entity_id
        if type_slug:
            params["typeSlug"] = type_slug
        if type_name:
            params["typeName"] = type_name
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch contact relationships."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_delete_relationship(
        tenant: int,
        contact_id: str,
        related_entity_id: int,
        type_slug: str,
        environment: str = "production",
    ) -> str:
        """Delete a contact relationship.

        Mirrors Contacts_DeleteContactRelationship.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/relationships/{related_entity_id}/{type_slug}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete contact relationship."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_create_relationship(
        tenant: int,
        contact_id: str,
        related_entity_id: int,
        type_slug: str,
        environment: str = "production",
    ) -> str:
        """Create a contact relationship.

        Mirrors Contacts_CreateContactRelationship.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/relationships/{related_entity_id}/{type_slug}"

        data = await make_st_post(url)
        if not data:
            return "Unable to create contact relationship."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_update(
        tenant: int,
        id: str,
        name: Optional[str] = None,
        title: Optional[str] = None,
        reference_id: Optional[str] = None,
        is_archived: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update a contact (PATCH).

        Mirrors Contacts_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if title is not None:
            body["title"] = title
        if reference_id is not None:
            body["referenceId"] = reference_id
        if is_archived is not None:
            body["isArchived"] = is_archived

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_replace(
        tenant: int,
        id: str,
        name: Optional[str] = None,
        title: Optional[str] = None,
        reference_id: Optional[str] = None,
        is_archived: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Replace a contact (PUT).

        Mirrors Contacts_Replace.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if title is not None:
            body["title"] = title
        if reference_id is not None:
            body["referenceId"] = reference_id
        if is_archived is not None:
            body["isArchived"] = is_archived

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to replace contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_get(
        tenant: int,
        id: str,
        environment: str = "production",
    ) -> str:
        """Get a contact by ID.

        Mirrors Contacts_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contacts_delete(
        tenant: int,
        id: str,
        environment: str = "production",
    ) -> str:
        """Delete a contact by ID.

        Mirrors Contacts_DeleteContact.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete contact."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


