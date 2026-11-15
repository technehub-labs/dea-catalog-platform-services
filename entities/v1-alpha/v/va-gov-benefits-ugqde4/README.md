# Benefits Intake (va.gov:benefits)

> The Benefits Intake API allows authorized third-party systems used by Veteran Service Organizations (VSOs), agencies, and Veterans to digitally submit VA benefits claim documents directly to the Veterans Benefits Administration's (VBA) claims intake process. This API handles documents related to the following benefit claim types: * Compensation * Pension/Survivors Benefits * Education * Fiduciary * Insurance * Veteran Readiness & Employment (VRE) * Board of Veteran Appeals (BVA) This API also provides submission status updates until documents are successfully established for VBA claim processing, eliminating the need for users to switch between systems to manually check whether documents have been successfully uploaded. ## Background This API provides a secure, efficient, and tracked alternative to mail or fax for VA benefit claim document submissions. Documents are uploaded directly to the VBA so they can be processed as quickly as possible. ## Technical overview The Benefits Intake API first provides an upload location and unique submission identifier, and then accepts a payload consisting of a document in PDF format, zero or more optional attachments in PDF format, and some JSON metadata. The metadata describes the document and attachments, and identifies the person for whom it is being submitted. This payload is encoded as binary multipart/form-data (not base64). The unique identifier supplied with the payload can subsequently be used to request the processing status of the uploaded document package. To avoid errors and processing delays, API consumers are encouraged to validate the `zipcode`,`fileNumber`, `veteranFirstName`, `veteranLastName` and `businessLine` fields before submission according to their description in the DocumentUploadMetadata model and use the 'businessLine' attribute for the most efficient processing. Additionally, please ensure no PDF user passwords are used in submitted PDFs. ### Attachment & file size limits There is no limit on the numb

## Identity

- **Record id**: `dea:platform-service-va-gov-benefits-ugqde4`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: va.gov:benefits; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
