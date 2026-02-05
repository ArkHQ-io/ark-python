# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for the credential.

    Can only contain letters, numbers, hyphens, and underscores. Max 50 characters.
    """

    type: Required[Literal["smtp", "api"]]
    """Type of credential:

    - `smtp` - For SMTP-based email sending
    - `api` - For API-based email sending
    """
