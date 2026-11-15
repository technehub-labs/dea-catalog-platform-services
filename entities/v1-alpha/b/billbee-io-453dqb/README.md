# Billbee API (billbee.io)

> Documentation of the Billbee REST API to connect a Billbee account to external aplications. ## Endpoint The Billbee API endpoint base url is https://api.billbee.io/api/v1 ## Activation You have to enable the API in the settings of your Billbee account. In addition you need a Billbee API Key identifying the application you develop. To get an API key, send a mail to support@billbee.io and send us a short note about what you are building. ## Authorization & security Because you can access private data with the Billbee API, every request has to be sent over https and must * Contain a valid API Key identifying the application/developer. It has to be sent as the HTTP header X-Billbee-Api-Key * Contain a valid user login with billbee username and api password in form of a basic auth HTTP header ## Throttling Each endpoint has a throttle of max 2 requests per second per combination of API Key and Billbee user. When you exceed these 2 calls, the API will return a HTTP 429 status code

## Identity

- **Record id**: `dea:platform-service-billbee-io-453dqb`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: billbee.io; spec: https://www.billbee.io)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
