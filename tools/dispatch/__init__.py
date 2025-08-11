from typing import Any

from .export import register_dispatch_export_tools
from .appointmentassignments import register_dispatch_appointment_assignments_tools
from .arrivalwindows import register_dispatch_arrival_windows_tools
from .businesshour import register_dispatch_business_hour_tools
from .capacity import register_dispatch_capacity_tools
from .customeronly import register_dispatch_customer_only_tools
from .nonjobappointments import register_dispatch_non_job_appointments_tools
from .team import register_dispatch_team_tools
from .technicianshifts import register_dispatch_technician_shifts_tools
from .techniciantracking import register_dispatch_technician_tracking_tools
from .zone import register_dispatch_zone_tools

__all__ = ["register_dispatch_tools"]


def register_dispatch_tools(mcp: Any) -> None:
    """Register Dispatch-related tools with the MCP server instance."""
    register_dispatch_export_tools(mcp)
    register_dispatch_appointment_assignments_tools(mcp)
    register_dispatch_arrival_windows_tools(mcp)
    register_dispatch_business_hour_tools(mcp)
    register_dispatch_capacity_tools(mcp)
    register_dispatch_customer_only_tools(mcp)
    register_dispatch_non_job_appointments_tools(mcp)
    register_dispatch_team_tools(mcp)
    register_dispatch_technician_shifts_tools(mcp)
    register_dispatch_technician_tracking_tools(mcp)
    register_dispatch_zone_tools(mcp)



