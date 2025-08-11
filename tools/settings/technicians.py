import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_put

__all__ = ["register_settings_technicians_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_settings_technicians_tools(mcp: Any) -> None:
    @mcp.tool()
    async def settings_technicians_get_list(
        tenant: int,
        ids: Optional[str] = None,
        user_ids: Optional[str] = None,
        name: Optional[str] = None,
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
        """Get a paginated list of technicians. Mirrors Technicians_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/technicians"

        params: dict[str, Any] = {}
        if ids:
            params["ids"] = ids
        if user_ids:
            params["userIds"] = user_ids
        if name:
            params["name"] = name
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
            return "Unable to fetch technicians."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_technicians_create(
        tenant: int,
        name: str,
        account_creation_method: str,
        role_id: int,
        positions: Sequence[str],
        license_type: str,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        login: Optional[str] = None,
        password: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        aad_user_id: Optional[str] = None,
        team: Optional[str] = None,
        daily_goal: Optional[float] = None,
        burden_rate: Optional[float] = None,
        bio: Optional[str] = None,
        memo: Optional[str] = None,
        job_filter: Optional[str] = None,
        job_history_date_filter: Optional[str] = None,
        home: Optional[dict[str, Any]] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new technician. Mirrors Technicians_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/technicians"

        body: dict[str, Any] = {
            "name": name,
            "accountCreationMethod": account_creation_method,
            "roleId": int(role_id),
            "positions": list(positions),
            "licenseType": license_type,
        }
        if phone_number is not None:
            body["phoneNumber"] = phone_number
        if email is not None:
            body["email"] = email
        if login is not None:
            body["login"] = login
        if password is not None:
            body["password"] = password
        if business_unit_id is not None:
            body["businessUnitId"] = business_unit_id
        if aad_user_id is not None:
            body["aadUserId"] = aad_user_id
        if team is not None:
            body["team"] = team
        if daily_goal is not None:
            body["dailyGoal"] = daily_goal
        if burden_rate is not None:
            body["burdenRate"] = burden_rate
        if bio is not None:
            body["bio"] = bio
        if memo is not None:
            body["memo"] = memo
        if job_filter is not None:
            body["jobFilter"] = job_filter
        if job_history_date_filter is not None:
            body["jobHistoryDateFilter"] = job_history_date_filter
        if home is not None:
            body["home"] = dict(home)
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create technician."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_technicians_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        login: Optional[str] = None,
        business_unit_id: Optional[int] = None,
        role_id: Optional[int] = None,
        positions: Optional[Sequence[str]] = None,
        aad_user_id: Optional[str] = None,
        license_type: Optional[str] = None,
        team: Optional[str] = None,
        daily_goal: Optional[float] = None,
        burden_rate: Optional[float] = None,
        bio: Optional[str] = None,
        memo: Optional[str] = None,
        job_filter: Optional[str] = None,
        job_history_date_filter: Optional[str] = None,
        home: Optional[dict[str, Any]] = None,
        custom_fields: Optional[Sequence[dict[str, Any]]] = None,
        account_locked: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update a technician. Mirrors Technicians_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/technicians/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
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
        if license_type is not None:
            body["licenseType"] = license_type
        if team is not None:
            body["team"] = team
        if daily_goal is not None:
            body["dailyGoal"] = daily_goal
        if burden_rate is not None:
            body["burdenRate"] = burden_rate
        if bio is not None:
            body["bio"] = bio
        if memo is not None:
            body["memo"] = memo
        if job_filter is not None:
            body["jobFilter"] = job_filter
        if job_history_date_filter is not None:
            body["jobHistoryDateFilter"] = job_history_date_filter
        if home is not None:
            body["home"] = dict(home)
        if custom_fields is not None:
            body["customFields"] = list(custom_fields)
        if account_locked is not None:
            body["accountLocked"] = account_locked

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update technician."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_technicians_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a technician by ID. Mirrors Technicians_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/technicians/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch technician."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def settings_technicians_account_actions(
        tenant: int,
        id: int,
        action: str,
        license_type: Optional[str] = None,
        truck_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Perform account action for a technician. Mirrors Technicians_AccountActions."""

        base_url = get_base_url(environment)
        url = f"{base_url}/settings/v2/tenant/{tenant}/technicians/{id}/account-actions"

        body: dict[str, Any] = {"action": action}
        if license_type is not None:
            body["licenseType"] = license_type
        if truck_id is not None:
            body["truckId"] = int(truck_id)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to perform technician account action."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



