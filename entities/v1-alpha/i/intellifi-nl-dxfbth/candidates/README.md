# Brain Web API (intellifi.nl)

> This document describes the [Intellifi Brain](https://intellifi.zendesk.com/hc/en-us/categories/360000685454) Web API specification using the [OpenAPI specification](https://github.com/OAI/OpenAPI-Specification). The Brain Web API is a RESTful API that allows you to interact with the [Intellifi devices](https://intellifi.zendesk.com/hc/en-us/categories/360000685434) and services in a powerful and simple way. Our end-to-end solution allows you to localize your items/assets based on technologies such as RFID and Bluetooth. # Try it out! The API can be tried out and tested using the ['api-doc/tryitout' endpoint on this site](./tryitout/). This UI allows anyone to visualize and interact with the API’s resources without having any of the implementation logic in place. It’s automatically generated from this Specification, with the visual documentation making it easy for back end implementation and client side consumption. # Authentication Applications are required to provide some form of authentication to the API for every secured endpoint. The Brain offers two forms of authentication. - API key (Via an HTTP request header or URL parameter) - Session cookie <!-- ReDoc-Inject: <security-definitions> --> # See also - About Intellifi and what we do: [intellifi.nl](https://intellifi.nl) - Technical and background information: [intellifi.zendesk.com](https://intellifi.zendesk.com)

## Identity

- **Record id**: `dea:platform-service-intellifi-nl-dxfbth`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: intellifi.nl; spec: https://intellifi.zendesk.com)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
