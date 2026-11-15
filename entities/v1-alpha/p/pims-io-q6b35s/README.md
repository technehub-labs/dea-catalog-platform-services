# Pims (pims.io)

> Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions). ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized. As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.) <div class="info"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io): <ul> <li>Base path: `https://demo.pims.io/api`</li> <li>Username: `demo`</li> <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li> </ul> </div> ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs. Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style="-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;"> <div style="display: inline-block; width:100%;"> <strong>So when you read in the doc:</strong> <pre><code class="lang-json">{ <span class="token string">"id"</span>: <span class="token number">123</span>, <span class="token string">"property1"</span>: <span class="token string">"Lorem ipsum"</span>,

## Identity

- **Record id**: `dea:platform-service-pims-io-q6b35s`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: pims.io; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
