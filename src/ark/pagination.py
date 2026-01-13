# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "EmailsPageData",
    "EmailsPagePagination",
    "EmailsPageMeta",
    "SyncEmailsPage",
    "AsyncEmailsPage",
    "SuppressionsPageData",
    "SuppressionsPagePagination",
    "SuppressionsPageMeta",
    "SyncSuppressionsPage",
    "AsyncSuppressionsPage",
]

_T = TypeVar("_T")


class EmailsPagePagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = FieldInfo(alias="perPage", default=None)

    total: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class EmailsPageData(GenericModel, Generic[_T]):
    messages: List[_T]

    pagination: EmailsPagePagination


class EmailsPageMeta(BaseModel):
    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)


class SyncEmailsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    success: Optional[bool] = None
    data: Optional[EmailsPageData[_T]] = None
    meta: Optional[EmailsPageMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncEmailsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    success: Optional[bool] = None
    data: Optional[EmailsPageData[_T]] = None
    meta: Optional[EmailsPageMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class SuppressionsPagePagination(BaseModel):
    page: Optional[int] = None

    per_page: Optional[int] = FieldInfo(alias="perPage", default=None)

    total: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class SuppressionsPageData(GenericModel, Generic[_T]):
    pagination: SuppressionsPagePagination

    suppressions: List[_T]


class SuppressionsPageMeta(BaseModel):
    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)


class SyncSuppressionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    success: Optional[bool] = None
    data: Optional[SuppressionsPageData[_T]] = None
    meta: Optional[SuppressionsPageMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = None
        if self.data is not None:
            if self.data.suppressions is not None:  # pyright: ignore[reportUnnecessaryComparison]
                suppressions = self.data.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncSuppressionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    success: Optional[bool] = None
    data: Optional[SuppressionsPageData[_T]] = None
    meta: Optional[SuppressionsPageMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = None
        if self.data is not None:
            if self.data.suppressions is not None:  # pyright: ignore[reportUnnecessaryComparison]
                suppressions = self.data.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.page is not None:
                    current_page = self.data.pagination.page
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.data is not None:
            if self.data.pagination is not None:  # pyright: ignore[reportUnnecessaryComparison]
                if self.data.pagination.total_pages is not None:
                    total_pages = self.data.pagination.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})
