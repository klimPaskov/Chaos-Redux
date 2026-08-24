"""Synthetic Blender proof for scale-aware hierarchy animation retargeting."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import tempfile
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


BONES = ("Root", "Spine", "Chest", "Head", "Arm", "Accessory")


def reset_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)


def make_rig(name: str, bone_length: float, world_scale: float) -> bpy.types.Object:
    data = bpy.data.armatures.new(f"{name}Data")
    rig = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    parent = None
    for index, bone_name in enumerate(BONES):
        bone = data.edit_bones.new(bone_name)
        bone.head = (0.0, 0.0, bone_length * index)
        bone.tail = (0.0, 0.0, bone_length * (index + 1))
        bone.parent = parent
        parent = bone
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.scale = (world_scale,) * 3
    return rig


def make_source(path: Path) -> tuple[str, str]:
    reset_scene()
    rig = make_rig("SourceRig", 1.0, 1.0)
    action = bpy.data.actions.new("VerifiedSource")
    rig.animation_data_create()
    rig.animation_data.action = action
    for frame, root_z, chest_angle in ((1, 0.0, 0.0), (8, 0.2, 0.35), (16, 0.0, 0.0)):
        for bone_name in BONES:
            bone = rig.pose.bones[bone_name]
            bone.rotation_mode = "QUATERNION"
            angle = chest_angle if bone_name == "Chest" else 0.0
            bone.rotation_quaternion = (math.cos(angle / 2), math.sin(angle / 2), 0.0, 0.0)
            bone.keyframe_insert("rotation_quaternion", frame=frame, group=bone_name)
        root = rig.pose.bones["Root"]
        root.location = (0.0, 0.0, root_z)
        root.keyframe_insert("location", frame=frame, group="Root")
    bpy.ops.wm.save_as_mainfile(filepath=str(path))
    digest = hashlib.sha256(path.read_bytes()).hexdigest().upper()
    return action.name, digest


def make_target(path: Path) -> None:
    reset_scene()
    rig = make_rig("TargetRig", 100.0, 0.01)
    rig["chaosx_working"] = True
    mesh = bpy.data.meshes.new("TargetMeshData")
    mesh.from_pydata(
        [(-0.2, 0.0, 0.0), (0.2, 0.0, 0.0), (0.0, 0.0, 500.0)],
        [(0, 1), (1, 2), (2, 0)],
        [(0, 1, 2)],
    )
    body = bpy.data.objects.new("TargetMesh", mesh)
    bpy.context.scene.collection.objects.link(body)
    body.parent = rig
    body["chaosx_working"] = True
    modifier = body.modifiers.new("TargetRig", "ARMATURE")
    modifier.object = rig
    group = body.vertex_groups.new(name="Chest")
    group.add([0, 1, 2], 1.0, "REPLACE")
    accessory_mesh = bpy.data.meshes.new("AccessoryData")
    accessory_mesh.from_pydata([(0.0, 0.0, 0.0), (20.0, 0.0, 0.0), (0.0, 5.0, 0.0)], [], [(0, 1, 2)])
    accessory = bpy.data.objects.new("Accessory", accessory_mesh)
    bpy.context.scene.collection.objects.link(accessory)
    accessory.parent = rig
    accessory.parent_type = "BONE"
    accessory.parent_bone = "Accessory"
    accessory["chaosx_bone_parented_accessory"] = True
    bpy.ops.wm.save_as_mainfile(filepath=str(path))


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chaosx_scale_retarget_") as temporary:
        job = Path(temporary)
        (job / "blender" / "reports").mkdir(parents=True)
        source = job / "source.blend"
        target = job / "target.blend"
        output = job / "output.blend"
        provenance = job / "provenance.json"
        source_action, digest = make_source(source)
        make_target(target)
        provenance.write_text(
            json.dumps(
                {
                    "verification_status": "verified",
                    "source_kind": "professional_source",
                    "source_reference_id": "synthetic-regression",
                    "source_action_name": source_action,
                    "source_sha256": digest,
                }
            ),
            encoding="utf-8",
        )
        result = blender_worker.import_animation_action(
            {
                "job_root": str(job),
                "payload": {
                    "blend_rel": target.name,
                    "source_rel": source.name,
                    "provenance_rel": provenance.name,
                    "checkpoint_rel": output.name,
                    "source_action_name": source_action,
                    "target_armature_name": "TargetRig",
                    "target_action_name": "Retargeted",
                    "source_kind": "professional_source",
                    "source_reference_id": "synthetic-regression",
                    "source_sha256": digest,
                    "bone_chains": {name: [name] for name in BONES},
                    "promote_audited_target": False,
                },
            }
        )
        assert math.isclose(result["data_length_ratio"], 100.0, abs_tol=1e-4)
        assert all(
            math.isclose(component, 1.0, abs_tol=1e-8)
            for component in result["source_armature_world_scale"]
        )
        assert math.isclose(result["location_scale"], 1.0, abs_tol=1e-4)
        assert math.isclose(
            blender_worker.scale_aware_retarget_location_scale(
                100.0,
                blender_worker.Vector((0.5, 0.5, 0.5)),
                blender_worker.Vector((0.01, 0.01, 0.01)),
            ),
            2.0,
            abs_tol=1e-6,
        )
        assert all(
            math.isclose(component, 0.01, abs_tol=1e-8)
            for component in result["target_armature_world_scale"]
        )
        assert result["source_target_motion_crosscheck"]["target_motion_peak"] < 2.0
        bpy.ops.wm.open_mainfile(filepath=str(output))
        rig = bpy.data.objects["TargetRig"]
        action = bpy.data.actions["Retargeted"]
        rig.animation_data.action = action
        root_peak = 0.0
        bounds = []
        for frame in (1, 8, 16):
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            root_peak = max(root_peak, abs(float(rig.pose.bones["Root"].location.z)))
            bounds.append(blender_worker.world_bounds([bpy.data.objects["TargetMesh"]]))
        assert root_peak <= 0.21
        assert max(float(maximum.z - minimum.z) for minimum, maximum in bounds) < 6.0
        accessory = bpy.data.objects["Accessory"]
        assert accessory.parent is rig
        assert accessory.parent_type == "BONE"
        assert accessory.parent_bone == "Accessory"
        assert bool(accessory["chaosx_bone_parented_accessory"])
        assert len(rig.data.bones["Accessory"].parent_recursive) == 5
        print(json.dumps({"status": "pass", "location_scale": round(result["location_scale"], 6)}, sort_keys=True))


if __name__ == "__main__":
    main()
