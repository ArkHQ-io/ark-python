# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.api_meta import APIMeta

__all__ = ["EmailRetryResponse", "Data"]


class Data(BaseModel):
    id: str
    """Email identifier (token)"""

    message: str

    tenant_id: str = FieldInfo(alias="tenantId")
    """The tenant ID this email belongs to"""


class EmailRetryResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
