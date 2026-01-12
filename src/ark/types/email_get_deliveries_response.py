# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .delivery import Delivery

__all__ = ["EmailGetDeliveriesResponse", "Data"]


class Data(BaseModel):
    deliveries: List[Delivery]

    message_id: str = FieldInfo(alias="messageId")
    """Internal message ID"""

    message_token: str = FieldInfo(alias="messageToken")
    """Message token"""


class EmailGetDeliveriesResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
