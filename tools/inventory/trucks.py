import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_patch

__all__ = ["register_inventory_trucks_tools"]


def register_inventory_trucks_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_trucks_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
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
        """Get a paginated list of trucks with filters. Mirrors Trucks_GetList.

        - active: one of "True", "Any", "False" (case-insensitive).
        - CSV filters (ids) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/trucks"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values
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
            return "Unable to fetch trucks."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_trucks_update(
        tenant: int,
        id: int,
        external_data_patch_mode: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update a truck's external data. Mirrors Trucks_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/trucks/{id}"

        body: dict[str, Any] = {}
        external_data: dict[str, Any] = {}

        if external_data_patch_mode is not None:
            mode_norm = str(external_data_patch_mode).strip().lower()
            if mode_norm in {"replace", "merge"}:
                external_data["patchMode"] = {"replace": "Replace", "merge": "Merge"}[mode_norm]
            else:
                return "Invalid 'external_data_patch_mode'. Use one of: Replace, Merge."

        if external_data_application_guid is not None:
            external_data["applicationGuid"] = external_data_application_guid
        if external_data_items is not None:
            external_data["externalData"] = list(external_data_items)
        if external_data:
            body["externalData"] = external_data

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update truck."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


