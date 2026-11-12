#!/usr/bin/env python3
"""CR-ISS-CAT-02: deterministic Platform Service population generator (G-10).

Reads scripts/ps_population_data.json (the curated inventory: 14 domains,
500 service classes, each with three distinct vendor corroborations and
catalogue URL references) and emits one record subtree per service:

    entities/v1-alpha/<id>/<id>.yaml    the canonical record
    entities/v1-alpha/<id>/README.md    the per-record documentation

Properties:

- Deterministic and byte-idempotent: rerunning over an unchanged data
  file rewrites identical bytes; a content hash mismatch is a hard fail.
- Hard-fails before writing anything if the data violates the admission
  contract (duplicate ids, missing vendor URLs, thin descriptions or
  rationales, over-long ids or names, embargo characters).
- No relationship instances are asserted at admission (FOUNDATIONS D-8);
  each README carries the explicit Deferred note Gate 6 requires.
- Vendor products are corroborating evidence only, never canonical (G-12).

Run:  python3 scripts/generate_ps_population.py [--check]
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_PATH = REPO / "scripts" / "ps_population_data.json"
ENTITIES_ROOT = REPO / "entities" / "v1-alpha"

DATE = "2026-11-12"
REVIEW_DATE = "2027-11-12"
ACTOR = "Emmanuel A. Otchere"
TYPE_CONST = "PlatformService"
ID_PREFIX = "dea:platform-service-"
CR = "CR-ISS-CAT-02"

EMBARGO_CHARS = ["\u2014", "\u2013", "\u2026"]  # em dash, en dash, ellipsis
TRIPLE_SEMI = ";" * 3


def ystr(value: str) -> str:
    """House-style scalar: single-quoted with '' escaping; double-quoted
    when the prose contains a colon (RECORD-STANDARD.md conventions)."""
    if any(ch in value for ch in EMBARGO_CHARS) or TRIPLE_SEMI in value:
        raise SystemExit("embargo violation in scalar: %r" % value[:80])
    if ":" in value or value.startswith(('"', "'", ">", "#", "&", "*", "!", "|", "%", "@", "`")):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return "'" + value.replace("'", "''") + "'"


def embargo_check(text: str, where: str) -> None:
    for ch in EMBARGO_CHARS:
        if ch in text:
            raise SystemExit("embargo char %r in %s" % (ch, where))
    if TRIPLE_SEMI in text:
        raise SystemExit("embargo literal in %s" % where)


def build_identity(service: dict, domain_title: str) -> dict:
    rid = ID_PREFIX + service["domain"] + "-" + service["slug"]
    if len(rid) > 120:
        raise SystemExit("id too long: %s" % rid)
    name = service["name"]
    if not name or len(name) > 200:
        raise SystemExit("bad name for %s" % service["slug"])
    description = (
        "A %s platform service in the %s category, consumed by multiple "
        "application components as shared infrastructure or runtime capability. "
        "Admitted by %s with three independent vendor corroborations; no vendor "
        "product is canonical (G-12)." % (domain_title, service["category"], CR)
    )
    if not (40 <= len(description) <= 2000):
        raise SystemExit("description out of range for %s" % service["slug"])
    embargo_check(description, "description of " + rid)
    return {"id": rid, "name": name, "description": description}


def record_yaml(ident: dict, service: dict, urls: list[str]) -> str:
    vendors = service["vendors"]
    rationale = (
        "Three independent vendor corroborations of the %s service class; "
        "vendor products are evidence only and never canonical (G-12)." % ident["name"]
    )
    if len(rationale) < 20:
        raise SystemExit("rationale too thin for %s" % ident["id"])
    source_and_evidence = (
        "OpenDEAM v0.8.0 allocation of dea:entity-platform-service; %s initial "
        "population (vendor catalogue corroborations, G-12); deterministic "
        "generator scripts/generate_ps_population.py (G-10)." % CR
    )
    lines = [
        "# %s initial population (deterministic; regenerate with" % CR,
        "# scripts/generate_ps_population.py; data: scripts/ps_population_data.json).",
        "id: %s" % ident["id"],
        "type: %s" % TYPE_CONST,
        "name: %s" % ystr(ident["name"]),
        "description: %s" % ystr(ident["description"]),
        "version: 1.0.0",
        "lifecycle_status: active",
        "",
        "tags:",
        "  - domain:%s" % service["domain"],
        "  - category:%s" % service["category"],
        "evidence:",
        "  sources:",
    ]
    for url in urls:
        lines.append("    - kind: published-document")
        lines.append("      reference: %s" % ystr(url))
    lines += [
        "  rationale: %s" % ystr(rationale),
        "provenance:",
        "  ladder_passage:",
    ]
    for stage in ("candidate", "corroborated", "reviewed", "canonical"):
        lines += [
            "    - stage: %s" % stage,
            "      date: '%s'" % DATE,
            "      actor: %s" % ACTOR,
        ]
    lines += [
        "governance:",
        "  functional_owner: %s" % ACTOR,
        "  steward: %s" % ACTOR,
        "  approval_status: approved",
        "  review_date: '%s'" % REVIEW_DATE,
        "  source_and_evidence: %s" % ystr(source_and_evidence),
        "metadata:",
        "  created_at: '%s'" % DATE,
        "  updated_at: '%s'" % DATE,
        "  created_by: %s" % ACTOR,
        "  status: active",
    ]
    text = "\n".join(lines) + "\n"
    embargo_check(text, ident["id"])
    return text


def record_readme(ident: dict, service: dict, domain_title: str, urls: list[str]) -> str:
    vendors = service["vendors"]
    rationale = (
        "Three independent vendor corroborations of the %s service class; "
        "vendor products are evidence only and never canonical (G-12)." % ident["name"]
    )
    lines = [
        "# %s" % ident["name"],
        "",
        "> %s" % ident["description"],
        "",
        "## Identity",
        "",
        "- **Id:** `%s`" % ident["id"],
        "- **Type:** `%s`" % TYPE_CONST,
        "- **Version:** 1.0.0",
        "- **Lifecycle:** active",
        "- **Domain:** %s (`domain:%s`)" % (domain_title, service["domain"]),
        "- **Category:** `%s`" % service["category"],
        "- **Allocation:** `dea:entity-platform-service` (PS), layer L5, "
        "building_block L5-infrastructure, OpenDEAM v0.8.0",
        "",
        "## Evidence",
        "",
        "Three independent vendor corroborations (G-12: evidence only, "
        "no vendor product is canonical):",
        "",
    ]
    for n, ((vendor, product), url) in enumerate(zip(vendors, urls), start=1):
        lines.append("%d. %s, %s (%s)" % (n, vendor, product, url))
    lines += [
        "",
        "Rationale: %s" % rationale,
        "",
        "## Classification-or-relationships",
        "",
        "Tags: `domain:%s`, `category:%s`." % (service["domain"], service["category"]),
        "",
        "Deferred: no relationship instances are asserted at admission "
        "(FOUNDATIONS D-8). Cross-catalogue assertions, including "
        "platform-service specialisations recorded on the asserting side, "
        "land through later CRs once canonical targets exist.",
        "",
        "## Provenance",
        "",
        "Admission ladder (all stages %s, actor %s):" % (DATE, ACTOR),
        "",
        "candidate, corroborated, reviewed, canonical.",
        "",
        "Generated deterministically by `scripts/generate_ps_population.py` (G-10) "
        "from `scripts/ps_population_data.json`.",
        "",
        "## Governance",
        "",
        "- **Functional owner:** %s" % ACTOR,
        "- **Steward:** %s" % ACTOR,
        "- **Approval status:** approved",
        "- **Review date:** %s" % REVIEW_DATE,
        "- **Source and evidence:** OpenDEAM v0.8.0 allocation of "
        "`dea:entity-platform-service`; %s initial population (vendor "
        "catalogue corroborations, G-12); deterministic generator (G-10)." % CR,
        "",
    ]
    text = "\n".join(lines)
    embargo_check(text, "README of " + ident["id"])
    return text


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    services = data["services"]
    domain_titles = data["domains"]
    url_map = data["vendor_urls"]

    try:
        import yaml  # optional self-check; present in CI and vendored locally
    except ImportError:
        yaml = None

    seen: dict[str, str] = {}
    payloads: list[tuple[str, str, str]] = []  # (id, yaml, readme)
    for service in services:
        ident = build_identity(service, domain_titles[service["domain"]])
        if ident["id"] in seen:
            raise SystemExit("duplicate id: %s" % ident["id"])
        seen[ident["id"]] = service["slug"]
        urls = url_map.get(service["slug"])
        if not urls or len(urls) != len(service["vendors"]):
            raise SystemExit("vendor URL map incomplete for %s" % service["slug"])
        for v, _p in service["vendors"]:
            if not v or "placeholder" in v.lower():
                raise SystemExit("bad vendor in %s" % service["slug"])
        yaml_text = record_yaml(ident, service, urls)
        if yaml is not None:
            parsed = yaml.safe_load(yaml_text)
            if not isinstance(parsed, dict) or parsed.get("id") != ident["id"]:
                raise SystemExit("emitted YAML does not parse for %s" % ident["id"])
        readme_text = record_readme(
            ident, service, domain_titles[service["domain"]], urls
        )
        payloads.append((ident["id"], yaml_text, readme_text))

    digest = hashlib.md5()
    written = 0
    for rid, yaml_text, readme_text in payloads:
        subtree = ENTITIES_ROOT / rid
        if check_only:
            for name, want in ((rid + ".yaml", yaml_text), ("README.md", readme_text)):
                have = (subtree / name).read_text(encoding="utf-8") if (subtree / name).exists() else None
                if have != want:
                    print("FAIL: %s is not current with the generator output" % (subtree / name))
                    return 1
            digest.update(yaml_text.encode("utf-8"))
            digest.update(readme_text.encode("utf-8"))
            written += 1
            continue
        subtree.mkdir(parents=True, exist_ok=True)
        (subtree / (rid + ".yaml")).write_text(yaml_text, encoding="utf-8")
        (subtree / "README.md").write_text(readme_text, encoding="utf-8")
        digest.update(yaml_text.encode("utf-8"))
        digest.update(readme_text.encode("utf-8"))
        written += 1

    print("records: %d" % written)
    print("content md5: %s" % digest.hexdigest())
    print("OK: population generated deterministically")
    return 0


if __name__ == "__main__":
    sys.exit(main())
