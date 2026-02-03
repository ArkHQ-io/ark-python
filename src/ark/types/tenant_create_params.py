# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TenantCreateParams"]


class TenantCreateParams(TypedDict, total=False):
    name: Required[str]
    """Display name for the tenant (e.g., your customer's company name)"""

    metadata: Optional[Dict[str, Union[str, float, bool, None]]]
    """Custom key-value pairs. Useful for storing references to your internal systems.

    **Limits:**

    - Max 50 keys
    - Key names max 40 characters
    - String values max 500 characters
    - Total size max 8KB
    """
