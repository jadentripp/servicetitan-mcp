from typing import Any

from .attributedleads import register_marketingads_attributed_leads_tools
from .capacityawarenesswarning import register_marketingads_capacity_awareness_warning_tools
from .externalcallattributions import register_marketingads_external_call_attributions_tools
from .performance import register_marketingads_performance_tools
from .scheduledjobattributions import register_marketingads_scheduled_job_attributions_tools
from .webbookingattributions import register_marketingads_web_booking_attributions_tools
from .webleadformattributes import register_marketingads_web_lead_form_attributions_tools

__all__ = ["register_marketingads_tools"]


def register_marketingads_tools(mcp: Any) -> None:
    """Register Marketing Ads-related tools with the MCP server instance."""
    register_marketingads_attributed_leads_tools(mcp)
    register_marketingads_capacity_awareness_warning_tools(mcp)
    register_marketingads_external_call_attributions_tools(mcp)
    register_marketingads_performance_tools(mcp)
    register_marketingads_scheduled_job_attributions_tools(mcp)
    register_marketingads_web_booking_attributions_tools(mcp)
    register_marketingads_web_lead_form_attributions_tools(mcp)


