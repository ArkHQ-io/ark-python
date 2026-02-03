# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    tenant_id: str
    """Filter domains by tenant ID"""
