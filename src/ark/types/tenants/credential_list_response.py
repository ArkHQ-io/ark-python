# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CredentialListResponse"]


class CredentialListResponse(BaseModel):
    id: int
    """Unique identifier for the credential"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the credential was created"""

    hold: bool
    """
    Whether the credential is on hold (disabled). When `true`, the credential cannot
    be used to send emails.
    """

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
    """When the credential was last used to send an email"""

    name: str
    """Name of the credential"""

    type: Literal["smtp", "api"]
    """Type of credential:

    - `smtp` - For SMTP-based email sending
    - `api` - For API-based email sending
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the credential was last updated"""
