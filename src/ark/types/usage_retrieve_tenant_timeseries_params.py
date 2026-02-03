# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UsageRetrieveTenantTimeseriesParams"]


class UsageRetrieveTenantTimeseriesParams(TypedDict, total=False):
    granularity: Literal["hour", "day", "week", "month"]
    """Time bucket size for data points"""

    period: str
    """Time period for timeseries data. Defaults to current month."""

    timezone: str
    """Timezone for period calculations (IANA format). Defaults to UTC."""
