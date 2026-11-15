# Pendo Feedback API (pendo.io)

> ## Who is this for? This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration. ## Authentication API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'. ## Endpoint API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located. ## Notes API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname. ## Generating client code This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)

## Identity

- **Record id**: `dea:platform-service-pendo-io-ss266q`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: pendo.io; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
