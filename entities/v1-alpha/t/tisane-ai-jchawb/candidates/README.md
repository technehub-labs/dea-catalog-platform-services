# Tisane API Documentation (tisane.ai)

> Tisane is a natural language processing library, providing: * standard NLP functionality * special functions for detection of problematic or abusive content * low-level NLP like morphological analysis and tokenization of no-space languages (Chinese, Japanese, Thai) Tisane has monolithic architecture. All the functions are exposed using the same language models and the same analysis process invoked using the [POST /parse](#561264c5-6dbe-4bde-aba3-7defe837989f) method. Other methods in the API are either wrappers based on the process, helper methods, or allow inspection of the language models. The current section of the documentation describes the two structures used in the parsing & transformation methods. # Getting Started This guide describes how to setup your Tisane account. The steps you need to complete are as follows: * Step 1 – Create an Account * Step 2 – Save Your API Key * Step 3 – Integrate the API ## Step 1 – Create an Account Navigate to [Sign up to Tisane API](https://tisane.ai/signup/). The free Community Plan allows up to 50,000 requests but comes with a limitation of 10 requests per minute. ## Step 2 - Save Your API Key You will need the API key to make requests. Open your [Developer Profile](https://tisane.ai/developer/) to find your API keys. ## Step 3 - Integrate with the API In summary, the POST /parse method has 3 attributes: *content*, *language*, and *settings*. All 3 attributes are mandatory. For example: `{"language": "en", "content": "hello", "settings": {}}` Read on for more info on the [response](#response-reference) and the [settings](#settings-reference) specs. The method doc pages contain snippets of code for your favorite languages and platforms. # Response Reference The response of the [POST /parse](#561264c5-6dbe-4bde-aba3-7defe837989f) method contains several sections displayed or hidden according to the [settings](#settings-reference) provided. The common attributes are: * `text` (string) - the original input * `reduced_output` (b

## Identity

- **Record id**: `dea:platform-service-tisane-ai-jchawb`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: tisane.ai; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
