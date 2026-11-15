# Shorten.REST API Documentation (shorten.rest)

> ## Introduction The Shorten.rest API allows you to programmatically create short URLs (an &apos;alias&apos;) for longer URL (a &apos;destination&apos;). Each alias you create can be used to redirect the end user (person clicking on the link) to one or more destination URLs A default destination is always set and specific destinations can be set to redirect the end user to preferred destinations based on the user&apos;s geographical location (country) and device Operating System. In order to use the Shorten.Rest URL Shortening API you can choose to bind your own branded domain, sub-domain or to use our default domain - Short.FYI ### Destination Matching When creating or editing a short URL (&apos;alias&apos;) you can choose to specify a destination for each country and OS ([Supported OSes list](#tag/OperatingSystems)) combination. When a user clicks on the short link, Shorten.rest will examine the end user's country (determined by User's IP) and OS (User agent) and match the most suitable destination for each user. (*) If no destination is set for a specific request combination Shorten.rest will use the default destination that exists within each short URL (**) BRANDED DOMAINS: If the requested alias does not exist in our database - Shorten.rest will redirect the user to the default fallback you set within your dashboard under the ‘Alias Not Found Page Url’ value for a custom domain. (***) Operating System (OS) destinations are stronger than a country destination! For example - if you have a custom landing page that is targeting people in the USA and a second landing page that is hyper focused for people who use iOS devices - a person clicking on your link in the USA that is on an iPhone will be redirected to the iOS landing page, while all other devices will be redirected to the USA landing page. | OS | Country | Destination | | :------------: |:---------------:| -----| | iOS | | YourDestination.com/ios | | | US | YourDestination.com/usa | Shorten.rest will choose t

## Identity

- **Record id**: `dea:platform-service-shorten-rest-w9vq97`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: shorten.rest; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
