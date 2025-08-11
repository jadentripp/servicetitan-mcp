import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_jobplanningandmanagement_projects_tools"]


def register_jobplanningandmanagement_projects_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_projects_get_list(
        tenant: int,
        ids: Optional[str] = None,
        customer_id: Optional[int] = None,
        location_id: Optional[int] = None,
        project_type_id: Optional[int] = None,
        invoice_id: Optional[int] = None,
        technician_id: Optional[int] = None,
        job_id: Optional[int] = None,
        appointment_id: Optional[int] = None,
        project_manager_ids: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        starts_before: Optional[str] = None,
        starts_on_or_after: Optional[str] = None,
        completed_before: Optional[str] = None,
        completed_on_or_after: Optional[str] = None,
        target_completion_date_before: Optional[str] = None,
        target_completion_date_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        status: Optional[str] = None,
        sort: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of projects with filters. Mirrors Projects_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if customer_id is not None:
            params["customerId"] = customer_id
        if location_id is not None:
            params["locationId"] = location_id
        if project_type_id is not None:
            params["projectTypeId"] = project_type_id
        if invoice_id is not None:
            params["invoiceId"] = invoice_id
        if technician_id is not None:
            params["technicianId"] = technician_id
        if job_id is not None:
            params["jobId"] = job_id
        if appointment_id is not None:
            params["appointmentId"] = appointment_id
        if project_manager_ids:
            params["projectManagerIds"] = project_manager_ids
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if starts_before:
            params["startsBefore"] = starts_before
        if starts_on_or_after:
            params["startsOnOrAfter"] = starts_on_or_after
        if completed_before:
            params["completedBefore"] = completed_before
        if completed_on_or_after:
            params["completedOnOrAfter"] = completed_on_or_after
        if target_completion_date_before:
            params["targetCompletionDateBefore"] = target_completion_date_before
        if target_completion_date_on_or_after:
            params["targetCompletionDateOnOrAfter"] = target_completion_date_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if status:
            params["status"] = status
        if sort:
            params["sort"] = sort
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch projects."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_create(
        tenant: int,
        location_id: int,
        customer_id: Optional[int] = None,
        project_type_id: Optional[int] = None,
        project_manager_ids: Optional[Sequence[int]] = None,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        status_id: Optional[int] = None,
        sub_status_id: Optional[int] = None,
        start_date: Optional[str] = None,
        target_completion_date: Optional[str] = None,
        actual_completion_date: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        external_data: Optional[dict[str, Any]] = None,
        business_unit_ids: Optional[Sequence[int]] = None,
        environment: str = "production",
    ) -> str:
        """Create a project. Mirrors Projects_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects"

        body: dict[str, Any] = {
            "locationId": location_id,
        }
        if customer_id is not None:
            body["customerId"] = customer_id
        if project_type_id is not None:
            body["projectTypeId"] = project_type_id
        if project_manager_ids is not None:
            body["projectManagerIds"] = list(project_manager_ids)
        if name is not None:
            body["name"] = name
        if summary is not None:
            body["summary"] = summary
        if status_id is not None:
            body["statusId"] = status_id
        if sub_status_id is not None:
            body["subStatusId"] = sub_status_id
        if start_date is not None:
            body["startDate"] = start_date
        if target_completion_date is not None:
            body["targetCompletionDate"] = target_completion_date
        if actual_completion_date is not None:
            body["actualCompletionDate"] = actual_completion_date
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if external_data is not None:
            body["externalData"] = external_data
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create project."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_get_custom_field_types(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get project custom field types. Mirrors Projects_GetCustomFieldTypes."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/custom-fields"

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
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_detach_job(
        tenant: int,
        job_id: int,
        environment: str = "production",
    ) -> str:
        """Detach a job from its project. Mirrors Projects_DetachJob."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/detach-job/{job_id}"

        data = await make_st_post(url)
        if not data:
            return "Unable to detach job from project."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_update(
        tenant: int,
        id: int,
        project_manager_ids: Optional[Sequence[int]] = None,
        job_ids: Optional[Sequence[int]] = None,
        business_unit_ids: Optional[Sequence[int]] = None,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        status_id: Optional[int] = None,
        sub_status_id: Optional[int] = None,
        project_type_id: Optional[int] = None,
        start_date: Optional[str] = None,
        target_completion_date: Optional[str] = None,
        actual_completion_date: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update a project. Mirrors Projects_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/{id}"

        body: dict[str, Any] = {}
        if project_manager_ids is not None:
            body["projectManagerIds"] = list(project_manager_ids)
        if job_ids is not None:
            body["jobIds"] = list(job_ids)
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)
        if name is not None:
            body["name"] = name
        if summary is not None:
            body["summary"] = summary
        if status_id is not None:
            body["statusId"] = status_id
        if sub_status_id is not None:
            body["subStatusId"] = sub_status_id
        if project_type_id is not None:
            body["projectTypeId"] = project_type_id
        if start_date is not None:
            body["startDate"] = start_date
        if target_completion_date is not None:
            body["targetCompletionDate"] = target_completion_date
        if actual_completion_date is not None:
            body["actualCompletionDate"] = actual_completion_date
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if external_data is not None:
            body["externalData"] = external_data

        if not body:
            return "No fields provided to update project."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update project."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a project by ID. Mirrors Projects_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_attach_job(
        tenant: int,
        id: int,
        job_id: int,
        environment: str = "production",
    ) -> str:
        """Attach a job to a project. Mirrors Projects_AttachJob."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/{id}/attach-job/{job_id}"

        data = await make_st_post(url)
        if not data:
            return "Unable to attach job to project."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_get_notes(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get project notes. Mirrors Projects_GetNotes."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/{id}/notes"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch project notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_projects_create_note(
        tenant: int,
        id: int,
        text: str,
        pin_to_top: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a project note. Mirrors Projects_CreateNote."""

        if not text:
            return "text cannot be empty."

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/projects/{id}/notes"

        body: dict[str, Any] = {"text": text}
        if pin_to_top is not None:
            body["pinToTop"] = bool(pin_to_top)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create project note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


