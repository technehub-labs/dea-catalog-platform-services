# Geneea Natural Language Processing (geneea.com)

> <div class="api-description"> <h2>Authentication</h2> <p>For all calls, supply your API key. <a href="https://www.geneea.com/pricing">Sign up to <em>obtain the key</em></a>.</p> <p> Our API supports both <em>unencrypted (HTTP)</em> and <em>encrypted (HTTPS)</em> protocols. However, for security reasons, we strongly encourage using only the encrypted version. </p> <p>The API key should be supplied as either a request parameter <code>user_key</code> or in <code>Authorization</code> header.</p> <pre><code>Authorization: user_key &lt;YOUR_API_KEY&gt;</code></pre> <h2>API operations</h2> <p> All API operations can perform analysis on supplied raw text or on text extracted from a given URL. Optionally, one can supply additional information which can make the result more precise. An example of such information would be the language of text or a particular text extractor for URL resources. </p> <p>The supported types of analyses are:</p> <ul> <li><strong>lemmatization</strong> &longrightarrow; Finds out lemmata (basic forms) of all the words in the document. </li> <li><strong>correction</strong> &longrightarrow; Performs correction (diacritization) on all the words in the document. </li> <li><strong>topic detection</strong> &longrightarrow; Determines a topic of the document, e.g. finance or sports. </li> <li><strong>sentiment analysis</strong> &longrightarrow; Determines a sentiment of the document, i.e. how positive or negative the document is. </li> <li><strong>named entity recognition</strong> &longrightarrow; Finds named entities (like person, location, date etc.) mentioned the the document. </li> </ul> <h2>Encoding</h2> <p>The supplied text is expected to be in UTF-8 encoding, this is especially important for non-english texts.</p> <h2>Returned values</h2> <p>The API calls always return objects in serialized JSON format in UTF-8 encoding.</p> <p> If any error occurs, the HTTP response code will be in the range <code>4xx</code> (client-side error) or <code>5xx</code> (

## Identity

- **Record id**: `dea:platform-service-geneea-com-qxqmab`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: geneea.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
