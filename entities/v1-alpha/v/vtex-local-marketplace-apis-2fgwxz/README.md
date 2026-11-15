# Marketplace API (vtex.local:Marketplace-APIs)

> The **Marketplace API** enables marketplaces and sellers hosted on VTEX to perform their collaborative operations. >⚠️ The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/guides/getting-started-authentication) for each non-VTEX seller that will use this API. ## Index ### Notification Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs. `POST` [Notify marketplace of price update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) `POST` [Notify marketplace of inventory update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory) ### Suggestions #### Get Suggestions Search and filter all suggestions using specific criteria. `GET` [Get all SKU Suggestions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions) `GET` [Get SKU Suggestion by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerSkuId-) #### Manage Suggestions Send or delete SKU suggestions from the seller to marketplace. `PUT` [Send SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerSkuId-) `DELETE` [Delete SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#delete-/suggestions/-sellerId-/-sellerSkuId-) #### Get Versions Search and filter all versions of suggestions, using specific criteria. `GET` [Get all versions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions) `GET` [Get version by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions/-version-) #### Match Received SKUs Match SKU sugge

## Identity

- **Record id**: `dea:platform-service-vtex-local-marketplace-apis-2fgwxz`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: vtex.local:Marketplace-APIs; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
