"""Decoded PDX animation delivery and existing-curve continuity tests."""
from __future__ import annotations

import math
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import animation_delivery_checks as delivery  # noqa: E402


def quaternion_z(degrees, sign=1.0):
    half = math.radians(degrees) / 2.0
    return (0.0, 0.0, sign * math.sin(half), sign * math.cos(half))


def animation_tree(translations, rotations, *, fps=30.0, channels="tq", initial_translation=None,
                   initial_rotation=None):
    count = len(translations)
    root = ET.Element("File", {"pdxasset": "[1, 0]"})
    info = ET.SubElement(root, "info", {"fps": repr([fps]), "sa": repr([count]), "j": "[1]"})
    ET.SubElement(info, "Hips", {"sa": repr([channels]),
                                     "t": repr(list(initial_translation or translations[0])),
                                     "q": repr(list(initial_rotation or rotations[0])),
                                     "s": "[1.0]"})
    samples = ET.SubElement(root, "samples")
    if "t" in channels:
        samples.set("t", repr([value for translation in translations for value in translation]))
    if "q" in channels:
        samples.set("q", repr([value for rotation in rotations for value in rotation]))
    object_root = ET.SubElement(root, "object")
    model = ET.SubElement(object_root, "Model")
    skeleton = ET.SubElement(model, "skeleton")
    ET.SubElement(skeleton, "Hips", {"ix": "[0]", "tx": repr([1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.])})
    return root


def parent_rotation_tree():
    root = ET.Element("File", {"pdxasset": "[1, 0]"})
    info = ET.SubElement(root, "info", {"fps": "[30.0]", "sa": "[2]", "j": "[2]"})
    ET.SubElement(info, "Hips", {"sa": "['q']", "t": "[0., 0., 0.]", "q": repr(list(quaternion_z(0))), "s": "[1.0]"})
    ET.SubElement(info, "Hand", {"sa": "['']", "t": "[1., 0., 0.]", "q": "[0., 0., 0., 1.]", "s": "[1.0]"})
    samples = ET.SubElement(root, "samples", {"q": repr(list(quaternion_z(0) + quaternion_z(90)))})
    model = ET.SubElement(ET.SubElement(root, "object"), "Model")
    skeleton = ET.SubElement(model, "skeleton")
    ET.SubElement(skeleton, "Hips", {"ix": "[0]", "tx": "[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]"})
    ET.SubElement(skeleton, "Hand", {"ix": "[1]", "pa": "[0]", "tx": "[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]"})
    return root


class MutableCoordinate:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __getitem__(self, index):
        return (self.x, self.y)[index]


class FakeKey:
    def __init__(self, frame, value):
        self.co = MutableCoordinate(frame, value)
        self.handle_left = MutableCoordinate(frame - 0.25, value - 0.1)
        self.handle_right = MutableCoordinate(frame + 0.25, value + 0.1)


class FakeCurve:
    def __init__(self, path, index, values):
        self.data_path = path
        self.array_index = index
        self.keyframe_points = [FakeKey(frame, value) for frame, value in values]


class QuaternionCurveContinuity(unittest.TestCase):
    def curves(self, second=( -0.98, -0.2, 0.0, 0.0), aligned=True):
        path = 'pose.bones["Hips"].rotation_quaternion'
        first = (1.0, 0.0, 0.0, 0.0)
        return [FakeCurve(path, component,
                          [(1.0, first[component]),
                           (2.0 if aligned or component < 3 else 2.00001, second[component])])
                for component in range(4)]

    def test_negates_existing_components_and_handles_without_adding_keys(self):
        curves = self.curves()
        key_counts = [len(curve.keyframe_points) for curve in curves]
        old_xy = [[(point.co.x, point.handle_left.x, point.handle_right.x) for point in curve.keyframe_points]
                  for curve in curves]
        old_handle_values = [(curve.keyframe_points[1].handle_left.y, curve.keyframe_points[1].handle_right.y)
                             for curve in curves]
        report = delivery.normalize_quaternion_curve_signs(curves)
        values = tuple(curves[index].keyframe_points[1].co.y for index in range(4))
        self.assertAlmostEqual(values[0], 0.98)
        self.assertAlmostEqual(values[1], 0.2)
        self.assertEqual(report["sign_flipped_key_count"], 1)
        self.assertEqual([len(curve.keyframe_points) for curve in curves], key_counts)
        for channel, curve in enumerate(curves):
            self.assertEqual([(point.co.x, point.handle_left.x, point.handle_right.x) for point in curve.keyframe_points], old_xy[channel])
            self.assertAlmostEqual(curve.keyframe_points[1].handle_left.y, -old_handle_values[channel][0])
            self.assertAlmostEqual(curve.keyframe_points[1].handle_right.y, -old_handle_values[channel][1])
        self.assertEqual(report["keys_added"], 0)
        self.assertEqual(report["keys_removed"], 0)

    def test_misaligned_channels_block_before_any_curve_mutation(self):
        curves = self.curves(aligned=False)
        before = [[(key.co.x, key.co.y, key.handle_left.y, key.handle_right.y) for key in curve.keyframe_points]
                  for curve in curves]
        with self.assertRaisesRegex(ValueError, "exactly aligned"):
            delivery.normalize_quaternion_curve_signs(curves)
        after = [[(key.co.x, key.co.y, key.handle_left.y, key.handle_right.y) for key in curve.keyframe_points]
                 for curve in curves]
        self.assertEqual(after, before)

    def test_zero_quaternion_in_later_group_blocks_before_earlier_group_mutation(self):
        good = self.curves()
        path = 'pose.bones["Wrist"].rotation_quaternion'
        bad = [FakeCurve(path, component, [(1.0, 0.0)]) for component in range(4)]
        curves = good + bad
        before = [[(key.co.x, key.co.y, key.handle_left.y, key.handle_right.y) for key in curve.keyframe_points]
                  for curve in curves]
        with self.assertRaisesRegex(ValueError, "zero quaternion"):
            delivery.normalize_quaternion_curve_signs(curves)
        after = [[(key.co.x, key.co.y, key.handle_left.y, key.handle_right.y) for key in curve.keyframe_points]
                 for curve in curves]
        self.assertEqual(after, before)


class AnimationDelivery(unittest.TestCase):
    def test_sign_flips_and_single_frame_spikes_are_reported_from_decoded_samples(self):
        tree = animation_tree([(0., 0., 0.), (0., 0., 0.), (0.3, 0., 0.)],
                              [quaternion_z(0), quaternion_z(25, -1), quaternion_z(70)])
        result = delivery.inspect_animation_delivery(tree, action_name="test_attack", role="attack",
                                                     looped=False, root_bone="Hips")
        self.assertEqual(result["quaternion_sign_continuity"]["status"], "blocked")
        self.assertEqual(result["single_frame_limits"]["status"], "blocked")
        self.assertGreaterEqual(len(result["single_frame_limits"]["violations"]), 1)
        self.assertTrue(result["motion_peak_table"])
        self.assertTrue({"frame", "bone", "angular_deg", "translation_step", "time_seconds"} <= set(result["motion_peak_table"][0]))
        self.assertEqual(result["root_motion"]["pdx_horizontal_axes"], ["x", "z"])
        self.assertEqual(result["root_motion"]["pdx_vertical_axis"], "y")

    def test_quaternion_sign_equivalence_does_not_create_a_rotation_spike(self):
        q = quaternion_z(4)
        tree = animation_tree([(0., 0., 0.), (0., 0., 0.)], [q, tuple(-value for value in q)])
        result = delivery.inspect_animation_delivery(tree, role="move", action_name="move", looped=False,
                                                     root_bone="Hips", humanoid=False)
        self.assertEqual(result["quaternion_sign_continuity"]["status"], "blocked")
        self.assertFalse(any(row["kind"] == "single_frame_rotation_exceeds_limit"
                             for row in result["single_frame_limits"]["violations"]))

    def test_strike_window_exempts_only_declared_transition(self):
        tree = animation_tree([(0., 0., 0.), (0., 0., 0.), (0.3, 0., 0.)],
                              [quaternion_z(0), quaternion_z(40), quaternion_z(40)])
        result = delivery.inspect_animation_delivery(tree, role="attack", action_name="attack", looped=False,
                                                     root_bone="Hips", strike_windows=[(2, 2)])
        self.assertEqual([row["kind"] for row in result["single_frame_limits"]["violations"]],
                         ["world_joint_translation_exceeds_limit"])
        self.assertEqual(result["single_frame_limits"]["violations"][0]["frame"], 3)
        self.assertEqual(result["root_motion"]["status"], "blocked")

    def test_pdx_y_is_preserved_vertical_and_death_forward_uses_negative_z(self):
        vertical_tree = animation_tree([(0., 0., 0.), (0., 0.5, 0.)],
                                       [quaternion_z(0), quaternion_z(0)])
        nondeath = delivery.inspect_animation_delivery(vertical_tree, role="idle", looped=False,
                                                        root_bone="Hips", humanoid=False)
        self.assertEqual(nondeath["root_motion"]["status"], "pass")
        death_tree = animation_tree([(0., 0., 0.), (0.3, 0., 0.)],
                                   [quaternion_z(0), quaternion_z(0)])
        death = delivery.inspect_animation_delivery(death_tree, role="death", looped=False,
                                                     root_bone="Hips", humanoid=False)
        self.assertEqual(death["root_motion"]["status"], "pass")
        forward_tree = animation_tree([(0., 0., 0.), (0., 0., -0.21)],
                                      [quaternion_z(0), quaternion_z(0)])
        forward = delivery.inspect_animation_delivery(forward_tree, role="death", looped=False,
                                                       root_bone="Hips", humanoid=False)
        self.assertEqual(forward["root_motion"]["status"], "blocked")

    def test_loop_seam_requires_both_angle_and_position_limits(self):
        tree = animation_tree([(0., 0., 0.), (0.06, 0., 0.)],
                              [quaternion_z(0), quaternion_z(4)])
        result = delivery.inspect_animation_delivery(tree, role="idle", action_name="idle", looped=True,
                                                     root_bone="Hips", humanoid=False)
        self.assertEqual(result["loop_seam"]["status"], "blocked")
        self.assertEqual(result["status"], "blocked")

    def test_unresolved_profile_loop_root_or_foot_evidence_never_passes(self):
        tree = animation_tree([(0., 0., 0.), (0., 0., 0.)],
                              [quaternion_z(0), quaternion_z(0)])
        result = delivery.inspect_animation_delivery(tree, role="move", action_name="move")
        self.assertEqual(result["status"], "needs_review")
        self.assertEqual(result["root_motion"]["status"], "needs_review")
        self.assertEqual(result["foot_contacts"]["status"], "unmeasured")
        self.assertEqual(result["foot_contacts"]["suggested_event_times_seconds"], [])

    def test_measured_humanoid_move_contact_counts_and_suggested_times(self):
        tree = animation_tree([(0., 0., 0.)] * 3, [quaternion_z(0)] * 3, fps=2.0, channels="q")
        feet = {"left": {"bone": "LeftFoot", "world_positions": [(0., 0., 0.), (0., 0., 0.), (0.1, 0., 0.1)]},
                "right": {"bone": "RightFoot", "world_positions": [(1., 0., 0.), (1., 0., 0.), (1.1, 0., 0.1)]}}
        evidence = {"feet": feet, "ground_plane": {"normal": [0., 0., 1.], "offset": 0.0},
                    "contact_tolerance": 0.01, "stationary_tolerance": 0.02,
                    "measurement_uncertainty": 0.0, "min_contact_frames": 1}
        result = delivery.inspect_animation_delivery(tree, role="move", action_name="move", looped=False,
                                                     root_bone="Hips", humanoid=True, foot_world_measurements=evidence)
        self.assertEqual(result["cycle_duration_seconds"], 1.5)
        self.assertEqual(result["foot_contacts"]["status"], "pass")
        self.assertEqual(result["foot_contacts"]["plant_counts"], {"left": {"certain": 1, "possible": 1, "uncertain": 0},
                                                                    "right": {"certain": 1, "possible": 1, "uncertain": 0}})
        self.assertEqual(result["status"], "pass")

    def test_world_joint_motion_catches_parent_rotation_with_static_local_translation(self):
        tree = parent_rotation_tree()
        result = delivery.inspect_animation_delivery(tree, role="move", action_name="move", looped=False,
                                                     root_bone="Hips", humanoid=False)
        self.assertFalse(result["single_frame_limits"]["local_channel_translation_exceedances_review_only"])
        rows = [row for row in result["world_motion"]["violations"]
                if row["bone"] == "Hand" and row["kind"] == "world_joint_translation_exceeds_limit"]
        self.assertEqual(len(rows), 1)
        self.assertGreater(rows[0]["translation_step"], 0.25)
        self.assertEqual(result["world_motion"]["measurement_space"], "PDX Y-up local TRS composed through decoded mesh parent indices")


if __name__ == "__main__":
    unittest.main()
