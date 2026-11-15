# Changelog

## [Unreleased]

### CR-ISS-CAT-09: Canonical Admission Wave

3025 InformationSystemService records promoted from the candidate slot to the canonical slot (provenance ladder completed per record; evidence citations preserved; ids untouched). Index: canonical 3025, candidates 0. All gates green.

### CR-ISS-CAT-08: Shard Subdivision (R5 Remedy)

Over-cap shard 'a' (queue + entities at 1,235 each) subdivided into two-character sub-shards (R5 findings resolved); vendored toolchain upgraded to depth-3 shard walking; candidates 2,525 / canonical 500 unchanged; ids untouched. All gates green.

### CR-ISS-CAT-05: InformationSystemService Candidate Admission Batch 02

Admitted 1225 new `InformationSystemService` CANDIDATE records through the gated intake workflow (queue gate → admission tool → catalog gates); ids content-derived and collision-checked; records land in `candidates/` subtrees at `lifecycle_status: proposed` / version 0.1.0; candidates count +1225, canonical unchanged; queue entries flipped to `admitted`.

### CR-ISS-CAT-04: InformationSystemService Candidate Admission Batch 01

Admitted 1300 new `InformationSystemService` CANDIDATE records through the gated intake workflow (queue gate → admission tool → catalog gates); ids content-derived and collision-checked; records land in `candidates/` subtrees at `lifecycle_status: proposed` / version 0.1.0; candidates count +1300, canonical unchanged; queue entries flipped to `admitted`.

### CR-ISS-CAT-03: InformationSystemService Candidate Corpus

2525 InformationSystemService candidate submissions landed in the contribution queue (sharded, gate-CONFORMANT) from 1 evidence bank(s); published prose + evidence citations + source_refs; provenance in ingestion/manifest.yaml. No catalog entities change; admission follows in CR-ISS-CAT-04+.

### CR-ISS-CAT-06: Entity Ingestion Groundwork (candidate intake queue + gates)

Gated intake workflow stood up: contribution queue + blocking queue gate (`scripts/check_contributions.py`, self-deriving from the projected schema) + admission tool (`scripts/admit_entity.py`: content-derived ids, collision-checked, candidates/ subtrees at `lifecycle_status: proposed` / v0.1.0) + intake template and process docs. CI: queue gate added as a blocking step; metaframework pin v2.6.0 → v2.8.0 with the shard-aware toolchain re-vendored from the v2.8.0 release (cmp'd). No records admitted by this CR.

### `CR-ISS-CAT-01` — catalogue foundation (kit bring-up)

Standard kit generated from the metamodel (org-wide catalog advancement
programme): hybrid pointer pinned to OpenDEAM v0.8.0;
`dependencies.yaml`; schema projection (copied-and-narrowed) with the
catalogue-instance layer; vendored relationship-instance contract; fixtures;
gates 1-6 wired into `validate-catalogue.yml` plus allocation and authorship
workflows; FOUNDATIONS (D-1..D-6) and record documentation standard. No
records admitted (population gated on CR-CR-ISS-CAT-06).

### `CR-CR-ISS-CAT-06`: platform service catalogue re-point and initial population

Kit re-pointed from the stale information-system-service identity to the
platform-service identity of OpenDEAM v0.8.0 (`dea:entity-platform-service`,
class alias PS, layer L5) per FOUNDATIONS D-7, and the initial population
landed: 500 canonical Platform Service records across 14 domains with three
distinct vendor corroborations each (519 distinct vendors cited), generated
deterministically (G-10) and vendor-neutral (G-12, evidence only). No
relationship instances asserted at admission (D-8); each record README
carries the explicit deferral note.
