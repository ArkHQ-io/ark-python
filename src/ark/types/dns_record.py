# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DNSRecord"]


class DNSRecord(BaseModel):
    """A DNS record that needs to be configured in your domain's DNS settings"""

    name: str
    """The hostname where the record should be created (relative to your domain)"""

    type: Literal["TXT", "CNAME", "MX"]
    """The DNS record type to create"""

    value: str
    """The value to set for the DNS record"""

    status: Optional[Literal["OK", "Missing", "Invalid"]] = None
    """Current verification status of this DNS record:

    - `OK` - Record is correctly configured and verified
    - `Missing` - Record was not found in your DNS
    - `Invalid` - Record exists but has an incorrect value
    - `null` - Record has not been checked yet
    """
