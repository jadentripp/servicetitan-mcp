import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_location_labor_type_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_payroll_location_labor_type_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_location_labor_type_get_list_by_locations(
        tenant: int,
        location_ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of location hourly rates by locations.

        Mirrors LocationLaborType_GetListByLocations.
        - active: one of "True", "Any", "False".
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/locations/rates"

        params: dict[str, Any] = {}
        if location_ids:
            params["locationIds"] = location_ids
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
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch location labor rates by locations."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


