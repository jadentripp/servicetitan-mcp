from typing import Any

from .export import register_export_tools
from .apcredits import register_apcredits_tools
from .appayments import register_appayments_tools
from .glaccounts import register_glaccounts_tools
from .inventorybills import register_inventory_bills_tools
from .invoices import register_invoices_tools
from .journalentries import register_journal_entries_tools
from .payments import register_payments_tools
from .paymentterms import register_payment_terms_tools
from .paymenttypes import register_payment_types_tools
from .taxzones import register_tax_zones_tools

# Public API of this module
__all__ = ["register_accounting_tools"]


def register_accounting_tools(mcp: Any) -> None:
    """Register accounting-related tools with the provided MCP server instance."""
    register_export_tools(mcp)
    register_apcredits_tools(mcp)
    register_appayments_tools(mcp)
    register_glaccounts_tools(mcp)
    register_inventory_bills_tools(mcp)
    register_invoices_tools(mcp)
    register_journal_entries_tools(mcp)
    register_payments_tools(mcp)
    register_payment_terms_tools(mcp)
    register_payment_types_tools(mcp)
    register_tax_zones_tools(mcp)


