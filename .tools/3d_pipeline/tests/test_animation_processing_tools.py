"""Focused live-schema and client-forwarding tests for bounded animation processing."""

from __future__ import annotations

import json
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
    "chaosx_blender_hoi4_prepare_export_coordinate_checkpoint": {
        "job_id", "blend_rel", "checkpoint_rel", "action_name", "target_armature_name",
    },
}

# Bounded candidate preparation inputs consumed by the pilot orchestrator.
CANDIDATE_INPUTS = {
    "source_rel", "asset_kind", "target_height_m", "runtime_entity_scale", "runtime_stem",
    "target_triangles", "vanilla_reference", "texture_source_rels",
    "max_runtime_footprint_m", "runtime_footprint_policy",
}

# Repository Python no longer binds provider geometry to a rig, so these payload
# keys must not come back: rigs and skin weights are authored live in Blender.
REMOVED_CANDIDATE_INPUTS = {
    "rig_mesh", "source_armature_name", "geometry_weight_mode", "dual_source_base_rig",
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
        prepare_properties = set(live["chaosx_blender_hoi4_prepare_candidate"]["inputSchema"]["properties"])
        self.assertTrue(CANDIDATE_INPUTS <= prepare_properties)
        self.assertFalse(REMOVED_CANDIDATE_INPUTS & prepare_properties)
        self.assertNotIn("geometry_object_names", prepare_properties)

    def test_config_and_lock_match_version_and_operations(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        route = json.loads((PIPELINE_ROOT / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))["routes"]["blender_hoi4_adapter"]
        self.assertEqual(config["adapter_version"], route["version"])
        for operation in ("prepare_candidate", "prepare_export_coordinate_checkpoint"):
            self.assertIn(operation, config["operations"])
            self.assertIn(operation, route["operations"])

    def test_client_wrappers_forward_locked_arguments(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        calls: list[tuple[str, dict[str, object]]] = []
        client.call = lambda tool, arguments: calls.append((tool, arguments)) or {"status": "pass"}  # type: ignore[method-assign]
        client.prepare_export_coordinate_checkpoint(
            "unit", "grounded.blend", "export_coordinates.blend", "runtime_action", "Armature",
        )
        self.assertEqual([name for name, _ in calls], list(TOOLS))
        self.assertEqual(calls[0][1]["checkpoint_rel"], "export_coordinates.blend")

    def test_export_coordinate_checkpoint_is_drift_guarded(self) -> None:
        source = (PIPELINE_ROOT / "adapter" / "blender_worker.py").read_text(encoding="utf-8")
        self.assertIn("existing_pdx_export_coordinate_conversion_checkpoint_only", source)
        self.assertIn("Export-coordinate checkpoint drift validation failed", source)
        self.assertIn("protected source/reference drift", source)
        self.assertIn("material/image binding drift", source)
        self.assertIn("action_provenance(reopened_action) != action_source", source)

    def test_prepare_candidate_forwards_bounded_candidate_inputs(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        calls: list[tuple[str, dict[str, object]]] = []
        client.call = lambda tool, arguments: calls.append((tool, arguments)) or {"status": "pass"}  # type: ignore[method-assign]
        client.prepare_candidate(
            "unit",
            source_rel="source.glb",
            asset_kind="static",
            target_height_m=1.5,
            runtime_entity_scale=2.0,
            runtime_stem="beacon",
            target_triangles=15000,
            vanilla_reference={"mesh": "reference.mesh"},
            texture_source_rels={"diffuse": "provider/downloads/base_color.png"},
            max_runtime_footprint_m=4.0,
            runtime_footprint_policy="reject",
        )
        self.assertEqual(calls[0][0], "chaosx_blender_hoi4_prepare_candidate")
        payload = calls[0][1]
        self.assertTrue(CANDIDATE_INPUTS <= set(payload))
        self.assertEqual(payload["asset_kind"], "static")
        self.assertEqual(payload["target_triangles"], 15000)
        self.assertEqual(payload["texture_source_rels"], {"diffuse": "provider/downloads/base_color.png"})
        self.assertEqual(payload["runtime_footprint_policy"], "reject")
        self.assertFalse(REMOVED_CANDIDATE_INPUTS & set(payload))

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


if __name__ == "__main__":
    unittest.main()
