# GeoDB Cities API (mashape.com:geodb)

> The GeoDB API focuses on getting global city and region data. Easily obtain country, region, and city data for use in your apps! <ul> <li>Filter cities by name prefix, country, location, time-zone, and even minimum population.</li> <li>Sort cities by name, country code, elevation, and population - or any combination of these.</li> <li>Get all country regions.</li> <li>Get all cities in a given region.</li> <li> Display results in multiple languages.</li> <li>RESTful API adheres to industry best-practices, including HATEOAS-style links to facilitate paging results. </li> <li>Backed by cloud-based load-balanced infrastructure for resiliency and performance!</li> <li>Data is periodically refreshed from GeoNames and WikiData.</li> </ul> <p>Notes: <ul> <li> Since the database is periodically updated, this may <strong>very rarely</strong> result in certain cities being marked deleted (e.g., duplicates removed). By default, endpoints returning city data will exclude cities marked deleted. However, in the unlikely event that this occurs while your app is paging through a set of affected results - and you care about the paged results suddenly changing underneath - specify <tt>includeDeleted=SINCE_YESTERDAY</tt> (or <tt>SINCE_LAST_WEEK</tt> if you're really paranoid!). </li> </ul> <hr/> <h3>Useful Resources</h3> <ul> <li> SDKs <ul> <li> <a href='https://www.npmjs.com/package/wft-geodb-angular-client'>Angular</a>, <a href='https://github.com/wirefreethought/geodb-sample-angular-app'>Sample App</a> </li> <li><a href='https://github.com/wirefreethought/geodb-java-client'>Java</a></li> <li><a href='https://www.npmjs.com/package/wft-geodb-js-client'>JavaScript</a></li> </ul> <li><a href='swagger.json'>Swagger Docs</a></li> <li><a href='http://creativecommons.org/licenses/by/3.0/'>Usage License</a></li> </li> </ul>

## Identity

- **Record id**: `dea:platform-service-mashape-com-geodb-hve77b`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: mashape.com:geodb; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
