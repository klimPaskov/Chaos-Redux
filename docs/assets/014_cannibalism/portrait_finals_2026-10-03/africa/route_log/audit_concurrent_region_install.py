"""Attribute post-Africa Middle East DDS changes without altering either tranche."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


MOD_ROOT = Path(__file__).resolve().parents[6]
AFRICA = Path(__file__).resolve().parents[1]
AFRICA_AFTER = AFRICA / "route_log/runtime_install_snapshot_after.json"
AFRICA_RECEIPT = AFRICA / "evidence/runtime_install_receipt.json"
MIDDLE_EAST = MOD_ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/middle_east"
ME_RECEIPT = MIDDLE_EAST / "evidence/runtime_install_receipt.json"
ME_SNAPSHOT = MIDDLE_EAST / "evidence/runtime_postinstall_snapshot.json"
FINAL_SNAPSHOT_PATH = AFRICA / "route_log/runtime_install_snapshot_final.json"
AUDIT_PATH = AFRICA / "route_log/runtime_install_final_audit.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def relative(path: Path) -> str:
    return path.relative_to(MOD_ROOT).as_posix()


def main() -> None:
    if FINAL_SNAPSHOT_PATH.exists() or AUDIT_PATH.exists():
        raise FileExistsError("Final runtime audit already exists; refusing to overwrite")
    africa_after = json.loads(AFRICA_AFTER.read_text(encoding="utf-8"))
    africa_receipt = json.loads(AFRICA_RECEIPT.read_text(encoding="utf-8"))
    me_receipt = json.loads(ME_RECEIPT.read_text(encoding="utf-8"))
    me_snapshot = json.loads(ME_SNAPSHOT.read_text(encoding="utf-8"))

    previous_map = {row["path"]: row for row in africa_after["dds"]}
    current_paths = sorted((MOD_ROOT / "gfx/leaders/014_cannibalism").glob("*.dds"), key=lambda p: p.name.lower())
    if len(current_paths) != 60:
        raise RuntimeError(f"Expected 60 Event 014 DDS files in final snapshot; found {len(current_paths)}")
    current_rows = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": digest(path.read_bytes())}
        for path in current_paths
    ]
    current_map = {row["path"]: row for row in current_rows}

    me_rows = me_receipt["installed_assets"]
    me_map = {row["runtime_path"]: row for row in me_rows}
    if len(me_map) != 8:
        raise RuntimeError(f"Middle East install receipt does not cover eight assets: {len(me_map)}")
    changed_since_africa = {
        path for path, row in previous_map.items() if row["sha256"] != current_map[path]["sha256"]
    }
    if changed_since_africa != set(me_map):
        raise RuntimeError(
            "Post-Africa runtime changes include paths outside the documented Middle East install; "
            f"expected={sorted(me_map)}, observed={sorted(changed_since_africa)}"
        )

    me_changes = []
    for path, row in me_map.items():
        current_hash = current_map[path]["sha256"]
        if current_hash != row["candidate_sha256_parent_approved"].upper():
            raise RuntimeError(f"Current Middle East bytes do not match its parent-approved receipt: {path}")
        if current_hash != row["installed_runtime_sha256"].upper() or not row["installed_exact_candidate"]:
            raise RuntimeError(f"Middle East receipt does not establish approved candidate installation: {path}")
        me_changes.append(
            {
                "path": path,
                "region": "middle_east",
                "before_africa_postinstall_sha256": previous_map[path]["sha256"],
                "current_sha256": current_hash,
                "parent_approved_candidate_sha256": row["candidate_sha256_parent_approved"].upper(),
                "owner_receipt": relative(ME_RECEIPT),
                "owner_postinstall_snapshot": relative(ME_SNAPSHOT),
                "attribution": "Parent-approved Middle East tranche installed these disjoint paths after the Africa post-install snapshot; files were preserved, not reset.",
            }
        )

    africa_checks = []
    for row in africa_receipt["installed_candidates"]:
        current_hash = current_map[row["runtime_path"]]["sha256"]
        if current_hash != row["candidate_sha256"].upper():
            raise RuntimeError(f"Africa runtime no longer matches its approved candidate: {row['runtime_path']}")
        africa_checks.append({"path": row["runtime_path"], "sha256": current_hash, "matches_approved_candidate": True})

    gfx_path = MOD_ROOT / "interface/014_cannibalism.gfx"
    characters_path = MOD_ROOT / "common/characters/014_cannibalism_characters.txt"
    definitions = [
        {"path": relative(path), "bytes": path.stat().st_size, "sha256": digest(path.read_bytes())}
        for path in (gfx_path, characters_path)
    ]
    me_definitions = {row["path"]: row for row in (me_snapshot["gfx_snapshot"], me_snapshot["character_snapshot"])}
    definitions_match_me_snapshot = all(row["sha256"] == me_definitions[row["path"]]["sha256"] for row in definitions)
    if not definitions_match_me_snapshot:
        raise RuntimeError("GFX or Event 014 character definition changed after the Middle East post-install snapshot")
    if len(me_snapshot["all_sixty_dds"]) != 60:
        raise RuntimeError("Middle East post-install snapshot does not cover all 60 Event 014 DDS files")
    me_snapshot_map = {row["path"]: row["sha256"].upper() for row in me_snapshot["all_sixty_dds"]}
    final_dds_match_me_snapshot = all(current_map[path]["sha256"] == me_snapshot_map[path] for path in current_map)
    if not final_dds_match_me_snapshot:
        raise RuntimeError("Current Event 014 DDS files differ from the later Middle East post-install snapshot")

    final_snapshot = {
        "snapshot_type": "current Event 014 portrait package after Africa and Middle East disjoint installations",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "dds_count": 60,
        "all_sixty_dds": current_rows,
        "gfx_snapshot": definitions[0],
        "character_snapshot": definitions[1],
    }
    FINAL_SNAPSHOT_PATH.write_text(json.dumps(final_snapshot, indent=2) + "\n", encoding="utf-8")

    audit = {
        "captured_utc": final_snapshot["captured_utc"],
        "africa_install_receipt": relative(AFRICA_RECEIPT),
        "later_disjoint_region_receipt": relative(ME_RECEIPT),
        "later_disjoint_region_snapshot": relative(ME_SNAPSHOT),
        "current_all_60_match_later_middle_east_postinstall_snapshot": final_dds_match_me_snapshot,
        "current_gfx_and_character_definitions_match_later_middle_east_postinstall_snapshot": definitions_match_me_snapshot,
        "africa_eight_still_match_parent_approved_candidates": len(africa_checks) == 8,
        "africa_runtime_current_hashes": africa_checks,
        "subsequent_middle_east_changes": me_changes,
        "all_other_paths_preserved_and_no_unattributed_changes_since_africa_snapshot": len(changed_since_africa) == 8,
        "final_snapshot": relative(FINAL_SNAPSHOT_PATH),
    }
    AUDIT_PATH.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "audit": relative(AUDIT_PATH),
                "current_60_match_middle_east_receipt_snapshot": final_dds_match_me_snapshot,
                "africa_approved_files_match": len(africa_checks) == 8,
                "subsequent_middle_east_paths_attributed": len(me_changes),
                "definitions_unchanged": definitions_match_me_snapshot,
            }
        )
    )


if __name__ == "__main__":
    main()
