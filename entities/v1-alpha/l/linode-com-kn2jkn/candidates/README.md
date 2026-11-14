# Linode API (linode.com)

> ## Introduction The Linode API provides the ability to programmatically manage the full range of Linode products and services. This reference is designed to assist application developers and system administrators. Each endpoint includes descriptions, request syntax, and examples using standard HTTP requests. Response data is returned in JSON format. This document was generated from our OpenAPI Specification. See the <a target="_top" href="https://www.openapis.org">OpenAPI website</a> for more information. <a target="_top" href="/docs/api/openapi.yaml">Download the Linode OpenAPI Specification</a>. ## Changelog <a target="_top" href="/docs/products/tools/api/release-notes/">View our Changelog</a> to see release notes on all changes made to our API. ## Access and Authentication Some endpoints are publicly accessible without requiring authentication. All endpoints affecting your Account, however, require either a Personal Access Token or OAuth authentication (when using third-party applications). ### Personal Access Token The easiest way to access the API is with a Personal Access Token (PAT) generated from the <a target="_top" href="https://cloud.linode.com/profile/tokens">Linode Cloud Manager</a> or the [Create Personal Access Token](/docs/api/profile/#personal-access-token-create) endpoint. All scopes for the OAuth security model ([defined below](/docs/api/profile/#oauth)) apply to this security model as well. #### Authentication | Security Scheme Type: | HTTP | |-----------------------|------| | **HTTP Authorization Scheme** | bearer | ### OAuth If you only need to access the Linode API for personal use, we recommend that you create a [personal access token](/docs/api/#personal-access-token). If you're designing an application that can authenticate with an arbitrary Linode user, then you should use the OAuth 2.0 workflows presented in this section. For a more detailed example of an OAuth 2.0 implementation, see our guide on [How to Create an OAuth App with the Lino

## Identity

- **Record id**: `dea:platform-service-linode-com-kn2jkn`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: linode.com; spec: https://linode.com)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
