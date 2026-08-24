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

    def test_config_and_lock_match_version_and_operations(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        route = json.loads((PIPELINE_ROOT / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))["routes"]["blender_hoi4_adapter"]
        self.assertEqual(config["adapter_version"], "1.10.2")
        self.assertEqual(route["version"], "1.10.2")
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
        self.assertEqual(calls[0][1]["geometry_weight_mode"], "bone_distance")
        self.assertEqual(calls[0][1]["source_armature_name"], "Rig")
        self.assertEqual(calls[0][1]["source_mesh_names"], ["Body", "Head"])


if __name__ == "__main__":
    unittest.main()
