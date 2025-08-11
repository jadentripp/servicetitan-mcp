import json
from typing import Any, Optional, Sequence

from ..utils import (
    get_base_url,
    make_st_request,
    make_st_post,
    make_st_put,
    make_st_patch,
    make_st_delete,
)

__all__ = ["register_sales_estimates_tools"]


def _normalize_active(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[normalized]
    return None


def register_sales_estimates_tools(mcp: Any) -> None:
    @mcp.tool()
    async def sales_estimates_get_list(
        tenant: int,
        job_id: Optional[int] = None,
        project_id: Optional[int] = None,
        job_number: Optional[str] = None,
        total_greater: Optional[float] = None,
        total_less: Optional[float] = None,
        sold_by_id: Optional[int] = None,
        sold_by_employee_id: Optional[int] = None,
        ids: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sold_after: Optional[str] = None,
        sold_before: Optional[str] = None,
        status: Optional[str] = None,
        active: Optional[str] = None,
        order_by: Optional[str] = None,
        order_by_direction: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        location_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Retrieve a paginated list of estimates with filters. Mirrors Estimates_GetList."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates"

        params: dict[str, Any] = {}
        if job_id is not None:
            params["jobId"] = job_id
        if project_id is not None:
            params["projectId"] = project_id
        if job_number:
            params["jobNumber"] = job_number
        if total_greater is not None:
            params["totalGreater"] = total_greater
        if total_less is not None:
            params["totalLess"] = total_less
        if sold_by_id is not None:
            params["soldById"] = sold_by_id
        if sold_by_employee_id is not None:
            params["soldByEmployeeId"] = sold_by_employee_id
        if ids:
            params["ids"] = ids
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sold_after:
            params["soldAfter"] = sold_after
        if sold_before:
            params["soldBefore"] = sold_before
        if status:
            params["status"] = status
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
        if order_by:
            params["orderBy"] = order_by
        if order_by_direction:
            params["orderByDirection"] = order_by_direction
        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if location_id is not None:
            params["locationId"] = location_id

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch estimates."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_create(
        tenant: int,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        tax: Optional[float] = None,
        status: Optional[str] = None,
        review_status: Optional[str] = None,
        sold_by: Optional[int] = None,
        is_recommended: Optional[bool] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        external_links: Optional[Sequence[dict[str, Any]]] = None,
        use_default_project_labels: Optional[bool] = None,
        job_id: Optional[int] = None,
        project_id: Optional[int] = None,
        location_id: Optional[int] = None,
        environment: str = "production",
    ) -> str:
        """Create a new estimate. Mirrors Estimates_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if summary is not None:
            body["summary"] = summary
        if tax is not None:
            body["tax"] = tax
        if status is not None:
            body["status"] = status
        if review_status is not None:
            body["reviewStatus"] = review_status
        if sold_by is not None:
            body["soldBy"] = sold_by
        if is_recommended is not None:
            body["isRecommended"] = is_recommended
        if items is not None:
            body["items"] = list(items)
        if external_links is not None:
            body["externalLinks"] = list(external_links)
        if use_default_project_labels is not None:
            body["useDefaultProjectLabels"] = use_default_project_labels
        if job_id is not None:
            body["jobId"] = job_id
        if project_id is not None:
            body["projectId"] = project_id
        if location_id is not None:
            body["locationId"] = location_id

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_get_items(
        tenant: int,
        estimate_id: Optional[int] = None,
        ids: Optional[str] = None,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        environment: str = "production",
    ) -> str:
        """Get estimate items (paginated). Mirrors Estimates_GetItems."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/items"

        params: dict[str, Any] = {}
        if estimate_id is not None:
            params["estimateId"] = estimate_id
        if ids:
            params["ids"] = ids
        if active is not None:
            normalized = _normalize_active(active)
            if not normalized:
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized
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

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch estimate items."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_update(
        tenant: int,
        id: int,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        tax: Optional[float] = None,
        status: Optional[str] = None,
        review_status: Optional[str] = None,
        sold_by: Optional[int] = None,
        is_recommended: Optional[bool] = None,
        items: Optional[Sequence[dict[str, Any]]] = None,
        external_links: Optional[Sequence[dict[str, Any]]] = None,
        use_default_project_labels: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Update an estimate by ID. Mirrors Estimates_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}"

        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if summary is not None:
            body["summary"] = summary
        if tax is not None:
            body["tax"] = tax
        if status is not None:
            body["status"] = status
        if review_status is not None:
            body["reviewStatus"] = review_status
        if sold_by is not None:
            body["soldBy"] = sold_by
        if is_recommended is not None:
            body["isRecommended"] = is_recommended
        if items is not None:
            body["items"] = list(items)
        if external_links is not None:
            body["externalLinks"] = list(external_links)
        if use_default_project_labels is not None:
            body["useDefaultProjectLabels"] = use_default_project_labels

        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to update estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_get(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Get a single estimate by ID. Mirrors Estimates_Get."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_dismiss(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Dismiss an estimate. Mirrors Estimates_Dismiss."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}/dismiss"

        data = await make_st_post(url)
        if not data:
            return "Unable to dismiss estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_put_item(
        tenant: int,
        id: int,
        item: dict[str, Any],
        environment: str = "production",
    ) -> str:
        """Create or update a single estimate item. Mirrors Estimates_PutItem."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}/items"

        body = dict(item or {})
        data = await make_st_put(url, json_body=body)
        if not data:
            return "Unable to put estimate item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_delete_item(
        tenant: int,
        id: int,
        item_id: int,
        environment: str = "production",
    ) -> str:
        """Delete an estimate item by ID. Mirrors Estimates_DeleteItem."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}/items/{item_id}"

        data = await make_st_delete(url)
        if data is None:
            return "Unable to delete estimate item."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_sell(
        tenant: int,
        id: int,
        sold_by: int,
        environment: str = "production",
    ) -> str:
        """Sell an estimate. Mirrors Estimates_Sell."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}/sell"

        body = {"soldBy": int(sold_by)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to sell estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def sales_estimates_unsell(
        tenant: int,
        id: int,
        environment: str = "production",
    ) -> str:
        """Unsell an estimate. Mirrors Estimates_Unsell."""

        base_url = get_base_url(environment)
        url = f"{base_url}/sales/v2/tenant/{tenant}/estimates/{id}/unsell"

        data = await make_st_post(url)
        if not data:
            return "Unable to unsell estimate."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



