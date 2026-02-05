# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["UsagePeriod"]


class UsagePeriod(BaseModel):
    """Time period for usage data"""

    end: datetime
    """Period end (inclusive)"""

    start: datetime
    """Period start (inclusive)"""
