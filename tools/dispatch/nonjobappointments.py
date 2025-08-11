import json
from typing import Any, Optional

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_put,
    make_st_delete,
)

__all__ = ["register_dispatch_non_job_appointments_tools"]


def register_dispatch_non_job_appointments_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_non_job_appointments(
        tenant: int,
        technician_id: Optional[int] = None,
        starts_on_or_after: Optional[str] = None,
        starts_on_or_before: Optional[str] = None,
        timesheet_code_id: Optional[int] = None,
        active_only: Optional[bool] = None,
        show_on_technician_schedule: Optional[bool] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a list of non-job appointments (paginated) with filters.

        Mirrors NonJobAppointments_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/non-job-appointments"

        params: dict[str, Any] = {}
        if technician_id is not None:
            params["technicianId"] = technician_id
        if starts_on_or_after:
            params["startsOnOrAfter"] = starts_on_or_after
        if starts_on_or_before:
            params["startsOnOrBefore"] = starts_on_or_before
        if timesheet_code_id is not None:
            params["timesheetCodeId"] = timesheet_code_id
        if active_only is not None:
            params["activeOnly"] = bool(active_only)
        if show_on_technician_schedule is not None:
            params["showOnTechnicianSchedule"] = bool(show_on_technician_schedule)
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if ids:
            params["ids"] = ids
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
            return "Unable to fetch non-job appointments."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_non_job_appointment(
        tenant: int,
        technician_id: int,
        start: str,
        duration: str,
        name: str,
        timesheet_code_id: Optional[int] = None,
        summary: Optional[str] = None,
        clear_dispatch_board: Optional[bool] = None,
        clear_technician_view: Optional[bool] = None,
        show_on_technician_schedule: Optional[bool] = None,
        remove_technician_from_capacity_planning: Optional[bool] = None,
        all_day: Optional[bool] = None,
        repeat: Optional[bool] = None,
        count_occurrences: Optional[int] = None,
        interval: Optional[int] = None,
        frequency: Optional[str] = None,
        end_type: Optional[str] = None,
        end_on: Optional[str] = None,
        days_of_week: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new non-job appointment.

        Mirrors NonJobAppointments_Create.
        """

        if not technician_id:
            return "'technician_id' is required."
        if not start:
            return "'start' is required."
        if not duration:
            return "'duration' is required."
        if not name:
            return "'name' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/non-job-appointments"

        body: dict[str, Any] = {
            "technicianId": int(technician_id),
            "start": start,
            "duration": duration,
            "name": name,
        }
        if timesheet_code_id is not None:
            body["timesheetCodeId"] = int(timesheet_code_id)
        if summary is not None:
            body["summary"] = summary
        if clear_dispatch_board is not None:
            body["clearDispatchBoard"] = bool(clear_dispatch_board)
        if clear_technician_view is not None:
            body["clearTechnicianView"] = bool(clear_technician_view)
        if show_on_technician_schedule is not None:
            body["showOnTechnicianSchedule"] = bool(show_on_technician_schedule)
        if remove_technician_from_capacity_planning is not None:
            body["removeTechnicianFromCapacityPlanning"] = bool(
                remove_technician_from_capacity_planning
            )
        if all_day is not None:
            body["allDay"] = bool(all_day)
        if repeat is not None:
            body["repeat"] = bool(repeat)
        if count_occurrences is not None:
            body["countOccurrences"] = int(count_occurrences)
        if interval is not None:
            body["interval"] = int(interval)
        if frequency is not None:
            body["frequency"] = frequency
        if end_type is not None:
            body["endType"] = end_type
        if end_on is not None:
            body["endOn"] = end_on
        if days_of_week is not None:
            body["daysOfWeek"] = days_of_week

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create non-job appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_update_non_job_appointment(
        tenant: int,
        id: int,
        technician_id: int,
        start: str,
        duration: str,
        name: str,
        timesheet_code_id: Optional[int] = None,
        summary: Optional[str] = None,
        clear_dispatch_board: Optional[bool] = None,
        clear_technician_view: Optional[bool] = None,
        show_on_technician_schedule: Optional[bool] = None,
        remove_technician_from_capacity_planning: Optional[bool] = None,
        all_day: Optional[bool] = None,
        repeat: Optional[bool] = None,
        count_occurrences: Optional[int] = None,
        interval: Optional[int] = None,
        frequency: Optional[str] = None,
        end_type: Optional[str] = None,
        end_on: Optional[str] = None,
        days_of_week: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing non-job appointment.

        Mirrors NonJobAppointments_Update.
        """

        if not technician_id:
            return "'technician_id' is required."
        if not start:
            return "'start' is required."
        if not duration:
            return "'duration' is required."
        if not name:
            return "'name' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/non-job-appointments/{id}"

        body: dict[str, Any] = {
            "technicianId": int(technician_id),
            "start": start,
            "duration": duration,
            "name": name,
        }
        if timesheet_code_id is not None:
            body["timesheetCodeId"] = int(timesheet_code_id)
        if summary is not None:
            body["summary"] = summary
        if clear_dispatch_board is not None:
            body["clearDispatchBoard"] = bool(clear_dispatch_board)
        if clear_technician_view is not None:
            body["clearTechnicianView"] = bool(clear_technician_view)
        if show_on_technician_schedule is not None:
            body["showOnTechnicianSchedule"] = bool(show_on_technician_schedule)
        if remove_technician_from_capacity_planning is not None:
            body["removeTechnicianFromCapacityPlanning"] = bool(
                remove_technician_from_capacity_planning
            )
        if all_day is not None:
            body["allDay"] = bool(all_day)
        if repeat is not None:
            body["repeat"] = bool(repeat)
        if count_occurrences is not None:
            body["countOccurrences"] = int(count_occurrences)
        if interval is not None:
            body["interval"] = int(interval)
        if frequency is not None:
            body["frequency"] = frequency
        if end_type is not None:
            body["endType"] = end_type
        if end_on is not None:
            body["endOn"] = end_on
        if days_of_week is not None:
            body["daysOfWeek"] = days_of_week

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update non-job appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_non_job_appointment(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single non-job appointment by ID.

        Mirrors NonJobAppointments_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/non-job-appointments/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch non-job appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_delete_non_job_appointment(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a non-job appointment by ID.

        Mirrors NonJobAppointments_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/non-job-appointments/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete non-job appointment."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


