"""User-authorized existing-mesh rig/action recovery for Event 016 units.

This script does not generate or replace geometry. It normalizes the selected
checkpoint, creates a package-specific armature, assigns bounded four-bone
weights, preserves/attaches only the already-approved firearm where required,
and authors genuine multi-frame skeletal actions. The resulting .blend is then
exported and reimported through the locked Chaos Redux adapter by the parent.

The direct Blender invocation is an explicit user-authorized exception to the
normal provider-only motion route for this recovery pass. Every output remains
a candidate until adapter export/reimport and runtime review succeed.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import bpy
from mathutils import Matrix, Vector


ROOT = Path(__file__).resolve().parents[3]
RIFLE_BLEND = ROOT / "docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/reimport_vanilla_ENG_weapon_rifle.blend"
VANILLA_UNIT_TEXTURES = Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units")


def v3(values: Sequence[float]) -> Vector:
    return Vector((float(values[0]), float(values[1]), float(values[2])))


def remove_object(obj: bpy.types.Object) -> None:
    bpy.data.objects.remove(obj, do_unlink=True)


def selected_mesh(name: str) -> bpy.types.Object:
    obj = bpy.data.objects.get(name)
    if obj is None or obj.type != "MESH":
        raise RuntimeError(f"Visible source mesh not found: {name}")
    return obj


def world_bounds(obj: bpy.types.Object) -> Tuple[Vector, Vector]:
    points = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    return (
        Vector((min(point.x for point in points), min(point.y for point in points), min(point.z for point in points))),
        Vector((max(point.x for point in points), max(point.y for point in points), max(point.z for point in points))),
    )


def bake_object_world_transform(obj: bpy.types.Object, pre_rotation: Matrix | None = None) -> None:
    """Bake a mesh's current world transform into its vertices and reset it."""

    transform = obj.matrix_world.copy()
    if pre_rotation is not None:
        transform = pre_rotation @ transform
    # Detach first while retaining the evaluated world matrix.  Assigning an
    # identity matrix before clearing a scaled parent would otherwise leave the
    # parent scale baked a second time when Blender recomputes matrix_basis.
    obj.parent = None
    obj.matrix_world = Matrix.Identity(4)
    for vertex in obj.data.vertices:
        vertex.co = transform @ vertex.co
    obj.matrix_world = Matrix.Identity(4)
    obj.data.update()
    bpy.context.view_layer.update()


def clear_scene_except(mesh: bpy.types.Object) -> None:
    for obj in list(bpy.data.objects):
        if obj != mesh:
            remove_object(obj)
    for armature in list(bpy.data.armatures):
        if armature.users == 0:
            bpy.data.armatures.remove(armature)


def normalize_ground(mesh: bpy.types.Object) -> Tuple[Vector, Vector]:
    minimum, maximum = world_bounds(mesh)
    for vertex in mesh.data.vertices:
        vertex.co.z -= minimum.z
    mesh.data.update()
    bpy.context.view_layer.update()
    return world_bounds(mesh)


def new_bone(edit_bones, name: str, head: Sequence[float], tail: Sequence[float], parent=None):
    bone = edit_bones.new(name)
    bone.head = v3(head)
    bone.tail = v3(tail)
    if (bone.tail - bone.head).length < 0.02:
        bone.tail = bone.head + Vector((0, 0, 0.05))
    if parent is not None:
        bone.parent = edit_bones.get(parent)
    return bone


def make_humanoid_rig(mesh: bpy.types.Object, name: str, height: float, width: float, depth: float):
    data = bpy.data.armatures.new(name + "_data")
    arm = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(arm)
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    eb = data.edit_bones
    h = max(height, 1.0)
    w = max(width, 1.0)
    d = max(depth, 0.5)
    new_bone(eb, "Hips", (0, 0, h * 0.40), (0, 0, h * 0.48))
    new_bone(eb, "Spine", (0, 0, h * 0.48), (0, 0, h * 0.60), "Hips")
    new_bone(eb, "Spine01", (0, 0, h * 0.60), (0, 0, h * 0.70), "Spine")
    new_bone(eb, "Spine02", (0, 0, h * 0.70), (0, 0, h * 0.78), "Spine01")
    new_bone(eb, "neck", (0, 0, h * 0.78), (0, 0, h * 0.86), "Spine02")
    new_bone(eb, "Head", (0, 0, h * 0.86), (0, 0, h * 0.95), "neck")
    new_bone(eb, "head_end", (0, 0, h * 0.95), (0, 0, h * 0.995), "Head")
    new_bone(eb, "headfront", (0, -d * 0.18, h * 0.90), (0, -d * 0.48, h * 0.90), "Head")
    for side, sign in (("Left", 1.0), ("Right", -1.0)):
        x = sign * w * 0.14
        new_bone(eb, side + "UpLeg", (x, 0, h * 0.40), (x * 1.08, 0, h * 0.20), "Hips")
        new_bone(eb, side + "Leg", (x * 1.08, 0, h * 0.20), (x * 1.10, 0, h * 0.07), side + "UpLeg")
        new_bone(eb, side + "Foot", (x * 1.10, 0, h * 0.07), (x * 1.10, -d * 0.13, h * 0.035), side + "Leg")
        new_bone(eb, side + "ToeBase", (x * 1.10, -d * 0.13, h * 0.035), (x * 1.10, -d * 0.35, h * 0.035), side + "Foot")
        sx = sign * w * 0.12
        new_bone(eb, side + "Shoulder", (sx, 0, h * 0.75), (sign * w * 0.22, -d * 0.02, h * 0.75), "Spine02")
        new_bone(eb, side + "Arm", (sign * w * 0.22, -d * 0.02, h * 0.75), (sign * w * 0.30, -d * 0.16, h * 0.66), side + "Shoulder")
        new_bone(eb, side + "ForeArm", (sign * w * 0.30, -d * 0.16, h * 0.66), (sign * w * 0.33, -d * 0.30, h * 0.61), side + "Arm")
        new_bone(eb, side + "Hand", (sign * w * 0.33, -d * 0.30, h * 0.61), (sign * w * 0.34, -d * 0.40, h * 0.60), side + "ForeArm")
    bpy.ops.object.mode_set(mode="POSE")
    for pose_bone in arm.pose.bones:
        pose_bone.rotation_mode = "XYZ"
    bpy.ops.object.mode_set(mode="OBJECT")
    return arm, {"root": "Hips", "spine": ["Spine", "Spine01", "Spine02"], "head": "Head", "arms": [["LeftShoulder", "LeftArm", "LeftForeArm", "LeftHand"], ["RightShoulder", "RightArm", "RightForeArm", "RightHand"]], "legs": [["LeftUpLeg", "LeftLeg", "LeftFoot"], ["RightUpLeg", "RightLeg", "RightFoot"]]}


def make_creature_rig(mesh: bpy.types.Object, name: str, family: str, height: float, width: float, depth: float):
    data = bpy.data.armatures.new(name + "_data")
    arm = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(arm)
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    eb = data.edit_bones
    h = max(height, 1.0)
    w = max(width, 1.0)
    d = max(depth, 0.5)
    if family == "paleogenetic":
        new_bone(eb, "CreatureRoot", (0, 0, h * 0.28), (0, 0, h * 0.38))
        new_bone(eb, "CreatureSpine", (0, 0, h * 0.38), (0, 0, h * 0.66), "CreatureRoot")
        new_bone(eb, "CreatureNeck", (0, 0, h * 0.66), (0, 0, h * 0.78), "CreatureSpine")
        new_bone(eb, "CreatureHead", (0, 0, h * 0.78), (0, -d * 0.05, h * 0.93), "CreatureNeck")
        for side, sign in (("L", 1.0), ("R", -1.0)):
            x = sign * w * 0.15
            new_bone(eb, f"Leg_{side}", (x, 0, h * 0.30), (x * 1.10, 0, h * 0.10), "CreatureRoot")
            new_bone(eb, f"Foot_{side}", (x * 1.10, 0, h * 0.10), (x * 1.10, -d * 0.22, h * 0.04), f"Leg_{side}")
            for idx, z0 in enumerate((0.66, 0.55), 1):
                root = f"Arm{idx}_{side}_Upper"
                mid = f"Arm{idx}_{side}_Lower"
                tip = f"Arm{idx}_{side}_Tip"
                start_x = sign * w * (0.15 if idx == 1 else 0.11)
                start_z = h * z0
                end_x = sign * w * (0.36 if idx == 1 else 0.42)
                end_z = h * (z0 - 0.12)
                new_bone(eb, root, (start_x, -d * 0.02, start_z), (end_x, -d * 0.12, end_z), "CreatureSpine")
                new_bone(eb, mid, (end_x, -d * 0.12, end_z), (end_x * 1.12, -d * 0.16, end_z - h * 0.14), root)
                new_bone(eb, tip, (end_x * 1.12, -d * 0.16, end_z - h * 0.14), (end_x * 1.18, -d * 0.20, end_z - h * 0.22), mid)
        groups = {"root": "CreatureRoot", "spine": ["CreatureSpine", "CreatureNeck"], "head": "CreatureHead", "arms": [["Arm1_L_Upper", "Arm1_L_Lower", "Arm1_L_Tip"], ["Arm1_R_Upper", "Arm1_R_Lower", "Arm1_R_Tip"], ["Arm2_L_Upper", "Arm2_L_Lower", "Arm2_L_Tip"], ["Arm2_R_Upper", "Arm2_R_Lower", "Arm2_R_Tip"]], "legs": [["Leg_L", "Foot_L"], ["Leg_R", "Foot_R"]]}
    else:
        new_bone(eb, "AbdomenRoot", (0, 0, h * 0.30), (0, 0, h * 0.43))
        new_bone(eb, "Thorax", (0, 0, h * 0.43), (0, 0, h * 0.66), "AbdomenRoot")
        new_bone(eb, "InsectNeck", (0, 0, h * 0.66), (0, 0, h * 0.77), "Thorax")
        new_bone(eb, "InsectHead", (0, -d * 0.04, h * 0.77), (0, -d * 0.08, h * 0.90), "InsectNeck")
        for side, sign in (("L", 1.0), ("R", -1.0)):
            x = sign * w * 0.16
            new_bone(eb, f"Leg_{side}_Upper", (x, 0, h * 0.31), (x * 1.10, 0, h * 0.16), "AbdomenRoot")
            new_bone(eb, f"Leg_{side}_Lower", (x * 1.10, 0, h * 0.16), (x * 1.12, -d * 0.02, h * 0.05), f"Leg_{side}_Upper")
            new_bone(eb, f"Leg_{side}_Foot", (x * 1.12, -d * 0.02, h * 0.05), (x * 1.12, -d * 0.26, h * 0.04), f"Leg_{side}_Lower")
            new_bone(eb, f"PrimaryArm_{side}_Upper", (sign * w * 0.14, -d * 0.01, h * 0.60), (sign * w * 0.28, -d * 0.10, h * 0.48), "Thorax")
            new_bone(eb, f"PrimaryArm_{side}_Lower", (sign * w * 0.28, -d * 0.10, h * 0.48), (sign * w * 0.40, -d * 0.18, h * 0.39), f"PrimaryArm_{side}_Upper")
            new_bone(eb, f"PrimaryArm_{side}_Claw", (sign * w * 0.40, -d * 0.18, h * 0.39), (sign * w * 0.46, -d * 0.21, h * 0.34), f"PrimaryArm_{side}_Lower")
            new_bone(eb, f"ClawArm_{side}_Upper", (sign * w * 0.11, d * 0.01, h * 0.64), (sign * w * 0.25, d * 0.04, h * 0.76), "Thorax")
            new_bone(eb, f"ClawArm_{side}_Lower", (sign * w * 0.25, d * 0.04, h * 0.76), (sign * w * 0.40, d * 0.02, h * 0.83), f"ClawArm_{side}_Upper")
            new_bone(eb, f"ClawArm_{side}_Tip", (sign * w * 0.40, d * 0.02, h * 0.83), (sign * w * 0.46, -d * 0.01, h * 0.86), f"ClawArm_{side}_Lower")
            new_bone(eb, f"Antenna_{side}", (sign * w * 0.04, -d * 0.06, h * 0.87), (sign * w * 0.10, -d * 0.10, h * 1.02), "InsectHead")
        groups = {"root": "AbdomenRoot", "spine": ["Thorax", "InsectNeck"], "head": "InsectHead", "arms": [["PrimaryArm_L_Upper", "PrimaryArm_L_Lower", "PrimaryArm_L_Claw"], ["PrimaryArm_R_Upper", "PrimaryArm_R_Lower", "PrimaryArm_R_Claw"], ["ClawArm_L_Upper", "ClawArm_L_Lower", "ClawArm_L_Tip"], ["ClawArm_R_Upper", "ClawArm_R_Lower", "ClawArm_R_Tip"]], "legs": [["Leg_L_Upper", "Leg_L_Lower", "Leg_L_Foot"], ["Leg_R_Upper", "Leg_R_Lower", "Leg_R_Foot"]]}
    bpy.ops.object.mode_set(mode="POSE")
    for pose_bone in arm.pose.bones:
        pose_bone.rotation_mode = "XYZ"
    bpy.ops.object.mode_set(mode="OBJECT")
    return arm, groups


def segment_distance(point: Vector, head: Vector, tail: Vector) -> float:
    axis = tail - head
    length_sq = axis.length_squared
    if length_sq <= 1e-9:
        return (point - head).length
    t = max(0.0, min(1.0, (point - head).dot(axis) / length_sq))
    return (point - (head + axis * t)).length


def bind_by_nearest(mesh: bpy.types.Object, arm: bpy.types.Object, max_influences: int = 4) -> Dict[str, int]:
    # Provider checkpoints often carry stale vertex groups and an obsolete
    # armature modifier.  Remove those links before binding so the recovered
    # skeleton is the only deformation source and every vertex has a bounded
    # four-bone influence set.
    for modifier in list(mesh.modifiers):
        if modifier.type == "ARMATURE":
            mesh.modifiers.remove(modifier)
    mesh.vertex_groups.clear()
    mesh.parent = arm
    mesh.parent_type = "OBJECT"
    mesh.matrix_parent_inverse = arm.matrix_world.inverted()
    modifier = mesh.modifiers.new("Armature", "ARMATURE")
    modifier.object = arm
    bones = list(arm.data.bones)
    for bone in bones:
        mesh.vertex_groups.new(name=bone.name)
    stats = {"vertices": len(mesh.data.vertices), "influences": max_influences}
    for vertex in mesh.data.vertices:
        point = vertex.co.copy()
        ranked = sorted(
            ((segment_distance(point, bone.head_local, bone.tail_local), bone) for bone in bones),
            key=lambda item: item[0],
        )[:max_influences]
        inv = [1.0 / max(item[0], 0.025) for item in ranked]
        total = sum(inv)
        for weight, (_, bone) in zip(inv, ranked):
            mesh.vertex_groups[bone.name].add([vertex.index], weight / total, "REPLACE")
    return stats


def set_parented_world(obj: bpy.types.Object, arm: bpy.types.Object, bone_name: str, matrix_world: Matrix) -> None:
    obj.parent = arm
    obj.parent_type = "BONE"
    obj.parent_bone = bone_name
    obj.matrix_world = matrix_world


def rifle_contact_targets(mesh: bpy.types.Object) -> Tuple[Vector, Vector]:
    """Return stable trigger and support-hand targets in the normalized body space."""

    w = max(float(mesh.dimensions.x), 1.0)
    h = max(float(mesh.dimensions.z), 1.0)
    d = max(float(mesh.dimensions.y), 0.5)
    # Bring the two hand targets onto a compact ready-to-fire pose in front of
    # the torso. The source rifle then remains at a readable approximately
    # 0.7 scale and its two measured contact points are solved exactly to these
    # targets without adding or reshaping any geometry.
    right = Vector((-w * 0.10, -d * 0.45, h * 0.70))
    left = Vector((w * 0.10, -d * 0.56, h * 0.72))
    return right, left


def append_rifle(arm: bpy.types.Object, mesh: bpy.types.Object, body_material=None) -> Dict[str, str]:
    if not RIFLE_BLEND.exists():
        raise RuntimeError(f"Approved vanilla rifle checkpoint is missing: {RIFLE_BLEND}")
    before = set(bpy.data.objects)
    with bpy.data.libraries.load(str(RIFLE_BLEND), link=False) as (data_from, data_to):
        wanted = [name for name in ("Mesh", "muzzle", "cartridge") if name in data_from.objects]
        data_to.objects = wanted
    appended = [obj for obj in data_to.objects if obj is not None]
    for obj in appended:
        if obj.name not in bpy.context.collection.objects:
            try:
                bpy.context.collection.objects.link(obj)
            except RuntimeError:
                pass
    weapon = next((obj for obj in appended if obj.type == "MESH"), None)
    if weapon is None:
        raise RuntimeError("Vanilla rifle checkpoint did not contain a mesh object")
    weapon.name = "clone_rifle"
    weapon.data = weapon.data.copy()
    # Preserve the approved rifle's own material slots and texture bindings.
    # The checkpoint references the installed vanilla DDS names without a
    # filepath, so bind and pack those existing vanilla images when available.
    # No new texture or geometry is generated by this recovery step.
    if weapon.data.materials:
        rifle_material = weapon.data.materials[0]
        for node in getattr(rifle_material, "node_tree", None).nodes if getattr(rifle_material, "node_tree", None) else []:
            if node.type != "TEX_IMAGE" or node.image is None:
                continue
            source = VANILLA_UNIT_TEXTURES / node.image.name
            if source.exists():
                image = bpy.data.images.load(str(source), check_existing=True)
                image.pack()
                node.image = image
    # Only use the body material when the source attachment has no material at
    # all; replacing a firearm material with clothing made the rifle render as
    # an untextured body-colour bar in the recovery previews.
    if body_material is not None and not weapon.data.materials:
        weapon.data.materials.append(body_material)
    trigger_local = Vector((0.0, 0.30, 0.22))
    support_local = Vector((0.0, -1.45, 0.16))
    right_target, left_target = rifle_contact_targets(mesh)
    source_axis = support_local - trigger_local
    target_axis = left_target - right_target
    if source_axis.length < 0.01 or target_axis.length < 0.01:
        raise RuntimeError("Existing rifle contact points are degenerate")
    scale = target_axis.length / source_axis.length
    weapon_rotation = source_axis.normalized().rotation_difference(target_axis.normalized())
    # Solve the complete source rifle transform from trigger to right hand and
    # foregrip to support hand.  This keeps the original rifle shape intact,
    # while making the hand contact exact in the normalized body space.
    desired = (
        Matrix.Translation(right_target)
        @ weapon_rotation.to_matrix().to_4x4()
        @ Matrix.Scale(scale, 4)
        @ Matrix.Translation(-trigger_local)
    )
    weapon.parent = arm
    weapon.parent_type = "OBJECT"
    weapon.parent_bone = ""
    weapon.matrix_parent_inverse = Matrix.Identity(4)
    weapon.matrix_world = desired
    weapon["chaosx_weapon_attachment"] = "approved_vanilla_rifle; measured_trigger_foregrip_two_hand_solve; two_hand_ik_bake"
    weapon["chaosx_firearm_axis"] = "local_negative_y_to_muzzle"
    names = {"weapon": weapon.name}
    for source_name, role in (("muzzle", "muzzle"), ("cartridge", "cartridge")):
        source = next((obj for obj in appended if obj.name.startswith(source_name)), None)
        if source is not None:
            source.name = role
            local = Vector((0, -3.42908096, 0.28620052)) if role == "muzzle" else Vector((0, -0.10875721, 0.43430269))
            source.parent = weapon
            source.parent_type = "OBJECT"
            source.matrix_parent_inverse = Matrix.Identity(4)
            source.matrix_world = weapon.matrix_world @ Matrix.Translation(local)
            source.empty_display_type = "ARROWS"
            source.empty_display_size = 0.12
            source.hide_render = True
            source["chaosx_locator_role"] = role
            names[role] = source.name
    return names


def attach_rifle_geometry(weapon: bpy.types.Object, body: bpy.types.Object, arm: bpy.types.Object) -> Dict[str, object]:
    """Attach the approved rifle to the skinned body without changing its mesh.

    The rifle is joined into the existing body object only after action baking.
    Every rifle vertex receives a single Spine02 influence, and the idle pose
    delta is removed from the rest-space vertices so the gun stays stable in
    the trigger/support-hand pose while both hands follow it in attack clips.
    """

    locators = {
        obj.name: obj
        for obj in bpy.context.scene.objects
        if obj.name in {"muzzle", "cartridge"}
    }
    locator_world = {name: obj.matrix_world.copy() for name, obj in locators.items()}
    weapon_world = weapon.matrix_world.copy()
    weapon.parent = None
    weapon.matrix_world = weapon_world
    for vertex in weapon.data.vertices:
        vertex.co = weapon.matrix_world @ vertex.co
    weapon.matrix_world = Matrix.Identity(4)
    weapon.parent = None
    weapon.matrix_parent_inverse = Matrix.Identity(4)
    for modifier in list(weapon.modifiers):
        weapon.modifiers.remove(modifier)
    weapon.vertex_groups.clear()
    rifle_vertex_count = len(weapon.data.vertices)
    # A hand bone carries the wrist's aiming rotation, which makes a joined
    # rifle swing vertical when the baked IK wrist turns.  Weight the weapon
    # to the upper-torso control instead: the rifle stays in a stable firing
    # orientation while both hands remain genuinely IK-baked onto its grip
    # and foregrip.  The visible mesh is unchanged; only its existing rifle
    # vertices receive the package's stable weapon-bone influence.
    weapon_bone_name = "Spine02"
    hand_group = weapon.vertex_groups.new(name=weapon_bone_name)
    hand_group.add([vertex.index for vertex in weapon.data.vertices], 1.0, "REPLACE")
    # Make the rest-space gun compensate for the current idle hand pose.
    arm.animation_data_create()
    idle = bpy.data.actions.get(f"{arm.name.removesuffix('_rig')}_idle")
    if idle is not None:
        arm.animation_data.action = idle
    bpy.context.scene.frame_set(0)
    bpy.context.view_layer.update()
    hand = arm.pose.bones.get(weapon_bone_name)
    if hand is None:
        raise RuntimeError(f"{weapon_bone_name} bone is required for rifle attachment")
    rest = hand.bone.matrix_local.copy()
    pose_delta = hand.matrix.copy() @ rest.inverted()
    inverse_delta = pose_delta.inverted()
    for vertex in weapon.data.vertices:
        vertex.co = inverse_delta @ vertex.co
    weapon.data.update()
    # Join only the approved rifle geometry into the existing visible object;
    # no source vertices are generated or replaced.
    bpy.ops.object.select_all(action="DESELECT")
    body.select_set(True)
    weapon.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.join()
    body["chaosx_weapon_attachment"] = "approved_vanilla_rifle_joined; Spine02_weighted; two_hand_ik_baked; idle_pose_compensated"
    body["chaosx_weapon_mesh_source"] = "reimport_vanilla_ENG_weapon_rifle.blend"
    for name, locator in locators.items():
        set_parented_world(locator, arm, weapon_bone_name, locator_world[name])
        locator["chaosx_locator_role"] = name
        locator["chaosx_locator_attachment"] = f"{weapon_bone_name}_bone_parent_after_rifle_join"
    return {
        "joined_into": body.name,
        "rifle_vertices": rifle_vertex_count,
        "locators": sorted(locators),
        "attachment": "armature_modifier_Spine02_single_influence_with_idle_pose_compensation",
    }


def make_target(name: str, arm: bpy.types.Object, location: Vector) -> bpy.types.Object:
    target = bpy.data.objects.new(name, None)
    target.empty_display_type = "SPHERE"
    target.empty_display_size = 0.08
    bpy.context.collection.objects.link(target)
    target.parent = arm
    target.parent_type = "OBJECT"
    target.matrix_parent_inverse = Matrix.Identity(4)
    target.matrix_world = Matrix.Translation(location)
    target.hide_render = True
    return target


def remove_action(action: bpy.types.Action | None) -> None:
    if action is None:
        return
    if action.users:
        action.use_fake_user = False
    if action.users == 0:
        bpy.data.actions.remove(action)


def prune_actions(keep_names: Iterable[str]) -> List[str]:
    """Drop provider/source-only actions from the recovered output.

    The source checkpoints sometimes retain fake-user actions after their
    source armature has been removed.  Keeping those one-frame/provider clips
    makes the exported package look as if it has duplicate or static runtime
    actions.  The recovery output owns only the explicitly authored action
    set, so unreferenced actions are safe to remove here.
    """

    keep = set(keep_names)
    removed: List[str] = []
    for action in list(bpy.data.actions):
        if action.name in keep:
            continue
        action.use_fake_user = False
        if action.users == 0:
            removed.append(action.name)
            bpy.data.actions.remove(action)
    return sorted(removed)


def bake_weapon_actions(
    arm: bpy.types.Object,
    package: str,
    dimensions: Vector,
    weapon: bpy.types.Object | None = None,
) -> List[Dict[str, object]]:
    """Bake genuine two-hand IK actions on the existing humanoid geometry.

    This is the explicit user-authorized manual-recovery exception.  Blender
    evaluates IK constraints, bakes visual bone transforms at every frame, and
    removes the temporary targets/constraints.  It never creates or edits the
    visible mesh.
    """

    h = max(float(dimensions.z), 1.0)
    w = max(float(dimensions.x), 1.0)
    d = max(float(dimensions.y), 0.5)
    if weapon is not None:
        weapon_world = weapon.matrix_world.copy()
        # The approved rifle checkpoint is authored with the trigger/grip
        # around +0.3Y and the forward support contact around -1.45Y.  The
        # transform in append_rifle() maps those measured points to the same
        # normalized hand targets used here.
        right_base = weapon_world @ Vector((0.0, 0.30, 0.22))
        left_base = weapon_world @ Vector((0.0, -1.45, 0.16))
        muzzle_base = weapon_world @ Vector((0.0, -3.42908096, 0.28620052))
    else:
        # Integrated firearms stay part of the approved mesh.  The same two
        # hand pose is still baked so their trigger and support hands animate
        # consistently with the explicit muzzle locator.
        right_base = Vector((-w * 0.07, -d * 0.55, h * 0.68))
        left_base = Vector((w * 0.05, -d * 0.56, h * 0.68))
        muzzle_base = Vector((-w * 0.20, -d * 0.70, h * 0.77))
    fire_direction = (muzzle_base - right_base).normalized()
    records: List[Dict[str, object]] = []
    for role in ("idle", "attack", "defend", "support_attack", "retreat"):
        old = bpy.data.actions.get(f"{package}_{role}")
        arm.animation_data_create()
        arm.animation_data.action = None
        for pose_bone in arm.pose.bones:
            pose_bone.matrix_basis = Matrix.Identity(4)
        if role in ("attack", "support_attack"):
            frames = list(range(0, 49 if role == "attack" else 37, 4))
            frames.append(48 if role == "attack" else 36)
        else:
            frames = list(range(0, 49, 4))
            frames.append(48)
        right_target = make_target(f"{package}_ik_right", arm, right_base)
        left_target = make_target(f"{package}_ik_left", arm, left_base)
        for target in (right_target, left_target):
            target.animation_data_create()
        constraints = []
        for forearm_name, target in (("RightForeArm", right_target), ("LeftForeArm", left_target)):
            forearm = arm.pose.bones.get(forearm_name)
            if forearm is None:
                continue
            constraint = forearm.constraints.new("IK")
            constraint.name = f"CHAOSX_{package}_{forearm_name}_IK"
            constraint.target = target
            constraint.chain_count = 2
            constraints.append(constraint)
        for frame in frames:
            t = frame / max(frames[-1], 1)
            phase = t * math.tau
            recoil_phase = 0.0
            if role in ("attack", "support_attack"):
                if t < 0.30:
                    aim = t / 0.30
                elif t < 0.48:
                    aim = 1.0
                elif t < 0.62:
                    aim = 0.65
                else:
                    aim = max(0.0, 1.0 - (t - 0.62) / 0.38)
                recoil_phase = max(0.0, 1.0 - abs(t - 0.52) / 0.10)
            else:
                aim = 1.0
            sway = Vector((0.0, math.sin(phase) * d * 0.025, math.sin(phase * 0.5) * h * 0.008))
            recoil = -fire_direction * (0.09 * recoil_phase)
            crouch = Vector((0.0, 0.0, -h * 0.015 * aim)) if role == "retreat" else Vector()
            right_target.location = right_base + sway + recoil + crouch
            left_target.location = left_base + sway * 0.75 + recoil * 0.8 + crouch
            right_target.keyframe_insert(data_path="location", frame=frame)
            left_target.keyframe_insert(data_path="location", frame=frame)
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
        bpy.context.view_layer.objects.active = arm
        bpy.ops.object.select_all(action="DESELECT")
        arm.select_set(True)
        bpy.context.view_layer.objects.active = arm
        bpy.ops.nla.bake(
            frame_start=frames[0],
            frame_end=frames[-1],
            step=1,
            only_selected=False,
            visual_keying=True,
            clear_constraints=True,
            use_current_action=False,
            bake_types={"POSE"},
        )
        baked = arm.animation_data.action
        if baked is None:
            raise RuntimeError(f"IK bake produced no action for {package}_{role}")
        baked.name = f"{package}_{role}"
        # Blender's layered-action bake can leave the action range at 0 even
        # when the channelbag contains the full keyed pose.  Persist the
        # authored range explicitly so the runtime and adapter evaluate every
        # firing/ready phase instead of treating the clip as a one-frame pose.
        baked.frame_start = frames[0]
        baked.frame_end = frames[-1]
        baked.use_fake_user = True
        baked["chaosx_semantic_role"] = role
        baked["chaosx_genuine_skeletal"] = True
        baked["chaosx_manual_user_authorized"] = True
        baked["chaosx_ik_baked"] = True
        baked["chaosx_firing_action"] = role in ("attack", "support_attack")
        if role in ("attack", "support_attack"):
            baked["chaosx_aim_start_frame"] = 0
            baked["chaosx_discharge_frame"] = 25 if role == "attack" else 19
            baked["chaosx_recovery_start_frame"] = 30 if role == "attack" else 23
        # NLA bake also emits constant local-scale channels.  Scale is not a
        # firearm animation signal and can make the PDX action look like a
        # transform-only clip, so remove those channels before export.
        for layer in getattr(baked, "layers", []):
            for strip in getattr(layer, "strips", []):
                for channelbag in getattr(strip, "channelbags", []):
                    for fcurve in list(getattr(channelbag, "fcurves", [])):
                        if ".scale" in fcurve.data_path:
                            channelbag.fcurves.remove(fcurve)
        remove_action(old)
        for target in (right_target, left_target):
            target.animation_data_clear()
            bpy.data.objects.remove(target, do_unlink=True)
        records.append(
            {
                "name": baked.name,
                "role": role,
                "frames": len(frames),
                "frame_start": frames[0],
                "frame_end": frames[-1],
                "firing": role in ("attack", "support_attack"),
                "discharge_frame": 25 if role == "attack" else 19 if role == "support_attack" else None,
                "method": "blender_visual_ik_bake_existing_mesh_user_authorized",
            }
        )
    return records


def add_locator(arm: bpy.types.Object, name: str, bone_name: str, location: Vector, role: str) -> str:
    locator = bpy.data.objects.new(name, None)
    locator.empty_display_type = "ARROWS"
    locator.empty_display_size = 0.14
    bpy.context.collection.objects.link(locator)
    set_parented_world(locator, arm, bone_name, Matrix.Translation(location))
    locator["chaosx_locator_role"] = role
    return locator.name


def clear_action(arm: bpy.types.Object) -> None:
    if arm.animation_data:
        arm.animation_data.action = None


def evaluated_minimum_z(mesh: bpy.types.Object) -> float:
    """Return the evaluated skinned mesh's lowest world-space point."""

    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated = mesh.evaluated_get(depsgraph)
    evaluated_mesh = evaluated.to_mesh()
    try:
        if not evaluated_mesh.vertices:
            return 0.0
        return min((evaluated.matrix_world @ vertex.co).z for vertex in evaluated_mesh.vertices)
    finally:
        evaluated.to_mesh_clear()


def ground_action(arm: bpy.types.Object, mesh: bpy.types.Object, action_name: str, root_name: str) -> Dict[str, object]:
    """Ground one authored clip without replacing its skeletal motion.

    This is a bounded manual contact correction: body rotations and limb
    motion remain untouched, while each sampled frame receives the smallest
    root-Z offset needed to keep the evaluated mesh on the floor.  Applying it
    to every authored role prevents source-pose-dependent hovering or floor
    penetration in idle, combat, movement, creature, and death clips alike.
    """

    action = bpy.data.actions.get(action_name)
    root = arm.pose.bones.get(root_name)
    if action is None or root is None:
        return {"status": "skipped", "reason": "missing_action_or_root"}
    arm.animation_data_create()
    arm.animation_data.action = action
    start = int(round(action.frame_start))
    end = int(round(action.frame_end))
    # Capture the uncorrected root pose first. Mutating the action while
    # sampling it would make later frames accumulate the prior correction and
    # can leave the final collapse hovering above the ground. The correction
    # is applied as a world-Z translation to the root pose matrix rather than
    # by adding to root.location.z, because the collapsing root rotates and its
    # local Z axis is no longer the world vertical.
    samples = []
    for frame in range(start, end + 1):
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        samples.append((frame, root.matrix.copy(), evaluated_minimum_z(mesh)))
    offsets = []
    for frame, base_root_matrix, minimum in samples:
        # Restore the sampled frame before assigning the corrected pose.  The
        # root matrix is evaluated in the current pose context; applying every
        # sample while the scene remains on the final frame causes Blender to
        # key the right numeric channel against the wrong dependency graph pose.
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        offset = -minimum
        root.matrix = Matrix.Translation(Vector((0.0, 0.0, offset))) @ base_root_matrix
        root.keyframe_insert(data_path="location", frame=frame, group=root.name)
        offsets.append(offset)
    bpy.context.view_layer.update()
    action["chaosx_grounded_root_contact"] = True
    action["chaosx_grounding_method"] = "manual_evaluated_mesh_root_z_contact"
    action["chaosx_grounding_minimum_offset"] = float(min(offsets) if offsets else 0.0)
    action["chaosx_grounding_maximum_offset"] = float(max(offsets) if offsets else 0.0)
    return {
        "status": "grounded",
        "action": action_name,
        "root": root_name,
        "frames": end - start + 1,
        "minimum_root_offset": round(min(offsets) if offsets else 0.0, 6),
        "maximum_root_offset": round(max(offsets) if offsets else 0.0, 6),
    }


def ground_death_action(arm: bpy.types.Object, mesh: bpy.types.Object, action_name: str, root_name: str) -> Dict[str, object]:
    """Compatibility wrapper retaining the explicit death-contact entry point."""

    return ground_action(arm, mesh, action_name, root_name)


def keyframe_pose_bone(pose_bone, frame: int, rotation=(0.0, 0.0, 0.0), location=None):
    pose_bone.rotation_mode = "XYZ"
    pose_bone.rotation_euler = rotation
    pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame, group=pose_bone.name)
    if location is not None:
        pose_bone.location = location
        pose_bone.keyframe_insert(data_path="location", frame=frame, group=pose_bone.name)


def action_for(arm: bpy.types.Object, name: str, frame_values: Sequence[int], groups: Dict, role: str, firing: bool = False):
    clear_action(arm)
    action = bpy.data.actions.new(name)
    action.use_fake_user = True
    action["chaosx_semantic_role"] = role
    action["chaosx_genuine_skeletal"] = True
    action["chaosx_manual_user_authorized"] = True
    action["chaosx_firing_action"] = bool(firing)
    if firing:
        action["chaosx_aim_start_frame"] = 0
        action["chaosx_discharge_frame"] = 25 if role == "attack" else 19
        action["chaosx_recovery_start_frame"] = 30 if role == "attack" else 23
    arm.animation_data_create()
    arm.animation_data.action = action
    pose = arm.pose.bones
    arm.data.pose_position = "POSE"
    # Derive a bounded height from the authored armature for grounded death
    # translation; this keeps the helper independent of any source mesh.
    bone_points = [point.z for bone in arm.data.bones for point in (bone.head_local, bone.tail_local)]
    h = max(max(bone_points) - min(bone_points), 1.0) if bone_points else 1.0
    arms = groups.get("arms", [])
    legs = groups.get("legs", [])
    spine = groups.get("spine", [])
    root = groups.get("root")
    head = groups.get("head")
    for idx, frame in enumerate(frame_values):
        t = idx / max(1, len(frame_values) - 1)
        phase = t * math.tau
        # Reset every known bone explicitly so each clip is self-contained.
        for bone in pose:
            keyframe_pose_bone(bone, frame)
        if role == "idle" and len(arms) == 2:
            # Most source checkpoints are neutral T/A poses.  Keep the mesh
            # in the authored rest pose, but settle humanoid shoulders into a
            # readable ready stance for the idle clip.  The sign follows the
            # mirrored shoulder bone so both arms rotate downward together.
            for arm_index, chain in enumerate(arms):
                if chain:
                    side = 1.0 if arm_index == 0 else -1.0
                    keyframe_pose_bone(pose[chain[0]], frame, (0.0, 0.48 * side, 0.0))
                    if len(chain) > 1:
                        keyframe_pose_bone(pose[chain[1]], frame, (0.10, 0.0, 0.0))
                    if len(chain) > 2:
                        keyframe_pose_bone(pose[chain[2]], frame, (0.18, 0.0, 0.0))
            # Add a restrained breathing/attention loop to every idle rig,
            # including the non-humanoid families that do not use the firearm
            # IK path.  This keeps idle a genuine keyed skeletal action rather
            # than a static hold while preserving the approved source pose.
            breath = math.sin(phase) * 0.025
            if spine:
                keyframe_pose_bone(pose[spine[-1]], frame, (breath, 0.0, 0.0))
            if head:
                keyframe_pose_bone(pose[head], frame, (0.0, breath * 0.75, 0.0))
        elif role == "idle":
            # Creature silhouettes use a smaller pulse across the primary
            # appendages so their idle clips remain visibly skeletal without
            # flattening the authored anatomy.
            breath = math.sin(phase) * 0.035
            if spine:
                keyframe_pose_bone(pose[spine[-1]], frame, (breath, 0.0, 0.0))
            if head:
                keyframe_pose_bone(pose[head], frame, (0.0, breath * 0.6, 0.0))
            for arm_index, chain in enumerate(arms):
                if chain:
                    offset = 0.35 * arm_index
                    keyframe_pose_bone(pose[chain[0]], frame, (breath * math.cos(offset), 0.0, breath * math.sin(offset)))
        elif role in ("move", "retreat", "crawl"):
            sign = -1.0 if role == "retreat" else 1.0
            for leg_index, chain in enumerate(legs):
                if chain:
                    bend = math.sin(phase + (0 if leg_index == 0 else math.pi)) * 0.20 * sign
                    keyframe_pose_bone(pose[chain[0]], frame, (bend, 0.0, 0.0))
                    if len(chain) > 1:
                        keyframe_pose_bone(pose[chain[1]], frame, (-abs(bend) * 0.55, 0.0, 0.0))
            for arm_index, chain in enumerate(arms):
                if chain:
                    sway = math.sin(phase + arm_index * 0.5) * 0.12
                    keyframe_pose_bone(pose[chain[0]], frame, (sway, 0.0, 0.0))
            if role == "crawl" and root:
                keyframe_pose_bone(pose[root], frame, (0.12 * math.sin(phase), 0.0, 0.0))
        elif role in ("attack", "support_attack", "laser_attack", "ranged_strike"):
            # Aiming, discharge, recoil, and recovery are separate keyed phases.
            if t < 0.30:
                aim = t / 0.30
            elif t < 0.48:
                aim = 1.0
            elif t < 0.62:
                aim = 0.65
            else:
                aim = max(0.0, 1.0 - (t - 0.62) / 0.38)
            for arm_index, chain in enumerate(arms):
                if chain:
                    handed = -1.0 if arm_index % 2 else 1.0
                    keyframe_pose_bone(pose[chain[0]], frame, (-0.18 * aim, 0.04 * handed * aim, 0.05 * handed * aim))
                    if len(chain) > 1:
                        keyframe_pose_bone(pose[chain[1]], frame, (-0.38 * aim, 0.0, -0.04 * handed * aim))
                    if len(chain) > 2:
                        keyframe_pose_bone(pose[chain[2]], frame, (-0.28 * aim, 0.0, 0.0))
            if spine:
                keyframe_pose_bone(pose[spine[-1]], frame, (-0.10 * aim, 0.0, 0.0))
        elif role in ("defend", "training", "wounded", "stalk"):
            guard = 0.18 + 0.06 * math.sin(phase)
            for arm_index, chain in enumerate(arms):
                if chain:
                    side = -1 if arm_index % 2 else 1
                    keyframe_pose_bone(pose[chain[0]], frame, (-guard, 0.02 * side, 0.08 * side))
                    if len(chain) > 1:
                        keyframe_pose_bone(pose[chain[1]], frame, (-0.20, 0.0, 0.0))
        elif role in ("portal_arrival", "arrival", "roar", "charge", "leap", "entrain", "temporal_anchor", "synchronization"):
            pulse = math.sin(math.pi * t)
            if root:
                keyframe_pose_bone(pose[root], frame, (0.0, 0.0, 0.10 * pulse), (0.0, 0.0, 0.12 * pulse))
            for chain in arms:
                if chain:
                    keyframe_pose_bone(pose[chain[0]], frame, (-0.30 * pulse, 0.0, 0.0))
            if head:
                keyframe_pose_bone(pose[head], frame, (0.0, 0.12 * pulse, 0.0))
        elif role in ("death", "collapse"):
            fall = max(0.0, (t - 0.15) / 0.85)
            if root:
                # Finish as a grounded collapse rather than an airborne
                # ragdoll.  The fall remains a real keyed skeletal action;
                # the vertical drop is deliberately conservative and is
                # subsequently eligible for the adapter's contact check.
                drop = h * (0.24 if len(arms) == 2 else 0.16)
                keyframe_pose_bone(pose[root], frame, (0.95 * fall, 0.0, 0.0), (0.0, 0.12 * fall, -drop * fall))
            if spine:
                for bone_name in spine:
                    keyframe_pose_bone(pose[bone_name], frame, (0.45 * fall, 0.0, 0.0))
            for chain in arms:
                if chain:
                    side = -1 if arms.index(chain) % 2 else 1
                    keyframe_pose_bone(pose[chain[0]], frame, (0.65 * fall, 0.18 * side * fall, 0.20 * side * fall))
            for chain in legs:
                if chain:
                    keyframe_pose_bone(pose[chain[0]], frame, (-0.22 * fall, 0.0, 0.0))
        action.frame_start = frame_values[0]
        action.frame_end = frame_values[-1]
    # Use smooth interpolation without collapsing any keyed bone motion.
    for fcurve in getattr(action, "fcurves", []):
        for key in fcurve.keyframe_points:
            key.interpolation = "BEZIER"
    return action


def package_config(package: str):
    configs = {
        "portal_raider": {
            "source": ROOT / "docs/assets/shared_portal_raider_system/models_3d/portal_raider/blender/checkpoints/03_rig_approved.blend",
            "mesh": "Mesh_0.001", "runtime_mesh": "char1.004", "armature": "portal_raider_rig", "kind": "humanoid", "attach_rifle": False,
            "actions": ["idle", "move", "attack", "defend", "support_attack", "retreat", "portal_arrival", "wounded", "death"],
        },
        "clone_infantry": {
            "source": ROOT / "docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/03_rig_approved.blend",
            "mesh": "Mesh_0.001", "runtime_mesh": "Mesh_0.002", "armature": "clone_infantry_rig", "kind": "humanoid", "attach_rifle": True,
            "actions": ["idle", "move", "attack", "defend", "support_attack", "retreat", "training", "wounded", "death"],
        },
        "autonomous_robot": {
            "source": ROOT / "docs/assets/shared_robot_system/models_3d/autonomous_robot/blender/checkpoints/03_rig_approved.blend",
            "mesh": "char1.001", "runtime_mesh": "char1.003", "armature": "autonomous_robot_rig", "kind": "humanoid", "attach_rifle": False,
            "actions": ["idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"],
        },
        "alien_infantry": {
            "source": ROOT / "docs/assets/016_brilliant_scientist/models_3d/alien_infantry/blender/checkpoints/reimport_v13_firearm_preset_idle_final.blend",
            "mesh": "char1.002", "runtime_mesh": "char1.002", "armature": "alien_infantry_rig", "kind": "humanoid", "attach_rifle": False,
            "actions": ["idle", "move", "attack", "defend", "support_attack", "retreat", "death"],
        },
        "temporal_guard": {
            "source": ROOT / "docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/blender/checkpoints/03_rig_approved.blend",
            "mesh": "char1.001", "runtime_mesh": "char1.004", "armature": "temporal_guard_rig", "kind": "humanoid", "attach_rifle": False,
            "actions": ["idle", "move", "attack", "defend", "entrain", "death", "temporal_anchor", "synchronization"],
        },
        "paleogenetic_creature": {
            "source": ROOT / "docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/blender/checkpoints/02b_segmented_creature.blend",
            "mesh": "paleogenetic_component_000", "runtime_mesh": "paleogenetic_component_000", "armature": "paleogenetic_creature_rig", "kind": "paleogenetic", "actions": ["idle", "stalk", "move", "charge", "attack", "defend", "support_attack", "retreat", "roar", "wounded", "death"],
        },
        "xenobiological_assault_organism": {
            "source": ROOT / "docs/assets/chaos_redux_3d_model_pilots/models_3d/xenobiological_assault_organism/blender/checkpoints/04_unrigged_segmented_geometry.blend",
            "mesh": "xenobiological_component_000", "runtime_mesh": "xenobiological_component_000", "armature": "xenobiological_assault_rig", "kind": "xenobiological", "actions": ["idle", "crawl", "move", "attack", "defend", "leap", "wounded", "death"],
        },
    }
    if package not in configs:
        raise RuntimeError(f"Unknown package {package}")
    return configs[package]


def process(package: str, output: Path) -> Dict:
    cfg = package_config(package)
    if not cfg["source"].exists():
        raise RuntimeError(f"Checkpoint missing: {cfg['source']}")
    bpy.ops.wm.open_mainfile(filepath=str(cfg["source"]))
    mesh = selected_mesh(cfg["mesh"])
    pre_rotation = Matrix.Rotation(cfg.get("rotate_x", 0.0), 4, "X") if cfg.get("rotate_x") else None
    bake_object_world_transform(mesh, pre_rotation)
    clear_scene_except(mesh)
    mesh.name = cfg["runtime_mesh"]
    minimum, maximum = normalize_ground(mesh)
    dimensions = maximum - minimum
    if cfg["kind"] == "humanoid":
        arm, groups = make_humanoid_rig(mesh, cfg["armature"], dimensions.z, dimensions.x, dimensions.y)
    else:
        family = "paleogenetic" if cfg["kind"] == "paleogenetic" else "xenobiological"
        arm, groups = make_creature_rig(mesh, cfg["armature"], family, dimensions.z, dimensions.x, dimensions.y)
    weight_stats = bind_by_nearest(mesh, arm)
    # Mark the recovered pair as the adapter's explicit working scope.  This
    # is required by export and contact-correction passes and prevents source
    # or helper objects from being selected accidentally.
    arm["chaosx_working"] = True
    mesh["chaosx_working"] = True
    locator_names = {}
    weapon = None
    if cfg.get("attach_rifle"):
        material = mesh.data.materials[0] if mesh.data.materials else None
        locator_names.update(append_rifle(arm, mesh, material))
        weapon = bpy.data.objects.get(locator_names.get("weapon"))
    elif package in ("portal_raider", "alien_infantry", "autonomous_robot"):
        y = -max(dimensions.y * 0.60, 0.35)
        x = -dimensions.x * 0.22
        z = dimensions.z * (0.66 if package != "alien_infantry" else 0.78)
        locator_names["muzzle"] = add_locator(arm, "muzzle", "RightHand", Vector((x, y, z)), "muzzle")
        if package == "autonomous_robot":
            locator_names["muzzle_left"] = add_locator(arm, "muzzle_left", "LeftHand", Vector((-x, y, z)), "muzzle")
    actions = []
    firearm_roles = {"idle", "attack", "defend", "support_attack", "retreat"}
    for role in cfg["actions"]:
        if cfg["kind"] == "humanoid" and package in ("portal_raider", "clone_infantry", "autonomous_robot", "alien_infantry") and role in firearm_roles:
            continue
        action_name = f"{package}_{role}"
        firing = role in ("attack", "support_attack", "laser_attack", "ranged_strike") and package in ("portal_raider", "clone_infantry", "autonomous_robot", "alien_infantry")
        if role in ("attack", "support_attack", "laser_attack", "ranged_strike"):
            frames = list(range(0, 49 if role == "attack" else 37, 4))
            if frames[-1] != (48 if role == "attack" else 36):
                frames.append(48 if role == "attack" else 36)
        elif role == "death":
            frames = list(range(0, 49, 4))
        else:
            frames = list(range(0, 49, 8))
        action = action_for(arm, action_name, frames, groups, role, firing)
        actions.append({"name": action.name, "role": role, "frames": len(frames), "frame_start": frames[0], "frame_end": frames[-1], "firing": firing})
    attachment = None
    if cfg["kind"] == "humanoid" and package in ("portal_raider", "clone_infantry", "autonomous_robot", "alien_infantry"):
        actions = bake_weapon_actions(arm, package, dimensions, weapon) + actions
        if weapon is not None:
            attachment = attach_rifle_geometry(weapon, mesh, arm)
    death_root = groups.get("root")
    grounding_all = {}
    if death_root:
        for action_record in actions:
            grounding_all[action_record["name"]] = ground_action(
                arm,
                mesh,
                action_record["name"],
                death_root,
            )
    else:
        grounding_all = {action_record["name"]: {"status": "skipped", "reason": "no_root"} for action_record in actions}
    grounding = grounding_all.get(
        f"{package}_death",
        {"status": "skipped", "reason": "missing_death_action"},
    )
    # Leave the neutral idle action active for scene inspection.  Remove any
    # stale provider actions that survived the source checkpoint load; only
    # this explicitly authored set is part of the recovered runtime package.
    removed_actions = prune_actions(record["name"] for record in actions)
    arm.animation_data.action = bpy.data.actions.get(f"{package}_idle")
    bpy.context.view_layer.objects.active = arm
    arm.select_set(True)
    mesh.select_set(False)
    output.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(output))
    result = {
        "package": package,
        "source": str(cfg["source"]),
        "output": str(output),
        "mesh": mesh.name,
        "mesh_dimensions": [round(value, 6) for value in dimensions],
        "armature": arm.name,
        "bones": [bone.name for bone in arm.data.bones],
        "weight_stats": weight_stats,
        "locators": locator_names,
        "attachment": attachment,
        "grounding": grounding,
        "grounding_all": grounding_all,
        "actions": actions,
        "removed_source_actions": removed_actions,
        "manual_authorization": "user_authorized_existing_mesh_rig_and_action_recovery_2026-08-27",
        "geometry_regenerated": False,
    }
    report = output.with_suffix(".recovery.json")
    report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--output", required=True)
    argv = os.sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1 :]
    args = parser.parse_args(argv)
    result = process(args.package, Path(args.output).resolve())
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
