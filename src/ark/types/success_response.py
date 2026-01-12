# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .api_meta import APIMeta

__all__ = ["SuccessResponse", "Data"]


class Data(BaseModel):
    message: str


class SuccessResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
