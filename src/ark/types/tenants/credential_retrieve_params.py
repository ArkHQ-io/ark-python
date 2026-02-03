# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CredentialRetrieveParams"]


class CredentialRetrieveParams(TypedDict, total=False):
    tenant_id: Required[Annotated[str, PropertyInfo(alias="tenantId")]]

    reveal: bool
    """Set to `true` to include the credential key in the response"""
