# Change Requests: dea-catalog-platform-services

This index tracks every change request that lands on this repository.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-ISS-CAT-01](CR-ISS-CAT-01-catalogue-foundation.md) | Catalogue foundation (kit bring-up) | Landed (this PR) | Standard kit: pointer, dependencies, schema projection, gates 1-6, workflows, FOUNDATIONS, record standard. No records admitted. |
| [CR-CR-ISS-CAT-06](CR-CR-ISS-CAT-06-platform-service-repoint-and-initial-population.md) | Platform service re-point and initial population | Landed (this PR) | Kit re-pointed to `dea:entity-platform-service` (PS, L5) per D-7; 500 canonical records across 14 domains, G-10 deterministic, G-12 vendor-neutral (3 corroborations each, 519 vendors). Relationships deferred per D-8. |

## Numbering

Series tag `CR-ISS-CAT-NN`, sequential. Cross-repo CRs that touch this
repository are recorded here with their home-repo identifier.
| [CR-ISS-CAT-06](CR-ISS-CAT-06-iss-cat-02.md) | Entity Ingestion Groundwork (candidate intake queue + gates) | **Proposed (this PR)** | Gated intake: queue + blocking queue gate + admission tool (candidate-state subtrees, content-derived ids); pin v2.6.0→v2.8.0 + shard-aware toolchain re-vendor. No records. |
| [CR-ISS-CAT-03](CR-ISS-CAT-03-iss-cat-03.md) | InformationSystemService Candidate Corpus | **Landed (this PR)** | 2525 queue submissions from 1 bank(s); manifest with sha256s; queue gate CONFORMANT; no entities change. |
| [CR-ISS-CAT-04](CR-ISS-CAT-04-iss-cat-04.md) | InformationSystemService Candidate Admission Batch 01 (1Forge Finance APIs (1forge.com) … Clever-Cloud API (clever-cloud.com)) | **Landed (this PR)** | Admitted 1300 `InformationSystemService` CANDIDATE records via the gated intake workflow (queue gate → admission tool → catalog gates); candidates +1300, canonical unchanged; records at `lifecycle_status: proposed` in `candidates/` subtrees. |
| [CR-ISS-CAT-05](CR-ISS-CAT-05-iss-cat-05.md) | InformationSystemService Candidate Admission Batch 02 (Data API (clever.com) … API Reference: Billing (zuora.com)) | **Landed (this PR)** | Admitted 1225 `InformationSystemService` CANDIDATE records via the gated intake workflow (queue gate → admission tool → catalog gates); candidates +1225, canonical unchanged; records at `lifecycle_status: proposed` in `candidates/` subtrees. |
| [CR-ISS-CAT-07](CR-ISS-CAT-07-cr-iss-cat-07.md) | CR Naming/Numbering Correction | **Landed (this PR)** | Programme batch CRs renamed to house-form CR-prefixed identifiers (mapping in the CR); content unchanged. |
| [CR-ISS-CAT-08](CR-ISS-CAT-08-cr-iss-cat-08.md) | Shard Subdivision (R5 Remedy) | **Landed (this PR)** | Over-cap shard 'a' subdivided (two-character sub-shards); toolchain depth-3 shard walking; counts unchanged. |
| [CR-ISS-CAT-09](CR-ISS-CAT-09-cr-iss-cat-09.md) | Canonical Admission Wave (3025) | **Landed (this PR)** | 3025 records promoted candidates/ -> canonical root; ladder completed; evidence preserved; canonical 3025, candidates 0. |
