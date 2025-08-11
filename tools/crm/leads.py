import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_crm_leads_tools"]


def register_crm_leads_tools(mcp: Any) -> None:
    """Register CRM Leads tools."""

    @mcp.tool()
    async def crm_leads_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        ids: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        customer_id: Optional[int] = None,
        is_prospect: Optional[bool] = None,
        without_customer: Optional[bool] = None,
        status: Optional[str] = None,
        customer_city: Optional[str] = None,
        customer_state: Optional[str] = None,
        customer_zip: Optional[str] = None,
        customer_created_on_or_after: Optional[str] = None,
        customer_created_before: Optional[str] = None,
        customer_modified_on_or_after: Optional[str] = None,
        sort: Optional[str] = None,
        gen_perm_url: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of leads with filters.

        Mirrors Leads_GetList.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if ids:
            params["ids"] = ids
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if customer_id is not None:
            params["customerId"] = customer_id
        if is_prospect is not None:
            params["isProspect"] = is_prospect
        if without_customer is not None:
            params["withoutCustomer"] = without_customer
        if status:
            params["status"] = status
        if customer_city:
            params["customerCity"] = customer_city
        if customer_state:
            params["customerState"] = customer_state
        if customer_zip:
            params["customerZip"] = customer_zip
        if customer_created_on_or_after:
            params["customerCreatedOnOrAfter"] = customer_created_on_or_after
        if customer_created_before:
            params["customerCreatedBefore"] = customer_created_before
        if customer_modified_on_or_after:
            params["customerModifiedOnOrAfter"] = customer_modified_on_or_after
        if sort:
            params["sort"] = sort
        if gen_perm_url is not None:
            params["genPermUrl"] = gen_perm_url

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch leads."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_create(
        tenant: int,
        campaign_id: int,
        summary: str,
        customer_id: Optional[int] = None,
        location_id: Optional[int] = None,
        business_unit_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        tag_type_ids: Optional[Sequence[int]] = None,
        priority: Optional[str] = None,
        call_reason_id: Optional[int] = None,
        follow_up_date: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a lead.

        Mirrors Leads_Create.
        """

        if not campaign_id or not summary:
            return "campaign_id and summary are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads"

        body: dict[str, Any] = {"campaignId": campaign_id, "summary": summary}
        if customer_id is not None:
            body["customerId"] = customer_id
        if location_id is not None:
            body["locationId"] = location_id
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if job_type_id is not None:
            body["jobTypeId"] = job_type_id
        if tag_type_ids is not None:
            body["tagTypeIds"] = list(tag_type_ids)
        if priority is not None:
            body["priority"] = priority
        if call_reason_id is not None:
            body["callReasonId"] = call_reason_id
        if follow_up_date is not None:
            body["followUpDate"] = follow_up_date

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create lead."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_update(
        tenant: int,
        id: int,
        campaign_id: Optional[int] = None,
        priority: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        job_type_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Update a lead.

        Mirrors Leads_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}"

        body: dict[str, Any] = {}
        if campaign_id is not None:
            body["campaignId"] = campaign_id
        if priority is not None:
            body["priority"] = priority
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if job_type_id is not None:
            body["jobTypeId"] = job_type_id

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update lead."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a lead by ID.

        Mirrors Leads_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch lead."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_dismiss(
        tenant: int,
        id: int,
        dismissing_reason_id: int,
        environment: str = "production",
    ) -> str:
        """Dismiss a lead.

        Mirrors Leads_Dismiss.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}/dismiss"

        body = {"dismissingReasonId": dismissing_reason_id}

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to dismiss lead."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_create_follow_up(
        tenant: int,
        id: int,
        follow_up_date: str,
        text: Optional[str] = None,
        pin_to_top: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a follow-up for a lead.

        Mirrors Leads_CreateFollowUp.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}/follow-up"

        body: dict[str, Any] = {"followUpDate": follow_up_date}
        if text is not None:
            body["text"] = text
        if pin_to_top is not None:
            body["pinToTop"] = pin_to_top

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create follow-up."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_get_notes(
        tenant: int,
        id: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get notes for a lead (paginated).

        Mirrors Leads_GetNotes.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}/notes"

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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch lead notes."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_leads_create_note(
        tenant: int,
        id: int,
        text: str,
        pin_to_top: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Create a note on a lead.

        Mirrors Leads_CreateNote.
        """

        if not text:
            return "text is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/leads/{id}/notes"

        body: dict[str, Any] = {"text": text}
        if pin_to_top is not None:
            body["pinToTop"] = pin_to_top

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create lead note."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


