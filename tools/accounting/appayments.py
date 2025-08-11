import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_appayments_tools"]


def register_appayments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def ap_payments_get_list(
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
        """Get a paginated list of AP payments.

        Args mirror the ServiceTitan API query parameters. `ids` should be a comma-separated
        list of IDs (max 50) if provided.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/ap-payments"

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
            return "Unable to fetch AP payments list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def ap_payments_mark_as_exported(
        tenant: int,
        ap_payment_ids: Sequence[int],
        external_ids: Optional[Sequence[str]] = None,
        external_messages: Optional[Sequence[str]] = None,
        environment: str = "production",
    ) -> str:
        """Mark AP payments as exported.

        Args:
            tenant: Tenant ID
            ap_payment_ids: Sequence of AP Payment IDs to mark as exported
            external_ids: Optional sequence of external IDs aligned by index to ap_payment_ids
            external_messages: Optional sequence of external messages aligned by index
            environment: "production" or "integration"
        """

        if not ap_payment_ids:
            return "No AP payment IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/ap-payments/markasexported"

        body = []
        for idx, payment_id in enumerate(ap_payment_ids):
            item: dict[str, Any] = {"apPaymentId": int(payment_id)}
            if external_ids and idx < len(external_ids) and external_ids[idx] is not None:
                item["externalId"] = external_ids[idx]
            if external_messages and idx < len(external_messages) and external_messages[idx] is not None:
                item["externalMessage"] = external_messages[idx]
            body.append(item)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to mark AP payments as exported."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


