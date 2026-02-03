# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from ark.types import (
    Tenant,
    TenantCreateResponse,
    TenantDeleteResponse,
    TenantUpdateResponse,
    TenantRetrieveResponse,
)
from tests.utils import assert_matches_type
from ark.pagination import SyncPageNumberPagination, AsyncPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ark) -> None:
        tenant = client.tenants.create(
            name="Acme Corp",
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ark) -> None:
        tenant = client.tenants.create(
            name="Acme Corp",
            metadata={
                "plan": "pro",
                "internal_id": "cust_12345",
                "region": "us-west",
            },
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ark) -> None:
        response = client.tenants.with_raw_response.create(
            name="Acme Corp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ark) -> None:
        with client.tenants.with_streaming_response.create(
            name="Acme Corp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantCreateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        tenant = client.tenants.retrieve(
            "cm6abc123def456",
        )
        assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.tenants.with_raw_response.retrieve(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.tenants.with_streaming_response.retrieve(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Ark) -> None:
        tenant = client.tenants.update(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Ark) -> None:
        tenant = client.tenants.update(
            tenant_id="cm6abc123def456",
            metadata={
                "plan": "pro",
                "internal_id": "cust_12345",
                "region": "us-west",
            },
            name="Acme Corporation",
            status="active",
        )
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Ark) -> None:
        response = client.tenants.with_raw_response.update(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Ark) -> None:
        with client.tenants.with_streaming_response.update(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.with_raw_response.update(
                tenant_id="",
            )

    @parametrize
    def test_method_list(self, client: Ark) -> None:
        tenant = client.tenants.list()
        assert_matches_type(SyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Ark) -> None:
        tenant = client.tenants.list(
            page=1,
            per_page=1,
            status="active",
        )
        assert_matches_type(SyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ark) -> None:
        response = client.tenants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(SyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ark) -> None:
        with client.tenants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(SyncPageNumberPagination[Tenant], tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Ark) -> None:
        tenant = client.tenants.delete(
            "cm6abc123def456",
        )
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ark) -> None:
        response = client.tenants.with_raw_response.delete(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ark) -> None:
        with client.tenants.with_streaming_response.delete(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.with_raw_response.delete(
                "",
            )


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.create(
            name="Acme Corp",
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.create(
            name="Acme Corp",
            metadata={
                "plan": "pro",
                "internal_id": "cust_12345",
                "region": "us-west",
            },
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.with_raw_response.create(
            name="Acme Corp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.with_streaming_response.create(
            name="Acme Corp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantCreateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.retrieve(
            "cm6abc123def456",
        )
        assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.with_raw_response.retrieve(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.with_streaming_response.retrieve(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantRetrieveResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.update(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.update(
            tenant_id="cm6abc123def456",
            metadata={
                "plan": "pro",
                "internal_id": "cust_12345",
                "region": "us-west",
            },
            name="Acme Corporation",
            status="active",
        )
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.with_raw_response.update(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.with_streaming_response.update(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantUpdateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.with_raw_response.update(
                tenant_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.list()
        assert_matches_type(AsyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.list(
            page=1,
            per_page=1,
            status="active",
        )
        assert_matches_type(AsyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(AsyncPageNumberPagination[Tenant], tenant, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(AsyncPageNumberPagination[Tenant], tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArk) -> None:
        tenant = await async_client.tenants.delete(
            "cm6abc123def456",
        )
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.with_raw_response.delete(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.with_streaming_response.delete(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.with_raw_response.delete(
                "",
            )
