# Record Documentation Standard (CR-ISS-CAT-01; re-pointed by CR-ISS-CAT-02)

Every canonical Platform Service record must satisfy this standard. Gate 6
(`scripts/check_record_documentation.py`) enforces the machine-checkable
subset; steward review enforces the rest.

## 1. Record file

One record per subtree: `entities/v1-alpha/<id>/<id>.yaml`, where `<id>` is
the canonical id (`dea:platform-service-<slug>`). Obligations beyond the schema:

1. `name` is the real name as consumers know it.
2. `description` states what the record is and its consuming purpose: not
   a restatement of the name.
3. `evidence.sources` cites at least one verifiable source; `rationale`
   says why it justifies admission.
4. `provenance.ladder_passage` records passage to canonical with quoted
   dates and authorship-bearing actors (AUT rules).
5. Relationship instances are asserted only against canonical targets, or
   the README carries an explicit `Deferred:` note.

## 2. YAML conventions

- Dates single-quoted so they stay strings.
- Apostrophes escaped (`''`) in single-quoted prose; double quotes when the
  prose contains a colon.

## 3. Per-record README

Sections: `# <Name>` + verbatim definition blockquote, `## Identity`,
`## Evidence`, `## Classification-or-relationships`, `## Provenance`,
`## Governance`. The definition blockquote must equal the record's
`description` verbatim (Gate 6 checks).

## 4. Change discipline

Record changes land through CRs; a record edit regenerates `CATALOG.yaml`
in the same PR. Retired records move to `retired/`, never deleted.

## 5. Platform Service specifics (CR-ISS-CAT-02)

- Records describe shared infrastructure or runtime services consumed by
  multiple application components, per the OpenDEAM v0.8.0 allocation of
  `dea:entity-platform-service`.
- Evidence corroboration follows G-12: at least three distinct vendors must
  independently corroborate the service class; vendor products are
  evidence only and never canonical.
- Records carry no relationship instances at admission; each README's
  Classification-or-relationships section carries the explicit `Deferred:`
  note required by Gate 6 until the cross-catalogue relationship CRs land.
