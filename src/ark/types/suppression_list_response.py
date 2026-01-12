# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .pagination import Pagination

__all__ = ["SuppressionListResponse", "Data", "DataSuppression"]


class DataSuppression(BaseModel):
    id: str
    """Suppression ID"""

    address: str

    created_at: datetime = FieldInfo(alias="createdAt")

    reason: Optional[str] = None


class Data(BaseModel):
    pagination: Pagination

    suppressions: List[DataSuppression]


class SuppressionListResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
