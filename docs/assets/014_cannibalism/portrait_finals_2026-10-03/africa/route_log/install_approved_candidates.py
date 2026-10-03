"""Install only the eight parent-approved Event 014 Africa DDS candidates."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


MOD_ROOT = Path(__file__).resolve().parents[6]
PACKAGE = Path(__file__).resolve().parents[1]
APPROVAL = MOD_ROOT / "docs/plans/014_cannibalism_plans/evidence/2026-10-03_africa_portrait_parent_review.json"
PREVIOUS_SNAPSHOT = MOD_ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/evidence/runtime_preinstall_snapshot.json"
RUNTIME_DIR = MOD_ROOT / "gfx/leaders/014_cannibalism"
TRACKED_DEFINITIONS = (
    MOD_ROOT / "interface/014_cannibalism.gfx",
    MOD_ROOT / "common/characters/014_cannibalism_characters.txt",
)
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
OWNED_RUNTIME = {
    f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_africa.dds" for slot in SLOTS
}
PROTECTED_HANNIBAL = {
    "gfx/leaders/014_cannibalism/hannibal.dds",
    "gfx/leaders/014_cannibalism/hannibal_wendigo.dds",
    "gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds",
    "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def relative(path: Path) -> str:
    return path.relative_to(MOD_ROOT).as_posix()


def capture_snapshot() -> dict[str, object]:
    dds_paths = sorted(RUNTIME_DIR.glob("*.dds"), key=lambda path: path.name.lower())
    if len(dds_paths) != 60:
        raise RuntimeError(f"Expected all 60 Event 014 leader DDS files; found {len(dds_paths)}")
    definitions = []
    for path in TRACKED_DEFINITIONS:
        if not path.is_file():
            raise FileNotFoundError(f"Required Event 014 portrait definition is missing: {path}")
        data = path.read_bytes()
        definitions.append({"path": relative(path), "bytes": len(data), "sha256": sha256(data)})
    status = subprocess.run(
        ["git", "status", "--short", "--", "gfx/leaders/014_cannibalism", "interface/014_cannibalism.gfx", "common/characters/014_cannibalism_characters.txt"],
        cwd=MOD_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    return {
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "dds_count": len(dds_paths),
        "dds": [
            {"path": relative(path), "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes())}
            for path in dds_paths
        ],
        "definitions": definitions,
        "worktree_status_in_scope": status,
    }


def write_json_new(path: Path, payload: dict[str, object]) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite install evidence: {path}")
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    approval = json.loads(APPROVAL.read_text(encoding="utf-8"))
    previous = json.loads(PREVIOUS_SNAPSHOT.read_text(encoding="utf-8"))
    approved_rows = {row["runtime"].replace("\\", "/"): row for row in approval["rows"]}
    old_rows = {row["Path"].replace("\\", "/"): row for row in previous["dds"]}
    if set(approved_rows) != OWNED_RUNTIME or len(approved_rows) != 8:
        raise RuntimeError("Parent approval does not cover exactly the eight authorized Africa paths")

    candidate_data: dict[str, bytes] = {}
    for slot in SLOTS:
        runtime_rel = f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_africa.dds"
        row = approved_rows[runtime_rel]
        candidate_path = MOD_ROOT / row["candidate"]
        runtime_path = MOD_ROOT / runtime_rel
        candidate_bytes = candidate_path.read_bytes()
        if sha256(candidate_bytes) != row["candidate_sha256"].upper():
            raise RuntimeError(f"Candidate bytes do not match parent approval for {slot}")
        previous_row = old_rows.get(runtime_rel)
        if previous_row is None or previous_row["SHA256"].upper() != row["runtime_before_sha256"].upper():
            raise RuntimeError(f"Parent-approved prior-runtime baseline disagrees for {slot}")
        if sha256(runtime_path.read_bytes()) != row["runtime_before_sha256"].upper():
            raise RuntimeError(f"Current Africa runtime DDS differs from parent-approved before hash for {slot}; refusing install")
        candidate_data[runtime_rel] = candidate_bytes

    before_path = PACKAGE / "route_log/runtime_install_snapshot_before.json"
    after_path = PACKAGE / "route_log/runtime_install_snapshot_after.json"
    receipt_path = PACKAGE / "evidence/runtime_install_receipt.json"
    backup_dir = PACKAGE / "evidence/runtime_before"
    if any(path.exists() for path in (before_path, after_path, receipt_path, backup_dir)):
        raise FileExistsError("Install snapshot, receipt, or backup already exists; refusing to overwrite")

    before = capture_snapshot()
    before_map = {row["path"]: row for row in before["dds"]}
    for runtime_rel, row in approved_rows.items():
        actual_before = before_map[runtime_rel]["sha256"]
        if actual_before != row["runtime_before_sha256"].upper():
            raise RuntimeError(f"Pre-install snapshot disagrees with parent before hash: {runtime_rel}")
    write_json_new(before_path, before)

    backup_dir.mkdir(parents=True)
    backups = []
    for slot in SLOTS:
        runtime_rel = f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_africa.dds"
        runtime_path = MOD_ROOT / runtime_rel
        backup_path = backup_dir / runtime_path.name
        original = runtime_path.read_bytes()
        if sha256(original) != before_map[runtime_rel]["sha256"]:
            raise RuntimeError(f"Africa runtime changed after snapshot and before backup: {runtime_rel}")
        backup_path.write_bytes(original)
        backup_bytes = backup_path.read_bytes()
        if backup_bytes != original:
            raise RuntimeError(f"Africa runtime backup is not byte-identical: {runtime_rel}")
        backups.append(
            {
                "runtime_path": runtime_rel,
                "backup_path": relative(backup_path),
                "bytes": len(backup_bytes),
                "sha256": sha256(backup_bytes),
                "matches_current_preinstall_snapshot": True,
            }
        )

    installed_rows = []
    for slot in SLOTS:
        runtime_rel = f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_africa.dds"
        runtime_path = MOD_ROOT / runtime_rel
        approved = approved_rows[runtime_rel]
        data = candidate_data[runtime_rel]
        runtime_path.write_bytes(data)
        installed_hash = sha256(runtime_path.read_bytes())
        if installed_hash != approved["candidate_sha256"].upper():
            raise RuntimeError(f"Installed bytes do not match approved candidate for {slot}")
        installed_rows.append(
            {
                "slot": slot,
                "candidate_path": approved["candidate"],
                "candidate_sha256": approved["candidate_sha256"].upper(),
                "runtime_path": runtime_rel,
                "runtime_after_sha256": installed_hash,
                "installed_bytes_equal_approved_candidate": True,
            }
        )

    after = capture_snapshot()
    write_json_new(after_path, after)
    after_map = {row["path"]: row for row in after["dds"]}
    other_differences = []
    for runtime_rel, before_row in before_map.items():
        if runtime_rel in OWNED_RUNTIME:
            continue
        after_row = after_map[runtime_rel]
        if before_row["sha256"] != after_row["sha256"]:
            other_differences.append(
                {
                    "path": runtime_rel,
                    "before_sha256": before_row["sha256"],
                    "after_sha256": after_row["sha256"],
                    "region_hint": next((region for region in ("asia", "europe", "middle_east", "north_america", "south_america", "oceania") if f"_{region}.dds" in runtime_rel), "non-regional"),
                    "attribution": "Concurrent or external change observed during the bounded install; preserved and not reverted.",
                }
            )
    definition_differences = []
    before_definitions = {row["path"]: row for row in before["definitions"]}
    after_definitions = {row["path"]: row for row in after["definitions"]}
    for path, before_row in before_definitions.items():
        if before_row["sha256"] != after_definitions[path]["sha256"]:
            definition_differences.append(
                {"path": path, "before_sha256": before_row["sha256"], "after_sha256": after_definitions[path]["sha256"]}
            )

    receipt = {
        "installed_utc": datetime.now(timezone.utc).isoformat(),
        "approval_evidence": relative(APPROVAL),
        "approval_scope": approval["acceptance_scope"],
        "snapshot_before": relative(before_path),
        "snapshot_after": relative(after_path),
        "backup_scope": "only the eight existing Africa runtime DDS files; no other runtime bytes were backed up or replaced",
        "backups": backups,
        "installed_candidates": installed_rows,
        "installed_count": len(installed_rows),
        "all_eight_runtime_hashes_match_parent_approved_candidates": all(row["installed_bytes_equal_approved_candidate"] for row in installed_rows),
        "other_52_dds_unchanged_at_immediate_africa_postinstall_snapshot": not other_differences,
        "other_dds_differences": other_differences,
        "gfx_and_character_definitions_unchanged_at_immediate_africa_postinstall_snapshot": not definition_differences,
        "definition_differences": definition_differences,
        "protected_hannibal_unchanged_at_immediate_africa_postinstall_snapshot": all(
            before_map[path]["sha256"] == after_map[path]["sha256"] for path in PROTECTED_HANNIBAL
        ),
        "europe_asia_and_other_disjoint_runtime_paths_were_not_written_by_this_install": True,
        "gfx_or_character_files_written": False,
        "full_56_portrait_or_event_goal_complete": False,
    }
    write_json_new(receipt_path, receipt)
    print(
        json.dumps(
            {
                "receipt": relative(receipt_path),
                "installed": len(installed_rows),
                "other_52_unchanged": receipt["other_52_dds_unchanged_from_current_preinstall_snapshot"],
                "definitions_unchanged": receipt["gfx_and_character_definitions_unchanged_from_current_preinstall_snapshot"],
                "other_differences": other_differences,
                "definition_differences": definition_differences,
            }
        )
    )


if __name__ == "__main__":
    main()
