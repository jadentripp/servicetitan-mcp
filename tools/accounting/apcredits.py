import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_apcredits_tools"]


def register_apcredits_tools(mcp: Any) -> None:
    @mcp.tool()
    async def ap_credits_get_list(
        tenant: int,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of AP credits.

        Args mirror the ServiceTitan API query parameters. `ids` should be a comma-separated
        list of IDs (max 50) if provided.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/ap-credits"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
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
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch AP credits list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def ap_credits_mark_as_exported(
        tenant: int,
        ap_credit_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Mark AP credits as exported.

        Args:
            tenant: Tenant ID
            ap_credit_ids: Sequence of AP Credit IDs to mark as exported
            environment: "production" or "integration"
        """

        if not ap_credit_ids:
            return "No AP credit IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/ap-credits/markasexported"

        body = [{"apCreditId": credit_id} for credit_id in ap_credit_ids]

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark AP credits as exported."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


