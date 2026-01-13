# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.api_meta import APIMeta

__all__ = ["SuppressionListResponse", "Data", "DataPagination", "DataSuppression"]


class DataPagination(BaseModel):
    page: int
    """Current page number (1-indexed)"""

    per_page: int = FieldInfo(alias="perPage")
    """Items per page"""

    total: int
    """Total number of items"""

    total_pages: int = FieldInfo(alias="totalPages")
    """Total number of pages"""


class DataSuppression(BaseModel):
    id: str
    """Suppression ID"""

    address: str

    created_at: datetime = FieldInfo(alias="createdAt")

    reason: Optional[str] = None


class Data(BaseModel):
    pagination: DataPagination

    suppressions: List[DataSuppression]


class SuppressionListResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
