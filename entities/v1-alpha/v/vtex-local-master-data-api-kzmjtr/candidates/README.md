# Master Data API - v2 (vtex.local:Master-Data-API-)

> # ATTENTION: **This version isn't compliant with data entities of old version (e.g. CL and AD). It's possible to use this configuration only to new data entities.** ## Welcome! VTEX Master Data is an easy-to-use, secure, fast, scalable and extensible repository. On it you can create your own Entities, store data and consult directly from the storefront or use it to store info for some external integration. There are internal VTEX modules that use VTEX Master Data as data repository. We have the VTEX Customer Service, VTEX Profile System and VTEX InStore, for example. It is also used by other internal services. There are two ways to use Master Data: 1. Directly from the storefront 2. External integration ### Directly from the storefront If your scenario is to be used inside the storefront, be aware of the following observations: 1. Use the storefront host to query or store information to avoid **CORS**; 2. Configure which information should be public and which shouldn't, inside the JSON Schema of the Data Entity; 3. Do not create query loops (the storefront may be affected with Throttling and apis may be turned off as a security protection); 4. Never add via JS any type of authentication key (x-vtex-api-appkey or x-vtex-api-apptoken); **It's important to avoid CORS using the relative path** ### External Integration If your scenario is to perform external integration, such as migrating client data from another service, be aware of the following observations: 1. Use the host ```{{accountName}}.vtexcommercestable.com.br```; 2. Use the authentication keys (x-vtex-api-appkey ou x-vtex-api-apptoken); ### Most used attributes listed here | Name | Description | | -------- | -------- | | accountName | Account name in VTEX License Manager | | name | Data Entity name | | schema | JSON Schema of a Data Entity | | id | Identifier of a document | | x-vtex-api-appKey | User key | | x-vtex-api-appToken | User token |

## Identity

- **Record id**: `dea:platform-service-vtex-local-master-data-api-kzmjtr`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: vtex.local:Master-Data-API-; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
