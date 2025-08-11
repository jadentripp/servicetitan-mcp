import json
from typing import Any

from ..utils import get_base_url, make_st_request

__all__ = ["register_dispatch_technician_tracking_tools"]


def register_dispatch_technician_tracking_tools(mcp: Any) -> None:
    @mcp.tool()
    async def dispatch_get_technician_tracking(
        tenant: int,
        technician_id: int,
        appointment_id: int,
        environment: str = "production",
    ) -> str:
        """Get a technician tracking URL for a technician and appointment.

        Mirrors TechnicianTracking_Get.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/dispatch/v2/tenant/{tenant}/technician-tracking"

        params = {"technicianId": int(technician_id), "appointmentId": int(appointment_id)}

        data = await make_st_request(url, params=params)
        if not data:
            return "Unable to fetch technician tracking URL."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


