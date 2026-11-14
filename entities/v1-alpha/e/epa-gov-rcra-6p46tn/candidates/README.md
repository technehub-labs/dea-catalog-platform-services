# U.S. EPA Enforcement and Compliance History Online (ECHO) - Resource Conservation and Recovery Act (epa.gov:rcra)

> Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA's Office of Enforcement and Compliance Assurance for public use. ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide. RCRA Rest Services provides multiple service endpoints, each with specific capabilities, to search and retrieve data on hazardous waste handlers/facilities regulated under the Resource Conservation and Recovery Act (RCRA). The returned results reflect data drawn from EPA's RCRAInfo database. \ The get_facilities, get_map, get_qid, and get_download end points are meant to be used together, while the enhanced get_facility_info end point is self contained. The get_facility_info end point returns either an array of state, county or zip clusters with summary statistics per cluster or an array of facilities. \ The recommended use scenario for get_facilities, get_qid, get_map, and get_downoad is: \ <b>1)</b> Use get_facilities to validate passed query parameters, obtain summary statistics and to obtain a query_id (QID). QIDs are time sensitive and will be valid for approximately 30 minutes. <b>2)</b> Use get_qid, with the returned QID, to paginate through arrays of facility results. <b>3)</b> Use get_map, with the returned QID, to zoom in/out and pan on the clustered and individual facility coordinates that meet the QID query criteria. <b>4)</b> Use get_download, with the returned QID, to generate a Comma Separated Value (CSV) file of facility information that meets the QID query criteria. \ \ Use the qcolumns parameter to customize your search results. Use the Metadata service endpoint for a list of available output objects, their Column Ids, and their definitions to help you build your customized output. \ Additional ECHO Resources: <a href="https://echo.epa.gov/tools/web-services">Web Services</a>, <a href="https://echo.epa.gov/resources/echo-data/about-the-data">About ECHO's Data</a>, <a href="https://

## Identity

- **Record id**: `dea:platform-service-epa-gov-rcra-6p46tn`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: epa.gov:rcra; spec: https://echo.epa.gov/resources/general-info/contact-us)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
