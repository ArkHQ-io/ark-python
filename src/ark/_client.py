# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ArkError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import logs, usage, emails, limits, tenants, platform
    from .resources.logs import LogsResource, AsyncLogsResource
    from .resources.usage import UsageResource, AsyncUsageResource
    from .resources.emails import EmailsResource, AsyncEmailsResource
    from .resources.limits import LimitsResource, AsyncLimitsResource
    from .resources.tenants.tenants import TenantsResource, AsyncTenantsResource
    from .resources.platform.platform import PlatformResource, AsyncPlatformResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Ark", "AsyncArk", "Client", "AsyncClient"]


class Ark(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Ark client instance.

        This automatically infers the `api_key` argument from the `ARK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        if api_key is None:
            raise ArkError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ARK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ARK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.arkhq.io/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def emails(self) -> EmailsResource:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import EmailsResource

        return EmailsResource(self)

    @cached_property
    def logs(self) -> LogsResource:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import LogsResource

        return LogsResource(self)

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
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def limits(self) -> LimitsResource:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import LimitsResource

        return LimitsResource(self)

    @cached_property
    def tenants(self) -> TenantsResource:
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
        from .resources.tenants import TenantsResource

        return TenantsResource(self)

    @cached_property
    def platform(self) -> PlatformResource:
        from .resources.platform import PlatformResource

        return PlatformResource(self)

    @cached_property
    def with_raw_response(self) -> ArkWithRawResponse:
        return ArkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArkWithStreamedResponse:
        return ArkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncArk(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncArk client instance.

        This automatically infers the `api_key` argument from the `ARK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ARK_API_KEY")
        if api_key is None:
            raise ArkError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ARK_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ARK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.arkhq.io/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import AsyncEmailsResource

        return AsyncEmailsResource(self)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import AsyncLogsResource

        return AsyncLogsResource(self)

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
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def limits(self) -> AsyncLimitsResource:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import AsyncLimitsResource

        return AsyncLimitsResource(self)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
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
        from .resources.tenants import AsyncTenantsResource

        return AsyncTenantsResource(self)

    @cached_property
    def platform(self) -> AsyncPlatformResource:
        from .resources.platform import AsyncPlatformResource

        return AsyncPlatformResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncArkWithRawResponse:
        return AsyncArkWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArkWithStreamedResponse:
        return AsyncArkWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ArkWithRawResponse:
    _client: Ark

    def __init__(self, client: Ark) -> None:
        self._client = client

    @cached_property
    def emails(self) -> emails.EmailsResourceWithRawResponse:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import EmailsResourceWithRawResponse

        return EmailsResourceWithRawResponse(self._client.emails)

    @cached_property
    def logs(self) -> logs.LogsResourceWithRawResponse:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import LogsResourceWithRawResponse

        return LogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
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
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def limits(self) -> limits.LimitsResourceWithRawResponse:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import LimitsResourceWithRawResponse

        return LimitsResourceWithRawResponse(self._client.limits)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithRawResponse:
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
        from .resources.tenants import TenantsResourceWithRawResponse

        return TenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def platform(self) -> platform.PlatformResourceWithRawResponse:
        from .resources.platform import PlatformResourceWithRawResponse

        return PlatformResourceWithRawResponse(self._client.platform)


class AsyncArkWithRawResponse:
    _client: AsyncArk

    def __init__(self, client: AsyncArk) -> None:
        self._client = client

    @cached_property
    def emails(self) -> emails.AsyncEmailsResourceWithRawResponse:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import AsyncEmailsResourceWithRawResponse

        return AsyncEmailsResourceWithRawResponse(self._client.emails)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithRawResponse:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import AsyncLogsResourceWithRawResponse

        return AsyncLogsResourceWithRawResponse(self._client.logs)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
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
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def limits(self) -> limits.AsyncLimitsResourceWithRawResponse:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import AsyncLimitsResourceWithRawResponse

        return AsyncLimitsResourceWithRawResponse(self._client.limits)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithRawResponse:
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
        from .resources.tenants import AsyncTenantsResourceWithRawResponse

        return AsyncTenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def platform(self) -> platform.AsyncPlatformResourceWithRawResponse:
        from .resources.platform import AsyncPlatformResourceWithRawResponse

        return AsyncPlatformResourceWithRawResponse(self._client.platform)


class ArkWithStreamedResponse:
    _client: Ark

    def __init__(self, client: Ark) -> None:
        self._client = client

    @cached_property
    def emails(self) -> emails.EmailsResourceWithStreamingResponse:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import EmailsResourceWithStreamingResponse

        return EmailsResourceWithStreamingResponse(self._client.emails)

    @cached_property
    def logs(self) -> logs.LogsResourceWithStreamingResponse:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import LogsResourceWithStreamingResponse

        return LogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
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
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def limits(self) -> limits.LimitsResourceWithStreamingResponse:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import LimitsResourceWithStreamingResponse

        return LimitsResourceWithStreamingResponse(self._client.limits)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithStreamingResponse:
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
        from .resources.tenants import TenantsResourceWithStreamingResponse

        return TenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def platform(self) -> platform.PlatformResourceWithStreamingResponse:
        from .resources.platform import PlatformResourceWithStreamingResponse

        return PlatformResourceWithStreamingResponse(self._client.platform)


class AsyncArkWithStreamedResponse:
    _client: AsyncArk

    def __init__(self, client: AsyncArk) -> None:
        self._client = client

    @cached_property
    def emails(self) -> emails.AsyncEmailsResourceWithStreamingResponse:
        """Send and manage email messages.

        **Quick Reference:**
        - `POST /emails` - Send a single email
        - `POST /emails/batch` - Send up to 100 emails
        - `GET /emails/{emailId}` - Get email status and details
        - `GET /emails` - List sent emails
        - `POST /emails/{emailId}/retry` - Retry failed delivery
        """
        from .resources.emails import AsyncEmailsResourceWithStreamingResponse

        return AsyncEmailsResourceWithStreamingResponse(self._client.emails)

    @cached_property
    def logs(self) -> logs.AsyncLogsResourceWithStreamingResponse:
        """Access API request logs for debugging and monitoring.

        Every API request is logged with details including:
        - Request method, path, and endpoint
        - Response status code and duration
        - Error details (code, message) for failed requests
        - SDK information (name, version)
        - Rate limit state at time of request
        - Request and response bodies (for single log retrieval)

        **Retention:** Logs are retained for 90 days.

        **Body storage:** Request and response bodies are stored encrypted
        and truncated at 25KB. Bodies are only returned when retrieving
        a single log entry.

        **Quick Reference:**
        - `GET /logs` - List API request logs with filters
        - `GET /logs/{requestId}` - Get full details including request/response bodies
        """
        from .resources.logs import AsyncLogsResourceWithStreamingResponse

        return AsyncLogsResourceWithStreamingResponse(self._client.logs)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
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
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def limits(self) -> limits.AsyncLimitsResourceWithStreamingResponse:
        """Check account rate limits and send limits.

        The limits endpoint returns current status for operational limits:
        - **Rate limit:** API requests per second (currently 10/sec)
        - **Send limit:** Emails per hour (default 100/hour for new accounts)
        - **Billing:** Credit balance and auto-recharge configuration

        **AI Integration Note:** This endpoint is designed for AI agents and MCP servers
        to understand account constraints before taking actions. Call this endpoint
        first when planning batch operations to avoid hitting limits unexpectedly.

        **Quick Reference:**
        - `GET /limits` - Get current rate limits and send limits
        - `GET /usage` - (Deprecated) Use `/limits` instead
        """
        from .resources.limits import AsyncLimitsResourceWithStreamingResponse

        return AsyncLimitsResourceWithStreamingResponse(self._client.limits)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithStreamingResponse:
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
        from .resources.tenants import AsyncTenantsResourceWithStreamingResponse

        return AsyncTenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def platform(self) -> platform.AsyncPlatformResourceWithStreamingResponse:
        from .resources.platform import AsyncPlatformResourceWithStreamingResponse

        return AsyncPlatformResourceWithStreamingResponse(self._client.platform)


Client = Ark

AsyncClient = AsyncArk
