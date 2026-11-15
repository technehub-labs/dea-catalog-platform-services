# Contract.fit API (contract-p.fit)

> This OpenAPI describes the API exposed by the contract.fit backend. ## Security ### Authentication All endpoints are protected: you need to make authenticated calls. There are 3 authentication mechanisms: - HTTP Basic (Username + Password) - JWT Token - API-Key By default you should have an account allowing you to bootstrap your tenant and create users and roles, using Basic Auth or after creating a Token - see */auth* endpoints. If you are missing credentials or permissions, please [contact us](https://contract.fit/contact-us). ### Authorization The security system is RBAC based: users must be granted scoped roles, allowing them to access resources. Each role grants a defined set of permissions, which can be restricted to a given inbox or document - see */roles* endpoints. ## Upload and Processing Below is a short description of common use cases of the API. ### Simple Upload The easiest and simplest way to get started is to use POST /documents : it will make a synchronous upload of your file and wait for the result. This is a simplified version of POST /documents/{inbox_id} with less arguments and settings; it may not be suitable for real workload as it offers less capabilities. ### Upload to Inbox The favored endpoint to upload files is POST /documents/{inbox_id}: it is also highly recommended to make async call using sync=false. **Sync / Async** For convenience uploads can be synchronous: it will make the request blocks until the document is processed. It is however discouraged to rely on sync requests, as our service is designed to process documents asynchronously. You might run into timeouts and unprocessed document depending on factors such as server load and number of pending documents. Asynchronous calls will only schedule the processing and directly return the document ID without waiting: the document will be processed as soon as possible. You can then wait for the processed result using GET */documents/{document_id}*. ### Reprocessing You can reprocess a d

## Identity

- **Record id**: `dea:platform-service-contract-p-fit-z2mtys`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: contract-p.fit; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
