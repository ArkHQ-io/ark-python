# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .email_rates import EmailRates
from .email_counts import EmailCounts
from .usage_period import UsagePeriod

__all__ = ["BulkTenantUsage", "Pagination", "Summary", "Tenant"]


class Pagination(BaseModel):
    """Pagination information for usage queries"""

    has_more: bool
    """Whether more pages are available"""

    limit: int
    """Maximum items per page"""

    offset: int
    """Number of items skipped"""

    total: int
    """Total number of tenants matching the query"""


class Summary(BaseModel):
    """Aggregate summary across all tenants"""

    total_delivered: int
    """Total emails delivered across all tenants"""

    total_sent: int
    """Total emails sent across all tenants"""

    total_tenants: int
    """Total number of tenants in the query"""


class Tenant(BaseModel):
    """Usage record for a single tenant in bulk response"""

    emails: EmailCounts
    """Email delivery counts"""

    rates: EmailRates
    """Email delivery rates (as decimals, e.g., 0.95 = 95%)"""

    status: Literal["active", "suspended", "archived"]
    """Current tenant status"""

    tenant_id: str
    """Unique tenant identifier"""

    tenant_name: str
    """Tenant display name"""

    external_id: Optional[str] = None
    """Your external ID for this tenant"""


class BulkTenantUsage(BaseModel):
    """Bulk tenant usage data with pagination"""

    pagination: Pagination
    """Pagination information for usage queries"""

    period: UsagePeriod
    """Time period for usage data"""

    summary: Summary
    """Aggregate summary across all tenants"""

    tenants: List[Tenant]
    """Array of tenant usage records"""
