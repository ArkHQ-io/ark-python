# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from tests.utils import assert_matches_type
from ark.types.tenants import (
    DomainListResponse,
    DomainCreateResponse,
    DomainDeleteResponse,
    DomainVerifyResponse,
    DomainRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ark) -> None:
        domain = client.tenants.domains.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ark) -> None:
        response = client.tenants.domains.with_raw_response.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ark) -> None:
        with client.tenants.domains.with_streaming_response.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.domains.with_raw_response.create(
                tenant_id="",
                name="notifications.myapp.com",
            )

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        domain = client.tenants.domains.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.tenants.domains.with_raw_response.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.tenants.domains.with_streaming_response.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.domains.with_raw_response.retrieve(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.tenants.domains.with_raw_response.retrieve(
                domain_id="",
                tenant_id="cm6abc123def456",
            )

    @parametrize
    def test_method_list(self, client: Ark) -> None:
        domain = client.tenants.domains.list(
            "cm6abc123def456",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ark) -> None:
        response = client.tenants.domains.with_raw_response.list(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ark) -> None:
        with client.tenants.domains.with_streaming_response.list(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.domains.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Ark) -> None:
        domain = client.tenants.domains.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ark) -> None:
        response = client.tenants.domains.with_raw_response.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ark) -> None:
        with client.tenants.domains.with_streaming_response.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.domains.with_raw_response.delete(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.tenants.domains.with_raw_response.delete(
                domain_id="",
                tenant_id="cm6abc123def456",
            )

    @parametrize
    def test_method_verify(self, client: Ark) -> None:
        domain = client.tenants.domains.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainVerifyResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: Ark) -> None:
        response = client.tenants.domains.with_raw_response.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainVerifyResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: Ark) -> None:
        with client.tenants.domains.with_streaming_response.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainVerifyResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_verify(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.domains.with_raw_response.verify(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            client.tenants.domains.with_raw_response.verify(
                domain_id="",
                tenant_id="cm6abc123def456",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArk) -> None:
        domain = await async_client.tenants.domains.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.domains.with_raw_response.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.domains.with_streaming_response.create(
            tenant_id="cm6abc123def456",
            name="notifications.myapp.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.create(
                tenant_id="",
                name="notifications.myapp.com",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        domain = await async_client.tenants.domains.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.domains.with_raw_response.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.domains.with_streaming_response.retrieve(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.retrieve(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.retrieve(
                domain_id="",
                tenant_id="cm6abc123def456",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncArk) -> None:
        domain = await async_client.tenants.domains.list(
            "cm6abc123def456",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.domains.with_raw_response.list(
            "cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.domains.with_streaming_response.list(
            "cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncArk) -> None:
        domain = await async_client.tenants.domains.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.domains.with_raw_response.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.domains.with_streaming_response.delete(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.delete(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.delete(
                domain_id="",
                tenant_id="cm6abc123def456",
            )

    @parametrize
    async def test_method_verify(self, async_client: AsyncArk) -> None:
        domain = await async_client.tenants.domains.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(DomainVerifyResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.domains.with_raw_response.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainVerifyResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.domains.with_streaming_response.verify(
            domain_id="123",
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainVerifyResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_verify(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.verify(
                domain_id="123",
                tenant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_id` but received ''"):
            await async_client.tenants.domains.with_raw_response.verify(
                domain_id="",
                tenant_id="cm6abc123def456",
            )
