#!/usr/bin/env python3
"""Verify active Event 015 identity sources against built-in ImageGen outputs."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[5]
BASE = REPO / "docs/assets/015_utopia_manifesto/route_identity_2026_07_14"
GENERATED = Path.home() / ".codex/generated_images"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(REPO)).replace("\\", "/")


def main() -> None:
    flag_records = json.loads((BASE / "flag_identity_asset_records.json").read_text(encoding="utf-8"))
    portrait_records = json.loads((BASE / "institutional_portrait_asset_records.json").read_text(encoding="utf-8"))
    active = [
        row
        for row in flag_records
        if row["kind"] == "flag_main" and not row.get("alias_of")
    ] + portrait_records
    if len(active) != 25:
        raise ValueError(f"expected 25 independent sources, found {len(active)}")
    if len({row["imagegen_handle"] for row in active}) != 25:
        raise ValueError("active built-in ImageGen handles are not distinct")
    evidence = []
    for row in active:
        handle = str(row["imagegen_handle"])
        matches = list(GENERATED.rglob(f"{handle}.png"))
        if len(matches) != 1:
            raise ValueError(f"expected one built-in output for {handle}, found {len(matches)}")
        generated = matches[0]
        source = REPO / str(row["source"])
        source_hash = sha256(source)
        generated_hash = sha256(generated)
        if source_hash != generated_hash or source.read_bytes() != generated.read_bytes():
            raise ValueError(f"packaged source is not an exact built-in output: {row['identifier']}")
        evidence.append(
            {
                "kind": "flag_composition" if str(row["kind"]).startswith("flag_") else "institutional_portrait",
                "identifier": row["identifier"],
                "imagegen_handle": handle,
                "package_source": rel(source),
                "package_source_sha256": source_hash,
                "built_in_store_object": f"{generated.parent.name}/{generated.name}",
                "built_in_store_sha256": generated_hash,
                "exact_byte_equality": True,
            }
        )
    result = {
        "status": "passed",
        "verified_at_packaging": "2026-07-15",
        "independent_sources": len(evidence),
        "flag_compositions": sum(1 for row in evidence if row["kind"] == "flag_composition"),
        "institutional_portraits": sum(1 for row in evidence if row["kind"] == "institutional_portrait"),
        "distinct_built_in_handles": len({row["imagegen_handle"] for row in evidence}),
        "check": "every active package source is an exact byte copy of the built-in ImageGen output named by its recorded handle",
        "documented_aliases": {
            "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH": "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic",
            "UTOPIA_MANIFESTO_COUNCIL_UNION": "UTOPIA_MANIFESTO_COUNCIL_UNION_communism",
            "UTOPIA_MANIFESTO_PLANNED_UTOPIA": "UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality",
            "UTOPIA_MANIFESTO_CLOSED_ISLAND": "UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism",
        },
        "sources": evidence,
    }
    (BASE / "imagegen_source_evidence_2026_07_15.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {len(evidence)} independent package sources against exact built-in ImageGen output bytes.")


if __name__ == "__main__":
    main()
