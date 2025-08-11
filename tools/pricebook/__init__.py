from typing import Any

from .export import register_pricebook_export_tools
from .categories import register_pricebook_categories_tools
from .clientspecificpricing import register_pricebook_client_specific_pricing_tools
from .discountandfees import register_pricebook_discounts_and_fees_tools
from .equipment import register_pricebook_equipment_tools
from .images import register_pricebook_images_tools
from .materials import register_pricebook_materials_tools
from .materialsmarkup import register_pricebook_materials_markup_tools
from .pricebookbulk import register_pricebook_bulk_tools
from .services import register_pricebook_services_tools

__all__ = ["register_pricebook_tools"]


def register_pricebook_tools(mcp: Any) -> None:
    register_pricebook_export_tools(mcp)
    register_pricebook_categories_tools(mcp)
    register_pricebook_client_specific_pricing_tools(mcp)
    register_pricebook_discounts_and_fees_tools(mcp)
    register_pricebook_equipment_tools(mcp)
    register_pricebook_images_tools(mcp)
    register_pricebook_materials_tools(mcp)
    register_pricebook_materials_markup_tools(mcp)
    register_pricebook_bulk_tools(mcp)
    register_pricebook_services_tools(mcp)


