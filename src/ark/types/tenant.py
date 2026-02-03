# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tenant"]


class Tenant(BaseModel):
    id: str
    """Unique identifier for the tenant"""

    created_at: datetime
    """When the tenant was created"""

    metadata: Dict[str, Union[str, float, bool, None]]
    """Custom key-value pairs for storing additional data"""

    name: str
    """Display name for the tenant"""

    status: Literal["active", "suspended", "archived"]
    """Current status of the tenant:

    - `active` - Normal operation
    - `suspended` - Temporarily disabled
    - `archived` - Soft-deleted
    """

    updated_at: datetime
    """When the tenant was last updated"""
