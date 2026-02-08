# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.api_meta import APIMeta

__all__ = ["WebhookRetrieveDeliveryResponse", "Data", "DataRequest", "DataResponse"]


class DataRequest(BaseModel):
    """Request details"""

    headers: Optional[Dict[str, str]] = None
    """Request headers including signature"""

    payload: Optional[Dict[str, object]] = None
    """The complete webhook payload that was sent"""


class DataResponse(BaseModel):
    """Response details"""

    body: Optional[str] = None
    """Response body (truncated if too large)"""

    duration: Optional[int] = None
    """Response time in milliseconds"""


class Data(BaseModel):
    id: str
    """Unique delivery ID"""

    attempt: int
    """Attempt number"""

    event: str
    """Event type"""

    request: DataRequest
    """Request details"""

    response: DataResponse
    """Response details"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP status code from your endpoint"""

    success: bool
    """Whether delivery was successful"""

    tenant_id: str = FieldInfo(alias="tenantId")
    """Tenant that triggered the event"""

    timestamp: datetime
    """When delivery was attempted"""

    url: str
    """Endpoint URL"""

    webhook_id: str = FieldInfo(alias="webhookId")
    """Platform webhook ID"""

    webhook_name: str = FieldInfo(alias="webhookName")
    """Platform webhook name"""

    will_retry: bool = FieldInfo(alias="willRetry")
    """Whether this will be retried"""


class WebhookRetrieveDeliveryResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
