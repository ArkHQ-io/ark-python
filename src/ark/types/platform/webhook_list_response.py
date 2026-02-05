# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.api_meta import APIMeta

__all__ = ["WebhookListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Platform webhook ID"""

    created_at: datetime = FieldInfo(alias="createdAt")

    enabled: bool

    events: List[str]

    name: str

    url: str


class WebhookListResponse(BaseModel):
    data: List[Data]

    meta: APIMeta

    success: Literal[True]
