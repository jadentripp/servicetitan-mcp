import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request

__all__ = ["register_serviceagreements_service_agreements_tools"]


def register_serviceagreements_service_agreements_tools(mcp: Any) -> None:
    @mcp.tool()
    async def service_agreements_get_list(
        tenant: int,
        ids: Optional[str] = None,
        customer_ids: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        status: Optional[str] = None,
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
        """Gets a list of service agreements (ServiceAgreements_GetList)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/service-agreements/v2/tenant/{tenant}/service-agreements"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if customer_ids:
            params["customerIds"] = customer_ids
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if status:
            params["status"] = status
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
            return "Unable to fetch service agreements."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def service_agreements_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a single service agreement by ID (ServiceAgreements_Get)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/service-agreements/v2/tenant/{tenant}/service-agreements/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch the specified service agreement."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


