"""Synthetic native-BVH import, retarget, provenance, and save/reopen proof."""

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


BONES = ("Root", "Spine", "Chest", "Neck", "Head", "Arm")
SOURCE_FRAME_TIME_TOKEN = ".0083333"
SOURCE_FPS = 1.0 / float(SOURCE_FRAME_TIME_TOKEN)


def reset_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)


def make_target(path: Path) -> None:
    reset_scene()
    armature_data = bpy.data.armatures.new("TargetRigData")
    rig = bpy.data.objects.new("TargetRig", armature_data)
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
    bpy.ops.wm.save_as_mainfile(filepath=str(path), check_existing=False)


def write_bvh(path: Path, frame_time_token: str = SOURCE_FRAME_TIME_TOKEN) -> None:
    lines = ["HIERARCHY", "ROOT Root", "{", "\tOFFSET 0 0 0", "\tCHANNELS 6 Xposition Yposition Zposition Zrotation Xrotation Yrotation"]
    indent = 1
    for name in BONES[1:]:
        lines.extend(["\t" * indent + f"JOINT {name}", "\t" * indent + "{", "\t" * (indent + 1) + "OFFSET 0 1 0", "\t" * (indent + 1) + "CHANNELS 3 Zrotation Xrotation Yrotation"])
        indent += 1
    lines.extend(["\t" * indent + "End Site", "\t" * indent + "{", "\t" * (indent + 1) + "OFFSET 0 1 0", "\t" * indent + "}"])
    for depth in range(indent - 1, -1, -1):
        lines.append("\t" * depth + "}")
    lines.extend(["MOTION", "Frames: 3", f"Frame Time: {frame_time_token}"])
    frames = []
    for frame in range(3):
        values = [0.0, 0.0, 0.0, 4.0 * frame, 2.0 * frame, 0.0]
        for index in range(5):
            values.extend([float((index + 1) * (frame + 1) * 3), float((index + 1) * frame), 0.0])
        frames.append(" ".join(str(value) for value in values))
    path.write_text("\n".join(lines + frames) + "\n", encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chaosx_bvh_import_") as temporary:
        job = Path(temporary)
        target = job / "target.blend"
        source = job / "79_86.bvh"
        provenance_path = job / "provenance.json"
        checkpoint = job / "output.blend"
        make_target(target)
        write_bvh(source)
        header = blender_worker.inspect_bvh_header(source)
        assert math.isclose(header["frame_time_seconds"], 0.0083333, abs_tol=1e-12)
        assert math.isclose(header["source_fps"], SOURCE_FPS, abs_tol=1e-9)
        for invalid_token in ("0", "-0.0083333", "nan", "inf", "1e999", ".", ".e3", "0.01junk"):
            invalid_source = job / f"invalid_{len(invalid_token)}_{abs(hash(invalid_token))}.bvh"
            write_bvh(invalid_source, invalid_token)
            try:
                blender_worker.inspect_bvh_header(invalid_source)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Invalid BVH Frame Time token was accepted: {invalid_token!r}")
        digest = hashlib.sha256(source.read_bytes()).hexdigest().upper()
        provenance_path.write_text(
            json.dumps(
                {
                    "verification_status": "verified",
                    "source_kind": "professional_source",
                    "source_format": "bvh",
                    "source_reference_id": "cmu-79-86-synthetic-test",
                    "source_action_name": "79_86",
                    "source_sha256": digest,
                    "source_fps": SOURCE_FPS,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        result = blender_worker.import_bvh_animation_action(
            {
                "job_root": str(job),
                "payload": {
                    "blend_rel": target.name,
                    "source_rel": source.name,
                    "provenance_rel": provenance_path.name,
                    "checkpoint_rel": checkpoint.name,
                    "source_action_name": "79_86",
                    "target_armature_name": "TargetRig",
                    "target_action_name": "unit_move",
                    "semantic_role": "move",
                    "source_reference_id": "cmu-79-86-synthetic-test",
                    "source_sha256": digest,
                    "source_fps": SOURCE_FPS,
                    "target_fps": 24.0,
                    "bone_chains": {name: [name] for name in BONES},
                    "root_motion_policy": "in_place_xy_preserve_z",
                    "global_scale": 1.0,
                    "axis_forward": "-Z",
                    "axis_up": "Y",
                },
            }
        )
        assert result["status"] == "pass"
        assert result["source_sha256"] == digest
        assert result["manual_or_procedural_replacement_authored"] is False
        assert result["save_reopen_status"] == "pass"
        assert result["root_xy_peak_after"] <= 1e-5
        assert len(result["curve_audit"]["driven_bones"]) >= 6
        assert len(result["curve_audit"]["articulated_bones"]) >= 4
        assert result["curve_audit"]["scale_curves"] == []
        assert result["action_provenance"]["source_sha256"] == digest
        print(json.dumps({"status": "pass", "result": result}, sort_keys=True))


if __name__ == "__main__":
    main()
