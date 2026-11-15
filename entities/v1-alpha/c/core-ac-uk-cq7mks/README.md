# CORE API v2 (core.ac.uk)

> <p style="text-align: justify;">You can use the CORE API to access the resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href="/contact">report them to us</a>.</p> <h2>Overview</h2> <p style="text-align: justify;">The API is organised by resource type. The resources are <b>articles</b>, <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore, each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p> <h2>Response format</h2> <p style="text-align: justify;">Response for each query contains two fields: <b>status</b> and <b>data</b>. In case of an error status, the data field is empty. The data field contains a single object in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or contains a list of objects, for example for search queries. In case of batch requests, the response is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields. For search queries the response contains an additional field <b>totalHits</b>, which is the total number of items which match the search criteria.</p> <h2>Search query syntax</h2> <p style="text-align: justify">Complex search queries can be used in all of the API search methods. The query can be a simple string or it can be built using terms and operators described in Elasticsearch <a href="http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax">documentation</a>. The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>, <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>, <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong> and <st

## Identity

- **Record id**: `dea:platform-service-core-ac-uk-cq7mks`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: core.ac.uk; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
