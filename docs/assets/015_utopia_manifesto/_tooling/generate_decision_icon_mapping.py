"""Regenerate the exact live Event 015 decision/mission/category icon map.

The gameplay files are authoritative. This documentation helper reads every
Event 015 decision package and the category registry, then records each live
``icon =`` assignment without maintaining a second hand-written ID map.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[4]
DECISION_FILES = [
    REPO_ROOT / "common/decisions/015_utopia_manifesto_decisions.txt",
    REPO_ROOT / "common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt",
    REPO_ROOT / "common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt",
]
CATEGORY_FILE = (
    REPO_ROOT / "common/decisions/categories/015_utopia_manifesto_categories.txt"
)
OUTPUT = REPO_ROOT / "docs/assets/015_utopia_manifesto/decision_icon_mapping.csv"

ASSIGNMENT = re.compile(r"^([a-z0-9_]+)\s*=\s*\{")
ICON = re.compile(r"^icon\s*=\s*(GFX_[A-Za-z0-9_]+)$")

IMAGEGEN_FINAL_SPRITES = {
    "decision_category_utopia_district",
    "decision_category_utopia_island",
    "decision_category_utopia_necessary_ground",
    "decision_category_utopia_stewardship",
    "decision_category_utopia_defense",
    "decision_category_utopia_governance",
    "decision_category_utopia_formation",
    "decision_utopia_publish_accounts",
    "decision_utopia_seasonal_reserve",
    "decision_utopia_second_trade",
    "decision_utopia_land_register",
    "decision_utopia_district_survey",
    "decision_utopia_district_foundation",
    "decision_utopia_island_project",
    "decision_utopia_common_harbor",
    "decision_utopia_inland_terminal",
    "decision_utopia_need_case",
    "decision_utopia_purchase",
    "decision_utopia_lease",
    "decision_utopia_joint_administration",
    "decision_utopia_ultimatum",
    "decision_utopia_emergency_provision",
    "decision_utopia_long_integration",
    "decision_utopia_technical_mission",
    "decision_utopia_reserve_compact",
    "decision_utopia_citizen_watch",
    "decision_utopia_engineer_companies",
    "decision_utopia_auxiliary_contract",
    "decision_utopia_constitutional_correction",
    "decision_utopia_formation_proclamation",
}


@dataclass(frozen=True)
class Entry:
    category_id: str
    script_id: str
    sprite_name: str


def strip_comment(line: str) -> str:
    return line.split("#", 1)[0].strip()


def parse_categories() -> list[tuple[str, str]]:
    categories: list[tuple[str, str]] = []
    depth = 0
    current_id: str | None = None
    current_icon: str | None = None

    for raw_line in CATEGORY_FILE.read_text(encoding="utf-8-sig").splitlines():
        code = strip_comment(raw_line)
        before = depth
        assignment = ASSIGNMENT.match(code)
        if before == 0 and assignment:
            current_id = assignment.group(1)
            current_icon = None
        elif before == 1 and current_id:
            icon = ICON.match(code)
            if icon:
                current_icon = icon.group(1)

        depth += code.count("{") - code.count("}")
        if current_id and depth == 0:
            if not current_icon:
                raise ValueError(f"Category has no icon: {current_id}")
            categories.append((current_id, current_icon))
            current_id = None
            current_icon = None

    return categories


def parse_decision_file(path: Path) -> list[Entry]:
    entries: list[Entry] = []
    depth = 0
    current_category: str | None = None
    current_id: str | None = None
    current_icon: str | None = None

    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        code = strip_comment(raw_line)
        before = depth
        assignment = ASSIGNMENT.match(code)
        if before == 0 and assignment:
            current_category = assignment.group(1)
        elif before == 1 and current_category and assignment:
            identifier = assignment.group(1)
            if identifier.startswith(("decision_", "mission_")):
                current_id = identifier
                current_icon = None
        elif before == 2 and current_id:
            icon = ICON.match(code)
            if icon:
                current_icon = icon.group(1)

        depth += code.count("{") - code.count("}")
        if current_id and depth == 1:
            if not current_icon:
                raise ValueError(f"Entry has no icon in {path.name}: {current_id}")
            entries.append(Entry(current_category or "", current_id, current_icon))
            current_id = None
            current_icon = None
        if depth == 0:
            current_category = None

    return entries


def source_family(sprite_name: str) -> str:
    stem = sprite_name.removeprefix("GFX_")
    if stem == "decision_utopia_archipelago_network":
        return "island_variant_imagegen_2026-07-15"
    if stem in IMAGEGEN_FINAL_SPRITES:
        return "imagegen_final_atlas_2026-07-14"
    return "existing_event_015_final_family"


def asset_file(sprite_name: str) -> str:
    stem = sprite_name.removeprefix("GFX_")
    return f"gfx/interface/decisions/015_utopia_manifesto/{stem}.dds"


def main() -> None:
    categories = parse_categories()
    entries = [entry for path in DECISION_FILES for entry in parse_decision_file(path)]
    category_icons = dict(categories)

    if len(category_icons) != len(categories):
        raise ValueError("Duplicate Event 015 category ID")
    entry_ids = [entry.script_id for entry in entries]
    if len(set(entry_ids)) != len(entry_ids):
        raise ValueError("Duplicate Event 015 decision or mission ID")
    unknown_categories = sorted(
        {entry.category_id for entry in entries} - set(category_icons)
    )
    if unknown_categories:
        raise ValueError(f"Entries use unregistered categories: {unknown_categories}")

    fields = [
        "entry_type",
        "category_id",
        "script_id",
        "sprite_name",
        "icon_value",
        "asset_file",
        "source_family",
    ]
    rows: list[dict[str, str]] = []
    for category_id, sprite_name in categories:
        rows.append(
            {
                "entry_type": "category",
                "category_id": category_id,
                "script_id": category_id,
                "sprite_name": sprite_name,
                "icon_value": sprite_name,
                "asset_file": asset_file(sprite_name),
                "source_family": source_family(sprite_name),
            }
        )
    for entry in entries:
        rows.append(
            {
                "entry_type": (
                    "mission" if entry.script_id.startswith("mission_") else "decision"
                ),
                "category_id": entry.category_id,
                "script_id": entry.script_id,
                "sprite_name": entry.sprite_name,
                "icon_value": entry.sprite_name,
                "asset_file": asset_file(entry.sprite_name),
                "source_family": source_family(entry.sprite_name),
            }
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    mission_count = sum(entry.script_id.startswith("mission_") for entry in entries)
    print(
        f"Wrote {len(rows)} rows: {len(categories)} categories, "
        f"{len(entries) - mission_count} decisions, {mission_count} missions."
    )


if __name__ == "__main__":
    main()
