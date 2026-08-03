"""Read-only audit for the Chaos Redux static HOI4 building contract.

This validator intentionally does not require MESHY_API_KEY, Blender, or a
provider route. It audits the checked-in runtime consumer and the local model
evidence so the building workflow can be verified out of the box.
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
PROFILE_PATH = REPO_ROOT / ".tools" / "3d_pipeline" / "config" / "asset_profiles.json"
GFX_PATH = REPO_ROOT / "gfx" / "entities" / "chaosx_buildings.gfx"
ENTITY_PATH = REPO_ROOT / "gfx" / "entities" / "chaosx_buildings.asset"
BUILDINGS_PATH = REPO_ROOT / "common" / "buildings" / "chaosx_buildings.txt"
SPAWNS_PATH = REPO_ROOT / "common" / "buildings" / "chaosx_3d_model_spawns.txt"
ANCHOR_EFFECT_PATH = REPO_ROOT / "common" / "scripted_effects" / "chaosx_camp_visual_anchor_effects.txt"


ASSETS: dict[str, dict[str, str]] = {
    "biowarfare_facility": {
        "job": "docs/assets/chaos_warfare_system/models_3d/biowarfare_facility",
        "mesh": "biowarfare_facility.mesh",
        "gfx_name": "biowarfare_facility_mesh",
        "proof": "biowarfare_facility_fixed",
        "prepare": "biowarfare_facility_prepare.json",
        "state_building": "biowarfare_facility",
    },
    "cw_facility": {
        "job": "docs/assets/chaos_warfare_system/models_3d/cw_facility",
        "mesh": "cw_facility.mesh",
        "gfx_name": "cw_facility_mesh",
        "proof": "cw_facility_fixed",
        "prepare": "cw_facility_prepare.json",
        "state_building": "cw_facility",
    },
    "chaosx_concentration_camp": {
        "job": "docs/assets/system_camp_repression_rework/models_3d/concentration_camp_building",
        "mesh": "chaosx_concentration_camp.mesh",
        "gfx_name": "chaosx_concentration_camp_mesh",
        "proof": "chaosx_concentration_camp_fixed",
        "prepare": "chaosx_concentration_camp_prepare.json",
        "state_building": "concentration_camp",
    },
    "chaosx_extermination_camp": {
        "job": "docs/assets/system_camp_repression_rework/models_3d/extermination_camp_building",
        "mesh": "chaosx_extermination_camp.mesh",
        "gfx_name": "chaosx_extermination_camp_mesh",
        "proof": "chaosx_extermination_camp_fixed",
        "prepare": "chaosx_extermination_camp_prepare.json",
        "state_building": "extermination_camp",
    },
}


def read_json(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.is_file():
        errors.append(f"missing JSON evidence: {path.relative_to(REPO_ROOT)}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON evidence {path.relative_to(REPO_ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON evidence is not an object: {path.relative_to(REPO_ROOT)}")
        return {}
    return value


def clausewitz_block(text: str, marker: str) -> str | None:
    start = text.find(marker)
    if start < 0:
        return None
    opening = text.find("{", start)
    if opening < 0:
        return None
    depth = 0
    for index in range(opening, len(text)):
        character = text[index]
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def require_pattern(text: str, pattern: str, label: str, errors: list[str]) -> None:
    if not re.search(pattern, text, flags=re.MULTILINE):
        errors.append(f"{label}: missing {pattern!r}")


def dds_dimensions(path: Path, errors: list[str]) -> tuple[int, int] | None:
    try:
        header = path.read_bytes()[:128]
    except OSError as exc:
        errors.append(f"cannot read DDS {path.relative_to(REPO_ROOT)}: {exc}")
        return None
    if len(header) < 128 or header[:4] != b"DDS ":
        errors.append(f"invalid DDS header: {path.relative_to(REPO_ROOT)}")
        return None
    height, width = struct.unpack_from("<II", header, 12)
    return width, height


def validate_model(asset_id: str, asset: dict[str, str], profile: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    job = REPO_ROOT / asset["job"]
    stem = Path(asset["mesh"]).stem
    gfx_block = clausewitz_block(GFX_PATH.read_text(encoding="utf-8"), f'name = "{asset["gfx_name"]}"')
    if gfx_block is None:
        errors.append(f"{asset_id}: missing GFX pdxmesh block")
    else:
        require_pattern(gfx_block, r"\bscale\s*=\s*0\.6\b", f"{asset_id} GFX scale", errors)
        require_pattern(gfx_block, r'name\s*=\s*"Mesh_0\.001"', f"{asset_id} meshsettings object name", errors)
        require_pattern(gfx_block, r'shader\s*=\s*"PdxMeshAdvancedSnow"', f"{asset_id} map shader", errors)

    runtime_root = REPO_ROOT / "gfx" / "models" / "buildings"
    runtime_files = [
        runtime_root / asset["mesh"],
        runtime_root / f"{stem}_diffuse.dds",
        runtime_root / f"{stem}_specular.dds",
        runtime_root / f"{stem}_normal.dds",
    ]
    dds_sizes: dict[str, list[int]] = {}
    for path in runtime_files:
        if not path.is_file():
            errors.append(f"{asset_id}: missing runtime file {path.relative_to(REPO_ROOT)}")
        elif path.suffix.casefold() == ".dds":
            dimensions = dds_dimensions(path, errors)
            if dimensions:
                dds_sizes[path.name] = list(dimensions)
                max_dimension = int(profile.get("texture_max_dimension", 1024))
                if max(dimensions) > max_dimension:
                    errors.append(
                        f"{asset_id}: DDS {path.name} exceeds {max_dimension}px: {dimensions}"
                    )

    prepare = read_json(job / "blender" / "reports" / asset["prepare"], errors)
    reference = profile.get("vanilla_reference", {})
    calibration = prepare.get("runtime_calibration", {})
    expected_source_height = float(reference.get("mesh_height_m", 0.0))
    expected_entity_scale = float(reference.get("entity_scale", 0.0))
    if abs(float(calibration.get("mesh_target_height_m", 0.0)) - expected_source_height) > 0.01:
        errors.append(f"{asset_id}: preparation is not calibrated to the building profile source height")
    if abs(float(calibration.get("entity_scale", 0.0)) - expected_entity_scale) > 0.001:
        errors.append(f"{asset_id}: preparation entity scale does not match the building profile")
    footprint = prepare.get("runtime_footprint", {})
    max_footprint = float(profile.get("footprint", {}).get("max_runtime_footprint_m", 4.0))
    actual_footprint = footprint.get("runtime_footprint_after_fit_m")
    if actual_footprint is None:
        errors.append(f"{asset_id}: prepare report has no runtime footprint evidence")
    elif float(actual_footprint) > max_footprint + 0.01:
        errors.append(
            f"{asset_id}: runtime footprint {actual_footprint} exceeds {max_footprint}m"
        )
    geometry = prepare.get("geometry", {})
    hard_max = int(profile.get("triangle_range", {}).get("hard_max", 60000))
    if geometry.get("triangles", 0) > hard_max:
        errors.append(f"{asset_id}: pre-export triangles exceed hard max {hard_max}")

    proof = read_json(job / "validation" / f'reimport_{asset["proof"]}.json', errors)
    meshes = proof.get("meshes", [])
    if not any(mesh.get("name") == "Mesh_0.001" for mesh in meshes if isinstance(mesh, dict)):
        errors.append(f"{asset_id}: reimport proof does not contain Mesh_0.001")
    welded = proof.get("geometry", {}).get("position_welded_topology", {})
    for metric in ("loose_boundary_edges", "non_manifold_edges", "degenerate_faces"):
        if welded.get(metric, 0) != 0:
            errors.append(f"{asset_id}: reimport welded topology has {metric}={welded.get(metric)}")

    for report_name, channel_checks in (
        ("pdx_material_pack.json", {"R": 0, "G": 32}),
        ("pdx_normal_pack.json", {"R": 0, "B": 0}),
    ):
        report = read_json(job / "blender" / "reports" / report_name, errors)
        stats = report.get("channel_stats", {})
        for channel, expected_max in channel_checks.items():
            actual_max = stats.get(channel, {}).get("max")
            if actual_max != expected_max:
                errors.append(
                    f"{asset_id}: {report_name} channel {channel} max {actual_max}, expected {expected_max}"
                )

    return {
        "runtime_files": [str(path.relative_to(REPO_ROOT)).replace("\\", "/") for path in runtime_files],
        "dds_dimensions": dds_sizes,
        "runtime_footprint_after_fit_m": actual_footprint,
        "reimport_meshes": meshes,
    }


def validate_placement(errors: list[str]) -> None:
    buildings = BUILDINGS_PATH.read_text(encoding="utf-8")
    spawns = SPAWNS_PATH.read_text(encoding="utf-8") if SPAWNS_PATH.is_file() else ""
    entities = ENTITY_PATH.read_text(encoding="utf-8")
    anchor_effect = ANCHOR_EFFECT_PATH.read_text(encoding="utf-8") if ANCHOR_EFFECT_PATH.is_file() else ""

    for building, spawn in (
        ("biowarfare_facility", "chaosx_biowarfare_facility_spawn"),
        ("cw_facility", "chaosx_cw_facility_spawn"),
    ):
        block = clausewitz_block(buildings, f"{building} =")
        if block is None:
            errors.append(f"placement: missing building {building}")
        else:
            require_pattern(block, rf"spawn_point\s*=\s*{spawn}", f"placement {building} spawn", errors)
            if "special_project_facility_spawn" in block:
                errors.append(f"placement {building}: uses the shared special-project spawn")

    for building in ("concentration_camp", "extermination_camp"):
        block = clausewitz_block(buildings, f"{building} =")
        if block is None:
            errors.append(f"placement: missing state building {building}")
            continue
        for key in ("spawn_point", "show_on_map", "show_on_map_meshes", "has_destroyed_mesh"):
            if re.search(rf"\b{key}\s*=", block):
                errors.append(f"placement {building}: state building still owns {key}")

    for building in ("concentration_camp_site", "extermination_camp_site"):
        block = clausewitz_block(buildings, f"{building} =")
        if block is None:
            errors.append(f"placement: missing provincial anchor {building}")
            continue
        require_pattern(block, r"spawn_point\s*=\s*chaosx_camp_visual_anchor_spawn", f"placement {building} spawn", errors)
        require_pattern(block, r"province_max\s*=\s*1", f"placement {building} province cap", errors)
        require_pattern(block, r"state_max\s*=\s*1", f"placement {building} state cap", errors)
        require_pattern(block, r"show_on_map\s*=\s*1", f"placement {building} map visibility", errors)

    for spawn in (
        "chaosx_biowarfare_facility_spawn",
        "chaosx_cw_facility_spawn",
        "chaosx_camp_visual_anchor_spawn",
    ):
        block = clausewitz_block(spawns, f"{spawn} =")
        if block is None:
            errors.append(f"placement: missing dedicated spawn {spawn}")
        else:
            require_pattern(block, r"type\s*=\s*province", f"placement {spawn} type", errors)
            require_pattern(block, r"max\s*=\s*1", f"placement {spawn} cap", errors)

    for entity in ("building_concentration_camp_site", "building_extermination_camp_site"):
        if f'name = "{entity}"' not in entities:
            errors.append(f"placement: missing entity {entity}")
    for building in ("concentration_camp_site", "extermination_camp_site"):
        if f"construct_building_in_random_province = {{ {building} = 1 }}" not in anchor_effect:
            errors.append(f"placement: anchor helper does not construct {building} randomly")
    if "province = { all_provinces = yes }" not in anchor_effect:
        errors.append("placement: anchor cleanup does not select all provinces explicitly")
    if (REPO_ROOT / "map" / "buildings.txt").exists():
        errors.append("placement: map/buildings.txt exists; scripted placement must remain authoritative")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asset", choices=["all", *ASSETS], default="all")
    parser.add_argument("--all", action="store_true", dest="all_assets", help="audit all registered building consumers")
    args = parser.parse_args()
    all_assets = args.all_assets or args.asset == "all"
    selected = list(ASSETS) if all_assets else [args.asset]
    errors: list[str] = []
    profile_data = read_json(PROFILE_PATH, errors)
    profile = profile_data.get("profiles", {}).get("building", {})
    if not profile:
        errors.append("missing building asset profile")
    else:
        reference = profile.get("vanilla_reference", {})
        if reference.get("mesh") != "gfx/models/buildings/facility_land.mesh":
            errors.append("building profile must name the installed facility_land mesh")
        if reference.get("entity") != "building_land_facility":
            errors.append("building profile must name the building_land_facility entity")
        if abs(float(reference.get("entity_scale", 0.0)) - 0.6) > 0.001:
            errors.append("building profile must use the installed land-facility entity scale 0.6")
        if abs(float(reference.get("mesh_height_m", 0.0)) - 3.4697628021) > 0.01:
            errors.append("building profile must use the measured facility_land source height")
        if profile.get("materials", {}).get("shader") != "PdxMeshAdvancedSnow":
            errors.append("building profile must use the installed map-building Snow shader")
        if float(profile.get("footprint", {}).get("max_runtime_footprint_m", 0)) <= 0:
            errors.append("building profile has no positive runtime footprint ceiling")
    if not GFX_PATH.is_file():
        errors.append(f"missing GFX file: {GFX_PATH.relative_to(REPO_ROOT)}")
    if not BUILDINGS_PATH.is_file():
        errors.append(f"missing building definitions: {BUILDINGS_PATH.relative_to(REPO_ROOT)}")
    if all_assets:
        validate_placement(errors)
    results = {asset_id: validate_model(asset_id, ASSETS[asset_id], profile, errors) for asset_id in selected}
    report = {"status": "pass" if not errors else "fail", "assets": results, "errors": errors}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
