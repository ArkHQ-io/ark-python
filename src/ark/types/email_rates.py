# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EmailRates"]


class EmailRates(BaseModel):
    """Email delivery rates (as decimals, e.g., 0.95 = 95%)"""

    bounce_rate: float
    """Percentage of sent emails that bounced (0-1)"""

    delivery_rate: float
    """Percentage of sent emails that were delivered (0-1)"""
