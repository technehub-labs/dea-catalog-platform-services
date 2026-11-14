# U.S. EPA Enforcement and Compliance History Online (ECHO) - Effluent Charting and Reporting (epa.gov:eff)

> Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA's Office of Enforcement and Compliance Assurance for public use. ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide. EFF Rest Services provides the data for ECHO's Effluent Charts, a set of dynamic charts and tables of permitted effluent limits, releases, and violations over time for Clean Water Act (CWA) wastewater discharge permits issued under the National Pollutant Discharge Elimination System (NPDES). See Effluent Charts Help (https://echo.epa.gov/help/reports/effluent-charts-help) for additional information. \ The are 3 service end points for Effluent Charts: get_summary_chart, get_effluent_chart, and download_effluent_chart. \ <b>1)</b> Use get_summary_chart to retrieve a summary matrix of effluent parameters by effluent outfall and an overall violation status for a provided NPDES Permit and date range. <b>2)</b> Use get_effluent_chart to retrieve detailed Discharge Limit, DMR and NPDES Violation information for a provided NPDES Permit, date range, effluent parameter, or outfall. <b>3)</b> Use download_effluent_chart to generate a Comma Separated Value (CSV) file of the detailed data provided with get_effluent chart, for a provided NPDES Permit, date range, effluent parameter, or outfall. \ Additional ECHO Resources: <a href="https://echo.epa.gov/tools/web-services">Web Services</a>, <a href="https://echo.epa.gov/resources/echo-data/about-the-data">About ECHO's Data</a>, <a href="https://echo.epa.gov/tools/data-downloads">Data Downloads</a>

## Identity

- **Record id**: `dea:platform-service-epa-gov-eff-4f3p3r`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: epa.gov:eff; spec: https://echo.epa.gov/resources/general-info/contact-us)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
