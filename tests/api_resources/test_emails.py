# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ark import Ark, AsyncArk
from ark.types import (
    SendEmail,
    EmailListResponse,
    EmailRetryResponse,
    EmailRetrieveResponse,
    EmailSendBatchResponse,
    EmailGetDeliveriesResponse,
)
from tests.utils import assert_matches_type
from ark.pagination import SyncEmailsPage, AsyncEmailsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Ark) -> None:
        email = client.emails.retrieve(
            email_id="emailId",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Ark) -> None:
        email = client.emails.retrieve(
            email_id="emailId",
            expand="content,deliveries",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Ark) -> None:
        response = client.emails.with_raw_response.retrieve(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Ark) -> None:
        with client.emails.with_streaming_response.retrieve(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.emails.with_raw_response.retrieve(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Ark) -> None:
        email = client.emails.list()
        assert_matches_type(SyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Ark) -> None:
        email = client.emails.list(
            after="after",
            before="before",
            from_="dev@stainless.com",
            page=1,
            per_page=1,
            status="pending",
            tag="tag",
            to="dev@stainless.com",
        )
        assert_matches_type(SyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Ark) -> None:
        response = client.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Ark) -> None:
        with client.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncEmailsPage[EmailListResponse], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_deliveries(self, client: Ark) -> None:
        email = client.emails.get_deliveries(
            "emailId",
        )
        assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_deliveries(self, client: Ark) -> None:
        response = client.emails.with_raw_response.get_deliveries(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_deliveries(self, client: Ark) -> None:
        with client.emails.with_streaming_response.get_deliveries(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_deliveries(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.emails.with_raw_response.get_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Ark) -> None:
        email = client.emails.retry(
            "emailId",
        )
        assert_matches_type(EmailRetryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Ark) -> None:
        response = client.emails.with_raw_response.retry(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Ark) -> None:
        with client.emails.with_streaming_response.retry(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRetryResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: Ark) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.emails.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Ark) -> None:
        email = client.emails.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Ark) -> None:
        email = client.emails.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
            attachments=[
                {
                    "content": "content",
                    "content_type": "application/pdf",
                    "filename": "filename",
                }
            ],
            bcc=["dev@stainless.com"],
            cc=["dev@stainless.com"],
            headers={"foo": "string"},
            html="<h1>Welcome!</h1><p>Thanks for signing up.</p>",
            reply_to="dev@stainless.com",
            tag="tag",
            text="text",
            idempotency_key="user_123_order_456",
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Ark) -> None:
        response = client.emails.with_raw_response.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Ark) -> None:
        with client.emails.with_streaming_response.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SendEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_batch(self, client: Ark) -> None:
        email = client.emails.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        )
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_batch_with_all_params(self, client: Ark) -> None:
        email = client.emails.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                    "html": "<p>Hi Alice, your order is ready!</p>",
                    "tag": "order-ready",
                    "text": "text",
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                    "html": "<p>Hi Bob, your order is ready!</p>",
                    "tag": "order-ready",
                    "text": "text",
                },
            ],
            from_="notifications@myapp.com",
            idempotency_key="user_123_order_456",
        )
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_batch(self, client: Ark) -> None:
        response = client.emails.with_raw_response.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_batch(self, client: Ark) -> None:
        with client.emails.with_streaming_response.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSendBatchResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_raw(self, client: Ark) -> None:
        email = client.emails.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_raw(self, client: Ark) -> None:
        response = client.emails.with_raw_response.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_raw(self, client: Ark) -> None:
        with client.emails.with_streaming_response.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SendEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.retrieve(
            email_id="emailId",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.retrieve(
            email_id="emailId",
            expand="content,deliveries",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.retrieve(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.retrieve(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.emails.with_raw_response.retrieve(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.list()
        assert_matches_type(AsyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.list(
            after="after",
            before="before",
            from_="dev@stainless.com",
            page=1,
            per_page=1,
            status="pending",
            tag="tag",
            to="dev@stainless.com",
        )
        assert_matches_type(AsyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncEmailsPage[EmailListResponse], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncEmailsPage[EmailListResponse], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_deliveries(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.get_deliveries(
            "emailId",
        )
        assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_deliveries(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.get_deliveries(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_deliveries(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.get_deliveries(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailGetDeliveriesResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_deliveries(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.emails.with_raw_response.get_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.retry(
            "emailId",
        )
        assert_matches_type(EmailRetryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.retry(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.retry(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRetryResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncArk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.emails.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
            attachments=[
                {
                    "content": "content",
                    "content_type": "application/pdf",
                    "filename": "filename",
                }
            ],
            bcc=["dev@stainless.com"],
            cc=["dev@stainless.com"],
            headers={"foo": "string"},
            html="<h1>Welcome!</h1><p>Thanks for signing up.</p>",
            reply_to="dev@stainless.com",
            tag="tag",
            text="text",
            idempotency_key="user_123_order_456",
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.send(
            from_="Acme <hello@acme.com>",
            subject="Hello World",
            to=["user@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(SendEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_batch(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        )
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_batch_with_all_params(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                    "html": "<p>Hi Alice, your order is ready!</p>",
                    "tag": "order-ready",
                    "text": "text",
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                    "html": "<p>Hi Bob, your order is ready!</p>",
                    "tag": "order-ready",
                    "text": "text",
                },
            ],
            from_="notifications@myapp.com",
            idempotency_key="user_123_order_456",
        )
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_batch(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSendBatchResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_batch(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.send_batch(
            emails=[
                {
                    "subject": "Hello Alice",
                    "to": ["alice@example.com"],
                },
                {
                    "subject": "Hello Bob",
                    "to": ["bob@example.com"],
                },
            ],
            from_="notifications@myapp.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSendBatchResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_raw(self, async_client: AsyncArk) -> None:
        email = await async_client.emails.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        )
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_raw(self, async_client: AsyncArk) -> None:
        response = await async_client.emails.with_raw_response.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(SendEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_raw(self, async_client: AsyncArk) -> None:
        async with async_client.emails.with_streaming_response.send_raw(
            data="data",
            mail_from="dev@stainless.com",
            rcpt_to=["dev@stainless.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(SendEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True
