# Probely Developers (probely.com)

> Probely is a Web Vulnerability Scanning suite for Agile Teams. It provides continuous scanning of your Web Applications and lets you efficiently manage the lifecycle of the vulnerabilities found, in a sleek and intuitive ~~web interface~~ API. ## Quick-Start ### Authentication To use the API, you first need to create a token (API Key). To create a token, select a target from the drop-down list, go to the "Settings" page, and click on the "Integrations" tab. Write a name for the API Key. For example, if you want to use the API Key for travis, you could name it "travis". In this example, we chose "**example.com_key**" ![Creating API key][1] [1]: assets/qs/create_api_key_1.png The API key was created successfully: ![API key created][2] [2]: assets/qs/create_api_key_2.png On every request, you need to pass this token in the authorization header, like this: ```yaml Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJBRlNJQlp 3elFsMDEiLCJ1c2VybmFtZSI6IkNIZ2tkSUROdzV0NSJ9.90UwiPGS2hlvgOLktFU0LfKuatNKm mEP79u17VnqT9M ``` **WARNING: Treat this token as a password. With this token, you have the power to fully manage the target.** In the following examples, the token will be named as *PROBELY_AUTH_TOKEN*. ### Scan target First let's view our target list: ```bash curl https://api.probely.com/targets/ \ -X GET \ -H "Content-Type: application/json" \ -H "Authorization: JWT PROBELY_AUTH_TOKEN" ``` From the results, we need the **target id**: ```json { "count":1, "page_total":1, "page":1, "length":10, "results":[ { "id":"AxtkqTE0v3E-", "name":"test-site", "desc":"", "url":"https://test-site.example.com", "settings": "(...)" , "stack": "(...)" , "verified":true, "(...)": "(...)" } ] } ``` Now we can send a request to start a scan on target id **AxtkqTE0v3E-** ```bash curl https://api.probely.com/targets/AxtkqTE0v3E-/scan_now/ \ -X POST \ -H "Content-Type: application/json" \ -H "Authorization: JWT PROBELY_AUTH_TOKEN" ``` And we get a response saying that the scan is s

## Identity

- **Record id**: `dea:platform-service-probely-com-qh8fv2`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: probely.com; spec: https://probely.com)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
