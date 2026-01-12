# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .api_meta import APIMeta
from .track_domain import TrackDomain

__all__ = ["TrackDomainResponse"]


class TrackDomainResponse(BaseModel):
    data: TrackDomain

    meta: APIMeta

    success: Literal[True]
