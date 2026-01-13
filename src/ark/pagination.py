# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from datetime import datetime
from typing_extensions import Literal, override

from pydantic import Field as FieldInfo

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "PageNumberPaginationData",
    "PageNumberPaginationMessage",
    "PageNumberPaginationPagination",
    "SyncPageNumberPagination",
    "AsyncPageNumberPagination",
    "SuppressionsPaginationData",
    "SuppressionsPaginationPagination",
    "SuppressionsPaginationSuppression",
    "SyncSuppressionsPagination",
    "AsyncSuppressionsPagination",
]

_T = TypeVar("_T")


class PageNumberPaginationMessage(BaseModel):
    id: str
    """Internal message ID"""

    token: str

    from_: str = FieldInfo(alias="from")

    status: Literal["pending", "sent", "softfail", "hardfail", "bounced", "held"]
    """Current delivery status:

    - `pending` - Email accepted, waiting to be processed
    - `sent` - Email transmitted to recipient's mail server
    - `softfail` - Temporary delivery failure, will retry
    - `hardfail` - Permanent delivery failure
    - `bounced` - Email bounced back
    - `held` - Held for manual review
    """

    subject: str

    timestamp: float

    timestamp_iso: datetime = FieldInfo(alias="timestampIso")

    to: str

    tag: Optional[str] = None


class PageNumberPaginationPagination(BaseModel):
    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class PageNumberPaginationData(GenericModel, Generic[_T]):
    messages: Optional[List[_T]] = None

    pagination: Optional[PageNumberPaginationPagination] = None


class SyncPageNumberPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[PageNumberPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPageNumberPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[PageNumberPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class SuppressionsPaginationPagination(BaseModel):
    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class SuppressionsPaginationSuppression(BaseModel):
    id: str
    """Suppression ID"""

    address: str

    created_at: datetime = FieldInfo(alias="createdAt")

    reason: Optional[str] = None


class SuppressionsPaginationData(GenericModel, Generic[_T]):
    pagination: Optional[SuppressionsPaginationPagination] = None

    suppressions: Optional[List[_T]] = None


class SyncSuppressionsPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[SuppressionsPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = None
        if self.data is not None:
            if self.data.suppressions is not None:
                suppressions = self.data.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncSuppressionsPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[SuppressionsPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = None
        if self.data is not None:
            if self.data.suppressions is not None:
                suppressions = self.data.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})
