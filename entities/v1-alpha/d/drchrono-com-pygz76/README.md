# drchrono.com (drchrono.com)

> This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href="/api-docs-old/tutorial">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section. # Authorization ## Initial authorization There are three main steps in the OAuth 2.0 authentication workflow: 1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to your web application. 3. Your application exchanges the `authorization_code` that came with the redirect for an `access_token` and `refresh_token`. ### Step 1: Redirect to drchrono The first step is redirecting your user to drchrono, typically with a button labeled "Connect to drchrono" or "Login with drchrono". This is just a link that takes your user to the following URL: https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes. The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested. Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends "Happy Birthday!" emails to a doctor's patients on their birthdays would use the scope parameter `"patients:summary:read"`, while one that allows patients to schedule appointments online would need a

## Identity

- **Record id**: `dea:platform-service-drchrono-com-pygz76`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: drchrono.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
