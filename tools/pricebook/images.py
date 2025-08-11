import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_post, make_st_request

__all__ = ["register_pricebook_images_tools"]


def register_pricebook_images_tools(mcp: Any) -> None:
    @mcp.tool()
    async def pricebook_images_post(
        tenant: int,
        file: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Upload an image to temporary storage.

        Mirrors Images_Post.
        Note: API expects binary file upload; this helper passes the string as-is.
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/images"

        body: dict[str, Any] = {}
        if file is not None:
            body["file"] = file

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to upload image."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def pricebook_images_get(
        tenant: int,
        path: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a signed URL for a stored image path.

        Mirrors Images_Get (returns redirect in API; here we return the JSON if any).
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/pricebook/v2/tenant/{tenant}/images"

        params: dict[str, Any] = {}
        if path:
            params["path"] = path

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to get image path."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


