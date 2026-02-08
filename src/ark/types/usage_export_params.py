# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageExportParams"]


class UsageExportParams(TypedDict, total=False):
    format: Literal["csv", "jsonl"]
    """Export format"""

    min_sent: Annotated[int, PropertyInfo(alias="minSent")]
    """Only include tenants with at least this many emails sent"""

    period: str
    """Time period for export.

    **Shortcuts:** `this_month`, `last_month`, `last_30_days`, etc.

    **Month format:** `2024-01` (YYYY-MM)

    **Custom range:** `2024-01-01..2024-01-15`
    """

    status: Literal["active", "suspended", "archived"]
    """Filter by tenant status"""

    timezone: str
    """Timezone for period calculations (IANA format)"""
