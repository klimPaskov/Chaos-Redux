#!/usr/bin/env python3
"""Validate package structure and hashes. This does not test HOI4 gameplay."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def main() -> int:
    manifest = json.loads((ROOT / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))
    for row in manifest["files"]:
        file = ROOT / row["path"]
        check(file.is_file(), f"Missing file: {row['path']}")
        check(hashlib.sha256(file.read_bytes()).hexdigest() == row["sha256"], f"Hash mismatch: {row['path']}")
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.name != "PACKAGE_MANIFEST.json"}
    check(actual == {row["path"] for row in manifest["files"]}, "File inventory differs from manifest")
    goal = (ROOT / "prompts/072_ireland_reclaims_north_goal_prompt.md").read_text(encoding="utf-8").strip()
    check(goal.startswith("/goal "), "Goal prompt does not begin with /goal")
    check(3500 <= len(goal) <= 4000, "Goal prompt length is outside the required range")
    actions = json.loads((ROOT / "specs/decisions/072_action_register.json").read_text(encoding="utf-8"))["actions"]
    check({a["id"] for a in actions} == {f"D{i:02}" for i in range(1, 43)}, "Action coverage must be D01 through D42")
    check(all(0 < len(a["costs"]) <= 4 for a in actions), "Action has an invalid number of cost types")
    check(all(a.get("response_window_days") == 30 for a in actions if a["mode"] == "offer"), "An offer lacks its 30-day response window")
    check(next(a for a in actions if a["id"] == "D03")["costs"] == {"political_power": 50, "support_equipment": 250}, "Extension cost differs from the final contract")
    group_ids: list[str] = []
    for file in (ROOT / "specs/focus_tree").glob("*.md"):
        group_ids.extend(re.findall(r"^## ([UGECTMNA]\d{2}):", file.read_text(encoding="utf-8"), re.M))
    expected = {f"{lane}{i:02}" for lane, count in {"U": 8, "G": 7, "E": 9, "C": 9, "T": 8, "M": 9, "N": 7, "A": 8}.items() for i in range(1, count + 1)}
    check(set(group_ids) == expected and len(group_ids) == 65, "Focus group coverage is incomplete or duplicated")
    assets = json.loads((ROOT / "specs/presentation/072_asset_manifest.json").read_text(encoding="utf-8"))["rows"]
    check(len({a["asset_id"] for a in assets}) == len(assets), "Duplicate asset ID")
    check({a["consumer"] for a in assets if a["family"] == "decision"} == {a["id"] for a in actions}, "Decision asset coverage mismatch")
    check(len([a for a in assets if a["family"] == "achievement_triplet"]) == 10, "Achievement icon coverage mismatch")
    source = json.loads((ROOT / "research/072_supplied_source_ledger.json").read_text(encoding="utf-8"))
    check(source["text_source_count"] == 42 and source["subagent_profile_count"] == 20, "Source count mismatch")
    check(source["all_packet_ids_logged"] and all(f["logged_packet_coverage"] for f in source["files"]), "Supplied reading coverage is incomplete")
    for file in ROOT.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        check("\u2014" not in text and ";" not in text, f"Prose punctuation constraint failed in {file.name}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            check((file.parent / local).resolve().exists(), f"Broken link in {file.relative_to(ROOT)}: {target}")
    print(json.dumps({"status": "passed", "kind": "planning_package_structure_not_gameplay", "manifested_files": len(manifest["files"]), "focus_groups": len(group_ids), "actions": len(actions), "asset_planning_rows": len(assets), "goal_characters_without_trailing_newline": len(goal), "supplied_text_files": source["text_source_count"], "subagent_profiles": source["subagent_profile_count"]}, indent=2))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"Package validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
