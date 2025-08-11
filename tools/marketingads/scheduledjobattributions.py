import json
from typing import Any, Optional

from ..utils import get_base_url, make_st_post

__all__ = ["register_marketingads_scheduled_job_attributions_tools"]


def register_marketingads_scheduled_job_attributions_tools(mcp: Any) -> None:
    @mcp.tool()
    async def marketingads_scheduled_job_attributions_create(
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
        # Entity
        job_id: int = 0,
        environment: str = "production",
    ) -> str:
        """Attributes a job to a web session.

        Mirrors ScheduledJobAttributions_Create.
        """

        if not landing_page_url or not referrer_url:
            return "'landing_page_url' and 'referrer_url' are required."
        if not job_id:
            return "'job_id' is required."

        base_url = get_base_url(environment)
        url = f"{base_url}/marketingads/v2/tenant/{tenant}/job-attributions"

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

        body = {"webSessionData": web_session, "jobId": int(job_id)}
        data = await make_st_post(url, json_body=body)
        if not data:
            return "Unable to create scheduled job attribution."

        try:
            return json.dumps(data, indent=2)
        except Exception:
            return str(data)


