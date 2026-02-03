# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .limits_data import LimitsData
from .shared.api_meta import APIMeta

__all__ = ["LimitRetrieveResponse"]


class LimitRetrieveResponse(BaseModel):
    """Account rate limits and send limits response"""

    data: LimitsData
    """Current usage and limit information"""

    meta: APIMeta

    success: Literal[True]
