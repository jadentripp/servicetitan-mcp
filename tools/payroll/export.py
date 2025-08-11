import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_export_tools"]


def register_payroll_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_export_activity_codes(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for payroll activity codes.

        Mirrors Export_ActivityCodes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/activity-codes"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for payroll activity codes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_export_gross_pay_items(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for gross pay items.

        Mirrors Export_GrossPayItems.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/gross-pay-items"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for gross pay items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_export_job_splits(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for job splits.

        Mirrors Export_JobSplits.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/jobs/splits"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for job splits."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_export_timesheets(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for job timesheets.

        Mirrors Export_Timesheets.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/jobs/timesheets"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for timesheets."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_export_payroll_adjustments(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for payroll adjustments.

        Mirrors Export_PayrollAdjustments.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/payroll-adjustments"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for payroll adjustments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_export_timesheet_codes(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for timesheet codes.

        Mirrors Export_TimesheetCodes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/export/timesheet-codes"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for timesheet codes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


