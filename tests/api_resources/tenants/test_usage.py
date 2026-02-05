# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from tests.utils import assert_matches_type
from ark.types.tenants import (
    UsageRetrieveResponse,
    UsageRetrieveTimeseriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        usage = client.tenants.usage.retrieve(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ark) -> None:
        usage = client.tenants.usage.retrieve(
            tenant_id="cm6abc123def456",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.tenants.usage.with_raw_response.retrieve(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.tenants.usage.with_streaming_response.retrieve(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.usage.with_raw_response.retrieve(
                tenant_id="",
            )

    @parametrize
    def test_method_retrieve_timeseries(self, client: Ark) -> None:
        usage = client.tenants.usage.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_method_retrieve_timeseries_with_all_params(self, client: Ark) -> None:
        usage = client.tenants.usage.retrieve_timeseries(
            tenant_id="cm6abc123def456",
            granularity="hour",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve_timeseries(self, client: Ark) -> None:
        response = client.tenants.usage.with_raw_response.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_timeseries(self, client: Ark) -> None:
        with client.tenants.usage.with_streaming_response.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_timeseries(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.usage.with_raw_response.retrieve_timeseries(
                tenant_id="",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        usage = await async_client.tenants.usage.retrieve(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.tenants.usage.retrieve(
            tenant_id="cm6abc123def456",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.usage.with_raw_response.retrieve(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.usage.with_streaming_response.retrieve(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageRetrieveResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.usage.with_raw_response.retrieve(
                tenant_id="",
            )

    @parametrize
    async def test_method_retrieve_timeseries(self, async_client: AsyncArk) -> None:
        usage = await async_client.tenants.usage.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_timeseries_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.tenants.usage.retrieve_timeseries(
            tenant_id="cm6abc123def456",
            granularity="hour",
            period="period",
            timezone="timezone",
        )
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_timeseries(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.usage.with_raw_response.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_timeseries(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.usage.with_streaming_response.retrieve_timeseries(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageRetrieveTimeseriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_timeseries(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.usage.with_raw_response.retrieve_timeseries(
                tenant_id="",
            )
