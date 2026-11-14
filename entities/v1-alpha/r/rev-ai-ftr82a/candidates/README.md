# Asynchronous Speech-To-Text API Documentation (rev.ai)

> Rev.ai provides quality speech-text recognition via a RESTful API. All public methods and objects are documented here for developer reference. For a real-time speech to text solution, use Rev.ai's [Streaming API](/docs/streaming). # Base Endpoint The base url for this version of the API is > `https://api.rev.ai/speechtotext/v1` All endpoints described in this documentation are relative to this base url. # Quick Start Follow the [getting started checklist](https://www.rev.ai/getting_started) ## Get your Access Token You can generate your [access token](#section/Authentication/Access-Token) on the [settings page](https://www.rev.ai/access_token) of your account. This access token only needs to be generated once and never expires. You can re-generate your token, however this will invalidate the previous token. ## Submit a File To submit an audio file for transcription to Rev.ai: ``` curl -X POST "https://api.rev.ai/speechtotext/v1/jobs" -H "Authorization: Bearer $REV_ACCESS_TOKEN" -H "Content-Type: application/json" -d "{\"media_url\":\"https://www.rev.ai/FTC_Sample_1.mp3\",\"metadata\":\"This is a sample submit jobs option\"}" ``` You’ll receive a response like this: ~~~ { "id": "Umx5c6F7pH7r", "created_on": "2018-09-15T05:14:38.13", "name": "sample.mp3", "metadata": "This is a sample submit jobs option for multipart", "status": "in_progress" } ~~~ The `id` (in this case `Umx5c6F7pH7r`) will allow you to retrieve your transcript. ## Get Your Transcript Once a transcription job's `status` becomes `transcribed`, you can retrieve the transcript in JSON format by running: ``` curl -X GET "https://api.rev.ai/speechtotext/v1/jobs/{id}/transcript" -H "Authorization: Bearer $REV_ACCESS_TOKEN" -H "Accept: application/vnd.rev.transcript.v1.0+json" ``` Alternatively you can get the plain text version by running: ``` curl -X GET "https://api.rev.ai/speechtotext/v1/jobs/{id}/transcript" -H "Authorization: Bearer $REV_ACCESS_TOKEN" -H "Accept: text/plain" ``` You can poll for the `

## Identity

- **Record id**: `dea:platform-service-rev-ai-ftr82a`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: rev.ai; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
