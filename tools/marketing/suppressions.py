import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_marketing_suppressions_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def _normalize_suppression_type(reason: Optional[str]) -> str | None:
    if reason is None:
        return None
    mapping = {
        "unsubscribe": "Unsubscribe",
        "bounce": "Bounce",
        "spamreport": "SpamReport",
        "spam_report": "SpamReport",
        "manualunsubscribe": "ManualUnsubscribe",
        "manual_unsubscribe": "ManualUnsubscribe",
        "neveremail": "NeverEmail",
        "never_email": "NeverEmail",
    }
    key = str(reason).strip().lower().replace(" ", "")
    return mapping.get(key)


def register_marketing_suppressions_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketing_suppressions_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        ids: Optional[str] = None,
        email: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of suppressions.

        Mirrors Suppressions_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/suppressions"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if active is not None:
            mapped = _normalize_tristate(active)
            if mapped == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if ids:
            params["ids"] = ids
        if email:
            params["email"] = email
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch suppressions."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_suppressions_add(
        tenant: int,
        emails: Sequence[str],
        reason: str,
        environment: str = "production",
    ) -> str:
        """Add emails to the suppression list.

        Mirrors Suppressions_Add.
        """

        if not emails:
            return "No emails provided."
        if len(emails) > 1000:
            return "Maximum 1000 emails allowed per request."

        normalized_reason = _normalize_suppression_type(reason)
        if not normalized_reason:
            return "Invalid 'reason'. Use one of: Unsubscribe, Bounce, SpamReport, ManualUnsubscribe, NeverEmail."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/suppressions/suppress"

        body = {"emails": list(emails), "reason": normalized_reason}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to add suppressions."

        # 200 returns empty body; our helper returns {"status": 200} if empty
        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_suppressions_remove(
        tenant: int,
        emails: Sequence[str],
        environment: str = "production",
    ) -> str:
        """Remove emails from the suppression list.

        Mirrors Suppressions_Remove.
        """

        if not emails:
            return "No emails provided."
        if len(emails) > 1000:
            return "Maximum 1000 emails allowed per request."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketing/v2/tenant/{tenant}/suppressions/unsuppress"

        body = {"emails": list(emails)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to remove suppressions."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def marketing_suppressions_get(
        tenant: int,
        email: str,
        environment: str = "production",
    ) -> str:
        """Gets suppression record by email.

        Mirrors Suppressions_Get.
        """

        base_url = get_base_url(environment)
        # Email lives in the path; do not encode here, rely on httpx to encode path? We keep it literal per other modules
        url = f"{base_url}/marketing/v2/tenant/{tenant}/suppressions/{email}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch suppression by email."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


