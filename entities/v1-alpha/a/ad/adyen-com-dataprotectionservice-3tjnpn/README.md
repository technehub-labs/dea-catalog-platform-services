# Adyen Data Protection API (adyen.com:DataProtectionService)

> Adyen Data Protection API provides a way for you to process [Subject Erasure Requests](https://gdpr-info.eu/art-17-gdpr/) as mandated in GDPR. Use our API to submit a request to delete shopper's data, including payment details and other related information (for example, delivery address or shopper email).## Authentication Each request to the Data Protection API must be signed with an API key. Get your API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the `X-API-Key` header value, for example: ``` curl -H "Content-Type: application/json" \ -H "X-API-Key: Your_API_key" \ ... ``` Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints). ## Versioning Data Protection Service API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number. For example: ``` https://ca-test.adyen.com/ca/services/DataProtectionService/v1/requestSubjectErasure ```

## Identity

- **Record id**: `dea:platform-service-adyen-com-dataprotectionservice-3tjnpn`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: adyen.com:DataProtectionService; spec: https://www.adyen.help/hc/en-us/community/topics)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
