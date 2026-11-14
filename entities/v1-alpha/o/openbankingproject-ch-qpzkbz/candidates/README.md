# Swiss NextGen Banking API-Framework (openbankingproject.ch)

> # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data. The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples. The possible Approaches are: * Redirect SCA Approach * *(Not recommended by obp.ch community) OAuth SCA Approach* * *(Not recommended by obp.ch community) Decoupled SCA Approach* * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method* * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available* * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method* Not every message defined in this API definition is necessary for all approaches. Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional Therefore for a particular implementation of a compliant API it is only necessary to support a certain subset of the methods defined in this API definition. **Please have a look at the implementation guidelines if you are not sure which message has to be used for the approach you are going to use.** ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).** It is not a replacement in any sen

## Identity

- **Record id**: `dea:platform-service-openbankingproject-ch-qpzkbz`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: openbankingproject.ch; spec: https://www.openbankingproject.ch)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
