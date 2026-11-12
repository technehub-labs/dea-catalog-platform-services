# Threat Intelligence Platform

> A Security and Protection platform service in the threat-intel category, consumed by multiple application components as shared infrastructure or runtime capability. Admitted by CR-ISS-CAT-02 with three independent vendor corroborations; no vendor product is canonical (G-12).

## Identity

- **Id:** `dea:platform-service-security-and-protection-threat-intelligence-platform`
- **Type:** `PlatformService`
- **Version:** 1.0.0
- **Lifecycle:** active
- **Domain:** Security and Protection (`domain:security-and-protection`)
- **Category:** `threat-intel`
- **Allocation:** `dea:entity-platform-service` (PS), layer L5, building_block L5-infrastructure, OpenDEAM v0.8.0

## Evidence

Three independent vendor corroborations (G-12: evidence only, no vendor product is canonical):

1. Recorded Future, Recorded Future (https://www.recordedfuture.com)
2. CrowdStrike, CrowdStrike Falcon Intelligence (https://www.crowdstrike.com/products/)
3. Google, Google Mandiant threat intelligence (https://cloud.google.com/products)

Rationale: Three independent vendor corroborations of the Threat Intelligence Platform service class; vendor products are evidence only and never canonical (G-12).

## Classification-or-relationships

Tags: `domain:security-and-protection`, `category:threat-intel`.

Deferred: no relationship instances are asserted at admission (FOUNDATIONS D-8). Cross-catalogue assertions, including platform-service specialisations recorded on the asserting side, land through later CRs once canonical targets exist.

## Provenance

Admission ladder (all stages 2026-11-12, actor Emmanuel A. Otchere):

candidate, corroborated, reviewed, canonical.

Generated deterministically by `scripts/generate_ps_population.py` (G-10) from `scripts/ps_population_data.json`.

## Governance

- **Functional owner:** Emmanuel A. Otchere
- **Steward:** Emmanuel A. Otchere
- **Approval status:** approved
- **Review date:** 2027-11-12
- **Source and evidence:** OpenDEAM v0.8.0 allocation of `dea:entity-platform-service`; CR-ISS-CAT-02 initial population (vendor catalogue corroborations, G-12); deterministic generator (G-10).
