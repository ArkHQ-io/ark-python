# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "EmailsPageData",
    "EmailsPagePagination",
    "SyncEmailsPage",
    "AsyncEmailsPage",
    "SuppressionsPageData",
    "SuppressionsPagePagination",
    "SyncSuppressionsPage",
    "AsyncSuppressionsPage",
]

_T = TypeVar("_T")


class EmailsPagePagination(BaseModel):
    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class EmailsPageData(GenericModel, Generic[_T]):
    messages: Optional[List[_T]] = None

    pagination: Optional[EmailsPagePagination] = None


class SyncEmailsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[EmailsPageData[_T]] = None

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


class AsyncEmailsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[EmailsPageData[_T]] = None

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


class SuppressionsPagePagination(BaseModel):
    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)


class SuppressionsPageData(GenericModel, Generic[_T]):
    pagination: Optional[SuppressionsPagePagination] = None

    suppressions: Optional[List[_T]] = None


class SyncSuppressionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[SuppressionsPageData[_T]] = None

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


class AsyncSuppressionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[SuppressionsPageData[_T]] = None

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
