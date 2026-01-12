# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .track_domain import TrackDomain

__all__ = ["TrackingListResponse", "Data"]


class Data(BaseModel):
    track_domains: Optional[List[TrackDomain]] = FieldInfo(alias="trackDomains", default=None)


class TrackingListResponse(BaseModel):
    data: Optional[Data] = None

    meta: Optional[APIMeta] = None

    success: Optional[Literal[True]] = None
