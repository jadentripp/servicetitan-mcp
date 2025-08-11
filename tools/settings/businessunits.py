import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_put

__all__ = ["register_settings_business_units_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_settings_business_units_tools(mcp: Any) -> None:
    @mcp.tool()
    async def settings_business_units_get_list(
        tenant: int,
        ids: Optional[str] = None,
        name: Optional[str] = None,
        active: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of business units. Mirrors BusinessUnits_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/business-units"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if name:
            params["name"] = name
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
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
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch business units."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_business_units_update(
        tenant: int,
        id: int,
        external_data_patch_mode: Optional[str] = None,  # Replace or Merge
        external_data_application_guid: Optional[str] = None,
        external_data: Optional[list[dict[str, Optional[str]]]] = None,
        environment: str = "production",
    ) -> str:
        """Update BusinessUnit external data. Mirrors BusinessUnits_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/business-units/{id}"

        body: dict[str, Any] = {}
        if (
            external_data_patch_mode is not None
            or external_data_application_guid is not None
            or external_data is not None
        ):
            ext: dict[str, Any] = {}
            if external_data_patch_mode is not None:
                ext["patchMode"] = external_data_patch_mode
            if external_data_application_guid is not None:
                ext["applicationGuid"] = external_data_application_guid
            if external_data is not None:
                ext["externalData"] = [
                    {"key": item.get("key"), **({"value": item.get("value")} if item.get("value") is not None else {})}
                    for item in external_data
                    if item.get("key") is not None
                ]
            body["externalData"] = ext

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update business unit."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_business_units_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a single business unit by ID. Mirrors BusinessUnits_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/business-units/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch business unit."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



