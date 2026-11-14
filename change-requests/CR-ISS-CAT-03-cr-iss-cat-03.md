# CR-CR-ISS-CAT-03: InformationSystemService Candidate Corpus

**Status**: Landed (this PR)

**Naming/numbering correction**: this CR landed as `ISS-CAT-03` without the house `CR-` prefix (driver defect, fixed in the programme tooling). Renamed to `CR-ISS-CAT-03` by the naming-correction CR (CR-ISS-CAT-07); content unchanged.
**Layer**: Catalog content (candidate corpus intake)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-15
**Admission authority**: candidate corpus only (canonical admission remains the evidence-gated step; FOUNDATIONS D-4/D-5)
**Trigger**: Catalog population programme (2026-11 owner directive): advance 10 foundational skeleton catalogs with evidence-backed candidate corpora (>=1,000 each) through a gated intake workflow. Platform-services is sixth: the APIs.guru public API directory (2,500+ catalogued public APIs) is the candidate seed source named per FOUNDATIONS §7; each catalogued API is an InformationSystemService candidate.
**Carrier**: Single PR on feature branch `feat/iss-cat-03`. PR review, not direct push.
**Lands against**: `main`
**Depends on**: ISS-CAT-02 (ingestion groundwork).

## 1. What this CR lands

**2525 InformationSystemService candidate submissions** in `contributions/queue/<shard>/<slug>.yaml` from 1 evidence bank(s):

| Bank | Source | Records |
|---|---|---|
| apis-guru.json | APIs.guru public API directory (v2 list API) | 2525 |

Provenance in `ingestion/manifest.yaml` (bank sha256s, source URLs, retrieval dates, mapping note). Every submission carries `source_ref`, a `published-document` evidence citation, and published description prose. Provisional field mappings are documented per record and in the manifest; per-organization values are canonical-admission decisions.


## 2. What changes

- `contributions/queue/<shard>/` — 2525 intake submissions (`status: queued`)
- `ingestion/manifest.yaml` — corpus provenance record (new)
- No `CATALOG.yaml` change (queue ≠ index)
- This CR file and the index row

## 3. Verification

- `check_contributions.py`: CONFORMANT (2525 queue files)
- No directory holds 800+ entries (slug-prefix distribution)
- Spot-checks: records trace to their published source identifiers

## 4. NOT-List

- NOT record admission (nothing under `entities/` changes; admission follows in ISS-CAT-04+).
- NOT a modification of gates, schemas, or intake tooling.
- NOT an authoritative assessment of provisional mapped values.

## 5. Acceptance criteria

1. 2525 gate-CONFORMANT submissions; manifest carries bank sha256s + source URLs.
2. Submissions carry no `id`; `status: queued`; `submitted_by: Emmanuel A. Otchere`.
3. `CATALOG.yaml` counts unchanged.
