# CR-ISS-CAT-02: Platform Service Re-Point and Initial Population

| Field | Value |
|---|---|
| **CR** | CR-ISS-CAT-02 |
| **Title** | Platform service catalogue re-point and initial population (500 records) |
| **Status** | Landed (this PR) |
| **Layer** | Catalogue (L5) |
| **Programme** | Org-wide catalog advancement |
| **Repository** | `technehub-labs/dea-catalog-platform-services` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-12 |
| **Depends on** | CR-ISS-CAT-01 (kit bring-up); OpenDEAM v0.8.0 allocation of `dea:entity-platform-service` |
| **Trigger** | The org-wide catalog advancement programme populates this catalogue. The kit was generated against the information-system-service identity while the root model allocates `dea:catalog-platform-services` to the platform-service entity; this CR re-points the kit and lands the evidence-gated initial population. |

## 1. Executive summary

This CR re-points the catalogue kit from the stale information-system-service
identity to the platform-service identity (OpenDEAM v0.8.0,
`dea:entity-platform-service`, class alias PS, layer L5, building_block
L5-infrastructure) and lands the initial population: 500 canonical
Platform Service records across 14 domains, generated deterministically
(G-10) with three distinct vendor corroborations per record (G-12:
evidence only, no vendor product is canonical). No relationship instances
are asserted at admission (FOUNDATIONS D-8); each per-record README
carries the explicit `Deferred:` note Gate 6 requires.

## 2. Kit re-point (D-7)

The repository id (`dea:catalog-platform-services`) never changed; only the
entity identity the kit points at was stale. Re-pointed artefacts:

- `metamodel-pointer.yaml`: name Platform Service, abbreviation PS, version
  0.2.0, PS description, `metamodel:` block re-pointed to
  `dea:entity-platform-service` (PS, L5, L5-infrastructure, v0.8.0) and
  viewer URL `?entity=PS`. The `entities:` list already carried PS and is
  unchanged. The identity id `dea:catalog-platform-services` is unchanged.
- `scripts/check_pointer.py`: expected abbreviation PS, entity id and
  class alias re-pointed (layer L5 unchanged).
- `scripts/check_schema.py`: expected type const `PlatformService`, id
  pattern `^dea:platform-service-[a-z0-9-]+$`.
- `scripts/check_record_posture.py`: canonical id regex and type check
  re-pointed.
- `schemas/entity.schema.json`: title, id pattern, type const re-pointed;
  `metamodel_source` now cites the OpenDEAM v0.8.0 root-model allocation
  because dea-metamodel v1.0.0 does not yet carry a dedicated
  platform-service schema (follow-up recorded in remaining work).
- `schemas/fixtures/`: valid and invalid fixtures re-pointed to the PS
  namespace and type const.
- `docs/RECORD-STANDARD.md`, `docs/FOUNDATIONS.md`, `README.md`: ISS-to-PS
  rewrite; decision register extended with D-7 (re-point) and D-8 (no
  relationship instances at admission); D-3 id form amended to
  `dea:platform-service-<slug>`. The historical CR-ISS-CAT-01 document is
  untouched.

## 3. Population method (G-10, G-12)

- Data: `scripts/ps_population_data.json`, 500 service classes across 14
  domains (compute 40, storage 29, database 30, networking 41,
  identity-and-access 36, messaging-and-streaming 40,
  developer-tooling-and-ci-cd 50, observability 25, security-and-protection
  53, data-platform 50, ai-and-ml-platform 39, iot-and-edge 19,
  automation-and-orchestration 22, cost-and-governance 26), each with three
  distinct vendor corroborations and their catalogue URL references, from a
  curated inventory of 519 distinct vendors.
- Generator: `scripts/generate_ps_population.py`, deterministic and
  byte-idempotent (content md5 `e311c7bbd9e5d3d748e43a44b636e8c9` over the
  500 record subtrees); hard-fails on duplicate ids, missing vendor URLs,
  thin descriptions or rationales, over-long ids or names, and embargo
  characters (D-004/D-005: no em dash, en dash, ellipsis, or the
  triple-semicolon sequence, written in source as `(';' * 3)`);
- Record shape: id `dea:platform-service-<domain>-<slug>`, type
  `PlatformService`, version 1.0.0, lifecycle active, tags
  `domain:<d>` + `category:<c>`, three `published-document` evidence
  sources (vendor catalogue URLs) with a G-12 rationale, full admission
  ladder (candidate, corroborated, reviewed, canonical; all 2026-11-12,
  actor Emmanuel A. Otchere), governance with review date 2027-11-12, and
  metadata. Layout: `entities/v1-alpha/<id>/<id>.yaml` plus sibling
  `README.md` with the five required sections and the verbatim definition
  blockquote.
- `CATALOG.yaml` regenerated with the vendored regenerator; the
  `repository:` field is pinned to the GitHub origin URL because the
  regenerator reads the git remote, which is unavailable in the offline
  build environment (CI re-reads it from the checkout and produces the same
  value).

## 4. Deliverables

- 500 record subtrees under `entities/v1-alpha/` (1000 files).
- `scripts/ps_population_data.json`, `scripts/generate_ps_population.py`.
- Re-pointed kit per section 2.
- `CATALOG.yaml` regenerated (abbreviation PS, version 0.2.0, 500
  canonical entities).
- `CHANGELOG.md` entry; register row updated to Landed.

## 5. Acceptance criteria

1. All six local gates print `Findings: 0` (check_parse, check_pointer,
   check_record_posture, check_catalog_index --strict, check_schema,
   check_record_documentation); authorship gate conformant in --strict
   mode; CATALOG freshness parity with the committed index.
2. `validate-against-model` passes against OpenDEAM v0.8.0 for the
   re-pointed pointer (verified locally with
   `validate_consumer.py`).
3. The generator is byte-idempotent (`--check` run reproduces the
   committed records).
4. No embargo characters in any changed file (D-004/D-005), excluding
   pre-existing untouched content (NOTICE, CR-ISS-CAT-01 doc, CHANGELOG
   historical entry).

## 6. Risks

- The vendor URL references are evidence pointers, not SLA-tracked
  dependencies; rot is handled by record edits through future CRs.
- Population breadth (500 classes) trades review depth for coverage; the
  admission ladder records steward review at catalogue level, and per-record
  edits land through ordinary CRs.

## 7. Definition of done

All acceptance criteria green in CI on this PR; the register row and this
document land in the same commit series as the records.

## 8. Remaining work

- Metamodel follow-up: a dedicated platform-service schema in
  dea-metamodel (the projection currently cites the OpenDEAM v0.8.0
  allocation).
- Cross-catalogue relationship instances (for example ISS-to-PS
  specialisations, and specifies edges from the API catalogue) land
  through later CRs on the asserting side per FOUNDATIONS D-8 and the
  cross-catalogue policy.
- CR-ISS-CAT-01 historical document and NOTICE retain pre-existing em
  dashes (D-004 grandfathered, untouched by this CR).
