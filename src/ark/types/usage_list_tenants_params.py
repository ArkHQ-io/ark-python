# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageListTenantsParams"]


class UsageListTenantsParams(TypedDict, total=False):
    min_sent: Annotated[int, PropertyInfo(alias="minSent")]
    """Only include tenants with at least this many emails sent"""

    page: int
    """Page number (1-indexed)"""

    period: str
    """Time period for usage data. Defaults to current month.

    **Shortcuts:** `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
    `last_month`, `last_7_days`, `last_30_days`, `last_90_days`

    **Month format:** `2024-01` (YYYY-MM)

    **Custom range:** `2024-01-01..2024-01-15`
    """

    per_page: Annotated[int, PropertyInfo(alias="perPage")]
    """Results per page (max 100)"""

    sort: Literal[
        "sent",
        "-sent",
        "delivered",
        "-delivered",
        "bounce_rate",
        "-bounce_rate",
        "delivery_rate",
        "-delivery_rate",
        "tenant_name",
        "-tenant_name",
    ]
    """Sort order for results. Prefix with `-` for descending order."""

    status: Literal["active", "suspended", "archived"]
    """Filter by tenant status"""

    timezone: str
    """Timezone for period calculations (IANA format). Defaults to UTC."""
