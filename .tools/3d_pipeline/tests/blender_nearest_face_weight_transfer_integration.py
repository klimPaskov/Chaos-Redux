"""Synthetic Blender proof for fail-closed nearest-face interpolated skin weights."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


def reset_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def make_armature() -> bpy.types.Object:
    data = bpy.data.armatures.new("TransferRigData")
    armature = bpy.data.objects.new("TransferRig", data)
    bpy.context.scene.collection.objects.link(armature)
    bpy.context.view_layer.objects.active = armature
    armature.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    bone_a = data.edit_bones.new("BoneA")
    bone_a.head = (0.0, 0.0, 0.0)
    bone_a.tail = (0.0, 0.0, 1.0)
    bone_b = data.edit_bones.new("BoneB")
    bone_b.head = (1.0, 0.0, 0.0)
    bone_b.tail = (1.0, 0.0, 1.0)
    bpy.ops.object.mode_set(mode="OBJECT")
    return armature


def make_mesh(name: str, vertices: list[tuple[float, float, float]]) -> bpy.types.Object:
    data = bpy.data.meshes.new(f"{name}Data")
    data.from_pydata(vertices, [], [(0, 1, 2)])
    data.update()
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    return obj


def main() -> None:
    reset_scene()
    armature = make_armature()
    source = make_mesh("SourceSkin", [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 1.0)])
    group_a = source.vertex_groups.new(name="BoneA")
    group_b = source.vertex_groups.new(name="BoneB")
    group_a.add([0], 1.0, "REPLACE")
    group_b.add([1, 2], 1.0, "REPLACE")
    target = make_mesh("TargetSkin", [(0.2, 0.1, 0.1), (0.6, 0.1, 0.1), (0.2, 0.6, 0.6)])

    report = blender_worker.bind_geometry_to_existing_rig(
        [source], target, armature, "nearest_face_interpolated"
    )
    if report["transferred_vertices"] != len(target.data.vertices):
        raise AssertionError(report)
    audit = report.get("nearest_face_audit") or {}
    if audit.get("failed_vertices") != 0 or audit.get("source_triangles") != 1:
        raise AssertionError(report)
    for vertex in target.data.vertices:
        weights = [float(item.weight) for item in vertex.groups]
        if not weights or abs(sum(weights) - 1.0) > 1e-6:
            raise AssertionError({"vertex": vertex.index, "weights": weights, "report": report})
    if max(len(vertex.groups) for vertex in target.data.vertices) < 2:
        raise AssertionError("Expected an interpolated vertex to retain both source bone weights.")
    print(json.dumps({"status": "pass", "report": report}, sort_keys=True))


if __name__ == "__main__":
    main()
