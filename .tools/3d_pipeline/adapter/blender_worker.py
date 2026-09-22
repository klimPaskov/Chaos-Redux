"""Blender-side implementation for structured adapter operations.

This file is invoked only by the allowlisted adapter. It receives a validated
request file and emits one JSON result line for the adapter to return.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

ADAPTER_ROOT = Path(__file__).resolve().parent
if str(ADAPTER_ROOT) not in sys.path:
    sys.path.insert(0, str(ADAPTER_ROOT))

import bpy
import bmesh
from mathutils import Matrix, Quaternion, Vector
from mathutils.bvhtree import BVHTree
from mathutils.kdtree import KDTree
from normalization_convergence import evaluate_convergence_step


PREVIEW_LIGHT_REFERENCE_HEIGHT = 7.3518242835
CREATURE_GROUND_CONTACT_TOLERANCE_M = 0.01
CREATURE_GROUND_CONTACT_CLEARANCE_M = 0.001
LOCATOR_REGISTRY_VERSION = 1
# Blender's single-precision bone-parent round-trip accumulates ~1.05e-5 of
# matrix error on the repository's validated 0.0386299416 uniform runtime
# armature scale. Keep the guard tight while allowing that measured scale
# conversion error; the locator operation still records and validates the
# actual transform matrices after the round-trip.
LOCATOR_TRANSFORM_TOLERANCE = 2e-5


def shortest_quaternion_angle(left: Quaternion, right: Quaternion) -> float:
    """Return the shortest rotation angle while treating q and -q as equivalent."""

    left_normalized = left.normalized()
    right_normalized = right.normalized()
    dot = abs(float(left_normalized.dot(right_normalized)))
    return 2.0 * math.acos(max(-1.0, min(1.0, dot)))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", default=os.environ.get("CHAOSX_WORKER_REQUEST"))
    parser.add_argument("--io-pdx-root", default=os.environ.get("CHAOSX_IO_PDX_ROOT"))
    args, _ = parser.parse_known_args()
    return args


def safe_name(value: str) -> str:
    result = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    if not result:
        raise ValueError("A non-empty safe name is required.")
    return result


def within(root: Path, value: str, *, allow_missing: bool = False) -> Path:
    if not value or Path(value).is_absolute() or ":" in value:
        raise ValueError("Worker paths must be relative to the job root.")
    path = (root / value).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"Worker path escaped the job root: {value}") from exc
    if not allow_missing and not path.exists():
        raise FileNotFoundError(path)
    return path


def load_pdx(io_pdx_root: str) -> Dict[str, Any]:
    """Load the locked addon without relying on a UI context."""

    addon_root = Path(io_pdx_root).resolve()
    if not (addon_root / "blender_manifest.toml").exists():
        raise FileNotFoundError(addon_root / "blender_manifest.toml")
    package_parent = addon_root.parent
    if str(package_parent) not in sys.path:
        sys.path.insert(0, str(package_parent))
    try:
        import io_pdx_mesh  # type: ignore
    except ImportError:
        raise RuntimeError(f"Unable to import io_pdx_mesh from {addon_root}")
    if not hasattr(bpy.ops, "io_pdx_mesh") or not hasattr(bpy.ops.io_pdx_mesh, "import_mesh"):
        io_pdx_mesh.register()
    from io_pdx_mesh.pdx_blender.blender_import_export import (  # type: ignore
        PDX_MESHINDEX,
        PDX_SHADER,
        export_animfile,
        export_meshfile,
        import_animfile,
        import_meshfile,
        list_scene_pdx_meshes,
        set_mesh_index,
    )

    return {
        "module": io_pdx_mesh,
        "PDX_MESHINDEX": PDX_MESHINDEX,
        "PDX_SHADER": PDX_SHADER,
        "export_animfile": export_animfile,
        "export_meshfile": export_meshfile,
        "import_animfile": import_animfile,
        "import_meshfile": import_meshfile,
        "list_scene_pdx_meshes": list_scene_pdx_meshes,
        "set_mesh_index": set_mesh_index,
        "manifest": str(addon_root / "blender_manifest.toml"),
    }


def save_blend(path: Path) -> None:
    # Checkpoints are the source of truth for the complete runtime action set.
    # Keep every authored or transferred action across later saves even when
    # Blender's single active action slot is switched during the pipeline.
    for action in bpy.data.actions:
        action.use_fake_user = True
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(path))


def new_collection(name: str) -> bpy.types.Collection:
    existing = bpy.data.collections.get(name)
    if existing is not None:
        for obj in list(existing.objects):
            existing.objects.unlink(obj)
        if existing in bpy.context.scene.collection.children:
            bpy.context.scene.collection.children.unlink(existing)
        bpy.data.collections.remove(existing)
    collection = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(collection)
    return collection


def move_to_collection(obj: bpy.types.Object, collection: bpy.types.Collection) -> None:
    for owner in list(obj.users_collection):
        owner.objects.unlink(obj)
    collection.objects.link(obj)


def clear_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for collection in list(bpy.data.collections):
        if collection.name != "Collection":
            bpy.data.collections.remove(collection)
    default = bpy.data.collections.get("Collection")
    if default is not None:
        for obj in list(default.objects):
            default.objects.unlink(obj)
        bpy.data.collections.remove(default)


def import_candidate(source: Path) -> List[bpy.types.Object]:
    before = set(bpy.data.objects)
    suffix = source.suffix.lower()
    if suffix in {".glb", ".gltf"}:
        bpy.ops.import_scene.gltf(filepath=str(source))
    elif suffix == ".fbx":
        bpy.ops.import_scene.fbx(filepath=str(source))
    elif suffix == ".blend":
        before_actions = set(bpy.data.actions)
        with bpy.data.libraries.load(str(source), link=False) as (data_from, data_to):
            data_to.objects = [name for name in data_from.objects if name]
            data_to.actions = [name for name in data_from.actions if name]
        for obj in data_to.objects:
            if obj is not None:
                bpy.context.scene.collection.objects.link(obj)
        if not [action for action in bpy.data.actions if action not in before_actions]:
            raise RuntimeError(f"Blender appended no actions from provider Blend source {source}")
    else:
        raise ValueError(f"Unsupported provider source format: {source.suffix}")
    imported = [obj for obj in bpy.data.objects if obj not in before]
    if not imported:
        imported = list(bpy.context.selected_objects)
    if not imported:
        raise RuntimeError(f"Blender imported no objects from {source}")
    return imported


def import_geometry_candidate(source: Path) -> List[bpy.types.Object]:
    """Import a bounded geometry source, including an audited local Blend checkpoint.

    Provider animation/model inputs remain limited to FBX and glTF through
    ``import_candidate``.  A dual-source geometry handoff may additionally use
    a job-root-local ``.blend`` checkpoint so an already audited runtime mesh
    can receive weights from a separately licensed source rig without being
    round-tripped through an untracked interchange export.
    """

    if source.suffix.lower() != ".blend":
        return import_candidate(source)

    before = set(bpy.data.objects)
    with bpy.data.libraries.load(str(source), link=False) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects if name]
    for obj in data_to.objects:
        if obj is not None:
            bpy.context.scene.collection.objects.link(obj)
    imported = [obj for obj in bpy.data.objects if obj not in before]
    if not imported:
        raise RuntimeError(f"Blender appended no objects from geometry checkpoint {source}")
    return imported


def import_vanilla_reference(
    job: Path,
    payload: Dict[str, Any],
    pdx: Dict[str, Any],
) -> Optional[Dict[str, Any]]:
    reference = payload.get("vanilla_reference") or {}
    if not reference:
        if payload.get("asset_kind") == "humanoid":
            raise RuntimeError("Humanoid preparation requires an imported vanilla scale reference.")
        return None

    mesh_rel = str(reference.get("mesh_rel", ""))
    reference_path = within(job, mesh_rel)
    before = set(bpy.data.objects)
    pdx["import_meshfile"](
        str(reference_path),
        imp_mesh=True,
        imp_skel=False,
        imp_locs=True,
        join_materials=True,
    )
    imported = [obj for obj in bpy.data.objects if obj not in before]
    if not imported:
        raise RuntimeError(f"io_pdx_mesh imported no objects from vanilla reference {reference_path}.")

    collection = new_collection("00_REFERENCE_VANILLA")
    for obj in imported:
        move_to_collection(obj, collection)
        obj["chaosx_reference_read_only"] = True
        obj.hide_render = True
        obj.hide_set(True)

    main_names = {str(name) for name in reference.get("mesh_object_names", [])}
    excluded_patterns = [str(value).casefold() for value in reference.get("exclude_name_patterns", [])]
    meshes = [obj for obj in imported if obj.type == "MESH"]
    if main_names:
        selected = [obj for obj in meshes if obj.name in main_names]
    else:
        selected = meshes
    selected = [
        obj
        for obj in selected
        if not any(pattern in obj.name.casefold() for pattern in excluded_patterns)
    ]
    if not selected:
        raise RuntimeError(
            "Vanilla reference selection produced no mesh objects: "
            + json.dumps(
                {
                    "available_meshes": [obj.name for obj in meshes],
                    "requested_meshes": sorted(main_names),
                    "excluded_patterns": excluded_patterns,
                },
                sort_keys=True,
            )
        )

    minimum, maximum = world_bounds(selected)
    source_height = maximum.z - minimum.z
    expected_height = float(reference["mesh_height"])
    entity_scale = float(reference["entity_scale"])
    expected_runtime_height = float(reference["runtime_height"])
    measurement_tolerance = max(0.01, expected_height * 0.01)
    if abs(source_height - expected_height) > measurement_tolerance:
        raise RuntimeError(
            f"Vanilla reference height changed: measured {source_height:.6f}, "
            f"expected {expected_height:.6f}, tolerance {measurement_tolerance:.6f}."
        )
    return {
        "mesh_rel": mesh_rel,
        "objects": [obj.name for obj in imported],
        "selected_meshes": [obj.name for obj in selected],
        "excluded_patterns": excluded_patterns,
        "bounds_min": list(minimum),
        "bounds_max": list(maximum),
        "source_mesh_height": source_height,
        "entity_scale": entity_scale,
        "effective_runtime_height": source_height * entity_scale,
        "expected_mesh_height": expected_height,
        "expected_runtime_height": expected_runtime_height,
        "forward_axis": reference.get("forward_axis"),
        "up_axis": reference.get("up_axis"),
        "ground_contact_z": minimum.z,
        "reference_policy": "read_only_vanilla_source_measurement; pilot mesh target may bake its calibrated runtime scale",
        "status": "passed",
    }


def duplicate_hierarchy(
    source_objects: List[bpy.types.Object],
    source_collection: bpy.types.Collection,
    working_collection: bpy.types.Collection,
) -> List[bpy.types.Object]:
    mapping: Dict[bpy.types.Object, bpy.types.Object] = {}
    for source in source_objects:
        duplicate = source.copy()
        if source.data is not None:
            try:
                duplicate.data = source.data.copy()
            except AttributeError:
                pass
        working_collection.objects.link(duplicate)
        mapping[source] = duplicate
        duplicate["chaosx_working"] = True
        duplicate["chaosx_source_object"] = source.name
    for source, duplicate in mapping.items():
        if source.parent in mapping:
            duplicate.parent = mapping[source.parent]
        if duplicate.parent is not None:
            duplicate.matrix_parent_inverse = source.matrix_parent_inverse.copy()
        if source.animation_data and source.animation_data.action:
            duplicate.animation_data_create()
            duplicate.animation_data.action = source.animation_data.action.copy()
            duplicate.animation_data.action.name = f"{source.animation_data.action.name}_WORKING"
    for duplicate in mapping.values():
        for modifier in duplicate.modifiers:
            if modifier.type == "ARMATURE" and modifier.object in mapping:
                modifier.object = mapping[modifier.object]
    for source in source_objects:
        source["chaosx_source_protected"] = True
        source.hide_render = True
        source.hide_set(True)
    return list(mapping.values())


def mesh_objects(working_only: bool = True) -> List[bpy.types.Object]:
    result = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        if working_only and not obj.get("chaosx_working", False):
            continue
        result.append(obj)
    return result


def armatures(working_only: bool = True) -> List[bpy.types.Object]:
    result = []
    for obj in bpy.context.scene.objects:
        if obj.type != "ARMATURE":
            continue
        if working_only and not obj.get("chaosx_working", False):
            continue
        result.append(obj)
    return result


def prepare_pdx_export_transforms() -> Dict[str, Any]:
    """Bake the rig object scale into armature data before io_pdx_mesh export."""

    rigs = armatures()
    if not rigs:
        return require_identity_static_mesh_transforms()
    if len(rigs) != 1:
        raise RuntimeError(
            f"PDX export requires exactly one working armature, found {len(rigs)}."
        )
    rig = rigs[0]
    rig_scale = rig.matrix_world.to_scale()
    if (
        max(rig_scale) - min(rig_scale) > 1e-5
        or min(rig_scale) <= 0.0
    ):
        raise RuntimeError(
            "PDX export requires a positive uniform armature world scale, "
            f"got {tuple(rig_scale)}."
        )
    source_scale = float(sum(rig_scale) / 3.0)
    mesh_world_matrices = {
        obj.name: obj.matrix_world.copy()
        for obj in mesh_objects()
    }
    if abs(source_scale - 1.0) > 1e-6:
        rig.data.transform(Matrix.Scale(source_scale, 4))
        animation_translations = scale_action_location_channels(rig, source_scale)
        rig.scale = (1.0, 1.0, 1.0)
        bpy.context.view_layer.update()
        for obj in mesh_objects():
            obj.matrix_world = mesh_world_matrices[obj.name]
        bpy.context.view_layer.update()
    else:
        animation_translations = scale_action_location_channels(rig, 1.0)
    return {
        "policy": "bake_uniform_armature_object_scale_into_armature_data_and_preserve_mesh_world_transform",
        "armature": rig.name,
        "armature_world_scale_before": list(rig_scale),
        "armature_data_scale_factor": source_scale,
        "animation_translation_channels": animation_translations,
        "armature_world_scale_after": list(rig.matrix_world.to_scale()),
        "mesh_world_scales_after": {
            obj.name: list(obj.matrix_world.to_scale())
            for obj in mesh_objects()
        },
    }


def _export_checkpoint_action_snapshot(action: bpy.types.Action) -> List[Dict[str, Any]]:
    """Capture every keyed value and handle used by the export-coordinate drift guard."""

    records = []
    for fcurve, _ in action_fcurves(action):
        records.append(
            {
                "data_path": fcurve.data_path,
                "array_index": int(fcurve.array_index),
                "keys": [
                    {
                        "co": [float(value) for value in key.co],
                        "handle_left": [float(value) for value in key.handle_left],
                        "handle_right": [float(value) for value in key.handle_right],
                        "interpolation": key.interpolation,
                    }
                    for key in fcurve.keyframe_points
                ],
            }
        )
    return sorted(records, key=lambda item: (item["data_path"], item["array_index"]))


def _export_checkpoint_material_snapshot() -> Dict[str, Any]:
    """Capture working material and image bindings without modifying them."""

    return {
        obj.name: [
            {
                "material": material.name if material is not None else None,
                "images": sorted(
                    [
                        {
                            "name": node.image.name,
                            "filepath": bpy.path.abspath(node.image.filepath),
                        }
                        for node in material.node_tree.nodes
                        if material is not None
                        and material.use_nodes
                        and material.node_tree is not None
                        and node.type == "TEX_IMAGE"
                        and node.image is not None
                    ],
                    key=lambda item: (item["name"], item["filepath"]),
                )
                if material is not None
                else [],
            }
            for material in obj.data.materials
        ]
        for obj in mesh_objects()
    }


def _export_checkpoint_protected_snapshot() -> Dict[str, Any]:
    """Prove that protected source/reference objects remain unchanged."""

    return {
        obj.name: {
            "type": obj.type,
            "data": obj.data.name if obj.data is not None else None,
            "transform": object_transform_record(obj),
        }
        for obj in bpy.context.scene.objects
        if not obj.get("chaosx_working", False)
    }


def _validate_export_coordinate_drift(
    *,
    geometry_before: Dict[str, Any],
    bounds_before: Dict[str, Any],
    mesh_matrices_before: Dict[str, List[List[float]]],
    materials_before: Dict[str, Any],
    protected_before: Dict[str, Any],
    bones_before: Dict[str, Dict[str, Any]],
    action_before: List[Dict[str, Any]],
    action_after: List[Dict[str, Any]],
    source_scale: float,
    tolerance: float = 1e-5,
) -> Dict[str, Any]:
    """Reject any change outside the existing PDX coordinate conversion."""

    geometry_after = geometry_metrics()
    topology_keys = (
        "objects", "vertices", "polygons", "triangles", "loose_boundary_edges",
        "non_manifold_edges", "degenerate_faces", "zero_length_normals", "uv_layers",
    )
    topology_drift = {
        key: {"before": geometry_before[key], "after": geometry_after[key]}
        for key in topology_keys
        if geometry_before[key] != geometry_after[key]
    }
    bounds_after = bounds_record(mesh_objects())
    bounds_delta = max(
        abs(float(after) - float(before))
        for key in ("minimum", "maximum", "dimensions")
        for before, after in zip(bounds_before[key], bounds_after[key])
    )
    mesh_matrix_delta = max(
        (
            abs(float(after) - float(before))
            for obj in mesh_objects()
            for before_row, after_row in zip(mesh_matrices_before[obj.name], obj.matrix_world)
            for before, after in zip(before_row, after_row)
        ),
        default=0.0,
    )
    materials_after = _export_checkpoint_material_snapshot()
    protected_after = _export_checkpoint_protected_snapshot()

    rigs = armatures()
    if len(rigs) != 1:
        raise RuntimeError("Export-coordinate checkpoint lost its unique working armature.")
    rig = rigs[0]
    bones_after = {
        bone.name: {
            "parent": bone.parent.name if bone.parent else None,
            "head": [float(value) for value in bone.head_local],
            "tail": [float(value) for value in bone.tail_local],
        }
        for bone in rig.data.bones
    }
    bone_failures = []
    if set(bones_before) != set(bones_after):
        bone_failures.append("bone-name set changed")
    for name, before in bones_before.items():
        after = bones_after.get(name)
        if after is None:
            continue
        if before["parent"] != after["parent"]:
            bone_failures.append(f"{name}: parent changed")
        expected = [float(value) * source_scale for value in (*before["head"], *before["tail"])]
        observed = [float(value) for value in (*after["head"], *after["tail"])]
        if max(abs(left - right) for left, right in zip(expected, observed)) > tolerance:
            bone_failures.append(f"{name}: rest coordinates drifted outside scale conversion")

    action_failures = []
    if len(action_before) != len(action_after):
        action_failures.append("F-curve count changed")
    for before, after in zip(action_before, action_after):
        if (before["data_path"], before["array_index"]) != (after["data_path"], after["array_index"]):
            action_failures.append("F-curve identity/order changed")
            continue
        if len(before["keys"]) != len(after["keys"]):
            action_failures.append(f"{before['data_path']}[{before['array_index']}]: key count changed")
            continue
        location_curve = "pose.bones[" in before["data_path"] and ".location" in before["data_path"]
        factor = source_scale if location_curve else 1.0
        for index, (left, right) in enumerate(zip(before["keys"], after["keys"])):
            if left["interpolation"] != right["interpolation"]:
                action_failures.append(f"{before['data_path']}[{before['array_index']}]: interpolation changed")
                break
            expected = [
                left["co"][0], left["co"][1] * factor,
                left["handle_left"][0], left["handle_left"][1] * factor,
                left["handle_right"][0], left["handle_right"][1] * factor,
            ]
            observed = [*right["co"], *right["handle_left"], *right["handle_right"]]
            if max(abs(float(a) - float(b)) for a, b in zip(expected, observed)) > tolerance:
                action_failures.append(
                    f"{before['data_path']}[{before['array_index']}]: key {index} drifted"
                )
                break

    failures = []
    if topology_drift:
        failures.append("topology/UV drift")
    if bounds_delta > tolerance:
        failures.append(f"working bounds drift {bounds_delta}")
    if mesh_matrix_delta > tolerance:
        failures.append(f"working mesh matrix drift {mesh_matrix_delta}")
    if materials_before != materials_after:
        failures.append("material/image binding drift")
    if protected_before != protected_after:
        failures.append("protected source/reference drift")
    failures.extend(bone_failures)
    failures.extend(action_failures)
    if failures:
        raise RuntimeError("Export-coordinate checkpoint drift validation failed: " + "; ".join(failures))
    return {
        "status": "pass",
        "tolerance": tolerance,
        "topology_drift": topology_drift,
        "bounds_delta": bounds_delta,
        "mesh_matrix_delta": mesh_matrix_delta,
        "materials_preserved": True,
        "protected_sources_preserved": True,
        "bones_preserved_under_uniform_coordinate_conversion": len(bones_after),
        "action_fcurves_preserved_under_location_coordinate_conversion": len(action_after),
        "geometry_after": geometry_after,
        "bounds_after": bounds_after,
    }


def prepare_export_coordinate_checkpoint(req: Dict[str, Any]) -> Dict[str, Any]:
    """Save an accepted action in the exact coordinate system used by PDX export."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    requested_action = explicit_action_name(payload.get("action_name"), "action_name")
    requested_armature = explicit_safe_name(payload.get("target_armature_name"), "target_armature_name")
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rig, action, frame_start, frame_end = select_armature_and_action(requested_action)
    if rig.name != requested_armature:
        raise RuntimeError(
            f"Export-coordinate checkpoint requires target armature {requested_armature}, found {rig.name}."
        )
    action_source = action_provenance(action)
    geometry_before = geometry_metrics()
    bounds_before = bounds_record(mesh_objects())
    mesh_matrices_before = {
        obj.name: [[float(value) for value in row] for row in obj.matrix_world]
        for obj in mesh_objects()
    }
    materials_before = _export_checkpoint_material_snapshot()
    protected_before = _export_checkpoint_protected_snapshot()
    bones_before = {
        bone.name: {
            "parent": bone.parent.name if bone.parent else None,
            "head": [float(value) for value in bone.head_local],
            "tail": [float(value) for value in bone.tail_local],
        }
        for bone in rig.data.bones
    }
    action_before = _export_checkpoint_action_snapshot(action)
    conversion = prepare_pdx_export_transforms()
    action_after = _export_checkpoint_action_snapshot(action)
    drift = _validate_export_coordinate_drift(
        geometry_before=geometry_before,
        bounds_before=bounds_before,
        mesh_matrices_before=mesh_matrices_before,
        materials_before=materials_before,
        protected_before=protected_before,
        bones_before=bones_before,
        action_before=action_before,
        action_after=action_after,
        source_scale=float(conversion["armature_data_scale_factor"]),
    )
    save_blend(checkpoint)
    bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
    reopened_rig, reopened_action, reopened_start, reopened_end = select_armature_and_action(requested_action)
    if reopened_rig.name != requested_armature or (reopened_start, reopened_end) != (frame_start, frame_end):
        raise RuntimeError("Export-coordinate checkpoint changed target armature or action frame range after reopen.")
    reopened_drift = _validate_export_coordinate_drift(
        geometry_before=geometry_before,
        bounds_before=bounds_before,
        mesh_matrices_before=mesh_matrices_before,
        materials_before=materials_before,
        protected_before=protected_before,
        bones_before=bones_before,
        action_before=action_before,
        action_after=_export_checkpoint_action_snapshot(reopened_action),
        source_scale=float(conversion["armature_data_scale_factor"]),
    )
    if action_provenance(reopened_action) != action_source:
        raise RuntimeError("Export-coordinate checkpoint changed verified action provenance after reopen.")
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "action": reopened_action.name,
        "action_provenance": action_source,
        "target_armature": reopened_rig.name,
        "frame_start": reopened_start,
        "frame_end": reopened_end,
        "fps": bpy.context.scene.render.fps,
        "conversion": conversion,
        "drift_guard_before_save": drift,
        "drift_guard_after_reopen": reopened_drift,
        "policy": "existing_pdx_export_coordinate_conversion_checkpoint_only",
        "body_motion_authored": False,
        "warnings": [],
    }
    report = job / "blender" / "reports" / f"export_coordinate_checkpoint_{safe_name(reopened_action.name)}.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def ensure_material_nodes(material: bpy.types.Material) -> None:
    material.use_nodes = True
    nodes = material.node_tree.nodes
    output = next((node for node in nodes if node.bl_idname == "ShaderNodeOutputMaterial"), None)
    if output is None:
        output = nodes.new("ShaderNodeOutputMaterial")
    shader = next((node for node in nodes if node.bl_idname == "ShaderNodeBsdfPrincipled"), None)
    if shader is None:
        shader = nodes.new("ShaderNodeBsdfPrincipled")
    if not output.inputs["Surface"].is_linked:
        material.node_tree.links.new(shader.outputs["BSDF"], output.inputs["Surface"])


TEXTURE_IMAGE_NAMES = {
    "diffuse": "texture_0",
    "specular": "texture_specular",
    "normal": "texture_normal",
}

STATIC_TEXTURE_IMAGE_NAMES = {
    "diffuse": "Image_0",
    "specular": "Image_1",
    "normal": "Image_2",
}


def _principled_shader(material: bpy.types.Material) -> bpy.types.Node:
    ensure_material_nodes(material)
    shader = next(
        (node for node in material.node_tree.nodes if node.bl_idname == "ShaderNodeBsdfPrincipled"),
        None,
    )
    if shader is None:
        raise RuntimeError(f"Material has no Principled shader after node setup: {material.name}")
    return shader


def _load_texture_image(path: Path, name: str, *, non_color: bool) -> bpy.types.Image:
    # glTF imports often leave packed images with the same conventional names
    # used by the runtime handoff (Image_0/Image_1/Image_2). Reusing one keeps
    # the old packed pixels even after changing its filepath, so the export can
    # silently retain the provider's unprocessed normal/spec layout. Replace
    # the name collision and load the explicit source file instead.
    image = bpy.data.images.get(name)
    if image is not None:
        bpy.data.images.remove(image, do_unlink=True)
    image = bpy.data.images.load(str(path), check_existing=False)
    image.name = name
    try:
        image.colorspace_settings.name = "Non-Color" if non_color else "sRGB"
    except (AttributeError, TypeError):
        pass
    return image


def _sanitize_pdx_material(material: bpy.types.Material) -> None:
    """Remove glTF-only PBR/emission wiring from the PDX working material."""

    shader = _principled_shader(material)
    for input_name in ("Metallic", "Emission Color", "Emission Strength", "Alpha"):
        socket = shader.inputs.get(input_name)
        if socket is None:
            continue
        for link in list(socket.links):
            material.node_tree.links.remove(link)
        if input_name == "Metallic":
            socket.default_value = 0.0
        elif input_name == "Emission Strength":
            socket.default_value = 0.0
    allowed_nodes = {
        "CHAOSX_DIFFUSE_TEXTURE",
        "CHAOSX_SPECULAR_TEXTURE",
        "CHAOSX_NORMAL_TEXTURE",
    }
    for node in list(material.node_tree.nodes):
        if node.bl_idname == "ShaderNodeTexImage" and node.name not in allowed_nodes:
            material.node_tree.nodes.remove(node)


def bind_texture_sources(job: Path, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Bind explicit provider maps to the working materials before export."""

    source_rels = payload.get("texture_source_rels") or {}
    if payload.get("asset_kind") in {"humanoid", "creature"} and source_rels:
        required = {"diffuse", "specular", "normal"}
        missing = sorted(required - set(source_rels))
        if missing:
            raise RuntimeError(
                "Humanoid export requires explicit diffuse, specular, and normal texture sources; "
                f"missing {missing}."
            )

    working_meshes = mesh_objects()
    if not working_meshes:
        raise RuntimeError("Texture binding found no working mesh objects.")
    image_names = (
        STATIC_TEXTURE_IMAGE_NAMES
        if payload.get("asset_kind") in {"static", "building", "static_building"}
        else TEXTURE_IMAGE_NAMES
    )
    records: List[Dict[str, Any]] = []
    for role, rel in sorted(source_rels.items()):
        if role not in TEXTURE_IMAGE_NAMES:
            raise RuntimeError(f"Unsupported texture source role: {role}")
        source = within(job, str(rel))
        if not source.exists():
            raise FileNotFoundError(source)
        image = _load_texture_image(
            source,
            image_names[role],
            non_color=role in {"specular", "normal"},
        )
        node_count = 0
        for obj in working_meshes:
            if not obj.data.materials:
                obj.data.materials.append(bpy.data.materials.new("CHAOSX_PdxMeshAdvanced"))
            for material in obj.data.materials:
                if material is None:
                    continue
                _sanitize_pdx_material(material)
                shader = _principled_shader(material)
                node = material.node_tree.nodes.get(f"CHAOSX_{role.upper()}_TEXTURE")
                if node is None:
                    node = material.node_tree.nodes.new("ShaderNodeTexImage")
                    node.name = f"CHAOSX_{role.upper()}_TEXTURE"
                node.image = image
                node.label = f"Chaos Redux {role} texture"
                node_count += 1
                if role == "diffuse":
                    target = shader.inputs.get("Base Color")
                    if target is not None:
                        for link in list(target.links):
                            material.node_tree.links.remove(link)
                        material.node_tree.links.new(node.outputs["Color"], target)
                elif role == "normal":
                    normal_node = material.node_tree.nodes.get("CHAOSX_NORMAL_MAP")
                    if normal_node is None:
                        normal_node = material.node_tree.nodes.new("ShaderNodeNormalMap")
                        normal_node.name = "CHAOSX_NORMAL_MAP"
                    normal_node.inputs["Strength"].default_value = 1.0
                    for link in list(normal_node.inputs["Color"].links):
                        material.node_tree.links.remove(link)
                    material.node_tree.links.new(node.outputs["Color"], normal_node.inputs["Color"])
                    target = shader.inputs.get("Normal")
                    if target is not None:
                        for link in list(target.links):
                            material.node_tree.links.remove(link)
                        material.node_tree.links.new(normal_node.outputs["Normal"], target)
                elif role == "specular":
                    # io_pdx_mesh 0.91 reads the Blender Roughness input when
                    # emitting the PDX material's `spec` texture slot. The
                    # engine-side specular map is therefore bound here, not to
                    # Blender's scalar specular-IOR control.
                    target = shader.inputs.get("Roughness")
                    if target is not None:
                        for link in list(target.links):
                            material.node_tree.links.remove(link)
                        material.node_tree.links.new(node.outputs["Color"], target)
        records.append(
            {
                "role": role,
                "image": image.name,
                "source": str(source.relative_to(job)).replace("\\", "/"),
                "node_bindings": node_count,
                "size": [int(image.size[0]), int(image.size[1])],
            }
        )
    return records


def tag_pdx_materials(pdx: Dict[str, Any]) -> Dict[str, Any]:
    material_names: List[str] = []
    for index, obj in enumerate(mesh_objects()):
        pdx["set_mesh_index"](obj.data, index)
        for material in obj.data.materials:
            if material is None:
                continue
            ensure_material_nodes(material)
            material[pdx["PDX_SHADER"]] = "PdxMeshAdvanced"
            material["chaosx_pdx_shader"] = "PdxMeshAdvanced"
            if material.name not in material_names:
                material_names.append(material.name)
        obj["chaosx_export_approved"] = True
    return {"materials": material_names, "shader": "PdxMeshAdvanced"}


def action_fcurves(action: bpy.types.Action) -> Iterable[Tuple[Any, Any]]:
    """Yield action F-curves from both legacy and Blender 5 layered actions."""

    legacy = getattr(action, "fcurves", None)
    if legacy is not None:
        for fcurve in legacy:
            yield fcurve, legacy
        return
    for layer in getattr(action, "layers", []):
        for strip in getattr(layer, "strips", []):
            for channelbag in getattr(strip, "channelbags", []):
                fcurves = getattr(channelbag, "fcurves", None)
                if fcurves is None:
                    continue
                for fcurve in fcurves:
                    yield fcurve, fcurves


def scale_action_location_channels(rig: bpy.types.Object, factor: float) -> Dict[str, Any]:
    """Scale keyed local bone translations when armature data is rescaled."""

    action = rig.animation_data.action if rig.animation_data else None
    if action is None or abs(factor - 1.0) <= 1e-6:
        return {
            "action": action.name if action is not None else None,
            "factor": factor,
            "location_fcurves": 0,
            "keyframes": 0,
            "policy": "no_action_scale_required",
        }
    changed_curves = 0
    changed_keyframes = 0
    for fcurve, _ in action_fcurves(action):
        if "pose.bones[" not in fcurve.data_path or ".location" not in fcurve.data_path:
            continue
        changed_curves += 1
        for keyframe in fcurve.keyframe_points:
            keyframe.co[1] *= factor
            keyframe.handle_left[1] *= factor
            keyframe.handle_right[1] *= factor
            changed_keyframes += 1
        fcurve.update()
    return {
        "action": action.name,
        "factor": factor,
        "location_fcurves": changed_curves,
        "keyframes": changed_keyframes,
        "policy": "scale_local_bone_translation_channels_with_armature_data_bake",
    }


def sanitize_action_scale_channels() -> Dict[str, Any]:
    """Remove provider scale channels that rescale the whole unit in HOI4."""

    records: List[Dict[str, Any]] = []

    for rig in armatures():
        action = rig.animation_data.action if rig.animation_data else None
        if action is None:
            continue
        all_fcurves = list(action_fcurves(action))
        removable = [
            (fcurve, owner)
            for fcurve, owner in all_fcurves
            if "scale" in fcurve.data_path.casefold()
        ]
        paths = [fcurve.data_path for fcurve, _ in removable]
        for fcurve, owner in removable:
            owner.remove(fcurve)
        reset_bones = []
        for pose_bone in rig.pose.bones:
            if any(abs(value - 1.0) > 1e-5 for value in pose_bone.scale):
                reset_bones.append(pose_bone.name)
            pose_bone.scale = (1.0, 1.0, 1.0)
        records.append(
            {
                "armature": rig.name,
                "action": action.name,
                "removed_fcurves": len(removable),
                "removed_paths": paths,
                "reset_pose_scale_bones": reset_bones,
            }
        )
    return {
        "policy": "remove_all_working_action_scale_fcurves",
        "actions": records,
        "remaining_scale_fcurves": sum(
            1
            for rig in armatures()
            if rig.animation_data
            and rig.animation_data.action
            for fcurve, _ in action_fcurves(rig.animation_data.action)
            if "scale" in fcurve.data_path.casefold()
        ),
    }


def world_bounds(objects: Iterable[bpy.types.Object]) -> Tuple[Vector, Vector]:
    corners: List[Vector] = []
    for obj in objects:
        if obj.type != "MESH":
            continue
        # Blender's Object.bound_box can remain stale after provider geometry
        # is triangulated or decimated. Measure the actual mesh vertices so
        # normalization and preview framing cannot silently use old extents.
        corners.extend(obj.matrix_world @ vertex.co for vertex in obj.data.vertices)
    if not corners:
        return Vector((0, 0, 0)), Vector((0, 0, 0))
    minimum = Vector((min(item.x for item in corners), min(item.y for item in corners), min(item.z for item in corners)))
    maximum = Vector((max(item.x for item in corners), max(item.y for item in corners), max(item.z for item in corners)))
    return minimum, maximum


def vector_record(value: Vector) -> List[float]:
    return [float(component) for component in value]


def bounds_record(objects: Iterable[bpy.types.Object]) -> Dict[str, List[float]]:
    minimum, maximum = world_bounds(objects)
    return {
        "minimum": vector_record(minimum),
        "maximum": vector_record(maximum),
        "dimensions": vector_record(maximum - minimum),
    }


def object_transform_record(obj: bpy.types.Object) -> Dict[str, Any]:
    return {
        "location": [float(value) for value in obj.location],
        "rotation_euler": [float(value) for value in obj.rotation_euler],
        "scale": [float(value) for value in obj.scale],
        "matrix_world": [[float(value) for value in row] for row in obj.matrix_world],
    }


def require_identity_static_mesh_transforms(tolerance: float = 1e-7) -> Dict[str, Any]:
    """Fail closed when a static export retains any object-space transform."""

    meshes = mesh_objects()
    if not meshes:
        raise RuntimeError("Static mesh validation found no approved chaosx_working mesh objects.")
    failures = []
    records = []
    for obj in meshes:
        transform = object_transform_record(obj)
        flat_values = [
            *transform["location"],
            *transform["rotation_euler"],
            *transform["scale"],
            *(value for row in transform["matrix_world"] for value in row),
        ]
        if not all(math.isfinite(value) for value in flat_values):
            failures.append(f"{obj.name}: non-finite transform")
        if any(value <= 0.0 for value in transform["scale"]):
            failures.append(f"{obj.name}: non-positive or negative scale {transform['scale']}")
        if any(abs(value) > tolerance for value in transform["location"]):
            failures.append(f"{obj.name}: non-identity location {transform['location']}")
        if any(abs(value) > tolerance for value in transform["rotation_euler"]):
            failures.append(f"{obj.name}: non-identity rotation {transform['rotation_euler']}")
        if any(abs(value - 1.0) > tolerance for value in transform["scale"]):
            failures.append(f"{obj.name}: non-identity scale {transform['scale']}")
        records.append({"object": obj.name, "transform": transform})
    if failures:
        raise RuntimeError("Static PDX export transform validation failed: " + "; ".join(failures))
    return {
        "policy": "static_mesh_identity_transform_required",
        "tolerance": tolerance,
        "objects": records,
    }


def evaluated_world_bounds(objects: Iterable[bpy.types.Object]) -> Tuple[Vector, Vector]:
    """Measure evaluated, armature-deformed mesh vertices at the current frame."""

    corners: List[Vector] = []
    depsgraph = bpy.context.evaluated_depsgraph_get()
    for obj in objects:
        if obj.type != "MESH":
            continue
        evaluated = obj.evaluated_get(depsgraph)
        mesh = evaluated.to_mesh()
        try:
            corners.extend(evaluated.matrix_world @ vertex.co for vertex in mesh.vertices)
        finally:
            evaluated.to_mesh_clear()
    if not corners:
        return Vector((0, 0, 0)), Vector((0, 0, 0))
    minimum = Vector((min(item.x for item in corners), min(item.y for item in corners), min(item.z for item in corners)))
    maximum = Vector((max(item.x for item in corners), max(item.y for item in corners), max(item.z for item in corners)))
    return minimum, maximum


def evaluated_contact_bounds(
    objects: Iterable[bpy.types.Object],
    excluded_bones: Iterable[str],
) -> Tuple[Vector, Vector]:
    """Measure evaluated bounds while ignoring vertices dominated by excluded bones."""

    excluded = {str(name) for name in excluded_bones}
    if not excluded:
        return evaluated_world_bounds(objects)
    corners: List[Vector] = []
    depsgraph = bpy.context.evaluated_depsgraph_get()
    for obj in objects:
        if obj.type != "MESH":
            continue
        evaluated = obj.evaluated_get(depsgraph)
        mesh = evaluated.to_mesh()
        try:
            if len(mesh.vertices) != len(obj.data.vertices):
                raise RuntimeError(
                    f"Contact-filtered grounding requires topology-preserving deformation on {obj.name}."
                )
            group_names = {group.index: group.name for group in obj.vertex_groups}
            for source_vertex, evaluated_vertex in zip(obj.data.vertices, mesh.vertices):
                weighted_groups = [
                    (float(assignment.weight), group_names.get(assignment.group, ""))
                    for assignment in source_vertex.groups
                    if assignment.weight > 0.0
                ]
                dominant_bone = max(weighted_groups, default=(0.0, ""))[1]
                if dominant_bone in excluded:
                    continue
                corners.append(evaluated.matrix_world @ evaluated_vertex.co)
        finally:
            evaluated.to_mesh_clear()
    if not corners:
        raise RuntimeError("Contact-filtered grounding excluded every working mesh vertex.")
    minimum = Vector((min(item.x for item in corners), min(item.y for item in corners), min(item.z for item in corners)))
    maximum = Vector((max(item.x for item in corners), max(item.y for item in corners), max(item.z for item in corners)))
    return minimum, maximum


def root_objects(objects: List[bpy.types.Object]) -> List[bpy.types.Object]:
    object_set = set(objects)
    return [obj for obj in objects if obj.parent not in object_set]


def is_humanoid_asset_kind(asset_kind: str) -> bool:
    """Recognize both legacy and repository job-profile humanoid identifiers."""

    return asset_kind in {"humanoid", "humanoid_unit"}


def normalize_geometry(target_height: float) -> Dict[str, Any]:
    objects = [obj for obj in bpy.context.scene.objects if obj.get("chaosx_working", False)]
    meshes = mesh_objects()
    minimum, maximum = world_bounds(meshes)
    before_height = maximum.z - minimum.z
    if before_height <= 0:
        raise RuntimeError("Candidate has no positive vertical extent.")
    scale = target_height / before_height
    for obj in root_objects(objects):
        obj.scale *= scale
    bpy.context.view_layer.update()
    minimum, maximum = world_bounds(meshes)
    for obj in root_objects(objects):
        obj.location.z -= minimum.z
    bpy.context.view_layer.update()
    return {
        "target_height_m": target_height,
        "scale_factor": scale,
        "bounds_min": list(world_bounds(meshes)[0]),
        "bounds_max": list(world_bounds(meshes)[1]),
        "ground_contact_z": world_bounds(meshes)[0].z,
    }


def verify_saved_normalization(checkpoint: Path, target_height: float) -> Dict[str, Any]:
    """Reopen a checkpoint and fail if its measured height differs from its report."""

    bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
    persisted_geometry = geometry_metrics()
    persisted_height = float(persisted_geometry["dimensions"][2])
    tolerance = max(1e-5, abs(target_height) * 1e-5)
    height_delta = persisted_height - target_height
    if abs(height_delta) > tolerance:
        raise RuntimeError(
            "Saved normalization checkpoint does not preserve the requested mesh height: "
            f"target={target_height}, persisted={persisted_height}, delta={height_delta}."
        )
    return {
        "policy": "save_reopen_and_remeasure_working_world_bounds",
        "checkpoint": str(checkpoint),
        "target_height_m": target_height,
        "persisted_height_m": persisted_height,
        "height_delta_m": height_delta,
        "tolerance_m": tolerance,
        "geometry": persisted_geometry,
        "armatures": [
            {
                "name": rig.name,
                "world_scale": list(rig.matrix_world.to_scale()),
            }
            for rig in armatures()
        ],
    }


def stabilize_saved_normalization(
    checkpoint: Path,
    target_height: float,
) -> Dict[str, Any]:
    """Strictly renormalize a prepared candidate after dependency-graph reload."""

    corrections = []
    previous_delta = None
    max_corrections = 8
    for corrections_applied in range(max_corrections + 1):
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
        persisted_geometry = geometry_metrics()
        persisted_height = float(persisted_geometry["dimensions"][2])
        tolerance = max(1e-5, abs(target_height) * 1e-5)
        step = evaluate_convergence_step(
            target=target_height,
            persisted=persisted_height,
            tolerance=tolerance,
            previous_delta=previous_delta,
            corrections_applied=corrections_applied,
            max_corrections=max_corrections,
        )
        record = {
            "pass": corrections_applied,
            "target_height_m": target_height,
            "persisted_height_m": persisted_height,
            "height_delta_m": step["delta"],
            "correction_factor": step["correction_factor"],
        }
        corrections.append(record)
        if step["status"] == "accepted":
            return {
                "policy": "save_reopen_monotonic_convergence_and_strict_reverify",
                "checkpoint": str(checkpoint),
                "target_height_m": target_height,
                "persisted_height_m": persisted_height,
                "height_delta_m": step["delta"],
                "tolerance_m": tolerance,
                "geometry": persisted_geometry,
                "armatures": [
                    {"name": rig.name, "world_scale": list(rig.matrix_world.to_scale())}
                    for rig in armatures()
                ],
                "dependency_graph_corrections": corrections,
            }
        correction = normalize_geometry(target_height)
        record["normalization"] = correction
        save_blend(checkpoint)
        previous_delta = float(step["delta"])
    raise RuntimeError("Normalization convergence exhausted its correction cap.")


def constrain_runtime_footprint(
    max_runtime_footprint_m: Optional[float],
    runtime_entity_scale: float,
    policy: str,
) -> Dict[str, Any]:
    """Enforce a map-building footprint after source-height calibration.

    A building's height and map footprint are separate runtime contracts. The
    old pipeline checked only height, which allowed a compound-sized Meshy
    result to be rendered as one ordinary HOI4 building. The fit operation is
    explicit and uniform in X/Y; the default is a hard rejection so future
    work cannot silently distort a model.
    """

    if policy not in {"reject", "fit_to_budget"}:
        raise RuntimeError(f"Unsupported runtime footprint policy: {policy}")
    if max_runtime_footprint_m is None:
        return {
            "status": "not_configured",
            "policy": policy,
            "max_runtime_footprint_m": None,
        }
    maximum = float(max_runtime_footprint_m)
    if maximum <= 0.0:
        raise RuntimeError("The runtime building footprint budget must be positive.")
    if runtime_entity_scale <= 0.0:
        raise RuntimeError("Runtime entity scale must be positive for footprint validation.")
    minimum, maximum_bounds = world_bounds(mesh_objects())
    source_dimensions = maximum_bounds - minimum
    runtime_dimensions = source_dimensions * runtime_entity_scale
    current_footprint = max(float(runtime_dimensions.x), float(runtime_dimensions.y))
    record: Dict[str, Any] = {
        "policy": policy,
        "max_runtime_footprint_m": maximum,
        "source_dimensions_before_fit_m": list(source_dimensions),
        "runtime_dimensions_before_fit_m": list(runtime_dimensions),
        "runtime_footprint_before_fit_m": current_footprint,
        "fit_factor_xy": 1.0,
    }
    if current_footprint > maximum + 1e-6:
        if policy != "fit_to_budget":
            raise RuntimeError(
                "Building footprint exceeds its runtime budget: "
                f"{current_footprint:.6f}m > {maximum:.6f}m. "
                "Use an explicit fit_to_budget decision after visual review."
            )
        factor = maximum / current_footprint
        for obj in root_objects(
            [obj for obj in bpy.context.scene.objects if obj.get("chaosx_working", False)]
        ):
            obj.scale.x *= factor
            obj.scale.y *= factor
        bpy.context.view_layer.update()
        minimum, maximum_bounds = world_bounds(mesh_objects())
        source_dimensions = maximum_bounds - minimum
        runtime_dimensions = source_dimensions * runtime_entity_scale
        record["fit_factor_xy"] = factor
        record["fit_applied"] = True
    else:
        record["fit_applied"] = False
    record["source_dimensions_after_fit_m"] = list(source_dimensions)
    record["runtime_dimensions_after_fit_m"] = list(runtime_dimensions)
    record["runtime_footprint_after_fit_m"] = max(
        float(runtime_dimensions.x), float(runtime_dimensions.y)
    )
    if record["runtime_footprint_after_fit_m"] > maximum + 1e-5:
        raise RuntimeError("The explicit building footprint fit did not meet its budget.")
    return record


def triangulate_and_normals() -> Dict[str, Any]:
    changed = []
    for obj in mesh_objects():
        mesh = obj.data
        bm = bmesh.new()
        bm.from_mesh(mesh)
        bmesh.ops.triangulate(bm, faces=list(bm.faces))
        bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
        bm.to_mesh(mesh)
        bm.free()
        mesh.update()
        changed.append(obj.name)
    return {"triangulated_objects": changed}


def controlled_decimate(target_triangles: int) -> Dict[str, Any]:
    """Reduce dense provider geometry only to the profile's approved target."""

    before = geometry_metrics()
    if target_triangles <= 0 or before["triangles"] <= target_triangles:
        return {
            "applied": False,
            "target_triangles": target_triangles,
            "before_triangles": before["triangles"],
            "after_triangles": before["triangles"],
            "reason": "within_target_or_disabled",
        }
    objects = mesh_objects()
    if not objects:
        raise RuntimeError("Controlled decimation found no working mesh.")
    target_for_object = max(100, int(target_triangles / len(objects)))
    details = []
    for obj in objects:
        before_object = sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons)
        current = before_object
        if current <= target_for_object:
            continue
        passes = []
        while current > target_for_object and len(passes) < 8:
            ratio = max(0.01, min(1.0, target_for_object / current))
            bpy.ops.object.select_all(action="DESELECT")
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            modifier = obj.modifiers.new("CHAOSX_BOUNDED_DECIMATE", type="DECIMATE")
            modifier.ratio = ratio
            modifier.use_collapse_triangulate = False
            while obj.modifiers.find(modifier.name) > 0:
                bpy.ops.object.modifier_move_up(modifier=modifier.name)
            bpy.ops.object.modifier_apply(modifier=modifier.name)
            reduced = sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons)
            passes.append(
                {
                    "before_triangles": current,
                    "after_triangles": reduced,
                    "ratio": ratio,
                }
            )
            if reduced >= current:
                raise RuntimeError(
                    f"Controlled decimation stalled for {obj.name}: {current} -> {reduced} triangles."
                )
            current = reduced
        if current > target_for_object:
            raise RuntimeError(
                f"Controlled decimation did not reach the approved target for {obj.name}: "
                f"{current} > {target_for_object} triangles after {len(passes)} passes."
            )
        details.append(
            {
                "object": obj.name,
                "before_triangles": before_object,
                "target_triangles": target_for_object,
                "after_triangles": current,
                "passes": passes,
            }
        )
    triangulate_and_normals()
    after = geometry_metrics()
    if after["triangles"] > target_triangles:
        raise RuntimeError(
            "Controlled decimation exceeded its aggregate approved target: "
            f"{after['triangles']} > {target_triangles} triangles."
        )
    return {
        "applied": True,
        "target_triangles": target_triangles,
        "before_triangles": before["triangles"],
        "after_triangles": after["triangles"],
        "objects": details,
        "method": "bounded iterative Blender DECIMATE collapse followed by explicit triangulation",
    }


def repair_open_surface_boundaries(weld_distance: float = 1e-5) -> Dict[str, Any]:
    """Weld coincident provider seams, then cap only bounded small loops."""

    records: List[Dict[str, Any]] = []
    for obj in mesh_objects():
        before = geometry_metrics_for_object(obj)
        original_data = obj.data.copy()
        bm = bmesh.new()
        bm.from_mesh(obj.data)
        vertices_before_weld = len(bm.verts)
        bmesh.ops.remove_doubles(bm, verts=list(bm.verts), dist=weld_distance)
        welded_vertices = max(0, vertices_before_weld - len(bm.verts))
        bm.verts.index_update()
        bm.edges.index_update()
        duplicate_faces = set()
        for edge in bm.edges:
            if len(edge.link_faces) > 2:
                duplicate_faces.update(edge.link_faces[2:])
        if duplicate_faces:
            bmesh.ops.delete(bm, geom=list(duplicate_faces), context="FACES")
        duplicate_faces_removed = len(duplicate_faces)
        bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
        bm.to_mesh(obj.data)
        obj.data.update()
        welded_metrics = geometry_metrics_for_object(obj)
        welded_data = obj.data.copy()
        weld_rolled_back = welded_metrics["non_manifold_edges"] > before["non_manifold_edges"]
        if weld_rolled_back:
            repaired_data = obj.data
            obj.data = original_data
            if repaired_data.users == 0:
                bpy.data.meshes.remove(repaired_data)
            if welded_data.users == 0:
                bpy.data.meshes.remove(welded_data)
            records.append(
                {
                    "object": obj.name,
                    "boundary_edges_before": before["loose_boundary_edges"],
                    "boundary_edges_after": before["loose_boundary_edges"],
                    "welded_vertices": welded_vertices,
                    "duplicate_faces_removed": duplicate_faces_removed,
                    "welded_boundary_edges": welded_metrics["loose_boundary_edges"],
                    "welded_non_manifold_edges": welded_metrics["non_manifold_edges"],
                    "weld_rolled_back": True,
                    "faces_added": 0,
                    "skipped_components": 0,
                    "rolled_back_non_manifold": True,
                    "non_manifold_edges_before": before["non_manifold_edges"],
                    "non_manifold_edges_after": before["non_manifold_edges"],
                    "triangles_after": before["triangles"],
                }
            )
            continue

        bm.clear()
        bm.from_mesh(obj.data)
        boundary_edges = [edge for edge in bm.edges if len(edge.link_faces) == 1]
        edge_by_id = {id(edge): edge for edge in boundary_edges}
        edges_by_vertex: Dict[int, List[Any]] = {}
        for edge in boundary_edges:
            for vertex in edge.verts:
                edges_by_vertex.setdefault(vertex.index, []).append(edge)
        unvisited = set(edge_by_id)
        components: List[List[Any]] = []
        while unvisited:
            seed_id = next(iter(unvisited))
            stack = [edge_by_id[seed_id]]
            component: List[Any] = []
            while stack:
                edge = stack.pop()
                edge_id = id(edge)
                if edge_id not in unvisited:
                    continue
                unvisited.remove(edge_id)
                component.append(edge)
                for vertex in edge.verts:
                    stack.extend(
                        neighbour
                        for neighbour in edges_by_vertex.get(vertex.index, [])
                        if id(neighbour) in unvisited
                    )
            components.append(component)

        filled_face_count = 0
        skipped_components = 0
        max_bounded_loop_edges = 96
        cap_methods: Dict[str, int] = {}
        component_specs = [
            [tuple(sorted(vertex.index for vertex in edge.verts)) for edge in component]
            for component in components
        ]

        component_rejections = 0
        for component_spec in component_specs:
            vertices = {vertex for edge in component_spec for vertex in edge}
            if (
                len(component_spec) < 3
                or len(component_spec) > max_bounded_loop_edges
                or any(len(edges_by_vertex.get(vertex, [])) != 2 for vertex in vertices)
            ):
                skipped_components += 1
                continue
            candidate_bm = bm.copy()
            candidate_bm.verts.index_update()
            candidate_bm.edges.index_update()
            candidate_edges_by_vertices = {
                frozenset(vertex.index for vertex in edge.verts): edge
                for edge in candidate_bm.edges
            }
            candidate_edges = [
                candidate_edges_by_vertices.get(frozenset(edge))
                for edge in component_spec
            ]
            if any(edge is None for edge in candidate_edges):
                candidate_bm.free()
                skipped_components += 1
                continue
            result = bmesh.ops.holes_fill(
                candidate_bm,
                edges=candidate_edges,
                sides=0,
            ) or {}
            candidate_faces = [face for face in result.get("faces", []) if face.is_valid]
            fill_method = "holes_fill"
            if not candidate_faces:
                result = bmesh.ops.triangle_fill(
                    candidate_bm,
                    edges=candidate_edges,
                    use_beauty=True,
                ) or {}
                candidate_faces = [face for face in result.get("faces", []) if face.is_valid]
                fill_method = "triangle_fill"
            candidate_non_manifold_edges = sum(
                1 for edge in candidate_bm.edges if len(edge.link_faces) > 2
            )
            if candidate_non_manifold_edges > welded_metrics["non_manifold_edges"]:
                candidate_bm.free()
                component_rejections += 1
                skipped_components += 1
                continue
            for face in candidate_faces:
                face.material_index = 0
            bm.free()
            bm = candidate_bm
            filled_face_count += len(candidate_faces)
            cap_methods[fill_method] = cap_methods.get(fill_method, 0) + 1

        degenerate_faces = [face for face in bm.faces if face.calc_area() <= 1e-10]
        if degenerate_faces:
            bmesh.ops.delete(bm, geom=degenerate_faces, context="FACES")
        if filled_face_count or degenerate_faces:
            bmesh.ops.triangulate(bm, faces=list(bm.faces))
            bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
        bm.to_mesh(obj.data)
        bm.free()
        obj.data.update()
        after = geometry_metrics_for_object(obj)
        rolled_back_non_manifold = after["non_manifold_edges"] > welded_metrics["non_manifold_edges"]
        if rolled_back_non_manifold:
            # Keep a valid weld when the optional cap pass creates a bad edge.
            repaired_data = obj.data
            obj.data = welded_data
            if repaired_data.users == 0:
                bpy.data.meshes.remove(repaired_data)
            after = geometry_metrics_for_object(obj)
            filled_face_count = 0
        elif welded_data.users == 0:
            bpy.data.meshes.remove(welded_data)
        if original_data.users == 0:
            bpy.data.meshes.remove(original_data)
        records.append(
            {
                "object": obj.name,
                "boundary_edges_before": before["loose_boundary_edges"],
                "boundary_edges_after": after["loose_boundary_edges"],
                "welded_vertices": welded_vertices,
                "duplicate_faces_removed": duplicate_faces_removed,
                "welded_boundary_edges": welded_metrics["loose_boundary_edges"],
                "welded_non_manifold_edges": welded_metrics["non_manifold_edges"],
                "weld_rolled_back": False,
                "faces_added": filled_face_count,
                "skipped_components": skipped_components,
                "component_rejections": component_rejections,
                "cap_methods": cap_methods,
                "rolled_back_non_manifold": rolled_back_non_manifold,
                "non_manifold_edges_before": before["non_manifold_edges"],
                "degenerate_faces_removed": len(degenerate_faces),
                "non_manifold_edges_after": after["non_manifold_edges"],
                "triangles_after": after["triangles"],
            }
        )
    return {
        "applied": any(record["welded_vertices"] or record["faces_added"] for record in records),
        "method": f"bmesh remove_doubles at {weld_distance:g}, remove duplicate-overlap faces, then bounded holes_fill/triangle_fill on loops up to 96 edges with cap-only non-manifold rollback",
        "objects": records,
    }


def topology_metrics_from_bmesh(bm: bmesh.types.BMesh) -> Dict[str, Any]:
    boundary_edges = [edge for edge in bm.edges if len(edge.link_faces) == 1]
    loose_edges = len(boundary_edges)
    non_manifold_edges = sum(1 for edge in bm.edges if len(edge.link_faces) > 2)
    degenerate_faces = sum(1 for face in bm.faces if face.calc_area() <= 1e-10)
    edges_by_vertex: Dict[int, List[Any]] = {}
    boundary_by_id = {id(edge): edge for edge in boundary_edges}
    for edge in boundary_edges:
        for vertex in edge.verts:
            edges_by_vertex.setdefault(vertex.index, []).append(edge)
    unvisited = set(boundary_by_id)
    boundary_components = []
    while unvisited:
        seed_id = next(iter(unvisited))
        stack = [boundary_by_id[seed_id]]
        component = []
        while stack:
            edge = stack.pop()
            edge_id = id(edge)
            if edge_id not in unvisited:
                continue
            unvisited.remove(edge_id)
            component.append(edge)
            for vertex in edge.verts:
                stack.extend(
                    neighbour
                    for neighbour in edges_by_vertex.get(vertex.index, [])
                    if id(neighbour) in unvisited
                )
        vertices = {vertex.index for edge in component for vertex in edge.verts}
        degrees = [len(edges_by_vertex.get(vertex, [])) for vertex in vertices]
        boundary_components.append(
            {
                "edges": len(component),
                "vertices": len(vertices),
                "closed_simple_cycle": bool(degrees) and all(degree == 2 for degree in degrees),
                "endpoint_vertices": sum(degree == 1 for degree in degrees),
                "branch_vertices": sum(degree > 2 for degree in degrees),
                "max_vertex_degree": max(degrees, default=0),
                "perimeter": sum(edge.calc_length() for edge in component),
            }
        )
    zero_length_normals = sum(1 for face in bm.faces if face.normal.length <= 1e-8)
    return {
        "loose_boundary_edges": loose_edges,
        "non_manifold_edges": non_manifold_edges,
        "degenerate_faces": degenerate_faces,
        "triangles": sum(max(0, len(face.verts) - 2) for face in bm.faces),
        "boundary_component_count": len(boundary_components),
        "closed_boundary_component_count": sum(
            1 for component in boundary_components if component["closed_simple_cycle"]
        ),
        "branched_boundary_component_count": sum(
            1 for component in boundary_components if component["branch_vertices"]
        ),
        "max_boundary_component_edges": max(
            (component["edges"] for component in boundary_components), default=0
        ),
        "zero_length_normals": zero_length_normals,
    }


def geometry_metrics_for_object(obj: bpy.types.Object) -> Dict[str, Any]:
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    result = topology_metrics_from_bmesh(bm)
    bm.free()
    return result


def position_welded_geometry_metrics_for_object(
    obj: bpy.types.Object,
    weld_distance: float,
) -> Dict[str, Any]:
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    vertices_before = len(bm.verts)
    bmesh.ops.remove_doubles(bm, verts=list(bm.verts), dist=weld_distance)
    bm.verts.ensure_lookup_table()
    result = topology_metrics_from_bmesh(bm)
    result["vertices_before"] = vertices_before
    result["vertices_after_position_weld"] = len(bm.verts)
    result["weld_distance"] = weld_distance
    bm.free()
    return result


def geometry_metrics(
    working_only: bool = True,
    position_weld_distance: Optional[float] = None,
) -> Dict[str, Any]:
    meshes = mesh_objects(working_only=working_only)
    vertices = sum(len(obj.data.vertices) for obj in meshes)
    polygons = sum(len(obj.data.polygons) for obj in meshes)
    triangles = sum(sum(max(0, len(poly.vertices) - 2) for poly in obj.data.polygons) for obj in meshes)
    loose_edges = 0
    non_manifold_edges = 0
    degenerate_faces = 0
    boundary_component_count = 0
    closed_boundary_component_count = 0
    branched_boundary_component_count = 0
    max_boundary_component_edges = 0
    zero_length_normals = 0
    position_welded = []
    for obj in meshes:
        object_metrics = geometry_metrics_for_object(obj)
        loose_edges += object_metrics["loose_boundary_edges"]
        non_manifold_edges += object_metrics["non_manifold_edges"]
        degenerate_faces += object_metrics["degenerate_faces"]
        zero_length_normals += object_metrics["zero_length_normals"]
        boundary_component_count += object_metrics["boundary_component_count"]
        closed_boundary_component_count += object_metrics["closed_boundary_component_count"]
        branched_boundary_component_count += object_metrics["branched_boundary_component_count"]
        max_boundary_component_edges = max(
            max_boundary_component_edges, object_metrics["max_boundary_component_edges"]
        )
        if position_weld_distance is not None:
            position_welded.append(
                {
                    "object": obj.name,
                    **position_welded_geometry_metrics_for_object(obj, position_weld_distance),
                }
            )
    minimum, maximum = world_bounds(meshes)
    result = {
        "objects": len(meshes),
        "vertices": vertices,
        "polygons": polygons,
        "triangles": triangles,
        "loose_boundary_edges": loose_edges,
        "non_manifold_edges": non_manifold_edges,
        "degenerate_faces": degenerate_faces,
        "boundary_component_count": boundary_component_count,
        "closed_boundary_component_count": closed_boundary_component_count,
        "branched_boundary_component_count": branched_boundary_component_count,
        "max_boundary_component_edges": max_boundary_component_edges,
        "zero_length_normals": zero_length_normals,
        "bounds_min": list(minimum),
        "bounds_max": list(maximum),
        "dimensions": list(maximum - minimum),
        "negative_scale_objects": [
            obj.name for obj in bpy.context.scene.objects
            if (not working_only or obj.get("chaosx_working", False)) and any(value < 0 for value in obj.scale)
        ],
        "uv_layers": {
            obj.name: [layer.name for layer in obj.data.uv_layers]
            for obj in meshes
        },
    }
    if position_weld_distance is not None:
        result["position_welded_topology"] = {
            "policy": "diagnostic_position_weld_only; exported UV and normal seams remain unchanged",
            "weld_distance": position_weld_distance,
            "objects": position_welded,
            "loose_boundary_edges": sum(item["loose_boundary_edges"] for item in position_welded),
            "non_manifold_edges": sum(item["non_manifold_edges"] for item in position_welded),
            "degenerate_faces": sum(item["degenerate_faces"] for item in position_welded),
        }
    return result


def action_metrics() -> Dict[str, Any]:
    values: List[Dict[str, Any]] = []

    def action_fcurve_count(action: bpy.types.Action) -> int:
        legacy = getattr(action, "fcurves", None)
        if legacy is not None:
            return sum(1 for fcurve in legacy if "scale" in fcurve.data_path.casefold())
        return sum(
            1
            for layer in getattr(action, "layers", [])
            for strip in getattr(layer, "strips", [])
            for channelbag in getattr(strip, "channelbags", [])
            for fcurve in getattr(channelbag, "fcurves", [])
            if "scale" in fcurve.data_path.casefold()
        )

    for action in bpy.data.actions:
        start, end = action.frame_range
        values.append(
            {
                "name": action.name,
                "frame_start": int(math.floor(start)),
                "frame_end": int(math.ceil(end)),
                "frame_count": int(math.ceil(end) - math.floor(start) + 1),
                "fps": bpy.context.scene.render.fps,
                "scale_fcurves": action_fcurve_count(action),
            }
        )
    return {
        "armatures": [
            {"name": obj.name, "bones": len(obj.data.bones)}
            for obj in armatures()
        ],
        "actions": values,
    }


def validate_evaluated_frames(requested_frames, start, end):
    if requested_frames is None:
        return sorted({int(math.floor(start)), int(math.ceil((start + end) * 0.5)), int(math.ceil(end))})
    if not isinstance(requested_frames, list) or not 1 <= len(requested_frames) <= 241:
        raise ValueError("evaluated_frames requires 1..241 explicit frames.")
    if any(type(frame) is not int or frame < math.floor(start) or frame > math.ceil(end) for frame in requested_frames):
        raise ValueError("evaluated_frames must be integers within the selected action range.")
    if len(set(requested_frames)) != len(requested_frames):
        raise ValueError("evaluated_frames must not repeat frames.")
    return sorted(requested_frames)


def evaluated_action_metrics(selected_action_name="", requested_frames=None, target_armature_name="") -> List[Dict[str, Any]]:
    """Read evaluated working-mesh bounds for explicit action/frame selection."""
    if requested_frames is not None and not selected_action_name:
        raise ValueError("evaluated_frames requires an explicit selected action_name.")
    meshes = mesh_objects()
    rigs = [rig for rig in armatures() if not target_armature_name or rig.name == target_armature_name]
    if not meshes or not rigs:
        return []
    scene = bpy.context.scene
    original_frame = scene.frame_current
    original_bindings = []
    records = []
    try:
        for rig in rigs:
            rig.animation_data_create()
            original_bindings.append((rig, rig.animation_data.action, getattr(rig.animation_data, "action_slot", None)))
            if selected_action_name:
                action = bpy.data.actions.get(selected_action_name)
                if action is None: raise ValueError("Selected evaluated action does not exist.")
                actions = [action]
            else:
                actions = [action for action in bpy.data.actions if (("WORKING" in action.name and action.name.startswith("Armature|")) or action.name.startswith("creature_") or action.name.startswith("black_plague_rat_"))]
            for action in actions:
                rig.animation_data.action = action
                frames = validate_evaluated_frames(requested_frames, *action.frame_range)
                frame_records = []
                for frame in frames:
                    scene.frame_set(frame)
                    bpy.context.view_layer.update()
                    depsgraph = bpy.context.evaluated_depsgraph_get()
                    corners = []
                    mesh_bounds = []
                    for obj in meshes:
                        evaluated = obj.evaluated_get(depsgraph)
                        evaluated_mesh = evaluated.to_mesh()
                        try:
                            points = [evaluated.matrix_world @ vertex.co for vertex in evaluated_mesh.vertices]
                            corners.extend(points)
                            if points:
                                mesh_bounds.append({"name": obj.name, "bounds_min": [min(p[i] for p in points) for i in range(3)], "bounds_max": [max(p[i] for p in points) for i in range(3)]})
                        finally:
                            evaluated.to_mesh_clear()
                    if corners:
                        minimum = Vector(tuple(min(p[i] for p in corners) for i in range(3)))
                        maximum = Vector(tuple(max(p[i] for p in corners) for i in range(3)))
                        frame_records.append({"frame": frame, "bounds_min": list(minimum), "bounds_max": list(maximum), "dimensions": list(maximum-minimum), "meshes": mesh_bounds})
                records.append({"armature": rig.name, "action": action.name, "frames": frame_records})
    finally:
        for rig, action, slot in original_bindings:
            rig.animation_data.action = action
            if action is not None and slot is not None: rig.animation_data.action_slot = slot
        scene.frame_set(original_frame)
        bpy.context.view_layer.update()
    return records


def weight_metrics() -> List[Dict[str, Any]]:
    """Report skinning coverage before a runtime export is trusted."""

    records: List[Dict[str, Any]] = []
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        armature_modifiers = [
            modifier
            for modifier in obj.modifiers
            if modifier.type == "ARMATURE" and modifier.object is not None
        ]
        bone_names = set()
        armature_names = []
        for modifier in armature_modifiers:
            armature = modifier.object
            armature_names.append(armature.name)
            bone_names.update(bone.name for bone in armature.data.bones)

        group_names = {group.index: group.name for group in obj.vertex_groups}
        influence_histogram: Dict[str, int] = {}
        zero_weight_vertices = 0
        vertices_over_four = 0
        vertices_with_non_bone_groups = 0
        min_weight_sum = None
        max_weight_sum = None
        for vertex in obj.data.vertices:
            weights = []
            has_non_bone_group = False
            for assignment in vertex.groups:
                group_name = group_names.get(assignment.group)
                if group_name is None:
                    continue
                weight = float(assignment.weight)
                if weight <= 0.0:
                    continue
                weights.append(weight)
                if bone_names and group_name not in bone_names:
                    has_non_bone_group = True
            influence_count = len(weights)
            influence_key = str(influence_count)
            influence_histogram[influence_key] = influence_histogram.get(influence_key, 0) + 1
            if influence_count > 4:
                vertices_over_four += 1
            if has_non_bone_group:
                vertices_with_non_bone_groups += 1
            weight_sum = sum(weights)
            if weight_sum <= 1e-8:
                zero_weight_vertices += 1
            min_weight_sum = weight_sum if min_weight_sum is None else min(min_weight_sum, weight_sum)
            max_weight_sum = weight_sum if max_weight_sum is None else max(max_weight_sum, weight_sum)

        records.append(
            {
                "object": obj.name,
                "vertices": len(obj.data.vertices),
                "armature_modifiers": armature_names,
                "vertex_groups": len(obj.vertex_groups),
                "influence_histogram": dict(sorted(influence_histogram.items(), key=lambda item: int(item[0]))),
                "vertices_over_four_influences": vertices_over_four,
                "zero_weight_vertices": zero_weight_vertices,
                "vertices_with_non_bone_groups": vertices_with_non_bone_groups,
                "weight_sum_min": min_weight_sum,
                "weight_sum_max": max_weight_sum,
            }
        )
    return records


def sanitize_working_weights(
    *,
    preserve_skeleton_metadata: bool = False,
    max_influences_per_vertex: int = 4,
) -> Dict[str, Any]:
    """Enforce PDX influence limits on authored skinning without inventing weights."""

    if max_influences_per_vertex not in {1, 2, 3, 4}:
        raise ValueError("max_influences_per_vertex must be an integer from 1 through 4.")

    records: List[Dict[str, Any]] = []
    unweighted_by_object: Dict[str, int] = {}
    for obj in mesh_objects():
        armature_modifiers = [
            modifier
            for modifier in obj.modifiers
            if modifier.type == "ARMATURE" and modifier.object is not None
        ]
        named_transfer_modifiers = [
            modifier for modifier in armature_modifiers
            if modifier.name == "CHAOSX_RIG_TRANSFER"
        ]
        if len(named_transfer_modifiers) == 1:
            armature_modifier = named_transfer_modifiers[0]
        elif len(armature_modifiers) == 1:
            armature_modifier = armature_modifiers[0]
        elif armature_modifiers:
            raise RuntimeError(
                f"Weight sanitization requires one explicit working armature modifier on {obj.name}; "
                f"found {[modifier.name for modifier in armature_modifiers]}."
            )
        else:
            armature_modifier = None
        if armature_modifier is None:
            continue
        armature = armature_modifier.object
        bone_names = {bone.name for bone in armature.data.bones}
        root_bone = next(
            (bone for bone in armature.data.bones if bone.parent is None),
            None,
        )
        if root_bone is None:
            raise RuntimeError(f"Armature {armature.name} has no root bone for skinning review.")
        unweighted_vertices: List[int] = []
        over_cap_before = 0
        zero_before = 0
        removed_influences = 0
        normalized_vertices = 0
        for vertex in obj.data.vertices:
            assignments = []
            for assignment in list(vertex.groups):
                group = obj.vertex_groups.get(obj.vertex_groups[assignment.group].name)
                if group is None or group.name not in bone_names:
                    if group is not None:
                        group.remove([vertex.index])
                    removed_influences += 1
                    continue
                weight = max(0.0, float(assignment.weight))
                if weight > 0.0:
                    assignments.append((group, weight))
                else:
                    group.remove([vertex.index])
                    removed_influences += 1

            if len(assignments) > max_influences_per_vertex:
                over_cap_before += 1
                kept = sorted(assignments, key=lambda item: (-item[1], item[0].name))[:max_influences_per_vertex]
                kept_names = {group.name for group, _ in kept}
                removed = [
                    (group, weight)
                    for group, weight in assignments
                    if group.name not in kept_names
                ]
                for group, _ in removed:
                    group.remove([vertex.index])
                removed_influences += len(removed)
                assignments = kept

            total = sum(weight for _, weight in assignments)
            if total <= 1e-8:
                zero_before += 1
                unweighted_vertices.append(vertex.index)
                continue

            for group, weight in assignments:
                group.add([vertex.index], weight / total, "REPLACE")
            normalized_vertices += 1

        weighted_bone_names = {
            obj.vertex_groups[assignment.group].name
            for vertex in obj.data.vertices
            for assignment in vertex.groups
            if assignment.weight > 0.0
            and obj.vertex_groups[assignment.group].name in bone_names
        }
        required_export_bones = set(weighted_bone_names)
        for bone_name in list(weighted_bone_names):
            bone = armature.data.bones.get(bone_name)
            while bone is not None:
                required_export_bones.add(bone.name)
                bone = bone.parent
        unignored_export_bones = []
        if not preserve_skeleton_metadata:
            for bone_name in sorted(required_export_bones):
                bone = armature.data.bones.get(bone_name)
                if bone is not None and bone.get("pdxIgnoreJoint"):
                    bone["pdxIgnoreJoint"] = False
                    unignored_export_bones.append(bone_name)

        records.append(
            {
                "object": obj.name,
                "armature": armature.name,
                "root_bone": root_bone.name,
                "vertices_over_four_before": over_cap_before if max_influences_per_vertex == 4 else 0,
                "vertices_over_cap_before": over_cap_before,
                "zero_weight_vertices_before": zero_before,
                "removed_influences": removed_influences,
                "normalized_vertices": normalized_vertices,
                "unweighted_vertices": len(unweighted_vertices),
                "weighted_bones": sorted(weighted_bone_names),
                "required_export_bones": sorted(required_export_bones),
                "unignored_export_bones": unignored_export_bones,
            }
        )
        if unweighted_vertices:
            unweighted_by_object[obj.name] = len(unweighted_vertices)

    if unweighted_by_object:
        raise RuntimeError(
            "Unweighted vertices are a rigging defect and are not pinned to the root bone: "
            + json.dumps(unweighted_by_object, sort_keys=True)
            + ". Skin every vertex in Blender before export."
        )

    return {
        "policy": (
            "keep_four_strongest_bone_influences_and_renormalize"
            if max_influences_per_vertex == 4
            else "keep_bounded_strongest_bone_influences_and_renormalize"
        ),
        "max_influences_per_vertex": max_influences_per_vertex,
        "skeleton_metadata_policy": (
            "preserve_checkpoint_skeleton_metadata"
            if preserve_skeleton_metadata
            else "unignore_required_export_bones"
        ),
        "objects": records,
        "weights_after": weight_metrics(),
    }


def sanitize_working_materials() -> Dict[str, Any]:
    """Remove glTF-only emission and metallic state from PDX runtime materials."""

    allowed_nodes = {
        "CHAOSX_DIFFUSE_TEXTURE",
        "CHAOSX_SPECULAR_TEXTURE",
        "CHAOSX_NORMAL_TEXTURE",
        "CHAOSX_NORMAL_MAP",
    }
    records: List[Dict[str, Any]] = []
    for obj in mesh_objects():
        for material in obj.data.materials:
            if material is None or not material.get("chaosx_pdx_shader"):
                continue
            ensure_material_nodes(material)
            changed = []
            for node in material.node_tree.nodes:
                if node.bl_idname != "ShaderNodeBsdfPrincipled":
                    continue
                for input_name in ("Metallic", "Emission", "Emission Color", "Emission Strength", "Alpha"):
                    socket = node.inputs.get(input_name)
                    if socket is None:
                        continue
                    for link in list(socket.links):
                        material.node_tree.links.remove(link)
                    if input_name == "Metallic":
                        socket.default_value = 0.0
                    elif input_name in {"Emission", "Emission Color"}:
                        socket.default_value = (0.0, 0.0, 0.0, 1.0)
                    elif input_name == "Emission Strength":
                        socket.default_value = 0.0
                    elif input_name == "Alpha":
                        socket.default_value = 1.0
                    changed.append(input_name)
            removed_nodes = []
            for node in list(material.node_tree.nodes):
                if node.bl_idname == "ShaderNodeTexImage" and node.name not in allowed_nodes:
                    removed_nodes.append(node.name)
                    material.node_tree.nodes.remove(node)
            records.append(
                {
                    "material": material.name,
                    "object": obj.name,
                    "changed_inputs": sorted(set(changed)),
                    "removed_nodes": sorted(removed_nodes),
                }
            )
    return {"policy": "pdx_mesh_advanced_opaque_non_emissive", "materials": records}


def image_nodes() -> List[Tuple[bpy.types.Material, bpy.types.Image]]:
    values: List[Tuple[bpy.types.Material, bpy.types.Image]] = []
    seen = set()
    for material in bpy.data.materials:
        if not material.get("chaosx_pdx_shader"):
            continue
        for node in material.node_tree.nodes:
            image = getattr(node, "image", None)
            if image is None or image.name in seen:
                continue
            seen.add(image.name)
            values.append((material, image))
    return values


def all_image_nodes() -> List[Tuple[bpy.types.Material, bpy.types.Image]]:
    """Return local node images for bounded reimport texture relinking.

    PDX reimport creates local materials without the source scene's
    ``chaosx_pdx_shader`` tag.  Keep the normal source-scene selector strict,
    but let the explicit texture-relink operation see those reimport nodes.
    """
    values: List[Tuple[bpy.types.Material, bpy.types.Image]] = []
    seen = set()
    for material in bpy.data.materials:
        if material.library or material.override_library or not material.use_nodes:
            continue
        for node in material.node_tree.nodes:
            image = getattr(node, "image", None)
            if image is None or image.name in seen:
                continue
            seen.add(image.name)
            values.append((material, image))
    return values


def camera_point_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def validate_preview_region(region, resolution):
    if type(resolution) is not int or not 128 <= resolution <= 2048:
        raise ValueError("Preview resolution must be an integer from128 to2048.")
    if region is None:
        return None
    if not isinstance(region,dict) or set(region)!={"min","max"}:
        raise ValueError("Preview region requires exact min/max world bounds.")
    for values in region.values():
        if not isinstance(values,list) or len(values)!=3 or any(type(v) not in (int,float) or not math.isfinite(v) or abs(v)>10000 for v in values):
            raise ValueError("Preview world bounds must be finite bounded numeric triples.")
    if any(a>=b for a,b in zip(region['min'],region['max'])):
        raise ValueError("Preview world bounds must have positive extent on every axis.")
    return region


def render_previews(
    job: Path,
    runtime_stem: str,
    view_names: List[str] | None = None,
    *,
    working_only: bool = True,
    preview_region: Dict[str, Any] | None = None,
    preview_resolution: int = 512,
) -> List[str]:
    validate_preview_region(preview_region,preview_resolution)
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = preview_resolution
    scene.render.resolution_y = preview_resolution
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.world.color = (0.015, 0.02, 0.03)

    meshes = mesh_objects(working_only=working_only)
    if not meshes:
        object_class = "working" if working_only else "imported runtime-proof"
        raise RuntimeError(f"Preview rendering found no {object_class} mesh objects.")
    # Pose-dependent preview framing only; source normalization retains raw bounds.
    bpy.context.view_layer.update()
    minimum, maximum = evaluated_world_bounds(meshes)
    ground_z = minimum.z
    if preview_region is not None:
        minimum,maximum=Vector(preview_region["min"]),Vector(preview_region["max"])
    center = (minimum + maximum) * 0.5
    dimensions = maximum - minimum
    object_height = max(float(max(dimensions)), 0.1)
    ground_extent = max(8.0, float(max(dimensions.x, dimensions.y)) * 2.0)

    evidence_collection = new_collection("QA_EVIDENCE")
    ground_mesh = bpy.data.meshes.new("QA_Ground_Mesh")
    ground_mesh.from_pydata(
        [
            (-ground_extent, -ground_extent, ground_z),
            (ground_extent, -ground_extent, ground_z),
            (ground_extent, ground_extent, ground_z),
            (-ground_extent, ground_extent, ground_z),
        ],
        [],
        [(0, 1, 2, 3)],
    )
    ground = bpy.data.objects.new("QA_Ground", ground_mesh)
    evidence_collection.objects.link(ground)
    ground.hide_render = False
    ground_mat = bpy.data.materials.new("QA_Ground_Material")
    ground_mat.diffuse_color = (0.02, 0.025, 0.03, 1.0)
    ground.data.materials.append(ground_mat)

    lights = []
    light_energy_scale = max(
        0.02,
        min(1.0, (object_height / PREVIEW_LIGHT_REFERENCE_HEIGHT) ** 2),
    )
    for name, location, energy, size in (
        ("QA_Key", (object_height * 0.8, -object_height * 0.8, object_height * 1.2), 1200.0, object_height * 0.7),
        ("QA_Fill", (-object_height * 0.8, -object_height * 0.4, object_height * 0.7), 700.0, object_height * 0.7),
        ("QA_Rim", (0.0, object_height * 0.8, object_height * 1.0), 900.0, object_height * 0.6),
    ):
        light_data = bpy.data.lights.new(name, type="AREA")
        light_data.energy = energy * light_energy_scale
        light_data.shape = "DISK"
        light_data.size = size
        light = bpy.data.objects.new(name, light_data)
        evidence_collection.objects.link(light)
        light.location = center + Vector(location)
        camera_point_at(light, center)
        lights.append(light)

    camera_data = bpy.data.cameras.new("QA_Camera")
    camera = bpy.data.objects.new("QA_Camera", camera_data)
    evidence_collection.objects.link(camera)
    scene.camera = camera
    camera_data.lens = 55

    # Frame the whole object regardless of whether it is a 1.5 m prop or a
    # vanilla-calibrated 7.35-unit source mesh.
    # Fit a sphere enclosing actual evaluated bounds using the real camera FOV.
    # This also contains horizontal death poses and all selected view directions.
    preview_angle = min(camera_data.angle_x,camera_data.angle_y)
    fit_distance = max(float(dimensions.length)*0.5/(math.sin(preview_angle*0.5)*0.78),0.1)

    available_views = [
            ("front", (center.x, center.y - fit_distance, center.z)),
            ("rear", (center.x, center.y + fit_distance, center.z)),
            ("left", (center.x - fit_distance, center.y, center.z)),
            ("right", (center.x + fit_distance, center.y, center.z)),
            ("top", (center.x, center.y - fit_distance * 0.7, maximum.z + fit_distance * 0.7)),
            ("underside", (center.x, center.y - fit_distance * 0.7, minimum.z - fit_distance * 0.35)),
            ("three_quarter", (center.x + fit_distance * 0.75, center.y - fit_distance * 0.75, center.z + object_height * 0.08)),
        ]
    selected_views = set(view_names or [])
    for index, location in enumerate(
        [item for item in available_views if not selected_views or item[0] in selected_views]
    ):
        name, location = location
        camera.location = location
        camera_point_at(camera, center)
        scene.render.filepath = str(job / "blender" / "previews" / f"{runtime_stem}_{name}.png")
        output = Path(scene.render.filepath)
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.exists():
            try:
                output.unlink()
            except OSError:
                # OneDrive or an image viewer can briefly hold the previous
                # preview. Keep the existing evidence and write this pass to
                # a deterministic sibling so the Blender checkpoint remains
                # reviewable instead of failing the whole export.
                output = output.with_name(f"{output.stem}_rerender.png")
                scene.render.filepath = str(output)
        bpy.ops.render.render(write_still=True)

    light_data = [light.data for light in lights]
    for obj in list(evidence_collection.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    bpy.data.collections.remove(evidence_collection)
    if ground_mesh.users == 0:
        bpy.data.meshes.remove(ground_mesh)
    if ground_mat.users == 0:
        bpy.data.materials.remove(ground_mat)
    for data in light_data:
        if data and data.users == 0:
            bpy.data.lights.remove(data)
    if camera_data.users == 0:
        bpy.data.cameras.remove(camera_data)
    return sorted(
        str(path.relative_to(job)).replace("\\", "/")
        for path in (job / "blender" / "previews").glob(f"{runtime_stem}_*.png")
    )


def prepare(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    source = within(job, payload["source_rel"])
    runtime_stem = safe_name(payload["runtime_stem"])
    binding_keys = sorted(
        key
        for key in (
            "geometry_source_rel",
            "geometry_object_name",
            "geometry_weight_mode",
            "source_mesh_names",
            "source_armature_name",
            "dual_source_base_rig",
        )
        if key in payload
    )
    if binding_keys:
        raise ValueError(
            "prepare_candidate does not bind geometry to a rig: "
            + json.dumps(binding_keys, sort_keys=True)
            + " is not accepted. Skeletons, skin weights and skeletal actions are authored live in Blender."
        )
    clear_scene()
    source_collection = new_collection("PROVIDER_SOURCE")
    working_collection = new_collection("WORKING")
    vanilla_reference = import_vanilla_reference(job, payload, pdx)
    imported = import_candidate(source)
    excluded_names = {str(name) for name in payload.get("excluded_provider_objects", [])}
    for obj in imported:
        move_to_collection(obj, source_collection)
    working_source = [obj for obj in imported if obj.name not in excluded_names]
    if not working_source:
        raise RuntimeError("Provider-object exclusion removed the entire candidate.")
    working = duplicate_hierarchy(working_source, source_collection, working_collection)
    for obj in imported:
        if obj not in working_source:
            obj["chaosx_provider_excluded"] = True
            obj.hide_render = True
            obj.hide_set(True)

    source_blend = job / "blender" / "source" / f"{runtime_stem}_provider_source.blend"
    save_blend(source_blend)
    imported_metrics = geometry_metrics()
    imported_checkpoint = job / "blender" / "checkpoints" / "00_imported_candidate.blend"
    save_blend(imported_checkpoint)

    asset_kind = str(payload["asset_kind"])
    humanoid_asset = is_humanoid_asset_kind(asset_kind)
    # Provider FBX files commonly key the armature object's 0.01 import scale.
    # Remove those scale curves before normalization so a later dependency-graph
    # evaluation cannot restore the provider scale after the report is measured.
    scale_sanitization = (
        sanitize_action_scale_channels()
        if humanoid_asset
        else {"policy": "not_applicable", "actions": [], "remaining_scale_fcurves": 0}
    )
    target_height = float(payload["target_height_m"])
    runtime_entity_scale = float(payload.get("runtime_entity_scale", 1.0))
    if runtime_entity_scale <= 0.0:
        raise RuntimeError("Candidate preparation requires a positive runtime entity scale.")
    normalize = normalize_geometry(target_height)
    footprint = constrain_runtime_footprint(
        payload.get("max_runtime_footprint_m"),
        runtime_entity_scale,
        str(payload.get("runtime_footprint_policy", "reject")),
    )
    preserve_geometry_topology = bool(payload.get("preserve_geometry_topology", False))
    if preserve_geometry_topology and (
        payload.get("repair_before_reduction", False)
        or int(payload.get("target_triangles", 0)) > 0
    ):
        raise ValueError(
            "Preserved geometry topology cannot be combined with repair or decimation."
        )
    triangulation = (
        {
            "applied": False,
            "policy": "preserve_audited_geometry_topology",
            "triangulated_objects": [],
        }
        if preserve_geometry_topology
        else triangulate_and_normals()
    )
    weld_distance = float(payload.get("topology_weld_distance", 1e-5))
    pre_reduction_topology_repair = None
    if payload.get("repair_before_reduction", False):
        pre_reduction_topology_repair = repair_open_surface_boundaries(weld_distance)
    reduction = (
        {
            "applied": False,
            "policy": "preserve_audited_geometry_topology",
            "target_triangles": 0,
        }
        if preserve_geometry_topology
        else controlled_decimate(int(payload.get("target_triangles", 0)))
    )
    topology_repair = (
        {
            "applied": False,
            "policy": "preserve_audited_geometry_topology",
            "method": "skipped for audited geometry handoff",
            "objects": [],
        }
        if preserve_geometry_topology
        else repair_open_surface_boundaries(weld_distance)
    )
    if pre_reduction_topology_repair is not None:
        topology_repair = {
            "applied": bool(
                pre_reduction_topology_repair.get("applied") or topology_repair.get("applied")
            ),
            "method": "pre-reduction seam weld followed by post-reduction bounded repair",
            "weld_distance": weld_distance,
            "pre_reduction": pre_reduction_topology_repair,
            "post_reduction": topology_repair,
        }
    geometry = geometry_metrics()
    if vanilla_reference:
        final_height = float(geometry["dimensions"][2])
        vanilla_reference["final_mesh_height"] = final_height
        vanilla_reference["pilot_entity_scale"] = runtime_entity_scale
        vanilla_reference["pilot_target_runtime_height"] = target_height * runtime_entity_scale
        vanilla_reference["final_effective_runtime_height"] = final_height * runtime_entity_scale
        vanilla_reference["final_runtime_height_delta"] = (
            vanilla_reference["final_effective_runtime_height"]
            - vanilla_reference["pilot_target_runtime_height"]
        )
    geometry_checkpoint = job / "blender" / "checkpoints" / "01_geometry_approved.blend"
    save_blend(geometry_checkpoint)

    materials = tag_pdx_materials(pdx)
    texture_bindings = bind_texture_sources(job, payload)
    materials["texture_bindings"] = texture_bindings
    if (humanoid_asset or asset_kind == "creature") and payload.get("texture_source_rels") and not image_nodes():
        raise RuntimeError(
            "Humanoid preparation produced no image-backed material. Refusing to export a black unit."
        )
    material_checkpoint = job / "blender" / "checkpoints" / "02_materials_approved.blend"
    save_blend(material_checkpoint)

    actions = action_metrics()
    actions["scale_sanitization"] = scale_sanitization
    if humanoid_asset and scale_sanitization["remaining_scale_fcurves"]:
        raise RuntimeError("Humanoid action export still contains scale channels after sanitization.")
    rig_checkpoint = None
    if humanoid_asset:
        rig_checkpoint = job / "blender" / "checkpoints" / "03_rig_approved.blend"
        save_blend(rig_checkpoint)
        action_checkpoint = job / "blender" / "checkpoints" / "04_actions_approved.blend"
        save_blend(action_checkpoint)
    pre_export = job / "blender" / "checkpoints" / "05_pre_export.blend"
    previews = render_previews(job, runtime_stem) if payload.get("render_previews", True) else []
    save_blend(pre_export)
    normalization_persistence = stabilize_saved_normalization(pre_export, target_height)
    normalization_persistence["checkpoint"] = str(pre_export.relative_to(job)).replace("\\", "/")
    geometry = normalization_persistence["geometry"]

    report = {
        "asset_kind": payload["asset_kind"],
        "source": str(source.relative_to(job)).replace("\\", "/"),
        "source_objects": len(imported),
        "excluded_provider_objects": sorted(excluded_names),
        "vanilla_reference": vanilla_reference,
        "working_source_objects": len(working_source),
        "working_objects": len(working),
        "imported_geometry": imported_metrics,
        "normalization": normalize,
        "normalization_persistence": normalization_persistence,
        "runtime_footprint": footprint,
        "runtime_calibration": {
            "mesh_target_height_m": target_height,
            "entity_scale": runtime_entity_scale,
            "effective_runtime_height_m": target_height * runtime_entity_scale,
            "policy": "bake the calibrated pilot source height into mesh coordinates and preserve the specified vanilla entity scale",
        },
        "triangulation": triangulation,
        "controlled_reduction": reduction,
        "topology_repair": topology_repair,
        "geometry": geometry,
        "materials": materials,
        "rig_and_actions": actions,
        "checkpoints": {
            "source": str(source_blend.relative_to(job)).replace("\\", "/"),
            "imported": str(imported_checkpoint.relative_to(job)).replace("\\", "/"),
            "geometry": str(geometry_checkpoint.relative_to(job)).replace("\\", "/"),
            "materials": str(material_checkpoint.relative_to(job)).replace("\\", "/"),
            "rig": str(rig_checkpoint.relative_to(job)).replace("\\", "/") if rig_checkpoint else None,
            "pre_export": str(pre_export.relative_to(job)).replace("\\", "/"),
        },
        "previews": previews,
        "io_pdx_mesh_manifest": pdx["manifest"],
    }
    report_path = job / "blender" / "reports" / f"{runtime_stem}_prepare.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _mesh_region_name(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or len(value) > 128 or any(ord(char) < 32 for char in value):
        raise ValueError(f"{label} must be an exact nonempty name of at most 128 characters.")
    return value


def _mesh_region_inputs(req: Dict[str, Any]) -> Dict[str, Any]:
    payload = req["payload"]
    region = payload.get("mesh_region")
    required = {"mesh_name", "bone_name", "expected_source_sha256", "expected_action_sha256"}
    allowed = required | {"aabb", "weight", "offset", "limit", "measurement"}
    if not isinstance(region, dict) or not required.issubset(region) or set(region) - allowed:
        raise ValueError("mesh_region has missing or unsupported fields.")
    if payload.get("render_previews") or payload.get("runtime_stem") or payload.get("preview_view_names"):
        raise ValueError("Mesh-region inspection does not render or write previews.")
    result = dict(region)
    for key in ("mesh_name", "bone_name"):
        result[key] = _mesh_region_name(region[key], key)
    result["rig_name"] = _mesh_region_name(payload.get("target_armature_name"), "target_armature_name")
    result["action_name"] = _mesh_region_name(payload.get("action_name"), "action_name")
    frame = payload.get("preview_frame")
    if type(frame) is not int or not 0 <= frame <= 1000000:
        raise ValueError("Mesh-region preview_frame must be an explicit nonnegative bounded integer.")
    result["frame"] = frame
    for key in ("expected_source_sha256", "expected_action_sha256"):
        if not isinstance(region[key], str) or not re.fullmatch(r"[0-9A-Fa-f]{64}", region[key]):
            raise ValueError(f"{key} must be an explicit SHA-256.")
        result[key] = region[key].upper()
    if not any(key in region for key in ("aabb", "weight")):
        raise ValueError("Mesh-region inspection requires a spatial and/or bone-weight selector.")
    if "aabb" in region:
        box = region["aabb"]
        if not isinstance(box, dict) or set(box) != {"space", "min", "max"} or not isinstance(box["space"], str) or box["space"] not in {"WORLD", "BONE_LOCAL"}:
            raise ValueError("aabb requires WORLD or BONE_LOCAL space and exact min/max vectors.")
        low, high = _locator_numbers(box["min"], 3, "aabb min"), _locator_numbers(box["max"], 3, "aabb max")
        if any(abs(value) > 1000000 for value in low + high) or any(a > b for a, b in zip(low, high)):
            raise ValueError("AABB bounds must be ordered and inside +/-1000000 units.")
        result["aabb"] = {"space": box["space"], "min": low, "max": high}
    if "weight" in region:
        weight = region["weight"]
        if not isinstance(weight, dict) or set(weight) != {"bone_name", "min", "max"}:
            raise ValueError("weight requires an exact bone_name and inclusive min/max.")
        low, high = _locator_numbers([weight["min"], weight["max"]], 2, "weight range")
        if not 0 <= low <= high <= 1:
            raise ValueError("Weight range must be ordered inside [0,1].")
        result["weight"] = {"bone_name": _mesh_region_name(weight["bone_name"], "weight bone"), "min": low, "max": high}
    for key, default, maximum in (("offset", 0, 1000000), ("limit", 64, 256)):
        value = region.get(key, default)
        if type(value) is not int or not (0 if key == "offset" else 1) <= value <= maximum:
            raise ValueError(f"Invalid mesh-region {key}.")
        result[key] = value
    if "measurement" in region:
        measurement = region["measurement"]
        if not isinstance(measurement, dict) or set(measurement) != {"origin_vertex_indices", "endpoint_vertex_indices"}:
            raise ValueError("measurement requires origin and endpoint source-vertex index sets.")
        for name, values in measurement.items():
            if not isinstance(values, list) or not 1 <= len(values) <= 64 or any(type(value) is not int or not 0 <= value < 1000000 for value in values) or len(set(values)) != len(values):
                raise ValueError(f"{name} requires 1-64 unique bounded source vertex indices.")
        if set(measurement["origin_vertex_indices"]) & set(measurement["endpoint_vertex_indices"]):
            raise ValueError("Measurement origin and endpoint index sets must not overlap.")
    job = Path(req["job_root"]).resolve()
    source = _promotion_path(job, payload.get("blend_rel"), ".blend")
    if source.stat().st_size < 1 or file_sha256(source) != result["expected_source_sha256"]:
        raise ValueError("Mesh-region source SHA-256 mismatch.")
    result.update(job=job, source=source, source_bytes=source.stat().st_size)
    return result


def _action_channel_inventory_inputs(req: Dict[str, Any]) -> Dict[str, Any]:
    payload = req["payload"]
    if payload.get("include_action_channels") is not True:
        raise ValueError("Action-channel inventory requires include_action_channels=true.")
    if payload.get("render_previews") or payload.get("runtime_stem") or payload.get("preview_view_names") or payload.get("mesh_region") is not None:
        raise ValueError("Action-channel inventory cannot render or combine with mesh-region inspection.")
    if payload.get("preview_frame", -1) != -1:
        raise ValueError("Action-channel inventory does not evaluate a preview frame.")
    expected = payload.get("expected_source_sha256")
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9A-Fa-f]{64}", expected):
        raise ValueError("expected_source_sha256 must be an explicit SHA-256 for action-channel inventory.")
    job = Path(req["job_root"]).resolve()
    source = _promotion_path(job, payload.get("blend_rel"), ".blend")
    expected = expected.upper()
    size = source.stat().st_size
    if size < 1 or file_sha256(source) != expected:
        raise ValueError("Action-channel inventory source SHA-256 mismatch.")
    return {
        "job": job,
        "source": source,
        "source_bytes": size,
        "expected_source_sha256": expected,
        "rig_name": _mesh_region_name(payload.get("target_armature_name"), "target_armature_name"),
        "action_name": _mesh_region_name(payload.get("action_name"), "action_name"),
    }


def _action_channel_rows(action: Any, rig: Any) -> List[Dict[str, Any]]:
    curves = list(action_fcurves(action))
    if len(curves) > 4096:
        raise ValueError("Action-channel inventory exceeds the 4096-curve cap.")
    bone_owners = [(bone.path_from_id(), bone) for bone in rig.pose.bones]
    object_paths = {"location", "rotation_euler", "rotation_quaternion", "rotation_axis_angle", "scale"}
    rows = []
    total_keys = sum(len(curve.keyframe_points) for curve, _ in curves)
    if total_keys > 500000:
        raise ValueError("Action-channel key inventory exceeds 500000 keys.")
    for curve, _ in curves:
        path = str(curve.data_path)
        if not path or len(path) > 1024 or any(ord(character) < 32 for character in path):
            raise ValueError("Action-channel inventory encountered an invalid or overlong data_path.")
        index = int(curve.array_index)
        if not 0 <= index <= 1024:
            raise ValueError("Action-channel inventory encountered an invalid array_index.")
        group = getattr(curve, "group", None)
        group_name = None if group is None else str(group.name)
        if group_name is not None and (len(group_name) > 128 or any(ord(character) < 32 for character in group_name)):
            raise ValueError("Action-channel inventory encountered an invalid or overlong group name.")
        owners = [bone for prefix, bone in bone_owners if path == prefix or path.startswith(prefix + ".") or path.startswith(prefix + "[")]
        if len(owners) > 1:
            raise ValueError("Action-channel inventory found an ambiguous bone RNA owner.")
        rotation_mode = str(owners[0].rotation_mode) if owners else (str(rig.rotation_mode) if path in object_paths else None)
        rows.append({"data_path": path, "array_index": index, "group": group_name, "rotation_mode": rotation_mode,
                     "extrapolation": str(curve.extrapolation),
                     "keyframes": [{"co": list(point.co), "interpolation": str(point.interpolation),
                                    "handle_left": list(point.handle_left), "handle_right": list(point.handle_right),
                                    "handle_left_type": str(point.handle_left_type), "handle_right_type": str(point.handle_right_type)}
                                   for point in curve.keyframe_points]})
    return sorted(rows, key=lambda row: (row["data_path"], row["array_index"], row["group"] or "", row["rotation_mode"] or ""))


def _action_channel_binding_record(rig: Any) -> Dict[str, Any]:
    animation = rig.animation_data
    return {
        "frame": int(bpy.context.scene.frame_current),
        "subframe": float(bpy.context.scene.frame_subframe),
        "object_rotation_mode": str(rig.rotation_mode),
        "bone_rotation_modes": [(bone.name, str(bone.rotation_mode)) for bone in rig.pose.bones],
        "action": animation.action.name if animation and animation.action else None,
        "action_slot": getattr(getattr(animation, "action_slot", None), "identifier", None) if animation else None,
        "drivers": [(curve.data_path, int(curve.array_index)) for curve in animation.drivers] if animation else [],
        "nla": [
            {
                "name": track.name,
                "mute": bool(track.mute),
                "solo": bool(track.is_solo),
                "strips": [(strip.name, strip.action.name if strip.action else None, float(strip.frame_start), float(strip.frame_end)) for strip in track.strips],
            }
            for track in animation.nla_tracks
        ] if animation else [],
    }


def inspect_action_channels(req: Dict[str, Any]) -> Dict[str, Any]:
    context = _action_channel_inventory_inputs(req)
    try:
        bpy.ops.wm.open_mainfile(filepath=str(context["source"]), use_scripts=False)
        rig = bpy.context.scene.objects.get(context["rig_name"])
        action = bpy.data.actions.get(context["action_name"])
        if rig is None or rig.type != "ARMATURE" or action is None:
            raise ValueError("Action-channel inventory requires the exact armature and action.")
        if rig.library or rig.override_library or action.library or action.override_library:
            raise ValueError("Action-channel inventory requires local armature and action data.")
        before_actions = _mesh_region_action_integrity()
        before_binding = _action_channel_binding_record(rig)
        native_hash = _mesh_region_action_hash(action)
        rows = _action_channel_rows(action, rig)
        after_binding = _action_channel_binding_record(rig)
        if after_binding != before_binding or _mesh_region_action_integrity() != before_actions or _mesh_region_action_hash(action) != native_hash:
            raise RuntimeError("Read-only action-channel inventory changed action, frame, or rotation-mode data.")
        result = {
            "source_sha256": context["expected_source_sha256"],
            "source_bytes": context["source_bytes"],
            "source_immutable": True,
            "armature_name": rig.name,
            "action_name": action.name,
            "native_action_sha256": native_hash,
            "native_action_hash_policy": "inspect_scene_curve_slot_path_index_key_co_interpolation_v1_not_anim_file_sha256",
            "action_integrity_sha256": before_actions,
            "row_count": len(rows),
            "pose_local_snapshot": [{"name": bone.name, "location": list(bone.location),
                                     "rotation_mode": bone.rotation_mode, "rotation_quaternion": list(bone.rotation_quaternion),
                                     "rotation_euler": list(bone.rotation_euler), "scale": list(bone.scale)} for bone in rig.pose.bones],
            "rows": rows,
            "action_data_unchanged": True,
            "frame_action_rotation_modes_unchanged": True,
            "checkpoint_saved": False,
            "new_provider_call": False,
        }
        _promotion_digest(result)
        return {
            "blend": context["source"].relative_to(context["job"]).as_posix(),
            "inspected_target_armature": rig.name,
            "inspected_action_sha256": native_hash,
            "action_channels": result,
        }
    finally:
        if file_sha256(context["source"]) != context["expected_source_sha256"] or context["source"].stat().st_size != context["source_bytes"]:
            raise RuntimeError("Read-only action-channel inventory changed its source checkpoint.")


def _mesh_region_action_hash(action: bpy.types.Action) -> str:
    """The existing inspect_scene inspected_action_sha256 contract, not an .anim hash."""
    records = [{"slot": getattr(slot, "identifier", None), "data_path": curve.data_path, "array_index": int(curve.array_index),
                "keyframes": [[float(key.co.x), float(key.co.y), str(key.interpolation)] for key in curve.keyframe_points]}
               for curve, slot in action_fcurves(action)]
    return _promotion_digest(records)


def _mesh_region_action_integrity() -> str:
    records = {}
    for action in bpy.data.actions:
        curves = [{"path": curve.data_path, "index": curve.array_index, "settings": _promotion_scalars(curve),
                   "keys": [{"co": list(key.co), "left": list(key.handle_left), "right": list(key.handle_right), "settings": _promotion_scalars(key)} for key in curve.keyframe_points],
                   "samples": [list(point.co) for point in curve.sampled_points]}
                  for curve, _ in action_fcurves(action)]
        records[action.name] = {"settings": _promotion_scalars(action), "properties": _promotion_properties(action), "fake_user": action.use_fake_user, "curves": curves,
                                "slots": [_promotion_scalars(slot) for slot in getattr(action, "slots", [])]}
    return _promotion_digest(records)


def _mesh_region_topology(mesh: Any) -> str:
    return _promotion_digest({"vertices": [vertex.index for vertex in mesh.vertices],
                              "edges": [(edge.index, list(edge.vertices)) for edge in mesh.edges],
                              "loops": [(loop.index, loop.vertex_index, loop.edge_index) for loop in mesh.loops],
                              "polygons": [(face.index, face.loop_start, face.loop_total, list(face.vertices), face.material_index) for face in mesh.polygons]})


def _mesh_region_matrix(matrix: Matrix, label: str) -> Matrix:
    _locator_matrix_record(matrix)
    if matrix.determinant() <= 0:
        raise ValueError(f"{label} has a negative or singular transform.")
    try:
        inverse = matrix.inverted()
    except ValueError as exc:
        raise ValueError(f"{label} has a singular transform.") from exc
    _locator_matrix_record(inverse)
    return inverse


def _mesh_region_normal(normal: Vector, transform: Matrix) -> List[float]:
    result = transform @ normal
    if not math.isfinite(result.length) or result.length <= 1e-12:
        raise ValueError("Mesh-region normal is nonfinite or has zero length.")
    return _locator_numbers(list(result.normalized()), 3, "mesh-region normal")


def _mesh_region_measurement(specification: Dict[str, Any], matches: List[int], position: Any, bone_inverse: Matrix) -> Dict[str, Any]:
    required = set(specification["origin_vertex_indices"]) | set(specification["endpoint_vertex_indices"])
    if not required.issubset(set(matches)):
        raise ValueError("Every measurement vertex index must match the complete selector, independently of pagination.")
    def centroid(indices: List[int]) -> Vector:
        return sum((position(index) for index in indices), Vector()) / len(indices)
    origin, endpoint = centroid(specification["origin_vertex_indices"]), centroid(specification["endpoint_vertex_indices"])
    axis = endpoint - origin
    local_origin, local_endpoint = bone_inverse @ origin, bone_inverse @ endpoint
    local_axis = local_endpoint - local_origin
    if any(not math.isfinite(value.length) or value.length <= 1e-12 for value in (axis, local_axis)):
        raise ValueError("Measured centroid axis is nonfinite or zero length.")
    return {"policy": "caller_selected_vertex_centroids_no_semantic_detection_no_roll",
            "origin_vertex_indices": specification["origin_vertex_indices"], "endpoint_vertex_indices": specification["endpoint_vertex_indices"],
            "origin_count": len(specification["origin_vertex_indices"]), "endpoint_count": len(specification["endpoint_vertex_indices"]),
            "world_origin": list(origin), "world_endpoint": list(endpoint), "world_axis": list(axis.normalized()), "world_length": axis.length,
            "bone_local_origin": list(local_origin), "bone_local_endpoint": list(local_endpoint), "bone_local_axis": list(local_axis.normalized()),
            "rotation_quaternion": None, "semantic_muzzle_approval": False}


def _mesh_region_collect(mesh_obj: Any, evaluated_obj: Any, evaluated: Any, rig: Any, evaluated_rig: Any, context: Dict[str, Any]) -> Dict[str, Any]:
    source = mesh_obj.data
    if len(source.vertices) > 1000000 or len(source.loops) > 6000000 or len(source.uv_layers) > 8 or len(mesh_obj.vertex_groups) > 256:
        raise ValueError("Mesh-region source exceeds explicit vertex/loop/UV/group caps.")
    topology = _mesh_region_topology(source)
    if _mesh_region_topology(evaluated) != topology:
        raise ValueError("Evaluated topology/index correspondence changed.")
    if [layer.name for layer in source.uv_layers] != [layer.name for layer in evaluated.uv_layers]:
        raise ValueError("Evaluated UV-layer identity changed.")
    world = evaluated_obj.matrix_world.copy()
    world_inverse = _mesh_region_matrix(world, "mesh world")
    bone_world = evaluated_rig.matrix_world @ evaluated_rig.pose.bones[context["bone_name"]].matrix
    bone_inverse = _mesh_region_matrix(bone_world, "posed bone world")
    rest_bone_world = rig.matrix_world @ rig.data.bones[context["bone_name"]].matrix_local
    rest_bone_inverse = _mesh_region_matrix(rest_bone_world, "rest bone world")
    normal_world = world_inverse.to_3x3().transposed()
    normal_bone = bone_world.to_3x3().transposed()
    weight_group = None
    if "weight" in context:
        name = context["weight"]["bone_name"]
        if rig.data.bones.get(name) is None or mesh_obj.vertex_groups.get(name) is None:
            raise ValueError("Weight selector must name an existing rig bone and mesh group.")
        weight_group = mesh_obj.vertex_groups[name].index
    matches = []
    for vertex in evaluated.vertices:
        point = world @ vertex.co
        _locator_numbers(list(point), 3, "evaluated world position")
        box = context.get("aabb")
        if box:
            sample = point if box["space"] == "WORLD" else bone_inverse @ point
            if any(sample[axis] < box["min"][axis] or sample[axis] > box["max"][axis] for axis in range(3)):
                continue
        if weight_group is not None:
            value = sum(group.weight for group in source.vertices[vertex.index].groups if group.group == weight_group)
            if not context["weight"]["min"] <= value <= context["weight"]["max"]:
                continue
        matches.append(vertex.index)
    if context["offset"] > len(matches):
        raise ValueError("Mesh-region page offset exceeds total matched vertices.")
    loop_map = {}
    for face in source.polygons:
        for index in face.loop_indices:
            loop_map.setdefault(source.loops[index].vertex_index, []).append((index, face.index, face.material_index))
    selected, corner_count = [], 0
    for index in matches[context["offset"]:context["offset"] + context["limit"]]:
        count = len(loop_map.get(index, []))
        if corner_count + count > 8192:
            if not selected:
                raise ValueError("One vertex exceeds the 8192-corner page cap.")
            break
        selected.append(index)
        corner_count += count
    def position(index: int) -> Vector:
        return world @ evaluated.vertices[index].co
    records = []
    for index in selected:
        original, posed = source.vertices[index], evaluated.vertices[index]
        point = position(index)
        vertex_normal = _mesh_region_normal(posed.normal, normal_world)
        corners = []
        for loop_index, face_index, material_index in loop_map.get(index, []):
            material = mesh_obj.material_slots[material_index].material if material_index < len(mesh_obj.material_slots) else None
            posed_normal = _mesh_region_normal(evaluated.corner_normals[loop_index].vector, normal_world)
            corners.append({"loop_index": loop_index, "polygon_index": face_index, "material_index": material_index, "material_name": material.name if material else None,
                            "source_uvs": {layer.name: _locator_numbers(list(layer.data[loop_index].uv), 2, "source UV") for layer in source.uv_layers},
                            "evaluated_uvs": {layer.name: _locator_numbers(list(layer.data[loop_index].uv), 2, "evaluated UV") for layer in evaluated.uv_layers},
                            "source_normal": _locator_numbers(list(source.corner_normals[loop_index].vector), 3, "source corner normal"),
                            "evaluated_world_normal": posed_normal, "bone_local_normal": _mesh_region_normal(Vector(posed_normal), normal_bone)})
        records.append({"vertex_index": index, "source_position": list(original.co), "source_world_position": list(mesh_obj.matrix_world @ original.co),
                        "rest_bone_local_position": list(rest_bone_inverse @ (mesh_obj.matrix_world @ original.co)),
                        "evaluated_world_position": list(point), "bone_local_position": list(bone_inverse @ point),
                        "source_normal": list(original.normal), "evaluated_world_normal": vertex_normal,
                        "bone_local_normal": _mesh_region_normal(Vector(vertex_normal), normal_bone),
                        "weights": [{"group_index": group.group, "group_name": mesh_obj.vertex_groups[group.group].name, "weight": float(group.weight)} for group in original.groups],
                        "corners": corners})
    measurement = _mesh_region_measurement(context["measurement"], matches, position, bone_inverse) if "measurement" in context else None
    next_offset = context["offset"] + len(records)
    result = {"mesh_name": mesh_obj.name, "mesh_data_name": source.name, "rig_name": rig.name, "bone_name": context["bone_name"], "frame": context["frame"],
              "source_counts": {"vertices": len(source.vertices), "loops": len(source.loops), "polygons": len(source.polygons)}, "topology_sha256": topology,
              "topology_index_correspondence": True, "selector": {key: context[key] for key in ("aabb", "weight") if key in context},
              "total_matches": len(matches), "matched_vertex_indices_sha256": _promotion_digest(matches),
              "page": {"offset": context["offset"], "requested_limit": context["limit"], "returned_vertices": len(records), "returned_corners": corner_count,
                       "vertex_cap": 256, "corner_cap": 8192, "truncated": next_offset < len(matches), "corner_cap_reached": len(records) < len(matches[context["offset"]:context["offset"] + context["limit"]]),
                       "next_offset": next_offset if next_offset < len(matches) else None},
              "matrices": {"mesh_world": _locator_matrix_record(world), "mesh_world_inverse": _locator_matrix_record(world_inverse),
                           "bone_pose_world": _locator_matrix_record(bone_world), "bone_pose_world_inverse": _locator_matrix_record(bone_inverse),
                           "bone_rest_world": _locator_matrix_record(rest_bone_world), "bone_rest_world_inverse": _locator_matrix_record(rest_bone_inverse)},
              "records": records, "measurement": measurement}
    _promotion_digest(result)
    return result


def _mesh_region_object_dependencies(mesh: Any, rig: Any) -> None:
    if rig.parent is not None or (mesh.parent is not None and (mesh.parent != rig or mesh.parent_type != "OBJECT")):
        raise ValueError("Mesh-region targets have an uninspected parent dependency.")
    if mesh.data.animation_data is not None or rig.data.animation_data is not None:
        raise ValueError("Mesh-region does not support animated mesh or armature datablocks.")


def inspect_mesh_region(req: Dict[str, Any]) -> Dict[str, Any]:
    context = _mesh_region_inputs(req)
    bpy.ops.wm.open_mainfile(filepath=str(context["source"]), use_scripts=False)
    objects = bpy.context.scene.objects
    mesh, rig = objects.get(context["mesh_name"]), objects.get(context["rig_name"])
    if mesh is None or mesh.type != "MESH" or rig is None or rig.type != "ARMATURE" or rig.data.bones.get(context["bone_name"]) is None:
        raise ValueError("Mesh-region requires the exact mesh, armature, and existing bone.")
    _mesh_region_object_dependencies(mesh, rig)
    for obj in (mesh, rig):
        if obj.library or obj.override_library or obj.data.library or obj.data.override_library or obj.constraints or any(value <= 0 for value in obj.scale):
            raise ValueError("Mesh-region requires local unconstrained positive-transform targets.")
        _mesh_region_matrix(obj.matrix_world, obj.name)
    modifiers = list(mesh.modifiers)
    if len(modifiers) != 1 or modifiers[0].type != "ARMATURE" or modifiers[0].object != rig or not modifiers[0].show_viewport:
        raise ValueError("Mesh-region permits exactly one active Armature modifier consuming the named rig.")
    if mesh.data.shape_keys or mesh.animation_data or rig.data.pose_position != "POSE" or any(bone.constraints for bone in rig.pose.bones):
        raise ValueError("Mesh-region does not support shape keys, mesh animation, REST display, or pose constraints.")
    animation, action = rig.animation_data, bpy.data.actions.get(context["action_name"])
    if animation is None or animation.drivers or animation.nla_tracks or action is None or action.library or action.override_library or len(getattr(action, "slots", [])) > 1:
        raise ValueError("Mesh-region requires one explicit local action without NLA/drivers or ambiguous slots.")
    if any(curve.modifiers for curve, _ in action_fcurves(action)) or not action.frame_range[0] <= context["frame"] <= action.frame_range[1]:
        raise ValueError("Mesh-region requires an in-range frame and unmodified action curves.")
    actual_action_hash = _mesh_region_action_hash(action)
    if actual_action_hash != context["expected_action_sha256"]:
        raise ValueError("Mesh-region native action SHA-256 mismatch; obtain inspected_action_sha256 with ordinary read-only inspect_scene first.")
    before_actions = _mesh_region_action_integrity()
    old_action, old_slot = animation.action, getattr(animation, "action_slot", None)
    scene = bpy.context.scene
    old_frame, old_subframe = scene.frame_current, scene.frame_subframe
    evaluated_obj = None
    try:
        animation.action = action
        if getattr(action, "slots", []):
            animation.action_slot = action.slots[0]
        scene.frame_set(context["frame"])
        bpy.context.view_layer.update()
        if any(value <= 0 for value in rig.pose.bones[context["bone_name"]].scale):
            raise ValueError("Requested bone has negative or singular pose scale.")
        depsgraph = bpy.context.evaluated_depsgraph_get()
        evaluated_obj, evaluated_rig = mesh.evaluated_get(depsgraph), rig.evaluated_get(depsgraph)
        evaluated = evaluated_obj.to_mesh(preserve_all_data_layers=True, depsgraph=depsgraph)
        report = _mesh_region_collect(mesh, evaluated_obj, evaluated, rig, evaluated_rig, context)
    finally:
        if evaluated_obj is not None:
            evaluated_obj.to_mesh_clear()
        animation.action = old_action
        if old_slot is not None:
            animation.action_slot = old_slot
        scene.frame_set(old_frame, subframe=old_subframe)
        bpy.context.view_layer.update()
    if animation.action != old_action or getattr(animation, "action_slot", None) != old_slot or scene.frame_current != old_frame or scene.frame_subframe != old_subframe:
        raise RuntimeError("Mesh-region frame/action binding restoration failed.")
    if _mesh_region_action_integrity() != before_actions or _mesh_region_action_hash(action) != actual_action_hash:
        raise RuntimeError("Read-only mesh-region inspection changed action data.")
    if file_sha256(context["source"]) != context["expected_source_sha256"] or context["source"].stat().st_size != context["source_bytes"]:
        raise RuntimeError("Read-only mesh-region source changed.")
    report.update(source_sha256=context["expected_source_sha256"], source_bytes=context["source_bytes"], source_immutable=True,
                  action_name=action.name, native_action_sha256=actual_action_hash, native_action_hash_policy="inspect_scene_curve_slot_path_index_key_co_interpolation_v1_not_anim_file_sha256",
                  action_integrity_sha256=before_actions, all_actions_unchanged=True, action_provenance=_promotion_properties(action),
                  source_receipt_metadata={obj.name: {key: _promotion_value(obj[key]) for key in PROMOTION_METADATA_KEYS if key in obj} for obj in (rig, mesh)},
                  frame_action_binding_restored=True, new_provider_call=False, checkpoint_saved=False)
    return {"blend": context["source"].relative_to(context["job"]).as_posix(), "inspected_target_armature": rig.name,
            "inspected_action_sha256": actual_action_hash, "mesh_region": report}


def _component_review_inputs(req: Dict[str, Any]) -> Dict[str, Any]:
    payload = req["payload"]
    required = {"blend_rel", "expected_source_sha256", "mesh_name", "render_group", "component_ids", "component_offset", "component_limit", "preview_view_names"}
    if not isinstance(payload, dict) or set(payload) != required:
        raise ValueError("review_humanoid_components accepts only its exact read-only contract.")
    if payload["render_group"] is not True:
        raise ValueError("Humanoid component review requires render_group=true; bounds-only review is insufficient.")
    expected = payload["expected_source_sha256"]
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9A-Fa-f]{64}", expected):
        raise ValueError("expected_source_sha256 must be an explicit SHA-256.")
    ids = payload["component_ids"]
    if not isinstance(ids, list) or len(ids) > 16 or any(not isinstance(value, str) or not re.fullmatch(r"c_v[0-9]{1,7}", value) for value in ids) or len(set(ids)) != len(ids):
        raise ValueError("component_ids must contain at most 16 unique stable component IDs.")
    offset, limit = payload["component_offset"], payload["component_limit"]
    if type(offset) is not int or not 0 <= offset <= 8192 or type(limit) is not int or not 1 <= limit <= 16:
        raise ValueError("Component review offset/limit must stay inside the 8192-component and 16-component page caps.")
    if ids and (offset != 0 or limit != 16):
        raise ValueError("Explicit component_ids cannot be combined with nondefault pagination.")
    allowed_views = {"front", "left", "right", "rear", "top", "three_quarter"}
    requested_views = payload["preview_view_names"]
    if not isinstance(requested_views, list):
        raise ValueError("preview_view_names must be a list.")
    views = requested_views or ["front", "left", "right", "rear", "top", "three_quarter"]
    if not 1 <= len(views) <= 6 or any(type(value) is not str or value not in allowed_views for value in views) or len(set(views)) != len(views):
        raise ValueError("Component-review views must be unique supported named views.")
    job = Path(req["job_root"]).resolve()
    source = _promotion_path(job, payload["blend_rel"], ".blend")
    expected = expected.upper()
    source_bytes = source.stat().st_size
    if source_bytes < 1 or file_sha256(source) != expected:
        raise ValueError("Component-review source SHA-256 mismatch.")
    request_id = req.get("request_id")
    if not isinstance(request_id, str) or not re.fullmatch(r"[0-9a-f]{32}", request_id):
        raise ValueError("Component review requires the adapter's exact lowercase UUID request_id.")
    return {"job": job, "source": source, "source_bytes": source_bytes, "expected_source_sha256": expected,
            "mesh_name": _mesh_region_name(payload["mesh_name"], "mesh_name"), "component_ids": ids,
            "component_offset": offset, "component_limit": limit, "preview_view_names": views,
            "request_id": request_id}


def _component_index_catalog(vertex_count: int, edges: Iterable[Tuple[int, Iterable[int]]], polygons: Iterable[Tuple[int, Iterable[int]]]) -> List[Dict[str, Any]]:
    if type(vertex_count) is not int or not 1 <= vertex_count <= 250000:
        raise ValueError("Component review requires 1-250000 source vertices.")
    parent = list(range(vertex_count))
    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index
    def union(left: int, right: int) -> None:
        left, right = find(left), find(right)
        if left != right:
            parent[max(left, right)] = min(left, right)
    edge_rows, polygon_rows = [], []
    for edge_index, values in edges:
        values = tuple(values)
        if type(edge_index) is not int or len(values) != 2 or any(type(value) is not int or not 0 <= value < vertex_count for value in values) or values[0] == values[1]:
            raise ValueError("Component review found invalid edge topology.")
        union(values[0], values[1])
        edge_rows.append((edge_index, values))
    for polygon_index, values in polygons:
        values = tuple(values)
        if type(polygon_index) is not int or len(values) < 3 or any(type(value) is not int or not 0 <= value < vertex_count for value in values):
            raise ValueError("Component review found invalid polygon topology.")
        for value in values[1:]:
            union(values[0], value)
        polygon_rows.append((polygon_index, values))
    vertices_by_root: Dict[int, List[int]] = {}
    for vertex in range(vertex_count):
        vertices_by_root.setdefault(find(vertex), []).append(vertex)
    result = []
    for vertices in sorted(vertices_by_root.values(), key=lambda row: row[0]):
        members = set(vertices)
        component_edges = [index for index, values in edge_rows if values[0] in members]
        component_polygons = [index for index, values in polygon_rows if values[0] in members]
        if any(any(value not in members for value in values) for index, values in edge_rows if index in component_edges):
            raise ValueError("Component edge crosses a computed component boundary.")
        if any(any(value not in members for value in values) for index, values in polygon_rows if index in component_polygons):
            raise ValueError("Component polygon crosses a computed component boundary.")
        result.append({"component_id": f"c_v{vertices[0]}", "vertex_indices": vertices,
                       "edge_indices": component_edges, "polygon_indices": component_polygons})
    if len(result) > 8192:
        raise ValueError("Component review exceeds the 8192-component cap.")
    return result


def _component_boundary_record(mesh: Any, record: Dict[str, Any]) -> Dict[str, Any]:
    incidence = {index: 0 for index in record["edge_indices"]}
    for polygon_index in record["polygon_indices"]:
        for loop_index in mesh.polygons[polygon_index].loop_indices:
            edge_index = mesh.loops[loop_index].edge_index
            if edge_index not in incidence:
                raise ValueError("Polygon loop references an edge outside its component.")
            incidence[edge_index] += 1
    boundary = sorted(index for index, count in incidence.items() if count == 1)
    loose = sorted(index for index, count in incidence.items() if count == 0)
    non_manifold = sorted(index for index, count in incidence.items() if count > 2)
    adjacency: Dict[int, List[int]] = {}
    for edge_index in boundary:
        left, right = mesh.edges[edge_index].vertices
        adjacency.setdefault(left, []).append(right)
        adjacency.setdefault(right, []).append(left)
    unseen, groups = set(adjacency), []
    while unseen:
        pending, observed = [min(unseen)], set()
        while pending:
            value = pending.pop()
            if value in observed:
                continue
            observed.add(value)
            pending.extend(adjacency[value])
        unseen -= observed
        groups.append(sorted(observed))
    closed = sum(1 for group in groups if group and all(len(adjacency[index]) == 2 for index in group))
    return {"boundary_edge_indices": boundary, "loose_edge_indices": loose, "non_manifold_edge_indices": non_manifold,
            "boundary_graph_components": len(groups), "closed_boundary_loops": closed,
            "open_boundary_graphs": len(groups) - closed, "boundary_is_not_automatically_a_hole": True}


def _component_uv_record(mesh: Any, polygon_indices: List[int], layer: Any) -> Dict[str, Any]:
    polygon_indices = sorted(polygon_indices)
    owner = {value: value for value in polygon_indices}
    def find(value: int) -> int:
        while owner[value] != value:
            owner[value] = owner[owner[value]]
            value = owner[value]
        return value
    def union(left: int, right: int) -> None:
        left, right = find(left), find(right)
        if left != right:
            owner[max(left, right)] = min(left, right)
    signatures: Dict[Any, List[int]] = {}
    values = []
    for polygon_index in polygon_indices:
        polygon = mesh.polygons[polygon_index]
        loops = list(polygon.loop_indices)
        for position, loop_index in enumerate(loops):
            following = loops[(position + 1) % len(loops)]
            uv = _locator_numbers(list(layer.data[loop_index].uv), 2, "component UV")
            uv_next = _locator_numbers(list(layer.data[following].uv), 2, "component UV")
            values.append({"loop_index": loop_index, "uv": uv})
            signature = (mesh.loops[loop_index].edge_index, tuple(sorted((tuple(uv), tuple(uv_next)))))
            signatures.setdefault(signature, []).append(polygon_index)
    for polygons in signatures.values():
        for polygon in polygons[1:]:
            union(polygons[0], polygon)
    islands: Dict[int, List[int]] = {}
    for polygon in polygon_indices:
        islands.setdefault(find(polygon), []).append(polygon)
    coordinates = [coordinate for value in values for coordinate in value["uv"]]
    uv_pairs = [value["uv"] for value in values]
    return {"loop_values": sorted(values, key=lambda row: row["loop_index"]), "loop_values_sha256": _promotion_digest(values),
            "uv_bounds": {"min": [min(row[axis] for row in uv_pairs) for axis in range(2)],
                          "max": [max(row[axis] for row in uv_pairs) for axis in range(2)]} if coordinates else None,
            "uv_island_count": len(islands), "uv_islands": sorted((sorted(value) for value in islands.values()), key=lambda row: row[0])}


def _component_material_record(job: Path, material: Any) -> Dict[str, Any]:
    if material is None:
        return {"name": None}
    nodes, links, images = [], [], []
    if material.use_nodes and material.node_tree is not None:
        for node in material.node_tree.nodes:
            nodes.append({"name": node.name, "type": node.bl_idname,
                          "inputs": [(socket.identifier, _promotion_value(socket.default_value) if hasattr(socket, "default_value") else None) for socket in node.inputs],
                          "outputs": [(socket.identifier, _promotion_value(socket.default_value) if hasattr(socket, "default_value") else None) for socket in node.outputs]})
            image = getattr(node, "image", None)
            if image is not None:
                packed = [hashlib.sha256(item.packed_file.data).hexdigest().upper() for item in image.packed_files]
                path = Path(bpy.path.abspath(image.filepath)).resolve() if image.filepath else None
                inside_job = False
                if path is not None:
                    try:
                        path.relative_to(job)
                        inside_job = True
                    except ValueError:
                        pass
                images.append({"node": node.name, "name": image.name, "filepath": image.filepath,
                               "packed_sha256": packed, "same_job_file_sha256": file_sha256(path) if not packed and inside_job and path.is_file() else None,
                               "external_unpacked_reference": bool(not packed and path is not None and not inside_job)})
        links = sorted((link.from_node.name, link.from_socket.identifier, link.to_node.name, link.to_socket.identifier) for link in material.node_tree.links)
    result = {"name": material.name, "library": material.library.filepath if material.library else None,
              "use_nodes": bool(material.use_nodes), "diffuse_color": _promotion_value(material.diffuse_color),
              "properties": _promotion_properties(material), "nodes": nodes, "links": links, "images": images}
    result["graph_sha256"] = _promotion_digest(result)
    return result


def _component_source_record(job: Path, mesh_obj: Any) -> Dict[str, Any]:
    mesh = mesh_obj.data
    if (not 1 <= len(mesh.vertices) <= 250000 or len(mesh.polygons) > 500000 or len(mesh.loops) > 1500000
            or len(mesh.edges) > 1000000 or len(mesh.uv_layers) > 8 or len(mesh_obj.vertex_groups) > 256 or len(mesh.materials) > 64):
        raise ValueError("Component-review source exceeds explicit geometry, UV, group, or material caps.")
    world_inverse = _mesh_region_matrix(mesh_obj.matrix_world, "component-review mesh world")
    normal_world = world_inverse.to_3x3().transposed()
    catalog = _component_index_catalog(len(mesh.vertices),
                                       ((edge.index, tuple(edge.vertices)) for edge in mesh.edges),
                                       ((polygon.index, tuple(polygon.vertices)) for polygon in mesh.polygons))
    polygon_to_component = {polygon: row["component_id"] for row in catalog for polygon in row["polygon_indices"]}
    for row in catalog:
        loops = sorted(loop_index for polygon_index in row["polygon_indices"] for loop_index in mesh.polygons[polygon_index].loop_indices)
        row["loop_indices"] = loops
        row["triangle_count"] = sum(max(0, len(mesh.polygons[index].vertices) - 2) for index in row["polygon_indices"])
        row["degenerate_polygon_indices"] = sorted(index for index in row["polygon_indices"] if len(set(mesh.polygons[index].vertices)) < 3 or mesh.polygons[index].area <= 1e-12)
        row.update(_component_boundary_record(mesh, row))
        has_faces, has_loose = bool(row["polygon_indices"]), bool(row["loose_edge_indices"])
        row["topology_class"] = "mixed" if has_faces and has_loose else ("surface" if has_faces else ("wire" if row["edge_indices"] else "point"))
        positions = []
        for index in row["vertex_indices"]:
            vertex = mesh.vertices[index]
            point = _locator_numbers(list(vertex.co), 3, "component position")
            world_point = _locator_numbers(list(mesh_obj.matrix_world @ vertex.co), 3, "component world position")
            normal = _locator_numbers(list(vertex.normal), 3, "component normal")
            defined = Vector(normal).length > 1e-12
            world_normal = _mesh_region_normal(vertex.normal, normal_world) if defined else [0.0, 0.0, 0.0]
            weights = []
            for assignment in vertex.groups:
                if not 0 <= assignment.group < len(mesh_obj.vertex_groups) or not math.isfinite(assignment.weight):
                    raise ValueError("Component review found an invalid vertex-group assignment.")
                weights.append({"group_index": assignment.group, "group_name": mesh_obj.vertex_groups[assignment.group].name, "weight": float(assignment.weight)})
            positions.append({"vertex_index": index, "object_position": point, "world_position": world_point,
                              "object_normal": normal, "world_normal": world_normal, "normal_defined": defined, "weights": weights})
        row["vertices"] = positions
        row["object_centroid"] = [sum(value["object_position"][axis] for value in positions) / len(positions) for axis in range(3)]
        row["world_centroid"] = [sum(value["world_position"][axis] for value in positions) / len(positions) for axis in range(3)]
        row["object_bounds"] = {"min": [min(value["object_position"][axis] for value in positions) for axis in range(3)],
                                "max": [max(value["object_position"][axis] for value in positions) for axis in range(3)]}
        row["world_bounds"] = {"min": [min(value["world_position"][axis] for value in positions) for axis in range(3)],
                               "max": [max(value["world_position"][axis] for value in positions) for axis in range(3)]}
        row["edges"] = [{"edge_index": index, "vertex_indices": list(mesh.edges[index].vertices)} for index in row["edge_indices"]]
        row["polygons"] = [{"polygon_index": index, "vertex_indices": list(mesh.polygons[index].vertices),
                            "loop_indices": list(mesh.polygons[index].loop_indices), "material_index": int(mesh.polygons[index].material_index)}
                           for index in row["polygon_indices"]]
        row["loops"] = [{"loop_index": index, "vertex_index": int(mesh.loops[index].vertex_index), "edge_index": int(mesh.loops[index].edge_index),
                         "object_normal": _locator_numbers(list(mesh.corner_normals[index].vector), 3, "component corner normal"),
                         "world_normal": _mesh_region_normal(mesh.corner_normals[index].vector, normal_world),
                         "uvs": {layer.name: _locator_numbers(list(layer.data[index].uv), 2, "component UV") for layer in mesh.uv_layers}}
                        for index in loops]
        row["uv_layers"] = {layer.name: _component_uv_record(mesh, row["polygon_indices"], layer) for layer in mesh.uv_layers}
        material_counts: Dict[int, Dict[str, int]] = {}
        for polygon_index in row["polygon_indices"]:
            polygon = mesh.polygons[polygon_index]
            slot = material_counts.setdefault(int(polygon.material_index), {"polygons": 0, "loops": 0})
            slot["polygons"] += 1
            slot["loops"] += len(polygon.loop_indices)
        row["material_coverage"] = [{"material_index": index, "material_name": mesh.materials[index].name if 0 <= index < len(mesh.materials) and mesh.materials[index] else None,
                                     **counts} for index, counts in sorted(material_counts.items())]
        row["membership_sha256"] = _promotion_digest({key: row[key] for key in ("vertex_indices", "edge_indices", "polygon_indices", "loop_indices")})
    result = {"mesh_name": mesh_obj.name, "mesh_data_name": mesh.name, "source_topology_sha256": _mesh_region_topology(mesh),
              "source_counts": {"vertices": len(mesh.vertices), "edges": len(mesh.edges), "polygons": len(mesh.polygons), "loops": len(mesh.loops), "components": len(catalog)},
              "object_transform": {"matrix_world": _locator_matrix_record(mesh_obj.matrix_world), "matrix_world_inverse": _locator_matrix_record(world_inverse),
                                   "location": _locator_numbers(list(mesh_obj.location), 3, "component object location"),
                                   "rotation_euler": _locator_numbers(list(mesh_obj.rotation_euler), 3, "component object rotation"),
                                   "scale": _locator_numbers(list(mesh_obj.scale), 3, "component object scale")},
              "material_slots": [_component_material_record(job, material) for material in mesh.materials], "components": catalog,
              "polygon_component_ids_sha256": _promotion_digest(sorted(polygon_to_component.items()))}
    result["component_catalog_sha256"] = _promotion_digest(catalog)
    return result


def _component_integrity(mesh_obj: Any, source_record: Dict[str, Any]) -> Dict[str, Any]:
    inventories = {}
    for label, collection in (("objects", bpy.data.objects), ("meshes", bpy.data.meshes), ("materials", bpy.data.materials),
                              ("images", bpy.data.images), ("collections", bpy.data.collections), ("scenes", bpy.data.scenes),
                              ("actions", bpy.data.actions), ("cameras", bpy.data.cameras), ("lights", bpy.data.lights), ("curves", bpy.data.curves)):
        inventories[label] = sorted((block.name, int(block.users), block.library.filepath if block.library else None) for block in collection)
    scenes = {scene.name: {"frame": int(scene.frame_current), "subframe": float(scene.frame_subframe),
                           "camera": scene.camera.name if scene.camera else None, "objects": sorted(obj.name for obj in scene.objects),
                           "render": (scene.render.engine, scene.render.resolution_x, scene.render.resolution_y, scene.render.resolution_percentage, scene.render.filepath)}
              for scene in bpy.data.scenes}
    objects = {obj.name: {"type": obj.type, "data": obj.data.name if obj.data else None, "world": _locator_matrix_record(obj.matrix_world),
                          "hide_render": bool(obj.hide_render), "hide_viewport": bool(obj.hide_viewport), "hide_get": bool(obj.hide_get()),
                          "selected": bool(obj.select_get()), "collections": sorted(owner.name for owner in obj.users_collection), "properties": _promotion_properties(obj)}
               for obj in bpy.data.objects}
    sections = {"inventory": inventories, "scenes": scenes, "objects": objects,
                "actions": _mesh_region_action_integrity(), "selected_source": source_record,
                "context": {"active_object": bpy.context.view_layer.objects.active.name if bpy.context.view_layer.objects.active else None,
                            "selected_mesh": mesh_obj.name}}
    return {"sha256": _promotion_digest(sections), "sections": {key: _promotion_digest(value) for key, value in sections.items()}}


def _component_emission_material(name: str, color: Tuple[float, float, float, float]) -> Any:
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    nodes = material.node_tree.nodes
    nodes.clear()
    output = nodes.new("ShaderNodeOutputMaterial")
    shader = nodes.new("ShaderNodeBsdfPrincipled")
    shader.inputs["Base Color"].default_value = color
    emission = shader.inputs.get("Emission Color") or shader.inputs.get("Emission")
    if emission is not None:
        emission.default_value = color
    strength = shader.inputs.get("Emission Strength")
    if strength is not None:
        strength.default_value = 1.0
    material.node_tree.links.new(shader.outputs["BSDF"], output.inputs["Surface"])
    return material


def _render_component_group(job: Path, request_id: str, mesh_obj: Any, components: List[Dict[str, Any]], views: List[str]) -> List[Dict[str, Any]]:
    prefix = f"CHAOSX_COMPONENT_REVIEW_{request_id}"
    old_scene = bpy.context.window.scene
    before_images = {image.name for image in bpy.data.images}
    scene = bpy.data.scenes.new(prefix)
    temporary_objects, temporary_meshes, temporary_curves, temporary_materials = [], [], [], []
    camera_data = bpy.data.cameras.new(prefix + "_Camera")
    camera = bpy.data.objects.new(prefix + "_Camera", camera_data)
    temporary_objects.append(camera)
    scene.collection.objects.link(camera)
    scene.camera = camera
    world = bpy.data.worlds.new(prefix + "_World")
    scene.world = world
    world.color = (0.01, 0.012, 0.016)
    palette = ((0.95, 0.20, 0.12, 1.0), (0.15, 0.75, 1.0, 1.0), (1.0, 0.72, 0.08, 1.0), (0.25, 1.0, 0.32, 1.0),
               (0.85, 0.25, 1.0, 1.0), (1.0, 0.42, 0.68, 1.0), (0.20, 1.0, 0.85, 1.0), (0.65, 0.78, 1.0, 1.0))
    dim = _component_emission_material(prefix + "_Dim", (0.055, 0.065, 0.08, 1.0))
    colors = [_component_emission_material(f"{prefix}_Color_{index}", palette[index % len(palette)]) for index in range(len(components))]
    temporary_materials.extend([dim, *colors])
    body_mesh = mesh_obj.data.copy()
    body_mesh.name = prefix + "_Mesh"
    temporary_meshes.append(body_mesh)
    body = bpy.data.objects.new(prefix + "_Body", body_mesh)
    temporary_objects.append(body)
    scene.collection.objects.link(body)
    body.matrix_world = mesh_obj.matrix_world.copy()
    body_mesh.materials.clear()
    body_mesh.materials.append(dim)
    for material in colors:
        body_mesh.materials.append(material)
    polygon_colors = {polygon: index + 1 for index, row in enumerate(components) for polygon in row["polygon_indices"]}
    for polygon in body_mesh.polygons:
        polygon.material_index = polygon_colors.get(polygon.index, 0)
    points = [mesh_obj.matrix_world @ Vector(corner) for corner in mesh_obj.bound_box]
    low = Vector([min(point[axis] for point in points) for axis in range(3)])
    high = Vector([max(point[axis] for point in points) for axis in range(3)])
    center, dimensions = (low + high) * 0.5, high - low
    span = max(float(max(dimensions)), 0.1)
    distance = span * 2.5
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = span * 1.55
    camera.data.clip_start = max(span * 0.001, 0.001)
    camera.data.clip_end = distance * 4.0
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 1024
    scene.render.resolution_y = 1024
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    view_positions = {"front": (center.x, center.y - distance, center.z), "rear": (center.x, center.y + distance, center.z),
                      "left": (center.x - distance, center.y, center.z), "right": (center.x + distance, center.y, center.z),
                      "top": (center.x, center.y, center.z + distance),
                      "three_quarter": (center.x + distance * 0.7, center.y - distance * 0.7, center.z + distance * 0.2)}
    previews = []
    bpy.context.window.scene = scene
    try:
        for view in views:
            camera.location = view_positions[view]
            camera_point_at(camera, center)
            bpy.context.view_layer.update()
            labels, swatches, leaders = [], [], []
            for index, row in enumerate(components):
                anchor = camera.matrix_world @ Vector((-span * 0.70, span * (0.52 - index * 0.065), -span * 0.05))
                text_data = bpy.data.curves.new(f"{prefix}_{view}_{index}_Text", type="FONT")
                temporary_curves.append(text_data)
                text_data.body = row["component_id"]
                text_data.align_x = "LEFT"
                text_data.size = span * 0.035
                label = bpy.data.objects.new(f"{prefix}_{view}_{index}_Label", text_data)
                temporary_objects.append(label)
                scene.collection.objects.link(label)
                label.data.materials.append(colors[index])
                label.location = anchor
                label.rotation_mode = "QUATERNION"
                label.rotation_quaternion = camera.rotation_quaternion.copy()
                labels.append(label)
                swatch_mesh = bpy.data.meshes.new(f"{prefix}_{view}_{index}_SwatchMesh")
                temporary_meshes.append(swatch_mesh)
                size = span * 0.018
                swatch_mesh.from_pydata([(-size, -size, 0), (size, -size, 0), (size, size, 0), (-size, size, 0)], [], [(0, 1, 2, 3)])
                swatch = bpy.data.objects.new(f"{prefix}_{view}_{index}_Swatch", swatch_mesh)
                temporary_objects.append(swatch)
                scene.collection.objects.link(swatch)
                swatch.data.materials.append(colors[index])
                swatch.location = anchor + camera.matrix_world.to_quaternion() @ Vector((-span * 0.035, span * 0.008, 0))
                swatch.rotation_mode = "QUATERNION"
                swatch.rotation_quaternion = camera.rotation_quaternion.copy()
                swatches.append(swatch)
                leader_data = bpy.data.curves.new(f"{prefix}_{view}_{index}_Leader", type="CURVE")
                temporary_curves.append(leader_data)
                leader_data.dimensions = "3D"
                leader_data.bevel_depth = span * 0.0015
                spline = leader_data.splines.new("POLY")
                spline.points.add(1)
                centroid = Vector(row["world_centroid"])
                spline.points[0].co = (*centroid, 1.0)
                spline.points[1].co = (*anchor, 1.0)
                leader = bpy.data.objects.new(f"{prefix}_{view}_{index}_Leader", leader_data)
                temporary_objects.append(leader)
                scene.collection.objects.link(leader)
                leader.data.materials.append(colors[index])
                leaders.append(leader)
            output = job / "blender" / "previews" / f"component_review_{request_id}_{view}.png"
            output.parent.mkdir(parents=True, exist_ok=True)
            if output.exists():
                raise FileExistsError(f"Component-review preview already exists: {output}")
            scene.render.filepath = str(output)
            bpy.ops.render.render(write_still=True)
            if not output.is_file() or output.stat().st_size < 1:
                raise RuntimeError("Component-review render did not produce a nonempty PNG.")
            previews.append({"view": view, "path": output.relative_to(job).as_posix(), "bytes": output.stat().st_size,
                             "sha256": file_sha256(output), "component_ids": [row["component_id"] for row in components],
                             "label_policy": "fixed_legend_color_swatch_and_centroid_leader", "small_or_occluded_identity_requires_visual_review": True})
            for obj in [*labels, *swatches, *leaders]:
                bpy.data.objects.remove(obj, do_unlink=True)
                temporary_objects.remove(obj)
    finally:
        bpy.context.window.scene = old_scene
        for obj in reversed(temporary_objects):
            if obj.name in bpy.data.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
        for data in reversed(temporary_meshes):
            if data.name in bpy.data.meshes and data.users == 0:
                bpy.data.meshes.remove(data)
        for data in reversed(temporary_curves):
            if data.name in bpy.data.curves and data.users == 0:
                bpy.data.curves.remove(data)
        for material in reversed(temporary_materials):
            if material.name in bpy.data.materials and material.users == 0:
                bpy.data.materials.remove(material)
        if camera_data.name in bpy.data.cameras and camera_data.users == 0:
            bpy.data.cameras.remove(camera_data)
        if scene.name in bpy.data.scenes:
            bpy.data.scenes.remove(scene)
        if world.name in bpy.data.worlds and world.users == 0:
            bpy.data.worlds.remove(world)
        for image in list(bpy.data.images):
            if image.name not in before_images:
                bpy.data.images.remove(image)
    return previews


def review_humanoid_components(req: Dict[str, Any]) -> Dict[str, Any]:
    context = _component_review_inputs(req)
    try:
        bpy.ops.wm.open_mainfile(filepath=str(context["source"]), use_scripts=False)
        mesh_obj = bpy.context.scene.objects.get(context["mesh_name"])
        if mesh_obj is None or mesh_obj.type != "MESH" or mesh_obj.library or mesh_obj.override_library or mesh_obj.data.library or mesh_obj.data.override_library:
            raise ValueError("Component review requires one exact local mesh object and data block.")
        if (mesh_obj.parent is not None or mesh_obj.modifiers or mesh_obj.constraints or mesh_obj.data.shape_keys
                or mesh_obj.animation_data or mesh_obj.data.animation_data):
            raise ValueError("Component review requires an unparented unrigged static mesh without modifiers, shape keys, constraints, or animation.")
        if any(value <= 0 for value in mesh_obj.scale):
            raise ValueError("Component review rejects negative or singular object scale.")
        source_record = _component_source_record(context["job"], mesh_obj)
        before = _component_integrity(mesh_obj, source_record)
        by_id = {row["component_id"]: row for row in source_record["components"]}
        if context["component_ids"]:
            missing = [value for value in context["component_ids"] if value not in by_id]
            if missing:
                raise ValueError(f"Unknown component_ids: {missing}")
            selected = [by_id[value] for value in context["component_ids"]]
            offset = None
        else:
            offset = context["component_offset"]
            if offset >= len(source_record["components"]):
                raise ValueError("Component-review page offset exceeds the component count.")
            selected = source_record["components"][offset:offset + context["component_limit"]]
        try:
            previews = _render_component_group(context["job"], context["request_id"], mesh_obj, selected, context["preview_view_names"])
        finally:
            after_record = _component_source_record(context["job"], mesh_obj)
            after = _component_integrity(mesh_obj, after_record)
            if before != after or source_record != after_record:
                changed = sorted(key for key in before["sections"] if before["sections"][key] != after["sections"].get(key))
                raise RuntimeError(f"Read-only component review changed original scene or mesh data sections: {changed}")
        next_offset = None if offset is None or offset + len(selected) >= len(source_record["components"]) else offset + len(selected)
        result = {"operation": "review_humanoid_components", "blend": context["source"].relative_to(context["job"]).as_posix(),
                  "source_sha256": context["expected_source_sha256"], "source_bytes": context["source_bytes"], "source_immutable": True,
                  "mesh_name": mesh_obj.name, "mesh_data_name": mesh_obj.data.name, "source_topology_sha256": source_record["source_topology_sha256"],
                  "component_catalog_sha256": source_record["component_catalog_sha256"], "component_count": len(source_record["components"]),
                  "component_page": {"explicit_ids": context["component_ids"], "offset": offset, "returned": len(selected), "limit": context["component_limit"],
                                     "truncated": next_offset is not None, "next_offset": next_offset, "component_ids": [row["component_id"] for row in selected]},
                  "source_record": source_record, "previews": previews, "render_group": True,
                  "component_identity_policy": "source_vertex_edge_polygon_connectivity_no_position_weld_no_semantic_classification",
                  "original_data_integrity_sha256": before["sha256"], "original_data_section_sha256": before["sections"],
                  "original_data_unchanged": True, "checkpoint_saved": False, "new_provider_call": False,
                  "semantic_component_acceptance": False, "weapon_separability_approved": False}
        # The report is evidence, not a presentation file. Compact separators
        # preserve every exact member while keeping dense production meshes
        # inside the reviewed 64 MiB ceiling without raising that ceiling.
        encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
        if len(encoded) > 64 * 1024 * 1024:
            raise ValueError("Component-review report exceeds the 64 MiB full-membership ceiling.")
        report_path = context["job"] / "blender" / "reports" / f"component_review_{context['request_id']}.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        if report_path.exists():
            raise FileExistsError(f"Component-review report already exists: {report_path}")
        report_path.write_bytes(encoded)
        result["report"] = report_path.relative_to(context["job"]).as_posix()
        result["report_bytes"] = len(encoded)
        result["report_sha256"] = file_sha256(report_path)
        return result
    finally:
        if file_sha256(context["source"]) != context["expected_source_sha256"] or context["source"].stat().st_size != context["source_bytes"]:
            raise RuntimeError("Read-only component review changed its source checkpoint.")


def inspect(req: Dict[str, Any]) -> Dict[str, Any]:
    if req["payload"].get("material_visibility") is not None:
        validate_preview_region(req["payload"].get("preview_region"), req["payload"].get("preview_resolution", 512))
        from material_visibility_probe import run_material_visibility_probe
        return run_material_visibility_probe(req, bpy=bpy, render_previews=render_previews, action_hash=_mesh_region_action_hash)
    if req["payload"].get("include_action_channels") is not None:
        return inspect_action_channels(req)
    if req["payload"].get("mesh_region") is not None:
        return inspect_mesh_region(req)
    job = Path(req["job_root"]).resolve()
    blend = within(job, req["payload"]["blend_rel"])
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    materials = []
    for material in bpy.data.materials:
        if not material.use_nodes or material.node_tree is None:
            continue
        shader = next(
            (node for node in material.node_tree.nodes if node.bl_idname == "ShaderNodeBsdfPrincipled"),
            None,
        )
        input_links = {}
        surface_links = []
        principled_defaults = {}
        output = next(
            (node for node in material.node_tree.nodes if node.bl_idname == "ShaderNodeOutputMaterial"),
            None,
        )
        if output is not None:
            surface_links = [
                {
                    "node": link.from_node.name,
                    "socket": link.from_socket.name,
                }
                for link in output.inputs["Surface"].links
            ]
        if shader is not None:
            for input_name in (
                "Base Color",
                "Metallic",
                "Roughness",
                "IOR",
                "Alpha",
                "Normal",
                "Emission Color",
                "Emission Strength",
            ):
                socket = shader.inputs.get(input_name)
                if socket is None:
                    continue
                input_links[input_name] = [
                    {
                        "node": link.from_node.name,
                        "socket": link.from_socket.name,
                    }
                    for link in socket.links
                ]
            for input_name in ("Metallic", "Specular IOR Level", "Emission Color", "Emission Strength"):
                socket = shader.inputs.get(input_name)
                if socket is not None and not socket.is_linked:
                    value = socket.default_value
                    principled_defaults[input_name] = list(value) if hasattr(value, "__len__") else value
        materials.append(
            {
                "name": material.name,
                "principled_inputs": input_links,
                "principled_defaults": principled_defaults,
                "surface_links": surface_links,
                "images": [
                    {
                        "node": node.name,
                        "image": node.image.name if node.image else None,
                        "filepath": node.image.filepath if node.image else None,
                    }
                    for node in material.node_tree.nodes
                    if node.bl_idname == "ShaderNodeTexImage"
                ],
            }
        )
    def object_transform(obj: bpy.types.Object) -> Dict[str, Any]:
        return {
            "location": [float(value) for value in obj.location],
            "rotation_euler": [float(value) for value in obj.rotation_euler],
            "scale": [float(value) for value in obj.scale],
            "dimensions": [float(value) for value in obj.dimensions],
            "matrix_world": [
                [float(value) for value in row]
                for row in obj.matrix_world
            ],
            "hidden": bool(obj.hide_get()),
            "chaosx_working": bool(obj.get("chaosx_working", False)),
            "chaosx_source_object": obj.get("chaosx_source_object"),
        }

    preview_paths = []
    action_name = str(req["payload"].get("action_name") or "")
    inspected_target_armature = None
    inspected_action_sha256 = None
    muted_nla_tracks: List[str] = []
    if action_name:
        rigs = armatures()
        requested_target_armature = str(req["payload"].get("target_armature_name") or "")
        if requested_target_armature:
            matching_rigs = [
                rig for rig in armatures(working_only=False)
                if rig.name == requested_target_armature
            ]
            if len(matching_rigs) != 1:
                raise RuntimeError(
                    f"Action inspection requires one exact target armature named {requested_target_armature}."
                )
            inspected_target_armature = matching_rigs[0]
            inspected_target_armature["chaosx_working"] = True
            promoted_meshes = []
            for obj in mesh_objects(working_only=False):
                if obj.parent is inspected_target_armature or any(
                    modifier.type == "ARMATURE" and modifier.object is inspected_target_armature
                    for modifier in obj.modifiers
                ):
                    obj["chaosx_working"] = True
                    obj.hide_render = False
                    promoted_meshes.append(obj.name)
            if not promoted_meshes:
                raise RuntimeError(
                    f"Action inspection found no direct mesh consumers for {requested_target_armature}."
                )
            rigs = [inspected_target_armature]
        action = bpy.data.actions.get(action_name)
        if len(rigs) != 1 or action is None:
            raise RuntimeError(f"Action inspection selection failed for {action_name}.")
        rigs[0].animation_data_create()
        for track in rigs[0].animation_data.nla_tracks:
            track.mute = True
            muted_nla_tracks.append(track.name)
        rigs[0].animation_data.action = action
        action_records = []
        for fcurve, slot in action_fcurves(action):
            action_records.append(
                {
                    "slot": getattr(slot, "identifier", None),
                    "data_path": fcurve.data_path,
                    "array_index": int(fcurve.array_index),
                    "keyframes": [
                        [
                            float(point.co.x),
                            float(point.co.y),
                            str(point.interpolation),
                        ]
                        for point in fcurve.keyframe_points
                    ],
                }
            )
        inspected_action_sha256 = hashlib.sha256(
            json.dumps(action_records, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest().upper()
        requested_frame = int(req["payload"].get("preview_frame", -1))
        if requested_frame < 0:
            start, end = action.frame_range
            requested_frame = int(round((start + end) * 0.5))
        bpy.context.scene.frame_set(requested_frame)
        bpy.context.view_layer.update()
    if req["payload"].get("render_previews"):
        runtime_stem = safe_name(str(req["payload"].get("runtime_stem") or blend.stem))
        region=req['payload'].get('preview_region')
        resolution=req['payload'].get('preview_resolution',512)
        validate_preview_region(region,resolution)
        if region is not None or resolution != 512:
            expected=req['payload'].get('expected_source_sha256','')
            if not expected or file_sha256(blend)!=expected.upper():
                raise ValueError('Focused preview requires exact source SHA-256.')
            runtime_stem=runtime_stem+'_focused_'+req['request_id'][:12]
        preview_paths = render_previews(job,runtime_stem,req['payload'].get('preview_view_names') or None,preview_region=region,preview_resolution=resolution)
    return {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "inspected_target_armature": inspected_target_armature.name if inspected_target_armature else None,
        "inspected_action_sha256": inspected_action_sha256,
        "muted_nla_tracks": muted_nla_tracks,
        "objects": [
            {
                "name": obj.name,
                "type": obj.type,
                "parent": obj.parent.name if obj.parent else None,
                "parent_type": obj.parent_type if obj.parent else None,
                "parent_bone": obj.parent_bone if obj.parent_type == "BONE" else None,
                "transform": object_transform(obj),
                "modifiers": [
                    {
                        "name": modifier.name,
                        "type": modifier.type,
                        "object": modifier.object.name if getattr(modifier, "object", None) else None,
                    }
                    for modifier in obj.modifiers
                ],
            }
            for obj in bpy.context.scene.objects
        ],
        "geometry": geometry_metrics(),
        "locators": locator_records(),
        "rig_and_actions": action_metrics(),
        "evaluated_actions": evaluated_action_metrics(req["payload"].get("action_name", ""), req["payload"].get("evaluated_frames"), req["payload"].get("target_armature_name", "")),
        "weights": weight_metrics(),
        "materials": materials,
        "pose_bones": [
            {
                "armature": rig.name,
                "bone": bone.name,
                "head": list(rig.matrix_world @ bone.head),
                "tail": list(rig.matrix_world @ bone.tail),
            }
            for rig in armatures()
            for bone in rig.pose.bones
        ],
        "previews": preview_paths,
    }


def extract_textures(req: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    processed = job / "textures" / "processed"
    processed.mkdir(parents=True, exist_ok=True)
    records = []
    image_paths: Dict[str, str] = {}
    if not payload.get("rewrite_to_dds"):
        for material, image in image_nodes():
            filename = safe_name(Path(image.name).stem) + ".png"
            output = processed / filename
            if image.packed_file is not None or image.source == "GENERATED":
                image.save_render(filepath=str(output))
            else:
                original = Path(bpy.path.abspath(image.filepath))
                if original.exists() and original.suffix.lower() in {".png", ".jpg", ".jpeg", ".tga", ".tif", ".tiff"}:
                    if original.resolve() != output.resolve():
                        if output.exists():
                            if not output.is_file():
                                raise RuntimeError(f"Processed texture target is not a file: {output}")
                            output.unlink()
                        shutil.copy2(original, output)
                else:
                    image.save_render(filepath=str(output))
            image.filepath = str(output)
            image.source = "FILE"
            image_paths[image.name] = str(output.relative_to(job)).replace("\\", "/")
            records.append(
                {
                    "material": material.name,
                    "image": image.name,
                    "processed_png": image_paths[image.name],
                    "bytes": output.stat().st_size,
                }
            )
    if payload.get("rewrite_to_dds"):
        dds_map = payload.get("dds_map", {})
        rename_images = bool(payload.get("rename_images", False))
        relink_nodes = list(image_nodes())
        if not relink_nodes:
            relink_nodes = all_image_nodes()
        if not relink_nodes:
            # io_pdx_mesh may retain image datablocks while omitting source
            # material tags; the explicit caller mapping is safe here.
            relink_nodes = [(None, image) for image in bpy.data.images if image.name in dds_map]
        for _, image in relink_nodes:
            original_name = image.name
            dds_rel = dds_map.get(original_name)
            if not dds_rel:
                image_stem = Path(original_name).stem.lower()
                for mapped_name, mapped_rel in dds_map.items():
                    if Path(mapped_name).stem.lower() in image_stem:
                        dds_rel = mapped_rel
                        break
            if dds_rel:
                image.filepath = str(within(job, dds_rel))
                image.source = "FILE"
                if rename_images:
                    image.name = Path(dds_rel).stem
    save_blend(blend)
    report = {"blend": str(blend.relative_to(job)).replace("\\", "/"), "textures": records}
    report_path = job / "blender" / "reports" / "textures.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def bake_static_mesh_transforms(req: Dict[str, Any]) -> Dict[str, Any]:
    """Bake approved static-building object transforms into mesh data."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(job, payload["output_blend_rel"], allow_missing=True)
    asset_kind = str(payload.get("asset_kind") or "")
    if asset_kind not in {"building", "static_building"}:
        raise RuntimeError("Static transform baking accepts only building or static_building profiles.")
    tolerance = float(payload.get("bounds_tolerance", 1e-5))
    if not math.isfinite(tolerance) or tolerance <= 0.0 or tolerance > 1e-3:
        raise RuntimeError("bounds_tolerance must be finite and within (0, 0.001].")

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Static transform baking found no approved chaosx_working mesh objects.")
    if armatures(working_only=False) or bpy.data.actions:
        raise RuntimeError("Static transform baking rejects scenes containing armatures or actions.")
    if any(obj.parent is not None for obj in working):
        raise RuntimeError("Static transform baking rejects parented working mesh objects.")
    if any(obj.modifiers for obj in working):
        raise RuntimeError("Static transform baking requires applied working mesh modifiers.")

    protected = [obj for obj in mesh_objects(working_only=False) if not obj.get("chaosx_working", False)]
    protected_data = {obj.data for obj in protected}
    if any(obj.data in protected_data for obj in working):
        raise RuntimeError("Working mesh data is shared with a protected source or reference object.")
    protected_before = {
        obj.name: {"transform": object_transform_record(obj), "bounds": bounds_record([obj])}
        for obj in protected
    }
    scene_before = bounds_record(working)
    object_records = []
    for obj in working:
        before_transform = object_transform_record(obj)
        matrix = obj.matrix_world.copy()
        flat_matrix = [float(value) for row in matrix for value in row]
        if not all(math.isfinite(value) for value in flat_matrix):
            raise RuntimeError(f"{obj.name} has a non-finite world transform.")
        if any(not math.isfinite(float(value)) or float(value) <= 0.0 for value in obj.scale):
            raise RuntimeError(f"{obj.name} has a non-positive or negative scale: {list(obj.scale)}")
        if matrix.to_3x3().determinant() <= 0.0:
            raise RuntimeError(f"{obj.name} has a negative or singular world transform.")

        object_before = bounds_record([obj])
        uv_layers_before = [layer.name for layer in obj.data.uv_layers]
        material_slots_before = [slot.material.name if slot.material else None for slot in obj.material_slots]
        mesh_name = obj.data.name
        object_name = obj.name
        obj.data.transform(matrix)
        obj.matrix_world = Matrix.Identity(4)
        obj.location = (0.0, 0.0, 0.0)
        obj.rotation_euler = (0.0, 0.0, 0.0)
        obj.scale = (1.0, 1.0, 1.0)
        obj.data.update()
        bpy.context.view_layer.update()

        object_after = bounds_record([obj])
        deltas = {
            key: [object_after[key][index] - object_before[key][index] for index in range(3)]
            for key in ("minimum", "maximum", "dimensions")
        }
        max_drift = max(abs(value) for values in deltas.values() for value in values)
        if max_drift > tolerance:
            raise RuntimeError(f"{obj.name} bounds drift {max_drift} exceeded tolerance {tolerance}.")
        if obj.name != object_name or obj.data.name != mesh_name:
            raise RuntimeError(f"{object_name} name changed during static transform baking.")
        if [layer.name for layer in obj.data.uv_layers] != uv_layers_before:
            raise RuntimeError(f"{obj.name} UV layers changed during static transform baking.")
        if [slot.material.name if slot.material else None for slot in obj.material_slots] != material_slots_before:
            raise RuntimeError(f"{obj.name} material slots changed during static transform baking.")
        object_records.append(
            {
                "object": obj.name,
                "before_transform": before_transform,
                "after_transform": object_transform_record(obj),
                "before_bounds": object_before,
                "after_bounds": object_after,
                "bounds_delta": deltas,
                "maximum_bounds_drift": max_drift,
                "ground_contact_delta": object_after["minimum"][2] - object_before["minimum"][2],
                "uv_layers": uv_layers_before,
                "material_slots": material_slots_before,
            }
        )

    identity_validation = require_identity_static_mesh_transforms()
    scene_after = bounds_record(working)
    scene_delta = {
        key: [scene_after[key][index] - scene_before[key][index] for index in range(3)]
        for key in ("minimum", "maximum", "dimensions")
    }
    maximum_scene_drift = max(abs(value) for values in scene_delta.values() for value in values)
    if maximum_scene_drift > tolerance:
        raise RuntimeError(f"Static working-scene bounds drift {maximum_scene_drift} exceeded tolerance {tolerance}.")
    protected_after = {
        obj.name: {"transform": object_transform_record(obj), "bounds": bounds_record([obj])}
        for obj in protected
    }
    if protected_after != protected_before:
        raise RuntimeError("A protected provider/source or vanilla reference object changed during baking.")

    save_blend(output)
    report = {
        "asset_kind": asset_kind,
        "source_blend": str(blend.relative_to(job)).replace("\\", "/"),
        "output_blend": str(output.relative_to(job)).replace("\\", "/"),
        "bounds_tolerance": tolerance,
        "scene_before_bounds": scene_before,
        "scene_after_bounds": scene_after,
        "scene_bounds_delta": scene_delta,
        "maximum_scene_bounds_drift": maximum_scene_drift,
        "protected_objects_verified_unchanged": sorted(protected_before),
        "objects": object_records,
        "identity_validation": identity_validation,
    }
    report_path = job / "blender" / "reports" / "static_transform_bake.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def partition_static_mesh_export_batches(req: Dict[str, Any]) -> Dict[str, Any]:
    """Partition static geometry into material batches without changing its shape."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(job, payload["output_blend_rel"], allow_missing=True)
    asset_kind = str(payload.get("asset_kind") or "")
    if asset_kind not in {"building", "static_building"}:
        raise RuntimeError("Static export batching accepts only building or static_building profiles.")
    maximum_vertices = int(payload.get("max_export_vertices_per_batch", 60000))
    if maximum_vertices < 3 or maximum_vertices > 65535:
        raise RuntimeError("max_export_vertices_per_batch must be within [3, 65535].")
    maximum_triangles = maximum_vertices // 3
    if maximum_triangles < 1:
        raise RuntimeError("The export batch vertex ceiling cannot contain one triangle.")

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Static export batching found no approved chaosx_working mesh objects.")
    if armatures(working_only=False) or bpy.data.actions:
        raise RuntimeError("Static export batching rejects scenes containing armatures or actions.")
    if any(obj.parent is not None for obj in working):
        raise RuntimeError("Static export batching rejects parented working mesh objects.")
    if any(obj.modifiers for obj in working):
        raise RuntimeError("Static export batching requires applied working mesh modifiers.")
    identity_before = require_identity_static_mesh_transforms()
    scene_before = bounds_record(working)
    geometry_before = geometry_metrics()
    object_records = []

    for obj in working:
        mesh = obj.data
        if any(len(poly.vertices) != 3 for poly in mesh.polygons):
            raise RuntimeError(f"{obj.name} must be triangulated before static export batching.")
        original_slot_count = len(mesh.materials)
        if original_slot_count == 0:
            raise RuntimeError(f"{obj.name} has no material slots to partition.")
        bounds_before = bounds_record([obj])
        transforms_before = object_transform_record(obj)
        uv_layers_before = [layer.name for layer in mesh.uv_layers]
        object_name = obj.name
        mesh_name = mesh.name
        batches = []

        for material_index in range(original_slot_count):
            polygons = [poly for poly in mesh.polygons if poly.material_index == material_index]
            if not polygons:
                continue
            material = mesh.materials[material_index]
            if material is None:
                raise RuntimeError(f"{obj.name} material slot {material_index} is empty.")
            polygons.sort(
                key=lambda poly: (
                    float(poly.center.x),
                    float(poly.center.y),
                    float(poly.center.z),
                    int(poly.index),
                )
            )
            batch_count = max(1, math.ceil(len(polygons) / maximum_triangles))
            slot_indices = [material_index]
            for batch_number in range(1, batch_count):
                batch_material = material.copy()
                batch_material.name = f"{material.name}_export_batch_{batch_number + 1:02d}"
                mesh.materials.append(batch_material)
                slot_indices.append(len(mesh.materials) - 1)
            for batch_number, start in enumerate(range(0, len(polygons), maximum_triangles)):
                batch_polygons = polygons[start:start + maximum_triangles]
                slot_index = slot_indices[batch_number]
                for poly in batch_polygons:
                    poly.material_index = slot_index
                triangle_count = len(batch_polygons)
                batches.append(
                    {
                        "source_material_index": material_index,
                        "source_material": material.name,
                        "batch_number": batch_number + 1,
                        "material_slot_index": slot_index,
                        "material": mesh.materials[slot_index].name,
                        "triangles": triangle_count,
                        "worst_case_export_vertices": triangle_count * 3,
                    }
                )

        mesh.update()
        bpy.context.view_layer.update()
        bounds_after = bounds_record([obj])
        maximum_drift = max(
            abs(bounds_after[key][axis] - bounds_before[key][axis])
            for key in ("minimum", "maximum", "dimensions")
            for axis in range(3)
        )
        if maximum_drift > 1e-7:
            raise RuntimeError(f"{obj.name} bounds changed during static export batching.")
        if obj.name != object_name or mesh.name != mesh_name:
            raise RuntimeError(f"{object_name} name changed during static export batching.")
        if object_transform_record(obj) != transforms_before:
            raise RuntimeError(f"{obj.name} transform changed during static export batching.")
        if [layer.name for layer in mesh.uv_layers] != uv_layers_before:
            raise RuntimeError(f"{obj.name} UV layers changed during static export batching.")
        if any(batch["worst_case_export_vertices"] > maximum_vertices for batch in batches):
            raise RuntimeError(f"{obj.name} produced an oversized static export batch.")
        object_records.append(
            {
                "object": obj.name,
                "source_material_slots": original_slot_count,
                "final_material_slots": len(mesh.materials),
                "maximum_bounds_drift": maximum_drift,
                "batches": batches,
            }
        )

    geometry_after = geometry_metrics()
    for key in ("objects", "vertices", "polygons", "triangles", "bounds_min", "bounds_max", "dimensions"):
        if geometry_after[key] != geometry_before[key]:
            raise RuntimeError(f"Static export batching changed geometry metric {key}.")
    identity_after = require_identity_static_mesh_transforms()
    scene_after = bounds_record(working)
    if scene_after != scene_before:
        raise RuntimeError("Static export batching changed working-scene bounds.")

    save_blend(output)
    report = {
        "asset_kind": asset_kind,
        "source_blend": str(blend.relative_to(job)).replace("\\", "/"),
        "output_blend": str(output.relative_to(job)).replace("\\", "/"),
        "max_export_vertices_per_batch": maximum_vertices,
        "max_triangles_per_batch": maximum_triangles,
        "geometry_before": geometry_before,
        "geometry_after": geometry_after,
        "scene_bounds_before": scene_before,
        "scene_bounds_after": scene_after,
        "identity_before": identity_before,
        "identity_after": identity_after,
        "objects": object_records,
    }
    report_path = job / "blender" / "reports" / "static_export_batch_partition.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def exported_mesh_streams(text_path: Path) -> List[Dict[str, Any]]:
    """Read actual arrays at object/material depth through the locked parser."""
    from skeletal_export_partition import exported_mesh_streams as read_streams
    return read_streams(text_path)


PROMOTION_METADATA_KEYS = (
    "chaosx_working", "chaosx_promotion_operation", "chaosx_promotion_source",
    "chaosx_promotion_source_sha256", "chaosx_promotion_validation",
    "chaosx_promotion_validation_sha256", "chaosx_promotion_job",
)


def _promotion_digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest().upper()


def _promotion_value(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Promotion fingerprint contains a nonfinite value.")
        return value
    if isinstance(value, bpy.types.ID):
        return {"id_type": value.bl_rna.identifier, "name": value.name_full, "library": value.library.filepath if value.library else None}
    if hasattr(value, "to_dict"):
        value = value.to_dict()
    if isinstance(value, dict):
        return {str(key): _promotion_value(item) for key, item in value.items()}
    if isinstance(value, set):
        return sorted(_promotion_value(item) for item in value)
    # mathutils values can implement the sequence protocol without __iter__.
    # Index every element and recurse; never stringify or round numeric data.
    if hasattr(value, "__len__") and hasattr(value, "__getitem__"):
        return [_promotion_value(value[index]) for index in range(len(value))]
    if hasattr(value, "__iter__"):
        return [_promotion_value(item) for item in value]
    raise ValueError(f"Unsupported promotion fingerprint value: {type(value).__name__}")


def _promotion_properties(block: Any, exclude: Iterable[str] = ()) -> Dict[str, Any]:
    return {key: _promotion_value(block[key]) for key in sorted(block.keys()) if key not in exclude}


def _promotion_scalars(block: Any) -> Dict[str, Any]:
    """Read finite scalar RNA settings and ID references, without traversing arbitrary RNA graphs."""
    result = {}
    for prop in block.bl_rna.properties:
        if prop.identifier == "rna_type":
            continue
        if prop.type in {"BOOLEAN", "INT", "FLOAT", "STRING", "ENUM"} and not prop.is_readonly:
            result[prop.identifier] = _promotion_value(getattr(block, prop.identifier))
        elif prop.type == "POINTER":
            value = getattr(block, prop.identifier)
            if value is None or isinstance(value, bpy.types.ID):
                result[prop.identifier] = _promotion_value(value)
    return result


def _promotion_path(job: Path, value: Any, suffix: str, *, missing: bool = False) -> Path:
    if not isinstance(value, str) or not value or value != value.strip() or ".." in Path(value).parts or "\\" in value:
        raise ValueError("Promotion paths must be explicit job-relative forward-slash paths without traversal.")
    path = within(job, value, allow_missing=missing)
    if path.suffix.lower() != suffix or (not missing and not path.is_file()):
        raise ValueError(f"Promotion requires a {suffix} file: {value}")
    return path


def _promotion_unique_pairs(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate validation JSON key: {key}")
        result[key] = value
    return result


def _promotion_inputs(req: Dict[str, Any]) -> Dict[str, Any]:
    payload = req["payload"]
    expected = {"blend_rel", "expected_source_sha256", "validation_rel", "expected_validation_sha256", "checkpoint_rel", "target_armature_name", "target_mesh_names", "mesh_rel", "expected_mesh_sha256", "anim_rel", "expected_anim_sha256"}
    if not isinstance(payload, dict) or set(payload) != expected:
        raise ValueError("promote_accepted_reimport accepts only its exact hashed-proof contract.")
    _locator_exact_name(req.get("job_id"), "job_id", locator=True)
    job = Path(req["job_root"]).resolve()
    inputs = {}
    for role, field, hash_field, suffix in (
        ("source", "blend_rel", "expected_source_sha256", ".blend"),
        ("validation", "validation_rel", "expected_validation_sha256", ".json"),
        ("mesh", "mesh_rel", "expected_mesh_sha256", ".mesh"),
        ("anim", "anim_rel", "expected_anim_sha256", ".anim"),
    ):
        path = _promotion_path(job, payload[field], suffix)
        expected_hash = payload[hash_field]
        if not isinstance(expected_hash, str) or re.fullmatch(r"[0-9A-Fa-f]{64}", expected_hash) is None:
            raise ValueError(f"{hash_field} must be an explicit SHA-256.")
        if path.stat().st_size == 0 or file_sha256(path) != expected_hash.upper():
            raise ValueError(f"Promotion {role} checksum mismatch or empty input.")
        inputs[role] = {"path": path, "relative": path.relative_to(job).as_posix(), "sha256": expected_hash.upper(), "bytes": path.stat().st_size}
    output = _promotion_path(job, payload["checkpoint_rel"], ".blend", missing=True)
    if output.parent != inputs["source"]["path"].parent or output.exists():
        raise ValueError("Promotion output must be a new sibling checkpoint; overwrite is forbidden.")
    report_path = within(job, f"blender/reports/promote_{output.stem}.json", allow_missing=True)
    if report_path.exists():
        raise ValueError("Promotion report already exists; overwrite is forbidden.")
    rig_name = _locator_exact_name(payload["target_armature_name"], "target_armature_name")
    mesh_names = payload["target_mesh_names"]
    if not isinstance(mesh_names, (list, tuple)) or not 1 <= len(mesh_names) <= 512:
        raise ValueError("Promotion requires one to 512 exact mesh names from the complete same-rig receipt.")
    mesh_names = [_locator_exact_name(name, "target_mesh_names") for name in mesh_names]
    if len(set(mesh_names)) != len(mesh_names) or rig_name in mesh_names:
        raise ValueError("Promotion object identities must be unique.")
    receipt = json.loads(inputs["validation"]["path"].read_text(encoding="utf-8-sig"), object_pairs_hook=_promotion_unique_pairs)
    _promotion_digest(receipt)  # Reject JSON NaN/Infinity, including otherwise unused fields.
    required = {"proof_blend", "mesh", "anim", "objects", "meshes", "armatures", "actions", "geometry", "animation_bounds", "previews", "runtime_texture_staging"}
    if not isinstance(receipt, dict) or not required.issubset(receipt) or receipt.get("status", "pass") != "pass" or receipt.get("error") or receipt.get("errors"):
        raise ValueError("Validation is not a complete successful reimport_export receipt.")
    for role, key, suffix in (("source", "proof_blend", ".blend"), ("mesh", "mesh", ".mesh"), ("anim", "anim", ".anim")):
        if _promotion_path(job, receipt[key], suffix) != inputs[role]["path"]:
            raise ValueError(f"Validation {key} does not match the explicitly hashed input.")
        hash_key = "proof_blend_sha256" if role == "source" else f"{role}_sha256"
        if hash_key in receipt and str(receipt[hash_key]).upper() != inputs[role]["sha256"]:
            raise ValueError(f"Validation {hash_key} conflicts with the accepted hash.")
    def rows(key: str) -> Dict[str, Any]:
        values = receipt[key]
        if not isinstance(values, list) or not values or any(not isinstance(row, dict) or not isinstance(row.get("name"), str) for row in values):
            raise ValueError(f"Invalid validation {key} identities.")
        by_name = {row["name"]: row for row in values}
        if len(by_name) != len(values):
            raise ValueError(f"Duplicate validation {key} identities.")
        return by_name
    objects, meshes, rigs = rows("objects"), rows("meshes"), rows("armatures")
    if set(meshes) != set(mesh_names) or set(rigs) != {rig_name}:
        raise ValueError("Validation does not identify exactly the requested rig and meshes.")
    if objects.get(rig_name, {}).get("type") != "ARMATURE" or any(objects.get(name, {}).get("type") != "MESH" for name in mesh_names):
        raise ValueError("Validation object types do not match the promotion targets.")
    if {name for name, row in objects.items() if row.get("type") == "MESH"} != set(mesh_names) or {name for name, row in objects.items() if row.get("type") == "ARMATURE"} != {rig_name}:
        raise ValueError("Validation has undeclared mesh/armature identities.")
    if type(rigs[rig_name].get("bones")) is not int or rigs[rig_name]["bones"] < 1:
        raise ValueError("Validation lacks a positive bone count.")
    for row in meshes.values():
        if any(type(row.get(key)) is not int or row[key] < 1 for key in ("vertices", "polygons")) or not isinstance(row.get("materials"), list) or not row["materials"] or any(not isinstance(name, str) or not name for name in row["materials"]):
            raise ValueError("Validation lacks complete mesh counts/material bindings.")
    actions = receipt["actions"]
    if not isinstance(actions, list) or not actions or any(not isinstance(name, str) or not name for name in actions) or len(set(actions)) != len(actions):
        raise ValueError("Validation must identify a nonempty unique existing action set.")
    bounds = receipt["animation_bounds"]
    if not isinstance(bounds, list) or not bounds or any(not isinstance(row, dict) or type(row.get("frame")) is not int or any(not isinstance(row.get(key), list) or len(row[key]) != 3 for key in ("bounds_min", "bounds_max", "dimensions")) for row in bounds):
        raise ValueError("Validation lacks successful animated reimport sample evidence.")
    for row in bounds:
        for key in ("bounds_min", "bounds_max", "dimensions"):
            _locator_numbers(row[key], 3, f"validation {key}")
        if any(row["bounds_min"][index] > row["bounds_max"][index] or row["dimensions"][index] < 0 for index in range(3)):
            raise ValueError("Validation has invalid animated bounds.")
    if not isinstance(receipt["previews"], list) or not receipt["previews"] or not isinstance(receipt["runtime_texture_staging"], list) or not isinstance(receipt["geometry"], dict):
        raise ValueError("Validation lacks complete reimport geometry/preview evidence.")
    if any(type(receipt["geometry"].get(key)) is not int or receipt["geometry"][key] < 1 for key in ("objects", "vertices", "polygons", "triangles")) or receipt["geometry"]["objects"] != len(meshes):
        raise ValueError("Validation lacks complete positive geometry counts.")
    return {"job": job, "inputs": inputs, "output": output, "report_path": report_path, "receipt": receipt, "rig_name": rig_name, "mesh_names": mesh_names, "receipt_objects": objects, "receipt_meshes": meshes, "receipt_rigs": rigs}


def _promotion_targets(context: Dict[str, Any]) -> List[bpy.types.Object]:
    targets = []
    for name, kind in [(context["rig_name"], "ARMATURE")] + [(name, "MESH") for name in context["mesh_names"]]:
        matches = [obj for obj in bpy.data.objects if obj.name == name]
        if len(matches) != 1 or matches[0].type != kind or bpy.context.scene.objects.get(name) != matches[0]:
            raise ValueError(f"Promotion requires one exact local scene {kind}: {name}")
        obj = matches[0]
        for block in (obj, obj.data, *obj.users_collection):
            if block.library or getattr(block, "override_library", None) or block.get("chaosx_source_protected") or block.get("chaosx_reference_read_only"):
                raise ValueError("Linked, overridden, protected source/vanilla/reference data cannot be promoted.")
        scale = _locator_numbers(list(obj.matrix_world.to_scale()), 3, "promotion world scale")
        if min(scale) <= 0 or obj.matrix_world.determinant() <= 0:
            raise ValueError("Promotion requires positive nonsingular transforms without reflection.")
        if obj.get("chaosx_working") or any(key in obj for key in PROMOTION_METADATA_KEYS[1:]):
            raise ValueError("Promotion source is already working or has conflicting promotion metadata.")
        targets.append(obj)
    rig = targets[0]
    if len(rig.data.bones) != context["receipt_rigs"][rig.name].get("bones"):
        raise ValueError("Promotion bone count differs from the accepted receipt.")
    if {obj.name: obj.type for obj in bpy.context.scene.objects} != {name: row.get("type") for name, row in context["receipt_objects"].items()}:
        raise ValueError("Promotion scene inventory differs from the accepted receipt.")
    if sorted(action.name for action in bpy.data.actions) != sorted(context["receipt"]["actions"]):
        raise ValueError("Promotion action identities differ from the accepted receipt.")
    for obj in targets[1:]:
        modifiers = list(obj.modifiers)
        if len(modifiers) != 1 or modifiers[0].type != "ARMATURE" or modifiers[0].object != rig:
            raise ValueError("Promotion mesh must have exactly one modifier consuming the exact accepted rig.")
        row = context["receipt_meshes"][obj.name]
        if not obj.data.vertices or len(obj.data.polygons) != row.get("polygons") or [mat.name if mat else None for mat in obj.data.materials] != row.get("materials"):
            raise ValueError("Promotion topology/material identity differs from the accepted receipt.")
        if not obj.data.materials or any(mat is None or not mat.use_nodes or not mat.get("shader") for mat in obj.data.materials):
            raise ValueError("Promotion requires the accepted PDX material bindings.")
        if obj.data.shape_keys:
            raise ValueError("Promotion does not support shape-key proof scenes.")
    return targets


def _promotion_animation_state(block: Any) -> Any:
    animation = getattr(block, "animation_data", None)
    if animation is None:
        return None
    if animation.drivers or animation.nla_tracks:
        raise ValueError("Promotion does not support driver/NLA proof scenes.")
    return _promotion_scalars(animation)


def _promotion_attribute_record(attribute: Any) -> Dict[str, Any]:
    """Hash every component through the observed Blender 5.1 attribute RNA field."""
    fields = {"FLOAT": "value", "INT": "value", "INT8": "value", "BOOLEAN": "value", "FLOAT_VECTOR": "vector", "FLOAT2": "vector", "FLOAT_COLOR": "color", "BYTE_COLOR": "color", "QUATERNION": "value", "FLOAT4X4": "value", "INT16_2D": "value", "INT32_2D": "value", "STRING": "value"}
    field = fields.get(attribute.data_type)
    if field is None:
        raise ValueError(f"Unsupported promotion mesh attribute: {attribute.data_type}")
    values = [_promotion_value(getattr(item, field)) for item in attribute.data]
    return {"domain": attribute.domain, "type": attribute.data_type, "sha256": _promotion_digest(values)}


def _promotion_discardable_material(record: Dict[str, Any]) -> bool:
    """Only independently unconsumed, unretained local material IDs may disappear."""
    return (
        type(record["users"]) is int and record["users"] == 0
        and record["local"] is True and record["fake_user"] is False
        and record["extra_user"] is False and record["protected"] is False
        and record["tree_retained"] is False
        and record["id_consumers"] == [] and record["mesh_slots"] == []
        and record["object_slots"] == []
    )


def _promotion_material_retention(materials: Dict[str, Any]) -> Dict[str, Any]:
    """Record complete native ID consumers without changing any retention flag."""
    blocks = list(bpy.data.materials)
    user_map = bpy.data.user_map(subset=blocks)
    inventory = {}
    for material in blocks:
        if material not in user_map:
            raise ValueError("Promotion material is absent from the native ID user map.")
        tree = material.node_tree
        record = {
            "record_sha256": _promotion_digest(materials[material.name]),
            "users": material.users, "fake_user": material.use_fake_user,
            "extra_user": material.use_extra_user,
            "local": material.library is None and material.override_library is None,
            "protected": any(bool(block.get(key)) for block in (material, tree) for key in ("chaosx_source_protected", "chaosx_reference_read_only")),
            "tree_retained": bool(tree.use_fake_user or tree.use_extra_user or tree.library or tree.override_library),
            "id_consumers": sorted((_promotion_value(block) for block in user_map[material]), key=lambda row: json.dumps(row, sort_keys=True)),
            "mesh_slots": sorted((mesh.name, index) for mesh in bpy.data.meshes for index, slot in enumerate(mesh.materials) if slot == material),
            "object_slots": sorted((obj.name, index, slot.link) for obj in bpy.data.objects for index, slot in enumerate(obj.material_slots) if slot.material == material),
        }
        record["discardable_orphan"] = _promotion_discardable_material(record)
        inventory[material.name] = record
    retained = {name: materials[name] for name, row in inventory.items() if not row["discardable_orphan"]}
    return {"inventory": inventory, "retained_sha256": _promotion_digest(retained)}


def _promotion_orphan_image_consumers(record: Dict[str, Any], removed_materials: Iterable[str]) -> bool:
    """Only images whose complete consumers are independently removable materials."""
    materials = set(record["material_consumers"])
    bindings = record["material_nodes"]
    return (
        bool(materials) and materials <= set(removed_materials)
        and materials == {row["material"] for row in bindings}
        and type(record["users"]) is int and record["users"] == len(bindings)
        and record["local"] is True and record["fake_user"] is False
        and record["extra_user"] is False and record["protected"] is False
        and record["other_id_consumers"] == [] and record["retained_node_trees"] == []
    )


def _promotion_image_retention(images: Dict[str, Any], material_retention: Dict[str, Any]) -> Dict[str, Any]:
    """Cross-check native ID users, direct node references, and embedded tree ownership."""
    blocks = sorted(bpy.data.images, key=lambda block: block.name)
    materials = sorted(bpy.data.materials, key=lambda block: block.name)
    trees = [material.node_tree for material in materials]
    user_map = bpy.data.user_map(subset=blocks + trees)
    inventory = {}
    for image in blocks:
        if image not in user_map:
            raise ValueError("Promotion image is absent from the native ID user map.")
        bindings, owners, retained_trees = [], [], []
        for material in materials:
            tree = material.node_tree
            nodes = [node for node in tree.nodes if getattr(node, "image", None) == image]
            if not nodes:
                continue
            if tree not in user_map:
                raise ValueError("Promotion image consumer tree is absent from the native ID user map.")
            owners.append(material)
            bindings.extend({"material": material.name, "tree": tree.name, "node": node.name} for node in sorted(nodes, key=lambda node: node.name))
            # Fresh embedded trees have one internal user; loaded orphan trees
            # can have zero. Neither count is an independent retention claim.
            if (not tree.is_embedded_data or tree.users not in {0, 1} or user_map[tree]
                    or tree.use_fake_user or tree.use_extra_user or tree.library or tree.override_library
                    or any(bool(tree.get(key)) for key in ("chaosx_source_protected", "chaosx_reference_read_only"))):
                retained_trees.append({"material": material.name, "tree": _promotion_value(tree),
                                       "users": tree.users, "id_consumers": sorted((_promotion_value(block) for block in user_map[tree]), key=lambda row: json.dumps(row, sort_keys=True))})
        allowed_ids = set(owners) | {material.node_tree for material in owners}
        native_users = user_map[image]
        content = images[image.name]
        record = {
            "record_sha256": _promotion_digest(content), "users": image.users,
            "local": image.library is None and image.override_library is None,
            "fake_user": image.use_fake_user, "extra_user": image.use_extra_user,
            "protected": any(bool(image.get(key)) for key in ("chaosx_source_protected", "chaosx_reference_read_only")),
            "material_nodes": bindings, "material_consumers": sorted(material.name for material in owners),
            "id_consumers": sorted((_promotion_value(block) for block in native_users), key=lambda row: json.dumps(row, sort_keys=True)),
            "other_id_consumers": sorted((_promotion_value(block) for block in native_users if block not in allowed_ids), key=lambda row: json.dumps(row, sort_keys=True)),
            "retained_node_trees": retained_trees, "packed_hashes": content["packed_hashes"],
            "pixel_sha256": content["pixel_sha256"], "missing_data_sentinel": content["missing_data_sentinel"],
            "source_file": {"path": str(Path(bpy.path.abspath(image.filepath)).resolve()), "sha256": content["file_sha256"]} if content["file_sha256"] else None,
        }
        # A complete native user map must independently identify every observed node owner.
        record["consumer_map_complete"] = all(material in native_users or material.node_tree in native_users for material in owners)
        record["exclusive_orphan_consumers"] = record["consumer_map_complete"] and _promotion_orphan_image_consumers(record, [name for name, row in material_retention["inventory"].items() if row["discardable_orphan"] and _promotion_discardable_material(row)])
        inventory[image.name] = record
    return {"inventory": inventory, "content_sha256": _promotion_digest(images)}


def _promotion_reopen_comparison(before: Dict[str, Any], after: Dict[str, Any]) -> Dict[str, Any]:
    """Exact preservation except native disappearance of proven before-only orphans."""
    mismatches, removed = [], []
    if set(before) != set(after):
        mismatches.append("fingerprint_fields")
    for key in set(before) | set(after):
        if key not in {"sha256", "material_retention", "image_retention"} and before.get(key) != after.get(key):
            mismatches.append(key)
    left_hashes, right_hashes = before["sha256"], after["sha256"]
    if set(left_hashes) != set(right_hashes):
        mismatches.append("sha256.fields")
    for key in set(left_hashes) | set(right_hashes):
        if key != "materials" and left_hashes.get(key) != right_hashes.get(key):
            mismatches.append(f"sha256.{key}")
    left, right = before["material_retention"], after["material_retention"]
    if left["retained_sha256"] != right["retained_sha256"]:
        mismatches.append("material_retention.retained_sha256")
    old, new = left["inventory"], right["inventory"]
    for name in sorted(set(old) | set(new)):
        path = f"material_retention.inventory[{name!r}]"
        if name not in old:
            mismatches.append(path + ".added")
        elif name in new:
            if old[name] != new[name]:
                mismatches.append(path + ".changed")
        elif old[name]["discardable_orphan"] is True and _promotion_discardable_material(old[name]):
            removed.append({"name": name, "reason": "native_save_dropped_zero_user_unretained_local_unprotected_material_without_id_or_slot_consumers", "before": old[name]})
        else:
            mismatches.append(path + ".required_material_missing")
    if not removed and left_hashes["materials"] != right_hashes["materials"]:
        mismatches.append("sha256.materials")
    released_images = []
    if "image_retention" in before and "image_retention" in after:
        left, right = before["image_retention"], after["image_retention"]
        if left["content_sha256"] != right["content_sha256"]:
            mismatches.append("image_retention.content_sha256")
        old, new = left["inventory"], right["inventory"]
        for name in sorted(set(old) | set(new)):
            path = f"image_retention.inventory[{name!r}]"
            if name not in old:
                mismatches.append(path + ".added")
            elif name not in new:
                mismatches.append(path + ".required_image_missing")
            elif old[name] != new[name]:
                # The datablock and pixels survive exactly; only native release of
                # every node in already accepted removed materials may differ.
                expected = dict(old[name], users=0, material_nodes=[], material_consumers=[],
                                id_consumers=[], exclusive_orphan_consumers=False)
                if (old[name]["exclusive_orphan_consumers"] is True
                        and old[name]["consumer_map_complete"] is True
                        and _promotion_orphan_image_consumers(old[name], [row["name"] for row in removed])
                        and new[name] == expected):
                    released_images.append({"name": name,
                        "reason": "image_content_and_packed_bytes_retained_exactly_only_accepted_removed_orphan_material_consumers_released",
                        "before": old[name], "after": new[name]})
                else:
                    mismatches.append(path + ".changed")
    return {"accepted": not mismatches, "mismatches": sorted(mismatches), "removed_orphan_materials": removed,
            "retained_images_with_released_orphan_consumers": released_images,
            "policy": "exact_all_image_content_and_ids_only_proven_removed_orphan_material_consumer_release"}


def _promotion_image_record(job, image):
    """Hash local images; only truly empty paths may use persisted finite pixels."""
    import struct
    # Resolve lazy file metadata before snapshotting load state. Reading size can load a DDS.
    image_size = list(image.size)
    packed = [hashlib.sha256(item.packed_file.data).hexdigest().upper() for item in image.packed_files]
    path = Path(bpy.path.abspath(image.filepath)).resolve() if image.filepath else None
    file_hash = None
    pixel_hash = None
    if not packed and path is not None:
        try:
            path.relative_to(job)
        except ValueError as exc:
            raise ValueError("Promotion texture image must be packed or inside the same job.") from exc
        if not path.is_file():
            raise ValueError("Promotion texture image is missing.")
        file_hash = file_sha256(path)
    elif not packed and not image.has_data:
        # An existing missing image is evidence of absent data, never fabricated pixels.
        # Preserve the sentinel and actual metadata across save/reopen; final material QA remains required.
        if len(image.pixels) != 0:
            raise ValueError(f"Inconsistent empty-path image state: name={image.name!r}, source={image.source!r}, size={list(image.size)!r}, has_data={image.has_data!r}")
    elif not packed:
        # Full datablock inventory includes native viewer buffers; retain their
        # exact finite pixel bytes under the same budget as empty-path images.
        if image.source not in {"FILE", "GENERATED", "VIEWER"}:
            raise ValueError(f"Unsupported loaded empty-path image: name={image.name!r}, source={image.source!r}, size={list(image.size)!r}, has_data={image.has_data!r}")
        width,height = list(image.size)
        channels = int(image.channels)
        count = len(image.pixels)
        if not (0 < width <= 4096 and 0 < height <= 4096 and 1 <= channels <= 4 and count == width*height*channels and count <= 4194304):
            raise ValueError("Empty-path image exceeds the finite four-million-channel pixel budget.")
        hasher = hashlib.sha256()
        for offset in range(0,count,4096):
            values = list(image.pixels[offset:min(offset+4096,count)])
            if any(not math.isfinite(value) for value in values):
                raise ValueError("Empty-path image contains nonfinite pixels.")
            hasher.update(struct.pack('<'+str(len(values))+'f',*values))
        pixel_hash = hasher.hexdigest().upper()
    return {"name":image.name,"has_data":bool(image.has_data) if path is None and not packed else None,"missing_data_sentinel":bool(not packed and path is None and not image.has_data),"material_validity":"missing_pixels_requires_material_review" if not packed and path is None and not image.has_data else "not_assessed","filepath":image.filepath,"size":image_size,"source":image.source,"alpha_mode":image.alpha_mode,"colorspace":image.colorspace_settings.name,"packed_hashes":packed,"file_sha256":file_hash,"pixel_sha256":pixel_hash,"pixel_encoding":"little_endian_float32" if pixel_hash else None,"settings":{key:_promotion_value(getattr(image,key)) for key in ("channels","is_float","generated_type","generated_width","generated_height","generated_color","use_generated_float","use_view_as_render") if hasattr(image,key)},"properties":_promotion_properties(image)}


def _promotion_fingerprint(job: Path, target_names: Iterable[str], *, exclude_action_name: str = "", include_sections: bool = False, cache_image_records: bool = True, image_cache_stats: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Exact pre/post fingerprints; no evaluated mesh, conversion, or data mutation."""
    target_names = set(target_names)
    objects, geometry, rigs, materials, images, actions = {}, {}, {}, {}, {}, {}
    # Local to this synchronous snapshot only; never shared across mutations or loads.
    import time
    image_cache, image_stats = {}, {"hits": 0, "misses": 0, "image_record_seconds": 0.0}
    def image_content(image):
        if cache_image_records and image in image_cache:
            image_stats["hits"] += 1
            return image_cache[image]
        started = time.perf_counter()
        record = _promotion_image_record(job, image)
        image_stats["image_record_seconds"] += time.perf_counter() - started
        image_stats["misses"] += 1
        if cache_image_records:
            image_cache[image] = record
        return record
    for obj in bpy.data.objects:
        if obj.library or obj.override_library or obj.constraints:
            raise ValueError("Promotion proof must contain local unconstrained objects only.")
        objects[obj.name] = {
            "type": obj.type, "data": _promotion_value(obj.data), "parent": _promotion_value(obj.parent),
            "parent_type": obj.parent_type, "parent_bone": obj.parent_bone,
            "world": _locator_matrix_record(obj.matrix_world), "basis": _locator_matrix_record(obj.matrix_basis),
            "parent_inverse": _locator_matrix_record(obj.matrix_parent_inverse), "dimensions": list(obj.dimensions),
            "bounds": [list(corner) for corner in obj.bound_box], "settings": _promotion_scalars(obj),
            "properties": _promotion_properties(obj, PROMOTION_METADATA_KEYS if obj.name in target_names else ()),
            "animation": _promotion_animation_state(obj),
            "modifiers": [_promotion_scalars(modifier) for modifier in obj.modifiers],
        }
        if obj.type == "MESH":
            mesh = obj.data
            attributes = {attribute.name: _promotion_attribute_record(attribute) for attribute in mesh.attributes}
            geometry[obj.name] = {
                "vertices": len(mesh.vertices), "polygons": len(mesh.polygons), "loops": len(mesh.loops),
                "positions_normals": _promotion_digest([[list(vertex.co), list(vertex.normal)] for vertex in mesh.vertices]),
                "edges": _promotion_digest([[list(edge.vertices), edge.use_seam, edge.use_edge_sharp] for edge in mesh.edges]),
                "topology": _promotion_digest([[list(face.vertices), face.material_index, face.use_smooth, list(face.normal)] for face in mesh.polygons]),
                "loops_normals": _promotion_digest([[loop.vertex_index, loop.edge_index] for loop in mesh.loops] + [list(normal.vector) for normal in mesh.corner_normals]),
                "uvs": _promotion_digest({layer.name: [list(item.uv) for item in layer.data] for layer in mesh.uv_layers}),
                "uv_settings": [(layer.name, layer.active_render, layer.active_clone) for layer in mesh.uv_layers],
                "uv_active_index": mesh.uv_layers.active_index, "has_custom_normals": mesh.has_custom_normals,
                "groups": [group.name for group in obj.vertex_groups],
                "weights": _promotion_digest([[(group.group, group.weight) for group in vertex.groups] for vertex in mesh.vertices]),
                "materials": [mat.name if mat else None for mat in mesh.materials], "attributes": attributes,
                "properties": _promotion_properties(mesh), "settings": _promotion_scalars(mesh),
            }
        elif obj.type == "ARMATURE":
            if any(bone.constraints for bone in obj.pose.bones):
                raise ValueError("Promotion does not support constrained pose bones.")
            rigs[obj.name] = {
                "properties": _promotion_properties(obj.data), "settings": _promotion_scalars(obj.data),
                "bones": [{"name": bone.name, "parent": bone.parent.name if bone.parent else None, "head": list(bone.head_local), "tail": list(bone.tail_local), "rest": _locator_matrix_record(bone.matrix_local), "properties": _promotion_properties(bone), "settings": _promotion_scalars(bone)} for bone in obj.data.bones],
                "pose": [{"name": bone.name, "matrix": _locator_matrix_record(bone.matrix), "basis": _locator_matrix_record(bone.matrix_basis), "properties": _promotion_properties(bone), "settings": _promotion_scalars(bone)} for bone in obj.pose.bones],
            }
    for material in bpy.data.materials:
        if material.library or material.override_library or not material.use_nodes:
            raise ValueError("Promotion requires local node-based materials.")
        tree = material.node_tree
        if tree.library or any(node.type == "GROUP" for node in tree.nodes):
            raise ValueError("Promotion does not support linked or grouped material node trees.")
        nodes = []
        for node in tree.nodes:
            nodes.append({"name": node.name, "type": node.bl_idname, "settings": _promotion_scalars(node), "properties": _promotion_properties(node), "inputs": [(socket.identifier, _promotion_value(socket.default_value) if hasattr(socket, "default_value") else None) for socket in node.inputs], "outputs": [(socket.identifier, _promotion_value(socket.default_value) if hasattr(socket, "default_value") else None) for socket in node.outputs]})
            image = getattr(node, "image", None)
            if image is not None:
                if image.library or image.override_library:
                    raise ValueError("Promotion cannot adopt linked texture images.")
                image_record = image_content(image)
                if not {"filepath", "packed_hashes", "file_sha256", "pixel_sha256"} <= set(image_record):
                    raise RuntimeError("Incomplete image fingerprint record.")
                images[image.name] = image_record
        materials[material.name] = {"properties": _promotion_properties(material), "settings": _promotion_scalars(material), "animation": _promotion_animation_state(material), "tree_properties": _promotion_properties(tree), "tree_animation": _promotion_animation_state(tree), "nodes": nodes, "links": [(link.from_node.name, link.from_socket.identifier, link.to_node.name, link.to_socket.identifier) for link in tree.links]}
    for image in bpy.data.images:
        if image.name not in images:
            images[image.name] = image_content(image)
    for action in bpy.data.actions:
        if exclude_action_name and action.name == exclude_action_name:
            continue
        if action.library or action.override_library or (action.users == 0 and not action.use_fake_user):
            raise ValueError("Promotion cannot preserve linked/overridden/unretained actions.")
        curves = []
        for curve, _ in action_fcurves(action):
            if curve.modifiers:
                raise ValueError("Promotion does not support modified action curves.")
            curves.append({"path": curve.data_path, "index": curve.array_index, "settings": _promotion_scalars(curve), "keys": [{"co": list(key.co), "left": list(key.handle_left), "right": list(key.handle_right), "settings": _promotion_scalars(key)} for key in curve.keyframe_points], "samples": [list(point.co) for point in curve.sampled_points]})
        actions[action.name] = {"range": list(action.frame_range), "fake_user": action.use_fake_user, "settings": _promotion_scalars(action), "properties": _promotion_properties(action), "curves": curves, "slots": [_promotion_scalars(slot) for slot in getattr(action, "slots", [])], "layers": [{"settings": _promotion_scalars(layer), "strips": [{"type": strip.type, "bags": [bag.slot_handle for bag in getattr(strip, "channelbags", [])]} for strip in layer.strips]} for layer in getattr(action, "layers", [])]}
    scene = bpy.context.scene
    sections = {"objects": objects, "geometry": geometry, "rigs": rigs, "materials": materials, "images": images, "actions": actions,
                "scene": {"fps": scene.render.fps, "fps_base": scene.render.fps_base, "frame": scene.frame_current, "subframe": scene.frame_subframe, "start": scene.frame_start, "end": scene.frame_end, "properties": _promotion_properties(scene), "collections": {collection.name: {"objects": sorted(obj.name for obj in collection.objects), "children": sorted(child.name for child in collection.children), "properties": _promotion_properties(collection)} for collection in bpy.data.collections}}}
    material_retention = _promotion_material_retention(materials)
    result = {"sha256": {key: _promotion_digest(value) for key, value in sections.items()}, "material_retention": material_retention, "image_retention": _promotion_image_retention(images, material_retention), "mesh_counts": {name: {key: row[key] for key in ("vertices", "polygons", "loops")} for name, row in geometry.items()}, "actions": sorted(actions), "objects": sorted(objects)}
    if include_sections:
        result["sections"] = sections
    if image_cache_stats is not None:
        image_cache_stats.update(image_stats, unique_images=len(images), cache_enabled=cache_image_records)
    return result


def promote_accepted_reimport(req: Dict[str, Any]) -> Dict[str, Any]:
    """Derive a metadata-only working copy from four explicitly hashed immutable proof inputs."""
    context = _promotion_inputs(req)
    job, output = context["job"], context["output"]
    inputs = context["inputs"]
    result = {"operation": "promote_accepted_reimport", "status": "fail", "new_provider_call": False,
              "checkpoint": output.relative_to(job).as_posix(), "report": context["report_path"].relative_to(job).as_posix(),
              "inputs": {role: {key: value for key, value in row.items() if key != "path"} for role, row in inputs.items()},
              "receipt_policy": "complete_legacy_reimport_export_receipt_bound_to_explicit_caller_hashes",
              "comparison_policy": "exact_fingerprints_with_proven_unretained_orphan_material_disappearance_only_no_tolerance_no_export_vertex_count_assumption"}
    try:
        bpy.ops.wm.open_mainfile(filepath=str(inputs["source"]["path"]), use_scripts=False)
        targets = _promotion_targets(context)
        names = [obj.name for obj in targets]
        before = _promotion_fingerprint(job, names)
        result["fingerprints_before"] = before
        metadata = {"chaosx_working": True, "chaosx_promotion_operation": "promote_accepted_reimport",
                    "chaosx_promotion_source": inputs["source"]["relative"], "chaosx_promotion_source_sha256": inputs["source"]["sha256"],
                    "chaosx_promotion_validation": inputs["validation"]["relative"], "chaosx_promotion_validation_sha256": inputs["validation"]["sha256"], "chaosx_promotion_job": req["job_id"]}
        result["permitted_metadata"] = {"targets": names, "before": {obj.name: {key: _promotion_value(obj[key]) for key in PROMOTION_METADATA_KEYS if key in obj} for obj in targets}, "after": metadata}
        for obj in targets:
            for key, value in metadata.items():
                obj[key] = value
        if _promotion_fingerprint(job, names) != before:
            raise RuntimeError("Promotion changed protected scene data before saving.")
        if output.exists():
            raise ValueError("Promotion checkpoint appeared during processing; refusing overwrite.")
        saved = bpy.ops.wm.save_as_mainfile(filepath=str(output), copy=True, relative_remap=False)
        if "FINISHED" not in saved or not output.is_file():
            raise RuntimeError("Promotion checkpoint save did not finish.")
        bpy.ops.wm.open_mainfile(filepath=str(output), use_scripts=False)
        after = _promotion_fingerprint(job, names)
        result["fingerprints_after"] = after
        result["reopen_comparison"] = _promotion_reopen_comparison(before, after)
        if not result["reopen_comparison"]["accepted"]:
            raise RuntimeError("Promotion saved/reopened invariant mismatch; output is not approved.")
        for name in names:
            obj = bpy.context.scene.objects.get(name)
            if obj is None or any(obj.get(key) != value for key, value in metadata.items()):
                raise RuntimeError("Promotion metadata did not survive reopening.")
        for role, row in inputs.items():
            if row["path"].stat().st_size != row["bytes"] or file_sha256(row["path"]) != row["sha256"]:
                raise RuntimeError(f"Immutable promotion {role} input changed during processing.")
        result.update(status="pass", source_immutable=True, all_inputs_immutable=True, checkpoint_sha256=file_sha256(output), checkpoint_bytes=output.stat().st_size)
    except Exception as exc:
        result["error"] = str(exc)
        result["output_approved"] = False
        result["input_immutability"] = {role: row["path"].is_file() and row["path"].stat().st_size == row["bytes"] and file_sha256(row["path"]) == row["sha256"] for role, row in inputs.items()}
        if output.is_file():
            result.update(checkpoint_sha256=file_sha256(output), checkpoint_bytes=output.stat().st_size)
        context["report_path"].parent.mkdir(parents=True, exist_ok=True)
        with context["report_path"].open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
        raise RuntimeError(f"Promotion failed; do not use output. Evidence: {result['report']}: {exc}") from exc
    context["report_path"].parent.mkdir(parents=True, exist_ok=True)
    with context["report_path"].open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    return result


def _locator_exact_name(value: Any, field: str, *, locator: bool = False) -> str:
    if not isinstance(value, str) or not value or value != value.strip() or "\x00" in value:
        raise ValueError(f"{field} must be a non-empty exact name without surrounding whitespace.")
    if locator and re.fullmatch(r"[a-z][a-z0-9_]{0,62}", value) is None:
        raise ValueError("locator_name must be stable lowercase snake_case (1-63 ASCII characters).")
    return value


def _locator_numbers(value: Any, size: int, field: str) -> List[float]:
    if not isinstance(value, (list, tuple)) or len(value) != size:
        raise ValueError(f"{field} requires exactly {size} finite numbers.")
    if any(isinstance(item, bool) or not isinstance(item, (int, float)) or not math.isfinite(item) for item in value):
        raise ValueError(f"{field} requires exactly {size} finite numbers.")
    return [float(item) for item in value]


def _locator_request(req: Dict[str, Any]) -> Tuple[Path, Path, Path, str, str, str, List[float], List[float]]:
    payload = req["payload"]
    expected = {"blend_rel", "checkpoint_rel", "target_armature_name", "parent_bone", "locator_name", "bone_local_position", "bone_local_rotation_xyzw"}
    if set(payload) != expected:
        raise ValueError("author_locator accepts only its exact named, measured locator contract.")
    job = Path(req["job_root"]).resolve()
    _locator_exact_name(req.get("job_id"), "job_id", locator=True)
    for field in ("blend_rel", "checkpoint_rel"):
        value = payload[field]
        if not isinstance(value, str) or ".." in Path(value).parts:
            raise ValueError(f"{field} must be a job-relative checkpoint path without traversal.")
    source = within(job, payload["blend_rel"])
    output = within(job, payload["checkpoint_rel"], allow_missing=True)
    if not source.is_file() or source.suffix.lower() != ".blend" or output.suffix.lower() != ".blend":
        raise ValueError("author_locator requires .blend checkpoint files.")
    if source == output or output.exists():
        raise ValueError("author_locator requires a new checkpoint and never overwrites an existing path.")
    if source.parent != output.parent:
        raise ValueError("Locator checkpoints must be siblings to preserve all relative material paths.")
    armature_name = _locator_exact_name(payload["target_armature_name"], "target_armature_name")
    bone_name = _locator_exact_name(payload["parent_bone"], "parent_bone")
    name = _locator_exact_name(payload["locator_name"], "locator_name", locator=True)
    position = _locator_numbers(payload["bone_local_position"], 3, "bone_local_position")
    rotation = _locator_numbers(payload["bone_local_rotation_xyzw"], 4, "bone_local_rotation_xyzw")
    if abs(math.hypot(*rotation) - 1.0) > 1e-6:
        raise ValueError("bone_local_rotation_xyzw must be a unit quaternion; implicit normalization is forbidden.")
    return job, source, output, armature_name, bone_name, name, position, rotation


def _locator_registration(job: Path, job_id: str, name: str, rig_name: str, bone_name: str) -> Dict[str, Any]:
    return {
        "chaosx_export_locator": True,
        "chaosx_locator_registry_version": LOCATOR_REGISTRY_VERSION,
        "chaosx_locator_owner_job": job_id,
        "chaosx_locator_owner_root": hashlib.sha256(os.path.normcase(str(job.resolve())).encode("utf-8")).hexdigest(),
        "chaosx_locator_name": name,
        "chaosx_locator_armature": rig_name,
        "chaosx_locator_parent_bone": bone_name,
    }


def _locator_matrix_record(matrix: Matrix) -> List[List[float]]:
    values = [[float(value) for value in row] for row in matrix]
    if len(values) != 4 or any(len(row) != 4 for row in values) or any(not math.isfinite(value) for row in values for value in row):
        raise ValueError("Locator transforms must be finite 4x4 matrices.")
    return values


def _locator_bone_world(rig: bpy.types.Object, bone_name: str, *, rest: bool = False) -> Matrix:
    bone_matrix = rig.data.bones[bone_name].matrix_local if rest or rig.data.pose_position == "REST" else rig.pose.bones[bone_name].matrix
    matrix = rig.matrix_world @ bone_matrix
    _locator_matrix_record(matrix)
    if abs(matrix.determinant()) < 1e-12:
        raise ValueError("Locator parent has a singular transform.")
    return matrix


def _locator_parent(rig_name: str, bone_name: str) -> bpy.types.Object:
    matches = [obj for obj in bpy.data.objects if obj.name == rig_name]
    rig = matches[0] if len(matches) == 1 else None
    if rig is None or rig.type != "ARMATURE" or bpy.context.scene.objects.get(rig_name) != rig:
        raise ValueError(f"Locator requires one exact scene armature: {rig_name}")
    if rig.library or rig.override_library or rig.data.library or rig.get("chaosx_source_protected") or rig.get("chaosx_reference_read_only"):
        raise ValueError("Locator parent cannot be linked, overridden, or a protected source/reference rig.")
    if bone_name not in rig.data.bones or bone_name not in rig.pose.bones:
        raise ValueError(f"Locator parent bone does not exist: {rig_name}/{bone_name}")
    rig_scale = _locator_numbers(list(rig.matrix_world.to_scale()), 3, "locator armature world scale")
    if min(rig_scale) <= 0.0 or max(rig_scale) - min(rig_scale) > 1e-5 or rig.matrix_world.determinant() <= 0.0:
        raise ValueError("Locator authoring/export requires a positive uniform armature world scale without reflection.")
    _locator_bone_world(rig, bone_name)
    return rig


def _validate_registered_locator(obj: bpy.types.Object, rig: bpy.types.Object, bone_name: str, registration: Dict[str, Any]) -> None:
    if obj.type != "EMPTY" or obj.data is not None or obj.library or obj.override_library:
        raise ValueError("Locator name collision: only a local registered Empty may be updated/exported.")
    if bpy.context.scene.objects.get(obj.name) != obj or any(obj.get(key) != value for key, value in registration.items()):
        raise ValueError("Locator name collision or ownership/registration mismatch.")
    if obj.parent != rig or obj.parent_type != "BONE" or obj.parent_bone != bone_name:
        raise ValueError("Registered locator has a different parent; automatic reparenting is forbidden.")
    if obj.constraints or obj.modifiers or obj.animation_data or obj.children or obj.instance_type != "NONE":
        raise ValueError("Registered locator must be a non-animated, non-instancing leaf Empty without constraints or modifiers.")
    if obj.get("chaosx_source_protected") or obj.get("chaosx_reference_read_only"):
        raise ValueError("Protected source/reference locators cannot be updated/exported.")
    users = bpy.data.user_map(subset=[obj]).get(obj, set())
    if any(not isinstance(user, (bpy.types.Scene, bpy.types.Collection)) for user in users):
        raise ValueError("Locator is referenced by another data-block; non-deforming leaf ownership is required.")
    _locator_matrix_record(obj.matrix_world)
    _locator_matrix_record(obj.matrix_basis)
    _locator_matrix_record(obj.matrix_parent_inverse)


def locator_records(objects: Optional[Iterable[bpy.types.Object]] = None) -> List[Dict[str, Any]]:
    """Report true bone-head-local transforms, not Object.matrix_local (armature-relative)."""
    records = []
    for obj in bpy.context.scene.objects if objects is None else objects:
        if obj.type != "EMPTY" or obj.data is not None:
            continue
        record = {
            "name": obj.name,
            "parent": obj.parent.name if obj.parent else None,
            "parent_type": obj.parent_type if obj.parent else None,
            "parent_bone": obj.parent_bone if obj.parent_type == "BONE" else None,
            "matrix_world": _locator_matrix_record(obj.matrix_world),
            "matrix_basis": _locator_matrix_record(obj.matrix_basis),
            "matrix_parent_inverse": _locator_matrix_record(obj.matrix_parent_inverse),
            "registered_for_export": bool(obj.get("chaosx_export_locator", False)),
            "owner_job": obj.get("chaosx_locator_owner_job"),
            "frame": int(bpy.context.scene.frame_current),
        }
        if obj.parent and obj.parent.type == "ARMATURE" and obj.parent_type == "BONE" and obj.parent_bone in obj.parent.data.bones:
            record["bone_local_matrix"] = _locator_matrix_record(_locator_bone_world(obj.parent, obj.parent_bone).inverted() @ obj.matrix_world)
            record["rest_bone_relative_matrix"] = _locator_matrix_record(_locator_bone_world(obj.parent, obj.parent_bone, rest=True).inverted() @ obj.matrix_world)
        records.append(record)
    return sorted(records, key=lambda item: item["name"])


def author_locator(req: Dict[str, Any]) -> Dict[str, Any]:
    """Modify exactly one registered Empty in a new checkpoint; no mesh, bone or action editing."""
    job, source, output, rig_name, bone_name, name, position, rotation = _locator_request(req)
    source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest().upper()
    bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
    rig = _locator_parent(rig_name, bone_name)
    if any(name in candidate.data.bones for candidate in armatures(working_only=False)):
        raise ValueError("Locator name collides with a skeleton bone.")
    registration = _locator_registration(job, req["job_id"], name, rig_name, bone_name)
    matches = [obj for obj in bpy.data.objects if obj.name == name]
    if len(matches) > 1:
        raise ValueError("Duplicate locator names are ambiguous; no object may be adopted or renamed.")
    locator = matches[0] if matches else None
    if locator is not None:
        _validate_registered_locator(locator, rig, bone_name, registration)
    # Do not change fake-user flags through save_blend. Unretained actions would
    # be lost on reopening, so fail before touching the locator instead.
    unretained = [action.name for action in bpy.data.actions if action.users == 0 and not action.use_fake_user]
    if unretained:
        raise ValueError(f"Checkpoint contains unretained actions; locator-only save cannot preserve them: {unretained}")
    actions_before = {action.name: _export_checkpoint_action_snapshot(action) for action in bpy.data.actions}
    created = locator is None
    if created:
        locator = bpy.data.objects.new(name, None)
        if locator.name != name:
            raise RuntimeError("Blender changed the requested locator name; refusing an ambiguous locator.")
        bpy.context.scene.collection.objects.link(locator)
        locator.empty_display_type = "PLAIN_AXES"
        locator.parent = rig
        locator.parent_type = "BONE"
        locator.parent_bone = bone_name
        for key, value in registration.items():
            locator[key] = value
    # Setting world space after exact bone parenting lets Blender account for
    # its bone-tail parent offset without pretending matrix_local is bone-local.
    local = Matrix.Translation(position) @ Quaternion((rotation[3], *rotation[:3])).to_matrix().to_4x4()
    locator.matrix_parent_inverse = Matrix.Identity(4)
    locator.matrix_basis = Matrix.Identity(4)
    bpy.context.view_layer.update()
    locator.matrix_world = _locator_bone_world(rig, bone_name) @ local
    bpy.context.view_layer.update()
    actual = _locator_bone_world(rig, bone_name).inverted() @ locator.matrix_world
    delta = max(abs(actual[row][col] - local[row][col]) for row in range(4) for col in range(4))
    if not math.isfinite(delta) or delta > LOCATOR_TRANSFORM_TOLERANCE:
        raise RuntimeError(f"Locator bone-local transform did not round-trip through Blender parenting: {delta}")
    _validate_registered_locator(locator, rig, bone_name, registration)
    if actions_before != {action.name: _export_checkpoint_action_snapshot(action) for action in bpy.data.actions}:
        raise RuntimeError("Locator authoring altered existing action data.")
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise ValueError("Locator checkpoint output appeared during processing; refusing overwrite.")
    saved = bpy.ops.wm.save_as_mainfile(filepath=str(output), copy=True, relative_remap=False)
    if "FINISHED" not in saved or not output.is_file():
        raise RuntimeError("Blender did not save the requested locator checkpoint.")
    if hashlib.sha256(source.read_bytes()).hexdigest().upper() != source_sha256:
        raise RuntimeError("The input checkpoint changed during locator authoring.")
    return {
        "source": source.relative_to(job).as_posix(),
        "source_sha256": source_sha256,
        "checkpoint": output.relative_to(job).as_posix(),
        "checkpoint_sha256": hashlib.sha256(output.read_bytes()).hexdigest().upper(),
        "checkpoint_bytes": output.stat().st_size,
        "operation": "author_locator",
        "created": created,
        "locator": locator_records([locator])[0],
        "requested_bone_local_position": position,
        "requested_bone_local_rotation_xyzw": rotation,
        "bone_local_matrix_max_error": delta,
        "actions_verified_unchanged": sorted(actions_before),
        "policy": "one_registered_leaf_empty_only_no_mesh_material_weight_bone_action_or_scale_edits",
    }


def approved_export_locators(job: Path, job_id: str, working: List[bpy.types.Object]) -> List[bpy.types.Object]:
    """Select only registered locators on approved rigs exported by a mesh modifier."""
    exported_rigs = set()
    for mesh in working:
        modifiers = [modifier for modifier in mesh.modifiers if modifier.type == "ARMATURE"]
        if modifiers and modifiers[0].object is not None:
            exported_rigs.add(modifiers[0].object)  # matches io_pdx_mesh get_rig_from_mesh
    locators = []
    for obj in bpy.context.scene.objects:
        if not obj.get("chaosx_export_locator", False):
            continue
        name = _locator_exact_name(obj.name, "locator_name", locator=True)
        rig_name = _locator_exact_name(obj.get("chaosx_locator_armature"), "registered armature")
        bone_name = _locator_exact_name(obj.get("chaosx_locator_parent_bone"), "registered parent bone")
        rig = _locator_parent(rig_name, bone_name)
        registration = _locator_registration(job, job_id, name, rig_name, bone_name)
        _validate_registered_locator(obj, rig, bone_name, registration)
        if rig not in exported_rigs:
            continue
        if not rig.get("chaosx_working", False):
            raise ValueError("Registered locator parent is not an approved working export rig.")
        # The extension exports only the first root and skips pdxIgnoreJoint branches.
        bone = rig.data.bones[bone_name]
        while bone.parent is not None:
            if bone.get("pdxIgnoreJoint", False):
                raise ValueError("Locator parent is excluded from the exported skeleton.")
            bone = bone.parent
        # RNA access can produce distinct Python wrappers for the same bone.
        if bone != rig.data.bones[0]:
            raise ValueError("Locator parent is outside the exporter's first-root skeleton.")
        if any(name in candidate.data.bones for candidate in exported_rigs):
            raise ValueError("Locator name collides with an exported skeleton bone.")
        if sum(bone_name in candidate.data.bones for candidate in exported_rigs) != 1:
            raise ValueError("Locator parent bone is ambiguous across exported rigs.")
        locators.append(obj)
    return sorted(locators, key=lambda obj: obj.name)


def export_mesh(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(job, payload["output_rel"], allow_missing=True)
    explicit_checkpoint = payload.get("checkpoint_rel")
    exported_checkpoint = within(job, explicit_checkpoint, allow_missing=True) if explicit_checkpoint else job / "blender" / "checkpoints" / "06_exported.blend"
    if explicit_checkpoint and (exported_checkpoint.suffix != ".blend" or exported_checkpoint.parent != blend.parent or exported_checkpoint == blend or exported_checkpoint.exists()):
        raise ValueError("Explicit export checkpoint must be a new sibling .blend; overwrite is forbidden.")
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend), use_scripts=False)
    pdx = load_pdx(req["io_pdx_root"])
    working = [
        obj for obj in bpy.context.scene.objects
        if obj.type == "MESH" and obj.get("chaosx_working", False)
    ]
    if not working:
        raise RuntimeError("Mesh export found no approved chaosx_working mesh objects.")
    pdx_meshes = set(pdx["list_scene_pdx_meshes"]())
    locators = approved_export_locators(job, req["job_id"], [obj for obj in working if obj in pdx_meshes])
    locator_local = {obj.name: _locator_bone_world(obj.parent, obj.parent_bone).inverted() @ obj.matrix_world for obj in locators}
    export_transforms = prepare_pdx_export_transforms()
    locator_scale = float(export_transforms.get("armature_data_scale_factor", 1.0))
    if abs(locator_scale - 1.0) > 1e-6:
        for obj in locators:
            local = locator_local[obj.name]
            local.translation *= locator_scale
            obj.matrix_world = _locator_bone_world(obj.parent, obj.parent_bone) @ local
        bpy.context.view_layer.update()
    bpy.ops.object.select_all(action="DESELECT")
    for obj in working + locators:
        obj.select_set(True)
    if {obj.name for obj in bpy.context.selected_objects} != {obj.name for obj in working + locators}:
        raise RuntimeError("Mesh export selection differs from approved meshes and registered locators.")
    bpy.context.view_layer.objects.active = working[0]
    for old_output in (output, output.with_suffix(".txt")):
        if old_output.exists():
            if not old_output.is_file():
                raise RuntimeError(f"Mesh export target is not a file: {old_output}")
            old_output.unlink()
    # Locator serialization uses rest-bone matrices in io_pdx_mesh 0.91.0.
    # Evaluate only the approved locator rigs in REST, then restore their pose
    # display state even if the exporter fails; no action keys are changed.
    locator_pose_positions = {obj.parent: obj.parent.data.pose_position for obj in locators}
    try:
        for rig in locator_pose_positions:
            rig.data.pose_position = "REST"
        bpy.context.view_layer.update()
        exported_locators = locator_records(locators)
        pdx["export_meshfile"](
            str(output),
            exp_mesh=True,
            exp_skel=True,
            exp_locs=True,
            exp_selected=True,
            as_blendshape=False,
            debug_mode=True,
            # The HOI4 renderer's supported vertex/index envelope is materially
            # lower than the per-loop vertex stream produced by split_verts=True.
            # The pinned 0.91 exporter has an O(n^2) de-duplication pass when this
            # is false, but the shared-vertex route is required for runtime-safe
            # humanoid exports. A diagnostic may opt into split vertices explicitly.
            split_verts=bool(payload.get("split_verts", False)),
            sort_verts="+",
            plain_txt=True,
        )
    finally:
        for rig, pose_position in locator_pose_positions.items():
            rig.data.pose_position = pose_position
        bpy.context.view_layer.update()
    text_output = output.with_suffix(".txt")
    streams = exported_mesh_streams(text_output)
    from skeletal_export_partition import require_bounded_export_streams
    require_bounded_export_streams(streams)
    save_blend(exported_checkpoint)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "mesh": str(output.relative_to(job)).replace("\\", "/"),
        "mesh_bytes": output.stat().st_size,
        "mesh_text": str(output.with_suffix(".txt").relative_to(job)).replace("\\", "/")
        if output.with_suffix(".txt").exists()
        else None,
        "mesh_streams": streams,
        "maximum_stream_vertices": max(stream["vertices"] for stream in streams),
        "maximum_stream_triangle_indices": max(stream["triangle_indices"] for stream in streams),
        "vertex_stream_limit": 65535,
        "conservative_triangle_index_entry_budget": 65535,
        "exported_checkpoint": str(exported_checkpoint.relative_to(job)).replace("\\", "/"),
        "geometry": geometry_metrics(),
        "export_transforms": export_transforms,
        "locators": exported_locators,
        "selected_export_objects": sorted(obj.name for obj in working + locators),
        "locator_coordinate_policy": "bone_head_local_rest_export_with_uniform_rig_scale_conversion",
        "warnings": [],
    }
    report = job / "blender" / "reports" / "export_mesh.json"
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def select_armature_and_action(action_name: str) -> Tuple[bpy.types.Object, bpy.types.Action, int, int]:
    rigs = armatures()
    if not rigs:
        raise RuntimeError("Animation export requires a working armature.")
    rig = rigs[0]
    action = bpy.data.actions.get(action_name)
    if action is None:
        action = next(
            (
                candidate for candidate in bpy.data.actions
                if candidate.name.casefold() == action_name.casefold()
            ),
            None,
        )
    if action is None:
        raise RuntimeError(f"Requested Blender action was not found: {action_name}")
    rig.animation_data_create()
    rig.animation_data.action = action
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    start, end = action.frame_range
    return rig, action, int(math.floor(start)), int(math.ceil(end))


def explicit_safe_name(value: Any, field: str) -> str:
    """Require a caller-supplied Blender identifier without sanitizing it."""

    name = str(value or "")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]{0,127}", name):
        raise ValueError(
            f"{field} must be an explicit safe Blender identifier containing only "
            "letters, digits, underscores, periods, or hyphens."
        )
    return name


def explicit_action_name(value: Any, field: str) -> str:
    """Require an exact stable Blender action identifier, including layered action separators."""

    name = str(value or "")
    if name != name.strip() or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.|: -]{0,191}", name):
        raise ValueError(
            f"{field} must be an explicit action identifier containing only letters, digits, "
            "spaces, underscores, periods, vertical bars, colons, or hyphens."
        )
    return name


def explicit_reference_id(value: Any, field: str) -> str:
    """Require an auditable provider task id or professional-source receipt id."""

    identifier = str(value or "")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,191}", identifier):
        raise ValueError(f"{field} must be a stable provider task or approved source receipt identifier.")
    return identifier


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def action_provenance(action: bpy.types.Action) -> Dict[str, str]:
    """Read and validate the immutable verified-source lineage retained on an action."""

    fields = {
        "source_kind": str(action.get("chaosx_animation_source_kind", "")),
        "source_reference_id": str(action.get("chaosx_animation_source_reference_id", "")),
        "source_sha256": str(action.get("chaosx_animation_source_sha256", "")).upper(),
        "source_action_name": str(action.get("chaosx_animation_source_action", "")),
        "provenance_rel": str(action.get("chaosx_animation_provenance_rel", "")),
        "processing_policy": str(action.get("chaosx_animation_processing_policy", "")),
    }
    if fields["source_kind"] == "manual_blender_gpt6_astra":
        spec_hash = str(action.get("chaosx_manual_action_spec_sha256", "")).upper()
        if not re.fullmatch(r"[0-9A-F]{64}", spec_hash) or not re.fullmatch(r"[0-9A-F]{64}", fields["source_sha256"]):
            raise RuntimeError("Manual action requires retained source checkpoint and declarative spec SHA-256.")
        fields.update(source_reference_id=spec_hash, source_action_name=action.name, manual_spec_sha256=spec_hash,
                      processing_policy="manual_blender_gpt6_astra_hash_bound_declarative_action")
        return fields
    if fields["source_kind"] not in {"meshy_animate", "meshy_text_to_motion", "professional_source"}:
        raise RuntimeError(f"Action {action.name} is not marked as a verified provider/professional source action.")
    if not re.fullmatch(r"[0-9A-F]{64}", fields["source_sha256"]):
        raise RuntimeError(f"Action {action.name} has no retained verified source checksum.")
    if not fields["source_reference_id"] or not fields["source_action_name"] or not fields["provenance_rel"]:
        raise RuntimeError(f"Action {action.name} has incomplete retained source provenance.")
    return fields


def normalize_exported_animation_scales(
    output: Path,
    pdx: Dict[str, Any],
    translation_scale: float,
) -> Dict[str, Any]:
    """Keep animation samples from changing the authored unit scale at runtime."""

    from io_pdx_mesh import pdx_data  # type: ignore

    root_xml = pdx_data.read_meshfile(str(output))
    info_xml = root_xml.find("info")
    samples_xml = root_xml.find("samples")
    initial_values_changed = 0
    sample_values_changed = 0
    initial_translation_values_changed = 0
    sample_translation_values_changed = 0

    if info_xml is not None:
        for bone_xml in info_xml:
            values = bone_xml.get("s")
            if values is None:
                continue
            initial_values_changed += sum(1 for value in values if abs(float(value) - 1.0) > 1e-6)
            bone_xml.set("s", [1.0 for _ in values])
        if abs(translation_scale - 1.0) > 1e-6:
            for bone_xml in info_xml:
                values = bone_xml.get("t")
                if values is None:
                    continue
                initial_translation_values_changed += len(values)
                bone_xml.set("t", [float(value) * translation_scale for value in values])

    if samples_xml is not None:
        values = samples_xml.get("s")
        if values:
            sample_values_changed = sum(1 for value in values if abs(float(value) - 1.0) > 1e-6)
            samples_xml.set("s", [1.0 for _ in values])
        values = samples_xml.get("t")
        if values and abs(translation_scale - 1.0) > 1e-6:
            sample_translation_values_changed = len(values)
            samples_xml.set("t", [float(value) * translation_scale for value in values])

    if (
        initial_values_changed
        or sample_values_changed
        or initial_translation_values_changed
        or sample_translation_values_changed
    ):
        pdx_data.write_animfile(str(output), root_xml)
        text_path = output.with_suffix(".txt")
        text_path.write_text(f"{pdx_data.PDXData(root_xml)}\n", encoding="utf-8")

    return {
        "policy": "normalize_exported_bone_scales_and_preserve_mesh_unit_translations",
        "translation_scale": translation_scale,
        "initial_scale_values_changed": initial_values_changed,
        "sample_scale_values_changed": sample_values_changed,
        "initial_translation_values_changed": initial_translation_values_changed,
        "sample_translation_values_changed": sample_translation_values_changed,
        "remaining_non_unit_initial_scales": 0,
        "remaining_non_unit_sample_scales": 0,
    }


def export_animation(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(job, payload["output_rel"], allow_missing=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    pdx = load_pdx(req["io_pdx_root"])
    rig, action, start, end = select_armature_and_action(payload["action_name"])
    export_transforms = prepare_pdx_export_transforms()
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_end = end
    for old_output in (output, output.with_suffix(".txt")):
        if old_output.exists():
            if not old_output.is_file():
                raise RuntimeError(f"Animation export target is not a file: {old_output}")
            old_output.unlink()
    pdx["export_animfile"](
        str(output),
        frame_start=start,
        frame_end=end,
        uniform_scale=True,
        plain_txt=True,
    )
    scale_normalization = normalize_exported_animation_scales(output, pdx, 1.0)
    from animation_root_export import correct_exported_initial_roots
    initial_root_world_pose = correct_exported_initial_roots(output, rig, start, bpy)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "action": action.name,
        "armature": rig.name,
        "frame_start": start,
        "frame_end": end,
        "fps": bpy.context.scene.render.fps,
        "armature_world_scale": export_transforms["armature_world_scale_after"],
        "export_transforms": export_transforms,
        "anim": str(output.relative_to(job)).replace("\\", "/"),
        "anim_bytes": output.stat().st_size,
        "anim_text": str(output.with_suffix(".txt").relative_to(job)).replace("\\", "/")
        if output.with_suffix(".txt").exists()
        else None,
        "scale_normalization": scale_normalization,
        "initial_root_world_pose": initial_root_world_pose,
        "warnings": [],
    }
    report = job / "blender" / "reports" / f"export_anim_{safe_name(action.name)[:32]}_{hashlib.sha256(action.name.encode()).hexdigest()[:10]}.json"
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


WINGED_BIPED_BONE_NAMES = (
    "root",
    "pelvis",
    "spine",
    "neck",
    "head",
    "upper_arm_left",
    "lower_arm_left",
    "hand_left",
    "upper_arm_right",
    "lower_arm_right",
    "hand_right",
    "upper_leg_left",
    "lower_leg_left",
    "foot_left",
    "upper_leg_right",
    "lower_leg_right",
    "foot_right",
    "wing_root_left",
    "wing_mid_left",
    "wing_tip_left",
    "wing_root_right",
    "wing_mid_right",
    "wing_tip_right",
)


def reimport_export(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    mesh = within(job, payload["mesh_rel"])
    anim = within(job, payload["anim_rel"]) if payload.get("anim_rel") else None
    texture_staging = []
    stage_defaults = payload.get("stage_default_textures", True)
    if type(stage_defaults) is not bool:
        raise ValueError("stage_default_textures must be an explicit boolean.")
    if not stage_defaults:
        adjacent = sorted(mesh.parent.glob("*.dds"))
        if not 1 <= len(adjacent) <= 128:
            raise ValueError("Preserved candidate textures require 1-128 adjacent DDS files.")
        for path in adjacent:
            if path.stat().st_size < 128 or path.read_bytes()[:4] != b"DDS ":
                raise ValueError("Invalid prestaged candidate DDS.")
            texture_staging.append({"source":path.relative_to(job).as_posix(), "staged":path.relative_to(job).as_posix(), "bytes":path.stat().st_size, "sha256":file_sha256(path), "copied":False, "policy":"preserve_prestaged_candidate"})
    requested_texture_names = tuple(
        str(name)
        for name in (payload.get("texture_names") or [])
        if str(name).casefold().endswith(".dds")
    )
    default_texture_names = (
        "texture_0.dds",
        "texture_specular.dds",
        "texture_normal.dds",
        "elephant_shared_base_diff.dds",
        "elephant_shared_base_spec.dds",
        "elephant_shared_base_n.dds",
        "Image_0.dds",
        "Image_1.dds",
        "Image_2.dds",
        "Image_3.dds",
        "normal.dds",
    )
    for texture_name in (tuple(dict.fromkeys(requested_texture_names + default_texture_names)) if stage_defaults else ()):
        source = job / "textures" / "dds" / texture_name
        if not source.is_file():
            continue
        destination = mesh.parent / texture_name
        already_staged = (
            destination.is_file()
            and destination.stat().st_size == source.stat().st_size
            and destination.read_bytes() == source.read_bytes()
        )
        if not already_staged:
            shutil.copy2(source, destination)
        texture_staging.append(
            {
                "source": str(source.relative_to(job)).replace("\\", "/"),
                "staged": str(destination.relative_to(job)).replace("\\", "/"),
                "bytes": destination.stat().st_size,
                "copied": not already_staged,
            }
        )
    clear_scene()
    pdx = load_pdx(req["io_pdx_root"])
    pdx["import_meshfile"](
        str(mesh),
        imp_mesh=True,
        imp_skel=True,
        imp_locs=True,
        join_materials=True,
        bonespace=False,
    )
    if anim is not None:
        pdx["import_animfile"](str(anim), frame_start=1)
    proof_name = safe_name(
        payload.get("proof_name")
        or f"{mesh.stem}_{Path(payload['anim_rel']).stem if payload.get('anim_rel') else 'mesh'}"
    )
    animation_bounds = []
    preview_paths = []
    if anim is not None:
        actions = [action for action in bpy.data.actions if action.frame_range[1] >= action.frame_range[0]]
        if actions:
            action = max(actions, key=lambda candidate: candidate.frame_range[1] - candidate.frame_range[0])
            rigs = armatures(working_only=False)
            if len(rigs) == 1:
                rigs[0].animation_data_create()
                rigs[0].animation_data.action = action
            first = int(math.floor(float(action.frame_range[0])))
            last = int(math.ceil(float(action.frame_range[1])))
            span = last - first
            sample_frames = sorted(
                {
                    first,
                    int(round(first + span * 0.25)),
                    int(round(first + span * 0.5)),
                    int(round(first + span * 0.75)),
                    last,
                }
            )
            for frame in sample_frames:
                bpy.context.scene.frame_set(frame)
                bpy.context.view_layer.update()
                minimum, maximum = evaluated_world_bounds(mesh_objects(working_only=False))
                animation_bounds.append(
                    {
                        "frame": frame,
                        "bounds_min": list(minimum),
                        "bounds_max": list(maximum),
                        "ground_contact_z": float(minimum.z),
                        "dimensions": list(maximum - minimum),
                        "locators": locator_records(),
                    }
                )
                preview_paths.extend(
                    render_previews(
                        job,
                        f"reimport_{proof_name}_frame_{frame:03d}",
                        ["front", "left", "three_quarter"],
                        working_only=False,
                    )
                )
            bpy.context.scene.frame_set(first)
            bpy.context.view_layer.update()
    else:
        preview_paths.extend(
            render_previews(
                job,
                f"reimport_{proof_name}",
                working_only=False,
            )
        )
    proof = job / "blender" / "checkpoints" / f"reimport_{proof_name}.blend"
    save_blend(proof)
    report = {
        "mesh": str(mesh.relative_to(job)).replace("\\", "/"),
        "anim": str(anim.relative_to(job)).replace("\\", "/") if anim else None,
        "runtime_texture_staging": texture_staging,
        "proof_blend": str(proof.relative_to(job)).replace("\\", "/"),
        "objects": [
            {
                "name": obj.name,
                "type": obj.type,
                "parent": obj.parent.name if obj.parent else None,
                "parent_type": obj.parent_type if obj.parent else None,
                "parent_bone": obj.parent_bone if obj.parent_type == "BONE" else None,
            }
            for obj in bpy.context.scene.objects
        ],
        "locators": locator_records(),
        "meshes": [
            {
                "name": obj.name,
                "vertices": len(obj.data.vertices),
                "polygons": len(obj.data.polygons),
                "materials": [mat.name for mat in obj.data.materials],
            }
            for obj in bpy.context.scene.objects
            if obj.type == "MESH"
        ],
        "geometry": geometry_metrics(working_only=False, position_weld_distance=1e-6),
        "animation_bounds": animation_bounds,
        "previews": sorted(set(preview_paths)),
        "armatures": [
            {"name": obj.name, "bones": len(obj.data.bones)}
            for obj in bpy.context.scene.objects
            if obj.type == "ARMATURE"
        ],
        "actions": [action.name for action in bpy.data.actions],
    }
    report_path = job / "validation" / f"reimport_{proof_name}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def sanitize_runtime_candidate(req: Dict[str, Any]) -> Dict[str, Any]:
    """Create a reviewable runtime checkpoint with bounded skin/material cleanup."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(
        job,
        payload.get("output_blend_rel", "blender/checkpoints/07_runtime_candidate_sanitized.blend"),
        allow_missing=True,
    )
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    weight_only = bool(payload.get("weight_only", False))
    if weight_only and payload.get("target_height_m") is not None:
        raise ValueError("weight_only cleanup cannot be combined with target_height_m normalization.")
    geometry_normalization = (
        normalize_geometry(float(payload["target_height_m"]))
        if payload.get("target_height_m") is not None
        else {"policy": "preserve_checkpoint_geometry"}
    )
    weights_before = weight_metrics()
    max_influences_per_vertex = int(payload.get("max_influences_per_vertex", 4))
    weights = sanitize_working_weights(
        preserve_skeleton_metadata=weight_only,
        max_influences_per_vertex=max_influences_per_vertex,
    )
    materials = (
        {
            "applied": False,
            "policy": "preserve_checkpoint_materials",
            "objects": [],
        }
        if weight_only
        else sanitize_working_materials()
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    save_blend(output)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(output.relative_to(job)).replace("\\", "/"),
        "weight_only": weight_only,
        "max_influences_per_vertex": max_influences_per_vertex,
        "geometry_normalization": geometry_normalization,
        "weights_before": weights_before,
        "weights": weights,
        "materials": materials,
        "geometry": geometry_metrics(),
        "rig_and_actions": action_metrics(),
    }
    report_path = job / "blender" / "reports" / "weights_sanitized.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def save_checkpoint_operation(req: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    source = within(job, payload["blend_rel"])
    stage = safe_name(payload["stage"])
    destination = job / "blender" / "checkpoints" / f"{stage}.blend"
    bpy.ops.wm.open_mainfile(filepath=str(source))
    save_blend(destination)
    return {
        "source": str(source.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(destination.relative_to(job)).replace("\\", "/"),
    }


def health(req: Dict[str, Any]) -> Dict[str, Any]:
    pdx = load_pdx(req["io_pdx_root"])
    manifest = Path(req["io_pdx_root"]).resolve() / "blender_manifest.toml"
    return {
        "blender_version": ".".join(str(part) for part in bpy.app.version),
        "blender_binary": bpy.app.binary_path,
        "io_pdx_mesh_manifest": str(manifest),
        "io_pdx_mesh_loaded": True,
        "io_pdx_mesh_operators": [
            hasattr(bpy.ops.io_pdx_mesh, "import_mesh"),
            hasattr(bpy.ops.io_pdx_mesh, "export_mesh"),
            hasattr(bpy.ops.io_pdx_mesh, "import_anim"),
            hasattr(bpy.ops.io_pdx_mesh, "export_anim"),
        ],
        "export_functions": [
            pdx["export_meshfile"].__name__,
            pdx["export_animfile"].__name__,
        ],
    }


def run(req: Dict[str, Any]) -> Dict[str, Any]:
    operation = req["operation"]
    if operation in {"repair_explicit_mesh_winding_batch", "replace_explicit_corner_normals"}:
        import explicit_batch_repair
        return explicit_batch_repair.run_repair(req, sys.modules[__name__])
    if operation == "remove_explicit_duplicate_faces":
        import duplicate_face_repair
        return duplicate_face_repair.remove_explicit_duplicate_faces(req, globals())
    if operation in {"edit_explicit_mesh_vertices", "bind_existing_pdx_material"}:
        import mesh_vertex_material_repair
        return getattr(mesh_vertex_material_repair, operation)(req, globals())
    if operation == "inspect_animation_source":
        from retarget_root_motion import inspect_animation_source
        return inspect_animation_source(req, globals())
    if operation == "rotate_existing_assembly_yaw":
        from assembly_yaw import rotate_existing_assembly_yaw
        return rotate_existing_assembly_yaw(req, globals())
    if operation == "repair_explicit_vertex_remap":
        from explicit_vertex_remap import repair_explicit_vertex_remap
        return repair_explicit_vertex_remap(req, globals())
    if operation == "repair_explicit_mesh_patch":
        from mesh_patch_repair import repair_explicit_mesh_patch
        return repair_explicit_mesh_patch(req, globals())
    if operation in {"inspect_mesh_winding", "repair_mesh_winding"}:
        import mesh_winding_repair
        return getattr(mesh_winding_repair, operation)(req, sys.modules[__name__])
    if operation in {"inspect_mesh_landmarks", "repair_explicit_mesh_winding"}:
        import mesh_inspection_repair
        return getattr(mesh_inspection_repair, operation)(req, globals())
    if operation == "partition_skeletal_mesh_export_batches":
        from skeletal_export_partition import partition_skeletal_mesh_export_batches
        return partition_skeletal_mesh_export_batches(req, sys.modules[__name__])
    pdx = None
    if operation not in {"health", "inspect_scene", "review_humanoid_components", "save_checkpoint", "author_locator", "promote_accepted_reimport", "sanitize_runtime_candidate", "bake_static_mesh_transforms", "partition_static_mesh_export_batches", "prepare_export_coordinate_checkpoint"}:
        pdx = load_pdx(req["io_pdx_root"])
    if operation == "health":
        return health(req)
    if operation == "prepare_candidate":
        return prepare(req, pdx)
    if operation == "inspect_scene":
        return inspect(req)
    if operation == "review_humanoid_components":
        return review_humanoid_components(req)
    if operation == "author_locator":
        return author_locator(req)
    if operation == "promote_accepted_reimport":
        return promote_accepted_reimport(req)
    if operation == "process_textures":
        return extract_textures(req)
    if operation == "bake_static_mesh_transforms":
        return bake_static_mesh_transforms(req)
    if operation == "partition_static_mesh_export_batches":
        return partition_static_mesh_export_batches(req)
    if operation == "export_mesh":
        return export_mesh(req, pdx)
    if operation == "export_animation":
        return export_animation(req, pdx)
    if operation == "prepare_export_coordinate_checkpoint":
        return prepare_export_coordinate_checkpoint(req)
    if operation == "reimport_export":
        return reimport_export(req, pdx)
    if operation == "sanitize_runtime_candidate":
        return sanitize_runtime_candidate(req)
    if operation == "save_checkpoint":
        return save_checkpoint_operation(req)
    raise ValueError(f"Unknown worker operation: {operation}")


def main() -> int:
    args = parse_args()
    if not args.request or not args.io_pdx_root:
        print(json.dumps({"error": "worker request or io_pdx_root was not provided"}, sort_keys=True))
        return 2
    request = json.loads(Path(args.request).read_text(encoding="utf-8"))
    request["io_pdx_root"] = args.io_pdx_root
    try:
        result = run(request)
        print(json.dumps(result, sort_keys=True))
        return 0
    except Exception as exc:
        traceback.print_exc()
        print(json.dumps({"error": str(exc), "operation": request.get("operation")}, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
