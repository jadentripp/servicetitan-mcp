import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_put

__all__ = ["register_settings_employees_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_settings_employees_tools(mcp: Any) -> None:
    @mcp.tool()
    async def settings_employees_get_list(
        tenant: int,
        ids: Optional[str] = None,
        user_ids: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
        active: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of employees. Mirrors Employees_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/employees"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if user_ids:
            params["userIds"] = user_ids
        if name:
            params["name"] = name
        if email:
            params["email"] = email
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
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
            return "Unable to fetch employees."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_employees_create(
        tenant: int,
        name: str,
        email: str,
        account_creation_method: str,
        role_id: int,
        positions: Sequence[str],
        mobile_phone_number: Optional[str] = None,
        phone_number: Optional[str] = None,
        login: Optional[str] = None,
        password: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        aad_user_id: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new employee. Mirrors Employees_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/employees"

        body: dict[str, Any] = {
            "name": name,
            "email": email,
            "accountCreationMethod": account_creation_method,
            "roleId": int(role_id),
            "positions": list(positions),
        }
        if mobile_phone_number is not None:
            body["mobilePhoneNumber"] = mobile_phone_number
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if login is not None:
            body["login"] = login
        if password is not None:
            body["password"] = password
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if aad_user_id is not None:
            body["aadUserId"] = aad_user_id
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create employee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_employees_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        mobile_phone_number: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        login: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        role_id: Optional[int] = None,
        positions: Optional[Sequence[str]] = None,
        aad_user_id: Optional[str] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        account_locked: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update an employee. Mirrors Employees_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/employees/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if mobile_phone_number is not None:
            body["mobilePhoneNumber"] = mobile_phone_number
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if email is not None:
            body["email"] = email
        if login is not None:
            body["login"] = login
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if role_id is not None:
            body["roleId"] = role_id
        if positions is not None:
            body["positions"] = list(positions)
        if aad_user_id is not None:
            body["aadUserId"] = aad_user_id
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if account_locked is not None:
            body["accountLocked"] = account_locked

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update employee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_employees_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get an employee by ID. Mirrors Employees_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/employees/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch employee."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_employees_account_actions(
        tenant: int,
        id: int,
        action: str,
        environment: str = "production",
    ) -> str:
        """Perform account action for an employee. Mirrors Employees_AccountActions."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/employees/{id}/account-actions"

        body = {"action": action}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to perform employee account action."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



