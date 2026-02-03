# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.api_meta import APIMeta

__all__ = [
    "EmailRetrieveResponse",
    "Data",
    "DataActivity",
    "DataActivityClick",
    "DataActivityOpen",
    "DataAttachment",
    "DataDelivery",
]


class DataActivityClick(BaseModel):
    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)
    """IP address of the clicker"""

    timestamp: Optional[float] = None
    """Unix timestamp of the click event"""

    timestamp_iso: Optional[datetime] = FieldInfo(alias="timestampIso", default=None)
    """ISO 8601 timestamp of the click event"""

    url: Optional[str] = None
    """URL that was clicked"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User agent of the email client"""


class DataActivityOpen(BaseModel):
    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)
    """IP address of the opener"""

    timestamp: Optional[float] = None
    """Unix timestamp of the open event"""

    timestamp_iso: Optional[datetime] = FieldInfo(alias="timestampIso", default=None)
    """ISO 8601 timestamp of the open event"""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """User agent of the email client"""


class DataActivity(BaseModel):
    """Opens and clicks tracking data (included if expand=activity)"""

    clicks: Optional[List[DataActivityClick]] = None
    """List of link click events"""

    opens: Optional[List[DataActivityOpen]] = None
    """List of email open events"""


class DataAttachment(BaseModel):
    """An email attachment retrieved from a sent message"""

    content_type: str = FieldInfo(alias="contentType")
    """MIME type of the attachment"""

    data: str
    """Base64 encoded attachment content. Decode this to get the raw file bytes."""

    filename: str
    """Original filename of the attachment"""

    hash: str
    """SHA256 hash of the attachment content for verification"""

    size: int
    """Size of the attachment in bytes"""


class DataDelivery(BaseModel):
    id: str
    """Delivery attempt ID"""

    status: str
    """Delivery status (lowercase)"""

    timestamp: float
    """Unix timestamp"""

    timestamp_iso: datetime = FieldInfo(alias="timestampIso")
    """ISO 8601 timestamp"""

    classification: Optional[
        Literal[
            "invalid_recipient",
            "mailbox_full",
            "message_too_large",
            "spam_block",
            "policy_violation",
            "no_mailbox",
            "not_accepting_mail",
            "temporarily_unavailable",
            "protocol_error",
            "tls_required",
            "connection_error",
            "dns_error",
            "unclassified",
        ]
    ] = None
    """
    Bounce classification category (present for failed deliveries). Helps understand
    why delivery failed for analytics and automated handling.
    """

    classification_code: Optional[int] = FieldInfo(alias="classificationCode", default=None)
    """
    Numeric bounce classification code for programmatic handling. Codes:
    10=invalid_recipient, 11=no_mailbox, 12=not_accepting_mail, 20=mailbox_full,
    21=message_too_large, 30=spam_block, 31=policy_violation, 32=tls_required,
    40=connection_error, 41=dns_error, 42=temporarily_unavailable,
    50=protocol_error, 99=unclassified
    """

    code: Optional[int] = None
    """SMTP response code"""

    details: Optional[str] = None
    """Human-readable delivery summary. Format varies by status:

    - **sent**: `Message for {recipient} accepted by {ip}:{port} ({hostname})`
    - **softfail/hardfail**:
      `{code} {classification}: Delivery to {recipient} failed at {ip}:{port} ({hostname})`
    """

    output: Optional[str] = None
    """Raw SMTP response from the receiving mail server"""

    remote_host: Optional[str] = FieldInfo(alias="remoteHost", default=None)
    """
    Hostname of the remote mail server that processed the delivery. Present for all
    delivery attempts (successful and failed).
    """

    sent_with_ssl: Optional[bool] = FieldInfo(alias="sentWithSsl", default=None)
    """Whether TLS was used"""

    smtp_enhanced_code: Optional[str] = FieldInfo(alias="smtpEnhancedCode", default=None)
    """
    RFC 3463 enhanced status code from SMTP response (e.g., "5.1.1", "4.2.2"). First
    digit: 2=success, 4=temporary, 5=permanent. Second digit: category (1=address,
    2=mailbox, 7=security, etc.).
    """


class Data(BaseModel):
    id: str
    """Unique message identifier (token)"""

    from_: str = FieldInfo(alias="from")
    """Sender address"""

    scope: Literal["outgoing", "incoming"]
    """Message direction"""

    status: Literal["pending", "sent", "softfail", "hardfail", "bounced", "held"]
    """Current delivery status:

    - `pending` - Email accepted, waiting to be processed
    - `sent` - Email transmitted to recipient's mail server
    - `softfail` - Temporary delivery failure, will retry
    - `hardfail` - Permanent delivery failure
    - `bounced` - Email bounced back
    - `held` - Held for manual review
    """

    subject: str
    """Email subject line"""

    timestamp: float
    """Unix timestamp when the email was sent"""

    timestamp_iso: datetime = FieldInfo(alias="timestampIso")
    """ISO 8601 formatted timestamp"""

    to: str
    """Recipient address"""

    activity: Optional[DataActivity] = None
    """Opens and clicks tracking data (included if expand=activity)"""

    attachments: Optional[List[DataAttachment]] = None
    """File attachments (included if expand=attachments)"""

    deliveries: Optional[List[DataDelivery]] = None
    """Delivery attempt history (included if expand=deliveries)"""

    headers: Optional[Dict[str, str]] = None
    """Email headers (included if expand=headers)"""

    html_body: Optional[str] = FieldInfo(alias="htmlBody", default=None)
    """HTML body content (included if expand=content)"""

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """SMTP Message-ID header"""

    plain_body: Optional[str] = FieldInfo(alias="plainBody", default=None)
    """Plain text body (included if expand=content)"""

    raw_message: Optional[str] = FieldInfo(alias="rawMessage", default=None)
    """
    Complete raw MIME message, base64 encoded (included if expand=raw). Decode this
    to get the original RFC 2822 formatted email.
    """

    spam: Optional[bool] = None
    """Whether the message was flagged as spam"""

    spam_score: Optional[float] = FieldInfo(alias="spamScore", default=None)
    """Spam score (if applicable)"""

    tag: Optional[str] = None
    """Optional categorization tag"""


class EmailRetrieveResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
