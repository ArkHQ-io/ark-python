# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmailCounts"]


class EmailCounts(BaseModel):
    """Email delivery counts"""

    bounced: int
    """Emails that bounced"""

    delivered: int
    """Emails successfully delivered"""

    hard_failed: int
    """Emails that hard-failed (permanent failures)"""

    held: int
    """Emails currently held for review"""

    sent: int
    """Total emails sent"""

    soft_failed: int
    """Emails that soft-failed (temporary failures, may be retried)"""
