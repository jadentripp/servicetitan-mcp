import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_delete,
    make_st_patch,
)

__all__ = ["register_jobplanningandmanagement_appointments_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    key = v.lower()
    return lower_map.get(key, v)


def register_jobplanningandmanagement_appointments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_appointments_get_list(
        tenant: int,
        ids: Optional[str] = None,
        job_id: Optional[int] = None,
        project_id: Optional[int] = None,
        number: Optional[str] = None,
        status: Optional[str] = None,
        starts_on_or_after: Optional[str] = None,
        starts_before: Optional[str] = None,
        technician_id: Optional[int] = None,
        customer_id: Optional[int] = None,
        unused: Optional[bool] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of appointments with filters.

        Mirrors Appointments_GetList.
        - status: one of Scheduled, Dispatched, Working, Hold, Done, Canceled (case-insensitive)
        - CSV filters (ids) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if job_id is not None:
            params["jobId"] = job_id
        if project_id is not None:
            params["projectId"] = project_id
        if number:
            params["number"] = number
        if status:
            normalized = _normalize_enum(
                status,
                {"Scheduled", "Dispatched", "Working", "Hold", "Done", "Canceled"},
            )
            params["status"] = normalized
        if starts_on_or_after:
            params["startsOnOrAfter"] = starts_on_or_after
        if starts_before:
            params["startsBefore"] = starts_before
        if technician_id is not None:
            params["technicianId"] = technician_id
        if customer_id is not None:
            params["customerId"] = customer_id
        if unused is not None:
            params["unused"] = bool(unused)
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch appointments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_add(
        tenant: int,
        job_id: int,
        start: str,
        end: str,
        arrival_window_start: Optional[str] = None,
        arrival_window_end: Optional[str] = None,
        technician_ids: Optional[Sequence[int]] = None,
        special_instructions: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new appointment on an existing job. Mirrors Appointments_Add."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments"

        body: dict[str, Any] = {
            "jobId": job_id,
            "start": start,
            "end": end,
        }
        if arrival_window_start is not None:
            body["arrivalWindowStart"] = arrival_window_start
        if arrival_window_end is not None:
            body["arrivalWindowEnd"] = arrival_window_end
        if technician_ids is not None:
            body["technicianIds"] = list(technician_ids)
        if special_instructions is not None:
            body["specialInstructions"] = special_instructions

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get an appointment by ID. Mirrors Appointments_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch appointment by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete an appointment by ID. Mirrors Appointments_Delete."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}"

        data = await make_st_delete(url)
        if not data:
            return "Unable to delete appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_confirm(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Add a confirmation to the appointment. Mirrors Appointments_Confirm."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/confirmation"

        data = await make_st_post(url)
        if not data:
            return "Unable to confirm appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_remove_confirmation(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Remove confirmation from the appointment. Mirrors Appointments_RemoveConfirmation."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/confirmation"

        data = await make_st_delete(url)
        if not data:
            return "Unable to remove appointment confirmation."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_hold(
        tenant: int,
        id: int,
        reason_id: int,
        memo: str,
        environment: str = "production",
    ) -> str:
        """Put an appointment on hold. Mirrors Appointments_Hold."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/hold"

        body = {"reasonId": reason_id, "memo": memo}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to put appointment on hold."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_remove_hold(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Remove hold from an appointment. Mirrors Appointments_RemoveHold."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/hold"

        data = await make_st_delete(url)
        if not data:
            return "Unable to remove appointment hold."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_reschedule(
        tenant: int,
        id: int,
        start: Optional[str] = None,
        end: Optional[str] = None,
        arrival_window_start: Optional[str] = None,
        arrival_window_end: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Reschedule an appointment. Mirrors Appointments_Reschedule."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/reschedule"

        body: dict[str, Any] = {}
        if start is not None:
            body["start"] = start
        if end is not None:
            body["end"] = end
        if arrival_window_start is not None:
            body["arrivalWindowStart"] = arrival_window_start
        if arrival_window_end is not None:
            body["arrivalWindowEnd"] = arrival_window_end

        if not body:
            return "No fields provided to reschedule."

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to reschedule appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_appointments_update_special_instructions(
        tenant: int,
        id: int,
        special_instructions: str,
        environment: str = "production",
    ) -> str:
        """Update appointment special instructions. Mirrors Appointments_UpdateSpecialInstructions."""

        if not special_instructions:
            return "special_instructions cannot be empty."

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/appointments/{id}/special-instructions"

        body = {"specialInstructions": special_instructions}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to update appointment special instructions."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


