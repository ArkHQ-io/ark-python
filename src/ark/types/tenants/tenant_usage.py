# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..email_rates import EmailRates
from ..email_counts import EmailCounts
from ..usage_period import UsagePeriod

__all__ = ["TenantUsage"]


class TenantUsage(BaseModel):
    """Tenant usage statistics"""

    emails: EmailCounts
    """Email delivery counts"""

    period: UsagePeriod
    """Time period for usage data"""

    rates: EmailRates
    """Email delivery rates (as decimals, e.g., 0.95 = 95%)"""

    tenant_id: str
    """Unique tenant identifier"""

    tenant_name: str
    """Tenant display name"""

    external_id: Optional[str] = None
    """Your external ID for this tenant (from metadata)"""
