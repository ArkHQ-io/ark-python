# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "PageNumberPaginationMeta",
    "SyncPageNumberPagination",
    "AsyncPageNumberPagination",
    "OffsetPaginationData",
    "OffsetPaginationPagination",
    "SyncOffsetPagination",
    "AsyncOffsetPagination",
]

_T = TypeVar("_T")


class PageNumberPaginationMeta(BaseModel):
    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)


class SyncPageNumberPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page: Optional[int] = None
    per_page: Optional[int] = FieldInfo(alias="perPage", default=None)
    total: Optional[int] = None
    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    meta: Optional[PageNumberPaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPageNumberPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    page: Optional[int] = None
    per_page: Optional[int] = FieldInfo(alias="perPage", default=None)
    total: Optional[int] = None
    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    meta: Optional[PageNumberPaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class OffsetPaginationPagination(BaseModel):
    has_more: Optional[bool] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


class OffsetPaginationData(GenericModel, Generic[_T]):
    pagination: Optional[OffsetPaginationPagination] = None

    tenants: Optional[List[_T]] = None


class SyncOffsetPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[OffsetPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tenants = None
        if self.data is not None:
            if self.data.tenants is not None:
                tenants = self.data.tenants
        if not tenants:
            return []
        return tenants

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.offset is not None:
                    offset = self.data.pagination.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total is not None:
                    total = self.data.pagination.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncOffsetPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[OffsetPaginationData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tenants = None
        if self.data is not None:
            if self.data.tenants is not None:
                tenants = self.data.tenants
        if not tenants:
            return []
        return tenants

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.offset is not None:
                    offset = self.data.pagination.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.total is not None:
                    total = self.data.pagination.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None
