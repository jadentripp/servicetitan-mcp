from typing import Any, Callable, Dict, List

from .accounting import register_accounting_tools
from .crm import register_crm_tools
from .customerinteractions import register_customer_interactions_tools
from .dispatch import register_dispatch_tools
from .equipmentsystems import register_equipmentsystems_tools
from .inventory import register_inventory_tools
from .jobbooking import register_jobbooking_tools
from .forms import register_forms_tools
from .jobplanningandmanagement import register_jobplanningandmanagement_tools
from .marketing import register_marketing_tools
from .marketingads import register_marketingads_tools
from .marketingreputation import register_marketingreputation_tools
from .reporting import register_reporting_tools
from .salesandestimates import register_salesandestimates_tools
from .schedulingpro import register_schedulingpro_tools
from .memberships import register_memberships_tools
from .payroll import register_payroll_tools
from .pricebook import register_pricebook_tools
from .settings import register_settings_tools
from .serviceagreements import register_serviceagreements_tools
from .taskmanagement import register_taskmanagement_tools
from .timesheets import register_timesheets_tools
from .telecom import register_telecom_tools

__all__ = ["register_all_tools", "register_selected_tools", "TOOL_REGISTRARS"]


def register_all_tools(mcp: Any) -> None:
    """Register all tool groups (accounting, crm, etc.)."""
    register_accounting_tools(mcp)
    register_crm_tools(mcp)
    register_customer_interactions_tools(mcp)
    register_dispatch_tools(mcp)
    register_equipmentsystems_tools(mcp)
    register_inventory_tools(mcp)
    register_forms_tools(mcp)
    register_jobbooking_tools(mcp)
    register_jobplanningandmanagement_tools(mcp)
    register_marketing_tools(mcp)
    register_marketingads_tools(mcp)
    register_marketingreputation_tools(mcp)
    register_memberships_tools(mcp)
    register_payroll_tools(mcp)
    register_pricebook_tools(mcp)
    register_settings_tools(mcp)
    register_reporting_tools(mcp)
    register_salesandestimates_tools(mcp)
    register_schedulingpro_tools(mcp)
    register_serviceagreements_tools(mcp)
    register_taskmanagement_tools(mcp)
    register_timesheets_tools(mcp)
    register_telecom_tools(mcp)


# Mapping of group name -> registrar for selective enabling
TOOL_REGISTRARS: Dict[str, Callable[[Any], None]] = {
    "accounting": register_accounting_tools,
    "crm": register_crm_tools,
    "customerinteractions": register_customer_interactions_tools,
    "dispatch": register_dispatch_tools,
    "equipmentsystems": register_equipmentsystems_tools,
    "inventory": register_inventory_tools,
    "forms": register_forms_tools,
    "jobbooking": register_jobbooking_tools,
    "jobplanningandmanagement": register_jobplanningandmanagement_tools,
    "marketing": register_marketing_tools,
    "marketingads": register_marketingads_tools,
    "marketingreputation": register_marketingreputation_tools,
    "memberships": register_memberships_tools,
    "payroll": register_payroll_tools,
    "pricebook": register_pricebook_tools,
    "settings": register_settings_tools,
    "reporting": register_reporting_tools,
    "salesandestimates": register_salesandestimates_tools,
    "schedulingpro": register_schedulingpro_tools,
    "serviceagreements": register_serviceagreements_tools,
    "taskmanagement": register_taskmanagement_tools,
    "timesheets": register_timesheets_tools,
    "telecom": register_telecom_tools,
}


def register_selected_tools(
    mcp: Any,
    include_groups: List[str] | None = None,
    exclude_groups: List[str] | None = None,
) -> List[str]:
    """Register only selected tool groups.

    Args:
        mcp: FastMCP instance
        include_groups: explicit list of groups to include (lower/any case)
        exclude_groups: groups to exclude (applied after include)

    Returns:
        List of group names that were registered
    """

    include_set = {g.strip().lower() for g in (include_groups or []) if g and g.strip()}
    exclude_set = {g.strip().lower() for g in (exclude_groups or []) if g and g.strip()}

    if include_set:
        chosen = [g for g in TOOL_REGISTRARS.keys() if g in include_set]
    else:
        chosen = list(TOOL_REGISTRARS.keys())

    # apply excludes
    chosen = [g for g in chosen if g not in exclude_set]

    for group in chosen:
        TOOL_REGISTRARS[group](mcp)

    return chosen

