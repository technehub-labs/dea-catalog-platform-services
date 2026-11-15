# Item Feed Service (ebay.com:buy-feed)

> <span class="tablenote"><b>Note:</b> This is a <a href="https://developer.ebay.com/api-docs/static/versioning.html#limited " target="_blank"> <img src="/cms/img/docs/partners-api.svg" class="legend-icon partners-icon" title="Limited Release" alt="Limited Release" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href="api-docs/buy/static/buy-requirements.html" target="_blank">Buy APIs Requirements</a>.</span><br><br>The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. <p>In addition to the API, there is an open source <a href="https://github.com/eBay/FeedSDK " target="_blank">Feed SDK</a> written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.</p>

## Identity

- **Record id**: `dea:platform-service-ebay-com-buy-feed-7wgve7`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: ebay.com:buy-feed; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
