import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_dispatch_zone_tools"]


def register_dispatch_zone_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_zones(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of zones with filters.

        Mirrors Zone_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, only active returned by default.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/zones"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch zones."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_zone(
        tenant: int,
        name: Optional[str] = None,
        zips: Optional[Sequence[str]] = None,
        cities: Optional[Sequence[str]] = None,
        territory_numbers: Optional[Sequence[str]] = None,
        locn_numbers: Optional[Sequence[str]] = None,
        service_days_enabled: Optional[bool] = None,
        service_days_ids: Optional[Sequence[int]] = None,
        business_units: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new zone.

        Mirrors Zone_CreateZone.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/zones"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if zips is not None:
            body["zips"] = list(zips)
        if cities is not None:
            body["cities"] = list(cities)
        if territory_numbers is not None:
            body["territoryNumbers"] = list(territory_numbers)
        if locn_numbers is not None:
            body["locnNumbers"] = list(locn_numbers)
        if service_days_enabled is not None:
            body["serviceDaysEnabled"] = bool(service_days_enabled)
        if service_days_ids is not None:
            body["serviceDaysIds"] = [int(x) for x in service_days_ids]
        if business_units is not None:
            body["businessUnits"] = [int(x) for x in business_units]

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create zone."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_zone(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a specific zone by ID.

        Mirrors Zone_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/zones/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch zone."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_update_zone(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        zips: Optional[Sequence[str]] = None,
        cities: Optional[Sequence[str]] = None,
        territory_numbers: Optional[Sequence[str]] = None,
        locn_numbers: Optional[Sequence[str]] = None,
        service_days_enabled: Optional[bool] = None,
        service_days_ids: Optional[Sequence[int]] = None,
        business_units: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing zone by ID.

        Mirrors Zone_UpdateZone.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/zones/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if zips is not None:
            body["zips"] = list(zips)
        if cities is not None:
            body["cities"] = list(cities)
        if territory_numbers is not None:
            body["territoryNumbers"] = list(territory_numbers)
        if locn_numbers is not None:
            body["locnNumbers"] = list(locn_numbers)
        if service_days_enabled is not None:
            body["serviceDaysEnabled"] = bool(service_days_enabled)
        if service_days_ids is not None:
            body["serviceDaysIds"] = [int(x) for x in service_days_ids]
        if business_units is not None:
            body["businessUnits"] = [int(x) for x in business_units]

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update zone."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_delete_zone(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a zone by ID.

        Mirrors Zone_DeleteZone.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/zones/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete zone."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


