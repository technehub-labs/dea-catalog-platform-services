# SearchLy API v1 (asuarez.dev:searchly)

> # Introduction The SearchLy API provides similarity searching based on song lyrics. # Operations The API allows for the `/similarity/by_song` operation, which allows clients to search the similarity for an existing song in the database. Also, the API has an additional `/similarity/by_content` endpoint which allows clients to search similarity given a free String input through a JSON request body. Additional `/song/search` operation is available for searching songs given a query String. # Endpoint The API endpoint for the SearchLy API v1 is as follows: ``` https://searchly.asuarez.dev/api/v1 ``` # Motivation This project was built in order to create an API for searching similarities based on song lyrics. There are a lot of songs in the industry and most of them are talking about the same topic. What I wanted to prove with SearchLy was to estimate how similar are two songs between them based on the meaning of their lyrics. SearchLy is using a database of 100k songs from AZLyrics, using [this scraper](https://github.com/AlbertSuarez/azlyrics-scraper), which is being updated periodically. Then, using word2vec and NMSLIB, it was possible to create an index where you can search similarities using the k-nearest neighbors (KNN) algorithm. > **Note**: I am currently using a micro-instance from DigitalOcean where the API is deployed, so you should expect a bad performance. However, if this API becomes popular I will deploy it in a bigger instance.

## Identity

- **Record id**: `dea:platform-service-asuarez-dev-searchly-ufcrny`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: asuarez.dev:searchly; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
