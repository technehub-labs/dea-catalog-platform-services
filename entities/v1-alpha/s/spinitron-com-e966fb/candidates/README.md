# Spinitron v2 API (spinitron.com)

> ## Notes **Tutorial demo** using this API is at [https://spinitron.com/v2-api-demo/](https://spinitron.com/v2-api-demo/). For web integration using iframes and/or JavaScript instead of an API, see [https://spinitron.github.io/v2-web-integration/](https://spinitron.github.io/v2-web-integration/). **Your API key** is found in the Spinitron web app. Log in to Spinitron and go to *Automation & API* in the *Admin* menu. **Authenticate** by presenting your API key using either HTTP Bearer Authorization (preferred) curl -H 'Authorization: Bearer YOURAPIKEY' 'https://spinitron.com/api/spins' or in the query parameter `access-token` (less secure owing to webserver log files) curl 'https://spinitron.com/api/spins?access-token=YOURAPIKEY' **Limit** per page of results is 20 by default and miximally 200. **Try it out** below works to generate example cURL requests but not to get responses from Spinitron. We do not accept queries sent from web browsers. Copy-paste the cURL commands and run them from your computer. **Cache** the data you get from the API if you are using it in web or mobile integration. It's not ok to query the API on *every* page request you serve. The [demo](https://spinitron.com/v2-api-demo/) shows how easy it can be to implement a file cache. An extension to this API with access to all stations for partner applications is available. Contact us.

## Identity

- **Record id**: `dea:platform-service-spinitron-com-e966fb`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: spinitron.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
