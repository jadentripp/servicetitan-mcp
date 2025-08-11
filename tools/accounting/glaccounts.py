import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_glaccounts_tools"]


def register_glaccounts_tools(mcp: Any) -> None:
    @mcp.tool()
    async def gl_accounts_get_list(
        tenant: int,
        ids: Optional[str] = None,
        names: Optional[str] = None,
        numbers: Optional[str] = None,
        types: Optional[str] = None,
        subtypes: Optional[str] = None,
        description: Optional[str] = None,
        source: Optional[str] = None,
        active: Optional[str] = None,
        is_intacct_group: Optional[bool] = None,
        is_intacct_bank_account: Optional[bool] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Retrieve GL accounts with filters and pagination."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/gl-accounts"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if names:
            params["names"] = names
        if numbers:
            params["numbers"] = numbers
        if types:
            params["types"] = types
        if subtypes:
            params["subtypes"] = subtypes
        if description:
            params["description"] = description
        if source:
            params["source"] = source
        if active is not None:
            params["active"] = active
        if is_intacct_group is not None:
            params["isIntacctGroup"] = is_intacct_group
        if is_intacct_bank_account is not None:
            params["isIntacctBankAccount"] = is_intacct_bank_account
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
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
            return "Unable to fetch GL accounts."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def gl_accounts_create_account(
        tenant: int,
        name: Optional[str] = None,
        number: Optional[str] = None,
        description: Optional[str] = None,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a new GL account."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/gl-accounts"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if number is not None:
            body["number"] = number
        if description is not None:
            body["description"] = description
        if type is not None:
            body["type"] = type
        if subtype is not None:
            body["subtype"] = subtype

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create GL account."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def gl_account_types_get_list(
        tenant: int,
        ids: Optional[str] = None,
        names: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Retrieve GL account types with filters and pagination."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/gl-accounts/types"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if names:
            params["names"] = names
        if active is not None:
            params["active"] = active
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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch GL account types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def gl_accounts_update_account(
        tenant: int,
        account_id: int,
        name: Optional[str] = None,
        number: Optional[str] = None,
        description: Optional[str] = None,
        type: Optional[str] = None,
        subtype: Optional[str] = None,
        active: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing GL account by ID (can also deactivate)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/gl-accounts/{account_id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if number is not None:
            body["number"] = number
        if description is not None:
            body["description"] = description
        if type is not None:
            body["type"] = type
        if subtype is not None:
            body["subtype"] = subtype
        if active is not None:
            body["active"] = active

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update GL account."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def gl_accounts_get_account(
        tenant: int,
        account_id: int,
        environment: str = "production",
    ) -> str:
        """Retrieve a single GL account by ID."""

        base_url = get_base_url(environment)
        url = f"{base_url}/accounting/v2/tenant/{tenant}/gl-accounts/{account_id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch GL account."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



