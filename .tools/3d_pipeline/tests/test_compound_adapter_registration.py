"""Registration contract for bounded source-preserving mesh and runtime operations."""

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
    "chaosx_blender_hoi4_review_humanoid_components": {
        "job_id",
        "blend_rel",
        "expected_source_sha256",
        "mesh_name",
        "render_group",
        "component_ids",
        "component_offset",
        "component_limit",
        "preview_view_names",
    },
    "chaosx_blender_hoi4_sanitize_runtime_candidate": {
        "job_id",
        "blend_rel",
        "output_blend_rel",
        "target_height_m",
        "weight_only",
        "max_influences_per_vertex",
    },
}

# Rig, skin-weight and keyframe authoring now belongs to live Blender sessions
# through the MCP bridge, so no repository Python route may expose these again.
REMOVED_OPERATIONS = {
    "author_humanoid_rig",
    "author_humanoid_actions",
    "author_locomotion_action",
    "patch_existing_humanoid_action_phases",
    "author_creature_rig",
    "author_creature_action",
    "author_measured_creature_rig",
    "author_measured_creature_action",
    "inspect_fitted_humanoid_source",
    "author_fitted_humanoid_rig",
    "author_fitted_humanoid_action",
    "repair_explicit_skin",
    "preview_explicit_skin_selection",
    "repair_explicit_skin_batch",
    "collapse_identity_leaf_joints",
    "correct_action_grounding",
    "ground_existing_action",
    "offset_action_root",
    "retime_animation_action",
    "import_animation_action",
    "import_bvh_animation_action",
    "segment_creature_components",
    "calibrate_creature_scale",
    "attach_rigid_component",
}
REMOVED_TOOLS = {f"chaosx_blender_hoi4_{operation}" for operation in REMOVED_OPERATIONS}


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

    def test_production_registration_exposes_only_source_preserving_operations(self) -> None:
        config = tomllib.loads((REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8"))
        enabled = set(config["mcp_servers"]["blender_hoi4"]["enabled_tools"])
        self.assertTrue(set(REGISTERED_TOOLS) <= enabled)
        self.assertFalse(REMOVED_TOOLS & enabled, sorted(REMOVED_TOOLS & enabled))

    def test_live_schemas_are_bounded_and_exact(self) -> None:
        for tool_name, expected_properties in REGISTERED_TOOLS.items():
            self.assertIn(tool_name, self.live)
            properties = self.live[tool_name]["inputSchema"]["properties"]
            self.assertEqual(set(properties), expected_properties)
            self.assertFalse(
                {"python", "code", "shell", "url", "absolute_path"} & set(properties)
            )

    def test_adapter_config_registers_kept_operations_only(self) -> None:
        adapter_config = json.loads(
            (PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8")
        )
        operations = set(adapter_config["operations"])
        self.assertTrue(
            {
                "review_humanoid_components",
                "sanitize_runtime_candidate",
                "prepare_candidate",
                "prepare_export_coordinate_checkpoint",
                "process_textures",
                "export_mesh",
                "reimport_export",
            }
            <= operations
        )
        self.assertFalse(REMOVED_OPERATIONS & operations, sorted(REMOVED_OPERATIONS & operations))


if __name__ == "__main__":
    unittest.main()
