# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import usage_export_params, usage_retrieve_params, usage_list_tenants_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPageNumberPagination, AsyncPageNumberPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.org_usage_summary import OrgUsageSummary
from ..types.tenant_usage_item import TenantUsageItem
from ..types.usage_export_response import UsageExportResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsageSummary:
        """Returns aggregated email sending statistics for your entire organization.

        For
        per-tenant breakdown, use `GET /usage/tenants`.

        **Use cases:**

        - Platform dashboards showing org-wide metrics
        - Quick health check on overall sending
        - Monitoring total volume and delivery rates

        **Response includes:**

        - `emails` - Aggregated email counts across all tenants
        - `rates` - Overall delivery and bounce rates
        - `tenants` - Tenant count summary (total, active, with activity)

        **Related endpoints:**

        - `GET /usage/tenants` - Paginated usage per tenant
        - `GET /usage/export` - Export usage data for billing
        - `GET /tenants/{tenantId}/usage` - Single tenant usage details
        - `GET /limits` - Rate limits and send limits

        Args:
          period: Time period for usage data.

              **Shortcuts:** `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
              `last_month`, `last_7_days`, `last_30_days`, `last_90_days`

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          timezone: Timezone for period calculations (IANA format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "period": period,
                        "timezone": timezone,
                    },
                    usage_retrieve_params.UsageRetrieveParams,
                ),
            ),
            cast_to=OrgUsageSummary,
        )

    def export(
        self,
        *,
        format: Literal["csv", "jsonl"] | Omit = omit,
        min_sent: int | Omit = omit,
        period: str | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageExportResponse:
        """Export email usage data for all tenants in CSV or JSON Lines format.

        Designed
        for billing system integration, data warehousing, and analytics.

        **Jobs to be done:**

        - Import usage data into billing systems (Stripe, Chargebee, etc.)
        - Load into data warehouses (Snowflake, BigQuery, etc.)
        - Process in spreadsheets (Excel, Google Sheets)
        - Feed into BI tools (Looker, Metabase, etc.)

        **Export formats:**

        - `csv` - UTF-8 with BOM for Excel compatibility (default)
        - `jsonl` - JSON Lines (one JSON object per line, streamable)

        **CSV columns:** `tenant_id`, `tenant_name`, `external_id`, `status`, `sent`,
        `delivered`, `soft_failed`, `hard_failed`, `bounced`, `held`, `delivery_rate`,
        `bounce_rate`, `period_start`, `period_end`

        **Response headers:**

        - `Content-Disposition` - Filename for download
        - `Content-Type` - `text/csv` or `application/x-ndjson`

        Args:
          format: Export format

          min_sent: Only include tenants with at least this many emails sent

          period: Time period for export.

              **Shortcuts:** `this_month`, `last_month`, `last_30_days`, etc.

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/usage/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "min_sent": min_sent,
                        "period": period,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_export_params.UsageExportParams,
                ),
            ),
            cast_to=UsageExportResponse,
        )

    def list_tenants(
        self,
        *,
        min_sent: int | Omit = omit,
        page: int | Omit = omit,
        period: str | Omit = omit,
        per_page: int | Omit = omit,
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
        | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPagination[TenantUsageItem]:
        """Returns email usage statistics for all tenants in your organization.

        Results are
        paginated with page-based navigation.

        **Jobs to be done:**

        - Generate monthly billing invoices per tenant
        - Build admin dashboards showing all customer usage
        - Identify high-volume or problematic tenants
        - Track usage against plan limits

        **Sorting options:**

        - `sent`, `-sent` - Sort by emails sent (ascending/descending)
        - `delivered`, `-delivered` - Sort by emails delivered
        - `bounce_rate`, `-bounce_rate` - Sort by bounce rate
        - `tenant_name`, `-tenant_name` - Sort alphabetically by tenant name

        **Filtering:**

        - `status` - Filter by tenant status (active, suspended, archived)
        - `minSent` - Only include tenants with at least N emails sent

        **Auto-pagination:** SDKs support iterating over all pages automatically.

        Args:
          min_sent: Only include tenants with at least this many emails sent

          page: Page number (1-indexed)

          period: Time period for usage data. Defaults to current month.

              **Shortcuts:** `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
              `last_month`, `last_7_days`, `last_30_days`, `last_90_days`

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          per_page: Results per page (max 100)

          sort: Sort order for results. Prefix with `-` for descending order.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/usage/tenants",
            page=SyncPageNumberPagination[TenantUsageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_sent": min_sent,
                        "page": page,
                        "period": period,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_list_tenants_params.UsageListTenantsParams,
                ),
            ),
            model=TenantUsageItem,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsageSummary:
        """Returns aggregated email sending statistics for your entire organization.

        For
        per-tenant breakdown, use `GET /usage/tenants`.

        **Use cases:**

        - Platform dashboards showing org-wide metrics
        - Quick health check on overall sending
        - Monitoring total volume and delivery rates

        **Response includes:**

        - `emails` - Aggregated email counts across all tenants
        - `rates` - Overall delivery and bounce rates
        - `tenants` - Tenant count summary (total, active, with activity)

        **Related endpoints:**

        - `GET /usage/tenants` - Paginated usage per tenant
        - `GET /usage/export` - Export usage data for billing
        - `GET /tenants/{tenantId}/usage` - Single tenant usage details
        - `GET /limits` - Rate limits and send limits

        Args:
          period: Time period for usage data.

              **Shortcuts:** `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
              `last_month`, `last_7_days`, `last_30_days`, `last_90_days`

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          timezone: Timezone for period calculations (IANA format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "period": period,
                        "timezone": timezone,
                    },
                    usage_retrieve_params.UsageRetrieveParams,
                ),
            ),
            cast_to=OrgUsageSummary,
        )

    async def export(
        self,
        *,
        format: Literal["csv", "jsonl"] | Omit = omit,
        min_sent: int | Omit = omit,
        period: str | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageExportResponse:
        """Export email usage data for all tenants in CSV or JSON Lines format.

        Designed
        for billing system integration, data warehousing, and analytics.

        **Jobs to be done:**

        - Import usage data into billing systems (Stripe, Chargebee, etc.)
        - Load into data warehouses (Snowflake, BigQuery, etc.)
        - Process in spreadsheets (Excel, Google Sheets)
        - Feed into BI tools (Looker, Metabase, etc.)

        **Export formats:**

        - `csv` - UTF-8 with BOM for Excel compatibility (default)
        - `jsonl` - JSON Lines (one JSON object per line, streamable)

        **CSV columns:** `tenant_id`, `tenant_name`, `external_id`, `status`, `sent`,
        `delivered`, `soft_failed`, `hard_failed`, `bounced`, `held`, `delivery_rate`,
        `bounce_rate`, `period_start`, `period_end`

        **Response headers:**

        - `Content-Disposition` - Filename for download
        - `Content-Type` - `text/csv` or `application/x-ndjson`

        Args:
          format: Export format

          min_sent: Only include tenants with at least this many emails sent

          period: Time period for export.

              **Shortcuts:** `this_month`, `last_month`, `last_30_days`, etc.

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/usage/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "min_sent": min_sent,
                        "period": period,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_export_params.UsageExportParams,
                ),
            ),
            cast_to=UsageExportResponse,
        )

    def list_tenants(
        self,
        *,
        min_sent: int | Omit = omit,
        page: int | Omit = omit,
        period: str | Omit = omit,
        per_page: int | Omit = omit,
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
        | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TenantUsageItem, AsyncPageNumberPagination[TenantUsageItem]]:
        """Returns email usage statistics for all tenants in your organization.

        Results are
        paginated with page-based navigation.

        **Jobs to be done:**

        - Generate monthly billing invoices per tenant
        - Build admin dashboards showing all customer usage
        - Identify high-volume or problematic tenants
        - Track usage against plan limits

        **Sorting options:**

        - `sent`, `-sent` - Sort by emails sent (ascending/descending)
        - `delivered`, `-delivered` - Sort by emails delivered
        - `bounce_rate`, `-bounce_rate` - Sort by bounce rate
        - `tenant_name`, `-tenant_name` - Sort alphabetically by tenant name

        **Filtering:**

        - `status` - Filter by tenant status (active, suspended, archived)
        - `minSent` - Only include tenants with at least N emails sent

        **Auto-pagination:** SDKs support iterating over all pages automatically.

        Args:
          min_sent: Only include tenants with at least this many emails sent

          page: Page number (1-indexed)

          period: Time period for usage data. Defaults to current month.

              **Shortcuts:** `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
              `last_month`, `last_7_days`, `last_30_days`, `last_90_days`

              **Month format:** `2024-01` (YYYY-MM)

              **Custom range:** `2024-01-01..2024-01-15`

          per_page: Results per page (max 100)

          sort: Sort order for results. Prefix with `-` for descending order.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/usage/tenants",
            page=AsyncPageNumberPagination[TenantUsageItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_sent": min_sent,
                        "page": page,
                        "period": period,
                        "per_page": per_page,
                        "sort": sort,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_list_tenants_params.UsageListTenantsParams,
                ),
            ),
            model=TenantUsageItem,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_raw_response_wrapper(
            usage.retrieve,
        )
        self.export = to_raw_response_wrapper(
            usage.export,
        )
        self.list_tenants = to_raw_response_wrapper(
            usage.list_tenants,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_raw_response_wrapper(
            usage.retrieve,
        )
        self.export = async_to_raw_response_wrapper(
            usage.export,
        )
        self.list_tenants = async_to_raw_response_wrapper(
            usage.list_tenants,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.export = to_streamed_response_wrapper(
            usage.export,
        )
        self.list_tenants = to_streamed_response_wrapper(
            usage.list_tenants,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.export = async_to_streamed_response_wrapper(
            usage.export,
        )
        self.list_tenants = async_to_streamed_response_wrapper(
            usage.list_tenants,
        )
