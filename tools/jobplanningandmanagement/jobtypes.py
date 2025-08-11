import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_jobplanningandmanagement_job_types_tools"]


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    key = v.lower()
    return lower_map.get(key, v)


def register_jobplanningandmanagement_job_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def jpm_job_types_get_list(
        tenant: int,
        name: Optional[str] = None,
        min_duration: Optional[int] = None,
        max_duration: Optional[int] = None,
        priority: Optional[str] = None,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        order_by: Optional[str] = None,
        order_by_direction: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of job types.

        Mirrors JobTypes_GetList.
        - priority: one of Low, Normal, High, Urgent (case-insensitive)
        - active: one of True, Any, False (case-insensitive). If omitted, API defaults to only active.
        - order_by: id | modifiedOn | createdOn
        - order_by_direction: asc|ascending|desc|descending (case-insensitive)
        - CSV filters (ids) should be provided as comma-separated strings.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/job-types"

        params: dict[str, Any] = {}
        if name:
            params["name"] = name
        if min_duration is not None:
            params["minDuration"] = min_duration
        if max_duration is not None:
            params["maxDuration"] = max_duration
        if priority:
            params["priority"] = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"})
        if ids:
            params["ids"] = ids
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."
        if order_by:
            params["orderBy"] = order_by
        if order_by_direction:
            direction_normalized = order_by_direction.strip().lower()
            if direction_normalized in {"asc", "ascending"}:
                params["orderByDirection"] = "asc"
            elif direction_normalized in {"desc", "descending"}:
                params["orderByDirection"] = "desc"
            else:
                return "Invalid 'order_by_direction'. Use one of: asc, ascending, desc, descending."
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_job_types_create(
        tenant: int,
        name: str,
        business_unit_ids: Optional[Sequence[int]] = None,
        skills: Optional[Sequence[str]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        priority: Optional[str] = None,
        duration: Optional[int] = None,
        sold_threshold: Optional[float] = None,
        job_class: Optional[str] = None,
        summary: Optional[str] = None,
        no_charge: Optional[bool] = None,
        enforce_recurring_service_event_selection: Optional[bool] = None,
        invoice_signatures_required: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Create a job type. Mirrors JobTypes_Create."""

        if not name:
            return "name is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/job-types"

        body: dict[str, Any] = {"name": name}
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)
        if skills is not None:
            body["skills"] = list(skills)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if priority is not None:
            body["priority"] = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"}) or priority
        if duration is not None:
            body["duration"] = duration
        if sold_threshold is not None:
            body["soldThreshold"] = sold_threshold
        if job_class is not None:
            body["class"] = job_class
        if summary is not None:
            body["summary"] = summary
        if no_charge is not None:
            body["noCharge"] = bool(no_charge)
        if enforce_recurring_service_event_selection is not None:
            body["enforceRecurringServiceEventSelection"] = bool(enforce_recurring_service_event_selection)
        if invoice_signatures_required is not None:
            body["invoiceSignaturesRequired"] = bool(invoice_signatures_required)
        if external_data is not None:
            body["externalData"] = external_data

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create job type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_job_types_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        business_unit_ids: Optional[Sequence[int]] = None,
        skills: Optional[Sequence[str]] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        priority: Optional[str] = None,
        duration: Optional[int] = None,
        sold_threshold: Optional[float] = None,
        job_class: Optional[str] = None,
        summary: Optional[str] = None,
        no_charge: Optional[bool] = None,
        enforce_recurring_service_event_selection: Optional[bool] = None,
        invoice_signatures_required: Optional[bool] = None,
        external_data: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update a job type. Mirrors JobTypes_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/job-types/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)
        if skills is not None:
            body["skills"] = list(skills)
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if priority is not None:
            body["priority"] = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"}) or priority
        if duration is not None:
            body["duration"] = duration
        if sold_threshold is not None:
            body["soldThreshold"] = sold_threshold
        if job_class is not None:
            body["class"] = job_class
        if summary is not None:
            body["summary"] = summary
        if no_charge is not None:
            body["noCharge"] = bool(no_charge)
        if enforce_recurring_service_event_selection is not None:
            body["enforceRecurringServiceEventSelection"] = bool(enforce_recurring_service_event_selection)
        if invoice_signatures_required is not None:
            body["invoiceSignaturesRequired"] = bool(invoice_signatures_required)
        if external_data is not None:
            body["externalData"] = external_data

        if not body:
            return "No fields provided to update job type."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update job type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def jpm_job_types_get(
        tenant: int,
        id: int,
        external_data_application_guid: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a job type by ID. Mirrors JobTypes_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/jpm/v2/tenant/{tenant}/job-types/{id}"

        params: dict[str, Any] = {}
        if external_data_application_guid:
            params["externalDataApplicationGuid"] = external_data_application_guid

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch job type by id."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


