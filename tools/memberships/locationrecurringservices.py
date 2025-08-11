import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_patch

__all__ = ["register_memberships_location_recurring_services_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return "__INVALID__"


def _normalize_enum(value: Optional[str], allowed: set[str]) -> Optional[str]:
    if value is None:
        return None
    v = value.strip()
    lower_map = {a.lower(): a for a in allowed}
    return lower_map.get(v.lower())


def register_memberships_location_recurring_services_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_location_recurring_services_get_list(
        tenant: int,
        ids: Optional[str] = None,
        membership_ids: Optional[str] = None,
        location_ids: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of recurring services.

        Mirrors LocationRecurringServices_GetList.
        - active: one of "True", "Any", "False" (case-insensitive)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-services"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if membership_ids:
            params["membershipIds"] = membership_ids
        if location_ids:
            params["locationIds"] = location_ids
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch recurring services."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_location_recurring_services_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        active: Optional[bool] = None,
        recurring_service_type_id: Optional[int] = None,
        duration_type: Optional[str] = None,
        duration_length: Optional[int] = None,
        from_date: Optional[str] = None,
        memo: Optional[str] = None,
        invoice_template_id: Optional[int] = None,
        invoice_template_for_following_years_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        campaign_id: Optional[int] = None,
        priority: Optional[str] = None,
        job_summary: Optional[str] = None,
        recurrence_type: Optional[str] = None,
        recurrence_interval: Optional[int] = None,
        recurrence_months: Optional[Sequence[str]] = None,
        recurrence_days_of_week: Optional[Sequence[str]] = None,
        recurrence_week: Optional[str] = None,
        recurrence_day_of_nth_week: Optional[str] = None,
        job_start_time: Optional[str] = None,
        estimated_payroll_cost: Optional[float] = None,
        environment: str = "production",
    ) -> str:
        """Updates a recurring service by ID (patch).

        Mirrors LocationRecurringServices_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-services/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if active is not None:
            body["active"] = bool(active)
        if recurring_service_type_id is not None:
            body["recurringServiceTypeId"] = int(recurring_service_type_id)
        if duration_type is not None:
            mapped = _normalize_enum(duration_type, {"Continuous", "NumberOfVisits"})
            if not mapped:
                return "Invalid 'duration_type'. Use one of: Continuous, NumberOfVisits."
            body["durationType"] = mapped
        if duration_length is not None:
            body["durationLength"] = int(duration_length)
        if from_date is not None:
            body["from"] = from_date
        if memo is not None:
            body["memo"] = memo
        if invoice_template_id is not None:
            body["invoiceTemplateId"] = int(invoice_template_id)
        if invoice_template_for_following_years_id is not None:
            body["invoiceTemplateForFollowingYearsId"] = int(invoice_template_for_following_years_id)
        if business_unit_id is not None:
            body["businessUnitId"] = int(business_unit_id)
        if job_type_id is not None:
            body["jobTypeId"] = int(job_type_id)
        if campaign_id is not None:
            body["campaignId"] = int(campaign_id)
        if priority is not None:
            mapped = _normalize_enum(priority, {"Low", "Normal", "High", "Urgent"})
            if not mapped:
                return "Invalid 'priority'. Use one of: Low, Normal, High, Urgent."
            body["priority"] = mapped
        if job_summary is not None:
            body["jobSummary"] = job_summary
        if recurrence_type is not None:
            mapped = _normalize_enum(recurrence_type, {"Weekly", "Monthly", "Seasonal", "Daily", "NthWeekdayOfMonth"})
            if not mapped:
                return "Invalid 'recurrence_type'. Use one of: Weekly, Monthly, Seasonal, Daily, NthWeekdayOfMonth."
            body["recurrenceType"] = mapped
        if recurrence_interval is not None:
            body["recurrenceInterval"] = int(recurrence_interval)
        if recurrence_months is not None:
            body["recurrenceMonths"] = list(recurrence_months)
        if recurrence_days_of_week is not None:
            body["recurrenceDaysOfWeek"] = list(recurrence_days_of_week)
        if recurrence_week is not None:
            mapped = _normalize_enum(recurrence_week, {"None", "First", "Second", "Third", "Fourth", "Last"})
            if not mapped:
                return "Invalid 'recurrence_week'. Use one of: None, First, Second, Third, Fourth, Last."
            body["recurrenceWeek"] = mapped
        if recurrence_day_of_nth_week is not None:
            mapped = _normalize_enum(
                recurrence_day_of_nth_week,
                {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"},
            )
            if not mapped:
                return "Invalid 'recurrence_day_of_nth_week'. Use one of: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday."
            body["recurrenceDayOfNthWeek"] = mapped
        if job_start_time is not None:
            body["jobStartTime"] = job_start_time
        if estimated_payroll_cost is not None:
            body["estimatedPayrollCost"] = float(estimated_payroll_cost)

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update recurring service."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_location_recurring_services_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a recurring service by ID.

        Mirrors LocationRecurringServices_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/recurring-services/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch recurring service by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


