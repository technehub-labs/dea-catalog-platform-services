# Foundations: Platform Service Catalog

This document records the method the catalogue follows: cardinal scope,
exclusions, admission criteria, allocation, cross-catalogue policy, and the
decision register. The record documentation standard
([RECORD-STANDARD.md](RECORD-STANDARD.md)) and the schema projection carry
the operational contract.

## 1. Cardinal scope

**Platform Service**: a shared infrastructure or runtime service consumed
by multiple application components. Allocated to OpenDEAM v0.8.0 as
`dea:entity-platform-service` (class alias `PS`), layer L5, building_block
L5-infrastructure, with this repository (`dea-catalog-platform-services`)
as the owning catalog. The catalogue was re-pointed from the stale
information-system-service identity to the platform-service identity by
CR-ISS-CAT-02 (D-7); information system service records remain owned by
`dea-catalog-information-system-services`.

## 2. What is deliberately excluded

Boundaries against sibling entity types are governed by the root model
definitions; anything that is not a platform service record belongs to its
owning catalogue (see the OpenDEAM `catalog_repo` allocations). In
particular, information system services (ISS), integration interfaces (IF)
and APIs are separate entities with their own catalogues.

## 3. Admission criteria and evidence ladder

1. The record describes a platform service per the root model definition.
2. At least one evidence source verifiably exists at admission time
   (`repository-path`, `system-of-record`, or `published-document`);
   CR-ISS-CAT-02 population additionally requires three distinct vendor
   corroborations per record (G-12; evidence only, no vendor canonical).
3. Relationship instances are asserted only against canonical target ids
   that exist; absence is honest (no local substitutes).

Evidence ladder (asserted in `provenance.ladder_passage`):
candidate → corroborated → reviewed → canonical.

## 4. Allocation

`dea:entity-platform-service` (alias `PS`), layer L5 / L5-infrastructure,
pinned against OpenDEAM v0.8.0. Validated remotely by
`validate-allocation.yml` and locally by Gate 2. Upstream pins live in
`dependencies.yaml`.

## 5. Cross-catalogue reference policy

1. Crosswalks and references are recorded on the asserting record's side,
   as typed relationship instances (metamodel relationship-instance
   contract).
2. Assertions wait for canonical targets: no scheme invention where a
   sibling id scheme does not exist.
3. Gates never resolve remote repositories; vendored registry snapshots
   carry the offline contract where a specific target family is asserted.

## 6. Decision-points register

| # | Decision | Status |
|---|---|---|
| D-1 | Methodology-first bring-up: no records before the kit and population CR | Adopted (CR-ISS-CAT-01) |
| D-2 | Hybrid pointer: identity keys for the regenerator + `metamodel:` allocation block for the root-model validator | Adopted (CR-ISS-CAT-01) |
| D-3 | Record ids take the `dea:platform-service-<slug>` form (information-classes `dea:`-prefix precedent; namespace re-pointed by CR-ISS-CAT-02) | Adopted (CR-ISS-CAT-01, amended by CR-ISS-CAT-02) |
| D-4 | Admission ladder: candidate → corroborated → reviewed → canonical | Adopted (CR-ISS-CAT-01) |
| D-5 | Evidence-only admission: no record without a verifiable source; population plans document the wait | Adopted (CR-ISS-CAT-01) |
| D-6 | `CATALOG.yaml` is committed, not ignored (template deviation): the freshness gate diffs the committed index | Adopted (CR-ISS-CAT-01) |
| D-7 | Kit re-point from the stale information-system-service identity to the platform-service identity; ISS records stay in dea-catalog-information-system-services | Adopted (CR-ISS-CAT-02) |
| D-8 | Population records carry no relationship instances at admission; each README carries an explicit `Deferred:` note until the cross-catalogue relationship CRs land | Adopted (CR-ISS-CAT-02) |

## 7. Population plan

Initial population lands evidence-gated through CR-ISS-CAT-02: 500
platform service records across 14 domains, each admitted with three
distinct vendor corroborations (G-12) and a deterministic, byte-idempotent
generator (`scripts/generate_ps_population.py`; G-10). Relationship
instances (for example platform-service specialisations asserted on the
ISS side) are deferred to later CRs per D-8.
