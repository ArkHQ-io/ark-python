# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from ark.types import (
    UsageExportResponse,
    UsageRetrieveResponse,
    UsageRetrieveTenantUsageResponse,
    UsageRetrieveTenantTimeseriesResponse,
)
from tests.utils import assert_matches_type
from ark.pagination import SyncOffsetPagination, AsyncOffsetPagination
from ark.types.bulk_tenant_usage import Tenant

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        with pytest.warns(DeprecationWarning):
            usage = client.usage.retrieve()

        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with pytest.warns(DeprecationWarning):
            with client.usage.with_streaming_response.retrieve() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                usage = response.parse()
                assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export(self, client: Ark) -> None:
        usage = client.usage.export()
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Ark) -> None:
        usage = client.usage.export(
            format="csv",
            min_sent=0,
            period="period",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Ark) -> None:
        response = client.usage.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Ark) -> None:
        with client.usage.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageExportResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_by_tenant(self, client: Ark) -> None:
        usage = client.usage.list_by_tenant()
        assert_matches_type(SyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    def test_method_list_by_tenant_with_all_params(self, client: Ark) -> None:
        usage = client.usage.list_by_tenant(
            limit=1,
            min_sent=0,
            offset=0,
            period="period",
            sort="sent",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(SyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    def test_raw_response_list_by_tenant(self, client: Ark) -> None:
        response = client.usage.with_raw_response.list_by_tenant()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(SyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    def test_streaming_response_list_by_tenant(self, client: Ark) -> None:
        with client.usage.with_streaming_response.list_by_tenant() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(SyncOffsetPagination[Tenant], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_tenant_timeseries(self, client: Ark) -> None:
        usage = client.usage.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_method_retrieve_tenant_timeseries_with_all_params(self, client: Ark) -> None:
        usage = client.usage.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
            granularity="hour",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve_tenant_timeseries(self, client: Ark) -> None:
        response = client.usage.with_raw_response.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_tenant_timeseries(self, client: Ark) -> None:
        with client.usage.with_streaming_response.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_tenant_timeseries(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.usage.with_raw_response.retrieve_tenant_timeseries(
                tenant_id="",
            )

    @parametrize
    def test_method_retrieve_tenant_usage(self, client: Ark) -> None:
        usage = client.usage.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    def test_method_retrieve_tenant_usage_with_all_params(self, client: Ark) -> None:
        usage = client.usage.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve_tenant_usage(self, client: Ark) -> None:
        response = client.usage.with_raw_response.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_tenant_usage(self, client: Ark) -> None:
        with client.usage.with_streaming_response.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_tenant_usage(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.usage.with_raw_response.retrieve_tenant_usage(
                tenant_id="",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.warns(DeprecationWarning):
            usage = await async_client.usage.retrieve()

        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.usage.with_streaming_response.retrieve() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                usage = await response.parse()
                assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.export()
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.export(
            format="csv",
            min_sent=0,
            period="period",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageExportResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageExportResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_by_tenant(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.list_by_tenant()
        assert_matches_type(AsyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    async def test_method_list_by_tenant_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.list_by_tenant(
            limit=1,
            min_sent=0,
            offset=0,
            period="period",
            sort="sent",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(AsyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    async def test_raw_response_list_by_tenant(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.list_by_tenant()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Tenant], usage, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_tenant(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.list_by_tenant() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Tenant], usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_tenant_timeseries(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_tenant_timeseries_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
            granularity="hour",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_tenant_timeseries(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_tenant_timeseries(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.retrieve_tenant_timeseries(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageRetrieveTenantTimeseriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_tenant_timeseries(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.usage.with_raw_response.retrieve_tenant_timeseries(
                tenant_id="",
            )

    @parametrize
    async def test_method_retrieve_tenant_usage(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_tenant_usage_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_tenant_usage(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_tenant_usage(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.retrieve_tenant_usage(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageRetrieveTenantUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_tenant_usage(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.usage.with_raw_response.retrieve_tenant_usage(
                tenant_id="",
            )
