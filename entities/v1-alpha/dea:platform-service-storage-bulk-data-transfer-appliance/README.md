# Bulk Data Transfer Appliance

> A Storage platform service in the data-movement category, consumed by multiple application components as shared infrastructure or runtime capability. Admitted by CR-ISS-CAT-02 with three independent vendor corroborations; no vendor product is canonical (G-12).

## Identity

- **Id:** `dea:platform-service-storage-bulk-data-transfer-appliance`
- **Type:** `PlatformService`
- **Version:** 1.0.0
- **Lifecycle:** active
- **Domain:** Storage (`domain:storage`)
- **Category:** `data-movement`
- **Allocation:** `dea:entity-platform-service` (PS), layer L5, building_block L5-infrastructure, OpenDEAM v0.8.0

## Evidence

Three independent vendor corroborations (G-12: evidence only, no vendor product is canonical):

1. Amazon Web Services, AWS Snowball (https://aws.amazon.com/products/)
2. Microsoft Azure, Azure Data Box (https://azure.microsoft.com/en-us/products)
3. Google Cloud, Transfer Appliance (https://cloud.google.com/products)

Rationale: Three independent vendor corroborations of the Bulk Data Transfer Appliance service class; vendor products are evidence only and never canonical (G-12).

## Classification-or-relationships

Tags: `domain:storage`, `category:data-movement`.

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
