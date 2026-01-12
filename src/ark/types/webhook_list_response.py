# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .api_meta import APIMeta

__all__ = ["WebhookListResponse", "Data", "DataWebhook"]


class DataWebhook(BaseModel):
    id: str
    """Webhook ID"""

    enabled: bool

    events: List[str]

    name: str

    url: str

    signed: Optional[bool] = None
    """Whether webhook payloads are signed"""


class Data(BaseModel):
    webhooks: List[DataWebhook]


class WebhookListResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
