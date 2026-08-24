"""Registration contract for sourced-animation compound creature processing."""

from __future__ import annotations

import json
import os
import sys
import tomllib
import unittest
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.mcp_stdio import call_stdio  # noqa: E402


REGISTERED_TOOLS = {
    "chaosx_blender_hoi4_import_animation_action": {
        "job_id",
        "blend_rel",
        "source_rel",
        "provenance_rel",
        "checkpoint_rel",
        "source_action_name",
        "target_armature_name",
        "target_action_name",
        "source_kind",
        "source_reference_id",
        "source_sha256",
        "bone_chains",
        "promote_audited_target",
    },
    "chaosx_blender_hoi4_retime_animation_action": {
        "job_id",
        "blend_rel",
        "checkpoint_rel",
        "action_name",
        "target_armature_name",
        "source_fps",
        "target_fps",
    },
    "chaosx_blender_hoi4_segment_creature_components": {
        "job_id",
        "blend_rel",
        "checkpoint_rel",
        "region_mode",
        "rider_z_min_fraction",
        "rider_z_max_fraction",
        "rider_x_center_fraction",
        "rider_x_half_fraction",
        "rider_y_center_fraction",
        "rider_y_half_fraction",
        "rider_object_name",
        "body_object_name",
        "component_prefix",
    },
    "chaosx_blender_hoi4_calibrate_creature_scale": {
        "job_id",
        "blend_rel",
        "checkpoint_rel",
        "rider_component_names",
        "target_rider_runtime_height_m",
        "runtime_entity_scale",
    },
    "chaosx_blender_hoi4_correct_action_grounding": {
        "job_id",
        "blend_rel",
        "checkpoint_rel",
        "action_name",
        "target_armature_name",
        "grounding_policy",
        "root_bone",
    },
    "chaosx_blender_hoi4_prepare_export_coordinate_checkpoint": {
        "job_id",
        "blend_rel",
        "checkpoint_rel",
        "action_name",
        "target_armature_name",
    },
    "chaosx_blender_hoi4_sanitize_runtime_candidate": {
        "job_id",
        "blend_rel",
        "output_blend_rel",
        "target_height_m",
        "weight_only",
    },
}


class CompoundAdapterRegistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not os.environ.get("MESHY_API_KEY", "").strip():
            raise unittest.SkipTest("MESHY_API_KEY is required by the production adapter wrapper")
        wrapper = PIPELINE_ROOT / "wrappers" / "run_blender_hoi4_adapter.cmd"
        response = call_stdio(
            ["cmd.exe", "/d", "/c", "call", str(wrapper)],
            list_tools=True,
            timeout_seconds=60,
            cwd=REPO_ROOT,
        )
        cls.live = {tool["name"]: tool for tool in response["tools"]}

    def test_production_registration_exposes_only_source_preserving_compound_operations(self) -> None:
        config = tomllib.loads((REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8"))
        enabled = set(config["mcp_servers"]["blender_hoi4"]["enabled_tools"])
        self.assertTrue(set(REGISTERED_TOOLS) <= enabled)
        self.assertNotIn("chaosx_blender_hoi4_author_creature_action", enabled)
        self.assertNotIn("chaosx_blender_hoi4_offset_action_root", enabled)

    def test_live_schemas_are_bounded_and_exact(self) -> None:
        for tool_name, expected_properties in REGISTERED_TOOLS.items():
            self.assertIn(tool_name, self.live)
            properties = self.live[tool_name]["inputSchema"]["properties"]
            self.assertEqual(set(properties), expected_properties)
            self.assertFalse(
                {"python", "code", "shell", "url", "absolute_path"} & set(properties)
            )

    def test_external_action_and_compound_policies_are_fail_closed(self) -> None:
        import_schema = self.live["chaosx_blender_hoi4_import_animation_action"]["inputSchema"]
        self.assertEqual(
            import_schema["properties"]["source_kind"]["enum"],
            ["meshy_animate", "professional_source"],
        )
        grounding_schema = self.live["chaosx_blender_hoi4_correct_action_grounding"]["inputSchema"]
        self.assertEqual(
            grounding_schema["properties"]["grounding_policy"]["const"],
            "per_frame_root_contact_zero_clearance",
        )
        adapter_config = json.loads(
            (PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8")
        )
        operations = set(adapter_config["operations"])
        self.assertTrue(
            {
                "import_animation_action",
                "retime_animation_action",
                "segment_creature_components",
                "calibrate_creature_scale",
                "correct_action_grounding",
                "sanitize_runtime_candidate",
            }
            <= operations
        )


if __name__ == "__main__":
    unittest.main()
