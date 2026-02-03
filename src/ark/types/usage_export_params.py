# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UsageExportParams"]


class UsageExportParams(TypedDict, total=False):
    format: Literal["csv", "jsonl", "json"]
    """Export format"""

    min_sent: int
    """Only include tenants with at least this many emails sent"""

    period: str
    """Time period for export. Defaults to current month."""

    status: Literal["active", "suspended", "archived"]
    """Filter by tenant status"""

    timezone: str
    """Timezone for period calculations (IANA format). Defaults to UTC."""
