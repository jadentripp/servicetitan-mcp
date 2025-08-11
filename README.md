# ServiceTitan MCP Server

An MCP server that exposes ServiceTitan APIs as tools for MCP clients. Built with FastMCP, with coverage across all ServiceTitan APIs.

## Requirements
- Python 3.12+
- Dependencies: mcp[cli], httpx, python-dotenv

## Install
Using uv (recommended):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv add "mcp[cli]" httpx python-dotenv
```

## Quick start
```bash
uv run servicetitan-mcp.py
```

## Configuration
- Environment vars:
  - `SERVICETITAN_CLIENT_ID` (required)
  - `SERVICETITAN_CLIENT_SECRET` (required)
  - `SERVICETITAN_APP_KEY` (optional)
  - `SERVICETITAN_TENANT_ID` (optional; used by some tools as a default)
- Tools accept `environment`: "production" (default) or "integration"/"int"/"test"; base URL selection is automatic.

### .env (local dev)
This server auto-loads a local `.env` file if present.

```bash
# Create .env
cat > .env << 'EOF'
SERVICETITAN_CLIENT_ID=your_client_id_here
SERVICETITAN_CLIENT_SECRET=your_client_secret_here
SERVICETITAN_APP_KEY=your_app_key_here
SERVICETITAN_TENANT_ID=your_tenant_id_here
# Optional: limit tool groups (comma-separated, case-insensitive)
# SERVICETITAN_MCP_INCLUDE_GROUPS=crm,dispatch,inventory
# SERVICETITAN_MCP_EXCLUDE_GROUPS=marketing,marketingads,marketingreputation
EOF

# Ensure it’s ignored by git
echo ".env" >> .gitignore
```


## Client integration
This server uses the MCP stdio transport. Refer to your MCP client's documentation for configuring a local stdio server.

Typical client settings:
- Command: `uv`
- Args: `["--directory", "/ABSOLUTE/PATH/TO/servicetitan-mcp", "run", "servicetitan-mcp.py"]`
- Env: set `SERVICETITAN_CLIENT_ID`, `SERVICETITAN_CLIENT_SECRET`, and optional `SERVICETITAN_APP_KEY`
- Use absolute paths if the client runs in a GUI context

 

## Authorization

Provide credentials via environment variables:
- `SERVICETITAN_APP_KEY` (optional)

Tools accept `environment="production"|"integration"`, switching base URLs automatically.

## ServiceTitan developer portal quickstart

Use the ServiceTitan Developer Portal to obtain credentials and discover APIs:

- Developer Portal: https://developer.servicetitan.io/
- Docs (Getting Started): https://developer.servicetitan.io/docs/welcome
- API Reference: https://developer.servicetitan.io/apis

### Environments
- Integration APIs: `https://api-integration.servicetitan.io` | Token: `https://auth-integration.servicetitan.io/connect/token`
- Production APIs: `https://api.servicetitan.io` | Token: `https://auth.servicetitan.io/connect/token`

### Using with this MCP server
- Select environment per tool call via `environment` (default: production) or set per session in your client config
- Include your tenant ID in tool parameters where required (e.g., `/v2/tenant/{tenant}/...`)

Tip: Develop and test in Integration first, then switch credentials and base URLs to go live.

## What’s included
The server auto-registers tool groups from `tools/__init__.py`, including:
- Accounting, CRM, Customer Interactions, Dispatch, Equipment Systems
- Forms, Inventory, Job Booking, Job Planning & Management (JPM)
- Marketing, Marketing Ads, Marketing Reputation, Reporting
- Memberships, Payroll, Pricebook, Sales & Estimates, Scheduling Pro
- Service Agreements, Task Management, Timesheets, Telecom, Settings

Conventions:
- Base URL via `tools.utils.get_base_url(environment)`
- HTTP via `make_st_request`, `make_st_post`, `make_st_put`, `make_st_patch`, `make_st_delete`
- Include query params only when provided; booleans only when True
- JSON pretty-print on success; short error strings on failure
- Tri-state normalization for fields like `active` where applicable

## Example tools
- Timesheets export:
  - `timesheets_export_activities(tenant, from_token?, include_recent_changes?, environment?)`
  - `timesheets_export_activity_categories(tenant, from_token?, include_recent_changes?, environment?)`
  - `timesheets_export_activity_types(tenant, from_token?, include_recent_changes?, environment?)`
- Activities list/get:
  - `timesheets_activities_get_list(tenant, page?, page_size?, include_total?, created_before?, created_on_or_after?, modified_before?, modified_on_or_after?, active?, sort?, environment?)`
  - `timesheets_activities_get(tenant, id, environment?)`
- Service agreements export/list/get:
  - `service_agreements_export_service_agreements(tenant, from_token?, include_recent_changes?, environment?)`
  - `service_agreements_get_list(tenant, ids?, customer_ids?, business_unit_ids?, status?, created_before?, created_on_or_after?, modified_before?, modified_on_or_after?, page?, page_size?, include_total?, sort?, environment?)`
  - `service_agreements_get(tenant, id, environment?)`

## Selective tool registration (performance)
Many clients perform better with fewer tools. You can choose which tool groups to expose by setting these in your .env:

```bash
# .env (comma-separated group names, case-insensitive)
SERVICETITAN_MCP_INCLUDE_GROUPS=crm,dispatch,inventory
# Or exclude some from the default full set
SERVICETITAN_MCP_EXCLUDE_GROUPS=marketing,marketingads,marketingreputation
```

Behavior and precedence:
- INCLUDE only: registers exactly those groups listed in `SERVICETITAN_MCP_INCLUDE_GROUPS`.
- EXCLUDE only: registers all groups except those listed in `SERVICETITAN_MCP_EXCLUDE_GROUPS`.
- Both set: takes the INCLUDE set, then removes any groups also listed in EXCLUDE.
- Names are case-insensitive; values are comma-separated.

Available group names correspond to subpackages under `tools/`: `accounting`, `crm`, `customerinteractions`, `dispatch`, `equipmentsystems`, `inventory`, `forms`, `jobbooking`, `jobplanningandmanagement`, `marketing`, `marketingads`, `marketingreputation`, `memberships`, `payroll`, `pricebook`, `settings`, `reporting`, `salesandestimates`, `schedulingpro`, `serviceagreements`, `taskmanagement`, `timesheets`, `telecom`.

## Troubleshooting
- Verify env vars and tenant permissions
- Use `environment="integration"` for the integration API

Working directory and absolute paths:
- Use absolute paths in your client config (working directory can be undefined for GUI apps)
- Ensure the server directory and script paths are correct and readable

If tools don’t appear in your client:
- Validate the client configuration
- Restart the client after changes
- Tail the client’s MCP logs/output for errors

## Debugging
This section summarizes practical steps to debug MCP integrations on macOS.

### Tools overview
- MCP Inspector: interactive testing UI for direct server calls
- Your client's developer tools: integration testing and log collection
- Server logging: capture errors and performance via stderr

### Check server status in your client
- Review the client’s UI for connected servers and available tools
- Use the client’s developer tools/logs to inspect message payloads and timing

### Common issues
Working directory:
- GUI apps may not have a meaningful CWD; always use absolute paths in config

Initialization problems:
- Path issues (wrong executable, missing files, permissions)
- Config errors (invalid JSON, missing fields)
- Env problems (missing/invalid tokens)