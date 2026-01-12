# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .pagination import Pagination

__all__ = ["EmailListResponse", "Data", "DataMessage"]


class DataMessage(BaseModel):
    id: str
    """Internal message ID"""

    token: str

    from_: str = FieldInfo(alias="from")

    status: Literal["pending", "sent", "softfail", "hardfail", "bounced", "held"]
    """Current delivery status:

    - `pending` - Email accepted, waiting to be processed
    - `sent` - Email transmitted to recipient's mail server
    - `softfail` - Temporary delivery failure, will retry
    - `hardfail` - Permanent delivery failure
    - `bounced` - Email bounced back
    - `held` - Held for manual review
    """

    subject: str

    timestamp: float

    timestamp_iso: datetime = FieldInfo(alias="timestampIso")

    to: str

    tag: Optional[str] = None


class Data(BaseModel):
    messages: List[DataMessage]

    pagination: Pagination


class EmailListResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
