# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CredentialUpdateParams"]


class CredentialUpdateParams(TypedDict, total=False):
    tenant_id: Required[Annotated[str, PropertyInfo(alias="tenantId")]]

    hold: bool
    """
    Set to `true` to disable the credential (put on hold). Set to `false` to enable
    the credential (release from hold).
    """

    name: str
    """New name for the credential"""
