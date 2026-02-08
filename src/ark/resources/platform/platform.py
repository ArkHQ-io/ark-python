# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PlatformResource", "AsyncPlatformResource"]


class PlatformResource(SyncAPIResource):
    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> PlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return PlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return PlatformResourceWithStreamingResponse(self)


class AsyncPlatformResource(AsyncAPIResource):
    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncPlatformResourceWithStreamingResponse(self)


class PlatformResourceWithRawResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._platform.webhooks)


class AsyncPlatformResourceWithRawResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._platform.webhooks)


class PlatformResourceWithStreamingResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._platform.webhooks)


class AsyncPlatformResourceWithStreamingResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._platform.webhooks)
