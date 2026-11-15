# SEDRA IV API (bethmardutho.org)

> The SEDRA API is documented in **OpenAPI format** and uses [ReDoc](https://github.com/Rebilly/ReDoc) for documentation. # Introduction This document describes the JSON API for the Syriac Electronic Data Research Archive (SEDRA). The SEDRA project is a linguistic and literary database of Syriac language and literature focusing on providing electronic access to the corpus of Syriac lexicons with linguistic information added to each entry in those lexicons. The API is a mechanism to provide the linguistic information stored in SEDRA to a broader audience. Additionally there is a XML API for Syriac words which conforms to a prototype Semitic Languages schema which can be found in the XSD file https://sedra.bethmardutho.org/api/semiticLanguages.xsd. # Cross-Origin Resource Sharing This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with the [W3C spec](https://www.w3.org/TR/cors/) and allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site. # Samples Explaining how to lookup words in the SEDRA API is complex and would clutter the API description. For that reason we have chosen to give the explanation of how to lookup words in its own section. SEDRA can lookup words by the SEDRA word Id. However, it will often be the case that the consumer of information provided by the SEDRA API does not know the SEDRA word Id. It is for that reason that the SEDRA API provides a method to lookup words by the Syriac text. But that process is complicated by the nature of Syriac writing. So the SEDRA API will lookup words for consonantal, partially vocalized, and fully vocalized Syriac text. Using the word Id will provide the most accurate results as the exact word will be returned. Fully vocalized text will provide the next most accurate result. The least accurate results will be returned by partially vocalized and consonantal Syria

## Identity

- **Record id**: `dea:platform-service-bethmardutho-org-qw4vsy`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: bethmardutho.org; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
