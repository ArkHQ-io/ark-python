# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    page: int
    """Current page number (1-indexed)"""

    per_page: int = FieldInfo(alias="perPage")
    """Items per page"""

    total: int
    """Total number of items"""

    total_pages: int = FieldInfo(alias="totalPages")
    """Total number of pages"""
