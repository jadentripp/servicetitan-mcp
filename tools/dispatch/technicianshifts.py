import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_put, make_st_delete

__all__ = ["register_dispatch_technician_shifts_tools"]


def register_dispatch_technician_shifts_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_technician_shifts(
        tenant: int,
        starts_on_or_after: Optional[str] = None,
        ends_on_or_before: Optional[str] = None,
        shift_type: Optional[str] = None,
        technician_id: Optional[int] = None,
        title_contains: Optional[str] = None,
        note_contains: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of technician shifts with filters.

        Mirrors TechnicianShifts_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        - shift_type: one of Normal, OnCall, TimeOff (case-insensitive)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts"

        params: dict[str, Any] = {}
        if starts_on_or_after:
            params["startsOnOrAfter"] = starts_on_or_after
        if ends_on_or_before:
            params["endsOnOrBefore"] = ends_on_or_before
        if shift_type:
            normalized = shift_type.strip().lower()
            if normalized in {"normal", "oncall", "timeoff"}:
                params["shiftType"] = {
                    "normal": "Normal",
                    "oncall": "OnCall",
                    "timeoff": "TimeOff",
                }[normalized]
            else:
                return "Invalid 'shift_type'. Use one of: Normal, OnCall, TimeOff."
        if technician_id is not None:
            params["technicianId"] = technician_id
        if title_contains:
            params["titleContains"] = title_contains
        if note_contains:
            params["noteContains"] = note_contains
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if active is not None:
            a = str(active).strip().lower()
            if a in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[a]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."
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
            return "Unable to fetch technician shifts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_create_technician_shifts(
        tenant: int,
        technician_ids: Sequence[int],
        shift_type: str,
        title: str,
        start: str,
        end: str,
        note: Optional[str] = None,
        timesheet_code_id: Optional[int] = None,
        repeat_type: str = "Never",
        repeat_end_date: Optional[str] = None,
        repeat_interval: Optional[int] = None,
        shift_days: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create technician shift(s).

        Mirrors TechnicianShifts_Create.
        - shift_type: Normal | OnCall | TimeOff
        - repeat_type: Never | Daily | Weekly
        """

        if not technician_ids:
            return "'technician_ids' must contain at least one technician ID."
        if not title:
            return "'title' is required."
        if not start:
            return "'start' is required."
        if not end:
            return "'end' is required."

        st_norm = shift_type.strip().lower()
        if st_norm not in {"normal", "oncall", "timeoff"}:
            return "Invalid 'shift_type'. Use one of: Normal, OnCall, TimeOff."
        rt_norm = (repeat_type or "").strip().lower()
        if rt_norm not in {"never", "daily", "weekly"}:
            return "Invalid 'repeat_type'. Use one of: Never, Daily, Weekly."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts"

        body: dict[str, Any] = {
            "technicianIds": list(technician_ids),
            "shiftType": {"normal": "Normal", "oncall": "OnCall", "timeoff": "TimeOff"}[st_norm],
            "title": title,
            "start": start,
            "end": end,
            "repeatType": {"never": "Never", "daily": "Daily", "weekly": "Weekly"}[rt_norm],
        }
        if note is not None:
            body["note"] = note
        if timesheet_code_id is not None:
            body["timesheetCodeId"] = int(timesheet_code_id)
        if repeat_end_date is not None:
            body["repeatEndDate"] = repeat_end_date
        if repeat_interval is not None:
            body["repeatInterval"] = int(repeat_interval)
        if shift_days is not None:
            body["shiftDays"] = shift_days

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create technician shifts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_bulk_delete_technician_shifts(
        tenant: int,
        start: str,
        end: str,
        environment: str = "production",
    ) -> str:
        """Bulk delete technician shifts by date range.

        Mirrors TechnicianShifts_BulkDelete.
        """

        if not start:
            return "'start' is required."
        if not end:
            return "'end' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts/bulk-delete"

        body = {"start": start, "end": end}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to bulk delete technician shifts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_update_technician_shift(
        tenant: int,
        id: int,
        shift_type: Optional[str] = None,
        title: Optional[str] = None,
        start: Optional[str] = None,
        end: Optional[str] = None,
        note: Optional[str] = None,
        timesheet_code_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Update a technician shift by ID.

        Mirrors TechnicianShifts_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts/{id}"

        body: dict[str, Any] = {}
        if shift_type is not None:
            st_norm = shift_type.strip().lower()
            if st_norm not in {"normal", "oncall", "timeoff"}:
                return "Invalid 'shift_type'. Use one of: Normal, OnCall, TimeOff."
            body["shiftType"] = {"normal": "Normal", "oncall": "OnCall", "timeoff": "TimeOff"}[st_norm]
        if title is not None:
            body["title"] = title
        if start is not None:
            body["start"] = start
        if end is not None:
            body["end"] = end
        if note is not None:
            body["note"] = note
        if timesheet_code_id is not None:
            body["timesheetCodeId"] = int(timesheet_code_id)

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update technician shift."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_get_technician_shift(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single technician shift by ID.

        Mirrors TechnicianShifts_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch technician shift."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def dispatch_delete_technician_shift(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a technician shift by ID.

        Mirrors TechnicianShifts_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-shifts/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete technician shift."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


