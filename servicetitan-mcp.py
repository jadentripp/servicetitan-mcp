import os
import sys
import logging
from dotenv import load_dotenv

from mcp.server.fastmcp import FastMCP
from tools import register_all_tools, register_selected_tools

# Load environment variables from a local .env if present (dev convenience)
load_dotenv()

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    stream=sys.stderr,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

# Initialize FastMCP server (stdio by default)
mcp = FastMCP("servicetitan-mcp")

# Register tools: allow selective enablement via env vars
include_groups = os.environ.get("SERVICETITAN_MCP_INCLUDE_GROUPS")
exclude_groups = os.environ.get("SERVICETITAN_MCP_EXCLUDE_GROUPS")

if include_groups or exclude_groups:
    selected = register_selected_tools(
        mcp,
        include_groups=(include_groups.split(",") if include_groups else None),
        exclude_groups=(exclude_groups.split(",") if exclude_groups else None),
    )
    logging.info("Registered tool groups: %s", ", ".join(selected))
else:
    register_all_tools(mcp)

if __name__ == "__main__":
    # Basic environment validation and transport selection
    if not os.environ.get("SERVICETITAN_ACCESS_TOKEN"):
        logging.warning(
            "SERVICETITAN_ACCESS_TOKEN is not set. ServiceTitan API calls will fail."
        )

    # Start the MCP server (stdio only)
    mcp.run(transport="stdio")