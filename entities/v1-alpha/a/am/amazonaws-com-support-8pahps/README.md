# AWS Support (amazonaws.com:support)

> <fullname>Amazon Web Services Support</fullname> <p>The <i>Amazon Web Services Support API Reference</i> is intended for programmers who need detailed information about the Amazon Web Services Support operations and data types. You can use the API to manage your support cases programmatically. The Amazon Web Services Support API uses HTTP methods that return results in JSON format.</p> <note> <ul> <li> <p>You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. </p> </li> <li> <p>If you call the Amazon Web Services Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the <code>SubscriptionRequiredException</code> error message appears. For information about changing your support plan, see <a href="http://aws.amazon.com/premiumsupport/">Amazon Web Services Support</a>.</p> </li> </ul> </note> <p>You can also use the Amazon Web Services Support API to access features for <a href="http://aws.amazon.com/premiumsupport/trustedadvisor/">Trusted Advisor</a>. You can return a list of checks and their descriptions, get check results, specify checks to refresh, and get the refresh status of checks.</p> <p>You can manage your support cases with the following Amazon Web Services Support API operations:</p> <ul> <li> <p>The <a>CreateCase</a>, <a>DescribeCases</a>, <a>DescribeAttachment</a>, and <a>ResolveCase</a> operations create Amazon Web Services Support cases, retrieve information about cases, and resolve cases.</p> </li> <li> <p>The <a>DescribeCommunications</a>, <a>AddCommunicationToCase</a>, and <a>AddAttachmentsToSet</a> operations retrieve and add communications and attachments to Amazon Web Services Support cases.</p> </li> <li> <p>The <a>DescribeServices</a> and <a>DescribeSeverityLevels</a> operations return Amazon Web Service names, service codes, service categories, and problem severity levels. You use these values when you call the <a>CreateCase</a> op

## Identity

- **Record id**: `dea:platform-service-amazonaws-com-support-8pahps`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: amazonaws.com:support; spec: https://github.com/mermade/aws2openapi)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
