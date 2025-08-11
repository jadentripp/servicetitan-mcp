import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_marketingads_performance_tools"]


def _normalize_segmentation(value: Optional[str]) -> str | None:
    if value is None:
        return None
    mapping = {
        "campaign": "Campaign",
        "adgroup": "AdGroup",
        "ad_group": "AdGroup",
        "keyword": "Keyword",
    }
    key = str(value).strip().lower().replace(" ", "")
    return mapping.get(key)


def register_marketingads_performance_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingads_performance_get(
        tenant: int,
        from_utc: str,
        to_utc: str,
        performance_segmentation_type: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Returns performance data.

        Mirrors Performance_Get.
        """

        if not from_utc or not to_utc:
            return "'from_utc' and 'to_utc' are required."

        normalized = _normalize_segmentation(performance_segmentation_type)
        if not normalized:
            return "Invalid 'performance_segmentation_type'. Use one of: Campaign, AdGroup, Keyword."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingads/v2/tenant/{tenant}/performance"

        params: dict[str, Any] = {
            "fromUtc": from_utc,
            "toUtc": to_utc,
            "performanceSegmentationType": normalized,
        }
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch performance data."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


