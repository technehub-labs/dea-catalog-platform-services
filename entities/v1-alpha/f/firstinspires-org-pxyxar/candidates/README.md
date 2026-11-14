# FRC Events (firstinspires.org)

> <html><head></head><body><h1 id="overview">Overview</h1> <p><em>FIRST</em>/FMS FRC Events API is a service to return relevant information about the <em>FIRST</em> Robotics Competition (FRC). Information is made available from events operating around the world.</p> <p>For FRC, information is made available by the Field Management System (FMS) server operating at each event site. The FMS will attempt to sync all data from the event to "the cloud" as long as internet is available at the venue. If internet is unavailable, or "goes down" during the event, the FMS will automatically sync all data from the time the system was offline as soon as the connection is restored. The API will provide data as soon as it has synced, and we do not add any artificial delays. If you are receiving "stale" data, it may be because of connectivity problems at the venue. We recommend you try again later, and post on the FIRST FMS TeamForge site if the problem persists. <em>(Note: FMS does not sync while a match is running, so data that has to do with a particular match should become available once the score has been revealed to the audience at the event.)</em></p> <h3 id="migration-and-program-notes">Migration and Program Notes:</h3> <p>Pay close attention to the addresses for calling the various endpoints- as well as the notes regarding endpoints with multiple possible responses (i.e. score details and rankings).</p> <h1 id="documentation-notes">Documentation Notes</h1> <p>All times are listed in the local time to the event venue. HTTP-date values will show their timezone.</p> <p>If you specify a parameter, but no value for that parameter, it will be ignored. For example, if you request <strong>URL?teamNumber=</strong> the <strong>teamNumber</strong> parameter would be ignored.</p> <p>We will continue to support the current version of the API plus one version older. Old APIs are depricated once a version "two times newer" is available, at minimum 6 months. For example, version 2.0 and 1.0

## Identity

- **Record id**: `dea:platform-service-firstinspires-org-pxyxar`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: firstinspires.org; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
