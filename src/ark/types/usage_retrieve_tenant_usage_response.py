# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tenant_usage import TenantUsage
from .shared.api_meta import APIMeta

__all__ = ["UsageRetrieveTenantUsageResponse"]


class UsageRetrieveTenantUsageResponse(BaseModel):
    """Usage statistics for a single tenant"""

    data: TenantUsage
    """Tenant usage statistics"""

    meta: APIMeta

    success: Literal[True]
