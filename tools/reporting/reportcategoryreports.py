import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_post, make_st_request

__all__ = ["register_reporting_report_category_reports_tools"]


def register_reporting_report_category_reports_tools(mcp: Any) -> None:
    @mcp.tool()
    async def reporting_get_category_reports(
        tenant: int,
        report_category: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """List reports within the given category.

        Mirrors ReportCategoryReports_GetReports.
        """

        if not report_category:
            return "'report_category' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/reporting/v2/tenant/{tenant}/report-category/{report_category}/reports"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch reports for category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def reporting_get_report_description(
        tenant: int,
        report_category: str,
        report_id: int,
        environment: str = "production",
    ) -> str:
        """Get report description including input parameters and output fields.

        Mirrors ReportCategoryReports_Get.
        """

        if not report_category:
            return "'report_category' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/reporting/v2/tenant/{tenant}/report-category/{report_category}/reports/{report_id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch report description."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def reporting_get_report_data(
        tenant: int,
        report_category: str,
        report_id: int,
        parameters: Optional[Sequence[dict[str, Any]]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get report data for a given report and parameters.

        Mirrors ReportCategoryReports_GetData.
        'parameters' should be a list of objects like {"name": str, "value": Any}.
        """

        if not report_category:
            return "'report_category' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/reporting/v2/tenant/{tenant}/report-category/{report_category}/reports/{report_id}/data"

        params_qs: dict[str, Any] = {}
        if page is not None:
            params_qs["page"] = page
        if page_size is not None:
            params_qs["pageSize"] = page_size
        if include_total:
            params_qs["includeTotal"] = True

        body: dict[str, Any] = {
            "parameters": list(parameters) if parameters else [],
        }

        data = await make_st_post(url, json_body=body, params=params_qs or None)
        if not data:
            return "Unable to fetch report data."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


