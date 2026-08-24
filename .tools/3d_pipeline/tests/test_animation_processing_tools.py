"""Focused live-schema and client-forwarding tests for bounded animation processing."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from blender_client import BlenderAdapterClient  # noqa: E402
from adapter.normalization_convergence import evaluate_convergence_step  # noqa: E402
from lib.mcp_stdio import call_stdio  # noqa: E402


TOOLS = {
    "chaosx_blender_hoi4_import_animation_action": {
        "job_id", "blend_rel", "source_rel", "provenance_rel", "checkpoint_rel",
        "source_action_name", "target_armature_name", "target_action_name",
        "source_kind", "source_reference_id", "source_sha256", "bone_chains",
        "promote_audited_target",
    },
    "chaosx_blender_hoi4_retime_animation_action": {
        "job_id", "blend_rel", "checkpoint_rel", "action_name", "target_armature_name",
        "source_fps", "target_fps",
    },
    "chaosx_blender_hoi4_correct_action_grounding": {
        "job_id", "blend_rel", "checkpoint_rel", "action_name", "target_armature_name",
        "grounding_policy", "root_bone",
    },
}


class AnimationProcessingToolTests(unittest.TestCase):
    def test_fresh_mcp_process_lists_schema_locked_tools(self) -> None:
        wrapper = PIPELINE_ROOT / "wrappers" / "run_blender_hoi4_adapter.cmd"
        response = call_stdio(
            ["cmd.exe", "/d", "/c", "call", str(wrapper)],
            list_tools=True,
            timeout_seconds=60,
            cwd=REPO_ROOT,
        )
        live = {tool["name"]: tool for tool in response["tools"]}
        for name, expected_properties in TOOLS.items():
            self.assertIn(name, live)
            schema = live[name]["inputSchema"]
            self.assertEqual(set(schema["properties"]), expected_properties)
            self.assertFalse({"python", "code", "shell", "url", "absolute_path"} & set(schema["properties"]))
        import_schema = live["chaosx_blender_hoi4_import_animation_action"]["inputSchema"]
        self.assertEqual(import_schema["properties"]["source_kind"]["enum"], ["meshy_animate", "professional_source"])
        grounding_schema = live["chaosx_blender_hoi4_correct_action_grounding"]["inputSchema"]
        self.assertEqual(
            grounding_schema["properties"]["grounding_policy"]["const"],
            "per_frame_root_contact_zero_clearance",
        )
        prepare_properties = live["chaosx_blender_hoi4_prepare_candidate"]["inputSchema"]["properties"]
        self.assertIn("geometry_object_name", prepare_properties)
        self.assertIn("dual_source_base_rig", prepare_properties)
        self.assertNotIn("geometry_object_names", prepare_properties)

    def test_config_and_lock_match_version_and_operations(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        route = json.loads((PIPELINE_ROOT / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))["routes"]["blender_hoi4_adapter"]
        self.assertEqual(config["adapter_version"], "1.10.7")
        self.assertEqual(route["version"], "1.10.7")
        for operation in ("import_animation_action", "retime_animation_action", "correct_action_grounding"):
            self.assertIn(operation, config["operations"])
            self.assertIn(operation, route["operations"])

    def test_client_wrappers_forward_locked_arguments(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        calls: list[tuple[str, dict[str, object]]] = []
        client.call = lambda tool, arguments: calls.append((tool, arguments)) or {"status": "pass"}  # type: ignore[method-assign]
        client.import_animation_action(
            "unit", "target.blend", "source.glb", "provenance.json", "imported.blend",
            "SourceAction", "Armature", "runtime_action", "meshy_animate", "task-123", "A" * 64,
        )
        client.retime_animation_action("unit", "imported.blend", "retimed.blend", "runtime_action", "Armature", 30.0, 24.0)
        client.correct_action_grounding(
            "unit", "retimed.blend", "grounded.blend", "runtime_action", "Armature",
            "per_frame_root_contact_zero_clearance",
        )
        self.assertEqual([name for name, _ in calls], list(TOOLS))
        self.assertEqual(calls[0][1]["provenance_rel"], "provenance.json")
        self.assertEqual(calls[1][1]["target_fps"], 24.0)
        self.assertEqual(calls[2][1]["grounding_policy"], "per_frame_root_contact_zero_clearance")

    def test_prepare_candidate_forwards_topology_preservation(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        calls: list[tuple[str, dict[str, object]]] = []
        client.call = lambda tool, arguments: calls.append((tool, arguments)) or {"status": "pass"}  # type: ignore[method-assign]
        client.prepare_candidate(
            "unit",
            source_rel="source.fbx",
            geometry_source_rel="audited.blend",
            geometry_object_name="ApprovedGeometry.001",
            dual_source_base_rig=True,
            geometry_weight_mode="bone_distance",
            source_armature_name="Rig",
            source_mesh_names=["Body", "Head"],
            asset_kind="nonhumanoid_creature",
            target_height_m=7.0,
            runtime_stem="creature",
            preserve_geometry_topology=True,
        )
        self.assertEqual(calls[0][0], "chaosx_blender_hoi4_prepare_candidate")
        self.assertTrue(calls[0][1]["preserve_geometry_topology"])
        self.assertEqual(calls[0][1]["geometry_object_name"], "ApprovedGeometry.001")
        self.assertTrue(calls[0][1]["dual_source_base_rig"])
        self.assertEqual(calls[0][1]["geometry_weight_mode"], "bone_distance")
        self.assertEqual(calls[0][1]["source_armature_name"], "Rig")
        self.assertEqual(calls[0][1]["source_mesh_names"], ["Body", "Head"])

    def test_worker_requires_one_safe_local_geometry_mesh(self) -> None:
        source = (PIPELINE_ROOT / "adapter" / "blender_worker.py").read_text(encoding="utf-8")
        self.assertIn('dual_source_base_rig requires geometry_source_rel', source)
        self.assertIn('geometry_object_name requires geometry_source_rel', source)
        self.assertIn('explicit_safe_name(\n            payload.get("geometry_object_name")', source)
        self.assertIn('obj.name == requested_geometry_object', source)
        self.assertIn('selected_geometry.library is not None', source)
        self.assertIn('selected_geometry.data.library is not None', source)

    def test_dual_source_base_rig_contract_clears_bind_clip_and_sanitizes_weights(self) -> None:
        source = (PIPELINE_ROOT / "adapter" / "blender_worker.py").read_text(encoding="utf-8")
        self.assertIn("target_armature.animation_data_clear()", source)
        self.assertIn("pose_bone.matrix_basis = Matrix.Identity(4)", source)
        self.assertIn('"working_actions": []', source)
        self.assertIn("base_weight_sanitization = sanitize_working_weights()", source)
        self.assertIn("stabilize_dual_source_base_normalization(pre_export, target_height)", source)
        self.assertIn('obj["chaosx_working"] = False', source)

    def test_normalization_convergence_accepts_and_corrects(self) -> None:
        accepted = evaluate_convergence_step(
            target=8.0, persisted=8.00001, tolerance=0.0001,
            previous_delta=0.001, corrections_applied=2, max_corrections=8,
        )
        self.assertEqual(accepted["status"], "accepted")
        correction = evaluate_convergence_step(
            target=8.0, persisted=8.001, tolerance=0.0001,
            previous_delta=0.004, corrections_applied=2, max_corrections=8,
        )
        self.assertEqual(correction["status"], "correct")
        self.assertGreater(correction["correction_factor"], 0.0)

    def test_normalization_convergence_rejects_stall_divergence_and_sign_flip(self) -> None:
        cases = (
            (8.001, 0.0010001, "stalled"),
            (8.002, 0.001, "diverged"),
            (7.999, 0.001, "changed sign"),
        )
        for persisted, previous, expected in cases:
            with self.subTest(expected=expected):
                with self.assertRaisesRegex(RuntimeError, expected):
                    evaluate_convergence_step(
                        target=8.0, persisted=persisted, tolerance=0.00001,
                        previous_delta=previous, corrections_applied=2, max_corrections=8,
                    )

    def test_normalization_convergence_rejects_cap_exhaustion(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "correction cap"):
            evaluate_convergence_step(
                target=8.0, persisted=8.001, tolerance=0.00001,
                previous_delta=0.002, corrections_applied=8, max_corrections=8,
            )

    def test_dual_source_base_survives_clean_save_and_reopen(self) -> None:
        config = json.loads(
            (PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8")
        )
        integration = PIPELINE_ROOT / "tests" / "blender_dual_source_base_regression.py"
        completed = subprocess.run(
            [config["blender_executable"], "--background", "--factory-startup", "--python", str(integration)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        output = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0, output)
        self.assertIn('"status": "pass"', output)


if __name__ == "__main__":
    unittest.main()
