"""Ground interpolated zombie poses at source keys and 48 fps without altering limbs."""

import bpy
import json
import math
import numpy as np
import sys
from pathlib import Path


args = sys.argv[sys.argv.index("--") + 1 :]
source, out = (Path(value) for value in args[:2])
subdivisions = int(args[2]) if len(args) > 2 else 2
if subdivisions not in (2, 4):
    raise ValueError("Grounding subdivision must be 2 or 4")
out.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=str(source))
scene = bpy.context.scene
body = next(obj for obj in bpy.data.objects if obj.type == "MESH" and len(obj.data.vertices) == 14874)
rig = next(mod.object for mod in body.modifiers if mod.type == "ARMATURE")
root = rig.pose.bones["Hips"]


def curves(action):
    for layer in action.layers:
        for strip in layer.strips:
            for bag in strip.channelbags:
                yield from bag.fcurves


def minimum_z(frame):
    scene.frame_set(int(frame), subframe=frame % 1)
    evaluated = body.evaluated_get(bpy.context.evaluated_depsgraph_get())
    mesh = evaluated.to_mesh()
    coords = np.empty(len(mesh.vertices) * 3, dtype=np.float32)
    mesh.vertices.foreach_get("co", coords)
    coords = coords.reshape((-1, 3))
    matrix = np.asarray(evaluated.matrix_world, dtype=float)
    value = float(np.min(coords @ matrix[2, :3] + matrix[2, 3]))
    evaluated.to_mesh_clear()
    return value


def root_basis():
    original = root.location.copy()
    baseline = (rig.matrix_world @ root.matrix).translation.copy()
    columns = []
    for axis in range(3):
        root.location[axis] += 1.0
        bpy.context.view_layer.update()
        columns.append(np.asarray((rig.matrix_world @ root.matrix).translation - baseline, dtype=float))
        root.location = original.copy()
        bpy.context.view_layer.update()
    return np.column_stack(columns)


report = {"source": str(source), "target": str(out), "samples_per_frame": subdivisions, "actions": {}}
for role in ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"):
    action = bpy.data.actions[f"zombies_{role}_exact_final"]
    rig.animation_data_create()
    rig.animation_data.action = action
    rig.animation_data.action_slot = action.slots[0]
    root_curves = {curve.array_index: curve for curve in curves(action) if curve.data_path == 'pose.bones["Hips"].location'}
    original_times = [float(point.co.x) for point in root_curves[0].keyframe_points]
    start, end = original_times[0], original_times[-1]
    times = sorted(set(original_times) | {tick / subdivisions for tick in range(math.ceil(start * subdivisions), math.floor(end * subdivisions) + 1)})
    original_values = {axis: [curve.evaluate(time) for time in times] for axis, curve in root_curves.items()}
    clearances = [minimum_z(time) for time in times]
    basis = root_basis()
    adjustments = [np.linalg.solve(basis, np.array((0.0, 0.0, 0.001 - clearance))) for clearance in clearances]
    for axis, curve in root_curves.items():
        while curve.keyframe_points:
            curve.keyframe_points.remove(curve.keyframe_points[0], fast=True)
        for time, original, adjustment in zip(times, original_values[axis], adjustments):
            point = curve.keyframe_points.insert(time, float(original + adjustment[axis]), options={"FAST"})
            point.interpolation = "LINEAR"
        curve.update()
    after = [minimum_z(time) for time in times]
    report["actions"][role] = {
        "root_keys_before": len(original_times),
        "root_keys_after": len(times),
        "minimum_before": min(clearances),
        "maximum_before": max(clearances),
        "minimum_after": min(after),
        "maximum_after": max(after),
    }
    print(json.dumps({"role": role, **report["actions"][role]}), flush=True)
rig.animation_data.action = bpy.data.actions["zombies_idle_exact_final"]
rig.animation_data.action_slot = rig.animation_data.action.slots[0]
scene.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=str(out), compress=True)
(out.parent / "exact_reference_half_frame_grounding.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
