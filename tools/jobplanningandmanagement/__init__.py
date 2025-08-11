from typing import Any

from .export import register_jobplanningandmanagement_export_tools
from .appointments import register_jobplanningandmanagement_appointments_tools
from .jobcancelreasons import register_jobplanningandmanagement_job_cancel_reasons_tools
from .jobholdreasons import register_jobplanningandmanagement_job_hold_reasons_tools
from .jobs import register_jobplanningandmanagement_jobs_tools
from .jobtypes import register_jobplanningandmanagement_job_types_tools
from .projects import register_jobplanningandmanagement_projects_tools
from .projectstatuses import register_jobplanningandmanagement_project_statuses_tools
from .projectsubstatuses import register_jobplanningandmanagement_project_substatuses_tools
from .projecttypes import register_jobplanningandmanagement_project_types_reference_tools

__all__ = ["register_jobplanningandmanagement_tools"]


def register_jobplanningandmanagement_tools(mcp: Any) -> None:
    """Register Job Planning & Management-related tools with the MCP server instance."""
    register_jobplanningandmanagement_export_tools(mcp)
    register_jobplanningandmanagement_appointments_tools(mcp)
    register_jobplanningandmanagement_job_cancel_reasons_tools(mcp)
    register_jobplanningandmanagement_job_hold_reasons_tools(mcp)
    register_jobplanningandmanagement_jobs_tools(mcp)
    register_jobplanningandmanagement_job_types_tools(mcp)
    register_jobplanningandmanagement_projects_tools(mcp)
    register_jobplanningandmanagement_project_statuses_tools(mcp)
    register_jobplanningandmanagement_project_substatuses_tools(mcp)
    register_jobplanningandmanagement_project_types_reference_tools(mcp)


