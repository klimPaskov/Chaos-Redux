"""Real-Blender regression for dominant-bone contact exclusion during grounding."""

from __future__ import annotations

import json
import math
import tempfile
from pathlib import Path

import bpy

import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
ADAPTER_ROOT = REPO_ROOT / ".tools" / "3d_pipeline" / "adapter"
sys.path.insert(0, str(ADAPTER_ROOT))

import blender_worker  # noqa: E402


def build_scene(source: Path) -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    armature_data = bpy.data.armatures.new("GroundRigData")
    rig = bpy.data.objects.new("GroundRig", armature_data)
    bpy.context.collection.objects.link(rig)
    rig["chaosx_working"] = True
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    root = armature_data.edit_bones.new("Root")
    root.head = (0.0, 0.0, 0.0)
    root.tail = (0.0, 0.0, 1.0)
    tail = armature_data.edit_bones.new("Tail")
    tail.head = root.tail
    tail.tail = (0.0, 0.0, 2.0)
    tail.parent = root
    tail.use_connect = True
    bpy.ops.object.mode_set(mode="OBJECT")

    mesh_data = bpy.data.meshes.new("GroundMeshData")
    mesh_data.from_pydata(
        [
            (-1.0, -1.0, 1.0),
            (1.0, -1.0, 1.0),
            (1.0, 1.0, 2.0),
            (-1.0, 1.0, 2.0),
            (-0.2, 0.0, -2.0),
            (0.2, 0.0, -2.0),
            (0.0, 0.4, -1.5),
        ],
        [],
        [(0, 1, 2, 3), (4, 5, 6)],
    )
    mesh_data.update()
    mesh = bpy.data.objects.new("GroundMesh", mesh_data)
    bpy.context.collection.objects.link(mesh)
    mesh["chaosx_working"] = True
    mesh.parent = rig
    modifier = mesh.modifiers.new("CHAOSX_RIG_TRANSFER", type="ARMATURE")
    modifier.object = rig
    root_group = mesh.vertex_groups.new(name="Root")
    root_group.add([0, 1, 2, 3], 1.0, "REPLACE")
    tail_group = mesh.vertex_groups.new(name="Tail")
    tail_group.add([4, 5, 6], 1.0, "REPLACE")

    rig.animation_data_create()
    action = bpy.data.actions.new("VerifiedWalk")
    action["chaosx_animation_source_kind"] = "professional_source"
    action["chaosx_animation_source_reference_id"] = "synthetic-grounding-proof"
    action["chaosx_animation_source_sha256"] = "B" * 64
    action["chaosx_animation_source_action"] = "VerifiedWalk"
    action["chaosx_animation_provenance_rel"] = "provider/provenance/synthetic.json"
    action["chaosx_animation_processing_policy"] = "verified-source-preserved"
    rig.animation_data.action = action
    for frame, angle in ((1, 0.0), (2, 0.2)):
        rig.pose.bones["Root"].location = (0.0, 0.0, 0.0)
        rig.pose.bones["Root"].keyframe_insert(data_path="location", frame=frame)
        rig.pose.bones["Tail"].rotation_mode = "XYZ"
        rig.pose.bones["Tail"].rotation_euler.x = angle
        rig.pose.bones["Tail"].keyframe_insert(data_path="rotation_euler", frame=frame)
    bpy.ops.wm.save_as_mainfile(filepath=str(source))


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chaosx_excluded_contact_grounding_") as temp_dir:
        job = Path(temp_dir)
        (job / "blender" / "reports").mkdir(parents=True)
        source = job / "source.blend"
        checkpoint = job / "grounded.blend"
        build_scene(source)
        result = blender_worker.correct_action_grounding(
            {
                "job_root": str(job),
                "payload": {
                    "blend_rel": "source.blend",
                    "checkpoint_rel": "grounded.blend",
                    "target_armature_name": "GroundRig",
                    "action_name": "VerifiedWalk",
                    "root_bone": "Root",
                    "excluded_contact_bones": ["Tail"],
                    "grounding_policy": "per_frame_root_contact_zero_clearance",
                },
            }
        )
        assert checkpoint.exists()
        assert result["status"] == "pass"
        assert result["excluded_contact_bones"] == ["Tail"]
        assert result["contact_selection_policy"] == "exclude_vertices_dominated_by_named_bones"
        assert result["action_provenance"]["source_sha256"] == "B" * 64
        assert result["retention_evidence"]["manual_or_procedural_replacement_authored"] is False
        assert all(math.isclose(frame["ground_contact_after"], 0.0, abs_tol=1e-5) for frame in result["frames"])
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint))
        action = bpy.data.actions["VerifiedWalk"]
        assert blender_worker.action_provenance(action)["source_sha256"] == "B" * 64
        filtered_minimum, _ = blender_worker.evaluated_contact_bounds(
            [bpy.data.objects["GroundMesh"]], ["Tail"]
        )
        raw_minimum, _ = blender_worker.evaluated_world_bounds([bpy.data.objects["GroundMesh"]])
        assert math.isclose(filtered_minimum.z, 0.0, abs_tol=1e-5)
        assert raw_minimum.z < -2.5
        print(json.dumps({"status": "pass", "filtered_ground_z": filtered_minimum.z}, sort_keys=True))


if __name__ == "__main__":
    main()
