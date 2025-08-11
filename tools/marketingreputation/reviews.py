import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request

__all__ = ["register_marketingreputation_reviews_tools"]


def register_marketingreputation_reviews_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingreputation_reviews_get(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        search: Optional[str] = None,
        report_type: Optional[int] = None,
        sort: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        created_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        from_date: Optional[str] = None,
        to_date: Optional[str] = None,
        response_types: Optional[Sequence[str]] = None,
        location_ids: Optional[Sequence[int]] = None,
        sources: Optional[Sequence[str]] = None,
        review_statuses: Optional[Sequence[str]] = None,
        technician_ids: Optional[Sequence[int]] = None,
        campaign_ids: Optional[Sequence[int]] = None,
        from_rating: Optional[float] = None,
        to_rating: Optional[float] = None,
        include_reviews_without_location: bool = False,
        include_reviews_without_campaign: bool = False,
        include_reviews_without_technician: bool = False,
        environment: str = "production",
    ) -> str:
        """Gets a paginated list of reviews with filters.

        Mirrors marketingreputation/v2 reviews.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingreputation/v2/tenant/{tenant}/reviews"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if search:
            params["search"] = search
        if report_type is not None:
            params["reportType"] = int(report_type)
        if sort:
            params["sort"] = sort
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if created_before:
            params["createdBefore"] = created_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if from_date:
            params["fromDate"] = from_date
        if to_date:
            params["toDate"] = to_date
        if response_types:
            # API expects array; httpx encodes list as repeated query params
            params["responseTypes"] = list(response_types)
        if location_ids:
            params["locationIds"] = [int(x) for x in location_ids]
        if sources:
            params["sources"] = list(sources)
        if review_statuses:
            params["reviewStatuses"] = list(review_statuses)
        if technician_ids:
            params["technicianIds"] = [int(x) for x in technician_ids]
        if campaign_ids:
            params["campaignIds"] = [int(x) for x in campaign_ids]
        if from_rating is not None:
            params["fromRating"] = float(from_rating)
        if to_rating is not None:
            params["toRating"] = float(to_rating)
        if include_reviews_without_location:
            params["includeReviewsWithoutLocation"] = True
        if include_reviews_without_campaign:
            params["includeReviewsWithoutCampaign"] = True
        if include_reviews_without_technician:
            params["includeReviewsWithoutTechnician"] = True

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch reviews."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


