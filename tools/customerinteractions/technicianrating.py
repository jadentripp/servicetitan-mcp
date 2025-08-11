import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_put

__all__ = ["register_customer_interactions_technician_rating_tools"]


def register_customer_interactions_technician_rating_tools(mcp: Any) -> None:
    @mcp.tool()
    async def customer_interactions_update_technician_rating(
        tenant: int,
        technician_id: int,
        job_id: int,
        value: float,
        environment: str = "production",
    ) -> str:
        """Create or update a rating (0-10) for a technician on a specific job.

        Endpoint: /customer-interactions/v2/tenant/{tenant}/technician-rating/technician/{technicianId}/job/{jobId}
        Method: PUT
        """

        # Guardrails
        if value is None:
            return "Rating value is required."
        try:
            numeric_value = float(value)
        except Exception:
            return "Rating value must be a number."
        if numeric_value < 0 or numeric_value > 10:
            return "Rating value must be between 0 and 10."

        base_url = get_base_url(environment)
        url = (
            f"{base_url}/customer-interactions/v2/tenant/{tenant}/technician-rating/technician/{technician_id}/job/{job_id}"
        )

        body = {"value": numeric_value}

        data = await make_st_put(url, json_body=body)
        if data is None:
            return "Unable to create or update technician rating."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)



