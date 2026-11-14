# DVP Data API (docker.com:dvp)

> The Docker DVP Data API allows [Docker Verified Publishers](https://docs.docker.com/docker-hub/publish/) to view image pull analytics data for their namespaces. Analytics data can be retrieved as raw data, or in a summary format. #### Summary data In your summary data CSV, you will have access to the data points listed below. You can request summary data for a complete week (Monday through Sunday) or for a complete month (available on the first day of the following month). There are two levels of summary data: - Repository-level, a summary of every namespace and repository - Tag- or digest-level, a summary of every namespace, repository, and reference (tag or digest) The summary data formats contain the following data points: - Unique IP address count - Pulls by tag count - Pulls by digest count - Version check count #### Raw data In your raw data CSV you will have access to the data points listed below. You can request raw data for a complete week (Monday through Sunday) or for a complete month (available on the first day of the following month). **Note:** each action is represented as a single row. - Type (industry) - Host (cloud provider) - Country (geolocation) - Timestamp - Namespace - Repository - Reference (digest is always included, tag is provided when available) - HTTP request method - Action, one of the following: - Pull by tag - Pull by digest - Version check - User-Agent

## Identity

- **Record id**: `dea:platform-service-docker-com-dvp-5nn8h5`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: docker.com:dvp; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
