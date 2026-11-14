# Proxy API (apideck.com:proxy)

> Welcome to the Proxy API. You can use this API to access all Proxy API endpoints. ## Base URL The base URL for all API requests is `https://unify.apideck.com` ## Headers Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive. | Name | Type | Required | Description | | ---------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | | Authorization | String | Yes | Bearer API KEY | | x-apideck-app-id | String | Yes | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys. | | x-apideck-consumer-id | String | Yes | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-downstream-url | String | Yes | Downstream URL to forward the request too | | x-apideck-downstream-authorization | String | No | Downstream authorization header. This will skip the Vault token injection. | | x-apideck-downstream-method | String | No | Downstream method. If not provided the upstream method will be inherited, depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | | x-apideck-service-id | String | No | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API. | ## Authorization You can interact with the API through the authorization methods below. ### apiKey To use API you have to sign up and get your own API key. Unify API accounts have sandbox mode and live mode API keys. To change modes just use the appropriate key to get a live or test object. You can find your API keys on the unify settings of your Apideck app. Your

## Identity

- **Record id**: `dea:platform-service-apideck-com-proxy-a85xcg`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: apideck.com:proxy; spec: https://developers.apideck.com)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
