import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch, make_st_delete

__all__ = ["register_pricebook_categories_tools"]


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


def register_pricebook_categories_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_categories_create(
        tenant: int,
        name: str,
        category_type: str,
        active: Optional[bool] = None,
        description: Optional[str] = None,
        parent_id: Optional[int] = None,
        position: Optional[int] = None,
        image: Optional[str] = None,
        business_unit_ids: Optional[Sequence[int]] = None,
        sku_images: Optional[Sequence[str]] = None,
        sku_videos: Optional[Sequence[str]] = None,
        environment: str = "production",
    ) -> str:
        """Create a new pricebook category.

        Mirrors Categories_Create.
        - category_type: Services|Materials
        """

        mapped_type = _normalize_enum(category_type, {"Services", "Materials"})
        if not mapped_type:
            return "Invalid 'category_type'. Use one of: Services, Materials."

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/categories"

        body: dict[str, Any] = {
            "name": name,
            "categoryType": mapped_type,
        }
        if active is not None:
            body["active"] = bool(active)
        if description is not None:
            body["description"] = description
        if parent_id is not None:
            body["parentId"] = int(parent_id)
        if position is not None:
            body["position"] = int(position)
        if image is not None:
            body["image"] = image
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)
        if sku_images is not None:
            body["skuImages"] = list(sku_images)
        if sku_videos is not None:
            body["skuVideos"] = list(sku_videos)

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_categories_get_list(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        category_type: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of pricebook categories.

        Mirrors Categories_GetList.
        - category_type: Services|Materials
        - active: True|Any|False
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/categories"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort
        if category_type is not None:
            mapped = _normalize_enum(category_type, {"Services", "Materials"})
            if not mapped:
                return "Invalid 'category_type'. Use one of: Services, Materials."
            params["categoryType"] = mapped
        if active is not None:
            mapped_active = _normalize_tristate(active)
            if mapped_active == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = mapped_active
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
            return "Unable to fetch categories."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_categories_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get category details by ID.

        Mirrors Categories_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/categories/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch category by ID."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_categories_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        active: Optional[bool] = None,
        description: Optional[str] = None,
        parent_id: Optional[int] = None,
        position: Optional[int] = None,
        image: Optional[str] = None,
        category_type: Optional[str] = None,
        business_unit_ids: Optional[Sequence[int]] = None,
        sku_images: Optional[Sequence[str]] = None,
        sku_videos: Optional[Sequence[str]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing pricebook category.

        Mirrors Categories_Update.
        - category_type (optional): Services|Materials
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/categories/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if active is not None:
            body["active"] = bool(active)
        if description is not None:
            body["description"] = description
        if parent_id is not None:
            body["parentId"] = int(parent_id)
        if position is not None:
            body["position"] = int(position)
        if image is not None:
            body["image"] = image
        if category_type is not None:
            mapped = _normalize_enum(category_type, {"Services", "Materials"})
            if not mapped:
                return "Invalid 'category_type'. Use one of: Services, Materials."
            body["categoryType"] = mapped
        if business_unit_ids is not None:
            body["businessUnitIds"] = list(business_unit_ids)
        if sku_images is not None:
            body["skuImages"] = list(sku_images)
        if sku_videos is not None:
            body["skuVideos"] = list(sku_videos)

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_categories_delete(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Delete a pricebook category by ID.

        Mirrors Categories_Delete.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/categories/{id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete category."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


