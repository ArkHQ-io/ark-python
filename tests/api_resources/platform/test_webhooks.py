# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from tests.utils import assert_matches_type
from ark.pagination import SyncPageNumberPagination, AsyncPageNumberPagination
from ark.types.platform import (
    WebhookListResponse,
    WebhookTestResponse,
    WebhookCreateResponse,
    WebhookDeleteResponse,
    WebhookUpdateResponse,
    WebhookRetrieveResponse,
    WebhookListDeliveriesResponse,
    WebhookReplayDeliveryResponse,
    WebhookRetrieveDeliveryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Ark) -> None:
        webhook = client.platform.webhooks.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Ark) -> None:
        webhook = client.platform.webhooks.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
            events=["MessageSent", "MessageDeliveryFailed", "MessageBounced"],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        webhook = client.platform.webhooks.retrieve(
            "pwh_abc123def456",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.retrieve(
            "pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.retrieve(
            "pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.platform.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Ark) -> None:
        webhook = client.platform.webhooks.update(
            webhook_id="pwh_abc123def456",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Ark) -> None:
        webhook = client.platform.webhooks.update(
            webhook_id="pwh_abc123def456",
            enabled=True,
            events=["MessageSent"],
            name="x",
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.update(
            webhook_id="pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.update(
            webhook_id="pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.platform.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    def test_method_list(self, client: Ark) -> None:
        webhook = client.platform.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Ark) -> None:
        webhook = client.platform.webhooks.delete(
            "pwh_abc123def456",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.delete(
            "pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.delete(
            "pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.platform.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_list_deliveries(self, client: Ark) -> None:
        webhook = client.platform.webhooks.list_deliveries()
        assert_matches_type(SyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    def test_method_list_deliveries_with_all_params(self, client: Ark) -> None:
        webhook = client.platform.webhooks.list_deliveries(
            after=0,
            before=0,
            event="MessageSent",
            page=0,
            per_page=100,
            success=True,
            tenant_id="tenantId",
            webhook_id="webhookId",
        )
        assert_matches_type(SyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_list_deliveries(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.list_deliveries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list_deliveries(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.list_deliveries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_replay_delivery(self, client: Ark) -> None:
        webhook = client.platform.webhooks.replay_delivery(
            "pwd_abc123def456",
        )
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_replay_delivery(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.replay_delivery(
            "pwd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_replay_delivery(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.replay_delivery(
            "pwd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replay_delivery(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.platform.webhooks.with_raw_response.replay_delivery(
                "",
            )

    @parametrize
    def test_method_retrieve_delivery(self, client: Ark) -> None:
        webhook = client.platform.webhooks.retrieve_delivery(
            "pwd_abc123def456",
        )
        assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve_delivery(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.retrieve_delivery(
            "pwd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_delivery(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.retrieve_delivery(
            "pwd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_delivery(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.platform.webhooks.with_raw_response.retrieve_delivery(
                "",
            )

    @parametrize
    def test_method_test(self, client: Ark) -> None:
        webhook = client.platform.webhooks.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_test(self, client: Ark) -> None:
        response = client.platform.webhooks.with_raw_response.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_test(self, client: Ark) -> None:
        with client.platform.webhooks.with_streaming_response.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_test(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.platform.webhooks.with_raw_response.test(
                webhook_id="",
                event="MessageSent",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
            events=["MessageSent", "MessageDeliveryFailed", "MessageBounced"],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.create(
            name="Central Event Processor",
            url="https://myplatform.com/webhooks/email-events",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.retrieve(
            "pwh_abc123def456",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.retrieve(
            "pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.retrieve(
            "pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.update(
            webhook_id="pwh_abc123def456",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.update(
            webhook_id="pwh_abc123def456",
            enabled=True,
            events=["MessageSent"],
            name="x",
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.update(
            webhook_id="pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.update(
            webhook_id="pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.update(
                webhook_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.delete(
            "pwh_abc123def456",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.delete(
            "pwh_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.delete(
            "pwh_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_list_deliveries(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.list_deliveries()
        assert_matches_type(AsyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    async def test_method_list_deliveries_with_all_params(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.list_deliveries(
            after=0,
            before=0,
            event="MessageSent",
            page=0,
            per_page=100,
            success=True,
            tenant_id="tenantId",
            webhook_id="webhookId",
        )
        assert_matches_type(AsyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list_deliveries(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.list_deliveries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list_deliveries(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.list_deliveries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncPageNumberPagination[WebhookListDeliveriesResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_replay_delivery(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.replay_delivery(
            "pwd_abc123def456",
        )
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_replay_delivery(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.replay_delivery(
            "pwd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_replay_delivery(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.replay_delivery(
            "pwd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReplayDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replay_delivery(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.replay_delivery(
                "",
            )

    @parametrize
    async def test_method_retrieve_delivery(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.retrieve_delivery(
            "pwd_abc123def456",
        )
        assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_delivery(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.retrieve_delivery(
            "pwd_abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_delivery(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.retrieve_delivery(
            "pwd_abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveDeliveryResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_delivery(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.retrieve_delivery(
                "",
            )

    @parametrize
    async def test_method_test(self, async_client: AsyncArk) -> None:
        webhook = await async_client.platform.webhooks.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_test(self, async_client: AsyncArk) -> None:
        response = await async_client.platform.webhooks.with_raw_response.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncArk) -> None:
        async with async_client.platform.webhooks.with_streaming_response.test(
            webhook_id="pwh_abc123def456",
            event="MessageSent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_test(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.platform.webhooks.with_raw_response.test(
                webhook_id="",
                event="MessageSent",
            )
