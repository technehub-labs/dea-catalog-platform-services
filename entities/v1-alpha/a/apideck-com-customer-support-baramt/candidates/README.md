# Customer Support (apideck.com:customer-support)

> Welcome to the Customer Support API. You can use this API to access all Customer Support API endpoints. ## Base URL The base URL for all API requests is `https://unify.apideck.com` We also provide a [Mock API](https://developers.apideck.com/mock-api) that can be used for testing purposes: `https://mock-api.apideck.com` ## Headers Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive. | Name | Type | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String | Yes | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id | String | No | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API. | | x-apideck-raw | Boolean | No | Include raw response. Mostly used for debugging purposes. | | x-apideck-app-id | String | Yes | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys. | | Authorization | String | Yes | Bearer API KEY | ## Authorization You can interact with the API through the authorization methods below. <!-- ReDoc-Inject: <security-definitions> --> ## Pagination All API resources have support for bulk retrieval via list APIs. Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters. To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the l

## Identity

- **Record id**: `dea:platform-service-apideck-com-customer-support-baramt`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: apideck.com:customer-support; spec: https://developers.apideck.com)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
