# Pricing API (vtex.local:Pricing-API)

> > Check the new [Pricing onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer's journey. Pricing is the VTEX module responsible for the SKU's price list. At this module we have the base price of each SKU, some optional fixed prices by trade policy, and some rules that can be applied to generate dynamically different final prices according to the purchase context and the trade policy. The variables used in this collection are: * **{{accountName}}** = You VTEX account name. * **{{tradePolicyId}}** = Current Trade Policy ID. * **{{itemId}}** = SKU ID. * **{{X-VTEX-API-AppKey}}** and **{{X-VTEX-API-AppToken}}** = Credentials. You can get more information about how to use this module and its business logic at [VTEX Help](http://help.vtex.com). ## Rate Limits ### Limits per route - `GET`: routes are not rate limited at the moment - `PUT or POST`: `40 requests/second/account` in any **price insert/update route** with 1000 *Burst Credits* - `DELETE`: `16 requests/second/account` in any **price deletion route**, with 300 *Burst Credits*. ### What are Burst Credits? In case the account exceeds the limit frequency for a `Rate Limiter` (for instance, when one account makes `41 requests/second` in any `price insert/update route`), we decrease from the *Burst Credit* count the exceeding (in this example, *1 Credit*). In the event of the *Burst Credits* reaching **0 (zero)**, the request is blocked with a `Status 429` response. The credits fill up over time when the route is not being used, in the same rate as the route's `Rate Limiter`. In our example, for each second not sending a **PUT or POST request**, we increase *40 Burst Credits* to this `Rate Limiter` ### New Response Headers In the response headers of any request to Pricing v2 there are some new

## Identity

- **Record id**: `dea:platform-service-vtex-local-pricing-api-vryjwh`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: vtex.local:Pricing-API; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
