# Adyen Recurring API (adyen.com:RecurringService)

> The Recurring APIs allow you to manage and remove your tokens or saved payment details. Tokens should be created with validation during a payment request. For more information, refer to our [Tokenization documentation](https://docs.adyen.com/online-payments/tokenization). ## Authentication You need an [API credential](https://docs.adyen.com/development-resources/api-credentials) to authenticate to the API. If using an API key, add an `X-API-Key` header with the API key as the value, for example: ``` curl -H "Content-Type: application/json" \ -H "X-API-Key: YOUR_API_KEY" \ ... ``` Alternatively, you can use the username and password to connect to the API using basic authentication, for example: ``` curl -U "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \ -H "Content-Type: application/json" \ ... ``` ## Versioning Recurring API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number. For example: ``` https://pal-test.adyen.com/pal/servlet/Recurring/v68/disable ``` ## Going live To authenticate to the live endpoints, you need an [API credential](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area. The live endpoint URLs contain a prefix which is unique to your company account: ``` https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Recurring/v68/disable ``` Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**.

## Identity

- **Record id**: `dea:platform-service-adyen-com-recurringservice-6nsdw4`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: adyen.com:RecurringService; spec: https://www.adyen.help/hc/en-us/community/topics)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
