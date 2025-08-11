import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_patch

__all__ = ["register_pricebook_client_specific_pricing_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_pricebook_client_specific_pricing_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_client_specific_pricing_get_all_rate_sheets(
        tenant: int,
        ids: Optional[str] = None,
        search_term: Optional[str] = None,
        active: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get all client-specific pricing rate sheets.

        Mirrors ClientSpecificPricing_GetAllRateSheets.
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/clientspecificpricing"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if search_term:
            params["searchTerm"] = search_term
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch client-specific pricing rate sheets."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_client_specific_pricing_update_rate_sheet(
        tenant: int,
        rate_sheet_id: int,
        exceptions: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Update a client-specific pricing rate sheet.

        Mirrors ClientSpecificPricing_UpdateRateSheet.
        - exceptions: list of { skuId: int, value: number, valueType: one of Percent|Dollar|Multiplier|FlatPrice|DiscountPercent }
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/clientspecificpricing/{rate_sheet_id}"

        body: dict[str, Any] = {}
        if exceptions is not None:
            body["exceptions"] = list(exceptions)

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update client-specific pricing rate sheet."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


