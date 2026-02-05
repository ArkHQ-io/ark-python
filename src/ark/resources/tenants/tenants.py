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
from ..._utils import maybe_transform, async_maybe_transform
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
    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def suppressions(self) -> SuppressionsResource:
        return SuppressionsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def tracking(self) -> TrackingResource:
        return TrackingResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
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
            f"/tenants/{tenant_id}",
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
            f"/tenants/{tenant_id}",
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
            f"/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenantDeleteResponse,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResource:
        return AsyncSuppressionsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def tracking(self) -> AsyncTrackingResource:
        return AsyncTrackingResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
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
            f"/tenants/{tenant_id}",
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
            f"/tenants/{tenant_id}",
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
            f"/tenants/{tenant_id}",
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
        return DomainsResourceWithRawResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithRawResponse:
        return SuppressionsResourceWithRawResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> TrackingResourceWithRawResponse:
        return TrackingResourceWithRawResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
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
        return AsyncDomainsResourceWithRawResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithRawResponse:
        return AsyncSuppressionsResourceWithRawResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> AsyncTrackingResourceWithRawResponse:
        return AsyncTrackingResourceWithRawResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
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
        return DomainsResourceWithStreamingResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithStreamingResponse:
        return SuppressionsResourceWithStreamingResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> TrackingResourceWithStreamingResponse:
        return TrackingResourceWithStreamingResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
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
        return AsyncDomainsResourceWithStreamingResponse(self._tenants.domains)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        return AsyncSuppressionsResourceWithStreamingResponse(self._tenants.suppressions)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._tenants.webhooks)

    @cached_property
    def tracking(self) -> AsyncTrackingResourceWithStreamingResponse:
        return AsyncTrackingResourceWithStreamingResponse(self._tenants.tracking)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._tenants.usage)
