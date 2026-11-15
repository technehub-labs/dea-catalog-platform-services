# ThreatJammer.com User API (threatjammer.com)

> The public API open to the users. [Read the docs and learn more.](https://threatjammer.com/docs). ## General information ### Description Threat Jammer supports two end-user REST APIs: the User API and the Report API. The end-user uses the User API to interact with the different databases, heuristics, and machine learning processes. Devices use the Report API to interact with Threat Jammer. This document will explain how to use the User API and interact with the different services, create a token, interpret the quota information, and create the HTTP request to interact with the User API. ### Authentication The API is protected by a **Bearer authentication** schema. **Bearer authentication** (also called **token authentication**) is an HTTP authentication scheme that involves security tokens called bearer tokens. It is used to authenticate the user. All the different endpoints expect a `Bearer` token in the `Authorization` header. Example: ``` curl -X 'GET' 'https://dublin.api.threatjammer.com/test' -H 'accept: application/json' -H 'Authorization: Bearer YOUR_API_KEY' ``` You can obtain a token after registering on the [ThreatJammer.com](https://threatjammer.com) website for free. ### Region specific tokens All the `Bearer` tokens contain information about the authorized region. The developers have to use a token created for the region they want to use. A token used in a different region will return a `401 Unauthorized` error. ### Global errors The API will return the following permanent errors: - a `401 Unauthorized` error if the token is not valid, or does not belong to the region. - a `401 Unauthorized` error if the token does not exist. - a `401 Unauthorized` error if the token is malformed. - a `403 Forbidden` error if the subscription level is not enough. Some endpoints are only available for paid subscription levels. And these temporary errors: - a `429 Too Many Requests` error if the quota is exceeded (see below). ### Quota limits **Every request to the User A

## Identity

- **Record id**: `dea:platform-service-threatjammer-com-p8sr6w`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: threatjammer.com; spec: https://threatjammer.com/contactus)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
