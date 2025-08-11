import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_marketingads_attributed_leads_tools"]


def _normalize_lead_type(value: Optional[str]) -> str | None:
    if value is None:
        return None
    mapping = {
        "call": "Call",
        "webbooking": "WebBooking",
        "web_lead_form": "WebLeadForm",
        "webleadform": "WebLeadForm",
        "manualjob": "ManualJob",
        "manual_job": "ManualJob",
    }
    key = str(value).strip().lower().replace(" ", "")
    return mapping.get(key)


def register_marketingads_attributed_leads_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingads_attributed_leads_get(
        tenant: int,
        from_utc: str,
        to_utc: str,
        lead_type: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Returns attributed leads data.

        Mirrors AttributedLeads_Get.
        """

        if not from_utc or not to_utc:
            return "'from_utc' and 'to_utc' are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingads/v2/tenant/{tenant}/attributed-leads"

        params: dict[str, Any] = {
            "fromUtc": from_utc,
            "toUtc": to_utc,
        }
        if lead_type is not None:
            normalized = _normalize_lead_type(lead_type)
            if not normalized:
                return "Invalid 'lead_type'. Use one of: Call, WebBooking, WebLeadForm, ManualJob."
            params["leadType"] = normalized
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch attributed leads."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


