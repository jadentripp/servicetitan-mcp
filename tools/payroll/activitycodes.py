import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_activity_codes_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_payroll_activity_codes_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_activity_codes_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of payroll activity codes.

        Mirrors ActivityCodes_GetList.
        - active: one of "True", "Any", "False"
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/activity-codes"

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
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch payroll activity codes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_activity_codes_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a payroll activity code by ID.

        Mirrors ActivityCodes_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/activity-codes/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch payroll activity code by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


