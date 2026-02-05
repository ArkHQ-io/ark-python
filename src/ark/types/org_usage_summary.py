# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .email_rates import EmailRates
from .email_counts import EmailCounts
from .usage_period import UsagePeriod
from .shared.api_meta import APIMeta

__all__ = ["OrgUsageSummary", "Data", "DataTenants"]


class DataTenants(BaseModel):
    active: int
    """Number of active tenants"""

    total: int
    """Total number of tenants"""

    with_activity: int = FieldInfo(alias="withActivity")
    """Number of tenants with sending activity"""


class Data(BaseModel):
    emails: EmailCounts
    """Email delivery counts"""

    period: UsagePeriod
    """Time period for usage data"""

    rates: EmailRates
    """Email delivery rates (as decimals, e.g., 0.95 = 95%)"""

    tenants: DataTenants


class OrgUsageSummary(BaseModel):
    """Org-wide usage summary response"""

    data: Data

    meta: APIMeta

    success: Literal[True]
