"""Capture pre-install Africa and Hannibal hashes against the October 3 baseline."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


MOD_ROOT = Path(__file__).resolve().parents[6]
PACKAGE = Path(__file__).resolve().parents[1]
REFERENCE = (
    MOD_ROOT
    / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/evidence/runtime_preinstall_snapshot.json"
)
GFX = MOD_ROOT / "interface/014_cannibalism.gfx"
PROTECTED = (
    "gfx/leaders/014_cannibalism/hannibal.dds",
    "gfx/leaders/014_cannibalism/hannibal_wendigo.dds",
    "gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds",
    "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds",
)
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    snapshot = json.loads(REFERENCE.read_text(encoding="utf-8"))
    expected = {row["Path"].replace("\\", "/"): row for row in snapshot["dds"]}
    runtime_root = MOD_ROOT / "gfx/leaders/014_cannibalism"
    gfx_text = GFX.read_text(encoding="utf-8-sig")

    africa_rows = []
    for slot in SLOTS:
        relative = f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_africa.dds"
        path = MOD_ROOT / relative
        old = expected.get(relative)
        if old is None:
            raise ValueError(f"Missing pre-install baseline for {relative}")
        current = file_hash(path)
        if current != old["SHA256"]:
            raise ValueError(f"Existing Africa runtime portrait differs from preserved baseline: {relative}")
        sprite = f"GFX_portrait_{slot}_warlord_africa"
        pattern = rf'spriteType\s*=\s*\{{\s*name\s*=\s*"{re.escape(sprite)}"\s+texturefile\s*=\s*"([^"]+)"\s*\}}'
        matches = re.findall(pattern, gfx_text)
        if matches != [relative]:
            raise ValueError(f"Unexpected existing portrait registration for {slot}: {matches}")
        africa_rows.append(
            {
                "slot": slot,
                "sprite": sprite,
                "runtime_path": relative,
                "expected_dds_sha256": old["SHA256"],
                "current_dds_sha256": current,
                "current_matches_preinstall_baseline": True,
            }
        )

    hannibal_rows = []
    for relative in PROTECTED:
        old = expected.get(relative)
        if old is None:
            raise ValueError(f"Missing protected-file baseline for {relative}")
        current = file_hash(MOD_ROOT / relative)
        if current != old["SHA256"]:
            raise ValueError(f"Protected Hannibal DDS changed from baseline: {relative}")
        hannibal_rows.append(
            {
                "path": relative,
                "expected_sha256": old["SHA256"],
                "current_sha256": current,
                "byte_identical_to_preinstall_baseline": True,
            }
        )

    audit = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "audit_phase": "before_parent_authorized_africa_installation",
        "baseline": REFERENCE.relative_to(MOD_ROOT).as_posix(),
        "baseline_date": snapshot["date"],
        "scope": "read-only runtime/GFX preservation audit for Event 014 Africa portrait candidates",
        "gfx_registry": GFX.relative_to(MOD_ROOT).as_posix(),
        "gfx_registry_sha256": file_hash(GFX),
        "africa_current_runtime_paths_match_baseline": len(africa_rows) == 8,
        "africa_existing_registrations": africa_rows,
        "protected_hannibal_assets_match_baseline": len(hannibal_rows) == 4,
        "protected_hannibal_assets": hannibal_rows,
        "runtime_or_gfx_written_at_preinstall_audit": False,
        "superseded_for_postinstall_state_by": "evidence/runtime_install_receipt.json",
    }
    output = PACKAGE / "route_log/runtime_preservation_audit.json"
    if output.exists():
        raise FileExistsError(f"Refusing to overwrite runtime preservation audit: {output}")
    output.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "audit": output.as_posix(),
                "africa_paths_match": audit["africa_current_runtime_paths_match_baseline"],
                "protected_hannibal_files_match": audit["protected_hannibal_assets_match_baseline"],
                "gfx_sha256": audit["gfx_registry_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
