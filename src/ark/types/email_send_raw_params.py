# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailSendRawParams"]


class EmailSendRawParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender email address"""

    raw_message: Required[Annotated[str, PropertyInfo(alias="rawMessage")]]
    """Base64-encoded RFC 2822 MIME message"""

    to: Required[SequenceNotStr[str]]
    """Recipient email addresses"""

    bounce: Optional[bool]
    """Whether this is a bounce message (accepts null)"""
