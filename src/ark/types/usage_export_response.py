# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["UsageExportResponse", "UsageExportResponseItem"]


class UsageExportResponseItem(BaseModel):
    """Single row in usage export (JSON format)"""

    bounce_rate: float
    """Bounce rate (0-1)"""

    bounced: int
    """Emails that bounced"""

    delivered: int
    """Emails successfully delivered"""

    delivery_rate: float
    """Delivery rate (0-1)"""

    hard_failed: int
    """Emails that hard-failed"""

    held: int
    """Emails currently held"""

    sent: int
    """Total emails sent"""

    soft_failed: int
    """Emails that soft-failed"""

    status: Literal["active", "suspended", "archived"]
    """Current tenant status"""

    tenant_id: str
    """Unique tenant identifier"""

    tenant_name: str
    """Tenant display name"""

    external_id: Optional[str] = None
    """Your external ID for this tenant"""


UsageExportResponse: TypeAlias = List[UsageExportResponseItem]
