# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enable or disable the webhook"""

    events: List[
        Literal[
            "MessageSent",
            "MessageDelayed",
            "MessageDeliveryFailed",
            "MessageHeld",
            "MessageBounced",
            "MessageLinkClicked",
            "MessageLoaded",
            "DomainDNSError",
        ]
    ]
    """Events to subscribe to. Empty array means all events."""

    name: str
    """Display name for the webhook"""

    url: str
    """Webhook endpoint URL (must be HTTPS)"""
