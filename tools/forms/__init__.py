from typing import Any

from .form import register_forms_form_tools
from .formsubmission import register_forms_form_submission_tools
from .jobs import register_forms_jobs_tools

__all__ = ["register_forms_tools"]


def register_forms_tools(mcp: Any) -> None:
    """Register Forms-related tools with the MCP server instance."""
    register_forms_form_tools(mcp)
    register_forms_form_submission_tools(mcp)
    register_forms_jobs_tools(mcp)



