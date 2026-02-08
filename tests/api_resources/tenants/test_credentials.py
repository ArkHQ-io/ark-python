# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from tests.utils import assert_matches_type
from ark.pagination import SyncPageNumberPagination, AsyncPageNumberPagination
from ark.types.tenants import (
    CredentialListResponse,
    CredentialCreateResponse,
    CredentialDeleteResponse,
    CredentialUpdateResponse,
    CredentialRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ark) -> None:
        credential = client.tenants.credentials.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ark) -> None:
        response = client.tenants.credentials.with_raw_response.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ark) -> None:
        with client.tenants.credentials.with_streaming_response.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.credentials.with_raw_response.create(
                tenant_id="",
                name="production-smtp",
                type="smtp",
            )

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        credential = client.tenants.credentials.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ark) -> None:
        credential = client.tenants.credentials.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
            reveal=True,
        )
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.tenants.credentials.with_raw_response.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.tenants.credentials.with_streaming_response.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.credentials.with_raw_response.retrieve(
                credential_id=123,
                tenant_id="",
            )

    @parametrize
    def test_method_update(self, client: Ark) -> None:
        credential = client.tenants.credentials.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Ark) -> None:
        credential = client.tenants.credentials.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
            hold=True,
            name="production-smtp-v2",
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Ark) -> None:
        response = client.tenants.credentials.with_raw_response.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Ark) -> None:
        with client.tenants.credentials.with_streaming_response.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.credentials.with_raw_response.update(
                credential_id=123,
                tenant_id="",
            )

    @parametrize
    def test_method_list(self, client: Ark) -> None:
        credential = client.tenants.credentials.list(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(SyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Ark) -> None:
        credential = client.tenants.credentials.list(
            tenant_id="cm6abc123def456",
            page=1,
            per_page=1,
            type="smtp",
        )
        assert_matches_type(SyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ark) -> None:
        response = client.tenants.credentials.with_raw_response.list(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(SyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ark) -> None:
        with client.tenants.credentials.with_streaming_response.list(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(SyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.credentials.with_raw_response.list(
                tenant_id="",
            )

    @parametrize
    def test_method_delete(self, client: Ark) -> None:
        credential = client.tenants.credentials.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ark) -> None:
        response = client.tenants.credentials.with_raw_response.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ark) -> None:
        with client.tenants.credentials.with_streaming_response.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            client.tenants.credentials.with_raw_response.delete(
                credential_id=123,
                tenant_id="",
            )


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        )
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.credentials.with_raw_response.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialCreateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.credentials.with_streaming_response.create(
            tenant_id="cm6abc123def456",
            name="production-smtp",
            type="smtp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialCreateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.credentials.with_raw_response.create(
                tenant_id="",
                name="production-smtp",
                type="smtp",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
            reveal=True,
        )
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.credentials.with_raw_response.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.credentials.with_streaming_response.retrieve(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialRetrieveResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.credentials.with_raw_response.retrieve(
                credential_id=123,
                tenant_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
            hold=True,
            name="production-smtp-v2",
        )
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.credentials.with_raw_response.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.credentials.with_streaming_response.update(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialUpdateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.credentials.with_raw_response.update(
                credential_id=123,
                tenant_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.list(
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(AsyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.list(
            tenant_id="cm6abc123def456",
            page=1,
            per_page=1,
            type="smtp",
        )
        assert_matches_type(AsyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.credentials.with_raw_response.list(
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(AsyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.credentials.with_streaming_response.list(
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(AsyncPageNumberPagination[CredentialListResponse], credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.credentials.with_raw_response.list(
                tenant_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncArk) -> None:
        credential = await async_client.tenants.credentials.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArk) -> None:
        response = await async_client.tenants.credentials.with_raw_response.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArk) -> None:
        async with async_client.tenants.credentials.with_streaming_response.delete(
            credential_id=123,
            tenant_id="cm6abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialDeleteResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_id` but received ''"):
            await async_client.tenants.credentials.with_raw_response.delete(
                credential_id=123,
                tenant_id="",
            )
