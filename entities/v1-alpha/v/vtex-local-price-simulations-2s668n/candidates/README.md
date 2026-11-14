# Price Simulations API (vtex.local:Price-Simulations)

> > Check the new [Pricing onboarding guide](https://developers.vtex.com/docs/guides/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer's journey The Price Simulations API allows you to configure custom price selectors for B2B stores, based on the context set by the [Orders Configuration app](https://developers.vtex.com/docs/guides/vtex-order-configuration). ## Custom Prices In this section, you can create a specific shopping scenario with the criteria you want. For explaining purpose, we used the `orderType` and `state` as default values, but it can be others too. `GET` [Get custom prices schema](https://developers.vtex.com/docs/api-reference/price-simulations#get-/_v/custom-prices/session/schema) `POST` [Create or Update custom prices schema](https://developers.vtex.com/docs/api-reference/price-simulations#post-/_v/custom-prices/session/schema) ## Session Management Every time you edit a configuration value set on the Custom Prices session, you must use this endpoint to update the Order Configuration. `POST` [Update Order Configuration](https://developers.vtex.com/docs/api-reference/price-simulations#post-/sessions/) ## Price Association Use these routes to associate a shopping scenario, created at the Custom Price session, to a specific price table. `GET` [Get price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#get-/_v/custom-prices/rules/-priceAssociationId-) `POST` [Create price association](https://developers.vtex.com/docs/api-reference/price-simulations#post-/_v/custom-prices/rules) `PUT` [Update price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#put-/_v/custom-prices/rules/-priceAssociationId-) `DELETE` [Disassociate price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#delete-/_v/custo

## Identity

- **Record id**: `dea:platform-service-vtex-local-price-simulations-2s668n`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: vtex.local:Price-Simulations; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
