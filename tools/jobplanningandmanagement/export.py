import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_jobplanningandmanagement_export_tools"]


def register_jobplanningandmanagement_export_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_export_appointments(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for appointments.

        Mirrors Export_Appointments.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/appointments"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM appointments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_job_cancel_reasons(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for job canceled logs.

        Mirrors Export_JobCancelReasons.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/job-canceled-logs"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM job canceled logs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_job_history(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for job history.

        Mirrors Export_JobHistory.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/job-history"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM job history."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_job_notes(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for job notes.

        Mirrors Export_JobNotes.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/job-notes"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM job notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_jobs(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for jobs.

        Mirrors Export_Jobs.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/jobs"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM jobs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_project_notes(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for project notes.

        Mirrors Export_ProjectNotes.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/project-notes"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM project notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_export_projects(
        tenant: int,
        from_token: Optional[str] = None,
        include_recent_changes: bool = False,
        environment: str = "production",
    ) -> str:
        """Export feed for projects.

        Mirrors Export_Projects.
        - from_token: continuation token (or date string to start export from a point in time)
        - include_recent_changes: if True, receive recent changes sooner (results may repeat)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/export/projects"

        params: dict[str, Any] = {}
        if from_token:
            params["from"] = from_token
        if include_recent_changes:
            params["includeRecentChanges"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch export feed for JPM projects."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


