import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_reporting_report_categories_tools"]


def register_reporting_report_categories_tools(mcp: Any) -> None:
    @mcp.tool()
    async def reporting_get_report_categories(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """List categories for existing reports.

        Mirrors ReportCategories_GetCategories.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/reporting/v2/tenant/{tenant}/report-categories"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch report categories."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


