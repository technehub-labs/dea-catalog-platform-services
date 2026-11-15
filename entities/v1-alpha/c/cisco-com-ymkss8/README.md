# Cisco PSIRT openVuln API (cisco.com)

> The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). For more information about the Cisco PSIRT openVuln API visit https://developer.cisco.com/site/PSIRT/discover/overview For detail steps on how to use the API go to:https://developer.cisco.com/site/PSIRT/get-started/getting-started.gsp This is a beta release of a swagger YAML for the Cisco PSIRT openVuln API To access the API sign in with your Cisco CCO account at http://apiconsole.cisco.com and register an application to recieve a client_id and a client_secret You can then get your token using curl or any other method you prefer. 'curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=<your_client_id>" -d "client_secret=<your_client_secret>" -d "grant_type=client_credentials" https://cloudsso.cisco.com/as/token.oauth2' You will receive an access token as demonstrated in the following example: '{"access_token":"I7omWtBDAieSiUX3shOxNJfuy4J6","token_type":"Bearer","expires_in":3599}' In Swagger, click on Change Authentication enter the text "I7omWtBDAieSiUX3shOxNJfuy4J6" (which is the token you received) then click on "Try this operation"

## Identity

- **Record id**: `dea:platform-service-cisco-com-ymkss8`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: cisco.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
