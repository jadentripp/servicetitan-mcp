import json
from typing import Any, Sequence

from ..utils import get_base_url, make_st_post, make_st_delete

__all__ = ["register_crm_bulk_tags_tools"]


def register_crm_bulk_tags_tools(mcp: Any) -> None:
    """Register CRM Bulk Tags tools (add/remove)."""

    @mcp.tool()
    async def crm_bulk_tags_add(
        tenant: int,
        customer_ids: Sequence[int],
        tag_type_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Add multiple tags to more than one customer.

        Mirrors BulkTags_AddTags (POST /crm/v2/tenant/{tenant}/tags).
        """

        if not customer_ids or not tag_type_ids:
            return "customer_ids and tag_type_ids are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/tags"

        body = {
            "customerIds": list(customer_ids),
            "tagTypeIds": list(tag_type_ids),
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to add bulk tags."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def crm_bulk_tags_remove(
        tenant: int,
        customer_ids: Sequence[int],
        tag_type_ids: Sequence[int],
        environment: str = "production",
    ) -> str:
        """Remove multiple tags from more than one customer.

        Mirrors BulkTags_RemoveTags (DELETE /crm/v2/tenant/{tenant}/tags with JSON body).
        """

        if not customer_ids or not tag_type_ids:
            return "customer_ids and tag_type_ids are required."

        base_url = get_base_url(environment)
        url = f"{base_url}/crm/v2/tenant/{tenant}/tags"

        body = {
            "customerIds": list(customer_ids),
            "tagTypeIds": list(tag_type_ids),
        }

        data = await make_st_delete(url, json_body=body)
        if data is None:
            return "Unable to remove bulk tags."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


