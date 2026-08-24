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
from mathutils.kdtree import KDTree
from normalization_convergence import evaluate_convergence_step


PREVIEW_LIGHT_REFERENCE_HEIGHT = 7.3518242835
CREATURE_GROUND_CONTACT_TOLERANCE_M = 0.01
CREATURE_GROUND_CONTACT_CLEARANCE_M = 0.001


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


def bind_geometry_to_existing_rig(
    source_meshes: List[bpy.types.Object],
    target_mesh: bpy.types.Object,
    target_armature: bpy.types.Object,
    weight_mode: str = "four_nearest",
) -> Dict[str, Any]:
    """Transfer rest-pose weights from the provider rig mesh to a closed mesh candidate."""

    if weight_mode not in {"four_nearest", "automatic_bone_heat", "bone_distance"}:
        raise ValueError(
            "geometry_weight_mode must be four_nearest, automatic_bone_heat, or bone_distance."
        )

    if not source_meshes:
        raise RuntimeError("Dual-source rig transfer requires at least one source rig mesh.")
    source_minimum, source_maximum = world_bounds(source_meshes)
    target_minimum, target_maximum = world_bounds([target_mesh])
    source_height = source_maximum.z - source_minimum.z
    target_height = target_maximum.z - target_minimum.z
    if source_height <= 0 or target_height <= 0:
        raise RuntimeError("Dual-source rig transfer requires positive source and target heights.")

    target_world = target_mesh.matrix_world.copy()
    target_mesh.parent = None
    target_mesh.matrix_world = target_world
    for modifier in list(target_mesh.modifiers):
        if modifier.type == "ARMATURE":
            target_mesh.modifiers.remove(modifier)

    target_mesh.scale *= source_height / target_height
    bpy.context.view_layer.update()
    target_minimum, target_maximum = world_bounds([target_mesh])
    source_center = (source_minimum + source_maximum) * 0.5
    target_center = (target_minimum + target_maximum) * 0.5
    target_mesh.location += source_center - target_center
    bpy.context.view_layer.update()

    for group in list(target_mesh.vertex_groups):
        target_mesh.vertex_groups.remove(group)
    transferred_vertices = 0
    if weight_mode == "four_nearest":
        source_group_names = sorted({group.name for mesh in source_meshes for group in mesh.vertex_groups})
        target_groups = {name: target_mesh.vertex_groups.new(name=name) for name in source_group_names}
        if not target_groups:
            raise RuntimeError("Dual-source rig transfer found no provider vertex groups.")
        source_vertices = [
            (mesh, vertex)
            for mesh in source_meshes
            for vertex in mesh.data.vertices
        ]
        tree = KDTree(len(source_vertices))
        for source_index, (mesh, vertex) in enumerate(source_vertices):
            tree.insert(mesh.matrix_world @ vertex.co, source_index)
        tree.balance()
        for vertex in target_mesh.data.vertices:
            nearest = tree.find_n(target_mesh.matrix_world @ vertex.co, 4)
            accumulated: Dict[str, float] = {}
            for _, source_index, distance in nearest:
                influence = 1.0 / max(distance, 1e-6)
                source_mesh, source_vertex = source_vertices[source_index]
                for source_group in source_mesh.vertex_groups:
                    try:
                        weight = source_group.weight(source_vertex.index)
                    except RuntimeError:
                        continue
                    if weight > 0:
                        accumulated[source_group.name] = accumulated.get(source_group.name, 0.0) + weight * influence
            total = sum(accumulated.values())
            if total <= 1e-8:
                continue
            for name, weight in accumulated.items():
                target_groups[name].add([vertex.index], weight / total, "REPLACE")
            transferred_vertices += 1
    elif weight_mode == "bone_distance":
        deform_bones = [bone for bone in target_armature.data.bones if bone.use_deform]
        if not deform_bones:
            raise RuntimeError("Provider armature exposes no deform bones for distance weighting.")
        target_groups = {
            bone.name: target_mesh.vertex_groups.new(name=bone.name)
            for bone in deform_bones
        }
        bone_segments = []
        for bone in deform_bones:
            head = target_armature.matrix_world @ bone.head_local
            tail = target_armature.matrix_world @ bone.tail_local
            segment = tail - head
            length_squared = max(float(segment.length_squared), 1e-12)
            bone_segments.append((bone.name, head, segment, length_squared))
        for vertex in target_mesh.data.vertices:
            position = target_mesh.matrix_world @ vertex.co
            distances = []
            for bone_name, head, segment, length_squared in bone_segments:
                projection = max(0.0, min(1.0, float((position - head).dot(segment)) / length_squared))
                closest = head + segment * projection
                distances.append((float((position - closest).length), bone_name))
            nearest = sorted(distances, key=lambda item: (item[0], item[1]))[:4]
            weighted = [(bone_name, 1.0 / max(distance * distance, 1e-8)) for distance, bone_name in nearest]
            total = sum(weight for _, weight in weighted)
            for bone_name, weight in weighted:
                target_groups[bone_name].add([vertex.index], weight / total, "REPLACE")
            transferred_vertices += 1

    mesh_world_scale = target_mesh.matrix_world.to_scale()
    rig_world_scale = target_armature.matrix_world.to_scale()
    if (
        max(mesh_world_scale) - min(mesh_world_scale) > 1e-5
        or max(rig_world_scale) - min(rig_world_scale) > 1e-5
        or min(mesh_world_scale) <= 0.0
        or min(rig_world_scale) <= 0.0
    ):
        raise RuntimeError(
            "Dual-source rig transfer requires positive uniform mesh and armature transforms."
        )
    export_scale_ratio = float(mesh_world_scale[0] / rig_world_scale[0])
    for vertex in target_mesh.data.vertices:
        vertex.co *= export_scale_ratio
    target_mesh.data.update()
    target_mesh.scale = rig_world_scale
    bpy.context.view_layer.update()
    world_matrix = target_mesh.matrix_world.copy()
    if weight_mode == "automatic_bone_heat":
        bpy.ops.object.select_all(action="DESELECT")
        target_mesh.select_set(True)
        target_armature.select_set(True)
        bpy.context.view_layer.objects.active = target_armature
        bpy.ops.object.parent_set(type="ARMATURE_AUTO")
        target_mesh.matrix_world = world_matrix
        for vertex in target_mesh.data.vertices:
            influences = sorted(
                ((item.group, float(item.weight)) for item in vertex.groups if item.weight > 0.0),
                key=lambda item: item[1],
                reverse=True,
            )[:4]
            keep = {group_index for group_index, _ in influences}
            total = sum(weight for _, weight in influences)
            for group in target_mesh.vertex_groups:
                if group.index not in keep:
                    group.remove([vertex.index])
            if total > 0.0:
                for group_index, weight in influences:
                    target_mesh.vertex_groups[group_index].add([vertex.index], weight / total, "REPLACE")
                transferred_vertices += 1
        modifier = next(
            (item for item in target_mesh.modifiers if item.type == "ARMATURE" and item.object is target_armature),
            None,
        )
        if modifier is None or transferred_vertices != len(target_mesh.data.vertices):
            raise RuntimeError(
                "Automatic bone-heat binding did not produce a complete armature binding for every target vertex."
            )
    else:
        target_mesh.parent = target_armature
        target_mesh.parent_type = "OBJECT"
        target_mesh.matrix_world = world_matrix
        modifier = target_mesh.modifiers.new("CHAOSX_RIG_TRANSFER", type="ARMATURE")
        modifier.object = target_armature
    modifier.use_deform_preserve_volume = True
    return {
        "method": (
            "Blender automatic bone-heat weights clamped and normalized to four influences"
            if weight_mode == "automatic_bone_heat"
            else (
                "four-nearest provider deform-bone segment inverse-square distance weights"
                if weight_mode == "bone_distance"
                else "four-nearest-provider-vertex inverse-distance weight transfer"
            )
        ),
        "source_meshes": sorted(mesh.name for mesh in source_meshes),
        "target_mesh": target_mesh.name,
        "armature": target_armature.name,
        "source_vertices": sum(len(mesh.data.vertices) for mesh in source_meshes),
        "target_vertices": len(target_mesh.data.vertices),
        "transferred_vertices": transferred_vertices,
        "alignment_scale": source_height / target_height,
        "source_height": source_height,
        "target_height_before_alignment": target_height,
        "export_transform_policy": "bake mesh/armature scale agreement into mesh data before parenting",
        "mesh_world_scale_before_bake": list(mesh_world_scale),
        "armature_world_scale": list(rig_world_scale),
        "mesh_data_scale_ratio": export_scale_ratio,
        "mesh_world_scale_after_bake": list(target_mesh.matrix_world.to_scale()),
    }


def prepare_dual_source_base_rig(target_armature: bpy.types.Object) -> Dict[str, Any]:
    """Reset only the working rig to an action-free rest base before normalization."""

    if target_armature.type != "ARMATURE" or not target_armature.get("chaosx_working", False):
        raise RuntimeError("Dual-source base-rig mode requires the explicit working armature.")
    detached_action = None
    detached_nla_tracks = 0
    if target_armature.animation_data is not None:
        active = target_armature.animation_data.action
        detached_action = active.name if active is not None else None
        detached_nla_tracks = len(target_armature.animation_data.nla_tracks)
        target_armature.animation_data_clear()
    for pose_bone in target_armature.pose.bones:
        pose_bone.matrix_basis = Matrix.Identity(4)
    target_armature.data.pose_position = "REST"
    bpy.context.scene.frame_set(0)
    bpy.context.view_layer.update()
    target_armature.data.pose_position = "POSE"
    bpy.context.view_layer.update()
    removed_unused_working_actions = []
    for action in list(bpy.data.actions):
        if action.users == 0 and "WORKING" in action.name:
            removed_unused_working_actions.append(action.name)
            bpy.data.actions.remove(action)
    remaining_working_actions = []
    if target_armature.animation_data is not None:
        if target_armature.animation_data.action is not None:
            remaining_working_actions.append(target_armature.animation_data.action.name)
        remaining_working_actions.extend(track.name for track in target_armature.animation_data.nla_tracks)
    if remaining_working_actions:
        raise RuntimeError(
            "Dual-source base-rig mode retained working animation data: "
            + json.dumps(sorted(remaining_working_actions))
        )
    return {
        "policy": "working_armature_action_clear_and_identity_rest_pose",
        "detached_working_action": detached_action,
        "detached_working_nla_tracks": detached_nla_tracks,
        "removed_unused_working_actions": sorted(removed_unused_working_actions),
        "working_actions": [],
        "pose_bones_reset": len(target_armature.pose.bones),
        "provider_source_actions_preserved": sorted(
            action.name for action in bpy.data.actions if "WORKING" not in action.name
        ),
    }


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


def sanitize_root_translation_channels() -> Dict[str, Any]:
    """Keep the active humanoid action in place by locking Hips location."""

    records: List[Dict[str, Any]] = []
    for rig in armatures():
        action = rig.animation_data.action if rig.animation_data else None
        if action is None:
            continue
        root_curves = [
            fcurve
            for fcurve, _ in action_fcurves(action)
            if fcurve.data_path == 'pose.bones["Hips"].location'
        ]
        if not root_curves:
            records.append(
                {
                    "armature": rig.name,
                    "action": action.name,
                    "location_fcurves": 0,
                    "changed_keyframes": 0,
                    "policy": "no_hips_location_channels_found",
                }
            )
            continue
        fixed_values: Dict[int, float] = {}
        changed_keyframes = 0
        for fcurve in root_curves:
            if not fcurve.keyframe_points:
                continue
            first = min(fcurve.keyframe_points, key=lambda point: point.co[0])
            fixed_values[fcurve.array_index] = float(first.co[1])
            for keyframe in fcurve.keyframe_points:
                if abs(keyframe.co[1] - first.co[1]) > 1e-8:
                    changed_keyframes += 1
                keyframe.co[1] = first.co[1]
                keyframe.handle_left[1] = first.co[1]
                keyframe.handle_right[1] = first.co[1]
            fcurve.update()
        first_frame = int(math.floor(float(action.frame_range[0])))
        bpy.context.scene.frame_set(first_frame)
        bpy.context.view_layer.update()
        before_minimum, _ = evaluated_world_bounds(mesh_objects())
        ground_correction = 0.0
        armature_scale = float(rig.matrix_world.to_scale().z)
        z_curve = next(
            (fcurve for fcurve in root_curves if fcurve.array_index == 2),
            None,
        )
        if z_curve is not None and armature_scale > 1e-8:
            test_step = 1.0
            for keyframe in z_curve.keyframe_points:
                keyframe.co[1] += test_step
                keyframe.handle_left[1] += test_step
                keyframe.handle_right[1] += test_step
            z_curve.update()
            bpy.context.view_layer.update()
            test_minimum, _ = evaluated_world_bounds(mesh_objects())
            for keyframe in z_curve.keyframe_points:
                keyframe.co[1] -= test_step
                keyframe.handle_left[1] -= test_step
                keyframe.handle_right[1] -= test_step
            z_curve.update()
            bpy.context.view_layer.update()
            derivative = float(test_minimum.z - before_minimum.z) / test_step
            if abs(derivative) > 1e-8:
                ground_correction = -float(before_minimum.z) / derivative
                for keyframe in z_curve.keyframe_points:
                    keyframe.co[1] += ground_correction
                    keyframe.handle_left[1] += ground_correction
                    keyframe.handle_right[1] += ground_correction
                z_curve.update()
                bpy.context.view_layer.update()
        after_minimum, _ = evaluated_world_bounds(mesh_objects())
        records.append(
            {
                "armature": rig.name,
                "action": action.name,
                "location_fcurves": len(root_curves),
                "changed_keyframes": changed_keyframes,
                "fixed_values": fixed_values,
                "ground_correction_source_units": ground_correction,
                "ground_contact_before": float(before_minimum.z),
                "ground_contact_after": float(after_minimum.z),
                "policy": "in_place_root_translation_locked_to_first_keyframe",
            }
        )
    return {
        "policy": "remove_provider_root_motion_for_in_place_unit_actions",
        "actions": records,
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


def evaluated_action_metrics() -> List[Dict[str, Any]]:
    """Measure evaluated bounds at representative frames for deformation QA."""

    meshes = mesh_objects()
    rigs = armatures()
    if not meshes or not rigs:
        return []
    scene = bpy.context.scene
    original_frame = scene.frame_current
    records: List[Dict[str, Any]] = []
    for rig in rigs:
        rig.animation_data_create()
        original_action = rig.animation_data.action
        actions = [
            action
            for action in bpy.data.actions
            if (
                ("WORKING" in action.name and action.name.startswith("Armature|"))
                or action.name.startswith("creature_")
                or action.name.startswith("black_plague_rat_")
            )
        ]
        for action in actions:
            rig.animation_data.action = action
            start, end = action.frame_range
            frames = sorted({int(math.floor(start)), int(math.ceil((start + end) * 0.5)), int(math.ceil(end))})
            frame_records = []
            for frame in frames:
                scene.frame_set(frame)
                depsgraph = bpy.context.evaluated_depsgraph_get()
                corners: List[Vector] = []
                for obj in meshes:
                    evaluated = obj.evaluated_get(depsgraph)
                    evaluated_mesh = evaluated.to_mesh()
                    try:
                        corners.extend(
                            evaluated.matrix_world @ vertex.co
                            for vertex in evaluated_mesh.vertices
                        )
                    finally:
                        evaluated.to_mesh_clear()
                if corners:
                    minimum = Vector((min(point.x for point in corners), min(point.y for point in corners), min(point.z for point in corners)))
                    maximum = Vector((max(point.x for point in corners), max(point.y for point in corners), max(point.z for point in corners)))
                    frame_records.append(
                        {
                            "frame": frame,
                            "bounds_min": list(minimum),
                            "bounds_max": list(maximum),
                            "dimensions": list(maximum - minimum),
                        }
                    )
            records.append(
                {
                    "armature": rig.name,
                    "action": action.name,
                    "frames": frame_records,
                }
            )
        rig.animation_data.action = original_action
    scene.frame_set(original_frame)
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
                weights.append(float(assignment.weight))
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


def sanitize_working_weights(*, preserve_skeleton_metadata: bool = False) -> Dict[str, Any]:
    """Keep PDX-compatible skinning influences without altering provider geometry."""

    records: List[Dict[str, Any]] = []
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
            raise RuntimeError(f"Armature {armature.name} has no root bone for zero-weight repair.")
        root_group = obj.vertex_groups.get(root_bone.name)
        if root_group is None:
            root_group = obj.vertex_groups.new(name=root_bone.name)

        over_four_before = 0
        zero_before = 0
        removed_influences = 0
        normalized_vertices = 0
        zero_weight_repaired = 0
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

            if len(assignments) > 4:
                over_four_before += 1
                kept = sorted(assignments, key=lambda item: (-item[1], item[0].name))[:4]
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
                root_group.add([vertex.index], 1.0, "REPLACE")
                zero_weight_repaired += 1
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
                "vertices_over_four_before": over_four_before,
                "zero_weight_vertices_before": zero_before,
                "removed_influences": removed_influences,
                "normalized_vertices": normalized_vertices,
                "zero_weight_vertices_repaired": zero_weight_repaired,
                "weighted_bones": sorted(weighted_bone_names),
                "required_export_bones": sorted(required_export_bones),
                "unignored_export_bones": unignored_export_bones,
            }
        )
    return {
        "policy": "keep_four_strongest_bone_influences_and_renormalize",
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


def camera_point_at(camera: bpy.types.Object, target: Vector) -> None:
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def render_previews(
    job: Path,
    runtime_stem: str,
    view_names: List[str] | None = None,
    *,
    working_only: bool = True,
) -> List[str]:
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.world.color = (0.015, 0.02, 0.03)

    meshes = mesh_objects(working_only=working_only)
    if not meshes:
        object_class = "working" if working_only else "imported runtime-proof"
        raise RuntimeError(f"Preview rendering found no {object_class} mesh objects.")
    minimum, maximum = world_bounds(meshes)
    center = (minimum + maximum) * 0.5
    dimensions = maximum - minimum
    object_height = max(float(dimensions.z), 0.1)
    ground_extent = max(8.0, float(max(dimensions.x, dimensions.y)) * 2.0)

    evidence_collection = new_collection("QA_EVIDENCE")
    ground_mesh = bpy.data.meshes.new("QA_Ground_Mesh")
    ground_mesh.from_pydata(
        [
            (-ground_extent, -ground_extent, minimum.z),
            (ground_extent, -ground_extent, minimum.z),
            (ground_extent, ground_extent, minimum.z),
            (-ground_extent, ground_extent, minimum.z),
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
        light.location = location
        camera_point_at(light, center)
        lights.append(light)

    camera_data = bpy.data.cameras.new("QA_Camera")
    camera = bpy.data.objects.new("QA_Camera", camera_data)
    evidence_collection.objects.link(camera)
    scene.camera = camera
    camera_data.lens = 55

    # Frame the whole object regardless of whether it is a 1.5 m prop or a
    # vanilla-calibrated 7.35-unit source mesh.
    preview_angle = math.radians(38.0)
    fit_distance = object_height / (2.0 * math.tan(preview_angle * 0.5) * 0.78)
    fit_distance = max(fit_distance, float(max(dimensions.x, dimensions.y)) * 1.5, 4.0)

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
    if payload.get("dual_source_base_rig", False) and not payload.get("geometry_source_rel"):
        raise ValueError("dual_source_base_rig requires geometry_source_rel.")
    if payload.get("geometry_object_name") and not payload.get("geometry_source_rel"):
        raise ValueError("geometry_object_name requires geometry_source_rel.")
    clear_scene()
    source_collection = new_collection("PROVIDER_SOURCE")
    working_collection = new_collection("WORKING")
    vanilla_reference = import_vanilla_reference(job, payload, pdx)
    imported = import_candidate(source)
    excluded_names = {str(name) for name in payload.get("excluded_provider_objects", [])}
    geometry_source = None
    geometry_transfer = None
    dual_source_base_rig = None
    base_weight_sanitization = None
    if payload.get("geometry_source_rel"):
        geometry_source = within(job, str(payload["geometry_source_rel"]))
        imported_geometry = import_geometry_candidate(geometry_source)
        imported_rig = imported
        imported = imported_geometry + imported_rig
        requested_geometry_object = explicit_safe_name(
            payload.get("geometry_object_name"),
            "geometry_object_name",
        )
        geometry_candidates = [
            obj for obj in imported_geometry
            if (
                obj.type == "MESH"
                and obj.name == requested_geometry_object
                and obj.name not in excluded_names
            )
        ]
        if len(geometry_candidates) != 1:
            raise RuntimeError(
                "Dual-source rig preparation requires exactly one explicitly selected geometry MESH: "
                + json.dumps(
                    {
                        "requested": requested_geometry_object,
                        "observed": sorted(
                            obj.name
                            for obj in imported_geometry
                            if obj.type == "MESH" and obj.name == requested_geometry_object
                        ),
                    },
                    sort_keys=True,
                )
            )
        selected_geometry = geometry_candidates[0]
        if selected_geometry.library is not None or selected_geometry.data.library is not None:
            raise RuntimeError(
                "Dual-source geometry_object_name must select a local, fully appended MESH object."
            )
        rig_mesh_candidates = [
            obj for obj in imported_rig
            if obj.type == "MESH" and obj.name not in excluded_names
        ]
        requested_source_mesh_names = {
            str(name) for name in payload.get("source_mesh_names", [])
        }
        if requested_source_mesh_names:
            rig_mesh_candidates = [
                obj for obj in rig_mesh_candidates if obj.name in requested_source_mesh_names
            ]
            observed_source_mesh_names = {obj.name for obj in rig_mesh_candidates}
            if observed_source_mesh_names != requested_source_mesh_names:
                raise RuntimeError(
                    "Dual-source rig preparation did not find every explicitly named source mesh: "
                    + json.dumps(
                        {
                            "requested": sorted(requested_source_mesh_names),
                            "observed": sorted(observed_source_mesh_names),
                        },
                        sort_keys=True,
                    )
                )
        armature_candidates = [
            obj for obj in imported_rig
            if obj.type == "ARMATURE" and obj.name not in excluded_names
        ]
        requested_source_armature = str(payload.get("source_armature_name") or "")
        if requested_source_armature:
            armature_candidates = [
                obj for obj in armature_candidates if obj.name == requested_source_armature
            ]
        if not rig_mesh_candidates or len(armature_candidates) != 1:
            raise RuntimeError(
                "Dual-source rig preparation requires one geometry mesh, one or more explicitly selected rig meshes, and one source armature."
            )
        working_source = [geometry_candidates[0], armature_candidates[0]]
        for obj in imported:
            move_to_collection(obj, source_collection)
            obj["chaosx_working"] = False
        working = duplicate_hierarchy(working_source, source_collection, working_collection)
        working_by_source = {
            str(obj.get("chaosx_source_object")): obj
            for obj in working
        }
        target_mesh = working_by_source[geometry_candidates[0].name]
        target_armature = working_by_source[armature_candidates[0].name]
        geometry_transfer = bind_geometry_to_existing_rig(
            rig_mesh_candidates,
            target_mesh,
            target_armature,
            str(payload.get("geometry_weight_mode") or "four_nearest"),
        )
        if payload.get("dual_source_base_rig", False):
            dual_source_base_rig = prepare_dual_source_base_rig(target_armature)
            base_weight_sanitization = sanitize_working_weights()
    else:
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
        {
            "policy": "dual_source_base_rig_has_no_working_actions",
            "actions": [],
            "remaining_scale_fcurves": 0,
        }
        if dual_source_base_rig is not None
        else sanitize_action_scale_channels()
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
    if dual_source_base_rig is not None:
        actions["actions"] = []
        actions["base_rig"] = dual_source_base_rig
        actions["base_weight_sanitization"] = base_weight_sanitization
    actions["scale_sanitization"] = scale_sanitization
    actions["root_translation_sanitization"] = (
        sanitize_root_translation_channels()
        if humanoid_asset
        else {"policy": "not_applicable", "actions": []}
    )
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
        "geometry_source": (
            str(geometry_source.relative_to(job)).replace("\\", "/")
            if geometry_source
            else None
        ),
        "source_objects": len(imported),
        "excluded_provider_objects": sorted(excluded_names),
        "vanilla_reference": vanilla_reference,
        "working_source_objects": len(working_source),
        "working_objects": len(working),
        "geometry_transfer": geometry_transfer,
        "dual_source_base_rig": dual_source_base_rig,
        "base_weight_sanitization": base_weight_sanitization,
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


def inspect(req: Dict[str, Any]) -> Dict[str, Any]:
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
        preview_paths = render_previews(job, runtime_stem, req["payload"].get("preview_view_names") or None)
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
        "rig_and_actions": action_metrics(),
        "evaluated_actions": evaluated_action_metrics(),
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
        for _, image in list(image_nodes()):
            original_name = image.name
            dds_rel = dds_map.get(original_name)
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


def exported_mesh_streams(text_path: Path) -> List[Dict[str, int]]:
    """Read per-material PDX mesh stream sizes from the exporter text proof."""

    streams: List[Dict[str, int]] = []
    current: Optional[Dict[str, int]] = None
    for line in text_path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\s*mesh:\s*$", line):
            if current is not None:
                streams.append(current)
            current = {"stream_index": len(streams)}
            continue
        if current is None:
            continue
        position_match = re.search(r"\bp \(float,\s*(\d+)\)", line)
        if position_match:
            components = int(position_match.group(1))
            if components % 3:
                raise RuntimeError("PDX export position stream is not divisible by three.")
            current["vertices"] = components // 3
        triangle_match = re.search(r"\btri \(int,\s*(\d+)\)", line)
        if triangle_match:
            indices = int(triangle_match.group(1))
            if indices % 3:
                raise RuntimeError("PDX export triangle stream is not divisible by three.")
            current["triangles"] = indices // 3
    if current is not None:
        streams.append(current)
    streams = [stream for stream in streams if "vertices" in stream or "triangles" in stream]
    if not streams or any("vertices" not in stream or "triangles" not in stream for stream in streams):
        raise RuntimeError("Unable to prove complete per-stream vertex and triangle counts from PDX text export.")
    return streams


def export_mesh(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    output = within(job, payload["output_rel"], allow_missing=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    pdx = load_pdx(req["io_pdx_root"])
    export_transforms = prepare_pdx_export_transforms()
    bpy.ops.object.select_all(action="DESELECT")
    working = [
        obj for obj in bpy.context.scene.objects
        if obj.type == "MESH" and obj.get("chaosx_working", False)
    ]
    if not working:
        raise RuntimeError("Mesh export found no approved chaosx_working mesh objects.")
    for obj in working:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = working[0]
    for old_output in (output, output.with_suffix(".txt")):
        if old_output.exists():
            if not old_output.is_file():
                raise RuntimeError(f"Mesh export target is not a file: {old_output}")
            old_output.unlink()
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
    text_output = output.with_suffix(".txt")
    streams = exported_mesh_streams(text_output)
    oversized_streams = [stream for stream in streams if stream["vertices"] > 65535]
    if oversized_streams:
        raise RuntimeError(f"PDX export exceeded the 65,535-vertex per-stream limit: {oversized_streams}")
    exported_checkpoint = job / "blender" / "checkpoints" / "06_exported.blend"
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
        "vertex_stream_limit": 65535,
        "exported_checkpoint": str(exported_checkpoint.relative_to(job)).replace("\\", "/"),
        "geometry": geometry_metrics(),
        "export_transforms": export_transforms,
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


def scale_aware_retarget_location_scale(
    source_world_scale: Vector,
    target_world_scale: Vector,
) -> float:
    """Convert source pose-basis translation units to target pose-basis units."""

    for label, scale in (
        ("source", source_world_scale),
        ("target", target_world_scale),
    ):
        if min(scale) <= 0.0 or max(scale) - min(scale) > 1e-5:
            raise ValueError(
                f"Animation transfer requires a positive uniform {label} armature world scale: "
                + json.dumps(list(scale))
            )
    source_uniform_world_scale = float(sum(source_world_scale) / 3.0)
    target_uniform_world_scale = float(sum(target_world_scale) / 3.0)
    return source_uniform_world_scale / target_uniform_world_scale


def import_animation_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Transfer one provider skeletal action onto the approved working rig.

    Provider animation files are imported only long enough to read their real
    bone channels. The source armature and mesh are removed after the action
    is copied onto the calibrated candidate, so the runtime scene retains one
    model and one armature. This is deliberately a named adapter operation,
    rather than an arbitrary Blender script, because the action transfer is a
    repeatable part of the locked HOI4 asset pipeline.
    """

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    source = within(job, payload["source_rel"])
    provenance_path = within(job, payload["provenance_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    source_action_name = explicit_action_name(payload.get("source_action_name"), "source_action_name")
    target_armature_name = explicit_safe_name(payload.get("target_armature_name"), "target_armature_name")
    action_name = explicit_action_name(payload.get("target_action_name"), "target_action_name")
    source_kind = str(payload.get("source_kind") or "")
    if source_kind not in {"meshy_animate", "professional_source"}:
        raise ValueError("source_kind must be meshy_animate or professional_source.")
    source_reference_id = explicit_reference_id(payload.get("source_reference_id"), "source_reference_id")
    expected_source_sha256 = str(payload.get("source_sha256") or "").upper()
    if not re.fullmatch(r"[0-9A-F]{64}", expected_source_sha256):
        raise ValueError("source_sha256 must be an explicit 64-character SHA-256 digest.")
    actual_source_sha256 = file_sha256(source)
    if actual_source_sha256 != expected_source_sha256:
        raise RuntimeError(
            "Animation source checksum did not match the verified provenance receipt: "
            f"expected {expected_source_sha256}, observed {actual_source_sha256}."
        )
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Animation provenance receipt is not valid JSON: {provenance_path.name}") from exc
    required_provenance = {
        "verification_status": "verified",
        "source_kind": source_kind,
        "source_reference_id": source_reference_id,
        "source_action_name": source_action_name,
        "source_sha256": expected_source_sha256,
    }
    mismatched_provenance = {
        key: {"expected": value, "observed": provenance.get(key)}
        for key, value in required_provenance.items()
        if provenance.get(key) != value
    }
    if mismatched_provenance:
        raise ValueError(
            "Animation provenance receipt does not verify the requested source action: "
            + json.dumps(mismatched_provenance, sort_keys=True)
        )

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    audited_target_promotion = {
        "requested": bool(payload.get("promote_audited_target", False)),
        "applied": False,
        "target_armature": None,
        "promoted_meshes": [],
        "policy": "working objects only",
    }
    target_rigs = armatures()
    if not target_rigs and audited_target_promotion["requested"]:
        all_target_rigs = armatures(working_only=False)
        matching_audited_rigs = [rig for rig in all_target_rigs if rig.name == target_armature_name]
        if len(all_target_rigs) != 1 or len(matching_audited_rigs) != 1:
            raise RuntimeError(
                "Audited-target promotion requires exactly one scene armature with the explicit target name; "
                + json.dumps(
                    {
                        "requested_target_armature": target_armature_name,
                        "available_armatures": sorted(rig.name for rig in all_target_rigs),
                    },
                    sort_keys=True,
                )
            )
        promoted_rig = matching_audited_rigs[0]
        promoted_meshes = []
        for obj in mesh_objects(working_only=False):
            consumes_target = obj.parent is promoted_rig or any(
                modifier.type == "ARMATURE" and modifier.object is promoted_rig
                for modifier in obj.modifiers
            )
            if consumes_target:
                obj["chaosx_working"] = True
                promoted_meshes.append(obj.name)
        if not promoted_meshes:
            raise RuntimeError(
                "Audited-target promotion found no mesh parented or armature-modified to the requested rig."
            )
        promoted_rig["chaosx_working"] = True
        audited_target_promotion = {
            "requested": True,
            "applied": True,
            "target_armature": promoted_rig.name,
            "promoted_meshes": sorted(promoted_meshes),
            "policy": "promoted only the uniquely named audited armature and its direct mesh consumers",
        }
        target_rigs = [promoted_rig]
    matching_target_rigs = [rig for rig in target_rigs if rig.name == target_armature_name]
    if len(target_rigs) != 1 or len(matching_target_rigs) != 1:
        raise RuntimeError(
            "Animation transfer requires exactly one calibrated working armature with the explicit target name; "
            + json.dumps(
                {
                    "requested_target_armature": target_armature_name,
                    "available_armatures": sorted(rig.name for rig in target_rigs),
                },
                sort_keys=True,
            )
        )
    target_rig = matching_target_rigs[0]
    before_objects = set(bpy.data.objects)
    before_actions = set(bpy.data.actions)
    imported = import_candidate(source)
    imported_rigs = [obj for obj in imported if obj.type == "ARMATURE"]
    if len(imported_rigs) != 1:
        raise RuntimeError(
            "Provider animation import must expose exactly one source armature; "
            f"found {len(imported_rigs)} from {source.name}."
        )
    source_rig = imported_rigs[0]
    source_armature_name = source_rig.name
    source_actions = [action for action in bpy.data.actions if action not in before_actions]
    source_action = next((action for action in source_actions if action.name == source_action_name), None)
    if source_action is None and source_rig.animation_data:
        active_source_action = source_rig.animation_data.action
        if active_source_action is not None and active_source_action.name == source_action_name:
            source_action = active_source_action
    if source_action is None:
        raise RuntimeError(
            "Verified animation source did not expose the explicitly named source action: "
            + json.dumps(
                {
                    "requested_source_action": source_action_name,
                    "available_source_actions": sorted(action.name for action in source_actions),
                },
                sort_keys=True,
            )
        )
    source_action_name = source_action.name

    source_curves = list(action_fcurves(source_action))
    if not source_curves:
        raise RuntimeError(f"Provider animation action contains no F-curves: {source_action.name}")
    source_bone_names = sorted(
        {
            match.group(1)
            for fcurve, _ in source_curves
            for match in [re.search(r'pose\.bones\["([^"]+)"\]', fcurve.data_path)]
            if match is not None
        }
    )
    target_bone_names = {bone.name for bone in target_rig.data.bones}
    raw_bone_chains = payload.get("bone_chains") or {}
    if not isinstance(raw_bone_chains, dict):
        raise ValueError("bone_chains must map target bone names to ordered source bone-name lists.")
    bone_chains: Dict[str, List[str]] = {}
    for raw_target, raw_sources in raw_bone_chains.items():
        target_name = explicit_safe_name(raw_target, "bone_chains target")
        if not isinstance(raw_sources, list) or not raw_sources:
            raise ValueError(f"bone_chains[{target_name!r}] must be a non-empty list.")
        source_names = [
            explicit_safe_name(source_name, f"bone_chains[{target_name!r}] source")
            for source_name in raw_sources
        ]
        bone_chains[target_name] = source_names
    if not bone_chains:
        missing_bones = sorted(set(source_bone_names) - target_bone_names)
        if missing_bones:
            raise RuntimeError(
                "Provider animation bone channels do not match the calibrated rig: "
                + json.dumps({"missing_bones": missing_bones, "source_action": source_action.name}, sort_keys=True)
            )
        bone_chains = {name: [name] for name in source_bone_names}
    missing_target_bones = sorted(set(bone_chains) - target_bone_names)
    missing_source_bones = sorted(
        {
            source_name
            for source_names in bone_chains.values()
            for source_name in source_names
            if source_name not in source_bone_names or source_rig.data.bones.get(source_name) is None
        }
    )
    if len(bone_chains) < 6:
        raise RuntimeError(
            f"Provider animation action is not a usable skeletal action: only {len(bone_chains)} mapped target bones."
        )
    if missing_target_bones or missing_source_bones:
        raise RuntimeError(
            "Provider animation bone chains do not match the source and calibrated target rigs: "
            + json.dumps(
                {
                    "missing_source_bones": missing_source_bones,
                    "missing_target_bones": missing_target_bones,
                    "source_action": source_action.name,
                },
                sort_keys=True,
            )
        )

    source_rig.animation_data_create()
    source_rig.animation_data.action = source_action
    source_start, source_end = source_action.frame_range
    frame_start = int(math.floor(float(source_start)))
    frame_end = int(math.ceil(float(source_end)))
    if frame_end <= frame_start:
        raise RuntimeError(f"Provider animation action has no usable frame span: {source_action.name}")
    source_lengths = {
        target_name: max(
            sum(float(source_rig.data.bones[name].length) for name in source_names),
            1e-8,
        )
        for target_name, source_names in bone_chains.items()
    }
    length_ratios = sorted(
        float(target_rig.data.bones[target_name].length) / source_lengths[target_name]
        for target_name in bone_chains
    )
    data_length_ratio = length_ratios[len(length_ratios) // 2]
    source_world_scale = source_rig.matrix_world.to_scale()
    target_world_scale = target_rig.matrix_world.to_scale()
    try:
        location_scale = scale_aware_retarget_location_scale(
            source_world_scale,
            target_world_scale,
        )
    except ValueError as exc:
        raise RuntimeError(
            f"{exc} Source armature: {source_rig.name}; target armature: {target_rig.name}."
        ) from exc
    source_pose_cache: Dict[int, Dict[str, Tuple[Vector, Quaternion]]] = {}
    target_bones_by_depth = sorted(
        bone_chains,
        key=lambda name: len(target_rig.data.bones[name].parent_recursive),
    )
    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        source_deltas: Dict[str, Tuple[Vector, Quaternion]] = {}
        for target_name, source_names in bone_chains.items():
            first_pose_bone = source_rig.pose.bones[source_names[0]]
            last_pose_bone = source_rig.pose.bones[source_names[-1]]
            first_rest_bone = source_rig.data.bones[source_names[0]]
            last_rest_bone = source_rig.data.bones[source_names[-1]]
            pose_parent_matrix = (
                first_pose_bone.parent.matrix.copy()
                if first_pose_bone.parent is not None
                else Matrix.Identity(4)
            )
            rest_parent_matrix = (
                first_rest_bone.parent.matrix_local.copy()
                if first_rest_bone.parent is not None
                else Matrix.Identity(4)
            )
            animated_chain = pose_parent_matrix.inverted_safe() @ last_pose_bone.matrix
            rest_chain = rest_parent_matrix.inverted_safe() @ last_rest_bone.matrix_local
            delta = rest_chain.inverted_safe() @ animated_chain
            location, _, _ = delta.decompose()
            source_world_rotation = (
                last_pose_bone.matrix.to_quaternion().normalized()
                @ last_rest_bone.matrix_local.to_quaternion().normalized().inverted()
            ).normalized()
            source_deltas[target_name] = (location.copy(), source_world_rotation)

        frame_pose: Dict[str, Tuple[Vector, Quaternion]] = {}
        desired_target_world_rotations: Dict[str, Quaternion] = {}
        for target_name in target_bones_by_depth:
            target_rest_bone = target_rig.data.bones[target_name]
            target_rest_world_rotation = target_rest_bone.matrix_local.to_quaternion().normalized()
            source_location, source_rotation = source_deltas[target_name]
            desired_world_rotation = (source_rotation @ target_rest_world_rotation).normalized()
            target_parent = target_rest_bone.parent
            if target_parent is None:
                parent_rest_world_rotation = Quaternion()
                parent_desired_world_rotation = Quaternion()
            else:
                parent_rest_world_rotation = target_parent.matrix_local.to_quaternion().normalized()
                parent_desired_world_rotation = desired_target_world_rotations.get(
                    target_parent.name,
                    parent_rest_world_rotation,
                )
            target_rest_local_rotation = (
                parent_rest_world_rotation.inverted() @ target_rest_world_rotation
            ).normalized()
            desired_local_rotation = (
                parent_desired_world_rotation.inverted() @ desired_world_rotation
            ).normalized()
            target_basis_rotation = (
                target_rest_local_rotation.inverted() @ desired_local_rotation
            ).normalized()
            desired_target_world_rotations[target_name] = desired_world_rotation
            frame_pose[target_name] = (source_location, target_basis_rotation)
        source_pose_cache[frame] = frame_pose

    existing = bpy.data.actions.get(action_name)
    if existing is not None:
        for obj in bpy.context.scene.objects:
            if obj.animation_data and obj.animation_data.action == existing:
                obj.animation_data.action = None
        bpy.data.actions.remove(existing)
    transferred = bpy.data.actions.new(action_name)
    transferred.use_fake_user = True
    transferred["chaosx_animation_source_kind"] = source_kind
    transferred["chaosx_animation_source_reference_id"] = source_reference_id
    transferred["chaosx_animation_source_sha256"] = actual_source_sha256
    transferred["chaosx_animation_source_action"] = source_action_name
    transferred["chaosx_animation_provenance_rel"] = str(provenance_path.relative_to(job)).replace("\\", "/")
    transferred["chaosx_animation_processing_policy"] = "verified_source_transfer_only"
    target_rig.animation_data_create()
    target_rig.animation_data.action = transferred
    bpy.context.view_layer.objects.active = target_rig
    target_rig.select_set(True)
    target_root = next((bone for bone in target_rig.data.bones if bone.parent is None), None)
    target_root_name = target_root.name if target_root is not None and target_root.name in bone_chains else ""
    source_root_location = (
        source_pose_cache[frame_start][target_root_name][0]
        if target_root_name
        else Vector()
    )
    source_root_z_delta_peak = (
        max(
            abs(float(source_pose_cache[frame][target_root_name][0].z - source_root_location.z))
            for frame in range(frame_start, frame_end + 1)
        )
        if target_root_name
        else 0.0
    )
    for frame in range(frame_start, frame_end + 1):
        bpy.context.scene.frame_set(frame)
        for target_name in bone_chains:
            target_bone = target_rig.pose.bones[target_name]
            source_location, source_rotation = source_pose_cache[frame][target_name]
            target_bone.rotation_mode = "QUATERNION"
            if target_name == target_root_name:
                root_delta = source_location - source_root_location
                target_bone.location = Vector((0.0, 0.0, root_delta.z * location_scale))
            else:
                target_bone.location = Vector((0.0, 0.0, 0.0))
            target_bone.rotation_quaternion = source_rotation
            target_bone.scale = (1.0, 1.0, 1.0)
            target_bone.keyframe_insert(data_path="location", frame=frame, group=target_name)
            target_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=target_name)
        bpy.context.view_layer.update()

    scale_cleanup = sanitize_action_scale_channels()
    root_cleanup = {
        "action": transferred.name,
        "policy": "provider armature-space motion reconstructed hierarchy-first through target rest and animated parent bases; target-root X/Y motion removed and Z retained; source pose-basis translation is converted to target pose-basis units by source-world-scale divided by target-world-scale",
        "location_coordinate_space": "pose_bone_matrix_basis_translation",
        "location_scale_formula": "source_armature_uniform_world_scale / target_armature_uniform_world_scale",
        "rest_data_length_ratio_applied_to_location": False,
        "data_length_ratio": data_length_ratio,
        "source_armature_world_scale": list(source_world_scale),
        "target_armature_world_scale": list(target_world_scale),
        "location_scale": location_scale,
        "target_root": target_root_name or None,
        "source_root_location": list(source_root_location),
        "source_root_z_delta_peak": source_root_z_delta_peak,
    }
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    sample_frames = sorted(
        {
            frame_start,
            int(round(frame_start + (frame_end - frame_start) * 0.25)),
            int(round(frame_start + (frame_end - frame_start) * 0.50)),
            int(round(frame_start + (frame_end - frame_start) * 0.75)),
            frame_end,
        }
    )
    sampled_bones = sorted(bone_chains)
    source_reference = source_pose_cache[frame_start]
    motion_crosscheck = []
    source_motion_peak = 0.0
    target_motion_peak = 0.0
    for frame in sample_frames:
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        source_motion = 0.0
        target_motion = 0.0
        bones_report = []
        for bone_name in sampled_bones:
            source_location, source_rotation = source_pose_cache[frame][bone_name]
            source_base_location, source_base_rotation = source_reference[bone_name]
            target_location, target_rotation, _ = target_rig.pose.bones[bone_name].matrix_basis.decompose()
            target_rig.animation_data.action = transferred
            bpy.context.view_layer.update()
            target_base_location = Vector((0.0, 0.0, 0.0))
            target_base_rotation = source_base_rotation
            source_delta = float((source_location - source_base_location).length) + float(
                source_rotation.rotation_difference(source_base_rotation).angle
            )
            target_delta = float((target_location - target_base_location).length) + float(
                target_rotation.rotation_difference(target_base_rotation).angle
            )
            source_motion += source_delta
            target_motion += target_delta
            bones_report.append(
                {
                    "bone": bone_name,
                    "source_delta_from_start": source_delta,
                    "target_delta_from_start": target_delta,
                }
            )
        source_motion_peak = max(source_motion_peak, source_motion)
        target_motion_peak = max(target_motion_peak, target_motion)
        motion_crosscheck.append(
            {
                "frame": frame,
                "source_motion_total": source_motion,
                "target_motion_total": target_motion,
                "bones": bones_report,
            }
        )
    if source_motion_peak > 1e-4 and target_motion_peak < max(1e-4, source_motion_peak * 0.10):
        raise RuntimeError(
            "Provider action has source motion but the transferred target action remained static: "
            + json.dumps(
                {
                    "source_motion_peak": source_motion_peak,
                    "target_motion_peak": target_motion_peak,
                    "samples": motion_crosscheck,
                },
                sort_keys=True,
            )
        )
    bpy.context.scene.frame_set(frame_start)
    bpy.context.view_layer.update()

    imported_object_names = [obj.name for obj in imported]
    for obj in list(imported):
        if obj.name in {item.name for item in bpy.context.scene.objects if item is target_rig}:
            continue
        if obj.name in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
    removed_provider_actions: List[str] = []
    for action in list(bpy.data.actions):
        if action == transferred or action == existing:
            continue
        if action == source_action or action.name.startswith("Armature.002|"):
            removed_provider_actions.append(action.name)
            action.user_clear()
            bpy.data.actions.remove(action)

    save_blend(checkpoint)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "source": str(source.relative_to(job)).replace("\\", "/"),
        "source_sha256": actual_source_sha256,
        "provenance": str(provenance_path.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "target_armature": target_rig.name,
        "audited_target_promotion": audited_target_promotion,
        "source_armature": source_armature_name,
        "source_action": source_action_name,
        "action": transferred.name,
        "frame_start": frame_start,
        "frame_end": frame_end,
        "fps": bpy.context.scene.render.fps,
        "source_fcurves": len(source_curves),
        "source_driven_bones": source_bone_names,
        "target_driven_bones": sorted(bone_chains),
        "bone_chains": bone_chains,
        "imported_objects_removed": imported_object_names,
        "provider_actions_removed": removed_provider_actions,
        "scale_cleanup": scale_cleanup,
        "root_cleanup": root_cleanup,
        "location_coordinate_space": "pose_bone_matrix_basis_translation",
        "location_scale_formula": "source_armature_uniform_world_scale / target_armature_uniform_world_scale",
        "rest_data_length_ratio_applied_to_location": False,
        "data_length_ratio": data_length_ratio,
        "source_armature_world_scale": list(source_world_scale),
        "target_armature_world_scale": list(target_world_scale),
        "location_scale": location_scale,
        "source_target_motion_crosscheck": {
            "sample_frames": sample_frames,
            "source_motion_peak": source_motion_peak,
            "target_motion_peak": target_motion_peak,
            "samples": motion_crosscheck,
            "status": "pass",
        },
        "policy": "provider_skeletal_action_retargeted_by_explicit_bone_chains_and_hierarchy_aware_target_rest_bases",
        "action_provenance": action_provenance(transferred),
        "retention_evidence": {
            "source_motion_peak": source_motion_peak,
            "target_motion_peak": target_motion_peak,
            "source_driven_bones": source_bone_names,
            "target_driven_bones": sorted(bone_chains),
            "target_action_fcurves": len(list(action_fcurves(transferred))),
            "manual_or_procedural_replacement_authored": False,
            "provider_source_objects_removed_after_transfer": imported_object_names,
        },
        "new_provider_call": False,
        "warnings": [],
    }
    report = job / "blender" / "reports" / f"import_animation_{safe_name(action_name)}.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


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
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.|:-]{0,191}", name):
        raise ValueError(
            f"{field} must be an explicit action identifier containing only letters, digits, "
            "underscores, periods, vertical bars, colons, or hyphens."
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
    if fields["source_kind"] not in {"meshy_animate", "professional_source"}:
        raise RuntimeError(f"Action {action.name} is not marked as a verified provider/professional source action.")
    if not re.fullmatch(r"[0-9A-F]{64}", fields["source_sha256"]):
        raise RuntimeError(f"Action {action.name} has no retained verified source checksum.")
    if not fields["source_reference_id"] or not fields["source_action_name"] or not fields["provenance_rel"]:
        raise RuntimeError(f"Action {action.name} has incomplete retained source provenance.")
    return fields


def explicit_bvh_action_name(value: Any, field: str) -> str:
    """Allow a numeric archival motion id while retaining a bounded Blender name."""

    name = str(value or "")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", name):
        raise ValueError(
            f"{field} must be an explicit BVH action identifier containing only letters, "
            "digits, underscores, periods, or hyphens."
        )
    return name


def inspect_bvh_header(source: Path) -> Dict[str, Any]:
    """Read only the bounded BVH hierarchy/header needed for an import receipt."""

    if source.suffix.casefold() != ".bvh":
        raise ValueError("Native BVH import requires a .bvh source file.")
    if source.stat().st_size <= 0 or source.stat().st_size > 256 * 1024 * 1024:
        raise ValueError("BVH source must be non-empty and no larger than 256 MiB.")
    joints: List[str] = []
    frames = None
    frame_time = None
    with source.open("r", encoding="utf-8-sig", errors="strict") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if line_number > 20000:
                raise ValueError("BVH hierarchy/header exceeded the bounded 20,000-line scan.")
            line = raw_line.strip()
            match = re.match(r"^(?:ROOT|JOINT)\s+([^\s{}]+)$", line)
            if match:
                joints.append(explicit_safe_name(match.group(1), "BVH joint name"))
            frames_match = re.match(r"^Frames:\s*(\d+)\s*$", line, re.IGNORECASE)
            if frames_match:
                frames = int(frames_match.group(1))
            time_match = re.match(
                r"^Frame\s+Time:\s*([0-9]+(?:\.[0-9]+)?(?:[Ee][+-]?\d+)?)\s*$",
                line,
                re.IGNORECASE,
            )
            if time_match:
                frame_time = float(time_match.group(1))
                break
    if len(joints) < 6 or len(set(joints)) != len(joints):
        raise ValueError("BVH source must expose at least six uniquely named skeletal joints.")
    if frames is None or frames < 2 or frame_time is None or frame_time <= 0.0:
        raise ValueError("BVH source must declare at least two frames and a positive Frame Time.")
    source_fps = 1.0 / frame_time
    if not math.isfinite(source_fps) or source_fps <= 0.0:
        raise ValueError("BVH source frame rate is not finite and positive.")
    return {
        "joints": joints,
        "joint_count": len(joints),
        "frames": frames,
        "frame_time_seconds": frame_time,
        "source_fps": source_fps,
    }


def action_curve_signature(action: bpy.types.Action) -> str:
    """Hash exact curve/key identity for save-reopen verification."""

    records = []
    for fcurve, _ in sorted(
        action_fcurves(action),
        key=lambda item: (item[0].data_path, item[0].array_index),
    ):
        records.append(
            {
                "data_path": fcurve.data_path,
                "array_index": fcurve.array_index,
                "keys": [
                    [float(point.co.x), float(point.co.y), point.interpolation]
                    for point in fcurve.keyframe_points
                ],
            }
        )
    return hashlib.sha256(
        json.dumps(records, separators=(",", ":"), sort_keys=True).encode("utf-8")
    ).hexdigest().upper()


def import_bvh_animation_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Native-import and retarget one receipt-verified professional BVH action."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    source = within(job, payload["source_rel"])
    provenance_path = within(job, payload["provenance_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    source_action_name = explicit_bvh_action_name(
        payload.get("source_action_name"), "source_action_name"
    )
    if source.stem != source_action_name:
        raise ValueError(
            "source_action_name must exactly match the verified BVH filename stem."
        )
    target_armature_name = explicit_safe_name(
        payload.get("target_armature_name"), "target_armature_name"
    )
    target_action_name = explicit_action_name(
        payload.get("target_action_name"), "target_action_name"
    )
    semantic_role = explicit_safe_name(payload.get("semantic_role"), "semantic_role")
    normalized_role = semantic_role.casefold().replace("-", "_").replace(".", "_")
    normalized_target = target_action_name.casefold().replace("-", "_").replace(".", "_")
    if normalized_role not in normalized_target:
        raise ValueError("target_action_name must contain the explicit semantic_role identity.")
    source_reference_id = explicit_reference_id(
        payload.get("source_reference_id"), "source_reference_id"
    )
    expected_source_sha256 = str(payload.get("source_sha256") or "").upper()
    if not re.fullmatch(r"[0-9A-F]{64}", expected_source_sha256):
        raise ValueError("source_sha256 must be an explicit 64-character SHA-256 digest.")
    actual_source_sha256 = file_sha256(source)
    if actual_source_sha256 != expected_source_sha256:
        raise RuntimeError(
            "BVH source checksum did not match the verified provenance receipt: "
            f"expected {expected_source_sha256}, observed {actual_source_sha256}."
        )
    source_fps = float(payload.get("source_fps") or 0.0)
    target_fps = float(payload.get("target_fps") or 0.0)
    if not math.isfinite(source_fps) or not math.isfinite(target_fps) or source_fps <= 0.0 or target_fps <= 0.0:
        raise ValueError("BVH import requires finite positive source_fps and target_fps.")
    if target_fps > 240.0:
        raise ValueError("BVH target_fps must not exceed 240.")
    root_motion_policy = str(payload.get("root_motion_policy") or "")
    if root_motion_policy != "in_place_xy_preserve_z":
        raise ValueError("root_motion_policy must be in_place_xy_preserve_z.")
    global_scale = float(payload.get("global_scale", 1.0))
    if not math.isfinite(global_scale) or not 0.0001 <= global_scale <= 1000000.0:
        raise ValueError("global_scale must be finite and between 0.0001 and 1000000.")
    axis_forward = str(payload.get("axis_forward") or "-Z")
    axis_up = str(payload.get("axis_up") or "Y")
    axes = {"X", "Y", "Z", "-X", "-Y", "-Z"}
    if axis_forward not in axes or axis_up not in axes or axis_forward.lstrip("-") == axis_up.lstrip("-"):
        raise ValueError("BVH forward/up axes must be distinct signed X, Y, or Z axes.")
    raw_bone_chains = payload.get("bone_chains")
    if not isinstance(raw_bone_chains, dict) or not raw_bone_chains:
        raise ValueError("bone_chains is required for fail-closed BVH retargeting.")

    header = inspect_bvh_header(source)
    fps_tolerance = max(0.01, source_fps * 0.001)
    if abs(float(header["source_fps"]) - source_fps) > fps_tolerance:
        raise ValueError(
            "Declared BVH source_fps does not match Frame Time: "
            f"declared={source_fps}, observed={header['source_fps']}."
        )
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("BVH provenance receipt is not valid JSON.") from exc
    required_provenance = {
        "verification_status": "verified",
        "source_kind": "professional_source",
        "source_format": "bvh",
        "source_reference_id": source_reference_id,
        "source_action_name": source_action_name,
        "source_sha256": expected_source_sha256,
        "source_fps": source_fps,
    }
    mismatches = {
        key: {"expected": value, "observed": provenance.get(key)}
        for key, value in required_provenance.items()
        if provenance.get(key) != value
    }
    if mismatches:
        raise ValueError(
            "BVH provenance receipt does not verify the requested source action: "
            + json.dumps(mismatches, sort_keys=True)
        )

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    matching_targets = [rig for rig in armatures() if rig.name == target_armature_name]
    if len(armatures()) != 1 or len(matching_targets) != 1:
        raise RuntimeError("BVH retarget requires exactly one explicitly named working target armature.")
    if bpy.data.actions.get(target_action_name) is not None:
        raise RuntimeError("BVH target action already exists; action aliases or replacement are forbidden.")

    clear_scene()
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)
    import io_anim_bvh  # type: ignore
    from io_anim_bvh import import_bvh as native_import_bvh  # type: ignore

    try:
        io_anim_bvh.register()
    except ValueError:
        pass
    scene = bpy.context.scene
    scene.render.fps = max(1, int(round(target_fps)))
    scene.render.fps_base = scene.render.fps / target_fps
    before_objects = set(bpy.data.objects)
    before_actions = set(bpy.data.actions)
    native_result = bpy.ops.import_anim.bvh(
        filepath=str(source),
        target="ARMATURE",
        global_scale=global_scale,
        frame_start=1,
        use_fps_scale=True,
        update_scene_fps=False,
        update_scene_duration=True,
        use_cyclic=False,
        rotate_mode="QUATERNION",
        axis_forward=axis_forward,
        axis_up=axis_up,
    )
    if "FINISHED" not in native_result:
        raise RuntimeError(f"Blender native BVH import failed: {sorted(native_result)}")
    imported_rigs = [obj for obj in bpy.data.objects if obj not in before_objects and obj.type == "ARMATURE"]
    imported_actions = [action for action in bpy.data.actions if action not in before_actions]
    if len(imported_rigs) != 1 or len(imported_actions) != 1:
        raise RuntimeError(
            "Native BVH import must produce exactly one armature and one action: "
            + json.dumps(
                {"armatures": [rig.name for rig in imported_rigs], "actions": [action.name for action in imported_actions]},
                sort_keys=True,
            )
        )
    source_rig = imported_rigs[0]
    source_action = imported_actions[0]
    native_action_name = source_action.name
    derived_action_name = f"BVH_{source_action_name}"
    source_action.name = derived_action_name
    source_action.use_fake_user = True
    source_rig.animation_data_create()
    source_rig.animation_data.action = source_action
    derived_rel = f"blender/source/bvh_{safe_name(target_action_name)}_{actual_source_sha256[:12]}.blend"
    derived = within(job, derived_rel, allow_missing=True)
    save_blend(derived)
    derived_sha256 = file_sha256(derived)
    derived_receipt_rel = f"blender/reports/bvh_{safe_name(target_action_name)}_derived_receipt.json"
    derived_receipt = within(job, derived_receipt_rel, allow_missing=True)
    derived_receipt.parent.mkdir(parents=True, exist_ok=True)
    derived_receipt.write_text(
        json.dumps(
            {
                "verification_status": "verified",
                "source_kind": "professional_source",
                "source_reference_id": f"{source_reference_id}.native_bvh",
                "source_action_name": derived_action_name,
                "source_sha256": derived_sha256,
                "derived_from_bvh_rel": str(source.relative_to(job)).replace("\\", "/"),
                "derived_from_bvh_sha256": actual_source_sha256,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    transfer = import_animation_action(
        {
            "job_root": str(job),
            "payload": {
                "blend_rel": str(blend.relative_to(job)).replace("\\", "/"),
                "source_rel": derived_rel,
                "provenance_rel": derived_receipt_rel,
                "checkpoint_rel": str(checkpoint.relative_to(job)).replace("\\", "/"),
                "source_action_name": derived_action_name,
                "target_armature_name": target_armature_name,
                "target_action_name": target_action_name,
                "source_kind": "professional_source",
                "source_reference_id": f"{source_reference_id}.native_bvh",
                "source_sha256": derived_sha256,
                "bone_chains": raw_bone_chains,
                "promote_audited_target": bool(payload.get("promote_audited_target", False)),
            },
        }
    )

    bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
    target_action = bpy.data.actions.get(target_action_name)
    target_rig = bpy.data.objects.get(target_armature_name)
    if target_action is None or target_rig is None or target_rig.type != "ARMATURE":
        raise RuntimeError("BVH retarget checkpoint lost the exact target armature or action identity.")
    target_action["chaosx_animation_source_kind"] = "professional_source"
    target_action["chaosx_animation_source_reference_id"] = source_reference_id
    target_action["chaosx_animation_source_sha256"] = actual_source_sha256
    target_action["chaosx_animation_source_action"] = source_action_name
    target_action["chaosx_animation_provenance_rel"] = str(provenance_path.relative_to(job)).replace("\\", "/")
    target_action["chaosx_animation_processing_policy"] = "native_bvh_import_hierarchy_retarget_source_motion_only"
    target_action["chaosx_animation_source_format"] = "bvh"
    target_action["chaosx_animation_semantic_role"] = semantic_role
    target_action["chaosx_animation_source_fps"] = source_fps
    target_action["chaosx_animation_target_fps"] = target_fps
    target_action["chaosx_animation_root_motion_policy"] = root_motion_policy
    target_action["chaosx_animation_derived_blend_sha256"] = derived_sha256
    target_rig.animation_data_create()
    target_rig.animation_data.action = target_action
    curves = list(action_fcurves(target_action))
    scale_curves = [curve.data_path for curve, _ in curves if curve.data_path.endswith(".scale")]
    driven_bones = sorted(
        {
            match.group(1)
            for curve, _ in curves
            for match in [re.search(r'pose\.bones\["([^"]+)"\]', curve.data_path)]
            if match is not None
        }
    )
    articulated_bones = set()
    for curve, _ in curves:
        if "rotation" not in curve.data_path or not curve.keyframe_points:
            continue
        values = [float(point.co.y) for point in curve.keyframe_points]
        if max(values) - min(values) > 1e-4:
            match = re.search(r'pose\.bones\["([^"]+)"\]', curve.data_path)
            if match:
                articulated_bones.add(match.group(1))
    if scale_curves or len(driven_bones) < 6 or len(articulated_bones) < 4:
        raise RuntimeError(
            "BVH semantic/curve audit rejected a static, scale-bearing, or insufficiently articulated action: "
            + json.dumps(
                {"scale_curves": scale_curves, "driven_bones": driven_bones, "articulated_bones": sorted(articulated_bones)},
                sort_keys=True,
            )
        )
    root_name = next((bone.name for bone in target_rig.data.bones if bone.parent is None), None)
    root_xy_peak = 0.0
    if root_name:
        root_path = f'pose.bones["{root_name}"].location'
        for curve, _ in curves:
            if curve.data_path == root_path and curve.array_index in {0, 1}:
                root_xy_peak = max(root_xy_peak, *(abs(float(point.co.y)) for point in curve.keyframe_points))
    if root_xy_peak > 1e-5:
        raise RuntimeError("BVH in-place root-motion audit retained X/Y displacement.")
    signature_before = action_curve_signature(target_action)
    target_action.use_fake_user = True
    save_blend(checkpoint)
    bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
    reopened_action = bpy.data.actions.get(target_action_name)
    reopened_rig = bpy.data.objects.get(target_armature_name)
    if reopened_action is None or reopened_rig is None:
        raise RuntimeError("BVH target action or armature did not survive checkpoint reopen.")
    signature_after = action_curve_signature(reopened_action)
    if signature_after != signature_before:
        raise RuntimeError("BVH target action curves changed across checkpoint save/reopen.")
    reopened_provenance = action_provenance(reopened_action)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "source": str(source.relative_to(job)).replace("\\", "/"),
        "source_sha256": actual_source_sha256,
        "provenance": str(provenance_path.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "source_action": source_action_name,
        "native_imported_action_name": native_action_name,
        "derived_action_name": derived_action_name,
        "target_action": target_action_name,
        "target_armature": target_armature_name,
        "semantic_role": semantic_role,
        "source_fps_declared": source_fps,
        "source_fps_observed": header["source_fps"],
        "target_fps": target_fps,
        "retime_policy": "Blender native BVH use_fps_scale into explicit target scene FPS",
        "root_motion_policy": root_motion_policy,
        "root_xy_peak_after": root_xy_peak,
        "bone_chains": raw_bone_chains,
        "bvh_header": header,
        "native_importer": {
            "module": "io_anim_bvh",
            "module_path": str(Path(io_anim_bvh.__file__).resolve()),
            "module_sha256": file_sha256(Path(io_anim_bvh.__file__).resolve()),
            "implementation_path": str(Path(native_import_bvh.__file__).resolve()),
            "implementation_sha256": file_sha256(Path(native_import_bvh.__file__).resolve()),
            "native_operator": "bpy.ops.import_anim.bvh",
            "axis_forward": axis_forward,
            "axis_up": axis_up,
            "global_scale": global_scale,
        },
        "derived_source": {"blend": derived_rel, "sha256": derived_sha256, "receipt": derived_receipt_rel},
        "transfer": transfer,
        "curve_audit": {
            "fcurves": len(curves),
            "driven_bones": driven_bones,
            "articulated_bones": sorted(articulated_bones),
            "scale_curves": [],
            "signature_before_save": signature_before,
            "signature_after_reopen": signature_after,
        },
        "action_provenance": reopened_provenance,
        "save_reopen_status": "pass",
        "manual_or_procedural_replacement_authored": False,
        "status": "pass",
    }
    report_path = job / "blender" / "reports" / f"import_bvh_{safe_name(target_action_name)}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def retime_animation_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Retiming an existing action changes sample time, not skeletal motion."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    target_armature_name = explicit_safe_name(payload.get("target_armature_name"), "target_armature_name")
    action_name = explicit_action_name(payload.get("action_name"), "action_name")
    source_fps = float(payload.get("source_fps") or 0.0)
    target_fps = float(payload.get("target_fps") or 0.0)
    if source_fps <= 0.0 or target_fps <= 0.0:
        raise ValueError("Animation retiming requires positive source and target FPS values.")

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    matching_rigs = [rig for rig in rigs if rig.name == target_armature_name]
    if len(rigs) != 1 or len(matching_rigs) != 1:
        raise RuntimeError(
            "Animation retiming requires exactly one explicitly named working armature: "
            + json.dumps(
                {
                    "requested_target_armature": target_armature_name,
                    "available_armatures": sorted(rig.name for rig in rigs),
                },
                sort_keys=True,
            )
        )
    rig = matching_rigs[0]
    action = bpy.data.actions.get(action_name)
    if action is None:
        action = next(
            (
                candidate
                for candidate in bpy.data.actions
                if candidate.name.casefold() == action_name.casefold()
            ),
            None,
        )
    if action is None:
        raise RuntimeError(f"Requested action was not found: {action_name}")
    provenance = action_provenance(action)

    old_start = float(action.frame_range[0])
    old_end = float(action.frame_range[1])
    fcurve_count_before = len(list(action_fcurves(action)))
    frame_ratio = target_fps / source_fps
    moved_keyframes = 0
    moved_handles = 0
    for fcurve, _ in action_fcurves(action):
        for keyframe in fcurve.keyframe_points:
            keyframe.co.x *= frame_ratio
            keyframe.handle_left.x *= frame_ratio
            keyframe.handle_right.x *= frame_ratio
            moved_keyframes += 1
            moved_handles += 2
        fcurve.update()

    scene = bpy.context.scene
    scene.render.fps = int(round(target_fps))
    start = int(math.floor(float(action.frame_range[0])))
    end = int(math.ceil(float(action.frame_range[1])))
    if end <= start:
        raise RuntimeError(f"Retimed action has no usable frame span: {action.name}")
    scene.frame_start = start
    scene.frame_end = end
    rig.animation_data_create()
    rig.animation_data.action = action
    scene.frame_set(start)
    bpy.context.view_layer.update()
    save_blend(checkpoint)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "target_armature": rig.name,
        "action": action.name,
        "source_fps": source_fps,
        "target_fps": target_fps,
        "frame_ratio": frame_ratio,
        "frame_start_before": old_start,
        "frame_end_before": old_end,
        "frame_start": start,
        "frame_end": end,
        "moved_keyframes": moved_keyframes,
        "moved_handles": moved_handles,
        "fps": scene.render.fps,
        "policy": "existing_provider_action_time_rescaled_to_required_runtime_fps",
        "action_provenance": provenance,
        "retention_evidence": {
            "fcurve_count_before": fcurve_count_before,
            "fcurve_count_after": len(list(action_fcurves(action))),
            "keyframe_values_changed": False,
            "keyframe_times_rescaled": True,
            "manual_or_procedural_replacement_authored": False,
        },
        "body_motion_replaced": False,
        "new_model_created": False,
        "new_rig_created": False,
        "new_provider_call": False,
        "warnings": [],
    }
    report = job / "blender" / "reports" / f"retime_animation_{safe_name(action.name)}.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


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
        "warnings": [],
    }
    report = job / "blender" / "reports" / f"export_anim_{safe_name(action.name)}.json"
    report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


HUMANOID_BONE_NAMES = (
    "Hips",
    "Spine",
    "Spine01",
    "Spine02",
    "neck",
    "Head",
    "headfront",
    "head_end",
    "LeftShoulder",
    "LeftArm",
    "LeftForeArm",
    "LeftHand",
    "RightShoulder",
    "RightArm",
    "RightForeArm",
    "RightHand",
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftToeBase",
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightToeBase",
)


def _humanoid_bone_name_for_vertex(
    world_position: Vector,
    minimum: Vector,
    maximum: Vector,
) -> str:
    """Choose a deterministic HOI4 humanoid influence from the mesh silhouette."""

    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(float(dimensions.z), 1e-6)
    width = max(float(dimensions.x), 1e-6)
    length = max(float(dimensions.y), 1e-6)
    z_fraction = (world_position.z - minimum.z) / height
    x_fraction = (world_position.x - centre.x) / width
    y_fraction = (world_position.y - centre.y) / length
    abs_x = abs(x_fraction)
    side = "Left" if x_fraction < 0.0 else "Right"

    if z_fraction > 0.91:
        return "head_end"
    if z_fraction > 0.84 and y_fraction < -0.08:
        return "headfront"
    if z_fraction > 0.79:
        return "Head"
    if z_fraction > 0.69 and abs_x < 0.18:
        return "neck"
    if z_fraction > 0.58 and abs_x > 0.12:
        return f"{side}Shoulder"
    if z_fraction > 0.43 and abs_x > 0.13:
        return f"{side}Arm"
    if z_fraction > 0.27 and abs_x > 0.10:
        return f"{side}ForeArm"
    if z_fraction > 0.16 and abs_x > 0.08:
        return f"{side}Hand"
    if z_fraction < 0.13 and abs_x > 0.07:
        return f"{side}ToeBase" if y_fraction < -0.04 else f"{side}Foot"
    if z_fraction < 0.46 and abs_x > 0.08:
        return f"{side}Leg" if z_fraction < 0.28 else f"{side}UpLeg"
    if z_fraction > 0.63:
        return "Spine02"
    if z_fraction > 0.49:
        return "Spine01"
    if z_fraction > 0.33:
        return "Spine"
    return "Hips"


def _humanoid_weight_candidates(primary: str) -> List[str]:
    """Return a small same-region chain for bounded blended weights."""

    if primary in {"Head", "headfront", "head_end", "neck"}:
        return ["neck", "Head", "headfront", "head_end"]
    if primary.startswith("Left"):
        if primary in {"LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand"}:
            return ["LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand"]
        if primary in {"LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase"}:
            return ["LeftUpLeg", "LeftLeg", "LeftFoot", "LeftToeBase"]
    if primary.startswith("Right"):
        if primary in {"RightShoulder", "RightArm", "RightForeArm", "RightHand"}:
            return ["RightShoulder", "RightArm", "RightForeArm", "RightHand"]
        if primary in {"RightUpLeg", "RightLeg", "RightFoot", "RightToeBase"}:
            return ["RightUpLeg", "RightLeg", "RightFoot", "RightToeBase"]
    if primary == "Spine02":
        return ["Spine01", "Spine02", "neck"]
    if primary == "Spine01":
        return ["Spine", "Spine01", "Spine02"]
    if primary == "Spine":
        return ["Hips", "Spine", "Spine01"]
    return ["Hips", "Spine", "Spine01"]


def _point_segment_distance(point: Vector, start: Vector, end: Vector) -> float:
    segment = end - start
    length_squared = float(segment.length_squared)
    if length_squared <= 1e-12:
        return float((point - start).length)
    factor = max(0.0, min(1.0, float((point - start).dot(segment)) / length_squared))
    return float((point - (start + factor * segment)).length)


def author_humanoid_rig(req: Dict[str, Any]) -> Dict[str, Any]:
    """Create the repository's bounded HOI4 humanoid rig on approved geometry."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    rig_name = safe_name(str(payload.get("rig_name") or "chaosx_humanoid_armature"))
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Humanoid rigging found no approved working meshes.")
    for rig in armatures():
        bpy.data.objects.remove(rig, do_unlink=True)

    minimum, maximum = world_bounds(working)
    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(float(dimensions.z), 1e-6)
    width = max(float(dimensions.x), 1e-6)
    length = max(float(dimensions.y), 1e-6)
    z0 = minimum.z
    y_front = centre.y - length * 0.08
    y_rear = centre.y + length * 0.04
    armature_data = bpy.data.armatures.new(rig_name)
    rig = bpy.data.objects.new(rig_name, armature_data)
    _working_collection().objects.link(rig)
    rig["chaosx_working"] = True
    rig["chaosx_humanoid_rig"] = True
    rig["chaosx_humanoid_rig_route"] = "blender_failure_recovery_humanoid_v1"
    rig["chaosx_skeleton_contract"] = "hoi4_standard_humanoid_24_bone"
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bones: Dict[str, bpy.types.EditBone] = {}

    def add_bone(name: str, head: Vector, tail: Vector, parent: Optional[str] = None) -> None:
        bone = armature_data.edit_bones.new(name)
        bone.head = head
        bone.tail = tail
        if parent:
            bone.parent = bones[parent]
            bone.use_connect = False
        bones[name] = bone

    add_bone("Hips", Vector((centre.x, centre.y, z0 + height * 0.34)), Vector((centre.x, centre.y, z0 + height * 0.43)))
    add_bone("Spine", Vector((centre.x, centre.y, z0 + height * 0.41)), Vector((centre.x, centre.y, z0 + height * 0.51)), "Hips")
    add_bone("Spine01", Vector((centre.x, centre.y, z0 + height * 0.49)), Vector((centre.x, centre.y, z0 + height * 0.61)), "Spine")
    add_bone("Spine02", Vector((centre.x, centre.y, z0 + height * 0.59)), Vector((centre.x, centre.y, z0 + height * 0.70)), "Spine01")
    add_bone("neck", Vector((centre.x, y_front, z0 + height * 0.68)), Vector((centre.x, y_front, z0 + height * 0.78)), "Spine02")
    add_bone("Head", Vector((centre.x, y_front, z0 + height * 0.76)), Vector((centre.x, y_front, z0 + height * 0.87)), "neck")
    add_bone("headfront", Vector((centre.x, y_front, z0 + height * 0.82)), Vector((centre.x, y_front - length * 0.08, z0 + height * 0.84)), "Head")
    add_bone("head_end", Vector((centre.x, y_front, z0 + height * 0.86)), Vector((centre.x, y_front, z0 + height * 0.96)), "Head")

    for side, sign in (("Left", -1.0), ("Right", 1.0)):
        shoulder = Vector((centre.x + sign * width * 0.18, centre.y - length * 0.01, z0 + height * 0.66))
        elbow = Vector((centre.x + sign * width * 0.32, centre.y - length * 0.04, z0 + height * 0.50))
        wrist = Vector((centre.x + sign * width * 0.38, centre.y - length * 0.07, z0 + height * 0.33))
        hand = Vector((centre.x + sign * width * 0.39, centre.y - length * 0.10, z0 + height * 0.22))
        add_bone(f"{side}Shoulder", shoulder, elbow, "Spine02")
        add_bone(f"{side}Arm", elbow, wrist, f"{side}Shoulder")
        add_bone(f"{side}ForeArm", wrist, hand, f"{side}Arm")
        add_bone(f"{side}Hand", hand, hand + Vector((0.0, -length * 0.06, -height * 0.04)), f"{side}ForeArm")

        hip = Vector((centre.x + sign * width * 0.10, centre.y + length * 0.01, z0 + height * 0.35))
        knee = Vector((centre.x + sign * width * 0.12, centre.y + length * 0.01, z0 + height * 0.20))
        ankle = Vector((centre.x + sign * width * 0.12, centre.y - length * 0.02, z0 + height * 0.08))
        toe = Vector((centre.x + sign * width * 0.12, centre.y - length * 0.13, z0 + height * 0.035))
        add_bone(f"{side}UpLeg", hip, knee, "Hips")
        add_bone(f"{side}Leg", knee, ankle, f"{side}UpLeg")
        add_bone(f"{side}Foot", ankle, toe, f"{side}Leg")
        add_bone(f"{side}ToeBase", toe, toe + Vector((0.0, -length * 0.07, 0.0)), f"{side}Foot")

    bpy.ops.object.mode_set(mode="OBJECT")
    rig.show_in_front = True
    armature_data.display_type = "BBONE"
    segments = {
        bone.name: (Vector(bone.head_local), Vector(bone.tail_local))
        for bone in armature_data.bones
    }
    records = []
    for obj in working:
        for group in list(obj.vertex_groups):
            obj.vertex_groups.remove(group)
        groups = {name: obj.vertex_groups.new(name=name) for name in HUMANOID_BONE_NAMES}
        counts: Dict[str, int] = {name: 0 for name in groups}
        influence_histogram: Dict[str, int] = {"1": 0, "2": 0, "3": 0}
        for vertex in obj.data.vertices:
            world_position = obj.matrix_world @ vertex.co
            primary = _humanoid_bone_name_for_vertex(world_position, minimum, maximum)
            candidates = [name for name in _humanoid_weight_candidates(primary) if name in segments]
            ranked = sorted(
                (
                    _point_segment_distance(world_position, *segments[name]),
                    name,
                )
                for name in candidates
            )[:3]
            names = [name for _, name in ranked]
            if primary not in names:
                names = [primary] + names[:2]
            names = list(dict.fromkeys(name for name in names if name in groups))[:3]
            if not names:
                names = ["Hips"]
            if primary in names:
                names.remove(primary)
            weights = {primary: 0.68}
            if names:
                inverse = [1.0 / max(next((distance for distance, name in ranked if name == item), 1.0), 1e-4) for item in names]
                inverse_total = sum(inverse)
                for name, value in zip(names, inverse):
                    weights[name] = 0.32 * value / max(inverse_total, 1e-8)
            total = sum(weights.values())
            for name, weight in weights.items():
                groups[name].add([vertex.index], weight / max(total, 1e-8), "REPLACE")
                counts[name] += 1
            influence_histogram[str(len(weights))] = influence_histogram.get(str(len(weights)), 0) + 1
        modifier = next((item for item in obj.modifiers if item.type == "ARMATURE"), None)
        if modifier is None:
            modifier = obj.modifiers.new("CHAOSX_HUMANOID_ARMATURE", "ARMATURE")
        modifier.object = rig
        world_matrix = obj.matrix_world.copy()
        obj.parent = rig
        obj.parent_type = "OBJECT"
        obj.matrix_world = world_matrix
        records.append(
            {
                "object": obj.name,
                "vertices": len(obj.data.vertices),
                "vertex_group_counts": {name: count for name, count in counts.items() if count},
                "influence_histogram": influence_histogram,
            }
        )
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "bones": [bone.name for bone in armature_data.bones],
        "bone_count": len(armature_data.bones),
        "component_bindings": records,
        "rig_route": "blender_failure_recovery_humanoid_v1",
        "rig_map": f"{rig_name}_hoi4_standard_humanoid_24_bones_v1",
        "weight_policy": "bounded same-region blended weights with at most three influences per vertex; no unweighted vertices",
        "source_policy": "Meshy 7 geometry retained; provider rig is not used",
        "status": "pass" if len(armature_data.bones) == len(HUMANOID_BONE_NAMES) else "failed",
    }
    report_path = job / "blender" / "reports" / "humanoid_rig.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def author_humanoid_actions(req: Dict[str, Any]) -> Dict[str, Any]:
    """Author the four required in-place HOI4 humanoid skeletal actions."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    if len(rigs) != 1:
        raise RuntimeError(f"Humanoid action authoring requires exactly one armature, found {len(rigs)}.")
    rig = rigs[0]
    rig.animation_data_create()
    scene = bpy.context.scene
    scene.render.fps = int(payload.get("fps") or 24)
    base_rig_location = rig.location.copy()
    action_reports: Dict[str, Dict[str, Any]] = {}

    def role_frames(role: str) -> List[int]:
        return {
            "idle": [0, 12, 24, 36, 48],
            "move": [0, 6, 12, 18, 24],
            "attack": [0, 8, 16, 24, 32],
            "death": [0, 12, 24, 36],
        }[role]

    def phase(role: str, frame: int, frames: List[int]) -> float:
        normalized = (frame - frames[0]) / max(frames[-1] - frames[0], 1)
        if role in {"idle", "move"}:
            return math.sin(2.0 * math.pi * normalized)
        if role == "attack":
            return math.sin(math.pi * normalized)
        return normalized

    for role in ("idle", "move", "attack", "death"):
        frames = role_frames(role)
        action_name = safe_name(str(payload.get("action_names", {}).get(role) or f"chaosx_humanoid_{role}"))
        old_action = bpy.data.actions.get(action_name)
        if old_action is not None:
            bpy.data.actions.remove(old_action)
        action = bpy.data.actions.new(action_name)
        action.use_fake_user = True
        rig.animation_data.action = action
        scene.frame_start = frames[0]
        scene.frame_end = frames[-1]
        base = {}
        for bone in rig.pose.bones:
            bone.rotation_mode = "QUATERNION"
            base[bone.name] = (bone.location.copy(), bone.rotation_quaternion.copy())

        def rotate(name: str, axis: str, degrees: float, value: float) -> None:
            bone = rig.pose.bones.get(name)
            if bone is None:
                return
            bone.rotation_mode = "QUATERNION"
            bone.rotation_quaternion = base[name][1] @ _action_delta(axis, degrees * value)

        for frame in frames:
            scene.frame_set(frame)
            p = phase(role, frame, frames)
            for bone in rig.pose.bones:
                bone.rotation_mode = "QUATERNION"
                bone.location = base[bone.name][0].copy()
                bone.rotation_quaternion = base[bone.name][1].copy()
                bone.scale = (1.0, 1.0, 1.0)
            if role == "idle":
                rotate("Spine01", "x", 1.0, p)
                rotate("Spine02", "x", 1.5, p)
                rotate("neck", "x", 2.0, p)
                rotate("Head", "z", 1.0, p)
                rotate("LeftForeArm", "x", 1.0, p)
                rotate("RightForeArm", "x", -1.0, p)
            elif role == "move":
                for side, sign in (("Left", 1.0), ("Right", -1.0)):
                    gait = sign * p
                    rotate(f"{side}UpLeg", "x", 24.0, gait)
                    rotate(f"{side}Leg", "x", -10.0, gait)
                    rotate(f"{side}Foot", "x", 8.0, gait)
                    rotate(f"{side}Arm", "x", -16.0, gait)
                    rotate(f"{side}ForeArm", "x", -6.0, gait)
                rotate("Spine01", "x", 2.0, p)
                rotate("Spine02", "x", 1.5, p)
                rotate("neck", "x", -1.0, p)
                rotate("Head", "z", 1.0, p)
                hips = rig.pose.bones.get("Hips")
                if hips is not None:
                    hips.location = base["Hips"][0] + Vector((0.0, 0.0, 0.001 * p))
            elif role == "attack":
                rotate("Spine01", "x", -10.0, p)
                rotate("Spine02", "x", -8.0, p)
                rotate("neck", "x", -8.0, p)
                rotate("Head", "x", -12.0, p)
                for side, sign in (("Left", 1.0), ("Right", -1.0)):
                    rotate(f"{side}Shoulder", "x", -22.0, p)
                    rotate(f"{side}Arm", "x", -30.0, p)
                    rotate(f"{side}ForeArm", "x", -18.0, p)
                    rotate(f"{side}Hand", "z", 8.0 * sign, p)
                    rotate(f"{side}UpLeg", "x", -5.0, p)
            else:
                rotate("Spine", "x", -34.0, p)
                rotate("Spine01", "x", -38.0, p)
                rotate("Spine02", "x", -28.0, p)
                rotate("neck", "x", -24.0, p)
                rotate("Head", "x", -18.0, p)
                for side, sign in (("Left", 1.0), ("Right", -1.0)):
                    rotate(f"{side}Shoulder", "z", 20.0 * sign, p)
                    rotate(f"{side}Arm", "z", 28.0 * sign, p)
                    rotate(f"{side}ForeArm", "z", 20.0 * sign, p)
                    rotate(f"{side}UpLeg", "x", 8.0, p)
                    rotate(f"{side}Leg", "x", 12.0, p)
            for bone in rig.pose.bones:
                bone.keyframe_insert(data_path="location", frame=frame, group=bone.name)
                bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=bone.name)

        for fcurve, _ in action_fcurves(action):
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "LINEAR"

        ground_samples_before = []
        ground_samples_after = []
        corrections = []
        for frame in range(frames[0], frames[-1] + 1):
            scene.frame_set(frame)
            rig.location = base_rig_location.copy()
            bpy.context.view_layer.update()
            minimum, maximum = evaluated_world_bounds(mesh_objects())
            ground_samples_before.append({"frame": frame, "ground_contact_z": float(minimum.z), "bounds_max_z": float(maximum.z)})
            correction = max(0.0, -float(minimum.z))
            rig.location.z = base_rig_location.z + correction
            rig.keyframe_insert(data_path="location", index=2, frame=frame, group=rig.name)
            bpy.context.view_layer.update()
            corrected_minimum, corrected_maximum = evaluated_world_bounds(mesh_objects())
            ground_samples_after.append({"frame": frame, "ground_contact_z": float(corrected_minimum.z), "bounds_max_z": float(corrected_maximum.z)})
            corrections.append(correction)

        scene.frame_set(frames[0])
        rig.location = base_rig_location.copy()
        metrics = action_metrics()
        report = {
            "action": action.name,
            "role": role,
            "frame_start": frames[0],
            "frame_end": frames[-1],
            "fps": scene.render.fps,
            "loop": role in {"idle", "move"},
            "keyed_bones": len(rig.pose.bones) * len(frames),
            "keyed_channels": len(rig.pose.bones) * len(frames) * 2,
            "ground_contact": {
                "minimum_z": min(item["ground_contact_z"] for item in ground_samples_after),
                "maximum_z": max(item["ground_contact_z"] for item in ground_samples_after),
                "samples_before": ground_samples_before,
                "samples_after": ground_samples_after,
            },
            "grounding_correction": {
                "applied": any(value > 0.0 for value in corrections),
                "maximum_translation_m": max(corrections, default=0.0),
            },
            "policy": "blender-authored-hoi4-humanoid-skeletal-action-in-place-no-scale-channels",
            "rig_and_actions": metrics,
            "status": "pass" if min(item["ground_contact_z"] for item in ground_samples_after) >= -0.01 else "needs_grounding_review",
        }
        report_path = job / "blender" / "reports" / f"humanoid_action_{role}.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        action_reports[role] = report

    save_blend(checkpoint)
    result = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "actions": action_reports,
        "required_roles": ["idle", "move", "attack", "death"],
        "source_policy": "Meshy 7 geometry retained; actions authored locally only after provider-rig recovery failure",
        "status": "pass" if all(item.get("status") == "pass" for item in action_reports.values()) else "needs_grounding_review",
    }
    report_path = job / "blender" / "reports" / "humanoid_actions.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def author_locomotion_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Author a small in-place walk cycle on the approved humanoid rig."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    if not rigs:
        raise RuntimeError("Locomotion authoring requires a working armature.")
    rig = rigs[0]
    if not rig.animation_data or rig.animation_data.action is None:
        raise RuntimeError("Locomotion authoring requires the approved base action.")
    base_action = rig.animation_data.action
    frames = [0, 6, 12, 18, 24]
    scene = bpy.context.scene
    scene.frame_set(0)
    base_snapshot: Dict[str, Tuple[Vector, Any]] = {
        bone.name: (bone.location.copy(), bone.rotation_quaternion.copy())
        for bone in rig.pose.bones
    }

    action_name = str(payload.get("action_name") or "Armature|Move|baselayer_WORKING")
    old_action = bpy.data.actions.get(action_name)
    if old_action is not None:
        bpy.data.actions.remove(old_action)
    action = bpy.data.actions.new(action_name)
    rig.animation_data.action = action

    phase_values = {0: 1.0, 6: 0.0, 12: -1.0, 18: 0.0, 24: 1.0}
    root_bob_amplitude = 0.001
    walk_angles = {
        "LeftUpLeg": 24.0,
        "RightUpLeg": -24.0,
        "LeftArm": -16.0,
        "RightArm": 16.0,
        "LeftForeArm": -6.0,
        "RightForeArm": 6.0,
        "Spine01": 2.0,
        "Spine02": 1.5,
        "neck": -1.0,
        "Head": -1.0,
    }
    knee_angles = {
        "LeftLeg": -10.0,
        "RightLeg": -10.0,
        "LeftFoot": 8.0,
        "RightFoot": 8.0,
    }
    keyed_bones = 0
    for frame in frames:
        scene.frame_set(frame)
        phase = phase_values[frame]
        for bone in rig.pose.bones:
            base_location, base_rotation = base_snapshot[bone.name]
            bone.rotation_mode = "QUATERNION"
            if bone.name == "Hips":
                bone.location = base_location + Vector((0.0, 0.0, root_bob_amplitude * phase))
            else:
                bone.location = base_location
            angle_degrees = walk_angles.get(bone.name, 0.0) * phase
            if bone.name in knee_angles:
                angle_degrees += knee_angles[bone.name] * (0.5 + 0.5 * abs(phase))
            if bone.name == "Hips":
                angle_degrees += 1.5 * phase
            delta = Quaternion((1.0, 0.0, 0.0), math.radians(angle_degrees))
            bone.rotation_quaternion = base_rotation @ delta
            bone.scale = (1.0, 1.0, 1.0)
            bone.keyframe_insert(data_path="location", frame=frame, group=bone.name)
            bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=bone.name)
            keyed_bones += 1

    scene.frame_start = 0
    scene.frame_end = 24
    scene.frame_set(0)
    for fcurve, _ in action_fcurves(action):
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = "LINEAR"
    move_ground_before, _ = evaluated_world_bounds(mesh_objects())
    move_ground_correction = 0.0
    move_root_curves = [
        fcurve
        for fcurve, _ in action_fcurves(action)
        if fcurve.data_path == 'pose.bones["Hips"].location'
    ]
    move_z_curve = next(
        (fcurve for fcurve in move_root_curves if fcurve.array_index == 2),
        None,
    )
    if move_z_curve is not None:
        test_step = 1.0
        for keyframe in move_z_curve.keyframe_points:
            keyframe.co[1] += test_step
            keyframe.handle_left[1] += test_step
            keyframe.handle_right[1] += test_step
        move_z_curve.update()
        bpy.context.view_layer.update()
        move_test_minimum, _ = evaluated_world_bounds(mesh_objects())
        for keyframe in move_z_curve.keyframe_points:
            keyframe.co[1] -= test_step
            keyframe.handle_left[1] -= test_step
            keyframe.handle_right[1] -= test_step
        move_z_curve.update()
        bpy.context.view_layer.update()
        derivative = float(move_test_minimum.z - move_ground_before.z) / test_step
        if abs(derivative) > 1e-8:
            move_ground_correction = -float(move_ground_before.z) / derivative
            for keyframe in move_z_curve.keyframe_points:
                keyframe.co[1] += move_ground_correction
                keyframe.handle_left[1] += move_ground_correction
                keyframe.handle_right[1] += move_ground_correction
            move_z_curve.update()
            bpy.context.view_layer.update()
    move_ground_after, _ = evaluated_world_bounds(mesh_objects())
    save_blend(checkpoint)
    metrics = action_metrics()
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "base_action": base_action.name,
        "action": action.name,
        "frame_start": 0,
        "frame_end": 24,
        "fps": scene.render.fps,
        "keyed_bones": keyed_bones,
        "keyed_channels": keyed_bones * 2,
        "root_translation_channel": "forced_with_submillimeter_in_place_bob",
        "root_bob_amplitude": root_bob_amplitude,
        "ground_contact_before": float(move_ground_before.z),
        "ground_contact_after": float(move_ground_after.z),
        "ground_correction_source_units": move_ground_correction,
        "policy": "blender_authored_in_place_walk_no_scale_channels",
        "rig_and_actions": metrics,
    }
    report_path = job / "blender" / "reports" / "author_locomotion_action.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _working_collection() -> bpy.types.Collection:
    collection = bpy.data.collections.get("WORKING")
    if collection is None:
        raise RuntimeError("Creature operation requires the WORKING collection.")
    return collection


def _component_record(obj: bpy.types.Object, index: int) -> Dict[str, Any]:
    minimum, maximum = world_bounds([obj])
    dimensions = maximum - minimum
    return {
        "index": index,
        "name": obj.name,
        "bounds_min": list(minimum),
        "bounds_max": list(maximum),
        "center": list((minimum + maximum) * 0.5),
        "dimensions": list(dimensions),
        "vertices": len(obj.data.vertices),
        "polygons": len(obj.data.polygons),
        "volume_proxy": float(max(dimensions.x, 0.0) * max(dimensions.y, 0.0) * max(dimensions.z, 0.0)),
        "materials": [material.name for material in obj.data.materials if material is not None],
    }


def _creature_spatial_profile(obj: bpy.types.Object, z_bins: int = 20, xy_bins: int = 8) -> Dict[str, Any]:
    """Return a deterministic face-centroid profile for a fused creature mesh.

    Meshy can return a single topologically connected shell even when the image
    clearly contains an elephant, howdah, and rider.  A profile lets the parent
    choose an explicit, reviewable spatial rider mask instead of silently
    treating the whole shell as a miniature.  This is diagnostic only; it does
    not infer a rider from a machine-learning classifier.
    """

    minimum, maximum = world_bounds([obj])
    dimensions = maximum - minimum
    safe_z = max(float(dimensions.z), 1e-9)
    safe_x = max(float(dimensions.x), 1e-9)
    safe_y = max(float(dimensions.y), 1e-9)
    profile_z = [0 for _ in range(max(1, z_bins))]
    profile_xy = [[0 for _ in range(max(1, xy_bins))] for _ in range(max(1, xy_bins))]
    z_area = [0.0 for _ in range(max(1, z_bins))]
    z_min = [float("inf") for _ in range(max(1, z_bins))]
    z_max = [float("-inf") for _ in range(max(1, z_bins))]
    high_centers: List[Vector] = []
    high_slices: Dict[int, List[Vector]] = {}
    high_face_counts: Dict[str, int] = {}
    for polygon in obj.data.polygons:
        center = obj.matrix_world @ polygon.center
        fraction_z = min(0.999999, max(0.0, (center.z - minimum.z) / safe_z))
        fraction_x = min(0.999999, max(0.0, (center.x - minimum.x) / safe_x))
        fraction_y = min(0.999999, max(0.0, (center.y - minimum.y) / safe_y))
        zi = min(len(profile_z) - 1, int(fraction_z * len(profile_z)))
        xi = min(len(profile_xy) - 1, int(fraction_x * len(profile_xy)))
        yi = min(len(profile_xy) - 1, int(fraction_y * len(profile_xy)))
        area = float(polygon.area)
        profile_z[zi] += 1
        profile_xy[xi][yi] += 1
        z_area[zi] += area
        z_min[zi] = min(z_min[zi], float(center.z))
        z_max[zi] = max(z_max[zi], float(center.z))
        if fraction_z >= 0.70:
            high_centers.append(center)
            high_bin = f"z_{int(fraction_z * 10):02d}"
            high_face_counts[high_bin] = high_face_counts.get(high_bin, 0) + 1
            high_slices.setdefault(int(fraction_z * 10), []).append(center)
    high_minimum = Vector((
        min((point.x for point in high_centers), default=minimum.x),
        min((point.y for point in high_centers), default=minimum.y),
        min((point.z for point in high_centers), default=minimum.z),
    ))
    high_maximum = Vector((
        max((point.x for point in high_centers), default=maximum.x),
        max((point.y for point in high_centers), default=maximum.y),
        max((point.z for point in high_centers), default=maximum.z),
    ))
    high_mean = Vector((
        sum(point.x for point in high_centers) / max(1, len(high_centers)),
        sum(point.y for point in high_centers) / max(1, len(high_centers)),
        sum(point.z for point in high_centers) / max(1, len(high_centers)),
    ))
    return {
        "object": obj.name,
        "bounds_min": list(minimum),
        "bounds_max": list(maximum),
        "dimensions": list(dimensions),
        "z_bins": [
            {
                "index": index,
                "fraction_min": index / max(1, len(profile_z)),
                "fraction_max": (index + 1) / max(1, len(profile_z)),
                "face_count": profile_z[index],
                "surface_area": z_area[index],
                "center_z_min": None if z_min[index] == float("inf") else z_min[index],
                "center_z_max": None if z_max[index] == float("-inf") else z_max[index],
            }
            for index in range(len(profile_z))
        ],
        "xy_face_bins": profile_xy,
        "face_count": len(obj.data.polygons),
        "high_region_centroid_stats": {
            "threshold_fraction_z": 0.70,
            "face_count": len(high_centers),
            "bounds_min": list(high_minimum),
            "bounds_max": list(high_maximum),
            "mean": list(high_mean),
            "z_decile_face_counts": high_face_counts,
            "z_decile_bounds": {
                str(decile): {
                    "face_count": len(points),
                    "bounds_min": [
                        min(point.x for point in points),
                        min(point.y for point in points),
                        min(point.z for point in points),
                    ],
                    "bounds_max": [
                        max(point.x for point in points),
                        max(point.y for point in points),
                        max(point.z for point in points),
                    ],
                    "mean": [
                        sum(point.x for point in points) / len(points),
                        sum(point.y for point in points) / len(points),
                        sum(point.z for point in points) / len(points),
                    ],
                }
                for decile, points in sorted(high_slices.items())
                if points
            },
        },
    }


def _duplicate_spatial_region(
    source: bpy.types.Object,
    name: str,
    keep_face,
) -> Dict[str, Any]:
    """Copy a fused mesh and retain only faces accepted by a bounded mask."""

    data = source.data.copy()
    region = bpy.data.objects.new(name, data)
    _working_collection().objects.link(region)
    region.matrix_world = source.matrix_world.copy()
    region["chaosx_working"] = True
    region["chaosx_creature_component"] = True
    bm = bmesh.new()
    bm.from_mesh(data)
    bm.faces.ensure_lookup_table()
    removed_faces = [face for face in bm.faces if not keep_face(source.matrix_world @ face.calc_center_median())]
    if removed_faces:
        bmesh.ops.delete(bm, geom=removed_faces, context="FACES")
    bm.verts.ensure_lookup_table()
    loose_vertices = [vertex for vertex in bm.verts if not vertex.link_faces]
    if loose_vertices:
        bmesh.ops.delete(bm, geom=loose_vertices, context="VERTS")
    bm.to_mesh(data)
    bm.free()
    data.update()
    region.hide_set(False)
    return {
        "object": region,
        "removed_faces": len(removed_faces),
        "kept_faces": len(data.polygons),
        "geometry": geometry_metrics_for_object(region),
    }


def segment_creature_components(req: Dict[str, Any]) -> Dict[str, Any]:
    """Separate a provider creature into loose or explicitly spatial components."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    component_prefix = safe_name(str(payload.get("component_prefix") or "elephant_component"))
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Creature segmentation found no working meshes.")
    region_mode = str(payload.get("region_mode") or "loose").casefold()
    if region_mode == "profile":
        profiles = [_creature_spatial_profile(obj) for obj in working]
        report_path = job / "blender" / "reports" / "creature_components.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report = {
            "blend": str(blend.relative_to(job)).replace("\\", "/"),
            "checkpoint": None,
            "source_working_objects": sorted(obj.name for obj in working),
            "component_count": len(working),
            "components": [_component_record(obj, index) for index, obj in enumerate(working)],
            "spatial_profiles": profiles,
            "method": "diagnostic polygon-centroid spatial profile; no geometry mutation",
            "status": "profile_only",
        }
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        return report
    before_names = {obj.name for obj in working}
    spatial_mask_applied = False
    spatial_mask = None
    if region_mode in {"spatial_rider", "spatial_semantic"}:
        if len(working) != 1:
            raise RuntimeError("Spatial rider segmentation requires exactly one fused source mesh.")
        source = working[0]
        minimum, maximum = world_bounds([source])
        dimensions = maximum - minimum
        z_min_fraction = float(payload.get("rider_z_min_fraction", 0.72))
        z_max_fraction = float(payload.get("rider_z_max_fraction", 1.0))
        x_center_fraction = float(payload.get("rider_x_center_fraction", 0.5))
        x_half_fraction = float(payload.get("rider_x_half_fraction", 0.38))
        y_center_fraction = float(payload.get("rider_y_center_fraction", 0.5))
        y_half_fraction = float(payload.get("rider_y_half_fraction", 0.42))
        if not (0.0 <= z_min_fraction < z_max_fraction <= 1.0):
            raise ValueError("Rider z fractions must satisfy 0 <= min < max <= 1.")
        if x_half_fraction <= 0.0 or y_half_fraction <= 0.0:
            raise ValueError("Rider spatial half-width fractions must be positive.")
        x_center = minimum.x + dimensions.x * x_center_fraction
        y_center = minimum.y + dimensions.y * y_center_fraction
        z_min = minimum.z + dimensions.z * z_min_fraction
        z_max = minimum.z + dimensions.z * z_max_fraction
        x_half = dimensions.x * x_half_fraction
        y_half = dimensions.y * y_half_fraction

        def is_rider(center: Vector) -> bool:
            return (
                z_min <= center.z <= z_max
                and abs(center.x - x_center) <= x_half
                and abs(center.y - y_center) <= y_half
            )

        rider_name = str(payload.get("rider_object_name") or "elephant_rider_region")
        body_name = str(payload.get("body_object_name") or "elephant_body_region")
        if region_mode == "spatial_semantic":
            def semantic_region(center: Vector) -> str:
                if is_rider(center):
                    return rider_name
                fx = (center.x - minimum.x) / max(float(dimensions.x), 1e-9)
                fy = (center.y - minimum.y) / max(float(dimensions.y), 1e-9)
                fz = (center.z - minimum.z) / max(float(dimensions.z), 1e-9)
                side = "left" if fx < 0.5 else "right"
                if fy > 0.82 and 0.20 <= fz <= 0.68:
                    return "tail"
                if fy < 0.24 and fz < 0.30 and 0.28 <= fx <= 0.72:
                    return "trunk_02"
                if fy < 0.30 and 0.30 <= fz < 0.54 and 0.25 <= fx <= 0.75:
                    return "trunk_01"
                if fy < 0.34 and fz >= 0.48:
                    return "head"
                if fz < 0.52 and (fx < 0.38 or fx > 0.62):
                    end = "front" if fy < 0.5 else "rear"
                    section = "lower" if fz < 0.25 else "upper"
                    return f"{end}_{side}_{section}"
                if fz > 0.68 and 0.25 <= fy <= 0.78:
                    return "howdah"
                return body_name

            semantic_names = [
                rider_name,
                body_name,
                "head",
                "trunk_01",
                "trunk_02",
                "tail",
                "howdah",
                "front_left_upper",
                "front_left_lower",
                "front_right_upper",
                "front_right_lower",
                "rear_left_upper",
                "rear_left_lower",
                "rear_right_upper",
                "rear_right_lower",
            ]
            semantic_components = []
            semantic_records = {}
            for semantic_name in semantic_names:
                record = _duplicate_spatial_region(
                    source,
                    semantic_name,
                    lambda center, expected=semantic_name: semantic_region(center) == expected,
                )
                if record["kept_faces"]:
                    semantic_components.append(record["object"])
                    semantic_records[semantic_name] = {
                        "faces": record["kept_faces"],
                        "geometry": record["geometry"],
                    }
                else:
                    bpy.data.objects.remove(record["object"], do_unlink=True)
            if rider_name not in semantic_records or body_name not in semantic_records:
                raise RuntimeError("Spatial semantic segmentation produced an empty rider or body region; adjust the explicit mask.")
            rider = {"object": next(obj for obj in semantic_components if obj.name == rider_name), "kept_faces": semantic_records[rider_name]["faces"], "geometry": semantic_records[rider_name]["geometry"]}
            body = {"object": next(obj for obj in semantic_components if obj.name == body_name), "kept_faces": semantic_records[body_name]["faces"], "geometry": semantic_records[body_name]["geometry"]}
            components = semantic_components
        else:
            rider = _duplicate_spatial_region(source, rider_name, is_rider)
            body = _duplicate_spatial_region(source, body_name, lambda center: not is_rider(center))
            if rider["kept_faces"] == 0 or body["kept_faces"] == 0:
                raise RuntimeError("Spatial rider segmentation produced an empty rider or body region; adjust the explicit mask.")
            components = [rider["object"], body["object"]]
        bpy.data.objects.remove(source, do_unlink=True)
        spatial_mask_applied = True
        spatial_mask = {
            "region_mode": region_mode,
            "rider_z_min_fraction": z_min_fraction,
            "rider_z_max_fraction": z_max_fraction,
            "rider_x_center_fraction": x_center_fraction,
            "rider_x_half_fraction": x_half_fraction,
            "rider_y_center_fraction": y_center_fraction,
            "rider_y_half_fraction": y_half_fraction,
            "rider_object": rider_name,
            "body_object": body_name,
            "rider_faces": rider["kept_faces"],
            "body_faces": body["kept_faces"],
            "rider_geometry": rider["geometry"],
            "body_geometry": body["geometry"],
            "semantic_regions": semantic_records if region_mode == "spatial_semantic" else None,
        }
    elif len(working) == 1:
        target = working[0]
        bpy.ops.object.select_all(action="DESELECT")
        target.select_set(True)
        bpy.context.view_layer.objects.active = target
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.separate(type="LOOSE")
        bpy.ops.object.mode_set(mode="OBJECT")
    collection = _working_collection()
    if not spatial_mask_applied:
        components = [obj for obj in collection.objects if obj.type == "MESH"]
    if not components:
        raise RuntimeError("Creature segmentation produced no mesh components.")
    discarded_degenerate_components = []
    retained_components = []
    for obj in components:
        if len(obj.data.polygons) == 0:
            discarded_degenerate_components.append(
                {
                    "object": obj.name,
                    "vertices": len(obj.data.vertices),
                    "polygons": 0,
                    "reason": "zero_face_component_cannot_be_reimported_as_a_runtime_mesh_node",
                }
            )
            bpy.data.objects.remove(obj, do_unlink=True)
        else:
            retained_components.append(obj)
    components = retained_components
    if not components:
        raise RuntimeError("Creature segmentation retained no renderable mesh components.")
    for obj in components:
        obj["chaosx_working"] = True
        obj["chaosx_creature_component"] = True
        obj.hide_set(False)
    components.sort(key=lambda obj: _component_record(obj, 0)["volume_proxy"], reverse=True)
    records = []
    for index, obj in enumerate(components):
        if not spatial_mask_applied:
            obj.name = f"{component_prefix}_{index:03d}"
        records.append(_component_record(obj, index))
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "source_working_objects": sorted(before_names),
        "component_count": len(records),
        "components": records,
        "discarded_degenerate_components": discarded_degenerate_components,
        "method": (
            "explicit polygon-centroid spatial rider/semantic mask on a fused approved working mesh"
            if spatial_mask_applied
            else "Blender mesh separate by loose parts on the approved working mesh"
        ),
        "spatial_mask": spatial_mask,
        "status": "review_required",
    }
    report_path = job / "blender" / "reports" / "creature_components.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


























def calibrate_creature_scale(req: Dict[str, Any]) -> Dict[str, Any]:
    """Scale the complete creature around its ground centre so the rider is infantry-sized."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    rider_names = [str(name) for name in payload.get("rider_component_names", [])]
    if not rider_names:
        raise RuntimeError("Creature scale calibration requires rider component names.")
    target_runtime = float(payload["target_rider_runtime_height_m"])
    entity_scale = float(payload.get("runtime_entity_scale", 0.8))
    if target_runtime <= 0.0 or entity_scale <= 0.0:
        raise RuntimeError("Creature scale calibration requires positive target and entity scale.")
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    by_name = {obj.name: obj for obj in working}
    missing = sorted(set(rider_names) - set(by_name))
    if missing:
        raise RuntimeError(f"Rider component names were not found: {missing}")
    rider_objects = [by_name[name] for name in rider_names]
    rider_minimum, rider_maximum = world_bounds(rider_objects)
    rider_source_height = float(rider_maximum.z - rider_minimum.z)
    if rider_source_height <= 0.0:
        raise RuntimeError("Rider component height is not positive.")
    target_source_height = target_runtime / entity_scale
    scale_factor = target_source_height / rider_source_height
    all_minimum, all_maximum = world_bounds(working)
    pivot = Vector(((all_minimum.x + all_maximum.x) * 0.5, (all_minimum.y + all_maximum.y) * 0.5, all_minimum.z))
    scale_matrix = Matrix.Translation(pivot) @ Matrix.Scale(scale_factor, 4) @ Matrix.Translation(-pivot)
    for obj in working:
        obj.matrix_world = scale_matrix @ obj.matrix_world
    bpy.context.view_layer.update()
    for obj in working:
        bpy.ops.object.select_all(action="DESELECT")
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.context.view_layer.update()
    rider_minimum_after, rider_maximum_after = world_bounds(rider_objects)
    final_minimum, final_maximum = world_bounds(working)
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "rider_components": rider_names,
        "rider_source_height_before_m": rider_source_height,
        "target_rider_source_height_m": target_source_height,
        "target_rider_runtime_height_m": target_runtime,
        "runtime_entity_scale": entity_scale,
        "uniform_scale_factor": scale_factor,
        "pivot": list(pivot),
        "rider_source_height_after_m": float(rider_maximum_after.z - rider_minimum_after.z),
        "rider_runtime_height_after_m": float(rider_maximum_after.z - rider_minimum_after.z) * entity_scale,
        "final_bounds_min": list(final_minimum),
        "final_bounds_max": list(final_maximum),
        "final_dimensions": list(final_maximum - final_minimum),
        "policy": "rider-calibrated-uniform-creature-scale-around-ground-centre",
        "status": "pass" if abs(float(rider_maximum_after.z - rider_minimum_after.z) * entity_scale - target_runtime) <= 0.01 else "fail",
    }
    report_path = job / "blender" / "reports" / "creature_scale.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if report["status"] != "pass":
        raise RuntimeError("Rider runtime height did not meet the requested infantry calibration.")
    return report


def _creature_bone_name_for_component(
    center: Vector,
    dimensions: Vector,
    bounds_minimum: Vector,
    bounds_maximum: Vector,
    rider_names: set[str],
    object_name: str,
    total_minimum: Vector,
    total_maximum: Vector,
) -> str:
    semantic_object_names = {
        "body",
        "head",
        "trunk_01",
        "trunk_02",
        "tail",
        "howdah",
        "front_left_upper",
        "front_left_lower",
        "front_right_upper",
        "front_right_lower",
        "rear_left_upper",
        "rear_left_lower",
        "rear_right_upper",
        "rear_right_lower",
    }
    if object_name in semantic_object_names:
        return object_name
    if object_name == "elephant_body_region":
        return "body"
    total_dimensions = total_maximum - total_minimum
    total_height = max(total_dimensions.z, 1e-6)
    total_length = max(total_dimensions.y, 1e-6)
    centre = (total_minimum + total_maximum) * 0.5
    if object_name in rider_names or center.z > total_minimum.z + total_height * 0.86:
        return "rider"
    if center.z > total_minimum.z + total_height * 0.72 and dimensions.z < total_height * 0.35:
        return "howdah"
    if center.y < centre.y - total_length * 0.23:
        if center.z > total_minimum.z + total_height * 0.45:
            return "head"
        return "trunk_02"
    if center.y > centre.y + total_length * 0.25:
        return "tail"
    if center.z < total_minimum.z + total_height * 0.45 and dimensions.z < total_height * 0.55:
        side = "left" if center.x < centre.x else "right"
        end = "front" if center.y < centre.y else "rear"
        return f"{end}_{side}_lower"
    return "body"


def _creature_bone_name_for_vertex(
    world_position: Vector,
    minimum: Vector,
    maximum: Vector,
    rider_names: set[str],
    object_name: str,
) -> str:
    """Assign one deterministic semantic bone to a creature vertex.

    The provider is a fused shell, so object-level rigid binding would leave
    every leg, trunk, and tail action inert.  This spatial rigid weighting is
    intentionally conservative: each vertex receives one full influence, with
    body fallback at ambiguous seams.  It is a real skeletal rig, not a
    transform-only animation substitute.
    """

    if object_name in rider_names:
        return "rider"
    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(float(dimensions.z), 1e-6)
    length = max(float(dimensions.y), 1e-6)
    width = max(float(dimensions.x), 1e-6)
    z_fraction = (world_position.z - minimum.z) / height
    y_fraction = (world_position.y - centre.y) / length
    x_fraction = (world_position.x - centre.x) / width
    # Highest forward geometry is the head and trunk.  The trunk is divided
    # into two bones to give attack/impact/deploy actions visible articulation.
    if y_fraction < -0.23:
        if z_fraction > 0.47:
            return "head"
        return "trunk_02"
    if y_fraction < -0.10 and z_fraction > 0.44:
        return "trunk_01"
    # The rearward elevated geometry is the tail/harness area.
    if y_fraction > 0.30 and z_fraction > 0.35:
        return "tail"
    if z_fraction > 0.70 and abs(x_fraction) < 0.28:
        return "howdah"
    # Legs are split into four quadrants, then upper/lower sections.  Use the
    # wider body fallback for belly vertices so no thin sliver is assigned to a
    # leg bone by accident.
    if z_fraction < 0.43 and abs(x_fraction) > 0.16:
        side = "left" if x_fraction < 0.0 else "right"
        end = "front" if y_fraction < 0.0 else "rear"
        if z_fraction < 0.22:
            return f"{end}_{side}_lower"
        return f"{end}_{side}_upper"
    return "body"


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


def _winged_biped_bone_name_for_vertex(
    world_position: Vector,
    minimum: Vector,
    maximum: Vector,
    object_name: str,
) -> str:
    """Assign one full semantic influence to a winged/digitigrade biped vertex."""

    if object_name in WINGED_BIPED_BONE_NAMES:
        return object_name
    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(float(dimensions.z), 1e-6)
    length = max(float(dimensions.y), 1e-6)
    width = max(float(dimensions.x), 1e-6)
    z_fraction = (world_position.z - minimum.z) / height
    y_fraction = (world_position.y - centre.y) / length
    x_fraction = (world_position.x - centre.x) / width
    side = "left" if x_fraction < 0.0 else "right"
    abs_x = abs(x_fraction)

    # The reference and the HOI4 unit axes use -Y as forward. Rearward,
    # elevated geometry is therefore the folded wing plane, not a tail.
    if abs_x > 0.25 and y_fraction > 0.06 and z_fraction > 0.48:
        if abs_x > 0.58:
            return f"wing_tip_{side}"
        if abs_x > 0.38:
            return f"wing_mid_{side}"
        return f"wing_root_{side}"
    if z_fraction > 0.82:
        return "head"
    if z_fraction > 0.67 and y_fraction < 0.04:
        return "neck"
    if 0.28 < z_fraction < 0.72 and 0.13 < abs_x < 0.58:
        return f"upper_arm_{side}" if z_fraction > 0.48 else f"lower_arm_{side}"
    if z_fraction < 0.13 and abs_x > 0.08:
        return f"foot_{side}"
    if z_fraction < 0.48 and abs_x > 0.09:
        return f"upper_leg_{side}" if z_fraction > 0.22 else f"lower_leg_{side}"
    if z_fraction > 0.45:
        return "spine"
    return "pelvis"


def author_winged_biped_rig(req: Dict[str, Any]) -> Dict[str, Any]:
    """Create a custom rigid-semantic rig for a winged/digitigrade biped."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    rig_name = safe_name(str(payload.get("rig_name") or "winged_biped_armature"))
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Winged biped rigging found no working meshes.")
    for rig in armatures():
        bpy.data.objects.remove(rig, do_unlink=True)
    minimum, maximum = world_bounds(working)
    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(float(dimensions.z), 1e-6)
    length = max(float(dimensions.y), 1e-6)
    width = max(float(dimensions.x), 1e-6)
    z0 = minimum.z
    y_front = centre.y - length * 0.06
    y_rear = centre.y + length * 0.10
    armature_data = bpy.data.armatures.new(rig_name)
    rig = bpy.data.objects.new(rig_name, armature_data)
    _working_collection().objects.link(rig)
    rig["chaosx_working"] = True
    rig["chaosx_custom_creature_rig"] = True
    rig["chaosx_creature_rig_family"] = "winged_biped"
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bones: Dict[str, bpy.types.EditBone] = {}

    def add_bone(name: str, head: Vector, tail: Vector, parent: str | None = None) -> None:
        bone = armature_data.edit_bones.new(name)
        bone.head = head
        bone.tail = tail
        if parent:
            bone.parent = bones[parent]
            bone.use_connect = False
        bones[name] = bone

    add_bone("root", Vector((centre.x, centre.y, z0)), Vector((centre.x, centre.y, z0 + height * 0.12)))
    add_bone("pelvis", Vector((centre.x, centre.y, z0 + height * 0.30)), Vector((centre.x, centre.y, z0 + height * 0.46)), "root")
    add_bone("spine", Vector((centre.x, centre.y, z0 + height * 0.44)), Vector((centre.x, centre.y, z0 + height * 0.67)), "pelvis")
    add_bone("neck", Vector((centre.x, y_front, z0 + height * 0.64)), Vector((centre.x, y_front, z0 + height * 0.76)), "spine")
    add_bone("head", Vector((centre.x, y_front, z0 + height * 0.74)), Vector((centre.x, y_front - length * 0.10, z0 + height * 0.84)), "neck")
    for side, sign in (("left", -1.0), ("right", 1.0)):
        shoulder = Vector((centre.x + sign * width * 0.20, centre.y - length * 0.01, z0 + height * 0.64))
        elbow = Vector((centre.x + sign * width * 0.34, centre.y - length * 0.04, z0 + height * 0.46))
        wrist = Vector((centre.x + sign * width * 0.40, centre.y - length * 0.07, z0 + height * 0.28))
        hand = Vector((centre.x + sign * width * 0.41, centre.y - length * 0.11, z0 + height * 0.20))
        add_bone(f"upper_arm_{side}", shoulder, elbow, "spine")
        add_bone(f"lower_arm_{side}", elbow, wrist, f"upper_arm_{side}")
        add_bone(f"hand_{side}", wrist, hand, f"lower_arm_{side}")
        hip = Vector((centre.x + sign * width * 0.13, centre.y + length * 0.01, z0 + height * 0.43))
        knee = Vector((centre.x + sign * width * 0.16, centre.y - length * 0.02, z0 + height * 0.23))
        ankle = Vector((centre.x + sign * width * 0.16, centre.y - length * 0.08, z0 + height * 0.08))
        foot = Vector((centre.x + sign * width * 0.16, centre.y - length * 0.16, z0 + height * 0.04))
        add_bone(f"upper_leg_{side}", hip, knee, "pelvis")
        add_bone(f"lower_leg_{side}", knee, ankle, f"upper_leg_{side}")
        add_bone(f"foot_{side}", ankle, foot, f"lower_leg_{side}")
        wing_root = Vector((centre.x + sign * width * 0.17, y_rear, z0 + height * 0.63))
        wing_mid = Vector((centre.x + sign * width * 0.40, y_rear + length * 0.03, z0 + height * 0.73))
        wing_tip = Vector((centre.x + sign * width * 0.68, y_rear + length * 0.06, z0 + height * 0.80))
        add_bone(f"wing_root_{side}", wing_root, wing_mid, "spine")
        add_bone(f"wing_mid_{side}", wing_mid, wing_tip, f"wing_root_{side}")
        add_bone(f"wing_tip_{side}", wing_tip, wing_tip + Vector((sign * width * 0.12, length * 0.02, height * 0.02)), f"wing_mid_{side}")
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.show_in_front = True
    armature_data.display_type = "BBONE"
    records = []
    for obj in working:
        for group in list(obj.vertex_groups):
            obj.vertex_groups.remove(group)
        groups = {bone.name: obj.vertex_groups.new(name=bone.name) for bone in armature_data.bones}
        counts: Dict[str, int] = {name: 0 for name in groups}
        for vertex in obj.data.vertices:
            bone_name = _winged_biped_bone_name_for_vertex(
                obj.matrix_world @ vertex.co,
                minimum,
                maximum,
                obj.name,
            )
            if bone_name not in groups:
                bone_name = "spine"
            groups[bone_name].add([vertex.index], 1.0, "REPLACE")
            counts[bone_name] += 1
        modifier = next((item for item in obj.modifiers if item.type == "ARMATURE"), None)
        if modifier is None:
            modifier = obj.modifiers.new("CHAOSX_CREATURE_ARMATURE", "ARMATURE")
        modifier.object = rig
        world_matrix = obj.matrix_world.copy()
        obj.parent = rig
        obj.parent_type = "OBJECT"
        obj.matrix_world = world_matrix
        records.append(
            {
                "object": obj.name,
                "bone": "spatial_semantic_weights",
                "vertices": len(obj.data.vertices),
                "vertex_group_counts": {name: count for name, count in counts.items() if count},
            }
        )
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "bones": [bone.name for bone in armature_data.bones],
        "component_bindings": records,
        "creature_rig_family": "winged_biped",
        "rig_map": f"{rig_name}_winged_biped_semantic_bones_v1",
        "weight_policy": "one full influence per vertex; spatial semantic wings, limbs, head, spine, and pelvis",
        "status": "pass",
    }
    report_path = job / "blender" / "reports" / "creature_rig.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def author_creature_rig(req: Dict[str, Any]) -> Dict[str, Any]:
    """Create a bounded creature armature and bind the approved mesh to semantic bones."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    if str(payload.get("creature_rig_family") or "elephant").casefold() == "winged_biped":
        return author_winged_biped_rig(req)
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    rider_names = {str(name) for name in payload.get("rider_component_names", [])}
    weight_mode = str(payload.get("weight_mode") or "semantic").casefold()
    rig_name = safe_name(str(payload.get("rig_name") or "elephant_shared_base_armature"))
    if weight_mode not in {"semantic", "automatic_body", "automatic_semantic"}:
        raise ValueError(f"Unsupported creature rig weight mode: {weight_mode}")
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    working = mesh_objects()
    if not working:
        raise RuntimeError("Creature rigging found no working meshes.")
    existing = armatures()
    for rig in existing:
        bpy.data.objects.remove(rig, do_unlink=True)
    minimum, maximum = world_bounds(working)
    dimensions = maximum - minimum
    centre = (minimum + maximum) * 0.5
    height = max(dimensions.z, 1e-6)
    length = max(dimensions.y, 1e-6)
    width = max(dimensions.x, 1e-6)
    armature_data = bpy.data.armatures.new(rig_name)
    rig = bpy.data.objects.new(rig_name, armature_data)
    _working_collection().objects.link(rig)
    rig["chaosx_working"] = True
    rig["chaosx_custom_creature_rig"] = True
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bones: Dict[str, bpy.types.EditBone] = {}

    def add_bone(name: str, head: Vector, tail: Vector, parent: str | None = None) -> None:
        bone = armature_data.edit_bones.new(name)
        bone.head = head
        bone.tail = tail
        if parent:
            bone.parent = bones[parent]
            bone.use_connect = False
        bones[name] = bone

    z0 = minimum.z
    add_bone("root", Vector((centre.x, centre.y, z0)), Vector((centre.x, centre.y, z0 + height * 0.18)))
    add_bone("body", Vector((centre.x, centre.y, z0 + height * 0.38)), Vector((centre.x, centre.y, z0 + height * 0.68)), "root")
    add_bone("neck", Vector((centre.x, minimum.y + length * 0.17, z0 + height * 0.62)), Vector((centre.x, minimum.y + length * 0.06, z0 + height * 0.79)), "body")
    add_bone("head", Vector((centre.x, minimum.y + length * 0.06, z0 + height * 0.76)), Vector((centre.x, minimum.y - length * 0.12, z0 + height * 0.73)), "neck")
    add_bone("trunk_01", Vector((centre.x, minimum.y - length * 0.10, z0 + height * 0.71)), Vector((centre.x, minimum.y - length * 0.22, z0 + height * 0.47)), "head")
    add_bone("trunk_02", Vector((centre.x, minimum.y - length * 0.22, z0 + height * 0.47)), Vector((centre.x, minimum.y - length * 0.27, z0 + height * 0.16)), "trunk_01")
    add_bone("tail", Vector((centre.x, maximum.y - length * 0.12, z0 + height * 0.56)), Vector((centre.x, maximum.y + length * 0.08, z0 + height * 0.48)), "body")
    for end, y in (("front", minimum.y + length * 0.30), ("rear", maximum.y - length * 0.28)):
        for side, x in (("left", centre.x - width * 0.30), ("right", centre.x + width * 0.30)):
            upper = f"{end}_{side}_upper"
            lower = f"{end}_{side}_lower"
            add_bone(upper, Vector((x, y, z0 + height * 0.48)), Vector((x, y, z0 + height * 0.20)), "body")
            add_bone(lower, Vector((x, y, z0 + height * 0.20)), Vector((x, y, z0 + height * 0.04)), upper)
    add_bone("howdah", Vector((centre.x, centre.y, z0 + height * 0.75)), Vector((centre.x, centre.y, z0 + height * 0.90)), "body")
    add_bone("rider", Vector((centre.x, centre.y, z0 + height * 0.88)), Vector((centre.x, centre.y, z0 + height * 1.08)), "howdah")
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.show_in_front = True
    armature_data.display_type = "BBONE"
    records = []
    rigid_semantic_objects = {
        "elephant_body_region", "head", "trunk_01", "trunk_02", "tail", "howdah",
        "front_left_upper", "front_left_lower", "front_right_upper", "front_right_lower",
        "rear_left_upper", "rear_left_lower", "rear_right_upper", "rear_right_lower",
    }
    for obj in working:
        obj_minimum, obj_maximum = world_bounds([obj])
        obj_center = (obj_minimum + obj_maximum) * 0.5
        for group in list(obj.vertex_groups):
            obj.vertex_groups.remove(group)
        groups = {
            bone.name: obj.vertex_groups.new(name=bone.name)
            for bone in armature_data.bones
        }
        counts: Dict[str, int] = {name: 0 for name in groups}
        if weight_mode in {"automatic_body", "automatic_semantic"} and obj.name == "elephant_body_region":
            bpy.ops.object.select_all(action="DESELECT")
            obj.select_set(True)
            rig.select_set(True)
            bpy.context.view_layer.objects.active = rig
            bpy.ops.object.parent_set(type="ARMATURE_AUTO")
            for vertex in obj.data.vertices:
                influence_map = {item.group: float(item.weight) for item in vertex.groups if item.weight > 0.0}
                if weight_mode == "automatic_semantic":
                    primary_name = _creature_bone_name_for_vertex(
                        obj.matrix_world @ vertex.co,
                        minimum,
                        maximum,
                        rider_names,
                        obj.name,
                    )
                    primary_group = obj.vertex_groups.get(primary_name)
                    influence_map = {group_index: weight * 0.30 for group_index, weight in influence_map.items()}
                    if primary_group is not None:
                        influence_map[primary_group.index] = influence_map.get(primary_group.index, 0.0) + 0.70
                influences = sorted(influence_map.items(), key=lambda item: item[1], reverse=True)[:4]
                total_weight = sum(weight for _, weight in influences)
                keep = {group_index for group_index, _ in influences}
                for group in obj.vertex_groups:
                    if group.index not in keep:
                        group.remove([vertex.index])
                if total_weight > 0.0:
                    for group_index, weight in influences:
                        obj.vertex_groups[group_index].add([vertex.index], weight / total_weight, "REPLACE")
            counts = {
                group.name: sum(1 for vertex in obj.data.vertices if any(item.group == group.index and item.weight > 0.0 for item in vertex.groups))
                for group in obj.vertex_groups
            }
            binding_policy = "blender_automatic_body_weights"
        elif obj.name in rigid_semantic_objects or obj.name in rider_names:
            bone_name = _creature_bone_name_for_component(
                obj_center,
                obj_maximum - obj_minimum,
                obj_minimum,
                obj_maximum,
                rider_names,
                obj.name,
                minimum,
                maximum,
            )
            if bone_name not in groups:
                bone_name = "body"
            groups[bone_name].add(list(range(len(obj.data.vertices))), 1.0, "REPLACE")
            counts[bone_name] = len(obj.data.vertices)
            binding_policy = "rigid_semantic_component"
        else:
            for vertex in obj.data.vertices:
                world_position = obj.matrix_world @ vertex.co
                bone_name = _creature_bone_name_for_vertex(
                    world_position,
                    minimum,
                    maximum,
                    rider_names,
                    obj.name,
                )
                if bone_name not in groups:
                    bone_name = "body"
                groups[bone_name].add([vertex.index], 1.0, "REPLACE")
                counts[bone_name] += 1
            binding_policy = "spatial_semantic_weights"
        modifier = next((item for item in obj.modifiers if item.type == "ARMATURE"), None)
        if modifier is None:
            modifier = obj.modifiers.new("CHAOSX_CREATURE_ARMATURE", "ARMATURE")
        modifier.object = rig
        world_matrix = obj.matrix_world.copy()
        obj.parent = rig
        obj.parent_type = "OBJECT"
        obj.matrix_world = world_matrix
        records.append(
            {
                "object": obj.name,
                "bone": binding_policy,
                "vertices": len(obj.data.vertices),
                "vertex_group_counts": {name: count for name, count in counts.items() if count},
            }
        )
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "bones": [bone.name for bone in armature_data.bones],
        "component_bindings": records,
        "rider_components": sorted(rider_names),
        "rig_map": f"{rig_name}_semantic_bones_v1",
        "requested_weight_mode": weight_mode,
        "weight_policy": "one full influence per vertex; explicitly segmented semantic objects use rigid component bindings and rider remains distinct",
        "status": "pass",
    }
    report_path = job / "blender" / "reports" / "creature_rig.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _action_delta(axis: str, degrees: float) -> Quaternion:
    vector = {"x": Vector((1.0, 0.0, 0.0)), "y": Vector((0.0, 1.0, 0.0)), "z": Vector((0.0, 0.0, 1.0))}[axis]
    return Quaternion(vector, math.radians(degrees))


def author_winged_biped_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Author a real skeletal action on the winged/digitigrade biped rig."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    role = str(payload.get("action_role") or "").casefold()
    action_name = safe_name(str(payload.get("action_name") or f"winged_biped_{role}"))
    if role not in {"idle", "move", "attack", "death"}:
        raise ValueError(f"Unsupported winged biped action role: {role}")
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    if len(rigs) != 1:
        raise RuntimeError(f"Winged biped action authoring requires exactly one armature, found {len(rigs)}.")
    rig = rigs[0]
    rig.animation_data_create()
    action = bpy.data.actions.get(action_name)
    if action is not None:
        bpy.data.actions.remove(action)
    action = bpy.data.actions.new(action_name)
    action.use_fake_user = True
    rig.animation_data.action = action
    if role == "idle":
        frames = [0, 12, 24, 36, 48]
    elif role == "move":
        frames = [0, 6, 12, 18, 24]
    elif role == "attack":
        frames = [0, 8, 16, 24, 32]
    else:
        frames = [0, 12, 24, 36]
    scene = bpy.context.scene
    scene.render.fps = int(payload.get("fps") or 30)
    scene.frame_start = frames[0]
    scene.frame_end = frames[-1]
    base = {
        bone.name: (bone.location.copy(), bone.rotation_quaternion.copy())
        for bone in rig.pose.bones
    }

    def phase(frame: int) -> float:
        span = max(frames[-1] - frames[0], 1)
        if role in {"idle", "move"}:
            return math.sin(2.0 * math.pi * (frame - frames[0]) / span)
        return (frame - frames[0]) / span

    def rotate(name: str, axis: str, degrees: float, value: float) -> None:
        bone = rig.pose.bones.get(name)
        if bone is None:
            return
        bone.rotation_mode = "QUATERNION"
        bone.rotation_quaternion = base[name][1] @ _action_delta(axis, degrees * value)

    keyed = 0
    for frame in frames:
        scene.frame_set(frame)
        p = phase(frame)
        for bone in rig.pose.bones:
            bone.rotation_mode = "QUATERNION"
            bone.location = base[bone.name][0].copy()
            bone.rotation_quaternion = base[bone.name][1].copy()
        if role == "idle":
            rotate("spine", "x", 1.5, p)
            rotate("neck", "x", 2.5, p)
            rotate("head", "z", 1.5, p)
            for side in ("left", "right"):
                rotate(f"wing_mid_{side}", "z", 2.0, p)
                rotate(f"wing_tip_{side}", "z", 3.0, p)
        elif role == "move":
            for side, sign in (("left", 1.0), ("right", -1.0)):
                gait = sign * p
                rotate(f"upper_leg_{side}", "x", 8.0, gait)
                rotate(f"lower_leg_{side}", "x", -5.0, gait)
                rotate(f"foot_{side}", "x", 2.5, gait)
                rotate(f"upper_arm_{side}", "x", -5.5, gait)
                rotate(f"lower_arm_{side}", "x", 3.0, gait)
                rotate(f"wing_mid_{side}", "z", 1.0, p)
                rotate(f"wing_tip_{side}", "z", 1.5, p)
            rotate("spine", "x", 2.0, p)
            rotate("head", "z", 1.0, p)
        elif role == "attack":
            rotate("spine", "x", -10.0, p)
            rotate("neck", "x", -8.0, p)
            rotate("head", "x", -12.0, p)
            for side, sign in (("left", 1.0), ("right", -1.0)):
                rotate(f"upper_arm_{side}", "x", -28.0, p)
                rotate(f"lower_arm_{side}", "x", -20.0, p)
                rotate(f"hand_{side}", "z", 8.0 * sign, p)
                rotate(f"wing_root_{side}", "z", 12.0 * sign, p)
                rotate(f"wing_mid_{side}", "z", 20.0 * sign, p)
                rotate(f"wing_tip_{side}", "z", 25.0 * sign, p)
            rotate("upper_leg_left", "x", -5.0, p)
            rotate("upper_leg_right", "x", -5.0, p)
        else:
            rotate("spine", "x", -42.0, p)
            rotate("neck", "x", -28.0, p)
            rotate("head", "x", -22.0, p)
            for side, sign in (("left", 1.0), ("right", -1.0)):
                rotate(f"upper_arm_{side}", "z", 24.0 * sign, p)
                rotate(f"lower_arm_{side}", "z", 18.0 * sign, p)
                rotate(f"wing_root_{side}", "z", -18.0 * sign, p)
                rotate(f"wing_mid_{side}", "z", -26.0 * sign, p)
                rotate(f"wing_tip_{side}", "z", -32.0 * sign, p)
                rotate(f"upper_leg_{side}", "x", 10.0, p)
                rotate(f"lower_leg_{side}", "x", 12.0, p)
        for bone in rig.pose.bones:
            bone.keyframe_insert(data_path="location", frame=frame, group=bone.name)
            bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=bone.name)
            keyed += 1
    for fcurve, _ in action_fcurves(action):
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = "LINEAR"

    if rig.pose.bones.get("root") is None:
        raise RuntimeError("Winged biped action authoring requires a root bone.")
    base_rig_location = rig.location.copy()
    ground_samples_before = []
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        minimum, maximum = evaluated_world_bounds(mesh_objects())
        ground_samples_before.append({"frame": frame, "ground_contact_z": float(minimum.z), "bounds_max_z": float(maximum.z)})
    corrections = []
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        # Measure each pose from the uncorrected armature location.  Without
        # this reset, previously keyed offsets are included in the next sample
        # and the correction drifts instead of remaining an absolute offset.
        rig.location = base_rig_location.copy()
        bpy.context.view_layer.update()
        minimum, _ = evaluated_world_bounds(mesh_objects())
        correction = max(
            0.0,
            -float(minimum.z) + CREATURE_GROUND_CONTACT_CLEARANCE_M,
        )
        # Mesh objects are parented to the armature object in the custom route.
        # Keying the root pose bone alone does not translate the evaluated object
        # bounds, so ground correction must be authored on the armature object.
        rig.location = base_rig_location.copy()
        rig.location.z = base_rig_location.z + correction
        rig.keyframe_insert(data_path="location", index=2, frame=frame, group=rig.name)
        corrections.append(correction)
    for fcurve, _ in action_fcurves(action):
        if fcurve.data_path.endswith(".location") and fcurve.array_index == 2:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "LINEAR"
            fcurve.update()
    ground_samples_after = []
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        minimum, maximum = evaluated_world_bounds(mesh_objects())
        ground_samples_after.append({"frame": frame, "ground_contact_z": float(minimum.z), "bounds_max_z": float(maximum.z)})
    minimum_ground = min(item["ground_contact_z"] for item in ground_samples_after)
    maximum_ground = max(item["ground_contact_z"] for item in ground_samples_after)
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "action": action.name,
        "role": role,
        "frame_start": frames[0],
        "frame_end": frames[-1],
        "fps": scene.render.fps,
        "loop": role in {"idle", "move"},
        "keyed_bones": keyed,
        "keyed_channels": keyed * 2,
        "ground_contact": {
            "minimum_z": minimum_ground,
            "maximum_z": maximum_ground,
            "sample_count": len(ground_samples_after),
            "samples_before": ground_samples_before,
            "samples_after": ground_samples_after,
        },
        "grounding_correction": {
            "applied": any(value > 0.0 for value in corrections),
            "maximum_translation_m": max(corrections, default=0.0),
            "samples_before": ground_samples_before,
            "samples_after": ground_samples_after,
        },
        "creature_rig_family": "winged_biped",
        "policy": "blender-authored-winged-biped-semantic-skeletal-action-no-scale-channels",
        "status": (
            "pass"
            if minimum_ground >= -CREATURE_GROUND_CONTACT_TOLERANCE_M
            else "needs_grounding_review"
        ),
    }
    report_path = job / "blender" / "reports" / f"creature_action_{safe_name(role)}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def author_creature_action(req: Dict[str, Any]) -> Dict[str, Any]:
    """Author one semantic skeletal action for the custom creature rig."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    if str(payload.get("creature_rig_family") or "elephant").casefold() == "winged_biped":
        return author_winged_biped_action(req)
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    role = str(payload.get("action_role") or "").casefold()
    action_name = safe_name(str(payload.get("action_name") or f"creature_{role}"))
    allowed_roles = {"idle", "move", "retreat", "deploy", "supply_load", "attack", "impact", "death"}
    if role not in allowed_roles:
        raise ValueError(f"Unsupported creature action role: {role}")
    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    if len(rigs) != 1:
        raise RuntimeError(f"Creature action authoring requires exactly one armature, found {len(rigs)}.")
    rig = rigs[0]
    rig.animation_data_create()
    action = bpy.data.actions.get(action_name)
    if action is not None:
        bpy.data.actions.remove(action)
    action = bpy.data.actions.new(action_name)
    action.use_fake_user = True
    rig.animation_data.action = action
    if role == "idle":
        frames = [0, 12, 24, 36, 48]
    elif role in {"move", "retreat"}:
        frames = [0, 6, 12, 18, 24]
    elif role == "deploy":
        frames = [0, 12, 24, 36]
    elif role == "supply_load":
        frames = [0, 10, 20, 30, 40]
    elif role == "attack":
        frames = [0, 8, 16, 24, 32]
    elif role == "death":
        frames = [0, 12, 24, 36]
    else:
        frames = [0, 6, 12, 18, 24]
    scene = bpy.context.scene
    scene.frame_start = frames[0]
    scene.frame_end = frames[-1]
    base = {
        bone.name: (bone.location.copy(), bone.rotation_quaternion.copy())
        for bone in rig.pose.bones
    }

    def phase(frame: int) -> float:
        if role in {"idle", "move", "retreat"}:
            return math.sin(2.0 * math.pi * (frame - frames[0]) / max(frames[-1] - frames[0], 1))
        if role == "deploy":
            return (frame - frames[0]) / max(frames[-1] - frames[0], 1)
        if role == "supply_load":
            return math.sin(math.pi * (frame - frames[0]) / max(frames[-1] - frames[0], 1))
        if role == "attack":
            return math.sin(math.pi * (frame - frames[0]) / max(frames[-1] - frames[0], 1))
        if role == "death":
            return (frame - frames[0]) / max(frames[-1] - frames[0], 1)
        return math.sin(math.pi * (frame - frames[0]) / max(frames[-1] - frames[0], 1))

    keyed = 0
    for frame in frames:
        scene.frame_set(frame)
        p = phase(frame)
        for bone in rig.pose.bones:
            location, rotation = base[bone.name]
            bone.rotation_mode = "QUATERNION"
            bone.location = location.copy()
            bone.rotation_quaternion = rotation.copy()
            if role == "idle":
                if bone.name in {"body", "neck"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.6 * p)
                if bone.name in {"trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.2 * p)
            elif role in {"move", "retreat"}:
                cycle_phase = p if role == "move" else -p
                if bone.name == "body":
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.5 * cycle_phase)
                if bone.name in {"front_left_lower", "rear_right_lower"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.0 * cycle_phase)
                if bone.name in {"front_right_lower", "rear_left_lower"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.0 * cycle_phase)
                if bone.name in {"front_left_upper", "rear_right_upper"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.5 * cycle_phase)
                if bone.name in {"front_right_upper", "rear_left_upper"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.5 * cycle_phase)
                if bone.name in {"neck", "trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.8 * cycle_phase)
            elif role == "deploy":
                if bone.name == "body":
                    bone.rotation_quaternion = rotation @ _action_delta("x", -0.05 * p)
                if bone.name in {"neck", "head"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.20 * p)
                if bone.name in {"trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -0.50 * p)
            elif role == "supply_load":
                if bone.name in {"neck", "head", "trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.00 * p)
                if bone.name == "body":
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.05 * p)
            elif role == "attack":
                if bone.name in {"body", "neck", "head"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.0 * p)
                if bone.name in {"trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -2.0 * p)
                if bone.name in {"front_left_lower", "front_right_lower"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.0 * p)
            elif role == "death":
                if bone.name in {"body", "neck", "head"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.5 * p)
                if bone.name in {"trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -2.5 * p)
                if bone.name in {"front_left_upper", "rear_right_upper"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", -1.0 * p)
                if bone.name in {"front_right_upper", "rear_left_upper"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.0 * p)
                if bone.name in {"front_left_lower", "front_right_lower", "rear_left_lower", "rear_right_lower"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 1.5 * p)
            elif role == "impact":
                if bone.name in {"body", "neck", "head"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.04 * p)
                if bone.name in {"trunk_01", "trunk_02"}:
                    bone.rotation_quaternion = rotation @ _action_delta("x", 0.08 * p)
                if bone.name.startswith("front_"):
                    bone.rotation_quaternion = rotation @ _action_delta("x", -0.05 * p)
            bone.keyframe_insert(data_path="location", frame=frame, group=bone.name)
            bone.keyframe_insert(data_path="rotation_quaternion", frame=frame, group=bone.name)
            keyed += 1
    for fcurve, _ in action_fcurves(action):
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = "LINEAR"
    scene.frame_set(frames[0])
    bpy.context.view_layer.update()
    ground_samples = []
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        minimum, maximum = evaluated_world_bounds(mesh_objects())
        ground_samples.append({"frame": frame, "ground_contact_z": float(minimum.z), "bounds_max_z": float(maximum.z)})
    minimum_ground = min(item["ground_contact_z"] for item in ground_samples)
    maximum_ground = max(item["ground_contact_z"] for item in ground_samples)
    grounding_correction = {
        "applied": False,
        "root_bone": "root",
        "epsilon_m": CREATURE_GROUND_CONTACT_TOLERANCE_M,
        "clearance_m": CREATURE_GROUND_CONTACT_CLEARANCE_M,
        "maximum_translation_m": 0.0,
        "samples_before": ground_samples,
    }
    root = rig.pose.bones.get("root") or rig.pose.bones.get("body")
    if root is None:
        raise RuntimeError("Creature action authoring requires a semantic root bone.")
    # Ground every sampled frame with an explicit root translation channel.
    # This preserves the authored rotations and avoids feet/underside sinking
    # below the map plane after large elephant rotations.
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        current_minimum, _ = evaluated_world_bounds(mesh_objects())
        # Treat one centimetre as the contact tolerance used by the report.
        # Do not claim a lift when the semantic body channel cannot move the
        # rigidly separated shell in Blender's evaluated armature; such a case
        # remains visible as a failed contact sample instead of a silent fix.
        correction = max(
            0.0,
            -float(current_minimum.z) + CREATURE_GROUND_CONTACT_CLEARANCE_M,
        )
        if correction:
            # Lift the common root so the correction is represented once in
            # the exported skeleton and is not multiplied down child bones.
            root.location.z = base[root.name][0].z + correction
            root.keyframe_insert(data_path="location", index=2, frame=frame, group=root.name)
            grounding_correction["applied"] = True
            grounding_correction["maximum_translation_m"] = max(
                float(grounding_correction["maximum_translation_m"]), correction
            )
        root.keyframe_insert(data_path="location", index=2, frame=frame, group=root.name)
    for fcurve, _ in action_fcurves(action):
        if fcurve.data_path.endswith(".location") and fcurve.array_index == 2:
            for keyframe in fcurve.keyframe_points:
                keyframe.interpolation = "LINEAR"
            fcurve.update()
    scene.frame_set(frames[0])
    bpy.context.view_layer.update()
    corrected_samples = []
    for frame in range(frames[0], frames[-1] + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        current_minimum, current_maximum = evaluated_world_bounds(mesh_objects())
        corrected_samples.append(
            {
                "frame": frame,
                "ground_contact_z": float(current_minimum.z),
                "bounds_max_z": float(current_maximum.z),
            }
        )
    ground_samples = corrected_samples
    minimum_ground = min(item["ground_contact_z"] for item in ground_samples)
    maximum_ground = max(item["ground_contact_z"] for item in ground_samples)
    grounding_correction["samples_after"] = ground_samples
    grounding_correction["minimum_after_m"] = minimum_ground
    grounding_correction["maximum_after_m"] = maximum_ground
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "armature": rig.name,
        "action": action.name,
        "role": role,
        "frame_start": frames[0],
        "frame_end": frames[-1],
        "fps": scene.render.fps,
        "loop": role in {"idle", "move", "retreat"},
        "keyed_bones": keyed,
        "keyed_channels": keyed * 2,
        "ground_contact": {
            "minimum_z": minimum_ground,
            "maximum_z": maximum_ground,
            "sample_count": len(ground_samples),
            "samples": ground_samples,
        },
        "grounding_correction": grounding_correction,
        "policy": "blender-authored-semantic-skeletal-action-no-scale-channels",
        "status": (
            "pass"
            if minimum_ground >= -CREATURE_GROUND_CONTACT_TOLERANCE_M
            else "needs_grounding_review"
        ),
    }
    report_path = job / "blender" / "reports" / f"creature_action_{safe_name(role)}.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def correct_action_grounding(req: Dict[str, Any]) -> Dict[str, Any]:
    """Correct one existing skeletal action's root contact, preserving body keys."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    target_armature_name = explicit_safe_name(payload.get("target_armature_name"), "target_armature_name")
    action_name = explicit_action_name(payload.get("action_name"), "action_name")
    root_bone_name = explicit_safe_name(payload.get("root_bone"), "root_bone")
    grounding_policy = str(payload.get("grounding_policy") or "")
    if grounding_policy != "per_frame_root_contact_zero_clearance":
        raise ValueError(
            "grounding_policy must be per_frame_root_contact_zero_clearance; "
            "the adapter does not author or synthesize replacement body motion."
        )

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    matching_rigs = [rig for rig in rigs if rig.name == target_armature_name]
    if len(rigs) != 1 or len(matching_rigs) != 1:
        raise RuntimeError(
            "Grounding correction requires exactly one explicitly named working armature: "
            + json.dumps(
                {
                    "requested_target_armature": target_armature_name,
                    "available_armatures": sorted(rig.name for rig in rigs),
                },
                sort_keys=True,
            )
        )
    rig = matching_rigs[0]
    rig.animation_data_create()
    action = bpy.data.actions.get(action_name)
    if action is None:
        action = next(
            (
                candidate
                for candidate in bpy.data.actions
                if candidate.name.casefold() == action_name.casefold()
            ),
            None,
        )
    if action is None:
        raise RuntimeError(f"Requested action was not found: {action_name}")
    provenance = action_provenance(action)
    fcurve_count_before = len(list(action_fcurves(action)))
    rig.animation_data.action = action
    root = rig.pose.bones.get(root_bone_name)
    if root is None:
        raise RuntimeError(f"Grounding correction root bone was not found: {root_bone_name}")
    meshes = mesh_objects()
    if not meshes:
        raise RuntimeError("Grounding correction found no working mesh objects.")

    start = int(math.floor(float(action.frame_range[0])))
    end = int(math.ceil(float(action.frame_range[1])))
    if end < start:
        raise RuntimeError("Grounding correction requires a non-empty action frame range.")
    scene = bpy.context.scene
    scene.frame_start = start
    scene.frame_end = end

    # Blender pose-bone location channels use bone-local axes. Detect which
    # local channel produces the strongest world-Z response, then key that
    # channel at every integer frame so no sparse-key overshoot is introduced.
    scene.frame_set(start)
    bpy.context.view_layer.update()
    baseline_minimum, _ = evaluated_world_bounds(meshes)
    axis_responses = []
    for axis_index in range(3):
        original_axis_value = float(root.location[axis_index])
        root.location[axis_index] = original_axis_value + 1.0
        bpy.context.view_layer.update()
        test_minimum, _ = evaluated_world_bounds(meshes)
        root.location[axis_index] = original_axis_value
        bpy.context.view_layer.update()
        axis_responses.append(float(test_minimum.z - baseline_minimum.z))
    correction_axis = max(range(3), key=lambda index: abs(axis_responses[index]))
    if abs(axis_responses[correction_axis]) <= 1e-8:
        raise RuntimeError("Grounding correction found no usable pose-location response on any local axis.")
    for frame in range(start, end + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        root.keyframe_insert(data_path="location", index=correction_axis, frame=frame, group=root_bone_name)

    z_path = f'pose.bones["{root_bone_name}"].location'
    correction_curve = next(
        (
            fcurve
            for fcurve, _ in action_fcurves(action)
            if fcurve.data_path == z_path and fcurve.array_index == correction_axis
        ),
        None,
    )
    if correction_curve is None or len(correction_curve.keyframe_points) < end - start + 1:
        raise RuntimeError("Grounding correction could not create the selected root location channel.")
    for keyframe in correction_curve.keyframe_points:
        keyframe.interpolation = "LINEAR"
    correction_curve.update()

    frame_records: List[Dict[str, Any]] = []
    max_correction = 0.0
    before_values: List[float] = []
    after_values: List[float] = []

    def write_root_z(frame: int, value: float) -> None:
        root.location[correction_axis] = value
        root.keyframe_insert(data_path="location", index=correction_axis, frame=frame, group=root_bone_name)
        correction_curve.update()
        bpy.context.view_layer.update()

    for frame in range(start, end + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        before_minimum, _ = evaluated_world_bounds(meshes)
        original_value = float(root.location[correction_axis])
        test_step = 1.0
        write_root_z(frame, original_value + test_step)
        test_minimum, _ = evaluated_world_bounds(meshes)
        write_root_z(frame, original_value)
        derivative = float(test_minimum.z - before_minimum.z) / test_step
        if abs(derivative) <= 1e-8:
            raise RuntimeError(f"Grounding correction found no usable root-Z response at frame {frame}.")
        correction = -float(before_minimum.z) / derivative
        write_root_z(frame, original_value + correction)
        after_minimum, _ = evaluated_world_bounds(meshes)
        before_values.append(float(before_minimum.z))
        after_values.append(float(after_minimum.z))
        max_correction = max(max_correction, abs(correction))
        frame_records.append(
            {
                "frame": frame,
                "ground_contact_before": float(before_minimum.z),
                "ground_contact_after": float(after_minimum.z),
                "derivative": derivative,
                "correction_source_units": correction,
            }
        )

    scene.frame_set(start)
    bpy.context.view_layer.update()
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "action": action.name,
        "root_bone": root_bone_name,
        "target_armature": rig.name,
        "root_location_axis_index": correction_axis,
        "root_location_axis_world_z_responses": axis_responses,
        "frame_start": start,
        "frame_end": end,
        "fps": scene.render.fps,
        "corrected_frames": len(frame_records),
        "max_absolute_correction_source_units": max_correction,
        "ground_contact_before": {
            "minimum": min(before_values),
            "maximum": max(before_values),
        },
        "ground_contact_after": {
            "minimum": min(after_values),
            "maximum": max(after_values),
        },
        "action_preservation": {
            "grounding_policy": grounding_policy,
            "policy": "existing_action_root_z_only",
            "body_motion_replaced": False,
            "new_model_created": False,
            "new_rig_created": False,
            "new_provider_call": False,
        },
        "action_provenance": provenance,
        "retention_evidence": {
            "fcurve_count_before": fcurve_count_before,
            "fcurve_count_after": len(list(action_fcurves(action))),
            "only_root_location_channel_corrected": True,
            "body_motion_keys_retained": True,
            "manual_or_procedural_replacement_authored": False,
        },
        "frames": frame_records,
        "status": "pass" if max(after_values) <= 0.001 and min(after_values) >= -0.001 else "fail",
    }
    report_path = job / "blender" / "reports" / f"correct_action_grounding_{safe_name(action.name)}.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if report["status"] != "pass":
        raise RuntimeError(
            "Grounding correction did not satisfy the per-frame contact tolerance: "
            f"{report['ground_contact_after']}"
        )
    return report


def offset_action_root(req: Dict[str, Any]) -> Dict[str, Any]:
    """Apply a bounded source-space root offset to an existing action frame range."""

    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    blend = within(job, payload["blend_rel"])
    checkpoint = within(job, payload["checkpoint_rel"], allow_missing=True)
    action_name = str(payload.get("action_name") or "")
    frame_start = int(payload.get("frame_start"))
    frame_end = int(payload.get("frame_end"))
    offset_source_units = float(payload.get("offset_source_units") or 0.0)
    axis_index = int(payload.get("axis_index", 1))
    if not action_name:
        raise ValueError("Root offset requires an action name.")
    if frame_end < frame_start:
        raise ValueError("Root offset frame_end must not precede frame_start.")
    if axis_index not in {0, 1, 2}:
        raise ValueError("Root offset axis_index must be 0, 1, or 2.")

    bpy.ops.wm.open_mainfile(filepath=str(blend))
    rigs = armatures()
    if len(rigs) != 1:
        raise RuntimeError(f"Root offset requires exactly one working armature, found {len(rigs)}.")
    rig = rigs[0]
    action = bpy.data.actions.get(action_name)
    if action is None:
        action = next(
            (
                candidate
                for candidate in bpy.data.actions
                if candidate.name.casefold() == action_name.casefold()
            ),
            None,
        )
    if action is None:
        raise RuntimeError(f"Requested action was not found: {action_name}")
    root_bone_name = str(payload.get("root_bone") or "Hips")
    rig.animation_data_create()
    rig.animation_data.action = action
    root = rig.pose.bones.get(root_bone_name)
    if root is None:
        raise RuntimeError(f"Root offset bone was not found: {root_bone_name}")

    scene = bpy.context.scene
    scene.frame_start = frame_start
    scene.frame_end = frame_end
    correction_curve = None
    path = f'pose.bones["{root_bone_name}"].location'
    for fcurve, _ in action_fcurves(action):
        if fcurve.data_path == path and fcurve.array_index == axis_index:
            correction_curve = fcurve
            break
    for frame in range(frame_start, frame_end + 1):
        scene.frame_set(frame)
        bpy.context.view_layer.update()
        root.location[axis_index] = float(root.location[axis_index]) + offset_source_units
        root.keyframe_insert(data_path="location", index=axis_index, frame=frame, group=root_bone_name)
    if correction_curve is None:
        for fcurve, _ in action_fcurves(action):
            if fcurve.data_path == path and fcurve.array_index == axis_index:
                correction_curve = fcurve
                break
    if correction_curve is not None:
        correction_curve.update()
    scene.frame_set(frame_start)
    bpy.context.view_layer.update()
    save_blend(checkpoint)
    report = {
        "blend": str(blend.relative_to(job)).replace("\\", "/"),
        "checkpoint": str(checkpoint.relative_to(job)).replace("\\", "/"),
        "target_armature": rig.name,
        "action": action.name,
        "root_bone": root_bone_name,
        "axis_index": axis_index,
        "frame_start": frame_start,
        "frame_end": frame_end,
        "offset_source_units": offset_source_units,
        "corrected_frames": frame_end - frame_start + 1,
        "policy": "bounded_existing_action_root_frame_offset_for_export_reimport_contact",
        "body_motion_replaced": False,
        "new_model_created": False,
        "new_rig_created": False,
        "new_provider_call": False,
        "warnings": [],
    }
    report_path = job / "blender" / "reports" / f"offset_action_root_{safe_name(action.name)}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def reimport_export(req: Dict[str, Any], pdx: Dict[str, Any]) -> Dict[str, Any]:
    job = Path(req["job_root"]).resolve()
    payload = req["payload"]
    mesh = within(job, payload["mesh_rel"])
    anim = within(job, payload["anim_rel"]) if payload.get("anim_rel") else None
    texture_staging = []
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
    for texture_name in tuple(dict.fromkeys(requested_texture_names + default_texture_names)):
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
            {"name": obj.name, "type": obj.type}
            for obj in bpy.context.scene.objects
        ],
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
    weights = sanitize_working_weights(preserve_skeleton_metadata=weight_only)
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
    pdx = None
    if operation not in {"health", "inspect_scene", "save_checkpoint", "sanitize_runtime_candidate", "retime_animation_action", "offset_action_root", "bake_static_mesh_transforms", "partition_static_mesh_export_batches"}:
        pdx = load_pdx(req["io_pdx_root"])
    if operation == "health":
        return health(req)
    if operation == "prepare_candidate":
        return prepare(req, pdx)
    if operation == "inspect_scene":
        return inspect(req)
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
    if operation == "import_animation_action":
        return import_animation_action(req)
    if operation == "import_bvh_animation_action":
        return import_bvh_animation_action(req)
    if operation == "retime_animation_action":
        return retime_animation_action(req)
    if operation == "author_humanoid_rig":
        return author_humanoid_rig(req)
    if operation == "author_humanoid_actions":
        return author_humanoid_actions(req)
    if operation == "author_locomotion_action":
        return author_locomotion_action(req)
    if operation == "segment_creature_components":
        return segment_creature_components(req)
    if operation == "calibrate_creature_scale":
        return calibrate_creature_scale(req)
    if operation == "author_creature_rig":
        return author_creature_rig(req)
    if operation == "author_creature_action":
        return author_creature_action(req)
    if operation == "correct_action_grounding":
        return correct_action_grounding(req)
    if operation == "offset_action_root":
        return offset_action_root(req)
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
