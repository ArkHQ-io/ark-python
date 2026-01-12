# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailListParams"]


class EmailListParams(TypedDict, total=False):
    after: str
    """Return emails sent after this timestamp (Unix seconds or ISO 8601)"""

    before: str
    """Return emails sent before this timestamp"""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Filter by sender email address"""

    page: int
    """Page number (starts at 1)"""

    per_page: Annotated[int, PropertyInfo(alias="perPage")]
    """Results per page (max 100)"""

    status: Literal["queued", "sent", "delivered", "bounced", "failed", "delayed", "held"]
    """Filter by delivery status:

    - `queued` - Email accepted and waiting to be sent
    - `sent` - Email transmitted to recipient's mail server
    - `delivered` - Recipient's server confirmed receipt
    - `bounced` - Permanently rejected (hard bounce)
    - `failed` - Delivery failed after all retry attempts
    - `delayed` - Temporary failure, will retry
    - `held` - Held for manual review
    """

    tag: str
    """Filter by tag"""

    to: str
    """Filter by recipient email address"""
