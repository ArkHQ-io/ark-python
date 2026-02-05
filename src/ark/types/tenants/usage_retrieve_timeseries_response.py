# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.api_meta import APIMeta
from .tenant_usage_timeseries import TenantUsageTimeseries

__all__ = ["UsageRetrieveTimeseriesResponse"]


class UsageRetrieveTimeseriesResponse(BaseModel):
    """Timeseries usage data for a tenant"""

    data: TenantUsageTimeseries
    """Timeseries usage statistics"""

    meta: APIMeta

    success: Literal[True]
