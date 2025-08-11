import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_memberships_customer_memberships_tools"]


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


def register_memberships_customer_memberships_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_customer_memberships_get_list(
        tenant: int,
        ids: Optional[str] = None,
        customer_ids: Optional[str] = None,
        status: Optional[str] = None,
        duration: Optional[int] = None,
        billing_frequency: Optional[str] = None,
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
        """Get a paginated list of customer memberships with filters.

        Mirrors CustomerMemberships_GetList.
        - active: one of "True", "Any", "False" (case-insensitive). If omitted, API defaults to only active.
        - status: one of Active, Suspended, Expired, Canceled, Deleted
        - billing_frequency: one of OneTime, Monthly, EveryOtherMonth, Quarterly, BiAnnual, Annual
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if customer_ids:
            params["customerIds"] = customer_ids
        if status is not None:
            mapped_status = _normalize_enum(
                status, {"Active", "Suspended", "Expired", "Canceled", "Deleted"}
            )
            if not mapped_status:
                return "Invalid 'status'. Use one of: Active, Suspended, Expired, Canceled, Deleted."
            params["status"] = mapped_status
        if duration is not None:
            params["duration"] = int(duration)
        if billing_frequency is not None:
            mapped_bf = _normalize_enum(
                billing_frequency,
                {"OneTime", "Monthly", "EveryOtherMonth", "Quarterly", "BiAnnual", "Annual"},
            )
            if not mapped_bf:
                return "Invalid 'billing_frequency'. Use one of: OneTime, Monthly, EveryOtherMonth, Quarterly, BiAnnual, Annual."
            params["billingFrequency"] = mapped_bf
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
            return "Unable to fetch customer memberships."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_customer_memberships_get_custom_fields(
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
        """Gets a list of custom field types for customer memberships.

        Mirrors CustomerMemberships_GetCustomFields.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships/custom-fields"

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
            return "Unable to fetch membership custom field types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_customer_memberships_create(
        tenant: int,
        customer_id: int,
        business_unit_id: int,
        sale_task_id: int,
        duration_billing_id: int,
        location_id: Optional[int] = None,
        recurring_service_action: Optional[str] = None,
        recurring_location_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Creates a membership sale invoice.

        Mirrors CustomerMemberships_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships/sale"

        body: dict[str, Any] = {
            "customerId": int(customer_id),
            "businessUnitId": int(business_unit_id),
            "saleTaskId": int(sale_task_id),
            "durationBillingId": int(duration_billing_id),
        }
        if location_id is not None:
            body["locationId"] = int(location_id)
        if recurring_service_action is not None:
            mapped_action = _normalize_enum(recurring_service_action, {"None", "Single", "All"})
            if not mapped_action:
                return "Invalid 'recurring_service_action'. Use one of: None, Single, All."
            body["recurringServiceAction"] = mapped_action
        if recurring_location_id is not None:
            body["recurringLocationId"] = int(recurring_location_id)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create membership sale invoice."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_customer_memberships_update(
        tenant: int,
        id: int,
        business_unit_id: Optional[int] = None,
        next_scheduled_bill_date: Optional[str] = None,
        status: Optional[str] = None,
        memo: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        sold_by_id: Optional[int] = None,
        billing_template_id: Optional[int] = None,
        location_id: Optional[int] = None,
        recurring_service_action: Optional[str] = None,
        recurring_location_id: Optional[int] = None,
        payment_method_id: Optional[int] = None,
        payment_type_id: Optional[int] = None,
        renewal_membership_task_id: Optional[int] = None,
        initial_deferred_revenue: Optional[float] = None,
        cancellation_balance_invoice_id: Optional[int] = None,
        cancellation_invoice_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Updates a customer membership by ID (patch).

        Mirrors CustomerMemberships_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships/{id}"

        body: dict[str, Any] = {}
        if business_unit_id is not None:
            body["businessUnitId"] = int(business_unit_id)
        if next_scheduled_bill_date is not None:
            body["nextScheduledBillDate"] = next_scheduled_bill_date
        if status is not None:
            mapped_status = _normalize_enum(
                status, {"Active", "Suspended", "Expired", "Canceled", "Deleted"}
            )
            if not mapped_status:
                return "Invalid 'status'. Use one of: Active, Suspended, Expired, Canceled, Deleted."
            body["status"] = mapped_status
        if memo is not None:
            body["memo"] = memo
        if from_date is not None:
            body["from"] = from_date
        if to_date is not None:
            body["to"] = to_date
        if sold_by_id is not None:
            body["soldById"] = int(sold_by_id)
        if billing_template_id is not None:
            body["billingTemplateId"] = int(billing_template_id)
        if location_id is not None:
            body["locationId"] = int(location_id)
        if recurring_service_action is not None:
            mapped_action = _normalize_enum(recurring_service_action, {"None", "Single", "All"})
            if not mapped_action:
                return "Invalid 'recurring_service_action'. Use one of: None, Single, All."
            body["recurringServiceAction"] = mapped_action
        if recurring_location_id is not None:
            body["recurringLocationId"] = int(recurring_location_id)
        if payment_method_id is not None:
            body["paymentMethodId"] = int(payment_method_id)
        if payment_type_id is not None:
            body["paymentTypeId"] = int(payment_type_id)
        if renewal_membership_task_id is not None:
            body["renewalMembershipTaskId"] = int(renewal_membership_task_id)
        if initial_deferred_revenue is not None:
            body["initialDeferredRevenue"] = float(initial_deferred_revenue)
        if cancellation_balance_invoice_id is not None:
            body["cancellationBalanceInvoiceId"] = int(cancellation_balance_invoice_id)
        if cancellation_invoice_id is not None:
            body["cancellationInvoiceId"] = int(cancellation_invoice_id)

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update customer membership."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_customer_memberships_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a customer membership by ID.

        Mirrors CustomerMemberships_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch customer membership by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_customer_memberships_get_status_changes(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets status changes for a customer membership.

        Mirrors CustomerMemberships_GetStatusChanges.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/memberships/{id}/status-changes"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch membership status changes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


