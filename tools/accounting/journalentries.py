import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_patch

__all__ = ["register_journal_entries_tools"]


def register_journal_entries_tools(mcp: Any) -> None:
    @mcp.tool()
    async def journal_entries_get_list(
        tenant: int,
        ids: Optional[str] = None,
        exported_from: Optional[str] = None,
        exported_to: Optional[str] = None,
        posted_from: Optional[str] = None,
        posted_to: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        exported_by: Optional[str] = None,
        name: Optional[str] = None,
        number_from: Optional[int] = None,
        number_to: Optional[int] = None,
        statuses: Optional[Sequence[str]] = None,
        sync_statuses: Optional[Sequence[str]] = None,
        transaction_posted_from: Optional[str] = None,
        transaction_posted_to: Optional[str] = None,
        business_unit_ids: Optional[str] = None,
        service_agreement_ids: Optional[str] = None,
        customer_name: Optional[str] = None,
        location_name: Optional[str] = None,
        vendor_name: Optional[str] = None,
        inventory_location_name: Optional[str] = None,
        ref_number: Optional[str] = None,
        transaction_types: Optional[Sequence[str]] = None,
        custom_field: Optional[dict[str, str]] = None,
        sort: Optional[str] = None,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get a filtered, paginated list of journal entries."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/journal-entries"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if exported_from:
            params["exportedFrom"] = exported_from
        if exported_to:
            params["exportedTo"] = exported_to
        if posted_from:
            params["postedFrom"] = posted_from
        if posted_to:
            params["postedTo"] = posted_to
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if exported_by:
            params["exportedBy"] = exported_by
        if name:
            params["name"] = name
        if number_from is not None:
            params["numberFrom"] = number_from
        if number_to is not None:
            params["numberTo"] = number_to
        if statuses:
            params["statuses"] = list(statuses)
        if sync_statuses:
            params["syncStatuses"] = list(sync_statuses)
        if transaction_posted_from:
            params["transactionPostedFrom"] = transaction_posted_from
        if transaction_posted_to:
            params["transactionPostedTo"] = transaction_posted_to
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if service_agreement_ids:
            params["serviceAgreementIds"] = service_agreement_ids
        if customer_name:
            params["customerName"] = customer_name
        if location_name:
            params["locationName"] = location_name
        if vendor_name:
            params["vendorName"] = vendor_name
        if inventory_location_name:
            params["inventoryLocationName"] = inventory_location_name
        if ref_number:
            params["refNumber"] = ref_number
        if transaction_types:
            params["transactionTypes"] = list(transaction_types)
        if custom_field:
            for key, value in custom_field.items():
                params[f"customField.{key}"] = value
        if sort:
            params["sort"] = sort
        if page_size is not None:
            params["pageSize"] = page_size
        if page is not None:
            params["page"] = page
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch journal entries."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def journal_entries_update(
        tenant: int,
        id: str,
        status: Optional[str] = None,
        custom_fields: Optional[dict[str, Optional[str]]] = None,
        environment: str = "production",
    ) -> str:
        """Update a journal entry's status and/or custom fields."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/journal-entries/{id}"

        body: dict[str, Any] = {}
        if status is not None:
            body["status"] = status
        if custom_fields is not None:
            body["customFields"] = custom_fields

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update journal entry."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def journal_entries_get_details(
        tenant: int,
        id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get journal entry details aggregated by dimensions (paginated)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/journal-entries/{id}/details"

        params: dict[str, Any] = {}
        if page_size is not None:
            params["pageSize"] = page_size
        if page is not None:
            params["page"] = page
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch journal entry details."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def journal_entries_get_summary(
        tenant: int,
        id: str,
        page_size: Optional[int] = None,
        page: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get journal entry summary aggregated by account and business unit (paginated)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/journal-entries/{id}/summary"

        params: dict[str, Any] = {}
        if page_size is not None:
            params["pageSize"] = page_size
        if page is not None:
            params["page"] = page
        if include_total:
            params["includeTotal"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch journal entry summary."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def journal_entries_sync_update(
        tenant: int,
        id: str,
        sync_status: str,
        version_id: Optional[int] = None,
        message: Optional[str] = None,
        custom_fields: Optional[dict[str, Optional[str]]] = None,
        environment: str = "production",
    ) -> str:
        """Update a journal entry sync state."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/journal-entries/{id}/sync"

        body: dict[str, Any] = {"syncStatus": sync_status}
        if version_id is not None:
            body["versionId"] = version_id
        if message is not None:
            body["message"] = message
        if custom_fields is not None:
            body["customFields"] = custom_fields

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update journal entry sync status."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


