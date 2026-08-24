"""Synthetic save/reopen proof for a clean dual-source animation base."""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


TARGET_HEIGHT = 7.3518242835
BONES = ("Root", "Spine", "Chest", "Neck", "Head", "Accessory")


def reset_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)


def make_working_rig() -> tuple[bpy.types.Object, bpy.types.Object]:
    armature_data = bpy.data.armatures.new("CompoundRigData")
    rig = bpy.data.objects.new("CompoundRig", armature_data)
    bpy.context.scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    parent = None
    for index, name in enumerate(BONES):
        bone = armature_data.edit_bones.new(name)
        bone.head = (0.0, 0.0, float(index))
        bone.tail = (0.0, 0.0, float(index + 1))
        bone.parent = parent
        parent = bone
    bpy.ops.object.mode_set(mode="OBJECT")
    rig["chaosx_working"] = True

    mesh_data = bpy.data.meshes.new("CompoundMeshData")
    mesh_data.from_pydata(
        [(-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (1.0, 1.0, 10.0), (-1.0, 1.0, 10.0)],
        [],
        [(0, 1, 2), (0, 2, 3)],
    )
    mesh = bpy.data.objects.new("CompoundMesh", mesh_data)
    bpy.context.scene.collection.objects.link(mesh)
    mesh["chaosx_working"] = True
    mesh.parent = rig
    modifier = mesh.modifiers.new("CompoundRig", "ARMATURE")
    modifier.object = rig
    for index, name in enumerate(BONES):
        group = mesh.vertex_groups.new(name=name)
        group.add(range(len(mesh.data.vertices)), float(index + 1), "REPLACE")

    bind_action = bpy.data.actions.new("Compound|Bind|baselayer_WORKING")
    rig.animation_data_create()
    rig.animation_data.action = bind_action
    for frame, scale in ((1, 1.0), (2, 1.02)):
        rig.pose.bones["Root"].scale = (scale, scale, scale)
        rig.pose.bones["Root"].keyframe_insert("scale", frame=frame, group="Root")
    return rig, mesh


def main() -> None:
    reset_scene()
    rig, mesh = make_working_rig()
    base = blender_worker.prepare_dual_source_base_rig(rig)
    weights = blender_worker.sanitize_working_weights()
    assert base["working_actions"] == []
    assert rig.animation_data is None
    assert all(bone.matrix_basis == blender_worker.Matrix.Identity(4) for bone in rig.pose.bones)
    assert weights["policy"] == "keep_four_strongest_bone_influences_and_renormalize"

    blender_worker.normalize_geometry(TARGET_HEIGHT)
    with tempfile.TemporaryDirectory(prefix="chaosx_dual_source_base_") as temporary:
        checkpoint = Path(temporary) / "dual_source_base.blend"
        blender_worker.save_blend(checkpoint)
        proof = blender_worker.stabilize_saved_normalization(checkpoint, TARGET_HEIGHT)
        assert math.isclose(proof["persisted_height_m"], TARGET_HEIGHT, abs_tol=proof["tolerance_m"])
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
        reopened_rig = bpy.data.objects["CompoundRig"]
        reopened_mesh = bpy.data.objects["CompoundMesh"]
        assert reopened_rig.animation_data is None
        assert not [action for action in bpy.data.actions if "WORKING" in action.name]
        for vertex in reopened_mesh.data.vertices:
            positive = [element for element in vertex.groups if element.weight > 0.0]
            assert len(positive) <= 4
            assert math.isclose(sum(element.weight for element in positive), 1.0, abs_tol=1e-6)
        minimum, maximum = blender_worker.world_bounds([reopened_mesh])
        assert math.isclose(float(maximum.z - minimum.z), TARGET_HEIGHT, abs_tol=proof["tolerance_m"])
        print(
            json.dumps(
                {
                    "status": "pass",
                    "persisted_height_m": proof["persisted_height_m"],
                    "working_actions": [],
                    "maximum_influences": 4,
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
