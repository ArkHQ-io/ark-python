# Emails

Types:

```python
from ark.types import (
    Delivery,
    Pagination,
    SendEmail,
    EmailRetrieveResponse,
    EmailListResponse,
    EmailGetDeliveriesResponse,
    EmailRetryResponse,
    EmailSendBatchResponse,
)
```

Methods:

- <code title="get /emails/{emailId}">client.emails.<a href="./src/ark/resources/emails.py">retrieve</a>(email_id, \*\*<a href="src/ark/types/email_retrieve_params.py">params</a>) -> <a href="./src/ark/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="get /emails">client.emails.<a href="./src/ark/resources/emails.py">list</a>(\*\*<a href="src/ark/types/email_list_params.py">params</a>) -> <a href="./src/ark/types/email_list_response.py">SyncEmailsPage[EmailListResponse]</a></code>
- <code title="get /emails/{emailId}/deliveries">client.emails.<a href="./src/ark/resources/emails.py">get_deliveries</a>(email_id) -> <a href="./src/ark/types/email_get_deliveries_response.py">EmailGetDeliveriesResponse</a></code>
- <code title="post /emails/{emailId}/retry">client.emails.<a href="./src/ark/resources/emails.py">retry</a>(email_id) -> <a href="./src/ark/types/email_retry_response.py">EmailRetryResponse</a></code>
- <code title="post /emails">client.emails.<a href="./src/ark/resources/emails.py">send</a>(\*\*<a href="src/ark/types/email_send_params.py">params</a>) -> <a href="./src/ark/types/send_email.py">SendEmail</a></code>
- <code title="post /emails/batch">client.emails.<a href="./src/ark/resources/emails.py">send_batch</a>(\*\*<a href="src/ark/types/email_send_batch_params.py">params</a>) -> <a href="./src/ark/types/email_send_batch_response.py">EmailSendBatchResponse</a></code>
- <code title="post /emails/raw">client.emails.<a href="./src/ark/resources/emails.py">send_raw</a>(\*\*<a href="src/ark/types/email_send_raw_params.py">params</a>) -> <a href="./src/ark/types/send_email.py">SendEmail</a></code>

# Domains

Types:

```python
from ark.types import DNSRecord, DomainResponse, SuccessResponse, DomainListResponse
```

Methods:

- <code title="post /domains">client.domains.<a href="./src/ark/resources/domains.py">create</a>(\*\*<a href="src/ark/types/domain_create_params.py">params</a>) -> <a href="./src/ark/types/domain_response.py">DomainResponse</a></code>
- <code title="get /domains/{domainId}">client.domains.<a href="./src/ark/resources/domains.py">retrieve</a>(domain_id) -> <a href="./src/ark/types/domain_response.py">DomainResponse</a></code>
- <code title="get /domains">client.domains.<a href="./src/ark/resources/domains.py">list</a>() -> <a href="./src/ark/types/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /domains/{domainId}">client.domains.<a href="./src/ark/resources/domains.py">delete</a>(domain_id) -> <a href="./src/ark/types/success_response.py">SuccessResponse</a></code>
- <code title="post /domains/{domainId}/verify">client.domains.<a href="./src/ark/resources/domains.py">verify</a>(domain_id) -> <a href="./src/ark/types/domain_response.py">DomainResponse</a></code>

# Suppressions

Types:

```python
from ark.types import (
    SuppressionCreateResponse,
    SuppressionRetrieveResponse,
    SuppressionListResponse,
    SuppressionBulkCreateResponse,
)
```

Methods:

- <code title="post /suppressions">client.suppressions.<a href="./src/ark/resources/suppressions.py">create</a>(\*\*<a href="src/ark/types/suppression_create_params.py">params</a>) -> <a href="./src/ark/types/suppression_create_response.py">SuppressionCreateResponse</a></code>
- <code title="get /suppressions/{email}">client.suppressions.<a href="./src/ark/resources/suppressions.py">retrieve</a>(email) -> <a href="./src/ark/types/suppression_retrieve_response.py">SuppressionRetrieveResponse</a></code>
- <code title="get /suppressions">client.suppressions.<a href="./src/ark/resources/suppressions.py">list</a>(\*\*<a href="src/ark/types/suppression_list_params.py">params</a>) -> <a href="./src/ark/types/suppression_list_response.py">SyncEmailsPage[SuppressionListResponse]</a></code>
- <code title="delete /suppressions/{email}">client.suppressions.<a href="./src/ark/resources/suppressions.py">delete</a>(email) -> <a href="./src/ark/types/success_response.py">SuccessResponse</a></code>
- <code title="post /suppressions/bulk">client.suppressions.<a href="./src/ark/resources/suppressions.py">bulk_create</a>(\*\*<a href="src/ark/types/suppression_bulk_create_params.py">params</a>) -> <a href="./src/ark/types/suppression_bulk_create_response.py">SuppressionBulkCreateResponse</a></code>

# Webhooks

Types:

```python
from ark.types import WebhookResponse, WebhookListResponse, WebhookTestResponse
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/ark/resources/webhooks.py">create</a>(\*\*<a href="src/ark/types/webhook_create_params.py">params</a>) -> <a href="./src/ark/types/webhook_response.py">WebhookResponse</a></code>
- <code title="get /webhooks/{webhookId}">client.webhooks.<a href="./src/ark/resources/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/ark/types/webhook_response.py">WebhookResponse</a></code>
- <code title="patch /webhooks/{webhookId}">client.webhooks.<a href="./src/ark/resources/webhooks.py">update</a>(webhook_id, \*\*<a href="src/ark/types/webhook_update_params.py">params</a>) -> <a href="./src/ark/types/webhook_response.py">WebhookResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/ark/resources/webhooks.py">list</a>() -> <a href="./src/ark/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhookId}">client.webhooks.<a href="./src/ark/resources/webhooks.py">delete</a>(webhook_id) -> <a href="./src/ark/types/success_response.py">SuccessResponse</a></code>
- <code title="post /webhooks/{webhookId}/test">client.webhooks.<a href="./src/ark/resources/webhooks.py">test</a>(webhook_id, \*\*<a href="src/ark/types/webhook_test_params.py">params</a>) -> <a href="./src/ark/types/webhook_test_response.py">WebhookTestResponse</a></code>

# Tracking

Types:

```python
from ark.types import (
    APIMeta,
    TrackDomain,
    TrackDomainResponse,
    TrackingListResponse,
    TrackingVerifyResponse,
)
```

Methods:

- <code title="post /tracking">client.tracking.<a href="./src/ark/resources/tracking.py">create</a>(\*\*<a href="src/ark/types/tracking_create_params.py">params</a>) -> <a href="./src/ark/types/track_domain_response.py">TrackDomainResponse</a></code>
- <code title="get /tracking/{trackingId}">client.tracking.<a href="./src/ark/resources/tracking.py">retrieve</a>(tracking_id) -> <a href="./src/ark/types/track_domain_response.py">TrackDomainResponse</a></code>
- <code title="patch /tracking/{trackingId}">client.tracking.<a href="./src/ark/resources/tracking.py">update</a>(tracking_id, \*\*<a href="src/ark/types/tracking_update_params.py">params</a>) -> <a href="./src/ark/types/track_domain_response.py">TrackDomainResponse</a></code>
- <code title="get /tracking">client.tracking.<a href="./src/ark/resources/tracking.py">list</a>() -> <a href="./src/ark/types/tracking_list_response.py">TrackingListResponse</a></code>
- <code title="delete /tracking/{trackingId}">client.tracking.<a href="./src/ark/resources/tracking.py">delete</a>(tracking_id) -> <a href="./src/ark/types/success_response.py">SuccessResponse</a></code>
- <code title="post /tracking/{trackingId}/verify">client.tracking.<a href="./src/ark/resources/tracking.py">verify</a>(tracking_id) -> <a href="./src/ark/types/tracking_verify_response.py">TrackingVerifyResponse</a></code>
