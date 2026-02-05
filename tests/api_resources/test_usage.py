# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from ark.types import (
    OrgUsageSummary,
    TenantUsageItem,
    UsageExportResponse,
)
from tests.utils import assert_matches_type
from ark.pagination import SyncPageNumberPagination, AsyncPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        usage = client.usage.retrieve()
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ark) -> None:
        usage = client.usage.retrieve(
            period="period",
            timezone="timezone",
        )
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(OrgUsageSummary, usage, path=["response"])

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
    def test_method_list_tenants(self, client: Ark) -> None:
        usage = client.usage.list_tenants()
        assert_matches_type(SyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    def test_method_list_tenants_with_all_params(self, client: Ark) -> None:
        usage = client.usage.list_tenants(
            min_sent=0,
            page=1,
            period="period",
            per_page=1,
            sort="sent",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(SyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    def test_raw_response_list_tenants(self, client: Ark) -> None:
        response = client.usage.with_raw_response.list_tenants()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(SyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    def test_streaming_response_list_tenants(self, client: Ark) -> None:
        with client.usage.with_streaming_response.list_tenants() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(SyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve()
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.retrieve(
            period="period",
            timezone="timezone",
        )
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(OrgUsageSummary, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(OrgUsageSummary, usage, path=["response"])

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
    async def test_method_list_tenants(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.list_tenants()
        assert_matches_type(AsyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    async def test_method_list_tenants_with_all_params(self, async_client: AsyncArk) -> None:
        usage = await async_client.usage.list_tenants(
            min_sent=0,
            page=1,
            period="period",
            per_page=1,
            sort="sent",
            status="active",
            timezone="timezone",
        )
        assert_matches_type(AsyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    async def test_raw_response_list_tenants(self, async_client: AsyncArk) -> None:
        response = await async_client.usage.with_raw_response.list_tenants()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(AsyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

    @parametrize
    async def test_streaming_response_list_tenants(self, async_client: AsyncArk) -> None:
        async with async_client.usage.with_streaming_response.list_tenants() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(AsyncPageNumberPagination[TenantUsageItem], usage, path=["response"])

        assert cast(Any, response.is_closed) is True
