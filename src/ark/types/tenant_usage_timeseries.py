# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .usage_period import UsagePeriod

__all__ = ["TenantUsageTimeseries", "Data"]


class Data(BaseModel):
    """Single timeseries data point"""

    bounced: int
    """Bounces in this bucket"""

    delivered: int
    """Emails delivered in this bucket"""

    hard_failed: int
    """Hard failures in this bucket"""

    held: int
    """Emails held in this bucket"""

    sent: int
    """Emails sent in this bucket"""

    soft_failed: int
    """Soft failures in this bucket"""

    timestamp: datetime
    """Start of time bucket"""


class TenantUsageTimeseries(BaseModel):
    """Timeseries usage statistics"""

    data: List[Data]
    """Array of time-bucketed data points"""

    granularity: Literal["hour", "day", "week", "month"]
    """Time bucket granularity"""

    period: UsagePeriod
    """Time period for usage data"""

    tenant_id: str
    """Unique tenant identifier"""

    tenant_name: str
    """Tenant display name"""
