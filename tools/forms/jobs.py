import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_forms_jobs_tools"]


def register_forms_jobs_tools(mcp: Any) -> None:
    @mcp.tool()
    async def forms_get_job_attachment(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Download a specified job attachment (metadata/redirect).

        Mirrors Jobs_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/forms/v2/tenant/{tenant}/jobs/attachment/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch job attachment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def forms_create_job_attachment(
        tenant: int,
        id: int,
        file: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create an attachment on the specified Job.

        Mirrors Jobs_CreateAttachment. Accepts a 'file' string (binary content or URL depending on API expectations).
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/forms/v2/tenant/{tenant}/jobs/{id}/attachments"

        body = {}
        if file is not None:
            body["file"] = file

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create job attachment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def forms_get_job_attachments(
        tenant: int,
        job_id: int,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get attachments on the specified Job.

        Mirrors Jobs_GetJobAttachments.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/forms/v2/tenant/{tenant}/jobs/{job_id}/attachments"

        params: dict[str, Any] = {}
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if sort:
            params["sort"] = sort
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job attachments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


