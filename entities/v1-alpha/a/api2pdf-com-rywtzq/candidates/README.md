# Api2Pdf - PDF Generation, Powered by AWS Lambda (api2pdf.com)

> # Introduction [Api2Pdf](https://www.api2pdf.com) is a powerful PDF generation API with no rate limits or file size constraints. Api2Pdf runs on AWS Lambda, a serverless architecture powered by Amazon to scale to millions of requests while being up to 90% cheaper than alternatives. **Supports wkhtmltopdf, Headless Chrome, LibreOffice, and PDF Merge.** You can also generate barcodes with ZXING (Zebra Crossing). # SDKs & Client Libraries We've made a number of open source libraries available for the API - Python: [https://github.com/api2pdf/api2pdf.python](https://github.com/api2pdf/api2pdf.python) - .NET: [https://github.com/api2pdf/api2pdf.dotnet](https://github.com/api2pdf/api2pdf.dotnet) - Nodejs: [https://github.com/api2pdf/api2pdf.node](https://github.com/api2pdf/api2pdf.node) - PHP: [https://github.com/Api2Pdf/api2pdf.php](https://github.com/Api2Pdf/api2pdf.php) - Ruby: (Coming soon) # Authorization Create an account at [portal.api2pdf.com](https://portal.api2pdf.com/register) to get an API key. **Authorize your API calls** - GET requests, include apikey=YOUR-API-KEY as a query string parameter - POST requests, add **Authorization** to your header. ``` Authorization: YOUR-API-KEY ``` # Quickstart If you are looking for just a quick call to grab PDFs of a URL, you can do a GET request like: ``` https://v2018.api2pdf.com/chrome/url?url={UrlToConvert}&apikey={YourApiKey} ``` For more advanced usage and settings, see the API specification below.

## Identity

- **Record id**: `dea:platform-service-api2pdf-com-rywtzq`
- **Type**: PlatformService
- **Version**: 0.1.0
- **Lifecycle**: proposed (candidate corpus; admitted via the gated intake
  workflow; canonical admission is a separate evidence-gated step)

## Evidence

Cited from the APIs.guru public API directory (list API). The API specification is published and machine-verifiable via the cited listing/spec URL. No service-level operational fields are asserted at candidate state.

- kind: `published-document` — reference: https://apis.guru/browse-apis/ (APIs.guru listing: api2pdf.com; spec: https://apis.guru/)

## Classification-or-relationships

Deferred: relationship assertions are not made at candidate admission;
bindings land at canonical admission with per-assertion evidence.

## Provenance

Ladder passage: candidate (2026-11-14, Emmanuel A. Otchere).

## Governance

Functional owner: Emmanuel A. Otchere. Steward: Emmanuel A. Otchere. Approval: proposed
(candidate corpus; the approval decision belongs to canonical admission).
