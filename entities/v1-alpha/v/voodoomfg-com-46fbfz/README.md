# Voodoo Manufacturing 3D Print API (voodoomfg.com)

> Welcome to the Voodoo Manufacturing API docs! Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the "api_key" header of the request. <a href="https://voodoomfg.com/3d-print-api#get-access" target="_blank">You can request a key here.</a> This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows: - Get a list of the available materials with the /materials endpoint - Upload models to the API with the /models endpoint - Get quotes for shipping methods with the /order/shipping endpoint - Get a quote for an order with the /order/create endpoint - Confirm the order with the /order/confirm endpoint Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively. In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you've already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints.

## Identity

- **Record id**: `dea:platform-service-voodoomfg-com-46fbfz`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: voodoomfg.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
