# Account and Transaction API Specification - UK (nbg.gr)

> ## Functionality at a glance The NBG "UK OPB - Account and Transaction v3.1.5" API follows the [UK Open Banking Specification v3.1.5](https://openbankinguk.github.io/read-write-api-site3/v3.1.5/profiles/account-and-transaction-api-profile.html) This Account and Transaction API Specification describes the flows and payloads for retrieving a list of accounts and their transactions. The API endpoints described here allow a AISP to: * Create the Consent with the appropriate permissions in order to be able to access the API Endpoints * Retrieve the list of accounts * Retrieve an account's details * Retrieve an account's balances * Retrieve an account's transactions * Retrieve an account's beneficiaries * Retrieve an account's standing orders * Retrieve an account's party * Retrieve an account's scheduled payments * Retrieve an account's statements ## Quick Getting Started 1. **Login/Register** to the NBG Technology HUB 2. Go to **"APPS"** 3. Select your Organization and go to step 4. If you want to create a new Organization click **\"CREATE AN ORGANIZATION\"** and follow the steps below: 1. Enter the title of your Organization 2. Enter a short description of your Organization (optional) 3. Click **"SUBMIT"** 4. Select the Organization of choice and click **"ADD AN APPLICATION"** 1. Fill in the forms (title and short description) 2. Check **\"Authorization Code\" and \"Client Credentials\"** 3. Enter the **OAuth Redirect and Post Logout URIs** (these are the URIs that we will redirect the user upon logging in and logging out respectively) You can use the following redirect URL to easily test the API through the portal: *https://developer.nbg.gr/oauth2/redoc-callback* 4. Click **"SUBMIT"** 5. Store the APPs **"Client ID"** and **"Client Secret"** 5. Go to **"API PRODUCTS"** and select the **ACCOUNT INFORMATION - UK OPEN BANKING API** 6. Click **\"START USING THIS API\"**, choose your app and click **"SUBSCRIBE"** 7. Get an Access Token using the Access Token Flow and the A

## Identity

- **Record id**: `dea:platform-service-nbg-gr-sxs3ch`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: nbg.gr; spec: https://developer.nbg.gr/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
