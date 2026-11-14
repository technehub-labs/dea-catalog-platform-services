# Veteran Confirmation (va.gov:confirmation)

> The Veteran Confirmation API allows you to confirm Veteran status for a given person. This can be useful for offering Veterans discounts or other benefits. The API will only return “Confirmed” or “Not Confirmed”. ## Quickstart Guide ### 1. Get Access Credentials Get started by filling out the form on the [Apply for VA Lighthouse Developer Access](https://developer.va.gov/apply) page. After submitting a request, you will receive your credentials for using the API in the Development environment, which allows you to try it out with mock data before moving to the Production environment. ### 2. Test the API In the endpoint documentation below, we've provided a curl command builder for trying out the API before implementation with your app. Use [Test User](https://github.com/department-of-veterans-affairs/vets-api-clients/blob/master/test_accounts/confirmation_test_accounts.md) attributes to populate the request body. ### 3. Build your app The base URI for the Veteran Confirmation API in the Sandbox environment is: https://sandbox-api.va.gov/services/veteran_confirmation/v0 In this environment, use attributes from the list of [Test Users](https://github.com/department-of-veterans-affairs/vets-api-clients/blob/master/test_accounts/confirmation_test_accounts.md). Only Test Users can return a `"confirmed"` response. Check out some of our [sample apps](https://github.com/department-of-veterans-affairs/vets-api-clients). Please visit our VA Lighthouse [Support portal](https://developer.va.gov/support) should you need further assistance. ### 4. Show us a demo and get access to the Production environment After building your app, we ask that you give us a demo before we set you up with production credentials. Please see the [Path to Production](https://developer.va.gov/go-live) page for more details. ## Authorization This API requires an API key in combination with identifiable information for the person being confirmed listed below. API requests are authorized through a symmetri

## Identity

- **Record id**: `dea:platform-service-va-gov-confirmation-cjwjn2`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: va.gov:confirmation; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
