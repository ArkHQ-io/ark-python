# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..types import (
    usage_export_params,
    usage_list_by_tenant_params,
    usage_retrieve_tenant_usage_params,
    usage_retrieve_tenant_timeseries_params,
)
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
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.bulk_tenant_usage import Tenant
from ..types.usage_export_response import UsageExportResponse
from ..types.usage_retrieve_response import UsageRetrieveResponse
from ..types.usage_retrieve_tenant_usage_response import UsageRetrieveTenantUsageResponse
from ..types.usage_retrieve_tenant_timeseries_response import UsageRetrieveTenantTimeseriesResponse

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

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveResponse:
        """
        > **Deprecated:** Use `GET /limits` instead for rate limits and send limits.
        > This endpoint will be removed in a future version.

        Returns current usage and limit information for your account.

        This endpoint is designed for:

        - **AI agents/MCP servers:** Check constraints before planning batch operations
        - **Monitoring dashboards:** Display current usage status
        - **Rate limit awareness:** Know remaining capacity before making requests

        **Response includes:**

        - `rateLimit` - API request rate limit (requests per second)
        - `sendLimit` - Email sending limit (emails per hour)
        - `billing` - Credit balance and auto-recharge configuration

        **Notes:**

        - This request counts against your rate limit
        - `sendLimit` may be null if Postal is temporarily unavailable
        - `billing` is null if billing is not configured
        - Send limit resets at the top of each hour

        **Migration:**

        - For rate limits and send limits, use `GET /limits`
        - For per-tenant usage analytics, use `GET /tenants/{tenantId}/usage`
        - For bulk tenant usage, use `GET /usage/by-tenant`
        """
        return self._get(
            "/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageRetrieveResponse,
        )

    def export(
        self,
        *,
        format: Literal["csv", "jsonl", "json"] | Omit = omit,
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
        """
        Export usage data for all tenants in a format suitable for billing systems.

        **Use cases:**

        - Import into billing systems (Stripe, Chargebee, etc.)
        - Generate invoices
        - Archive usage data

        **Export formats:**

        - `csv` - Comma-separated values (default)
        - `jsonl` - JSON Lines (one JSON object per line)
        - `json` - JSON array

        **Response headers:**

        - `X-Total-Tenants` - Total number of tenants in export
        - `X-Total-Sent` - Total emails sent across all tenants
        - `Content-Disposition` - Suggested filename for download

        This endpoint returns up to 10,000 tenants per request. For organizations with
        more tenants, use the `/usage/by-tenant` endpoint with pagination.

        Args:
          format: Export format

          min_sent: Only include tenants with at least this many emails sent

          period: Time period for export. Defaults to current month.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

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

    def list_by_tenant(
        self,
        *,
        limit: int | Omit = omit,
        min_sent: int | Omit = omit,
        offset: int | Omit = omit,
        period: str | Omit = omit,
        sort: Literal["sent", "-sent", "delivered", "-delivered", "bounce_rate", "-bounce_rate", "name", "-name"]
        | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[Tenant]:
        """
        Returns email usage statistics for all tenants in your organization.

        **Use cases:**

        - Generate monthly billing reports
        - Build admin dashboards showing all customer usage
        - Identify high-volume or problematic tenants

        **Sorting options:**

        - `sent`, `-sent` - Sort by emails sent (ascending/descending)
        - `delivered`, `-delivered` - Sort by emails delivered
        - `bounce_rate`, `-bounce_rate` - Sort by bounce rate
        - `name`, `-name` - Sort alphabetically by tenant name

        **Filtering:**

        - `status` - Filter by tenant status (active, suspended, archived)
        - `min_sent` - Only include tenants with at least N emails sent

        Results are paginated. Use `limit` and `offset` for pagination.

        Args:
          limit: Maximum number of tenants to return (1-100)

          min_sent: Only include tenants with at least this many emails sent

          offset: Number of tenants to skip for pagination

          period: Time period for usage data. Defaults to current month.

          sort: Sort order for results. Prefix with `-` for descending order.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/usage/by-tenant",
            page=SyncOffsetPagination[Tenant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_sent": min_sent,
                        "offset": offset,
                        "period": period,
                        "sort": sort,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_list_by_tenant_params.UsageListByTenantParams,
                ),
            ),
            model=Tenant,
        )

    def retrieve_tenant_timeseries(
        self,
        tenant_id: str,
        *,
        granularity: Literal["hour", "day", "week", "month"] | Omit = omit,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveTenantTimeseriesResponse:
        """
        Returns time-bucketed email statistics for a specific tenant.

        **Use cases:**

        - Build usage charts and graphs
        - Identify sending patterns
        - Detect anomalies in delivery rates

        **Granularity options:**

        - `hour` - Hourly buckets (best for last 7 days)
        - `day` - Daily buckets (best for last 30-90 days)
        - `week` - Weekly buckets (best for last 6 months)
        - `month` - Monthly buckets (best for year-over-year)

        The response includes a data point for each time bucket with all email metrics.

        Args:
          granularity: Time bucket size for data points

          period: Time period for timeseries data. Defaults to current month.

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/tenants/{tenant_id}/usage/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "granularity": granularity,
                        "period": period,
                        "timezone": timezone,
                    },
                    usage_retrieve_tenant_timeseries_params.UsageRetrieveTenantTimeseriesParams,
                ),
            ),
            cast_to=UsageRetrieveTenantTimeseriesResponse,
        )

    def retrieve_tenant_usage(
        self,
        tenant_id: str,
        *,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveTenantUsageResponse:
        """
        Returns email sending statistics for a specific tenant over a time period.

        **Use cases:**

        - Display usage dashboard to your customers
        - Calculate per-tenant billing
        - Monitor tenant health and delivery rates

        **Period formats:**

        - Shortcuts: `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
          `last_month`, `last_7_days`, `last_30_days`, `last_90_days`
        - Month: `2024-01` (full month)
        - Date range: `2024-01-01..2024-01-31`
        - Single day: `2024-01-15`

        **Response includes:**

        - `emails` - Counts for sent, delivered, soft_failed, hard_failed, bounced, held
        - `rates` - Delivery rate and bounce rate as decimals (0.95 = 95%)

        Args:
          period: Time period for usage data. Defaults to current month.

              **Formats:**

              - Shortcuts: `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
                `last_month`, `last_7_days`, `last_30_days`, `last_90_days`
              - Month: `2024-01`
              - Range: `2024-01-01..2024-01-31`
              - Day: `2024-01-15`

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/tenants/{tenant_id}/usage",
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
                    usage_retrieve_tenant_usage_params.UsageRetrieveTenantUsageParams,
                ),
            ),
            cast_to=UsageRetrieveTenantUsageResponse,
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

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveResponse:
        """
        > **Deprecated:** Use `GET /limits` instead for rate limits and send limits.
        > This endpoint will be removed in a future version.

        Returns current usage and limit information for your account.

        This endpoint is designed for:

        - **AI agents/MCP servers:** Check constraints before planning batch operations
        - **Monitoring dashboards:** Display current usage status
        - **Rate limit awareness:** Know remaining capacity before making requests

        **Response includes:**

        - `rateLimit` - API request rate limit (requests per second)
        - `sendLimit` - Email sending limit (emails per hour)
        - `billing` - Credit balance and auto-recharge configuration

        **Notes:**

        - This request counts against your rate limit
        - `sendLimit` may be null if Postal is temporarily unavailable
        - `billing` is null if billing is not configured
        - Send limit resets at the top of each hour

        **Migration:**

        - For rate limits and send limits, use `GET /limits`
        - For per-tenant usage analytics, use `GET /tenants/{tenantId}/usage`
        - For bulk tenant usage, use `GET /usage/by-tenant`
        """
        return await self._get(
            "/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageRetrieveResponse,
        )

    async def export(
        self,
        *,
        format: Literal["csv", "jsonl", "json"] | Omit = omit,
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
        """
        Export usage data for all tenants in a format suitable for billing systems.

        **Use cases:**

        - Import into billing systems (Stripe, Chargebee, etc.)
        - Generate invoices
        - Archive usage data

        **Export formats:**

        - `csv` - Comma-separated values (default)
        - `jsonl` - JSON Lines (one JSON object per line)
        - `json` - JSON array

        **Response headers:**

        - `X-Total-Tenants` - Total number of tenants in export
        - `X-Total-Sent` - Total emails sent across all tenants
        - `Content-Disposition` - Suggested filename for download

        This endpoint returns up to 10,000 tenants per request. For organizations with
        more tenants, use the `/usage/by-tenant` endpoint with pagination.

        Args:
          format: Export format

          min_sent: Only include tenants with at least this many emails sent

          period: Time period for export. Defaults to current month.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

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

    def list_by_tenant(
        self,
        *,
        limit: int | Omit = omit,
        min_sent: int | Omit = omit,
        offset: int | Omit = omit,
        period: str | Omit = omit,
        sort: Literal["sent", "-sent", "delivered", "-delivered", "bounce_rate", "-bounce_rate", "name", "-name"]
        | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Tenant, AsyncOffsetPagination[Tenant]]:
        """
        Returns email usage statistics for all tenants in your organization.

        **Use cases:**

        - Generate monthly billing reports
        - Build admin dashboards showing all customer usage
        - Identify high-volume or problematic tenants

        **Sorting options:**

        - `sent`, `-sent` - Sort by emails sent (ascending/descending)
        - `delivered`, `-delivered` - Sort by emails delivered
        - `bounce_rate`, `-bounce_rate` - Sort by bounce rate
        - `name`, `-name` - Sort alphabetically by tenant name

        **Filtering:**

        - `status` - Filter by tenant status (active, suspended, archived)
        - `min_sent` - Only include tenants with at least N emails sent

        Results are paginated. Use `limit` and `offset` for pagination.

        Args:
          limit: Maximum number of tenants to return (1-100)

          min_sent: Only include tenants with at least this many emails sent

          offset: Number of tenants to skip for pagination

          period: Time period for usage data. Defaults to current month.

          sort: Sort order for results. Prefix with `-` for descending order.

          status: Filter by tenant status

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/usage/by-tenant",
            page=AsyncOffsetPagination[Tenant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_sent": min_sent,
                        "offset": offset,
                        "period": period,
                        "sort": sort,
                        "status": status,
                        "timezone": timezone,
                    },
                    usage_list_by_tenant_params.UsageListByTenantParams,
                ),
            ),
            model=Tenant,
        )

    async def retrieve_tenant_timeseries(
        self,
        tenant_id: str,
        *,
        granularity: Literal["hour", "day", "week", "month"] | Omit = omit,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveTenantTimeseriesResponse:
        """
        Returns time-bucketed email statistics for a specific tenant.

        **Use cases:**

        - Build usage charts and graphs
        - Identify sending patterns
        - Detect anomalies in delivery rates

        **Granularity options:**

        - `hour` - Hourly buckets (best for last 7 days)
        - `day` - Daily buckets (best for last 30-90 days)
        - `week` - Weekly buckets (best for last 6 months)
        - `month` - Monthly buckets (best for year-over-year)

        The response includes a data point for each time bucket with all email metrics.

        Args:
          granularity: Time bucket size for data points

          period: Time period for timeseries data. Defaults to current month.

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/tenants/{tenant_id}/usage/timeseries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "granularity": granularity,
                        "period": period,
                        "timezone": timezone,
                    },
                    usage_retrieve_tenant_timeseries_params.UsageRetrieveTenantTimeseriesParams,
                ),
            ),
            cast_to=UsageRetrieveTenantTimeseriesResponse,
        )

    async def retrieve_tenant_usage(
        self,
        tenant_id: str,
        *,
        period: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageRetrieveTenantUsageResponse:
        """
        Returns email sending statistics for a specific tenant over a time period.

        **Use cases:**

        - Display usage dashboard to your customers
        - Calculate per-tenant billing
        - Monitor tenant health and delivery rates

        **Period formats:**

        - Shortcuts: `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
          `last_month`, `last_7_days`, `last_30_days`, `last_90_days`
        - Month: `2024-01` (full month)
        - Date range: `2024-01-01..2024-01-31`
        - Single day: `2024-01-15`

        **Response includes:**

        - `emails` - Counts for sent, delivered, soft_failed, hard_failed, bounced, held
        - `rates` - Delivery rate and bounce rate as decimals (0.95 = 95%)

        Args:
          period: Time period for usage data. Defaults to current month.

              **Formats:**

              - Shortcuts: `today`, `yesterday`, `this_week`, `last_week`, `this_month`,
                `last_month`, `last_7_days`, `last_30_days`, `last_90_days`
              - Month: `2024-01`
              - Range: `2024-01-01..2024-01-31`
              - Day: `2024-01-15`

          timezone: Timezone for period calculations (IANA format). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/tenants/{tenant_id}/usage",
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
                    usage_retrieve_tenant_usage_params.UsageRetrieveTenantUsageParams,
                ),
            ),
            cast_to=UsageRetrieveTenantUsageResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                usage.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.export = to_raw_response_wrapper(
            usage.export,
        )
        self.list_by_tenant = to_raw_response_wrapper(
            usage.list_by_tenant,
        )
        self.retrieve_tenant_timeseries = to_raw_response_wrapper(
            usage.retrieve_tenant_timeseries,
        )
        self.retrieve_tenant_usage = to_raw_response_wrapper(
            usage.retrieve_tenant_usage,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                usage.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.export = async_to_raw_response_wrapper(
            usage.export,
        )
        self.list_by_tenant = async_to_raw_response_wrapper(
            usage.list_by_tenant,
        )
        self.retrieve_tenant_timeseries = async_to_raw_response_wrapper(
            usage.retrieve_tenant_timeseries,
        )
        self.retrieve_tenant_usage = async_to_raw_response_wrapper(
            usage.retrieve_tenant_usage,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                usage.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.export = to_streamed_response_wrapper(
            usage.export,
        )
        self.list_by_tenant = to_streamed_response_wrapper(
            usage.list_by_tenant,
        )
        self.retrieve_tenant_timeseries = to_streamed_response_wrapper(
            usage.retrieve_tenant_timeseries,
        )
        self.retrieve_tenant_usage = to_streamed_response_wrapper(
            usage.retrieve_tenant_usage,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                usage.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.export = async_to_streamed_response_wrapper(
            usage.export,
        )
        self.list_by_tenant = async_to_streamed_response_wrapper(
            usage.list_by_tenant,
        )
        self.retrieve_tenant_timeseries = async_to_streamed_response_wrapper(
            usage.retrieve_tenant_timeseries,
        )
        self.retrieve_tenant_usage = async_to_streamed_response_wrapper(
            usage.retrieve_tenant_usage,
        )
