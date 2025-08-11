import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_timesheets_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_payroll_timesheets_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_timesheets_get_job_timesheets_by_jobs(
        tenant: int,
        job_ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        technician_id: Optional[int] = None,
        started_on: Optional[str] = None,
        ended_on: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of job timesheets by multiple jobs.

        Mirrors Timesheets_GetJobTimesheetsByJobs.
        - active: True|Any|False
        - sort: e.g. +CreatedOn, -ModifiedOn
        - job_ids: CSV string
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/jobs/timesheets"

        params: dict[str, Any] = {}
        if job_ids:
            params["jobIds"] = job_ids
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
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if technician_id is not None:
            params["technicianId"] = int(technician_id)
        if started_on:
            params["startedOn"] = started_on
        if ended_on:
            params["endedOn"] = ended_on
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job timesheets by jobs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_timesheets_get_job_timesheets(
        tenant: int,
        job: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        active: Optional[str] = None,
        technician_id: Optional[int] = None,
        started_on: Optional[str] = None,
        ended_on: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of job timesheets.

        Mirrors Timesheets_GetJobTimesheets.
        - active: True|Any|False
        - sort: e.g. +CreatedOn, -ModifiedOn
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/jobs/{job}/timesheets"

        params: dict[str, Any] = {}
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
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if technician_id is not None:
            params["technicianId"] = int(technician_id)
        if started_on:
            params["startedOn"] = started_on
        if ended_on:
            params["endedOn"] = ended_on
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job timesheets."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_timesheets_get_non_job_timesheets(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        employee_id: Optional[int] = None,
        employee_type: Optional[str] = None,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a list of non job timesheets for employee.

        Mirrors Timesheets_GetNonJobTimesheets.
        - employee_type: Technician|Employee
        - active: True|Any|False
        - sort: e.g. +CreatedOn, -ModifiedOn
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/non-job-timesheets"

        params: dict[str, Any] = {}
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
        if employee_id is not None:
            params["employeeId"] = int(employee_id)
        if employee_type is not None:
            mapped_type = {"technician": "Technician", "employee": "Employee"}.get(
                employee_type.strip().lower()
            )
            if not mapped_type:
                return "Invalid 'employee_type'. Use one of: Technician, Employee."
            params["employeeType"] = mapped_type
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch non job timesheets."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


