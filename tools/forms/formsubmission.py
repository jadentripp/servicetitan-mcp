import json
from typing import Any, Optional, Sequence

from ..utils import get_base_url, make_st_request

__all__ = ["register_forms_form_submission_tools"]


def register_forms_form_submission_tools(mcp: Any) -> None:
    @mcp.tool()
    async def forms_get_form_submissions(
        tenant: int,
        form_ids: Optional[str] = None,
        active: Optional[str] = None,
        created_by_id: Optional[int] = None,
        status: Optional[str] = None,
        submitted_on_or_after: Optional[str] = None,
        submitted_before: Optional[str] = None,
        owner_type: Optional[str] = None,
        owners: Optional[Sequence[dict[str, Any]]] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Retrieve form submissions (paginated) with filters.

        Mirrors FormSubmission_GetFormSubmissions.
        - status: Started | Completed | Any (case-insensitive)
        - active: True | Any | False (case-insensitive)
        - owner_type: Job | Call | Customer | Location | Equipment | Technician | JobAppointment | Membership | Truck | Project | ServiceAgreement | InvoiceItem (case-insensitive)
        - owners: list of { type: OwnerType, id: int }
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/forms/v2/tenant/{tenant}/submissions"

        params: dict[str, Any] = {}
        if form_ids:
            params["formIds"] = form_ids
        if active is not None:
            a = str(active).strip().lower()
            if a in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[a]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."
        if created_by_id is not None:
            params["createdById"] = int(created_by_id)
        if status:
            s = status.strip().lower()
            if s in {"started", "completed", "any"}:
                params["status"] = {"started": "Started", "completed": "Completed", "any": "Any"}[s]
            else:
                return "Invalid 'status'. Use one of: Started, Completed, Any."
        if submitted_on_or_after:
            params["submittedOnOrAfter"] = submitted_on_or_after
        if submitted_before:
            params["submittedBefore"] = submitted_before
        if owner_type:
            ot = owner_type.strip().lower()
            allowed = {
                "job": "Job",
                "call": "Call",
                "customer": "Customer",
                "location": "Location",
                "equipment": "Equipment",
                "technician": "Technician",
                "jobappointment": "JobAppointment",
                "membership": "Membership",
                "truck": "Truck",
                "project": "Project",
                "serviceagreement": "ServiceAgreement",
                "invoiceitem": "InvoiceItem",
            }
            if ot not in allowed:
                return "Invalid 'owner_type'."
            params["ownerType"] = allowed[ot]
        if owners:
            # owners are sent as repeated query parameters: owners[0].type, owners[0].id, etc.
            for idx, item in enumerate(owners):
                if not isinstance(item, dict):
                    continue
                t = item.get("type")
                i = item.get("id")
                if t is None or i is None:
                    continue
                params[f"owners[{idx}].type"] = t
                params[f"owners[{idx}].id"] = int(i)
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["pageSize"] = page_size
        if include_total:
            params["includeTotal"] = True
        if sort:
            params["sort"] = sort

        data = await make_st_request(url, params=params or None)
        if not data:
            return "Unable to fetch form submissions."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


