# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from ark.types import LimitRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        limit = client.limits.retrieve()
        assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.limits.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = response.parse()
        assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.limits.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = response.parse()
            assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        limit = await async_client.limits.retrieve()
        assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.limits.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        limit = await response.parse()
        assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.limits.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            limit = await response.parse()
            assert_matches_type(LimitRetrieveResponse, limit, path=["response"])

        assert cast(Any, response.is_closed) is True
