import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_put, make_st_delete

__all__ = ["register_crm_contact_methods_tools"]


def register_crm_contact_methods_tools(mcp: Any) -> None:
    """Register CRM Contact Methods tools."""

    @mcp.tool()
    async def crm_contact_methods_get_list(
        tenant: int,
        contact_id: str,
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
        """Gets a paginated list of contact methods for a contact.

        Mirrors ContactMethods_GetContactMethods.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods"

        params: dict[str, Any] = {}
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
            return "Unable to fetch contact methods."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_methods_create(
        tenant: int,
        contact_id: str,
        type: str,
        value: str,
        reference_id: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new contact method.

        Mirrors ContactMethods_CreateContactMethod.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods"

        body: dict[str, Any] = {"type": type, "value": value}
        if reference_id is not None:
            body["referenceId"] = reference_id
        if memo is not None:
            body["memo"] = memo

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create contact method."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_methods_update(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        value: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update a contact method.

        Mirrors ContactMethods_UpdateContactMethod.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}"

        body: dict[str, Any] = {}
        if value is not None:
            body["value"] = value
        if memo is not None:
            body["memo"] = memo

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update contact method."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_methods_upsert(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        type: str,
        value: str,
        reference_id: Optional[str] = None,
        memo: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Replace (upsert) a contact method.

        Mirrors ContactMethods_UpsertContactMethod.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}"

        body: dict[str, Any] = {"type": type, "value": value}
        if reference_id is not None:
            body["referenceId"] = reference_id
        if memo is not None:
            body["memo"] = memo

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to upsert contact method."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_methods_get(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        environment: str = "production",
    ) -> str:
        """Get a contact method by ID.

        Mirrors ContactMethods_GetContactMethod.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch contact method."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_methods_delete(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        environment: str = "production",
    ) -> str:
        """Delete a contact method.

        Mirrors ContactMethods_DeleteContactMethod.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete contact method."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


