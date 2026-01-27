# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .dns_record import DNSRecord
from .shared.api_meta import APIMeta

__all__ = ["DomainRetrieveResponse", "Data", "DataDNSRecords"]


class DataDNSRecords(BaseModel):
    """DNS records that must be added to your domain's DNS settings.

    Null if records are not yet generated.
    """

    dkim: Optional[DNSRecord] = None
    """A DNS record that needs to be configured in your domain's DNS settings"""

    return_path: Optional[DNSRecord] = FieldInfo(alias="returnPath", default=None)
    """A DNS record that needs to be configured in your domain's DNS settings"""

    spf: Optional[DNSRecord] = None
    """A DNS record that needs to be configured in your domain's DNS settings"""


class Data(BaseModel):
    id: int
    """Unique domain identifier"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when the domain was added"""

    dns_records: Optional[DataDNSRecords] = FieldInfo(alias="dnsRecords", default=None)
    """DNS records that must be added to your domain's DNS settings.

    Null if records are not yet generated.
    """

    name: str
    """The domain name used for sending emails"""

    uuid: str
    """UUID of the domain"""

    verified: bool
    """Whether all DNS records (SPF, DKIM, Return Path) are correctly configured.

    Domain must be verified before sending emails.
    """

    verified_at: Optional[datetime] = FieldInfo(alias="verifiedAt", default=None)
    """Timestamp when the domain ownership was verified, or null if not yet verified"""


class DomainRetrieveResponse(BaseModel):
    data: Data

    meta: APIMeta

    success: Literal[True]
