# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CredentialListParams"]


class CredentialListParams(TypedDict, total=False):
    page: int
    """Page number (1-indexed)"""

    per_page: Annotated[int, PropertyInfo(alias="perPage")]
    """Number of items per page (max 100)"""

    type: Literal["smtp", "api"]
    """Filter by credential type"""
