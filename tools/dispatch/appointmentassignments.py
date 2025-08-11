import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post

__all__ = ["register_dispatch_appointment_assignments_tools"]


def register_dispatch_appointment_assignments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_appointment_assignments(
        tenant: int,
        ids: Optional[str] = None,
        appointment_ids: Optional[str] = None,
        job_id: Optional[int] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of appointment assignments with filters.

        Mirrors AppointmentAssignments_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        - sort: like "+FieldName" or "-FieldName". Allowed: Id, CreatedOn, ModifiedOn
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/appointment-assignments"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if appointment_ids:
            params["appointmentIds"] = appointment_ids
        if job_id is not None:
            params["jobId"] = job_id
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
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
        if sort:
            params["sort"] = sort
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch appointment assignments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_assign_technicians(
        tenant: int,
        job_appointment_id: int,
        technician_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Assign the list of technicians to an appointment.

        Mirrors AppointmentAssignments_AssignTechnicians.
        """

        if not technician_ids:
            return "No technician IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/appointment-assignments/assign-technicians"

        body = {"jobAppointmentId": int(job_appointment_id), "technicianIds": list(technician_ids)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to assign technicians to appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_unassign_technicians(
        tenant: int,
        job_appointment_id: int,
        technician_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Unassign the list of technicians from an appointment.

        Mirrors AppointmentAssignments_UnassignTechnicians.
        """

        if not technician_ids:
            return "No technician IDs provided."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/appointment-assignments/unassign-technicians"

        body = {"jobAppointmentId": int(job_appointment_id), "technicianIds": list(technician_ids)}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to unassign technicians from appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



