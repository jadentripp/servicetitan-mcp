import os
import time
import logging
from typing import Any, Optional

import httpx
from importlib.metadata import PackageNotFoundError, version as get_version

PRODUCTION_BASE_URL = "https://api.servicetitan.io"
INTEGRATION_BASE_URL = "https://api-integration.servicetitan.io"
LOGGER = logging.getLogger(__name__)

try:
    USER_AGENT = f"servicetitan-mcp/{get_version('servicetitan-mcp')}"
except PackageNotFoundError:
    USER_AGENT = "servicetitan-mcp"


def get_base_url(environment: str) -> str:
    env_normalized = (environment or "").strip().lower()
    if env_normalized in {"integration", "int", "test"}:
        return INTEGRATION_BASE_URL
    return PRODUCTION_BASE_URL


_TOKEN_CACHE: dict[str, tuple[str, float]] = {}


def _resolve_env_key_from_url(url: Optional[str]) -> str:
    if not url:
        return "production"
    if "api-integration.servicetitan.io" in url:
        return "integration"
    return "production"


def _fetch_access_token(env_key: str) -> Optional[str]:
    # Check cache
    cached = _TOKEN_CACHE.get(env_key)
    now = time.time()
    if cached and cached[1] > now:
        return cached[0]

    client_id = os.environ.get("SERVICETITAN_CLIENT_ID")
    client_secret = os.environ.get("SERVICETITAN_CLIENT_SECRET")
    if not client_id or not client_secret:
        return None

    token_url = (
        "https://auth-integration.servicetitan.io/connect/token"
        if env_key == "integration"
        else "https://auth.servicetitan.io/connect/token"
    )

    try:
        with httpx.Client(timeout=10.0, http2=True) as client:
            resp = client.post(
                token_url,
                data={
                    "grant_type": "client_credentials",
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            resp.raise_for_status()
            data = resp.json()
            access_token = data.get("access_token")
            expires_in = int(data.get("expires_in", 900))
            if access_token:
                # cache with 60s safety buffer
                _TOKEN_CACHE[env_key] = (access_token, now + max(expires_in - 60, 300))
                return access_token
    except Exception:
        LOGGER.error("Failed to fetch access token for %s", env_key, exc_info=True)
        return None

    return None


def build_headers(url: Optional[str] = None) -> dict[str, str]:
    headers: dict[str, str] = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }

    # Always fetch via client credentials
    env_key = _resolve_env_key_from_url(url)
    access_token = _fetch_access_token(env_key) or None
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"

    app_key = os.environ.get("SERVICETITAN_APP_KEY")
    if app_key:
        headers["ST-App-Key"] = app_key

    return headers


async def make_st_request(url: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any] | None:
    headers = build_headers(url)

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            LOGGER.error("GET %s failed", url, exc_info=True)
            return None


async def make_st_post(url: str, json_body: Any | None = None, params: Optional[dict[str, Any]] = None) -> dict[str, Any] | None:
    headers = build_headers(url)

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.post(url, headers=headers, params=params, json=json_body, timeout=30.0)
            response.raise_for_status()
            return response.json() if response.content else {"status": response.status_code}
        except Exception:
            LOGGER.error("POST %s failed", url, exc_info=True)
            return None


async def make_st_patch(url: str, json_body: Any | None = None, params: Optional[dict[str, Any]] = None) -> dict[str, Any] | None:
    headers = build_headers(url)

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.patch(url, headers=headers, params=params, json=json_body, timeout=30.0)
            response.raise_for_status()
            return response.json() if response.content else {"status": response.status_code}
        except Exception:
            LOGGER.error("PATCH %s failed", url, exc_info=True)
            return None


async def make_st_put(url: str, json_body: Any | None = None, params: Optional[dict[str, Any]] = None) -> dict[str, Any] | None:
    headers = build_headers(url)

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.put(url, headers=headers, params=params, json=json_body, timeout=30.0)
            response.raise_for_status()
            return response.json() if response.content else {"status": response.status_code}
        except Exception:
            LOGGER.error("PUT %s failed", url, exc_info=True)
            return None


async def make_st_delete(
    url: str,
    params: Optional[dict[str, Any]] = None,
    json_body: Any | None = None,
) -> dict[str, Any] | None:
    headers = build_headers(url)

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.delete(
                url, headers=headers, params=params, json=json_body, timeout=30.0
            )
            response.raise_for_status()
            return response.json() if response.content else {"status": response.status_code}
        except Exception:
            LOGGER.error("DELETE %s failed", url, exc_info=True)
            return None


async def make_st_get_bytes(url: str, params: Optional[dict[str, Any]] = None) -> bytes | None:
    headers = build_headers(url)
    # Override Accept for binary endpoints
    headers["Accept"] = "application/octet-stream"

    async with httpx.AsyncClient(http2=True, follow_redirects=False) as client:
        try:
            response = await client.get(url, headers=headers, params=params, timeout=60.0)
            response.raise_for_status()
            return response.content
        except Exception:
            LOGGER.error("GET(bytes) %s failed", url, exc_info=True)
            return None


