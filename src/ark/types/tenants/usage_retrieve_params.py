# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UsageRetrieveParams"]


class UsageRetrieveParams(TypedDict, total=False):
    period: str
    """Time period for usage data. Defaults to current month.

    **Formats:**

    - Shortcuts: `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
      `last_month`, `last_7_days`, `last_30_days`, `last_90_days`
    - Month: `2024-01`
    - Range: `2024-01-01..2024-01-31`
    - Day: `2024-01-15`
    """

    timezone: str
    """Timezone for period calculations (IANA format). Defaults to UTC."""
