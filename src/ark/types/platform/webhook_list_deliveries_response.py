# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
    """Summary of a platform webhook delivery attempt"""

    id: str
    """Unique delivery ID"""

    attempt: int
    """Attempt number (1 for first attempt, higher for retries)"""

    event: Literal[
        "MessageSent",
        "MessageDelayed",
        "MessageDeliveryFailed",
        "MessageHeld",
        "MessageBounced",
        "MessageLinkClicked",
        "MessageLoaded",
        "DomainDNSError",
    ]
    """Event type"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP status code returned by your endpoint (null if connection failed)"""

    success: bool
    """Whether delivery was successful (2xx response)"""

    tenant_id: str = FieldInfo(alias="tenantId")
    """Tenant that triggered the event"""

    timestamp: datetime
    """When the delivery was attempted"""

    url: str
    """Endpoint URL the delivery was sent to"""

    webhook_id: str = FieldInfo(alias="webhookId")
    """Platform webhook ID"""

    will_retry: bool = FieldInfo(alias="willRetry")
    """Whether this delivery will be retried"""
