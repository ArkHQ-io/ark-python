# Shared Types

```python
from ark.types import APIMeta
```

# Emails

Types:

```python
from ark.types import (
    EmailRetrieveResponse,
    EmailListResponse,
    EmailRetrieveDeliveriesResponse,
    EmailRetryResponse,
    EmailSendResponse,
    EmailSendBatchResponse,
    EmailSendRawResponse,
)
```

Methods:

- <code title="get /emails/{emailId}">client.emails.<a href="./src/ark/resources/emails.py">retrieve</a>(email_id, \*\*<a href="src/ark/types/email_retrieve_params.py">params</a>) -> <a href="./src/ark/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="get /emails">client.emails.<a href="./src/ark/resources/emails.py">list</a>(\*\*<a href="src/ark/types/email_list_params.py">params</a>) -> <a href="./src/ark/types/email_list_response.py">SyncPageNumberPagination[EmailListResponse]</a></code>
- <code title="get /emails/{emailId}/deliveries">client.emails.<a href="./src/ark/resources/emails.py">retrieve_deliveries</a>(email_id) -> <a href="./src/ark/types/email_retrieve_deliveries_response.py">EmailRetrieveDeliveriesResponse</a></code>
- <code title="post /emails/{emailId}/retry">client.emails.<a href="./src/ark/resources/emails.py">retry</a>(email_id) -> <a href="./src/ark/types/email_retry_response.py">EmailRetryResponse</a></code>
- <code title="post /emails">client.emails.<a href="./src/ark/resources/emails.py">send</a>(\*\*<a href="src/ark/types/email_send_params.py">params</a>) -> <a href="./src/ark/types/email_send_response.py">EmailSendResponse</a></code>
- <code title="post /emails/batch">client.emails.<a href="./src/ark/resources/emails.py">send_batch</a>(\*\*<a href="src/ark/types/email_send_batch_params.py">params</a>) -> <a href="./src/ark/types/email_send_batch_response.py">EmailSendBatchResponse</a></code>
- <code title="post /emails/raw">client.emails.<a href="./src/ark/resources/emails.py">send_raw</a>(\*\*<a href="src/ark/types/email_send_raw_params.py">params</a>) -> <a href="./src/ark/types/email_send_raw_response.py">EmailSendRawResponse</a></code>

# Logs

Types:

```python
from ark.types import LogEntry, LogEntryDetail, LogRetrieveResponse
```

Methods:

- <code title="get /logs/{requestId}">client.logs.<a href="./src/ark/resources/logs.py">retrieve</a>(request_id) -> <a href="./src/ark/types/log_retrieve_response.py">LogRetrieveResponse</a></code>
- <code title="get /logs">client.logs.<a href="./src/ark/resources/logs.py">list</a>(\*\*<a href="src/ark/types/log_list_params.py">params</a>) -> <a href="./src/ark/types/log_entry.py">SyncPageNumberPagination[LogEntry]</a></code>

# Usage

Types:

```python
from ark.types import (
    EmailCounts,
    EmailRates,
    OrgUsageSummary,
    TenantUsageItem,
    UsagePeriod,
    UsageExportResponse,
)
```

Methods:

- <code title="get /usage">client.usage.<a href="./src/ark/resources/usage.py">retrieve</a>(\*\*<a href="src/ark/types/usage_retrieve_params.py">params</a>) -> <a href="./src/ark/types/org_usage_summary.py">OrgUsageSummary</a></code>
- <code title="get /usage/export">client.usage.<a href="./src/ark/resources/usage.py">export</a>(\*\*<a href="src/ark/types/usage_export_params.py">params</a>) -> <a href="./src/ark/types/usage_export_response.py">UsageExportResponse</a></code>
- <code title="get /usage/tenants">client.usage.<a href="./src/ark/resources/usage.py">list_tenants</a>(\*\*<a href="src/ark/types/usage_list_tenants_params.py">params</a>) -> <a href="./src/ark/types/tenant_usage_item.py">SyncPageNumberPagination[TenantUsageItem]</a></code>

# Limits

Types:

```python
from ark.types import LimitsData, LimitRetrieveResponse
```

Methods:

- <code title="get /limits">client.limits.<a href="./src/ark/resources/limits.py">retrieve</a>() -> <a href="./src/ark/types/limit_retrieve_response.py">LimitRetrieveResponse</a></code>

# Tenants

Types:

```python
from ark.types import (
    Tenant,
    TenantCreateResponse,
    TenantRetrieveResponse,
    TenantUpdateResponse,
    TenantDeleteResponse,
)
```

Methods:

- <code title="post /tenants">client.tenants.<a href="./src/ark/resources/tenants/tenants.py">create</a>(\*\*<a href="src/ark/types/tenant_create_params.py">params</a>) -> <a href="./src/ark/types/tenant_create_response.py">TenantCreateResponse</a></code>
- <code title="get /tenants/{tenantId}">client.tenants.<a href="./src/ark/resources/tenants/tenants.py">retrieve</a>(tenant_id) -> <a href="./src/ark/types/tenant_retrieve_response.py">TenantRetrieveResponse</a></code>
- <code title="patch /tenants/{tenantId}">client.tenants.<a href="./src/ark/resources/tenants/tenants.py">update</a>(tenant_id, \*\*<a href="src/ark/types/tenant_update_params.py">params</a>) -> <a href="./src/ark/types/tenant_update_response.py">TenantUpdateResponse</a></code>
- <code title="get /tenants">client.tenants.<a href="./src/ark/resources/tenants/tenants.py">list</a>(\*\*<a href="src/ark/types/tenant_list_params.py">params</a>) -> <a href="./src/ark/types/tenant.py">SyncPageNumberPagination[Tenant]</a></code>
- <code title="delete /tenants/{tenantId}">client.tenants.<a href="./src/ark/resources/tenants/tenants.py">delete</a>(tenant_id) -> <a href="./src/ark/types/tenant_delete_response.py">TenantDeleteResponse</a></code>

## Credentials

Types:

```python
from ark.types.tenants import (
    CredentialCreateResponse,
    CredentialRetrieveResponse,
    CredentialUpdateResponse,
    CredentialListResponse,
    CredentialDeleteResponse,
)
```

Methods:

- <code title="post /tenants/{tenantId}/credentials">client.tenants.credentials.<a href="./src/ark/resources/tenants/credentials.py">create</a>(tenant_id, \*\*<a href="src/ark/types/tenants/credential_create_params.py">params</a>) -> <a href="./src/ark/types/tenants/credential_create_response.py">CredentialCreateResponse</a></code>
- <code title="get /tenants/{tenantId}/credentials/{credentialId}">client.tenants.credentials.<a href="./src/ark/resources/tenants/credentials.py">retrieve</a>(credential_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/credential_retrieve_params.py">params</a>) -> <a href="./src/ark/types/tenants/credential_retrieve_response.py">CredentialRetrieveResponse</a></code>
- <code title="patch /tenants/{tenantId}/credentials/{credentialId}">client.tenants.credentials.<a href="./src/ark/resources/tenants/credentials.py">update</a>(credential_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/credential_update_params.py">params</a>) -> <a href="./src/ark/types/tenants/credential_update_response.py">CredentialUpdateResponse</a></code>
- <code title="get /tenants/{tenantId}/credentials">client.tenants.credentials.<a href="./src/ark/resources/tenants/credentials.py">list</a>(tenant_id, \*\*<a href="src/ark/types/tenants/credential_list_params.py">params</a>) -> <a href="./src/ark/types/tenants/credential_list_response.py">SyncPageNumberPagination[CredentialListResponse]</a></code>
- <code title="delete /tenants/{tenantId}/credentials/{credentialId}">client.tenants.credentials.<a href="./src/ark/resources/tenants/credentials.py">delete</a>(credential_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/credential_delete_response.py">CredentialDeleteResponse</a></code>

## Domains

Types:

```python
from ark.types.tenants import (
    DNSRecord,
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainVerifyResponse,
)
```

Methods:

- <code title="post /tenants/{tenantId}/domains">client.tenants.domains.<a href="./src/ark/resources/tenants/domains.py">create</a>(tenant_id, \*\*<a href="src/ark/types/tenants/domain_create_params.py">params</a>) -> <a href="./src/ark/types/tenants/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /tenants/{tenantId}/domains/{domainId}">client.tenants.domains.<a href="./src/ark/resources/tenants/domains.py">retrieve</a>(domain_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="get /tenants/{tenantId}/domains">client.tenants.domains.<a href="./src/ark/resources/tenants/domains.py">list</a>(tenant_id) -> <a href="./src/ark/types/tenants/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /tenants/{tenantId}/domains/{domainId}">client.tenants.domains.<a href="./src/ark/resources/tenants/domains.py">delete</a>(domain_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="post /tenants/{tenantId}/domains/{domainId}/verify">client.tenants.domains.<a href="./src/ark/resources/tenants/domains.py">verify</a>(domain_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/domain_verify_response.py">DomainVerifyResponse</a></code>

## Suppressions

Types:

```python
from ark.types.tenants import (
    SuppressionCreateResponse,
    SuppressionRetrieveResponse,
    SuppressionListResponse,
    SuppressionDeleteResponse,
)
```

Methods:

- <code title="post /tenants/{tenantId}/suppressions">client.tenants.suppressions.<a href="./src/ark/resources/tenants/suppressions.py">create</a>(tenant_id, \*\*<a href="src/ark/types/tenants/suppression_create_params.py">params</a>) -> <a href="./src/ark/types/tenants/suppression_create_response.py">SuppressionCreateResponse</a></code>
- <code title="get /tenants/{tenantId}/suppressions/{email}">client.tenants.suppressions.<a href="./src/ark/resources/tenants/suppressions.py">retrieve</a>(email, \*, tenant_id) -> <a href="./src/ark/types/tenants/suppression_retrieve_response.py">SuppressionRetrieveResponse</a></code>
- <code title="get /tenants/{tenantId}/suppressions">client.tenants.suppressions.<a href="./src/ark/resources/tenants/suppressions.py">list</a>(tenant_id, \*\*<a href="src/ark/types/tenants/suppression_list_params.py">params</a>) -> <a href="./src/ark/types/tenants/suppression_list_response.py">SyncPageNumberPagination[SuppressionListResponse]</a></code>
- <code title="delete /tenants/{tenantId}/suppressions/{email}">client.tenants.suppressions.<a href="./src/ark/resources/tenants/suppressions.py">delete</a>(email, \*, tenant_id) -> <a href="./src/ark/types/tenants/suppression_delete_response.py">SuppressionDeleteResponse</a></code>

## Webhooks

Types:

```python
from ark.types.tenants import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookListDeliveriesResponse,
    WebhookReplayDeliveryResponse,
    WebhookRetrieveDeliveryResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /tenants/{tenantId}/webhooks">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">create</a>(tenant_id, \*\*<a href="src/ark/types/tenants/webhook_create_params.py">params</a>) -> <a href="./src/ark/types/tenants/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /tenants/{tenantId}/webhooks/{webhookId}">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">retrieve</a>(webhook_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="patch /tenants/{tenantId}/webhooks/{webhookId}">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">update</a>(webhook_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/webhook_update_params.py">params</a>) -> <a href="./src/ark/types/tenants/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /tenants/{tenantId}/webhooks">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">list</a>(tenant_id) -> <a href="./src/ark/types/tenants/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /tenants/{tenantId}/webhooks/{webhookId}">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">delete</a>(webhook_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /tenants/{tenantId}/webhooks/{webhookId}/deliveries">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">list_deliveries</a>(webhook_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/webhook_list_deliveries_params.py">params</a>) -> <a href="./src/ark/types/tenants/webhook_list_deliveries_response.py">WebhookListDeliveriesResponse</a></code>
- <code title="post /tenants/{tenantId}/webhooks/{webhookId}/deliveries/{deliveryId}/replay">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">replay_delivery</a>(delivery_id, \*, tenant_id, webhook_id) -> <a href="./src/ark/types/tenants/webhook_replay_delivery_response.py">WebhookReplayDeliveryResponse</a></code>
- <code title="get /tenants/{tenantId}/webhooks/{webhookId}/deliveries/{deliveryId}">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">retrieve_delivery</a>(delivery_id, \*, tenant_id, webhook_id) -> <a href="./src/ark/types/tenants/webhook_retrieve_delivery_response.py">WebhookRetrieveDeliveryResponse</a></code>
- <code title="post /tenants/{tenantId}/webhooks/{webhookId}/test">client.tenants.webhooks.<a href="./src/ark/resources/tenants/webhooks.py">test</a>(webhook_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/webhook_test_params.py">params</a>) -> <a href="./src/ark/types/tenants/webhook_test_response.py">WebhookTestResponse</a></code>

## Tracking

Types:

```python
from ark.types.tenants import (
    TrackDomain,
    TrackingCreateResponse,
    TrackingRetrieveResponse,
    TrackingUpdateResponse,
    TrackingListResponse,
    TrackingDeleteResponse,
    TrackingVerifyResponse,
)
```

Methods:

- <code title="post /tenants/{tenantId}/tracking">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">create</a>(tenant_id, \*\*<a href="src/ark/types/tenants/tracking_create_params.py">params</a>) -> <a href="./src/ark/types/tenants/tracking_create_response.py">TrackingCreateResponse</a></code>
- <code title="get /tenants/{tenantId}/tracking/{trackingId}">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">retrieve</a>(tracking_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/tracking_retrieve_response.py">TrackingRetrieveResponse</a></code>
- <code title="patch /tenants/{tenantId}/tracking/{trackingId}">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">update</a>(tracking_id, \*, tenant_id, \*\*<a href="src/ark/types/tenants/tracking_update_params.py">params</a>) -> <a href="./src/ark/types/tenants/tracking_update_response.py">TrackingUpdateResponse</a></code>
- <code title="get /tenants/{tenantId}/tracking">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">list</a>(tenant_id) -> <a href="./src/ark/types/tenants/tracking_list_response.py">TrackingListResponse</a></code>
- <code title="delete /tenants/{tenantId}/tracking/{trackingId}">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">delete</a>(tracking_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/tracking_delete_response.py">TrackingDeleteResponse</a></code>
- <code title="post /tenants/{tenantId}/tracking/{trackingId}/verify">client.tenants.tracking.<a href="./src/ark/resources/tenants/tracking.py">verify</a>(tracking_id, \*, tenant_id) -> <a href="./src/ark/types/tenants/tracking_verify_response.py">TrackingVerifyResponse</a></code>

## Usage

Types:

```python
from ark.types.tenants import (
    TenantUsage,
    TenantUsageTimeseries,
    UsageRetrieveResponse,
    UsageRetrieveTimeseriesResponse,
)
```

Methods:

- <code title="get /tenants/{tenantId}/usage">client.tenants.usage.<a href="./src/ark/resources/tenants/usage.py">retrieve</a>(tenant_id, \*\*<a href="src/ark/types/tenants/usage_retrieve_params.py">params</a>) -> <a href="./src/ark/types/tenants/usage_retrieve_response.py">UsageRetrieveResponse</a></code>
- <code title="get /tenants/{tenantId}/usage/timeseries">client.tenants.usage.<a href="./src/ark/resources/tenants/usage.py">retrieve_timeseries</a>(tenant_id, \*\*<a href="src/ark/types/tenants/usage_retrieve_timeseries_params.py">params</a>) -> <a href="./src/ark/types/tenants/usage_retrieve_timeseries_response.py">UsageRetrieveTimeseriesResponse</a></code>

# Platform

## Webhooks

Types:

```python
from ark.types.platform import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookListDeliveriesResponse,
    WebhookReplayDeliveryResponse,
    WebhookRetrieveDeliveryResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /platform/webhooks">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">create</a>(\*\*<a href="src/ark/types/platform/webhook_create_params.py">params</a>) -> <a href="./src/ark/types/platform/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /platform/webhooks/{webhookId}">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/ark/types/platform/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="patch /platform/webhooks/{webhookId}">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">update</a>(webhook_id, \*\*<a href="src/ark/types/platform/webhook_update_params.py">params</a>) -> <a href="./src/ark/types/platform/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /platform/webhooks">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">list</a>() -> <a href="./src/ark/types/platform/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /platform/webhooks/{webhookId}">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">delete</a>(webhook_id) -> <a href="./src/ark/types/platform/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="get /platform/webhooks/deliveries">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">list_deliveries</a>(\*\*<a href="src/ark/types/platform/webhook_list_deliveries_params.py">params</a>) -> <a href="./src/ark/types/platform/webhook_list_deliveries_response.py">SyncPageNumberPagination[WebhookListDeliveriesResponse]</a></code>
- <code title="post /platform/webhooks/deliveries/{deliveryId}/replay">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">replay_delivery</a>(delivery_id) -> <a href="./src/ark/types/platform/webhook_replay_delivery_response.py">WebhookReplayDeliveryResponse</a></code>
- <code title="get /platform/webhooks/deliveries/{deliveryId}">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">retrieve_delivery</a>(delivery_id) -> <a href="./src/ark/types/platform/webhook_retrieve_delivery_response.py">WebhookRetrieveDeliveryResponse</a></code>
- <code title="post /platform/webhooks/{webhookId}/test">client.platform.webhooks.<a href="./src/ark/resources/platform/webhooks.py">test</a>(webhook_id, \*\*<a href="src/ark/types/platform/webhook_test_params.py">params</a>) -> <a href="./src/ark/types/platform/webhook_test_response.py">WebhookTestResponse</a></code>
