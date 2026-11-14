# HERE Network Positioning API v2 (here.com:positioning)

> Positioning API accepts requests with radio network measurements and replies with corresponding location estimate. For more details and examples, see [Developer's Guide](https://developer.here.com/documentation/positioning). Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org. Breaking changes from v1: - JSON fields `altaccuracy`, `baselat`, `baselng`, `cellparams`, `pilotpower`, `pnoffset`, `powrx`, `rxlevel`, have been deprecated and replaced with `altAccuracy`, `baseLat`, `baseLng`, `cellParams`, `pilotPower`, `pnOffset`, `rss`, `rxLevel` respectively. - Dependent parameters combined as a subobject. - CDMA, GSM, WCDMA, TD-SCDMA and LTE local identification parameters for serving cell moved under `localId` property. - GSM neighbor global ID: `lac` and `cid` for neighbor cell moved under `globalIdentity` property.

## Identity

- **Record id**: `dea:platform-service-here-com-positioning-r89ba6`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: here.com:positioning; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
