# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal

import httpx

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from ...types import tenant_list_params, tenant_create_params, tenant_update_params
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .tracking import (
    TrackingResource,
    AsyncTrackingResource,
    TrackingResourceWithRawResponse,
    AsyncTrackingResourceWithRawResponse,
    TrackingResourceWithStreamingResponse,
    AsyncTrackingResourceWithStreamingResponse,
)
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
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ...pagination import SyncPageNumberPagination, AsyncPageNumberPagination
from .suppressions import (
    SuppressionsResource,
    AsyncSuppressionsResource,
    SuppressionsResourceWithRawResponse,
    AsyncSuppressionsResourceWithRawResponse,
    SuppressionsResourceWithStreamingResponse,
    AsyncSuppressionsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tenant import Tenant
from ...types.tenant_create_response import TenantCreateResponse
from ...types.tenant_delete_response import TenantDeleteResponse
from ...types.tenant_update_response import TenantUpdateResponse
from ...types.tenant_retrieve_response import TenantRetrieveResponse

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    """Manage tenants (your customers).

    Create a tenant for each of your customers to track their email sending separately.
    Store the tenant `id` in your database and use `metadata` for any custom data.

    **Quick Reference:**
    - `POST /tenants` - Create a new tenant
    - `GET /tenants` - List all tenants (paginated)
    - `GET /tenants/{id}` - Get tenant details
    - `PATCH /tenants/{id}` - Update tenant name, metadata, or status
    - `DELETE /tenants/{id}` - Delete a tenant
    """

    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return DomainsResource(self._client)

    @cached_property
    def suppressions(self) -> SuppressionsResource:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return SuppressionsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return WebhooksResource(self._client)

    @cached_property
    def tracking(self) -> TrackingResource:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return TrackingResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return UsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantCreateResponse:
        """Create a new tenant.

        Returns the created tenant with a unique `id`.

        Store this ID in your database to
        reference this tenant later.

        Args:
          name: Display name for the tenant (e.g., your customer's company name)

          metadata: Custom key-value pairs. Useful for storing references to your internal systems.

              **Limits:**

              - Max 50 keys
              - Key names max 40 characters
              - String values max 500 characters
              - Total size max 8KB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tenants",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                },
                tenant_create_params.TenantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantCreateResponse,
        )

    def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantRetrieveResponse:
        """
        Get a tenant by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantRetrieveResponse,
        )

    def update(
        self,
        tenant_id: str,
        *,
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantUpdateResponse:
        """Update a tenant's name, metadata, or status.

        At least one field is required.

        Metadata is replaced entirely—include all keys you want to keep.

        Args:
          metadata: Custom key-value pairs. Useful for storing references to your internal systems.

              **Limits:**

              - Max 50 keys
              - Key names max 40 characters
              - String values max 500 characters
              - Total size max 8KB

          name: Display name for the tenant

          status: Tenant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._patch(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "status": status,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPagination[Tenant]:
        """List all tenants with pagination.

        Filter by `status` if needed.

        Args:
          page: Page number (1-indexed)

          per_page: Number of items per page (max 100)

          status: Filter by tenant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/tenants",
            page=SyncPageNumberPagination[Tenant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            model=Tenant,
        )

    def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantDeleteResponse:
        """Permanently delete a tenant.

        This cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._delete(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantDeleteResponse,
        )


class AsyncTenantsResource(AsyncAPIResource):
    """Manage tenants (your customers).

    Create a tenant for each of your customers to track their email sending separately.
    Store the tenant `id` in your database and use `metadata` for any custom data.

    **Quick Reference:**
    - `POST /tenants` - Create a new tenant
    - `GET /tenants` - List all tenants (paginated)
    - `GET /tenants/{id}` - Get tenant details
    - `PATCH /tenants/{id}` - Update tenant name, metadata, or status
    - `DELETE /tenants/{id}` - Delete a tenant
    """

    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return AsyncDomainsResource(self._client)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResource:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return AsyncSuppressionsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return AsyncWebhooksResource(self._client)

    @cached_property
    def tracking(self) -> AsyncTrackingResource:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return AsyncTrackingResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return AsyncUsageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantCreateResponse:
        """Create a new tenant.

        Returns the created tenant with a unique `id`.

        Store this ID in your database to
        reference this tenant later.

        Args:
          name: Display name for the tenant (e.g., your customer's company name)

          metadata: Custom key-value pairs. Useful for storing references to your internal systems.

              **Limits:**

              - Max 50 keys
              - Key names max 40 characters
              - String values max 500 characters
              - Total size max 8KB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tenants",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                },
                tenant_create_params.TenantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantCreateResponse,
        )

    async def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantRetrieveResponse:
        """
        Get a tenant by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantRetrieveResponse,
        )

    async def update(
        self,
        tenant_id: str,
        *,
        metadata: Optional[Dict[str, Union[str, float, bool, None]]] | Omit = omit,
        name: str | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantUpdateResponse:
        """Update a tenant's name, metadata, or status.

        At least one field is required.

        Metadata is replaced entirely—include all keys you want to keep.

        Args:
          metadata: Custom key-value pairs. Useful for storing references to your internal systems.

              **Limits:**

              - Max 50 keys
              - Key names max 40 characters
              - String values max 500 characters
              - Total size max 8KB

          name: Display name for the tenant

          status: Tenant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._patch(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                    "status": status,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal["active", "suspended", "archived"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Tenant, AsyncPageNumberPagination[Tenant]]:
        """List all tenants with pagination.

        Filter by `status` if needed.

        Args:
          page: Page number (1-indexed)

          per_page: Number of items per page (max 100)

          status: Filter by tenant status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/tenants",
            page=AsyncPageNumberPagination[Tenant],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            model=Tenant,
        )

    async def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantDeleteResponse:
        """Permanently delete a tenant.

        This cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._delete(
            path_template("/tenants/{tenant_id}", tenant_id=tenant_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantDeleteResponse,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.create = to_raw_response_wrapper(
            tenants.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tenants.update,
        )
        self.list = to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._tenants.credentials)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return DomainsResourceWithRawResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithRawResponse:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return SuppressionsResourceWithRawResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return WebhooksResourceWithRawResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> TrackingResourceWithRawResponse:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return TrackingResourceWithRawResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return UsageResourceWithRawResponse(self._tenants.usage)


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.create = async_to_raw_response_wrapper(
            tenants.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tenants.update,
        )
        self.list = async_to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._tenants.credentials)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return AsyncDomainsResourceWithRawResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithRawResponse:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return AsyncSuppressionsResourceWithRawResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return AsyncWebhooksResourceWithRawResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> AsyncTrackingResourceWithRawResponse:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return AsyncTrackingResourceWithRawResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return AsyncUsageResourceWithRawResponse(self._tenants.usage)


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.create = to_streamed_response_wrapper(
            tenants.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._tenants.credentials)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return DomainsResourceWithStreamingResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithStreamingResponse:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return SuppressionsResourceWithStreamingResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return WebhooksResourceWithStreamingResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> TrackingResourceWithStreamingResponse:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return TrackingResourceWithStreamingResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return UsageResourceWithStreamingResponse(self._tenants.usage)


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.create = async_to_streamed_response_wrapper(
            tenants.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._tenants.credentials)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        """Manage sending domains.

        Before you can send emails, you need to:
        1. Add a domain
        2. Configure DNS records (SPF, DKIM, Return Path)
        3. Verify the domain

        **Quick Reference:**
        - `POST /domains` - Add a new domain
        - `GET /domains` - List all domains
        - `POST /domains/{id}/verify` - Check DNS and verify domain
        - `DELETE /domains/{id}` - Remove a domain
        """
        return AsyncDomainsResourceWithStreamingResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """Manage the suppression list.

        Suppressed email addresses will not receive any emails. Addresses are
        automatically suppressed when they hard bounce or file spam complaints.

        **Quick Reference:**
        - `GET /suppressions` - List suppressed addresses
        - `POST /suppressions` - Add to suppression list
        - `DELETE /suppressions/{email}` - Remove from suppression list
        - `GET /suppressions/{email}` - Check if address is suppressed
        """
        return AsyncSuppressionsResourceWithStreamingResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Configure webhook endpoints for real-time notifications.

        Webhooks notify your application when email events occur:
        - Email delivered, bounced, or failed
        - Email opened or link clicked
        - Spam complaint received

        **Quick Reference:**
        - `POST /webhooks` - Create a webhook endpoint
        - `GET /webhooks` - List all webhooks
        - `POST /webhooks/{id}/test` - Test a webhook with sample data
        - `PATCH /webhooks/{id}` - Update webhook configuration
        - `DELETE /webhooks/{id}` - Remove a webhook
        - `GET /webhooks/{id}/deliveries` - List delivery attempts
        - `GET /webhooks/{id}/deliveries/{deliveryId}` - Get delivery details
        - `POST /webhooks/{id}/deliveries/{deliveryId}/replay` - Replay a delivery

        ## Webhook Signatures

        All webhooks are cryptographically signed using RSA-SHA256 for security.
        Each webhook request includes:

        | Header | Description |
        |--------|-------------|
        | `X-Ark-Signature` | Base64-encoded RSA-SHA256 signature of the request body |
        | `X-Ark-Signature-KID` | Key ID identifying which public key was used |

        Verify signatures by fetching the public key from:
        ```
        GET https://mail.arkhq.io/.well-known/jwks.json
        ```

        ```javascript
        const crypto = require('crypto');

        async function verifyWebhook(payload, signatureBase64, publicKey) {
          const signature = Buffer.from(signatureBase64, 'base64');
          const verifier = crypto.createVerify('RSA-SHA256');
          verifier.update(payload);
          return verifier.verify(publicKey, signature);
        }

        // In your webhook handler:
        const isValid = await verifyWebhook(
          rawBody,
          req.headers['x-ark-signature'],
          cachedPublicKey
        );
        ```

        **Important:** Always verify signatures before processing webhook data.
        See the [Webhook Integration Guide](/guides/webhook-integration) for complete examples.
        """
        return AsyncWebhooksResourceWithStreamingResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> AsyncTrackingResourceWithStreamingResponse:
        """Manage track domains for open and click tracking.

        Track domains enable you to track when recipients:
        - Open your emails (tracking pixel)
        - Click links in your emails

        **Setup Process:**
        1. Create a track domain with `POST /tracking`
        2. Add the CNAME record to your DNS
        3. Verify DNS with `POST /tracking/{id}/verify`
        4. Track domain is ready when `dnsOk` is true

        **Quick Reference:**
        - `POST /tracking` - Create a new track domain
        - `GET /tracking` - List all track domains
        - `GET /tracking/{id}` - Get track domain details
        - `POST /tracking/{id}/verify` - Verify DNS configuration
        - `PATCH /tracking/{id}` - Enable/disable tracking features
        - `DELETE /tracking/{id}` - Remove a track domain
        """
        return AsyncTrackingResourceWithStreamingResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """Per-tenant usage analytics and bulk reporting.

        Track email sending statistics for each tenant to power billing, dashboards, and monitoring.

        **Single Tenant Usage:**
        - `GET /tenants/{id}/usage` - Get usage stats for a specific tenant
        - `GET /tenants/{id}/usage/timeseries` - Get time-bucketed data for charts

        **Bulk Usage:**
        - `GET /usage/tenants` - Get usage for all tenants (paginated, sortable)
        - `GET /usage/export` - Export usage data as CSV, JSONL, or JSON

        **Period Formats:**
        - Shortcuts: `today`, `yesterday`, `this_month`, `last_month`, `last_7_days`, `last_30_days`
        - Month: `2024-01`
        - Date range: `2024-01-01..2024-01-15`
        """
        return AsyncUsageResourceWithStreamingResponse(self._tenants.usage)
