# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.tenants import (
    credential_list_params,
    credential_create_params,
    credential_update_params,
    credential_retrieve_params,
)
from ...types.tenants.credential_list_response import CredentialListResponse
from ...types.tenants.credential_create_response import CredentialCreateResponse
from ...types.tenants.credential_delete_response import CredentialDeleteResponse
from ...types.tenants.credential_update_response import CredentialUpdateResponse
from ...types.tenants.credential_retrieve_response import CredentialRetrieveResponse

__all__ = ["CredentialsResource", "AsyncCredentialsResource"]


class CredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return CredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return CredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        tenant_id: str,
        *,
        name: str,
        type: Literal["smtp", "api"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialCreateResponse:
        """Create a new SMTP or API credential for a tenant.

        The credential can be used to
        send emails through Postal on behalf of the tenant.

        **Important:** The credential key is only returned once at creation time. Store
        it securely - you cannot retrieve it again.

        **Credential Types:**

        - `smtp` - For SMTP-based email sending. Returns both `key` and `smtpUsername`.
        - `api` - For API-based email sending. Returns only `key`.

        Args:
          name: Name for the credential. Can only contain letters, numbers, hyphens, and
              underscores. Max 50 characters.

          type:
              Type of credential:

              - `smtp` - For SMTP-based email sending
              - `api` - For API-based email sending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._post(
            f"/tenants/{tenant_id}/credentials",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialCreateResponse,
        )

    def retrieve(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        reveal: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialRetrieveResponse:
        """
        Get details of a specific credential.

        **Revealing the key:** By default, the credential key is not returned. Pass
        `reveal=true` to include the key in the response. Use this sparingly and only
        when you need to retrieve the key (e.g., for configuration).

        Args:
          reveal: Set to `true` to include the credential key in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"reveal": reveal}, credential_retrieve_params.CredentialRetrieveParams),
            ),
            cast_to=CredentialRetrieveResponse,
        )

    def update(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        hold: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialUpdateResponse:
        """
        Update a credential's name or hold status.

        **Hold Status:**

        - When `hold: true`, the credential is disabled and cannot be used to send
          emails.
        - When `hold: false`, the credential is active and can send emails.
        - Use this to temporarily disable a credential without deleting it.

        Args:
          hold: Set to `true` to disable the credential (put on hold). Set to `false` to enable
              the credential (release from hold).

          name: New name for the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._patch(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            body=maybe_transform(
                {
                    "hold": hold,
                    "name": name,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialUpdateResponse,
        )

    def list(
        self,
        tenant_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["smtp", "api"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPageNumberPagination[CredentialListResponse]:
        """List all SMTP and API credentials for a tenant.

        Credentials are used to send
        emails through Postal on behalf of the tenant.

        **Security:** Credential keys are not returned in the list response. Use the
        retrieve endpoint with `reveal=true` to get the key.

        Args:
          page: Page number (1-indexed)

          per_page: Number of items per page (max 100)

          type: Filter by credential type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            f"/tenants/{tenant_id}/credentials",
            page=SyncPageNumberPagination[CredentialListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            model=CredentialListResponse,
        )

    def delete(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialDeleteResponse:
        """Permanently delete (revoke) a credential.

        The credential can no longer be used
        to send emails.

        **Warning:** This action is irreversible. If you want to temporarily disable a
        credential, use the update endpoint to set `hold: true` instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._delete(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialDeleteResponse,
        )


class AsyncCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArkHQ-io/ark-python#with_streaming_response
        """
        return AsyncCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        tenant_id: str,
        *,
        name: str,
        type: Literal["smtp", "api"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialCreateResponse:
        """Create a new SMTP or API credential for a tenant.

        The credential can be used to
        send emails through Postal on behalf of the tenant.

        **Important:** The credential key is only returned once at creation time. Store
        it securely - you cannot retrieve it again.

        **Credential Types:**

        - `smtp` - For SMTP-based email sending. Returns both `key` and `smtpUsername`.
        - `api` - For API-based email sending. Returns only `key`.

        Args:
          name: Name for the credential. Can only contain letters, numbers, hyphens, and
              underscores. Max 50 characters.

          type:
              Type of credential:

              - `smtp` - For SMTP-based email sending
              - `api` - For API-based email sending

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._post(
            f"/tenants/{tenant_id}/credentials",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                credential_create_params.CredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialCreateResponse,
        )

    async def retrieve(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        reveal: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialRetrieveResponse:
        """
        Get details of a specific credential.

        **Revealing the key:** By default, the credential key is not returned. Pass
        `reveal=true` to include the key in the response. Use this sparingly and only
        when you need to retrieve the key (e.g., for configuration).

        Args:
          reveal: Set to `true` to include the credential key in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"reveal": reveal}, credential_retrieve_params.CredentialRetrieveParams
                ),
            ),
            cast_to=CredentialRetrieveResponse,
        )

    async def update(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        hold: bool | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialUpdateResponse:
        """
        Update a credential's name or hold status.

        **Hold Status:**

        - When `hold: true`, the credential is disabled and cannot be used to send
          emails.
        - When `hold: false`, the credential is active and can send emails.
        - Use this to temporarily disable a credential without deleting it.

        Args:
          hold: Set to `true` to disable the credential (put on hold). Set to `false` to enable
              the credential (release from hold).

          name: New name for the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._patch(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            body=await async_maybe_transform(
                {
                    "hold": hold,
                    "name": name,
                },
                credential_update_params.CredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialUpdateResponse,
        )

    def list(
        self,
        tenant_id: str,
        *,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["smtp", "api"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CredentialListResponse, AsyncPageNumberPagination[CredentialListResponse]]:
        """List all SMTP and API credentials for a tenant.

        Credentials are used to send
        emails through Postal on behalf of the tenant.

        **Security:** Credential keys are not returned in the list response. Use the
        retrieve endpoint with `reveal=true` to get the key.

        Args:
          page: Page number (1-indexed)

          per_page: Number of items per page (max 100)

          type: Filter by credential type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            f"/tenants/{tenant_id}/credentials",
            page=AsyncPageNumberPagination[CredentialListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "type": type,
                    },
                    credential_list_params.CredentialListParams,
                ),
            ),
            model=CredentialListResponse,
        )

    async def delete(
        self,
        credential_id: int,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CredentialDeleteResponse:
        """Permanently delete (revoke) a credential.

        The credential can no longer be used
        to send emails.

        **Warning:** This action is irreversible. If you want to temporarily disable a
        credential, use the update endpoint to set `hold: true` instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._delete(
            f"/tenants/{tenant_id}/credentials/{credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CredentialDeleteResponse,
        )


class CredentialsResourceWithRawResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_raw_response_wrapper(
            credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            credentials.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credentials.update,
        )
        self.list = to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            credentials.delete,
        )


class AsyncCredentialsResourceWithRawResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_raw_response_wrapper(
            credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            credentials.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credentials.update,
        )
        self.list = async_to_raw_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            credentials.delete,
        )


class CredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: CredentialsResource) -> None:
        self._credentials = credentials

        self.create = to_streamed_response_wrapper(
            credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            credentials.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            credentials.delete,
        )


class AsyncCredentialsResourceWithStreamingResponse:
    def __init__(self, credentials: AsyncCredentialsResource) -> None:
        self._credentials = credentials

        self.create = async_to_streamed_response_wrapper(
            credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            credentials.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credentials.update,
        )
        self.list = async_to_streamed_response_wrapper(
            credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            credentials.delete,
        )
