# SimplyRETS (simplyrets.com)

> The SimplyRETS API is an exciting step towards making it easier for developers and real estate agents to build something awesome with real estate data! The documentation below makes live requests to our API using the trial data. To get set up with the API using live MLS data, you must have RETS credentials from your MLS, which you can then use to create an app with SimplyRETS. For more information on that process, please see our [FAQ](https://simplyrets.com/faq), [Getting Started](https://simplyrets.com/blog/getting-set-up.html) page, or [contact us](https://simplyrets.com/\#home-contact). Below you'll find the API endpoints, query parameters, response bodies, and other information about using the SimplyRETS API. You can run queries by clicking the 'Try it Out' button at the bottom of each section. ### Authentication The SimplyRETS API uses Basic Authentication. When you create an app, you'll get a set of API credentials to access your listings. If you're trying out the test data, you can use `simplyrets:simplyrets` for connecting to the API. ### Media Types The SimplyRETS API uses the `Accept` header to allow clients to control media types (content versions). We maintain backwards compatibility with API clients by allowing them to specify a content version. We highly recommend setting and explicity media type when your application reaches production. Both the structure and content of our API response bodies is subject to change so we can add new features while respecting the stability of applications which have already been developed. To always use the latest SimplyRETS content version, simply use `application/json` in your application `Accept` header. If you want to pin your clients media type to a specific version, you can use the vendor-specific SimplyRETS media type, e.g. `application/vnd.simplyrets-v0.1+json"` To view all valid content-types for making an `OPTIONS`, make a request to the SimplyRETS api root `curl -XOPTIONS -u simplyrets:simplyrets https://api.

## Identity

- **Record id**: `dea:platform-service-simplyrets-com-q2q3nv`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: simplyrets.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
