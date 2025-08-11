import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_post

__all__ = ["register_marketingads_external_call_attributions_tools"]


def register_marketingads_external_call_attributions_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingads_external_call_attributions_create(
        tenant: int,
        # WebSessionData (landing/referrer required)
        landing_page_url: str,
        referrer_url: str,
        gclid: Optional[str] = None,
        gbraid: Optional[str] = None,
        wbraid: Optional[str] = None,
        fbclid: Optional[str] = None,
        msclkid: Optional[str] = None,
        utm_source: Optional[str] = None,
        utm_medium: Optional[str] = None,
        utm_campaign: Optional[str] = None,
        utm_adgroup: Optional[str] = None,
        utm_term: Optional[str] = None,
        utm_content: Optional[str] = None,
        google_analytics_client_id: Optional[str] = None,
        # ExternalCallData (all required)
        customer_phone_number: str = "",
        forwarding_phone_number: str = "",
        tracking_phone_number: str = "",
        call_started_on_utc: str = "",
        environment: str = "production",
    ) -> str:
        """Attributes an external call to a web session.

        Mirrors ExternalCallAttributions_Create.
        """

        if not landing_page_url or not referrer_url:
            return "'landing_page_url' and 'referrer_url' are required."
        if not (customer_phone_number and forwarding_phone_number and tracking_phone_number and call_started_on_utc):
            return "All external call fields are required: customer_phone_number, forwarding_phone_number, tracking_phone_number, call_started_on_utc."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingads/v2/tenant/{tenant}/external-call-attributions"

        web_session: dict[str, Any] = {
            "landingPageUrl": landing_page_url,
            "referrerUrl": referrer_url,
        }
        if gclid is not None:
            web_session["gclid"] = gclid
        if gbraid is not None:
            web_session["gbraid"] = gbraid
        if wbraid is not None:
            web_session["wbraid"] = wbraid
        if fbclid is not None:
            web_session["fbclid"] = fbclid
        if msclkid is not None:
            web_session["msclkid"] = msclkid
        if utm_source is not None:
            web_session["utmSource"] = utm_source
        if utm_medium is not None:
            web_session["utmMedium"] = utm_medium
        if utm_campaign is not None:
            web_session["utmCampaign"] = utm_campaign
        if utm_adgroup is not None:
            web_session["utmAdgroup"] = utm_adgroup
        if utm_term is not None:
            web_session["utmTerm"] = utm_term
        if utm_content is not None:
            web_session["utmContent"] = utm_content
        if google_analytics_client_id is not None:
            web_session["googleAnalyticsClientId"] = google_analytics_client_id

        external_call = {
            "customerPhoneNumber": customer_phone_number,
            "forwardingPhoneNumber": forwarding_phone_number,
            "trackingPhoneNumber": tracking_phone_number,
            "callStartedOnUtc": call_started_on_utc,
        }

        body = {"webSessionData": web_session, "externalCallData": external_call}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create external call attribution."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


