import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_jobplanningandmanagement_jobs_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    key = v.lower()
    return lower_map.get(key, v)


def register_jobplanningandmanagement_jobs_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_jobs_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        ids: Optional[str] = None,
        number: Optional[str] = None,
        project_id: Optional[int] = None,
        booking_id: Optional[int] = None,
        job_status: Optional[str] = None,
        appointment_status: Optional[str] = None,
        priority: Optional[str] = None,
        first_appointment_starts_on_or_after: Optional[str] = None,
        first_appointment_starts_before: Optional[str] = None,
        appointment_starts_on_or_after: Optional[str] = None,
        appointment_starts_before: Optional[str] = None,
        technician_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        location_id: Optional[int] = None,
        sold_by_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        campaign_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        invoice_id: Optional[int] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        completed_on_or_after: Optional[str] = None,
        completed_before: Optional[str] = None,
        tag_type_ids: Optional[str] = None,
        sort: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        external_data_key: Optional[str] = None,
        external_data_values: Optional[str] = None,
        has_unused_appointments: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of jobs with filters.

        Mirrors Jobs_GetList.
        - job_status: one of Scheduled, Dispatched, InProgress, Hold, Completed, Canceled (case-insensitive)
        - appointment_status: one of Scheduled, Dispatched, Working, Hold, Done, Canceled (case-insensitive)
        - priority: one of Low, Normal, High, Urgent (case-insensitive)
        - CSV filters (ids, tag_type_ids, external_data_values) should be provided as comma-separated strings.
        - has_unused_appointments is included only when True.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if ids:
            params["ids"] = ids
        if number:
            params["number"] = number
        if project_id is not None:
            params["projectId"] = project_id
        if booking_id is not None:
            params["bookingId"] = booking_id
        if job_status:
            params["jobStatus"] = _normalize_enum(
                job_status,
                {"Scheduled", "Dispatched", "InProgress", "Hold", "Completed", "Canceled"},
            )
        if appointment_status:
            params["appointmentStatus"] = _normalize_enum(
                appointment_status, {"Scheduled", "Dispatched", "Working", "Hold", "Done", "Canceled"}
            )
        if priority:
            params["priority"] = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"})
        if first_appointment_starts_on_or_after:
            params["firstAppointmentStartsOnOrAfter"] = first_appointment_starts_on_or_after
        if first_appointment_starts_before:
            params["firstAppointmentStartsBefore"] = first_appointment_starts_before
        if appointment_starts_on_or_after:
            params["appointmentStartsOnOrAfter"] = appointment_starts_on_or_after
        if appointment_starts_before:
            params["appointmentStartsBefore"] = appointment_starts_before
        if technician_id is not None:
            params["technicianId"] = technician_id
        if customer_id is not None:
            params["customerId"] = customer_id
        if location_id is not None:
            params["locationId"] = location_id
        if sold_by_id is not None:
            params["soldById"] = sold_by_id
        if job_type_id is not None:
            params["jobTypeId"] = job_type_id
        if campaign_id is not None:
            params["campaignId"] = campaign_id
        if business_unit_id is not None:
            params["businessUnitId"] = business_unit_id
        if invoice_id is not None:
            params["invoiceId"] = invoice_id
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if completed_on_or_after:
            params["completedOnOrAfter"] = completed_on_or_after
        if completed_before:
            params["completedBefore"] = completed_before
        if tag_type_ids:
            params["tagTypeIds"] = tag_type_ids
        if sort:
            params["sort"] = sort
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid
        if external_data_key:
            params["externalDataKey"] = external_data_key
        if external_data_values:
            params["externalDataValues"] = external_data_values
        if has_unused_appointments:
            params["hasUnusedAppointments"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch jobs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_update(
        tenant: int,
        id: int,
        customer_id: Optional[int] = None,
        location_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        job_generated_lead_source: Optional[dict[str, Any]] = None,
        job_type_id: Optional[int] = None,
        priority: Optional[str] = None,
        campaign_id: Optional[int] = None,
        summary: Optional[str] = None,
        should_update_invoice_items: Optional[bool] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        customer_po: Optional[str] = None,
        sold_by_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Update a job. Mirrors Jobs_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}"

        body: dict[str, Any] = {}
        if customer_id is not None:
            body["customerId"] = customer_id
        if location_id is not None:
            body["locationId"] = location_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if job_generated_lead_source is not None:
            body["jobGeneratedLeadSource"] = job_generated_lead_source
        if job_type_id is not None:
            body["jobTypeId"] = job_type_id
        if priority is not None:
            body["priority"] = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"}) or priority
        if campaign_id is not None:
            body["campaignId"] = campaign_id
        if summary is not None:
            body["summary"] = summary
        if should_update_invoice_items is not None:
            body["shouldUpdateInvoiceItems"] = bool(should_update_invoice_items)
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if external_data is not None:
            body["externalData"] = external_data
        if customer_po is not None:
            body["customerPo"] = customer_po
        if sold_by_id is not None:
            body["soldById"] = sold_by_id

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update job."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a job by ID. Mirrors Jobs_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}"
        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_booked_log(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get booked log for a job. Mirrors Jobs_GetBookedLog."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/booked-log"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch job booked log."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_cancel(
        tenant: int,
        id: int,
        reason_id: int,
        memo: str,
        environment: str = "production",
    ) -> str:
        """Cancel a job. Mirrors Jobs_Cancel."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/cancel"

        body = {"reasonId": reason_id, "memo": memo}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to cancel job."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_canceled_logs(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get canceled logs for a job. Mirrors Jobs_GetJobCanceledLogs."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/canceled-log"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job canceled logs."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_history(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get job history entries. Mirrors Jobs_GetHistory."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/history"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch job history."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_notes(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get job notes. Mirrors Jobs_GetNotes."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/notes"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_create_note(
        tenant: int,
        id: int,
        text: str,
        pin_to_top: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a job note. Mirrors Jobs_CreateNote."""

        if not text:
            return "text cannot be empty."

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/notes"

        body: dict[str, Any] = {"text": text}
        if pin_to_top is not None:
            body["pinToTop"] = bool(pin_to_top)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create job note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_remove_cancellation(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Remove cancellation from a job. Mirrors Jobs_RemoveCancellation."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/{id}/remove-cancellation"

        data = await make_st_post(url)
        if not data:
            return "Unable to remove job cancellation."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_create(
        tenant: int,
        customer_id: int,
        location_id: int,
        business_unit_id: int,
        job_type_id: int,
        priority: str,
        campaign_id: int,
        appointments: Sequence[dict[str, Any]],
        project_id: Optional[int] = None,
        job_generated_lead_source: Optional[dict[str, Any]] = None,
        summary: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        external_data: Optional[dict[str, Any]] = None,
        invoice_signature_is_required: Optional[bool] = None,
        customer_po: Optional[str] = None,
        sold_by_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Create a job. Mirrors Jobs_Create.

        Provide appointments as a list of AppointmentInformation objects.
        Optionally include custom fields, tag IDs, external data, and other fields.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs"

        body: dict[str, Any] = {
            "customerId": customer_id,
            "locationId": location_id,
            "businessUnitId": business_unit_id,
            "jobTypeId": job_type_id,
            "priority": _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"}) or priority,
            "campaignId": campaign_id,
            "appointments": list(appointments),
        }

        if project_id is not None:
            body["projectId"] = project_id
        if job_generated_lead_source is not None:
            body["jobGeneratedLeadSource"] = job_generated_lead_source
        if summary is not None:
            body["summary"] = summary
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if external_data is not None:
            body["externalData"] = external_data
        if invoice_signature_is_required is not None:
            body["invoiceSignatureIsRequired"] = bool(invoice_signature_is_required)
        if customer_po is not None:
            body["customerPo"] = customer_po
        if sold_by_id is not None:
            body["soldById"] = sold_by_id

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create job."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_cancel_reasons(
        tenant: int,
        ids: str,
        environment: str = "production",
    ) -> str:
        """Get cancel reasons for specific jobs. Mirrors Jobs_GetCancelReasons.

        ids: comma-separated job IDs (max 50)
        """

        if not ids:
            return "No 'ids' provided. Provide comma-separated job IDs."

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/cancel-reasons"

        params = {"ids": ids}
        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch job cancel reasons."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_jobs_get_custom_field_types(
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
        """Get job custom field types. Mirrors Jobs_GetCustomFieldTypes."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/jobs/custom-fields"

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
            return "Unable to fetch job custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


