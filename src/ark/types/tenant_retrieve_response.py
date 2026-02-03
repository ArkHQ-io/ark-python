# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .tenant import Tenant
from .._models import BaseModel
from .shared.api_meta import APIMeta

__all__ = ["TenantRetrieveResponse"]


class TenantRetrieveResponse(BaseModel):
    data: Tenant

    meta: APIMeta

    success: Literal[True]
