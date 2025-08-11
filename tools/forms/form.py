import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request

__all__ = ["register_forms_form_tools"]


def register_forms_form_tools(mcp: Any) -> None:
    @mcp.tool()
    async def forms_get_forms(
        tenant: int,
        has_conditional_logic: Optional[bool] = None,
        has_triggers: Optional[bool] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        ids: Optional[str] = None,
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
        """Retrieve form metadata (paginated) with filters.

        Mirrors Form_GetForms.
        - status: Any | Published | Unpublished (case-insensitive)
        - active: True | Any | False (case-insensitive)
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/forms/v2/tenant/{tenant}/forms"

        params: dict[str, Any] = {}
        if has_conditional_logic is not None:
            params["hasConditionalLogic"] = bool(has_conditional_logic)
        if has_triggers is not None:
            params["hasTriggers"] = bool(has_triggers)
        if name:
            params["name"] = name
        if status:
            s = status.strip().lower()
            if s in {"any", "published", "unpublished"}:
                params["status"] = {"any": "Any", "published": "Published", "unpublished": "Unpublished"}[s]
            else:
                return "Invalid 'status'. Use one of: Any, Published, Unpublished."
        if ids:
            params["ids"] = ids
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
            return "Unable to fetch forms."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


