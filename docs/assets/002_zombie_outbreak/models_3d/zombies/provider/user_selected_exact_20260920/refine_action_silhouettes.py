"""Correct the two exported silhouette defects by blending existing Meshy skeletal motions."""

import bpy
import json
import sys
from mathutils import Quaternion
from pathlib import Path


source, output = (Path(value) for value in sys.argv[sys.argv.index("--") + 1:])
bpy.ops.wm.open_mainfile(filepath=str(source))
actions = bpy.data.actions


def channel_map(action):
    return {
        (curve.data_path, curve.array_index): curve
        for layer in action.layers
        for strip in layer.strips
        for bag in strip.channelbags
        for curve in bag.fcurves
    }


def quaternion_at(curves, bone, frame):
    path = f'pose.bones["{bone}"].rotation_quaternion'
    return Quaternion(tuple(curves[(path, channel)].evaluate(frame) for channel in range(4))).normalized()


def smooth(low, high, value):
    t = min(1.0, max(0.0, (value - low) / (high - low)))
    return t * t * (3 - 2 * t)


def replace(action, samples):
    mapping = channel_map(action)
    for bone, values in samples.items():
        path = f'pose.bones["{bone}"].rotation_quaternion'
        for channel in range(4):
            curve = mapping[(path, channel)]
            while curve.keyframe_points:
                curve.keyframe_points.remove(curve.keyframe_points[0], fast=True)
            for frame, quaternion in values:
                point = curve.keyframe_points.insert(frame, quaternion[channel], options={"FAST"})
                point.interpolation = "LINEAR"
            curve.update()


idle = channel_map(actions["zombies_idle_exact_final"])
attack = channel_map(actions["zombies_attack_exact_final"])
move_action = actions["zombies_move_exact_final"]
support_action = actions["zombies_support_attack_exact_final"]
defend_action = actions["zombies_defend_exact_final"]
retreat_action = actions["zombies_retreat_exact_final"]
move = channel_map(move_action)
support = channel_map(support_action)
defend = channel_map(defend_action)
retreat = channel_map(retreat_action)

# The Meshy stumble kick lifted the left shoe too far behind the body at the
# first quarter of the cycle. Preserve the stride but draw those leg joints
# toward the independently generated Meshy idle leg pose during that passage.
move_samples = {}
for bone, weight in {"LeftUpLeg": 0.44, "LeftLeg": 0.62, "LeftFoot": 0.34}.items():
    values = []
    for frame in range(1, 50):
        idle_frame = frame / 49 * 97
        blend = weight * smooth(11, 14, frame) * (1 - smooth(18, 23, frame))
        values.append((frame, quaternion_at(move, bone, frame).slerp(quaternion_at(idle, bone, idle_frame), blend)))
    move_samples[bone] = values
replace(move_action, move_samples)

# Meshy's two-fist clip passes through an implausible lateral T silhouette.
# Keep its pelvis, stride, spine, and timing; source the reach pose from the
# separate Meshy forward-grapple action through the active contact phase.
support_samples = {}
for bone, weight in {
    "LeftShoulder": 0.8, "LeftArm": 0.92, "LeftForeArm": 0.92, "LeftHand": 0.65,
    "RightShoulder": 0.8, "RightArm": 0.92, "RightForeArm": 0.92, "RightHand": 0.65,
}.items():
    values = []
    for frame in range(0, 85):
        attack_frame = frame / 84 * 115
        blend = weight * smooth(5, 17, frame) * (1 - smooth(58, 82, frame))
        values.append((frame, quaternion_at(support, bone, frame).slerp(quaternion_at(attack, bone, attack_frame), blend)))
    support_samples[bone] = values
replace(support_action, support_samples)

# The Meshy block preset is a held guard with very little visible travel. Add
# a braced backward step from the independently generated injured-walk clip
# while keeping the guarded hands and all original block timing channels.
defend_samples = {}
for bone, weight in {
    "Hips": 0.22, "Spine": 0.20, "Spine01": 0.20,
    "LeftUpLeg": 0.60, "LeftLeg": 0.58, "LeftFoot": 0.48,
    "RightUpLeg": 0.60, "RightLeg": 0.58, "RightFoot": 0.48,
}.items():
    values = []
    for frame in range(0, 85):
        retreat_frame = 1 + frame / 84 * 39
        blend = weight * smooth(4, 17, frame) * (1 - smooth(64, 80, frame))
        values.append((frame, quaternion_at(defend, bone, frame).slerp(quaternion_at(retreat, bone, retreat_frame), blend)))
    defend_samples[bone] = values
replace(defend_action, defend_samples)

output.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output), compress=True)
report = {
    "source": str(source), "checkpoint": str(output),
    "move": {"problem": "excessive rear-leg kick at first-quarter stride", "source_actions": [move_action.name, "zombies_idle_exact_final"], "affected_bones": list(move_samples)},
    "support_attack": {"problem": "lateral T pose at first-quarter attack", "source_actions": [support_action.name, "zombies_attack_exact_final"], "affected_bones": list(support_samples)},
    "defend": {"problem": "held guard lacked a readable recoil step", "source_actions": [defend_action.name, retreat_action.name], "affected_bones": list(defend_samples)},
    "method": "bone-quaternion blends between full Meshy-derived skeletal actions; all other bone and translation channels retained",
}
(output.parent / "exact_reference_silhouette_refinement.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report), flush=True)
