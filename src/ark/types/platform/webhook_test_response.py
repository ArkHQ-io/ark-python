# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.api_meta import APIMeta

__all__ = ["WebhookTestResponse", "Data"]


class Data(BaseModel):
    duration_ms: int = FieldInfo(alias="durationMs")
    """Request duration in milliseconds"""

    status_code: int = FieldInfo(alias="statusCode")
    """HTTP status code from the webhook endpoint"""

    success: bool
    """Whether the webhook endpoint responded with a 2xx status"""

    error: Optional[str] = None
    """Error message if the request failed"""


class WebhookTestResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
