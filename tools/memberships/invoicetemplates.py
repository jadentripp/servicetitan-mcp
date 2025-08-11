import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_memberships_invoice_templates_tools"]


def register_memberships_invoice_templates_tools(mcp: Any) -> None:
    @mcp.tool()
    async def memberships_invoice_templates_create(
        tenant: int,
        items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Creates a new invoice template.

        Mirrors InvoiceTemplates_Create.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/invoice-templates"

        body: dict[str, Any] = {}
        if items is not None:
            body["items"] = list(items)

        data = await make_st_post(url, json_body=body or None)
        if not data:
            return "Unable to create invoice template."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_invoice_templates_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        created_on: Optional[str] = None,
        created_by_id: Optional[int] = None,
        active: Optional[bool] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Updates an invoice template by ID (patch).

        Mirrors InvoiceTemplates_Update.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/invoice-templates/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if created_on is not None:
            body["createdOn"] = created_on
        if created_by_id is not None:
            body["createdById"] = int(created_by_id)
        if active is not None:
            body["active"] = bool(active)
        if items is not None:
            body["items"] = list(items)

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update invoice template."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_invoice_templates_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Gets an invoice template by ID.

        Mirrors InvoiceTemplates_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/invoice-templates/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch invoice template by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def memberships_invoice_templates_get_list(
        tenant: int,
        ids: str,
        environment: str = "production",
    ) -> str:
        """Gets invoice templates by IDs (comma-separated, max 50).

        Mirrors InvoiceTemplates_GetList.
        """

        if not ids:
            return "'ids' is required (comma-separated, max 50)."

        base_url = get_base_url(environment)
        url = f"{base_url}/memberships/v2/tenant/{tenant}/invoice-templates"

        params = {"ids": ids}
        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch invoice templates list."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


