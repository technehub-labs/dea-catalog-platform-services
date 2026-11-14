# VA Facilities (va.gov:facilities)

> ## Background This RESTful API provides information about physical VA facilities. Information available includes geographic location, address, phone, hours of operation, and available services. VA operates several different types of facilities, the types represented in this API include: - Health Facilities (vha) - Benefits Facilities (vba) - Cemeteries (nca) - Vet Centers (vc) To read an FAQ on how wait times are calculated, click the "For more information" link on [this page](https://www.accesstocare.va.gov/PWT/SearchWaitTimes). ## Getting Started ### Base URLs The base URLs for the VA Facilities API in the various environments are: - Sandbox: `https://sandbox-api.va.gov/services/va_facilities/v0` - Production: `https://api.va.gov/services/va_facilities/v0` ### Authorization API requests are authorized through a symmetric API token, provided in an HTTP header with name `apikey`. ### Response Formats Clients may request several response formats by setting the `Accept` header. - `application/json` - The default JSON response format complies with JSON API. This media type is *not* available for bulk requests using the `/facilities/all` endpoint. It will return `406 Not Acceptable`. - `application/geo+json` - GeoJSON-compliant format, representing each facility as a feature with a point geometry. - `application/vnd.geo+json` - Deprecated. Prefer application/geo+json. - `text/csv` - Available for the bulk download operation only. Some structured fields are omitted from the CSV response. ### Response Elements Some data elements within the response are only present for facilities of a given type: - The patient satisfaction scores contained in the `satisfaction` element are only applicable to VA health facilities. - The patient wait time values contained in the `wait_times` element are only applicable to VA health facilities. - The list of available services in the `services` element is only applicable to VA health and benefits facilities. - The operational hours special i

## Identity

- **Record id**: `dea:platform-service-va-gov-facilities-qu5kgt`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: va.gov:facilities; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
