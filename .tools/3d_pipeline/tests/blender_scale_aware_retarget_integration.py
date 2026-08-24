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
    rig = make_rig("SourceRig", 1.0, 0.01)
    action = bpy.data.actions.new("VerifiedSource")
    rig.animation_data_create()
    rig.animation_data.action = action
    for frame, root_z, chest_angle in ((1, 0.0, 0.0), (8, 140.0, 0.35), (16, 0.0, 0.0)):
        for bone_name in BONES:
            bone = rig.pose.bones[bone_name]
            bone.rotation_mode = "QUATERNION"
            angle = chest_angle if bone_name == "Chest" else 0.0
            bone.rotation_quaternion = (math.cos(angle / 2), math.sin(angle / 2), 0.0, 0.0)
            bone.keyframe_insert("rotation_quaternion", frame=frame, group=bone_name)
        root = rig.pose.bones["Root"]
        root.location = (0.0, 0.0, root_z)
        root.keyframe_insert("location", frame=frame, group="Root")
    bpy.ops.object.select_all(action="DESELECT")
    rig.select_set(True)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"ARMATURE"},
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        add_leaf_bones=False,
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        bake_anim_force_startend_keying=True,
        bake_anim_simplify_factor=0.0,
    )
    digest = hashlib.sha256(path.read_bytes()).hexdigest().upper()
    return "SourceRig|Scene", digest


def make_target(path: Path) -> None:
    reset_scene()
    rig = make_rig("TargetRig", 100.0, 0.02722898125)
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
        source = job / "source.fbx"
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
            math.isclose(component, 0.01, abs_tol=1e-8)
            for component in result["source_armature_world_scale"]
        )
        assert math.isclose(result["location_scale"], 0.3672563849, abs_tol=1e-6)
        assert result["rest_data_length_ratio_applied_to_location"] is False
        assert result["location_coordinate_space"] == "pose_bone_matrix_basis_translation"
        assert all(
            math.isclose(component, 0.02722898125, abs_tol=1e-8)
            for component in result["target_armature_world_scale"]
        )
        assert result["source_target_motion_crosscheck"]["target_motion_peak"] < 52.0
        bpy.ops.wm.open_mainfile(filepath=str(output))
        rig = bpy.data.objects["TargetRig"]
        action = bpy.data.actions["Retargeted"]
        rig.animation_data.action = action
        root_peak = 0.0
        bounds = []
        for frame in range(result["frame_start"], result["frame_end"] + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            root_peak = max(root_peak, abs(float(rig.pose.bones["Root"].location.z)))
            bounds.append(blender_worker.world_bounds([bpy.data.objects["TargetMesh"]]))
        assert root_peak <= 51.42
        assert max(float(maximum.z - minimum.z) for minimum, maximum in bounds) < 15.0
        source_world_peak = (
            result["root_cleanup"]["source_root_z_delta_peak"]
            * result["source_armature_world_scale"][2]
        )
        target_world_peak = root_peak * result["target_armature_world_scale"][2]
        assert math.isclose(source_world_peak, target_world_peak, abs_tol=1e-5), (
            source_world_peak,
            target_world_peak,
            root_peak,
            result["root_cleanup"],
        )
        accessory = bpy.data.objects["Accessory"]
        assert accessory.parent is rig
        assert accessory.parent_type == "BONE"
        assert accessory.parent_bone == "Accessory"
        assert bool(accessory["chaosx_bone_parented_accessory"])
        assert len(rig.data.bones["Accessory"].parent_recursive) == 5

        before_export_bounds = blender_worker.world_bounds([bpy.data.objects["TargetMesh"]])
        export_transforms = blender_worker.prepare_pdx_export_transforms()
        assert math.isclose(
            export_transforms["armature_data_scale_factor"],
            result["target_armature_world_scale"][2],
            abs_tol=1e-8,
        )
        assert all(math.isclose(component, 1.0, abs_tol=1e-8) for component in rig.matrix_world.to_scale())
        baked_root_peak = 0.0
        for frame in range(result["frame_start"], result["frame_end"] + 1):
            bpy.context.scene.frame_set(frame)
            bpy.context.view_layer.update()
            baked_root_peak = max(baked_root_peak, abs(float(rig.pose.bones["Root"].location.z)))
        assert math.isclose(baked_root_peak, target_world_peak, abs_tol=1e-5)
        after_export_bounds = blender_worker.world_bounds([bpy.data.objects["TargetMesh"]])
        for before, after in zip(before_export_bounds, after_export_bounds):
            assert all(math.isclose(a, b, abs_tol=1e-5) for a, b in zip(before, after))
        assert accessory.parent is rig
        assert accessory.parent_bone == "Accessory"

        source_parent = bpy.data.objects.new("SourceScaleParent", None)
        target_parent = bpy.data.objects.new("TargetScaleParent", None)
        bpy.context.scene.collection.objects.link(source_parent)
        bpy.context.scene.collection.objects.link(target_parent)
        source_parent.scale = (0.5, 0.5, 0.5)
        target_parent.scale = (0.5, 0.5, 0.5)
        source_probe = make_rig("SourceScaleProbe", 1.0, 0.02)
        target_probe = make_rig("TargetScaleProbe", 100.0, 0.0544579625)
        source_probe.parent = source_parent
        target_probe.parent = target_parent
        source_probe.matrix_parent_inverse = blender_worker.Matrix.Identity(4)
        target_probe.matrix_parent_inverse = blender_worker.Matrix.Identity(4)
        bpy.context.view_layer.update()
        source_scale = source_probe.matrix_world.to_scale()
        target_scale = target_probe.matrix_world.to_scale()
        assert math.isclose(source_scale.x, 0.01, abs_tol=1e-8)
        assert math.isclose(target_scale.x, 0.02722898125, abs_tol=1e-8)
        assert math.isclose(
            target_probe.data.bones["Root"].length / source_probe.data.bones["Root"].length,
            100.0,
            abs_tol=1e-6,
        )
        real_matrix_factor = blender_worker.scale_aware_retarget_location_scale(
            source_scale,
            target_scale,
        )
        assert math.isclose(real_matrix_factor, 0.3672563849, abs_tol=1e-6)
        source_basis_delta = 0.2
        target_basis_delta = source_basis_delta * real_matrix_factor
        assert math.isclose(
            source_basis_delta * source_scale.x,
            target_basis_delta * target_scale.x,
            abs_tol=1e-8,
        )
        print(json.dumps({"status": "pass", "location_scale": round(result["location_scale"], 6)}, sort_keys=True))


if __name__ == "__main__":
    main()
