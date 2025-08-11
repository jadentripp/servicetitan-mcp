import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_payroll_job_splits_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def register_payroll_job_splits_tools(mcp: Any) -> None:
    @mcp.tool()
    async def payroll_job_splits_get_list_by_jobs(
        tenant: int,
        job_ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of job splits by multiple jobs.

        Mirrors JobSplits_GetListByJobs.
        - active: one of "True", "Any", "False".
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/jobs/splits"

        params: dict[str, Any] = {}
        if job_ids:
            params["jobIds"] = job_ids
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job splits by jobs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def payroll_job_splits_get_list(
        tenant: int,
        job: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        active: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of job splits for a job.

        Mirrors JobSplits_GetList.
        - active: one of "True", "Any", "False".
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/payroll/v2/tenant/{tenant}/jobs/{job}/splits"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job splits."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


