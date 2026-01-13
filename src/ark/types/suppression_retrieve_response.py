# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SuppressionRetrieveResponse", "Data"]


class Data(BaseModel):
    address: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    reason: Optional[str] = None

    suppressed: Optional[bool] = None


class SuppressionRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
