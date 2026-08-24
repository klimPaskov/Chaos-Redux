"""Registration and native Blender integration tests for bounded BVH import."""

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
from lib.mcp_stdio import call_stdio  # noqa: E402


TOOL = "chaosx_blender_hoi4_import_bvh_animation_action"
PROPERTIES = {
    "job_id", "blend_rel", "source_rel", "provenance_rel", "checkpoint_rel",
    "source_action_name", "target_armature_name", "target_action_name", "semantic_role",
    "source_reference_id", "source_sha256", "source_fps", "target_fps", "bone_chains",
    "root_motion_policy", "global_scale", "axis_forward", "axis_up", "promote_audited_target",
}


class BvhAnimationImportTests(unittest.TestCase):
    def test_live_schema_is_exact_and_fail_closed(self) -> None:
        wrapper = PIPELINE_ROOT / "wrappers" / "run_blender_hoi4_adapter.cmd"
        response = call_stdio(
            ["cmd.exe", "/d", "/c", "call", str(wrapper)],
            list_tools=True,
            timeout_seconds=60,
            cwd=REPO_ROOT,
        )
        live = {tool["name"]: tool for tool in response["tools"]}
        self.assertIn(TOOL, live)
        schema = live[TOOL]["inputSchema"]
        self.assertEqual(set(schema["properties"]), PROPERTIES)
        self.assertFalse({"python", "code", "shell", "url", "absolute_path"} & PROPERTIES)
        self.assertEqual(schema["properties"]["root_motion_policy"]["const"], "in_place_xy_preserve_z")
        self.assertEqual(set(schema["properties"]["axis_forward"]["enum"]), {"X", "Y", "Z", "-X", "-Y", "-Z"})

    def test_registration_lock_and_allowlist(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        route = json.loads((PIPELINE_ROOT / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))["routes"]["blender_hoi4_adapter"]
        self.assertEqual(config["adapter_version"], "1.10.8")
        self.assertEqual(route["version"], "1.10.8")
        self.assertIn("import_bvh_animation_action", config["operations"])
        self.assertIn("import_bvh_animation_action", route["operations"])
        codex_config = (REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8")
        self.assertIn(f'"{TOOL}"', codex_config)

    def test_client_forwards_exact_contract(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        calls: list[tuple[str, dict[str, object]]] = []
        client.call = lambda tool, arguments: calls.append((tool, arguments)) or {"status": "pass"}  # type: ignore[method-assign]
        digest = "A" * 64
        client.import_bvh_animation_action(
            "unit", "target.blend", "79_86.bvh", "provenance.json", "output.blend",
            "79_86", "TargetRig", "unit_move", "move", "cmu-79-86", digest,
            30.0, 24.0, {"Root": ["Root"]}, "in_place_xy_preserve_z",
        )
        self.assertEqual(calls[0][0], TOOL)
        self.assertEqual(set(calls[0][1]), PROPERTIES)
        self.assertEqual(calls[0][1]["source_sha256"], digest)

    def test_worker_uses_native_import_and_preserves_source_identity(self) -> None:
        source = (PIPELINE_ROOT / "adapter" / "blender_worker.py").read_text(encoding="utf-8")
        self.assertIn("bpy.ops.import_anim.bvh(", source)
        self.assertIn('source.stem != source_action_name', source)
        self.assertIn('"source_kind": "professional_source"', source)
        self.assertIn('"manual_or_procedural_replacement_authored": False', source)
        self.assertIn("action_curve_signature(reopened_action)", source)
        self.assertNotIn("exec(", source[source.index("def import_bvh_animation_action"):source.index("def retime_animation_action")])

    def test_native_bvh_import_retargets_and_survives_reopen(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        integration = PIPELINE_ROOT / "tests" / "blender_bvh_import_integration.py"
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
