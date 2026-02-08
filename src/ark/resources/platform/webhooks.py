# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPageNumberPagination, AsyncPageNumberPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.platform import (
    webhook_test_params,
    webhook_create_params,
    webhook_update_params,
    webhook_list_deliveries_params,
)
from ...types.platform.webhook_list_response import WebhookListResponse
from ...types.platform.webhook_test_response import WebhookTestResponse
from ...types.platform.webhook_create_response import WebhookCreateResponse
from ...types.platform.webhook_delete_response import WebhookDeleteResponse
from ...types.platform.webhook_update_response import WebhookUpdateResponse
from ...types.platform.webhook_retrieve_response import WebhookRetrieveResponse
from ...types.platform.webhook_list_deliveries_response import WebhookListDeliveriesResponse
from ...types.platform.webhook_replay_delivery_response import WebhookReplayDeliveryResponse
from ...types.platform.webhook_retrieve_delivery_response import WebhookRetrieveDeliveryResponse

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        url: str,
        events: List[
            Literal[
                "MessageSent",
                "MessageDelayed",
                "MessageDeliveryFailed",
                "MessageHeld",
                "MessageBounced",
                "MessageLinkClicked",
                "MessageLoaded",
                "DomainDNSError",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Create a platform webhook to receive email event notifications from all tenants.

        Platform webhooks receive events from **all tenants** in your organization. Each
        webhook payload includes a `tenant_id` field to identify which tenant the event
        belongs to.

        **Available events:**

        - `MessageSent` - Email accepted by recipient server
        - `MessageDeliveryFailed` - Delivery permanently failed
        - `MessageDelayed` - Delivery temporarily failed, will retry
        - `MessageBounced` - Email bounced
        - `MessageHeld` - Email held for review
        - `MessageLinkClicked` - Recipient clicked a link
        - `MessageLoaded` - Recipient opened the email
        - `DomainDNSError` - Domain DNS issue detected

        **Webhook payload includes:**

        - `event` - The event type
        - `tenant_id` - The tenant that sent the email
        - `timestamp` - Unix timestamp of the event
        - `payload` - Event-specific data (message details, status, etc.)

        Args:
          name: Display name for the webhook

          url: Webhook endpoint URL (must be HTTPS)

          events: Events to subscribe to. Empty array means all events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/platform/webhooks",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "events": events,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Get detailed information about a specific platform webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._get(
            f"/platform/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    def update(
        self,
        webhook_id: str,
        *,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "MessageSent",
                "MessageDelayed",
                "MessageDeliveryFailed",
                "MessageHeld",
                "MessageBounced",
                "MessageLinkClicked",
                "MessageLoaded",
                "DomainDNSError",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a platform webhook's configuration.

        You can update:

        - `name` - Display name for the webhook
        - `url` - The endpoint URL (must be HTTPS)
        - `events` - Array of event types to receive (empty array = all events)
        - `enabled` - Enable or disable the webhook

        Args:
          enabled: Enable or disable the webhook

          events: Events to subscribe to. Empty array means all events.

          name: Display name for the webhook

          url: Webhook endpoint URL (must be HTTPS)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._patch(
            f"/platform/webhooks/{webhook_id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "events": events,
                    "name": name,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Get all platform webhook endpoints configured for your organization.

        Platform webhooks receive events from **all tenants** in your organization,
        unlike tenant webhooks which only receive events for a specific tenant. This is
        useful for centralized event processing and monitoring.
        """
        return self._get(
            "/platform/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Delete a platform webhook.

        This stops all event delivery to the webhook URL.
        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._delete(
            f"/platform/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_deliveries(
        self,
        *,
        after: int | Omit = omit,
        before: int | Omit = omit,
        event: Literal[
            "MessageSent",
            "MessageDelayed",
            "MessageDeliveryFailed",
            "MessageHeld",
            "MessageBounced",
            "MessageLinkClicked",
            "MessageLoaded",
            "DomainDNSError",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        success: bool | Omit = omit,
        tenant_id: str | Omit = omit,
        webhook_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPagination[WebhookListDeliveriesResponse]:
        """
        Get a paginated list of platform webhook delivery attempts.

        Filter by:

        - `webhookId` - Specific webhook
        - `tenantId` - Specific tenant
        - `event` - Specific event type
        - `success` - Successful (2xx) or failed deliveries
        - `before`/`after` - Time range (Unix timestamps)

        Deliveries are returned in reverse chronological order.

        Args:
          after: Only deliveries after this Unix timestamp

          before: Only deliveries before this Unix timestamp

          event: Filter by event type

          page: Page number (default 1)

          per_page: Items per page (default 30, max 100)

          success: Filter by delivery success

          tenant_id: Filter by tenant ID

          webhook_id: Filter by platform webhook ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/platform/webhooks/deliveries",
            page=SyncPageNumberPagination[WebhookListDeliveriesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "event": event,
                        "page": page,
                        "per_page": per_page,
                        "success": success,
                        "tenant_id": tenant_id,
                        "webhook_id": webhook_id,
                    },
                    webhook_list_deliveries_params.WebhookListDeliveriesParams,
                ),
            ),
            model=WebhookListDeliveriesResponse,
        )

    def replay_delivery(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookReplayDeliveryResponse:
        """
        Replay a previous platform webhook delivery.

        This re-sends the original payload with a new timestamp and delivery ID. Useful
        for recovering from temporary endpoint failures.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._post(
            f"/platform/webhooks/deliveries/{delivery_id}/replay",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReplayDeliveryResponse,
        )

    def retrieve_delivery(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveDeliveryResponse:
        """
        Get detailed information about a specific platform webhook delivery.

        Returns the complete request payload, headers, response, and timing info.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            f"/platform/webhooks/deliveries/{delivery_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveDeliveryResponse,
        )

    def test(
        self,
        webhook_id: str,
        *,
        event: Literal[
            "MessageSent",
            "MessageDelayed",
            "MessageDeliveryFailed",
            "MessageHeld",
            "MessageBounced",
            "MessageLinkClicked",
            "MessageLoaded",
            "DomainDNSError",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTestResponse:
        """
        Send a test payload to your platform webhook endpoint.

        Use this to:

        - Verify your webhook URL is accessible
        - Test your payload handling code
        - Ensure your server responds correctly

        The test payload is marked with `_test: true` so you can distinguish test events
        from real events.

        Args:
          event: Event type to simulate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return self._post(
            f"/platform/webhooks/{webhook_id}/test",
            body=maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTestResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        url: str,
        events: List[
            Literal[
                "MessageSent",
                "MessageDelayed",
                "MessageDeliveryFailed",
                "MessageHeld",
                "MessageBounced",
                "MessageLinkClicked",
                "MessageLoaded",
                "DomainDNSError",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookCreateResponse:
        """
        Create a platform webhook to receive email event notifications from all tenants.

        Platform webhooks receive events from **all tenants** in your organization. Each
        webhook payload includes a `tenant_id` field to identify which tenant the event
        belongs to.

        **Available events:**

        - `MessageSent` - Email accepted by recipient server
        - `MessageDeliveryFailed` - Delivery permanently failed
        - `MessageDelayed` - Delivery temporarily failed, will retry
        - `MessageBounced` - Email bounced
        - `MessageHeld` - Email held for review
        - `MessageLinkClicked` - Recipient clicked a link
        - `MessageLoaded` - Recipient opened the email
        - `DomainDNSError` - Domain DNS issue detected

        **Webhook payload includes:**

        - `event` - The event type
        - `tenant_id` - The tenant that sent the email
        - `timestamp` - Unix timestamp of the event
        - `payload` - Event-specific data (message details, status, etc.)

        Args:
          name: Display name for the webhook

          url: Webhook endpoint URL (must be HTTPS)

          events: Events to subscribe to. Empty array means all events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/platform/webhooks",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                    "events": events,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookCreateResponse,
        )

    async def retrieve(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveResponse:
        """
        Get detailed information about a specific platform webhook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._get(
            f"/platform/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveResponse,
        )

    async def update(
        self,
        webhook_id: str,
        *,
        enabled: bool | Omit = omit,
        events: List[
            Literal[
                "MessageSent",
                "MessageDelayed",
                "MessageDeliveryFailed",
                "MessageHeld",
                "MessageBounced",
                "MessageLinkClicked",
                "MessageLoaded",
                "DomainDNSError",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookUpdateResponse:
        """
        Update a platform webhook's configuration.

        You can update:

        - `name` - Display name for the webhook
        - `url` - The endpoint URL (must be HTTPS)
        - `events` - Array of event types to receive (empty array = all events)
        - `enabled` - Enable or disable the webhook

        Args:
          enabled: Enable or disable the webhook

          events: Events to subscribe to. Empty array means all events.

          name: Display name for the webhook

          url: Webhook endpoint URL (must be HTTPS)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._patch(
            f"/platform/webhooks/{webhook_id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "events": events,
                    "name": name,
                    "url": url,
                },
                webhook_update_params.WebhookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookListResponse:
        """
        Get all platform webhook endpoints configured for your organization.

        Platform webhooks receive events from **all tenants** in your organization,
        unlike tenant webhooks which only receive events for a specific tenant. This is
        useful for centralized event processing and monitoring.
        """
        return await self._get(
            "/platform/webhooks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookListResponse,
        )

    async def delete(
        self,
        webhook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookDeleteResponse:
        """Delete a platform webhook.

        This stops all event delivery to the webhook URL.
        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._delete(
            f"/platform/webhooks/{webhook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeleteResponse,
        )

    def list_deliveries(
        self,
        *,
        after: int | Omit = omit,
        before: int | Omit = omit,
        event: Literal[
            "MessageSent",
            "MessageDelayed",
            "MessageDeliveryFailed",
            "MessageHeld",
            "MessageBounced",
            "MessageLinkClicked",
            "MessageLoaded",
            "DomainDNSError",
        ]
        | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        success: bool | Omit = omit,
        tenant_id: str | Omit = omit,
        webhook_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookListDeliveriesResponse, AsyncPageNumberPagination[WebhookListDeliveriesResponse]]:
        """
        Get a paginated list of platform webhook delivery attempts.

        Filter by:

        - `webhookId` - Specific webhook
        - `tenantId` - Specific tenant
        - `event` - Specific event type
        - `success` - Successful (2xx) or failed deliveries
        - `before`/`after` - Time range (Unix timestamps)

        Deliveries are returned in reverse chronological order.

        Args:
          after: Only deliveries after this Unix timestamp

          before: Only deliveries before this Unix timestamp

          event: Filter by event type

          page: Page number (default 1)

          per_page: Items per page (default 30, max 100)

          success: Filter by delivery success

          tenant_id: Filter by tenant ID

          webhook_id: Filter by platform webhook ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/platform/webhooks/deliveries",
            page=AsyncPageNumberPagination[WebhookListDeliveriesResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "event": event,
                        "page": page,
                        "per_page": per_page,
                        "success": success,
                        "tenant_id": tenant_id,
                        "webhook_id": webhook_id,
                    },
                    webhook_list_deliveries_params.WebhookListDeliveriesParams,
                ),
            ),
            model=WebhookListDeliveriesResponse,
        )

    async def replay_delivery(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookReplayDeliveryResponse:
        """
        Replay a previous platform webhook delivery.

        This re-sends the original payload with a new timestamp and delivery ID. Useful
        for recovering from temporary endpoint failures.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._post(
            f"/platform/webhooks/deliveries/{delivery_id}/replay",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReplayDeliveryResponse,
        )

    async def retrieve_delivery(
        self,
        delivery_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookRetrieveDeliveryResponse:
        """
        Get detailed information about a specific platform webhook delivery.

        Returns the complete request payload, headers, response, and timing info.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            f"/platform/webhooks/deliveries/{delivery_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookRetrieveDeliveryResponse,
        )

    async def test(
        self,
        webhook_id: str,
        *,
        event: Literal[
            "MessageSent",
            "MessageDelayed",
            "MessageDeliveryFailed",
            "MessageHeld",
            "MessageBounced",
            "MessageLinkClicked",
            "MessageLoaded",
            "DomainDNSError",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookTestResponse:
        """
        Send a test payload to your platform webhook endpoint.

        Use this to:

        - Verify your webhook URL is accessible
        - Test your payload handling code
        - Ensure your server responds correctly

        The test payload is marked with `_test: true` so you can distinguish test events
        from real events.

        Args:
          event: Event type to simulate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_id:
            raise ValueError(f"Expected a non-empty value for `webhook_id` but received {webhook_id!r}")
        return await self._post(
            f"/platform/webhooks/{webhook_id}/test",
            body=await async_maybe_transform({"event": event}, webhook_test_params.WebhookTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookTestResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = to_raw_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay_delivery = to_raw_response_wrapper(
            webhooks.replay_delivery,
        )
        self.retrieve_delivery = to_raw_response_wrapper(
            webhooks.retrieve_delivery,
        )
        self.test = to_raw_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = async_to_raw_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay_delivery = async_to_raw_response_wrapper(
            webhooks.replay_delivery,
        )
        self.retrieve_delivery = async_to_raw_response_wrapper(
            webhooks.retrieve_delivery,
        )
        self.test = async_to_raw_response_wrapper(
            webhooks.test,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = to_streamed_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay_delivery = to_streamed_response_wrapper(
            webhooks.replay_delivery,
        )
        self.retrieve_delivery = to_streamed_response_wrapper(
            webhooks.retrieve_delivery,
        )
        self.test = to_streamed_response_wrapper(
            webhooks.test,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.list_deliveries = async_to_streamed_response_wrapper(
            webhooks.list_deliveries,
        )
        self.replay_delivery = async_to_streamed_response_wrapper(
            webhooks.replay_delivery,
        )
        self.retrieve_delivery = async_to_streamed_response_wrapper(
            webhooks.retrieve_delivery,
        )
        self.test = async_to_streamed_response_wrapper(
            webhooks.test,
        )
