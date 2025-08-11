import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_post, make_st_request

__all__ = ["register_taskmanagement_tasks_tools"]


def _normalize_tristate(value: Optional[str]) -> str | None:
    if value is None:
        return None
    v = str(value).strip().lower()
    if v in {"true", "any", "false"}:
        return {"true": "True", "any": "Any", "false": "False"}[v]
    return "__INVALID__"


def register_taskmanagement_tasks_tools(mcp: Any) -> None:
    @mcp.tool()
    async def taskmanagement_tasks_create(
        tenant: int,
        reported_by_id: int,
        assigned_to_id: int,
        is_closed: bool,
        name: str,
        business_unit_id: int,
        employee_task_type_id: int,
        employee_task_source_id: int,
        priority: str,
        status: Optional[str] = None,
        employee_task_resolution_id: Optional[int] = None,
        reported_date: Optional[str] = None,
        complete_by: Optional[str] = None,
        started_on: Optional[str] = None,
        involved_employee_id_list: Optional[Sequence[int]] = None,
        customer_id: Optional[int] = None,
        job_id: Optional[int] = None,
        project_id: Optional[int] = None,
        description: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a task (Tasks_Create)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/taskmanagement/v2/tenant/{tenant}/tasks"

        body: dict[str, Any] = {
            "reportedById": reported_by_id,
            "assignedToId": assigned_to_id,
            "isClosed": is_closed,
            "name": name,
            "businessUnitId": business_unit_id,
            "employeeTaskTypeId": employee_task_type_id,
            "employeeTaskSourceId": employee_task_source_id,
            "priority": priority,
        }
        if status is not None:
            body["status"] = status
        if employee_task_resolution_id is not None:
            body["employeeTaskResolutionId"] = employee_task_resolution_id
        if reported_date is not None:
            body["reportedDate"] = reported_date
        if complete_by is not None:
            body["completeBy"] = complete_by
        if started_on is not None:
            body["startedOn"] = started_on
        if involved_employee_id_list is not None:
            body["involvedEmployeeIdList"] = list(involved_employee_id_list)
        if customer_id is not None:
            body["customerId"] = customer_id
        if job_id is not None:
            body["jobId"] = job_id
        if project_id is not None:
            body["projectId"] = project_id
        if description is not None:
            body["description"] = description

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create task."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def taskmanagement_tasks_get_tasks(
        tenant: int,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        reported_before: Optional[str] = None,
        reported_on_or_after: Optional[str] = None,
        complete_before: Optional[str] = None,
        complete_on_or_after: Optional[str] = None,
        is_closed: Optional[bool] = None,
        statuses: Optional[str] = None,
        ids: Optional[str] = None,
        name: Optional[str] = None,
        include_subtasks: Optional[bool] = None,
        business_unit_ids: Optional[str] = None,
        employee_task_type_ids: Optional[str] = None,
        employee_task_source_ids: Optional[str] = None,
        employee_task_resolution_ids: Optional[str] = None,
        reported_by_id: Optional[int] = None,
        assigned_to_id: Optional[int] = None,
        involved_employee_id_list: Optional[str] = None,
        customer_id: Optional[int] = None,
        job_id: Optional[int] = None,
        project_id: Optional[int] = None,
        priorities: Optional[str] = None,
        task_number: Optional[int] = None,
        job_number: Optional[str] = None,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a list of tasks (Tasks_GetTasks)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/taskmanagement/v2/tenant/{tenant}/tasks"

        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True

        if active is not None:
            normalized = _normalize_tristate(active)
            if normalized == "__INVALID__":
                return "Invalid 'active' value. Use one of: True, Any, False."
            params["active"] = normalized

        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
        if reported_before:
            params["reportedBefore"] = reported_before
        if reported_on_or_after:
            params["reportedOnOrAfter"] = reported_on_or_after
        if complete_before:
            params["completeBefore"] = complete_before
        if complete_on_or_after:
            params["completeOnOrAfter"] = complete_on_or_after
        if is_closed is not None:
            params["isClosed"] = is_closed
        if statuses:
            params["statuses"] = statuses
        if ids:
            params["ids"] = ids
        if name:
            params["name"] = name
        if include_subtasks is not None:
            params["includeSubtasks"] = include_subtasks
        if business_unit_ids:
            params["businessUnitIds"] = business_unit_ids
        if employee_task_type_ids:
            params["employeeTaskTypeIds"] = employee_task_type_ids
        if employee_task_source_ids:
            params["employeeTaskSourceIds"] = employee_task_source_ids
        if employee_task_resolution_ids:
            params["employeeTaskResolutionIds"] = employee_task_resolution_ids
        if reported_by_id is not None:
            params["reportedById"] = reported_by_id
        if assigned_to_id is not None:
            params["assignedToId"] = assigned_to_id
        if involved_employee_id_list:
            params["involvedEmployeeIdList"] = involved_employee_id_list
        if customer_id is not None:
            params["customerId"] = customer_id
        if job_id is not None:
            params["jobId"] = job_id
        if project_id is not None:
            params["projectId"] = project_id
        if priorities:
            params["priorities"] = priorities
        if task_number is not None:
            params["taskNumber"] = task_number
        if job_number:
            params["jobNumber"] = job_number
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch tasks."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def taskmanagement_tasks_get_task(
        tenant: int,
        id: int,
        include_subtasks: Optional[bool] = None,
        environment: str = "production",
    ) -> str:
        """Get a task by ID (Tasks_GetTask)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/taskmanagement/v2/tenant/{tenant}/tasks/{id}"

        params: dict[str, Any] = {}
        if include_subtasks is not None:
            params["includeSubtasks"] = include_subtasks

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch the specified task."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def taskmanagement_tasks_create_subtask(
        tenant: int,
        id: int,
        is_closed: bool,
        name: str,
        assigned_to_id: int,
        due_date_time: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Create a subtask (Tasks_CreateSubtask)."""

        base_url = get_base_url(environment)
        url = f"{base_url}/taskmanagement/v2/tenant/{tenant}/tasks/{id}/subtasks"

        body: dict[str, Any] = {
            "isClosed": is_closed,
            "name": name,
            "assignedToId": assigned_to_id,
        }
        if due_date_time is not None:
            body["dueDateTime"] = due_date_time

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create subtask."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


