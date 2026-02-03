# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.limit_retrieve_response import LimitRetrieveResponse

__all__ = ["LimitsResource", "AsyncLimitsResource"]


class LimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return LimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return LimitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LimitRetrieveResponse:
        """
        Returns current rate limit and send limit information for your account.

        This endpoint is the recommended way to check your account's operational limits.
        Use `/usage` endpoints for historical usage analytics.

        **Response includes:**

        - `rateLimit` - API request rate limit (requests per second)
        - `sendLimit` - Email sending limit (emails per hour)
        - `billing` - Credit balance and auto-recharge configuration

        **Notes:**

        - This request counts against your rate limit
        - `sendLimit` may be null if Postal is temporarily unavailable
        - `billing` is null if billing is not configured
        - Send limit resets at the top of each hour
        """
        return self._get(
            "/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LimitRetrieveResponse,
        )


class AsyncLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncLimitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LimitRetrieveResponse:
        """
        Returns current rate limit and send limit information for your account.

        This endpoint is the recommended way to check your account's operational limits.
        Use `/usage` endpoints for historical usage analytics.

        **Response includes:**

        - `rateLimit` - API request rate limit (requests per second)
        - `sendLimit` - Email sending limit (emails per hour)
        - `billing` - Credit balance and auto-recharge configuration

        **Notes:**

        - This request counts against your rate limit
        - `sendLimit` may be null if Postal is temporarily unavailable
        - `billing` is null if billing is not configured
        - Send limit resets at the top of each hour
        """
        return await self._get(
            "/limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LimitRetrieveResponse,
        )


class LimitsResourceWithRawResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.retrieve = to_raw_response_wrapper(
            limits.retrieve,
        )


class AsyncLimitsResourceWithRawResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.retrieve = async_to_raw_response_wrapper(
            limits.retrieve,
        )


class LimitsResourceWithStreamingResponse:
    def __init__(self, limits: LimitsResource) -> None:
        self._limits = limits

        self.retrieve = to_streamed_response_wrapper(
            limits.retrieve,
        )


class AsyncLimitsResourceWithStreamingResponse:
    def __init__(self, limits: AsyncLimitsResource) -> None:
        self._limits = limits

        self.retrieve = async_to_streamed_response_wrapper(
            limits.retrieve,
        )
