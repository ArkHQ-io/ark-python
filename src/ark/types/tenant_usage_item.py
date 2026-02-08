# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .email_rates import EmailRates
from .email_counts import EmailCounts

__all__ = ["TenantUsageItem"]


class TenantUsageItem(BaseModel):
    """Usage record for a single tenant (camelCase for SDK)"""

    emails: EmailCounts
    """Email delivery counts"""

    rates: EmailRates
    """Email delivery rates (as decimals, e.g., 0.95 = 95%)"""

    status: Literal["active", "suspended", "archived"]
    """Current tenant status"""

    tenant_id: str = FieldInfo(alias="tenantId")
    """Unique tenant identifier"""

    tenant_name: str = FieldInfo(alias="tenantName")
    """Tenant display name"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external ID for this tenant"""
