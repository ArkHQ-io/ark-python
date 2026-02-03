# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UsageListByTenantParams"]


class UsageListByTenantParams(TypedDict, total=False):
    limit: int
    """Maximum number of tenants to return (1-100)"""

    min_sent: int
    """Only include tenants with at least this many emails sent"""

    offset: int
    """Number of tenants to skip for pagination"""

    period: str
    """Time period for usage data. Defaults to current month."""

    sort: Literal["sent", "-sent", "delivered", "-delivered", "bounce_rate", "-bounce_rate", "name", "-name"]
    """Sort order for results. Prefix with `-` for descending order."""

    status: Literal["active", "suspended", "archived"]
    """Filter by tenant status"""

    timezone: str
    """Timezone for period calculations (IANA format). Defaults to UTC."""
