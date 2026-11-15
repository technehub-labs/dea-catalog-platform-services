# Discourse API Documentation (discourse.local)

> This page contains the documentation on how to use Discourse through API calls. > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint. ### Request Content-Type The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`. ### Endpoint Names and Response Content-Type Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format. Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format. ### Authentication Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated. To become authenticated you will need to create an API Key from the admin panel. Once you have your API Key you can pass it in along with your API Username as an HTTP header like this: ``` curl -X GET "http://127.0.0.1:3000/admin/users/list/active.json" \ -H "Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19" \ -H "Api-Username: system" ``` and this is how POST requests will look: ``` curl -X POST "http://127.0.0.1:3000/categories" \ -H "Content-Type: multipart/form-data;" \ -H "Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19" \ -H "Api-Username: system" \ -F "name=89853c20-4409-e91a-a8ea-f6cdff96aaaa" \ -F "color=49d9e9" \ -F "text_color=f0fcfd" ``` ### Boolean values If an end

## Identity

- **Record id**: `dea:platform-service-discourse-local-t98cgj`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: discourse.local; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
