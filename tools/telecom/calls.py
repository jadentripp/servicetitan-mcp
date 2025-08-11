import base64
import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_put, make_st_get_bytes

__all__ = ["register_telecom_calls_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_telecom_calls_tools(mcp: Any) -> None:
    @mcp.tool()
    async def telecom_calls_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        created_after: Optional[str] = None,
        modified_after: Optional[str] = None,
        campaign_id: Optional[int] = None,
        agent_id: Optional[int] = None,
        min_duration: Optional[int] = None,
        phone_number_called: Optional[str] = None,
        caller_phone_number: Optional[str] = None,
        agent_name: Optional[str] = None,
        agent_is_external: Optional[bool] = None,
        agent_external_id: Optional[int] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of telecom calls (v3). Mirrors Calls_Calls."""

        base_url = get_base_url(environment)
        url = f"{base_url}/telecom/v3/tenant/{tenant}/calls"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if ids:
            params["ids"] = ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
        if created_after:
            params["createdAfter"] = created_after
        if modified_after:
            params["modifiedAfter"] = modified_after
        if campaign_id is not None:
            params["campaignId"] = campaign_id
        if agent_id is not None:
            params["agentId"] = agent_id
        if min_duration is not None:
            params["minDuration"] = min_duration
        if phone_number_called:
            params["phoneNumberCalled"] = phone_number_called
        if caller_phone_number:
            params["callerPhoneNumber"] = caller_phone_number
        if agent_name:
            params["agentName"] = agent_name
        if agent_is_external is not None:
            params["agentIsExternal"] = agent_is_external
        if agent_external_id is not None:
            params["agentExternalId"] = agent_external_id
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch telecom calls."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def telecom_calls_update(
        tenant: int,
        id: int,
        call_type: Optional[str] = None,
        excuse_memo: Optional[str] = None,
        campaign_id: Optional[int] = None,
        job_id: Optional[int] = None,
        agent_id: Optional[int] = None,
        reason: Optional[dict[str, Any]] = None,
        customer: Optional[dict[str, Any]] = None,
        location: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update existing call (v2). Mirrors Calls_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/telecom/v2/tenant/{tenant}/calls/{id}"

        body: dict[str, Any] = {}
        if call_type is not None:
            body["callType"] = call_type
        if excuse_memo is not None:
            body["excuseMemo"] = excuse_memo
        if campaign_id is not None:
            body["campaignId"] = campaign_id
        if job_id is not None:
            body["jobId"] = job_id
        if agent_id is not None:
            body["agentId"] = agent_id
        if reason is not None:
            body["reason"] = dict(reason)
        if customer is not None:
            body["customer"] = dict(customer)
        if location is not None:
            body["location"] = dict(location)

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update telecom call."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def telecom_calls_get_details(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get call details (v2). Mirrors Calls_GetDetails."""

        base_url = get_base_url(environment)
        url = f"{base_url}/telecom/v2/tenant/{tenant}/calls/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch telecom call details."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def telecom_calls_get_recording(
        tenant: int,
        id: int,
        as_base64: bool = True,
        environment: str = "production",
    ) -> str:
        """Get call recording bytes; returns base64 string by default."""

        base_url = get_base_url(environment)
        url = f"{base_url}/telecom/v2/tenant/{tenant}/calls/{id}/recording"

        content = await make_st_get_bytes(url)
        if content is None:
            return "Unable to fetch call recording."

        if as_base64:
            return base64.b64encode(content).decode("ascii")
        # Return a short JSON wrapper with length to avoid raw binary in UI
        return json.dumps({"bytes": len(content)}, indent=2)

    @mcp.tool()
    async def telecom_calls_get_voicemail(
        tenant: int,
        id: int,
        as_base64: bool = True,
        environment: str = "production",
    ) -> str:
        """Get call voicemail bytes; returns base64 string by default."""

        base_url = get_base_url(environment)
        url = f"{base_url}/telecom/v2/tenant/{tenant}/calls/{id}/voicemail"

        content = await make_st_get_bytes(url)
        if content is None:
            return "Unable to fetch call voicemail."

        if as_base64:
            return base64.b64encode(content).decode("ascii")
        return json.dumps({"bytes": len(content)}, indent=2)



