# Reports API (nexmo.com:reports)

> The [Reports API](/reports/overview) enables you to request a report of activity for your Vonage account. Depending on your query pattern, you can choose from one of the two versions of the Reports API: asynchronous and synchronous. The asynchronous version is optimized for infrequent and large data queries (from several records to tens of millions). The synchronous version is optimized for frequent and periodic retrievals of small batches of data records (from one record to tens of thousand per query). Only synchronous version supports retrival of data records by message/record ID. Vonage recommends that you limit asynchronous queries to a maximum of 20 million records, by setting the start and end dates accordingly. On average, the asynchronous Reports API takes 5 - 10 minutes to generate 1 million records.

## Identity

- **Record id**: `dea:platform-service-nexmo-com-reports-xxcab2`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: nexmo.com:reports; spec: https://developer.nexmo.com/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
