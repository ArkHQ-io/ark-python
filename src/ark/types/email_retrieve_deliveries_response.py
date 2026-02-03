# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.api_meta import APIMeta

__all__ = ["EmailRetrieveDeliveriesResponse", "Data", "DataDelivery", "DataRetryState"]


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


class DataRetryState(BaseModel):
    """
    Information about the current retry state of a message that is queued for delivery.
    Only present when the message is in the delivery queue.
    """

    attempt: int
    """Current attempt number (0-indexed).

    The first delivery attempt is 0, the first retry is 1, and so on.
    """

    attempts_remaining: int = FieldInfo(alias="attemptsRemaining")
    """
    Number of attempts remaining before the message is hard-failed. Calculated as
    `maxAttempts - attempt`.
    """

    manual: bool
    """
    Whether this queue entry was created by a manual retry request. Manual retries
    bypass certain hold conditions like suppression lists.
    """

    max_attempts: int = FieldInfo(alias="maxAttempts")
    """
    Maximum number of delivery attempts before the message is hard-failed.
    Configured at the server level.
    """

    processing: bool
    """
    Whether the message is currently being processed by a delivery worker. When
    `true`, the message is actively being sent.
    """

    next_retry_at: Optional[float] = FieldInfo(alias="nextRetryAt", default=None)
    """
    Unix timestamp of when the next retry attempt is scheduled. `null` if the
    message is ready for immediate processing or currently being processed.
    """

    next_retry_at_iso: Optional[datetime] = FieldInfo(alias="nextRetryAtIso", default=None)
    """
    ISO 8601 formatted timestamp of the next retry attempt. `null` if the message is
    ready for immediate processing.
    """


class Data(BaseModel):
    id: str
    """Message identifier (token)"""

    can_retry_manually: bool = FieldInfo(alias="canRetryManually")
    """
    Whether the message can be manually retried via `POST /emails/{emailId}/retry`.
    `true` when the raw message content is still available (not expired). Messages
    older than the retention period cannot be retried.
    """

    deliveries: List[DataDelivery]
    """
    Chronological list of delivery attempts for this message. Each attempt includes
    SMTP response codes and timestamps.
    """

    retry_state: Optional[DataRetryState] = FieldInfo(alias="retryState", default=None)
    """
    Information about the current retry state of a message that is queued for
    delivery. Only present when the message is in the delivery queue.
    """

    status: Literal["pending", "sent", "softfail", "hardfail", "held", "bounced"]
    """Current message status (lowercase). Possible values:

    - `pending` - Initial state, awaiting first delivery attempt
    - `sent` - Successfully delivered
    - `softfail` - Temporary failure, will retry automatically
    - `hardfail` - Permanent failure, will not retry
    - `held` - Held for manual review (suppression list, etc.)
    - `bounced` - Bounced by recipient server
    """


class EmailRetrieveDeliveriesResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
