# Velo Payments APIs (velopayments.com)

> ## Terms and Definitions Throughout this document and the Velo platform the following terms are used: * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking. ## Overview The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution: * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference. ## API Considerations The Velo Payments API is REST based and uses the JSON format for requests and responses. Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details. Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } charac

## Identity

- **Record id**: `dea:platform-service-velopayments-com-zwbyvp`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: velopayments.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
