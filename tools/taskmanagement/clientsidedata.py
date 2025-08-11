import json
from typing import Any

from ..utils import get_base_url, make_st_request

__all__ = ["register_taskmanagement_client_side_data_tools"]


def register_taskmanagement_client_side_data_tools(mcp: Any) -> None:
    @mcp.tool()
    async def taskmanagement_client_side_data_get(
        tenant: int,
        environment: str = "production",
    ) -> str:
        """Get client-side data (ClientSideData_Get)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/taskmanagement/v2/tenant/{tenant}/data"

        data = await make_st_request(url)
        if not data:
            return "Unable to fetch task management client-side data."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


