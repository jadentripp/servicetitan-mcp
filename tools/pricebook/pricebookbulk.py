import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_post, make_st_put

__all__ = ["register_pricebook_bulk_tools"]


def register_pricebook_bulk_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_bulk_update(
        tenant: int,
        services: Optional[Sequence[dict[str, Any]]] = None,
        equipment: Optional[Sequence[dict[str, Any]]] = None,
        materials: Optional[Sequence[dict[str, Any]]] = None,
        discount_and_fees: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Bulk update pricebook entities (PricebookBulk_Update)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/pricebook"

        body: dict[str, Any] = {}
        if services is not None:
            body["services"] = list(services)
        if equipment is not None:
            body["equipment"] = list(equipment)
        if materials is not None:
            body["materials"] = list(materials)
        if discount_and_fees is not None:
            body["discountAndFees"] = list(discount_and_fees)

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to perform pricebook bulk update."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_bulk_create(
        tenant: int,
        services: Optional[Sequence[dict[str, Any]]] = None,
        equipment: Optional[Sequence[dict[str, Any]]] = None,
        materials: Optional[Sequence[dict[str, Any]]] = None,
        discount_and_fees: Optional[Sequence[dict[str, Any]]] = None,
        environment: str = "production",
    ) -> str:
        """Bulk create pricebook entities (PricebookBulk_Create)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/pricebook"

        body: dict[str, Any] = {}
        if services is not None:
            body["services"] = list(services)
        if equipment is not None:
            body["equipment"] = list(equipment)
        if materials is not None:
            body["materials"] = list(materials)
        if discount_and_fees is not None:
            body["discountAndFees"] = list(discount_and_fees)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to perform pricebook bulk create."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


