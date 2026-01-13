# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPageNumber", "AsyncPageNumber", "SyncSuppressionsPage", "AsyncSuppressionsPage"]

_T = TypeVar("_T")


class SyncPageNumber(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncPageNumber(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class SyncSuppressionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    suppressions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = self.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncSuppressionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    suppressions: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        suppressions = self.suppressions
        if not suppressions:
            return []
        return suppressions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})
