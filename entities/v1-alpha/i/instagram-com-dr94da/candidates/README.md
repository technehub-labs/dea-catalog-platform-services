# Instagram API (instagram.com)

> Description of Instagram RESTful API. Current limitations: * Instagram service does not support [cross origin headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) for security reasons, therefore it is not possible to use Swagger UI and make API calls directly from browser. * Modification API requests (`POST`, `DELETE`) require additional security [scopes](https://instagram.com/developer/authorization/) that are available for Apps [created on or after Nov 17, 2015](http://instagram.com/developer/review/) and started in [Sandbox Mode](http://instagram.com/developer/sandbox/). * Consider the [Instagram limitations](https://instagram.com/developer/limits/) for API calls that depends on App Mode. **Warning:** For Apps [created on or after Nov 17, 2015](http://instagram.com/developer/changelog/) API responses containing media objects no longer return the `data` field in `comments` and `likes` nodes. Last update: 2015-11-28

## Identity

- **Record id**: `dea:platform-service-instagram-com-dr94da`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: instagram.com; spec: https://instagram.com/developer/support)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
