import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_request, make_st_post, make_st_patch

__all__ = ["register_inventory_purchase_order_types_tools"]


def register_inventory_purchase_order_types_tools(mcp: Any) -> None:
    @mcp.tool()
    async def inventory_purchase_order_types_get_list(
        tenant: int,
        active: Optional[str] = None,
        created_before: Optional[str] = None,
        created_on_or_after: Optional[str] = None,
        modified_before: Optional[str] = None,
        modified_on_or_after: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        include_total: bool = False,
        sort: Optional[str] = None,
        environment: str = "production",
    ) -> str:
        """Get a paginated list of purchase order types.

        Mirrors PurchaseOrderTypes_GetList.
        - active: one of "True", "Any", "False" (case-insensitive).
        """

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-types"

        params: dict[str, Any] = {}

        if active is not None:
            normalized = str(active).strip().lower()
            if normalized in {"true", "any", "false"}:
                params["active"] = {"true": "True", "any": "Any", "false": "False"}[normalized]
            else:
                return "Invalid 'active' value. Use one of: True, Any, False."

        if created_before:
            params["createdBefore"] = created_before
        if created_on_or_after:
            params["createdOnOrAfter"] = created_on_or_after
        if modified_before:
            params["modifiedBefore"] = modified_before
        if modified_on_or_after:
            params["modifiedOnOrAfter"] = modified_on_or_after
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
            return "Unable to fetch purchase order types."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_types_create(
        tenant: int,
        name: str,
        active: bool,
        include_in_po_screen: bool,
        automatically_receive: bool,
        display_to_technician: bool,
        exclude_tax_from_job_costing: bool,
        impact_to_technician_payroll: bool,
        allow_technicians_to_send_po: bool,
        default_required_date_days_offset: int,
        skip_weekends: bool,
        include_in_sales_tax: bool,
        is_default: bool,
        copy_purchase_order_items_to_invoice_when_received: bool,
        is_default_for_consignment: bool,
        alert_settings: dict[str, Any],
        environment: str = "production",
    ) -> str:
        """Create a new Purchase Order Type. Mirrors PurchaseOrderTypes_Create."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-types"

        body: dict[str, Any] = {
            "name": name,
            "active": bool(active),
            "includeInPoScreen": bool(include_in_po_screen),
            "automaticallyReceive": bool(automatically_receive),
            "displayToTechnician": bool(display_to_technician),
            "excludeTaxFromJobCosting": bool(exclude_tax_from_job_costing),
            "impactToTechnicianPayroll": bool(impact_to_technician_payroll),
            "allowTechniciansToSendPo": bool(allow_technicians_to_send_po),
            "defaultRequiredDateDaysOffset": int(default_required_date_days_offset),
            "skipWeekends": bool(skip_weekends),
            "includeInSalesTax": bool(include_in_sales_tax),
            "isDefault": bool(is_default),
            "copyPurchaseOrderItemsToInvoiceWhenReceived": bool(
                copy_purchase_order_items_to_invoice_when_received
            ),
            "isDefaultForConsignment": bool(is_default_for_consignment),
            "alertSettings": alert_settings,
        }

        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create purchase order type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)

    @mcp.tool()
    async def inventory_purchase_order_types_update(
        tenant: int,
        id: int,
        active: Optional[bool] = None,
        name: Optional[str] = None,
        include_in_po_screen: Optional[bool] = None,
        automatically_receive: Optional[bool] = None,
        display_to_technician: Optional[bool] = None,
        exclude_tax_from_job_costing: Optional[bool] = None,
        impact_to_technician_payroll: Optional[bool] = None,
        allow_technicians_to_send_po: Optional[bool] = None,
        default_required_date_days_offset: Optional[int] = None,
        skip_weekends: Optional[bool] = None,
        include_in_sales_tax: Optional[bool] = None,
        is_default: Optional[bool] = None,
        copy_purchase_order_items_to_invoice_when_received: Optional[bool] = None,
        is_default_for_consignment: Optional[bool] = None,
        alert_settings: Optional[dict[str, Any]] = None,
        environment: str = "production",
    ) -> str:
        """Update an existing Purchase Order Type. Mirrors PurchaseOrderTypes_Update."""

        base_url = get_base_url(environment)
        url = f"{base_url}/inventory/v2/tenant/{tenant}/purchase-order-types/{id}"

        body: dict[str, Any] = {}
        if active is not None:
            body["active"] = bool(active)
        if name is not None:
            body["name"] = name
        if include_in_po_screen is not None:
            body["includeInPoScreen"] = bool(include_in_po_screen)
        if automatically_receive is not None:
            body["automaticallyReceive"] = bool(automatically_receive)
        if display_to_technician is not None:
            body["displayToTechnician"] = bool(display_to_technician)
        if exclude_tax_from_job_costing is not None:
            body["excludeTaxFromJobCosting"] = bool(exclude_tax_from_job_costing)
        if impact_to_technician_payroll is not None:
            body["impactToTechnicianPayroll"] = bool(impact_to_technician_payroll)
        if allow_technicians_to_send_po is not None:
            body["allowTechniciansToSendPo"] = bool(allow_technicians_to_send_po)
        if default_required_date_days_offset is not None:
            body["defaultRequiredDateDaysOffset"] = int(default_required_date_days_offset)
        if skip_weekends is not None:
            body["skipWeekends"] = bool(skip_weekends)
        if include_in_sales_tax is not None:
            body["includeInSalesTax"] = bool(include_in_sales_tax)
        if is_default is not None:
            body["isDefault"] = bool(is_default)
        if copy_purchase_order_items_to_invoice_when_received is not None:
            body["copyPurchaseOrderItemsToInvoiceWhenReceived"] = bool(
                copy_purchase_order_items_to_invoice_when_received
            )
        if is_default_for_consignment is not None:
            body["isDefaultForConsignment"] = bool(is_default_for_consignment)
        if alert_settings is not None:
            body["alertSettings"] = alert_settings

        if not body:
            return "No fields provided to update."

        data = await make_st_patch(url, json_body=body)
        if not data:
            return "Unable to update purchase order type."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


