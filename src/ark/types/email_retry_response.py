# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmailRetryResponse", "Data"]


class Data(BaseModel):
    message: Optional[str] = None


class EmailRetryResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
