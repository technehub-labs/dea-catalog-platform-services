# CR-ISS-CAT-08: Shard Subdivision (R5 Remedy — Two-Level Shards)

**Status**: Landed (this PR)
**Layer**: Catalog tooling (storage layout)
**Owner**: Emmanuel A. Otchere
**Date**: 2026-11-15
**Admission authority**: layout only (no record changes)
**Trigger**: Catalog population programme. The weekly reconciler (R5) flagged the over-cap shard directory created by this programme's ISS corpus (`contributions/queue/a` and `entities/v1-alpha/a` at 1,235 entries each — the APIs.guru slugs cluster on 'a') — remedy per entity-storage-layout.md §4 and the CR-MET-024/metrics subdivide recipe.
**Carrier**: Single PR on feature branch `feat/cr-iss-cat-08`. PR review, not direct push.

## 1. What this CR does

1. **Subdivides the over-cap shard into two-character sub-shards** (2,470 entries moved; every resulting directory well under the 800-entry cap).
2. **Upgrades the vendored toolchain to depth-3 shard walking**: `regenerate_catalog.py` (shard descent + relative-path rel-dir), `check_catalog_index.py` (shard descent), `check_contributions.py` (rglob queue walk); shard-name test accepts 1–2 character alnum shards (digits included).
3. `CATALOG.yaml` regenerated: `candidates: 2525`, `canonical: 500` (the pre-existing owner PlatformService records) — both unchanged; ids untouched.

## 2. Verification

- All gates green locally (parse/pointer/posture/queue/schema/documentation/index `--strict`/`regen --check`).
- R5 post-merge: the two over-cap findings for this repo are gone.

## 3. NOT-List

- No record content changes; no ids change; no canonical admissions.
- No gate-semantics changes beyond the depth-3 shard walk.
