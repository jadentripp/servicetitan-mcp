import json
from typing import Any

from ..utils import get_base_url, make_st_request, make_st_patch

__all__ = ["register_crm_contact_preferences_tools"]


def register_crm_contact_preferences_tools(mcp: Any) -> None:
    """Register CRM Contact Preferences tools."""

    @mcp.tool()
    async def crm_contact_preferences_get_list(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        environment: str = "production",
    ) -> str:
        """Get list of contact preferences for a contact method.

        Mirrors ContactPreferences_GetContactMethodPreferences.
        """

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}/preferences"
        )

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch contact method preferences."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_preferences_update(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        preference_name: str,
        value: str | None = None,
        environment: str = "production",
    ) -> str:
        """Update a single contact preference by name.

        Mirrors ContactPreferences_UpdateContactMethodPreference.
        """

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}/preferences/{preference_name}"
        )

        body: dict[str, Any] = {}
        if value is not None:
            body["value"] = value

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update contact method preference." 

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_contact_preferences_get(
        tenant: int,
        contact_id: str,
        contact_method_id: str,
        preference_name: str,
        environment: str = "production",
    ) -> str:
        """Get a single contact preference by name.

        Mirrors ContactPreferences_GetContactMethodPreference.
        """

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/crm/v2/tenant/{tenant}/contacts/{contact_id}/contact-methods/{contact_method_id}/preferences/{preference_name}"
        )

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch contact method preference."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


