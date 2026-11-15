# ART19 Content API Documentation (art19.com)

> The ART19 Content API conforms to the [JSON:API specification](http://jsonapi.org). API requests **MUST** use the HTTP Accept header: `Accept: application/vnd.api+json` API requests **MUST** be authenticated using the HTTP Authorization header: `Authorization: Token token="your-token", credential="your-credential"` ## General Notes Some query parameters use unencoded [ and ] characters simply for readability. Defaults, examples, and possible values are additionally rendered in double quotes for readability. In practice, query parameters should not have quotes around the values (e.g., `foo=bar` is valid, not `foo="bar"`), and both query parameter keys and values must be percent-encoded, per the requirements in [RFC 3986 § 3.4](https://tools.ietf.org/html/rfc3986#section-3.4). ## Rate Limiting In order to provide a fair distribution of available resources, all API calls are subject to rate limits. If you exceed the number of API calls per minute granted to your credential, a `429 Too Many Requests` error response will be returned. In that case, a `Retry-After` header MAY be included in the response, describing the number of seconds after which a request can be retried. If you run into a high number of 429 errors, please reach out to ART19 Support to adjust your rate limit. ### Example In the following example the request can be retried after waiting for 21 seconds: HTTP/1.1 429 Too Many Requests Content-Type: text/html Retry-After: 21 ## Pagination Requests to collection endpoints **SHOULD** provide pagination parameters. Some endpoints **REQUIRE** pagination parameters to be provided. Whenever pagination is provided, it **MUST** be valid. Failing to provide pagination when it is required or providing wrong or incomplete pagination always results in a `400 Bad Request` error response. The page numbering starts with `1` and the maximum page size (if not otherwise documented on an endpoint) is `100`. Pagination **MUST NOT** be specified if requesting a list of IDs (usin

## Identity

- **Record id**: `dea:platform-service-art19-com-hu6ugk`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: art19.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
