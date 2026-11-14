# BulkSMS JSON REST API (bulksms.com)

> ## Overview The JSON REST API allows you to submit and receive [BulkSMS](https://www.bulksms.com/) messages. You can also get access to past messages and see your account profile. The base URL to use for this service is `https://api.bulksms.com/v1`. The base URL cannot be used on its own; you must append a path that identifies an operation and you may have to specify some path parameters as well. [Click here](/developer/) to go to the main BulkSMS developer site. In order to give you an idea on how the API can be used, some JSON snippets are provided below. Have a look at the [messages section](#tag/Message) for more information. Probably the most simple example ``` { "to": "+27001234567", "body": "Hello World!" } ``` You can send unicode automatically using the `auto-unicode` query parameter. Alternatively, you can specify `UNICODE` for the `encoding` property in the request body. Please note: when `auto-unicode` is specified and the value of the `encoding` property is `UNICODE`, the message will always be sent as `UNICODE`. Here is an example that sets the `encoding` explicitly ``` { "to": "+27001234567", "body": "Dobrá práce! Jak se máš?", "encoding": "UNICODE" } ``` You can also specify a from number ``` { "from": "+27007654321", "to": "+27001234567", "body": "Hello World!" } ``` Similar to above, but repliable ``` { "from": { "type": "REPLIABLE" }, "to": "+27001234567", "body": "Hello World!" } ``` A message to a group called Everyone ``` { "to": { "type": "GROUP", "name": "Everyone" }, "body": "Hello World!" } ``` A message to multiple recipients ``` { "to": ["+27001234567", "+27002345678", "+27003456789"], "body": "Happy Holidays!" } ``` Sending more than one message in the same request ``` [ { "to": "+27001234567", "body": "Hello World!" }, { "to": "+27002345678", "body": "Hello Universe!" } ] ``` **The insecure base URL `http://api.bulksms.com/v1` is deprecated** and may in future result in a `301` redirect response, or insecure requests may be rejected out

## Identity

- **Record id**: `dea:platform-service-bulksms-com-rwxswm`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: bulksms.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
