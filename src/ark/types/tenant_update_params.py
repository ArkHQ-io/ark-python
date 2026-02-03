# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TenantUpdateParams"]


class TenantUpdateParams(TypedDict, total=False):
    metadata: Optional[Dict[str, Union[str, float, bool, None]]]
    """Custom key-value pairs. Useful for storing references to your internal systems.

    **Limits:**

    - Max 50 keys
    - Key names max 40 characters
    - String values max 500 characters
    - Total size max 8KB
    """

    name: str
    """Display name for the tenant"""

    status: Literal["active", "suspended", "archived"]
    """Tenant status"""
