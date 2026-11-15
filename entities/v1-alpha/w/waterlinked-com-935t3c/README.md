# The Water Linked Underwater GPS API (waterlinked.com)

> API for the Water Linked Underwater GPS. For more details: http://www.waterlinked.com Recommended approach for connecting to a Underwater GPS via the API is: - If "GET /api/" times out, the Underwater GPS is not running (on this IP address) - If "GET /api/" responds with 200 OK check that the api version returrned (eg "v1") is supported by the client (eg: also supports "v1"). - If the api version returned does not match what the client supports: give an error to the user and recommend upgrading. (Eg: response is "v2" while client only supports "v1") - If "GET /api/" responds with 301 Moved permanently. "GET /api/v1/version" to check if the kit has a version earlier than 1.5. - "GET /api/v1/version" will always respond with 200 OK on Underwater GPS earlier than 1.5 release. Configuration API is is not considered stable and will potentially be changed

## Identity

- **Record id**: `dea:platform-service-waterlinked-com-935t3c`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: waterlinked.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
