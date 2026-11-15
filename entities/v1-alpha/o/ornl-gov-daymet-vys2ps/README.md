# Daymet Single Pixel Extraction Tool API (ornl.gov:daymet)

> Welcome to the Daymet Single Pixel Extraction Tool API. You can use this API to download daily surface data within the Daymet database in a `csv` or `json` format for a single point. This API allows users to query a single geographic point by latitude and longitude in decimal degrees. A routine is executed that translates the (lon, lat) coordinates into projected Daymet (x,y) Lambert Conformal Coordinates. These coordinates are used to access the Daymet database of daily interpolated surface weather variables. Daily data from the nearest 1 km x 1 km Daymet grid cell are extracted from the database. If you would like to learn how to automate the download of multiple locations for the Daymet Single Pixel Extraction Tool, click [here](https://github.com/ornldaac/daymet-single-pixel-batch).

## Identity

- **Record id**: `dea:platform-service-ornl-gov-daymet-vys2ps`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: ornl.gov:daymet; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
