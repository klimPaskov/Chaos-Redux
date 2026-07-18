"""Task-specific audit for the Event 015 final icon and frame package."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import struct
from collections import Counter
from pathlib import Path

from PIL import Image


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[4]
ASSET_ROOT = REPO_ROOT / "docs/assets/015_utopia_manifesto"
GFX_FILE = REPO_ROOT / "interface/015_utopia_manifesto.gfx"
FOCUS_FILE = REPO_ROOT / "common/national_focus/015_utopia_manifesto_focus_tree.txt"
IDEA_FILE = REPO_ROOT / "common/ideas/015_utopia_manifesto_ideas.txt"
ACHIEVEMENT_FILE = REPO_ROOT / "common/achievements/chaos_redux_achievements.txt"
DECISION_FILES = [
    REPO_ROOT / "common/decisions/015_utopia_manifesto_decisions.txt",
    REPO_ROOT / "common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt",
    REPO_ROOT / "common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt",
]
CATEGORY_FILE = (
    REPO_ROOT / "common/decisions/categories/015_utopia_manifesto_categories.txt"
)
GUI_FILE = REPO_ROOT / "interface/015_utopia_manifesto_ledger.gui"
SCRIPTED_GUI_FILE = (
    REPO_ROOT / "common/scripted_guis/015_utopia_manifesto_scripted_gui.txt"
)
EFFECTS_FILE = REPO_ROOT / "common/scripted_effects/015_utopia_manifesto_effects.txt"
DECISION_EFFECTS_FILE = (
    REPO_ROOT / "common/scripted_effects/015_utopia_manifesto_decision_effects.txt"
)
CONSTANTS_FILE = REPO_ROOT / "common/script_constants/015_utopia_manifesto_constants.txt"
DECISION_CONSTANTS_FILE = (
    REPO_ROOT / "common/script_constants/015_utopia_manifesto_decision_constants.txt"
)
EVENT_FILE = REPO_ROOT / "events/015_utopia_manifesto.txt"
MAPPING_FILE = ASSET_ROOT / "decision_icon_mapping.csv"
REPORT_FILE = ASSET_ROOT / "final_icon_frame_audit.json"

CURRENT_ACHIEVEMENTS = [
    "utopia_manifesto_no_place_but_home",
    "utopia_manifesto_need_not_greed",
    "utopia_manifesto_every_calling_chosen",
    "utopia_manifesto_two_year_table",
    "utopia_manifesto_archipelago_of_small_places",
    "utopia_manifesto_inland_island",
    "utopia_manifesto_gold_for_common_use",
    "utopia_manifesto_the_joke_understood",
    "utopia_manifesto_consent_of_the_governed",
    "utopia_manifesto_the_perfect_measure",
    "utopia_manifesto_closed_circle",
    "utopia_manifesto_no_foreign_hands",
    "utopia_manifesto_the_stores_remain",
    "utopia_manifesto_no_one_in_chains",
]

NEW_DECISION_SPRITES = [
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
    "decision_utopia_archipelago_network",
]

NEW_IDEA_SPRITES = [
    "idea_utopia_unmeasured_country",
    "idea_utopia_inherited_order",
    "idea_utopia_charter_of_households",
    "idea_utopia_common_table",
    "idea_utopia_perfect_measure",
    "idea_utopia_closed_island",
    "idea_utopia_practical_commonwealth",
    "idea_utopia_garden_district_network",
    "idea_utopia_auxiliary_dependency",
    "idea_utopia_stewardship_burden",
]

ANIMATIONS = {
    "utopia_need_warning": {
        "frame_size": (64, 64),
        "count": 8,
        "fps": 5,
        "static_index": 4,
        "purpose": "critical Need warning",
    },
    "utopia_reserve_fill": {
        "frame_size": (300, 24),
        "count": 8,
        "fps": 4,
        "static_index": 4,
        "purpose": "public reserve fill",
    },
    "utopia_balance_to_choice": {
        "frame_size": (158, 24),
        "count": 8,
        "fps": 5,
        "static_index": 7,
        "looping": "no",
        "purpose": "public-band crossing toward Choice",
        "source_glob": "utopia_balance_to_choice_*_source.png",
        "processed_glob": "utopia_balance_to_choice_[0-9][0-9][0-9].png",
    },
    "utopia_balance_to_assignment": {
        "frame_size": (158, 24),
        "count": 8,
        "fps": 5,
        "static_index": 7,
        "looping": "no",
        "purpose": "public-band crossing toward Assignment",
        "source_glob": "utopia_balance_to_assignment_*_source.png",
        "processed_glob": "utopia_balance_to_assignment_[0-9][0-9][0-9].png",
    },
    "utopia_formation_ready_seal": {
        "frame_size": (96, 96),
        "count": 10,
        "fps": 5,
        "static_index": 5,
        "purpose": "formation-ready proof",
    },
}

LEDGER_STATIC_FAMILIES = {
    "value_icons": {
        "size": (32, 32),
        "purpose": "compact public Ledger values",
        "stems": [
            "utopia_ledger_value_need",
            "utopia_ledger_value_plenty",
            "utopia_ledger_value_concord",
            "utopia_ledger_value_balance",
        ],
    },
    "calling_icons": {
        "size": (48, 48),
        "purpose": "six occupational Calling families",
        "stems": [
            "utopia_ledger_calling_provisioning",
            "utopia_ledger_calling_workshops",
            "utopia_ledger_calling_civic_works",
            "utopia_ledger_calling_learning_and_care",
            "utopia_ledger_calling_maritime_and_settlement",
            "utopia_ledger_calling_defense_and_watches",
        ],
    },
    "case_cards": {
        "size": (300, 96),
        "purpose": "Necessary Ground target and negotiation state",
        "stems": [
            "utopia_ledger_case_no_target",
            "utopia_ledger_case_target_eligible",
            "utopia_ledger_case_target_selected",
            "utopia_ledger_case_offer_pending",
            "utopia_ledger_case_counteroffer",
            "utopia_ledger_case_refusal",
            "utopia_ledger_case_ultimatum_available",
            "utopia_ledger_case_expired",
            "utopia_ledger_case_stewardship_active",
            "utopia_ledger_case_associate_established",
        ],
    },
    "district_roles": {
        "size": (300, 96),
        "purpose": "seven settlement and island district roles",
        "stems": [
            "utopia_ledger_district_role_market_garden",
            "utopia_ledger_district_role_industrial_housing",
            "utopia_ledger_district_role_rail_junction",
            "utopia_ledger_district_role_port_town",
            "utopia_ledger_district_role_research_town",
            "utopia_ledger_district_role_refugee_municipality",
            "utopia_ledger_district_role_inland_island_ring",
        ],
    },
    "district_states": {
        "size": (48, 48),
        "purpose": "survey, plan, build, blockage, completion, and dispute state",
        "stems": [
            "utopia_ledger_district_state_surveyed",
            "utopia_ledger_district_state_planned",
            "utopia_ledger_district_state_building",
            "utopia_ledger_district_state_blocked",
            "utopia_ledger_district_state_complete",
            "utopia_ledger_district_state_disputed",
        ],
    },
}


def fail(message: str) -> None:
    raise AssertionError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dds_info(path: Path) -> dict[str, int]:
    data = path.read_bytes()
    if len(data) < 128 or data[:4] != b"DDS ":
        fail(f"Invalid DDS header: {path}")
    return {
        "size": len(data),
        "header_size": struct.unpack_from("<I", data, 4)[0],
        "flags": struct.unpack_from("<I", data, 8)[0],
        "height": struct.unpack_from("<I", data, 12)[0],
        "width": struct.unpack_from("<I", data, 16)[0],
        "pitch": struct.unpack_from("<I", data, 20)[0],
        "pixel_format_size": struct.unpack_from("<I", data, 76)[0],
        "pixel_format_flags": struct.unpack_from("<I", data, 80)[0],
        "fourcc": struct.unpack_from("<I", data, 84)[0],
        "rgb_bits": struct.unpack_from("<I", data, 88)[0],
        "r_mask": struct.unpack_from("<I", data, 92)[0],
        "g_mask": struct.unpack_from("<I", data, 96)[0],
        "b_mask": struct.unpack_from("<I", data, 100)[0],
        "a_mask": struct.unpack_from("<I", data, 104)[0],
        "caps": struct.unpack_from("<I", data, 108)[0],
    }


def require_dds(path: Path, expected: tuple[int, int], strict_bgra: bool = False) -> None:
    if not path.is_file():
        fail(f"Missing DDS: {path}")
    info = dds_info(path)
    if (info["width"], info["height"]) != expected:
        fail(
            f"DDS dimension mismatch for {path}: "
            f"{info['width']}x{info['height']} != {expected[0]}x{expected[1]}"
        )
    if strict_bgra:
        expected_fields = {
            "header_size": 124,
            "pitch": expected[0] * 4,
            "pixel_format_size": 32,
            "pixel_format_flags": 0x41,
            "fourcc": 0,
            "rgb_bits": 32,
            "r_mask": 0x00FF0000,
            "g_mask": 0x0000FF00,
            "b_mask": 0x000000FF,
            "a_mask": 0xFF000000,
            "caps": 0x1000,
            "size": 128 + expected[0] * expected[1] * 4,
        }
        for key, value in expected_fields.items():
            if info[key] != value:
                fail(f"DDS field mismatch for {path}: {key}={info[key]} != {value}")


def parse_gfx() -> tuple[dict[str, dict[str, str]], list[str]]:
    text = GFX_FILE.read_text(encoding="utf-8-sig")
    block_pattern = re.compile(
        r"(?P<kind>frameAnimatedSpriteType|spriteType)\s*=\s*\{(?P<body>.*?)^\s*\}",
        re.MULTILINE | re.DOTALL,
    )
    definitions: dict[str, dict[str, str]] = {}
    duplicates: list[str] = []
    for match in block_pattern.finditer(text):
        body = match.group("body")
        name_match = re.search(r'name\s*=\s*"([^"]+)"', body)
        texture_match = re.search(r'texturefile\s*=\s*"([^"]+)"', body)
        if not name_match or not texture_match:
            continue
        name = name_match.group(1)
        if name in definitions:
            duplicates.append(name)
        data = {
            "kind": match.group("kind"),
            "texture": texture_match.group(1),
        }
        for field in [
            "noOfFrames",
            "animation_rate_fps",
            "looping",
            "play_on_show",
            "alwaystransparent",
        ]:
            field_match = re.search(rf"{field}\s*=\s*([^\s#]+)", body)
            if field_match:
                data[field] = field_match.group(1)
        definitions[name] = data
    return definitions, duplicates


def require_sprite(
    definitions: dict[str, dict[str, str]],
    name: str,
    expected_path: str | None = None,
) -> dict[str, str]:
    if name not in definitions:
        fail(f"Missing sprite definition: {name}")
    data = definitions[name]
    if expected_path and data["texture"] != expected_path:
        fail(f"Sprite path mismatch for {name}: {data['texture']} != {expected_path}")
    texture = REPO_ROOT / data["texture"]
    if not texture.is_file():
        fail(f"Sprite texture missing for {name}: {texture}")
    return data


def audit_focus(definitions: dict[str, dict[str, str]]) -> dict[str, int]:
    text = FOCUS_FILE.read_text(encoding="utf-8-sig")
    usages = re.findall(r"\bicon\s*=\s*(GFX_goal_utopia_[a-z0-9_]+)", text)
    unique = sorted(set(usages))
    for sprite in unique:
        data = require_sprite(definitions, sprite)
        require_sprite(definitions, f"{sprite}_shine")
        require_dds(REPO_ROOT / data["texture"], (94, 86))
    physical = list((REPO_ROOT / "gfx/interface/goals/015_utopia_manifesto").glob("*.dds"))
    return {
        "usage_count": len(usages),
        "unique_sprite_count": len(unique),
        "physical_dds_count": len(physical),
        "surplus_physical_count": len(physical) - len(unique),
    }


def audit_ideas(definitions: dict[str, dict[str, str]]) -> dict[str, int]:
    text = IDEA_FILE.read_text(encoding="utf-8-sig")
    pictures = re.findall(r'^\s*picture\s*=\s*"?([a-z0-9_]+)"?', text, re.MULTILINE)
    unique = sorted(set(pictures))
    for token in unique:
        stem = f"idea_{token}"
        expected = f"gfx/interface/ideas/015_utopia_manifesto/{stem}.dds"
        require_sprite(definitions, f"GFX_{stem}", expected)
        require_dds(REPO_ROOT / expected, (64, 64))
    for stem in NEW_IDEA_SPRITES:
        require_dds(
            REPO_ROOT / f"gfx/interface/ideas/015_utopia_manifesto/{stem}.dds",
            (64, 64),
            strict_bgra=True,
        )
    return {
        "entry_count": len(pictures),
        "unique_picture_count": len(unique),
        "new_exact_sprite_count": len(NEW_IDEA_SPRITES),
    }


def audit_mapping(definitions: dict[str, dict[str, str]]) -> dict[str, int]:
    with MAPPING_FILE.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    counts = Counter(row["entry_type"] for row in rows)
    decision_text = "\n".join(
        path.read_text(encoding="utf-8-sig") for path in DECISION_FILES
    )
    source_entries = set(
        re.findall(
            r"^\s+((?:decision|mission)_[a-z0-9_]+)\s*=\s*\{",
            decision_text,
            re.MULTILINE,
        )
    )
    source_categories = set(
        re.findall(
            r"^([a-z0-9_]+_category)\s*=\s*\{",
            CATEGORY_FILE.read_text(encoding="utf-8-sig"),
            re.MULTILINE,
        )
    )
    mapped_entries = {
        row["script_id"] for row in rows if row["entry_type"] != "category"
    }
    mapped_categories = {
        row["script_id"] for row in rows if row["entry_type"] == "category"
    }
    if mapped_entries != source_entries:
        fail(
            "Decision mapping/source drift: "
            f"missing={sorted(source_entries - mapped_entries)}, "
            f"stale={sorted(mapped_entries - source_entries)}"
        )
    if mapped_categories != source_categories:
        fail(
            "Category mapping/source drift: "
            f"missing={sorted(source_categories - mapped_categories)}, "
            f"stale={sorted(mapped_categories - source_categories)}"
        )
    if len({row["script_id"] for row in rows}) != len(rows):
        fail("Duplicate script_id in decision icon mapping")
    for row in rows:
        if row["sprite_name"] != row["icon_value"]:
            fail(f"Mapping icon mismatch: {row['script_id']}")
        require_sprite(definitions, row["sprite_name"], row["asset_file"])
        require_dds(REPO_ROOT / row["asset_file"], (32, 32))
    for stem in NEW_DECISION_SPRITES:
        require_dds(
            REPO_ROOT / f"gfx/interface/decisions/015_utopia_manifesto/{stem}.dds",
            (32, 32),
            strict_bgra=True,
        )
    icon_assignment_count = len(
        re.findall(r"^\s*icon\s*=", decision_text, re.MULTILINE)
    )
    return {
        "mapping_row_count": len(rows),
        "category_count": counts["category"],
        "decision_count": counts["decision"],
        "mission_count": counts["mission"],
        "gameplay_icon_assignment_count": icon_assignment_count,
    }


def audit_achievements(definitions: dict[str, dict[str, str]]) -> dict[str, int]:
    text = ACHIEVEMENT_FILE.read_text(encoding="utf-8-sig")
    overlay = Image.open(
        REPO_ROOT
        / ".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png"
    ).convert("RGBA")
    current = re.findall(
        r"^(utopia_manifesto_[a-z0-9_]+)\s*=\s*\{",
        text,
        re.MULTILINE,
    )
    if current != CURRENT_ACHIEVEMENTS:
        fail(f"Achievement id drift: {current}")
    for achievement_id in CURRENT_ACHIEVEMENTS:
        grey_png = ASSET_ROOT / f"processed_png/final_icons/achievement_{achievement_id}_grey.png"
        not_png = ASSET_ROOT / (
            f"processed_png/final_icons/achievement_{achievement_id}_not_eligible.png"
        )
        if not grey_png.is_file() or not not_png.is_file():
            fail(f"Missing processed achievement variants for {achievement_id}")
        grey_image = Image.open(grey_png).convert("RGBA")
        not_image = Image.open(not_png).convert("RGBA")
        expected_not_eligible = Image.alpha_composite(grey_image, overlay)
        if not_image.tobytes() != expected_not_eligible.tobytes():
            fail(f"Mandated not-eligible overlay mismatch: {achievement_id}")
        for suffix in ["", "_grey", "_not_eligible"]:
            stem = f"{achievement_id}{suffix}"
            runtime = REPO_ROOT / f"gfx/achievements/{stem}.dds"
            staged = ASSET_ROOT / f"dds/final_icons/{stem}.dds"
            require_dds(runtime, (64, 64), strict_bgra=True)
            require_dds(staged, (64, 64), strict_bgra=True)
            if sha256(runtime) != sha256(staged):
                fail(f"Achievement staging mismatch: {stem}")
            require_sprite(
                definitions,
                f"GFX_achievement_{stem}",
                f"gfx/achievements/{stem}.dds",
            )
    legacy = list((REPO_ROOT / "gfx/achievements").glob("015_utopia_*.dds"))
    return {
        "achievement_count": len(CURRENT_ACHIEVEMENTS),
        "exact_variant_count": len(CURRENT_ACHIEVEMENTS) * 3,
        "retained_legacy_variant_count": len(legacy),
    }


def audit_animations(definitions: dict[str, dict[str, str]]) -> dict[str, dict]:
    results: dict[str, dict] = {}
    for name, spec in ANIMATIONS.items():
        base = ASSET_ROOT / "animations" / name
        source_frames = sorted(
            (base / "source_frames").glob(
                spec.get("source_glob", f"{name}_source_*.png")
            )
        )
        processed_frames = sorted(
            (base / "processed_frames").glob(
                spec.get("processed_glob", f"{name}_frame_*.png")
            )
        )
        if len(source_frames) != spec["count"] or len(processed_frames) != spec["count"]:
            fail(f"Frame-count mismatch for {name}")
        if len({sha256(path) for path in source_frames}) != spec["count"]:
            fail(f"Source frames are not all distinct for {name}")
        if len({sha256(path) for path in processed_frames}) != spec["count"]:
            fail(f"Processed frames are not all distinct for {name}")
        frame_images = [Image.open(path).convert("RGBA") for path in processed_frames]
        if any(image.size != spec["frame_size"] for image in frame_images):
            fail(f"Processed-frame dimensions differ for {name}")

        sheet_png = base / f"sheets/{name}_sheet.png"
        static_png = base / f"sheets/{name}_static.png"
        sheet = Image.open(sheet_png).convert("RGBA")
        frame_width, frame_height = spec["frame_size"]
        expected_sheet_size = (frame_width * spec["count"], frame_height)
        if sheet.size != expected_sheet_size:
            fail(f"Sheet PNG dimensions differ for {name}")
        for index, frame in enumerate(frame_images):
            extracted = sheet.crop(
                (index * frame_width, 0, (index + 1) * frame_width, frame_height)
            )
            if extracted.tobytes() != frame.tobytes():
                fail(f"Sheet frame mismatch for {name} frame {index}")
        static = Image.open(static_png).convert("RGBA")
        if static.tobytes() != frame_images[spec["static_index"]].tobytes():
            fail(f"Static fallback mismatch for {name}")

        static_runtime = REPO_ROOT / f"gfx/interface/015_utopia_manifesto/{name}_static.dds"
        sheet_runtime = REPO_ROOT / f"gfx/interface/015_utopia_manifesto/{name}_sheet.dds"
        require_dds(static_runtime, spec["frame_size"], strict_bgra=True)
        require_dds(sheet_runtime, expected_sheet_size, strict_bgra=True)

        static_sprite = require_sprite(
            definitions,
            f"GFX_{name}_static",
            f"gfx/interface/015_utopia_manifesto/{name}_static.dds",
        )
        animated = require_sprite(
            definitions,
            f"GFX_{name}_animated",
            f"gfx/interface/015_utopia_manifesto/{name}_sheet.dds",
        )
        if static_sprite["kind"] != "spriteType":
            fail(f"Static fallback is not spriteType: {name}")
        expected_metadata = {
            "kind": "frameAnimatedSpriteType",
            "noOfFrames": str(spec["count"]),
            "animation_rate_fps": str(spec["fps"]),
            "looping": spec.get("looping", "yes"),
            "play_on_show": "yes",
            "alwaystransparent": "yes",
        }
        for field, expected in expected_metadata.items():
            if animated.get(field) != expected:
                fail(f"Animation metadata mismatch for {name}: {field}")

        preview = Image.open(base / f"previews/{name}_preview.gif")
        if getattr(preview, "n_frames", 1) != spec["count"]:
            fail(f"GIF frame-count mismatch for {name}")
        if not (base / f"previews/{name}_contact.png").is_file():
            fail(f"Missing contact sheet for {name}")
        results[name] = {
            "source_frames": len(source_frames),
            "processed_frames": len(processed_frames),
            "frame_size": list(spec["frame_size"]),
            "sheet_size": list(expected_sheet_size),
            "fps": spec["fps"],
            "looping": spec.get("looping", "yes"),
            "purpose": spec["purpose"],
            "static_frame_index": spec["static_index"],
        }
    return results


def audit_ledger_static_assets(
    definitions: dict[str, dict[str, str]],
) -> dict[str, dict[str, object]]:
    gui = GUI_FILE.read_text(encoding="utf-8-sig")
    results: dict[str, dict[str, object]] = {}
    for family, spec in LEDGER_STATIC_FAMILIES.items():
        hashes: list[str] = []
        for stem in spec["stems"]:
            sprite = f"GFX_{stem}"
            texture = f"gfx/interface/015_utopia_manifesto/ledger/{stem}.dds"
            data = require_sprite(definitions, sprite, texture)
            runtime = REPO_ROOT / data["texture"]
            require_dds(runtime, spec["size"], strict_bgra=True)
            hashes.append(sha256(runtime))

            element = stem
            if family in {"value_icons", "calling_icons"}:
                element = f"{stem}_icon"
            if not re.search(
                rf'name\s*=\s*"{element}".*?spriteType\s*=\s*"{sprite}"',
                gui,
                re.DOTALL,
            ):
                fail(f"Missing live Ledger consumer for {stem}")

        if len(hashes) != len(set(hashes)):
            fail(f"Duplicate runtime art inside Ledger family: {family}")
        results[family] = {
            "count": len(spec["stems"]),
            "size": list(spec["size"]),
            "purpose": spec["purpose"],
            "unique_runtime_hashes": len(set(hashes)),
        }
    return results


def audit_ledger_static_bindings() -> dict[str, object]:
    gui = GUI_FILE.read_text(encoding="utf-8-sig")
    scripted_gui = SCRIPTED_GUI_FILE.read_text(encoding="utf-8-sig")
    effects = EFFECTS_FILE.read_text(encoding="utf-8-sig")
    decision_effects = DECISION_EFFECTS_FILE.read_text(encoding="utf-8-sig")
    constants = CONSTANTS_FILE.read_text(encoding="utf-8-sig")
    decision_constants = DECISION_CONSTANTS_FILE.read_text(encoding="utf-8-sig")
    events = EVENT_FILE.read_text(encoding="utf-8-sig")

    for stem in LEDGER_STATIC_FAMILIES["case_cards"]["stems"]:
        if f"{stem}_visible = {{" not in scripted_gui:
            fail(f"Missing case-card visibility binding: {stem}")
        if not re.search(
            rf'name\s*=\s*"{stem}".*?position\s*=\s*\{{\s*x\s*=\s*8\s+y\s*=\s*4\s*\}}',
            gui,
            re.DOTALL,
        ):
            fail(f"Missing or misplaced case-card consumer: {stem}")

    for stem in LEDGER_STATIC_FAMILIES["district_roles"]["stems"]:
        if f"{stem}_visible = {{" not in scripted_gui:
            fail(f"Missing district-role visibility binding: {stem}")
        if not re.search(
            rf'name\s*=\s*"{stem}".*?position\s*=\s*\{{\s*x\s*=\s*334\s+y\s*=\s*4\s*\}}',
            gui,
            re.DOTALL,
        ):
            fail(f"Missing or misplaced district-role consumer: {stem}")

    for stem in LEDGER_STATIC_FAMILIES["district_states"]["stems"]:
        if f"{stem}_visible = {{" not in scripted_gui:
            fail(f"Missing district-state visibility binding: {stem}")
        if not re.search(
            rf'name\s*=\s*"{stem}".*?position\s*=\s*\{{\s*x\s*=\s*578\s+y\s*=\s*12\s*\}}',
            gui,
            re.DOTALL,
        ):
            fail(f"Missing or misplaced district-state consumer: {stem}")

    case_inputs = [
        "utopia_manifesto_case_candidate_targets^num",
        "utopia_manifesto_selected_country_id",
        "utopia_manifesto_case_response_active",
        "utopia_manifesto_case_counteroffer_recorded",
        "utopia_manifesto_case_settlement_refused",
        "utopia_manifesto_case_ultimatum_refused",
        "utopia_manifesto_case_can_issue_ultimatum = yes",
        "utopia_manifesto_case_expired",
        "utopia_manifesto_stewardship_active",
        "utopia_manifesto_first_associate_recognized",
    ]
    for fragment in case_inputs:
        if fragment not in scripted_gui:
            fail(f"Missing live case-card state input: {fragment}")

    role_names = [
        "market_garden",
        "industrial_housing",
        "rail_junction",
        "refugee_municipality",
        "port_town",
        "research_town",
        "inland_island_ring",
    ]
    for index, role in enumerate(role_names, start=1):
        if not re.search(rf"\b{role}\s*=\s*{index}\b", decision_constants):
            fail(f"Missing durable district presentation role: {role}")
        if f"utopia_manifesto_decision_district_role.{role}" not in scripted_gui:
            fail(f"District presentation role is not bound in GUI: {role}")

    presentation_sources = effects + decision_effects + events
    for role in role_names:
        if f"utopia_manifesto_decision_district_role.{role}" not in presentation_sources:
            fail(f"District presentation role is never assigned: {role}")

    if not re.search(r"district_plan_card_days\s*=\s*7", constants):
        fail("Missing centralized seven-day district-plan presentation duration")
    planned_fragments = [
        "utopia_manifesto_district_plan_card_duration = constant:utopia_manifesto_durations.district_plan_card_days",
        "flag = utopia_manifesto_district_plan_committed_recent",
        "days = utopia_manifesto_district_plan_card_duration",
        "clr_country_flag = utopia_manifesto_district_plan_committed_recent",
        "clear_variable = utopia_manifesto_district_visual_role",
    ]
    for fragment in planned_fragments:
        if fragment not in decision_effects:
            fail(f"Missing district presentation lifecycle fragment: {fragment}")

    district_inputs = [
        "utopia_manifesto_district_project_phase",
        "utopia_manifesto_district_plan_committed_recent",
        "utopia_manifesto_district_obligation_dispute_unresolved",
        "utopia_manifesto_district_project_debt",
        "utopia_manifesto_district_site_surveyed",
        "utopia_manifesto_district_project_delayed",
        "utopia_manifesto_district_built",
        "utopia_manifesto_district_chartered",
        "utopia_manifesto_district_obligations_breached",
        "utopia_manifesto_district_project_refused",
        "utopia_manifesto_district_project_lost",
    ]
    joined = scripted_gui + decision_effects
    for fragment in district_inputs:
        if fragment not in joined:
            fail(f"Missing live district-card state input: {fragment}")

    return {
        "status": "pass",
        "case_states": 10,
        "district_roles": 7,
        "district_states": 6,
        "planned_visibility_days": 7,
        "durable_role_variable": "utopia_manifesto_district_visual_role",
        "cleanup": True,
        "recurring_scan": False,
    }


def audit_gui(definitions: dict[str, dict[str, str]]) -> dict[str, int]:
    text = GUI_FILE.read_text(encoding="utf-8-sig")
    refs = sorted(set(re.findall(r'"(GFX_utopia_[a-z0-9_]+)"', text)))
    for ref in refs:
        require_sprite(definitions, ref)
    required = {
        "GFX_utopia_ledger_background_panel",
        "GFX_utopia_ledger_header_plate",
        "GFX_utopia_ledger_seal_animated",
        "GFX_utopia_need_warning_animated",
        "GFX_utopia_reserve_fill_animated",
        "GFX_utopia_balance_to_choice_animated",
        "GFX_utopia_balance_to_assignment_animated",
        "GFX_utopia_formation_ready_seal_animated",
        "GFX_utopia_manifesto_household_congress_emblem",
        "GFX_utopia_manifesto_congress_of_common_tables_emblem",
        "GFX_utopia_manifesto_network_directorate_emblem",
        "GFX_utopia_manifesto_island_hierarchy_emblem",
        "GFX_utopia_manifesto_plural_compact_emblem",
    }
    for spec in LEDGER_STATIC_FAMILIES.values():
        required.update(f"GFX_{stem}" for stem in spec["stems"])
    if set(refs) != required:
        fail(f"Unexpected GUI sprite set: {refs}")
    return {"unique_gui_sprite_refs": len(refs)}


def audit_balance_shift_binding() -> dict[str, object]:
    gui = GUI_FILE.read_text(encoding="utf-8-sig")
    scripted_gui = SCRIPTED_GUI_FILE.read_text(encoding="utf-8-sig")
    effects = EFFECTS_FILE.read_text(encoding="utf-8-sig")
    constants = CONSTANTS_FILE.read_text(encoding="utf-8-sig")

    bindings = {
        "toward_choice": {
            "element": "utopia_ledger_balance_to_choice",
            "sprite": "GFX_utopia_balance_to_choice_animated",
            "visibility": "utopia_ledger_balance_to_choice_visible",
            "flag": "utopia_manifesto_balance_shift_to_choice_recent",
            "comparison": "less_than",
        },
        "toward_assignment": {
            "element": "utopia_ledger_balance_to_assignment",
            "sprite": "GFX_utopia_balance_to_assignment_animated",
            "visibility": "utopia_ledger_balance_to_assignment_visible",
            "flag": "utopia_manifesto_balance_shift_to_assignment_recent",
            "comparison": "greater_than",
        },
    }
    for direction, binding in bindings.items():
        if not re.search(
            rf'name\s*=\s*"{binding["element"]}".*?'
            rf'spriteType\s*=\s*"{binding["sprite"]}".*?'
            r'position\s*=\s*\{\s*x\s*=\s*516\s+y\s*=\s*70\s*\}',
            gui,
            re.DOTALL,
        ):
            fail(f"Missing or misplaced live GUI consumer: {direction}")
        if not re.search(
            rf'{binding["visibility"]}\s*=\s*\{{\s*'
            rf'has_country_flag\s*=\s*{binding["flag"]}\s*\}}',
            scripted_gui,
            re.DOTALL,
        ):
            fail(f"Missing scripted-GUI visibility binding: {direction}")
        if not re.search(
            r'var\s*=\s*utopia_assignment_band\s*'
            r'value\s*=\s*utopia_manifesto_previous_assignment_band\s*'
            rf'compare\s*=\s*{binding["comparison"]}',
            effects,
            re.DOTALL,
        ):
            fail(f"Missing public-band direction comparison: {direction}")
        if not re.search(
            rf'flag\s*=\s*{binding["flag"]}\s*'
            r'days\s*=\s*utopia_manifesto_balance_shift_animation_duration',
            effects,
            re.DOTALL,
        ):
            fail(f"Missing timed visibility flag: {direction}")

    required_effect_fragments = [
        "utopia_manifesto_refresh_balance_shift_animation = {",
        "utopia_manifesto_has_resolved_route = yes",
        "utopia_manifesto_previous_assignment_band = utopia_assignment_band",
        "utopia_manifesto_refresh_balance_shift_animation = yes",
        "clear_variable = utopia_manifesto_previous_assignment_band",
        "clr_country_flag = utopia_manifesto_balance_shift_to_choice_recent",
        "clr_country_flag = utopia_manifesto_balance_shift_to_assignment_recent",
    ]
    for fragment in required_effect_fragments:
        if fragment not in effects:
            fail(f"Missing balance-shift lifecycle fragment: {fragment}")
    if not re.search(r'balance_shift_animation_days\s*=\s*3', constants):
        fail("Missing centralized three-day balance-shift visibility duration")

    return {
        "status": "pass",
        "purpose": "route-resolved public Assignment-band crossing",
        "visibility_days": 3,
        "route_gate": "utopia_manifesto_has_resolved_route",
        "previous_band_capture": "utopia_manifesto_previous_assignment_band",
        "directions": bindings,
        "initialization_suppression": True,
        "runtime_cleanup": True,
        "recurring_scan": False,
    }


def main() -> None:
    definitions, duplicates = parse_gfx()
    if duplicates:
        fail(f"Duplicate sprite names: {duplicates}")
    gfx_text = GFX_FILE.read_text(encoding="utf-8-sig")
    if "gfx/interface/utopia_manifesto/" in gfx_text:
        fail("Stale Event 015 GUI texture path remains in .gfx")

    report = {
        "status": "pass",
        "focus": audit_focus(definitions),
        "ideas": audit_ideas(definitions),
        "decision_mapping": audit_mapping(definitions),
        "achievements": audit_achievements(definitions),
        "animations": audit_animations(definitions),
        "ledger_static_families": audit_ledger_static_assets(definitions),
        "scripted_gui": audit_gui(definitions),
        "balance_shift_binding": audit_balance_shift_binding(),
        "ledger_static_bindings": audit_ledger_static_bindings(),
        "sprite_definition_count": len(definitions),
        "duplicate_sprite_count": len(duplicates),
    }
    REPORT_FILE.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
