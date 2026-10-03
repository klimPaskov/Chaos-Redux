"""Install only the eight parent-approved Event 014 North America DDS files.

Run once from the mod root with: python -B <this file>.
The script validates the parent hashes, records all 60 current DDS plus portrait
GFX and character hashes immediately before installation, backs up only the
eight North America targets, installs exact approved candidate bytes, and
records all 60 hashes again without reverting concurrent work.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
PACKAGE = ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/north_america"
EVIDENCE = PACKAGE / "evidence"
RUNTIME_DIR = ROOT / "gfx/leaders/014_cannibalism"
REGISTRY = ROOT / "interface/014_cannibalism.gfx"
CHARACTERS = ROOT / "common/characters/014_cannibalism_characters.txt"
PARENT_REVIEW = ROOT / "docs/plans/014_cannibalism_plans/evidence/2026-10-03_north_america_portrait_parent_review.json"
SOURCE_PHASE_SNAPSHOT = EVIDENCE / "runtime_preinstall_snapshot.json"
PRE_SNAPSHOT = EVIDENCE / "runtime_install_preinstall_all60_snapshot.json"
POST_SNAPSHOT = EVIDENCE / "runtime_install_postinstall_all60_snapshot.json"
RECEIPT = EVIDENCE / "runtime_install_receipt.json"
BACKUP_DIR = EVIDENCE / "runtime_before_install"
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def file_row(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data), "sha256": sha(data)}


def snapshot(label: str) -> dict:
    files = sorted(RUNTIME_DIR.glob("*.dds"), key=lambda path: path.name.casefold())
    if len(files) != 60:
        raise RuntimeError(f"Expected 60 Event 014 DDS files, found {len(files)}")
    return {
        "label": label,
        "captured_utc": now_utc(),
        "runtime_dds_count": len(files),
        "runtime_dds": [file_row(path) for path in files],
        "portrait_registry": file_row(REGISTRY),
        "character_definition": file_row(CHARACTERS),
    }


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    if BACKUP_DIR.exists():
        raise RuntimeError(f"Backup destination exists; refusing to overwrite: {BACKUP_DIR}")
    parent = json.loads(PARENT_REVIEW.read_text(encoding="utf-8"))
    rows = parent.get("rows", [])
    if len(rows) != 8:
        raise RuntimeError("Parent review must contain exactly eight approved DDS rows.")
    parent_by_slot = {}
    for item in rows:
        runtime_name = Path(item["runtime"]).name
        parts = runtime_name.split("_", 2)
        slot = parts[1] if len(parts) > 1 else ""
        if slot not in SLOTS or slot in parent_by_slot:
            raise RuntimeError(f"Unexpected or duplicate parent-review slot: {slot}")
        stem = f"leader_{slot}_warlord_north_america"
        candidate_rel = f"docs/assets/014_cannibalism/portrait_finals_2026-10-03/north_america/candidate_dds/{stem}.dds"
        runtime_rel = f"gfx/leaders/014_cannibalism/{stem}.dds"
        if item["candidate"].replace("\\", "/") != candidate_rel or item["runtime"].replace("\\", "/") != runtime_rel:
            raise RuntimeError(f"Parent review path mismatch for {slot}")
        candidate = ROOT / candidate_rel
        runtime = ROOT / runtime_rel
        candidate_bytes = candidate.read_bytes()
        runtime_bytes = runtime.read_bytes()
        candidate_hash = sha(candidate_bytes)
        runtime_hash = sha(runtime_bytes)
        if candidate_hash.casefold() != item["candidate_sha256"].casefold():
            raise RuntimeError(f"Candidate DDS no longer matches parent approval for {slot}")
        if runtime_hash.casefold() != item["runtime_before_sha256"].casefold():
            raise RuntimeError(f"Runtime DDS changed after parent review for {slot}; refusing to replace")
        parent_by_slot[slot] = {
            "candidate": candidate,
            "runtime": runtime,
            "candidate_sha256": candidate_hash,
            "runtime_before_sha256": runtime_hash,
        }
    if set(parent_by_slot) != set(SLOTS):
        raise RuntimeError("Parent review is missing one or more North America slots.")

    source_snapshot = json.loads(SOURCE_PHASE_SNAPSHOT.read_text(encoding="utf-8"))
    root_posix = ROOT.as_posix().rstrip("/").casefold()
    source_hashes = {}
    for item in source_snapshot["files"]:
        if not item.get("exists"):
            continue
        source_path = item["path"].replace("\\", "/")
        if source_path.casefold().startswith(root_posix + "/"):
            source_path = source_path[len(root_posix) + 1 :]
        source_hashes[source_path.casefold()] = item["sha256"].casefold()
    for slot, item in parent_by_slot.items():
        rel = item["runtime"].relative_to(ROOT).as_posix()
        if source_hashes.get(rel.casefold()) != item["runtime_before_sha256"].casefold():
            raise RuntimeError(f"Source-phase baseline mismatch for {slot}")

    # This all-60 snapshot is taken immediately before the eight backups/install writes.
    before = snapshot("Immediately before authorized North America eight-file install")
    before_hashes = {item["path"]: item["sha256"].casefold() for item in before["runtime_dds"]}
    for slot, item in parent_by_slot.items():
        rel = item["runtime"].relative_to(ROOT).as_posix()
        if before_hashes.get(rel) != item["runtime_before_sha256"].casefold():
            raise RuntimeError(f"Immediate all-60 snapshot mismatch for {slot}")
    write_json(PRE_SNAPSHOT, before)

    BACKUP_DIR.mkdir(parents=True, exist_ok=False)
    backups = []
    for slot in SLOTS:
        item = parent_by_slot[slot]
        backup = BACKUP_DIR / item["runtime"].name
        shutil.copy2(item["runtime"], backup)
        backup_bytes = backup.read_bytes()
        if sha(backup_bytes).casefold() != item["runtime_before_sha256"].casefold():
            raise RuntimeError(f"North America backup verification failed for {slot}")
        backups.append({
            "path": backup.relative_to(ROOT).as_posix(),
            "bytes": len(backup_bytes),
            "sha256": sha(backup_bytes),
        })

    installed = []
    for slot in SLOTS:
        item = parent_by_slot[slot]
        shutil.copyfile(item["candidate"], item["runtime"])
        result = item["runtime"].read_bytes()
        result_hash = sha(result)
        if result != item["candidate"].read_bytes() or result_hash.casefold() != item["candidate_sha256"].casefold():
            raise RuntimeError(f"Installed bytes do not exactly match approved candidate for {slot}")
        installed.append({
            "slot": slot,
            "candidate": item["candidate"].relative_to(ROOT).as_posix(),
            "runtime": item["runtime"].relative_to(ROOT).as_posix(),
            "bytes": len(result),
            "candidate_sha256": item["candidate_sha256"],
            "runtime_before_sha256": item["runtime_before_sha256"],
            "runtime_after_sha256": result_hash,
            "runtime_exactly_equals_approved_candidate": True,
        })

    after = snapshot("Immediately after authorized North America eight-file install")
    after_hashes = {item["path"]: item["sha256"].casefold() for item in after["runtime_dds"]}
    authorized = {item["runtime"].relative_to(ROOT).as_posix() for item in parent_by_slot.values()}
    changed = []
    for rel, before_hash in before_hashes.items():
        after_hash = after_hashes.get(rel)
        if after_hash != before_hash:
            changed.append({
                "path": rel,
                "before_sha256": before_hash,
                "after_sha256": after_hash,
                "classification": "authorized North America replacement" if rel in authorized else "concurrent change outside this tranche; preserved",
            })
    added = sorted(set(after_hashes) - set(before_hashes))
    deleted = sorted(set(before_hashes) - set(after_hashes))
    registry_unchanged = before["portrait_registry"]["sha256"] == after["portrait_registry"]["sha256"]
    characters_unchanged = before["character_definition"]["sha256"] == after["character_definition"]["sha256"]
    write_json(POST_SNAPSHOT, after)
    receipt = {
        "status": "PASS: the eight exact parent-approved candidate DDS byte streams are installed at their existing North America runtime paths",
        "captured_utc": now_utc(),
        "authorization": "Parent final source/framing/native DDS review within the accepted 56-portrait scope; no new user-specific art decision is claimed.",
        "parent_review": PARENT_REVIEW.relative_to(ROOT).as_posix(),
        "preinstall_snapshot": PRE_SNAPSHOT.relative_to(ROOT).as_posix(),
        "postinstall_snapshot": POST_SNAPSHOT.relative_to(ROOT).as_posix(),
        "runtime_dds_count_before": before["runtime_dds_count"],
        "runtime_dds_count_after": after["runtime_dds_count"],
        "backups": backups,
        "installed": installed,
        "other_52_runtime_dds_unchanged": len(changed) == 8 and not added and not deleted,
        "additional_runtime_dds_changes": [item for item in changed if item["classification"] != "authorized North America replacement"],
        "runtime_dds_added_during_install": added,
        "runtime_dds_deleted_during_install": deleted,
        "portrait_registry_unchanged": registry_unchanged,
        "portrait_registry_before_sha256": before["portrait_registry"]["sha256"],
        "portrait_registry_after_sha256": after["portrait_registry"]["sha256"],
        "character_definition_unchanged": characters_unchanged,
        "character_definition_before_sha256": before["character_definition"]["sha256"],
        "character_definition_after_sha256": after["character_definition"]["sha256"],
        "changed_runtime_dds": changed,
        "runtime_install_scope": "Only the eight approved North America DDS paths above were written. No GFX, character, gameplay, localisation, event or other-region path was written.",
        "commit_created": False,
    }
    write_json(RECEIPT, receipt)
    print(json.dumps({
        "receipt": RECEIPT.relative_to(ROOT).as_posix(),
        "runtime_dds_count_before": before["runtime_dds_count"],
        "runtime_dds_count_after": after["runtime_dds_count"],
        "installed": installed,
        "changed_runtime_dds": changed,
        "portrait_registry_unchanged": registry_unchanged,
        "character_definition_unchanged": characters_unchanged,
    }, indent=2))


if __name__ == "__main__":
    main()
