import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_memberships_membership_types_tools"]


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


def register_memberships_membership_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_membership_types_get_list(
        tenant: int,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        duration: Optional[int] = None,
        billing_frequency: Optional[str] = None,
        include_duration_billing: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of membership types.

        Mirrors MembershipTypes_GetList.
        - active: one of "True", "Any", "False"
        - billing_frequency: OneTime|Monthly|EveryOtherMonth|Quarterly|BiAnnual|Annual
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/membership-types"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
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
        if include_duration_billing:
            params["includeDurationBilling"] = True
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
            return "Unable to fetch membership types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_membership_types_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets a membership type by ID.

        Mirrors MembershipTypes_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/membership-types/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch membership type by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_membership_types_get_discounts_list(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets discounts for a membership type.

        Mirrors MembershipTypes_GetDiscountsList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/membership-types/{id}/discounts"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch membership type discounts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_membership_types_get_duration_billing_list(
        tenant: int,
        id: int,
        active: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Gets duration/billing items for a membership type.

        Mirrors MembershipTypes_GetDurationBillingList.
        - active: one of "True", "Any", "False"
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/membership-types/{id}/duration-billing-items"

        params: dict[str, Any] = {}
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch membership type duration/billing items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_membership_types_get_recurring_service_items(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets recurring service items for a membership type.

        Mirrors MembershipTypes_GetRecurringServiceItems.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/membership-types/{id}/recurring-service-items"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch membership type recurring service items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


