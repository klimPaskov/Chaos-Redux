"""Focused schema, client, worker, and Blender preservation tests for weight-only cleanup."""

from __future__ import annotations

import ast
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


TOOL = "chaosx_blender_hoi4_sanitize_runtime_candidate"


class WeightOnlySanitizeContractTests(unittest.TestCase):
    def test_fresh_mcp_process_exposes_backward_compatible_option(self) -> None:
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
        self.assertEqual(
            set(schema["properties"]),
            {"job_id", "blend_rel", "output_blend_rel", "target_height_m", "weight_only", "max_influences_per_vertex"},
        )
        self.assertEqual(schema["properties"]["weight_only"]["type"], "boolean")
        self.assertFalse(schema["properties"]["weight_only"]["default"])
        self.assertEqual(schema["properties"]["max_influences_per_vertex"]["default"], 4)
        self.assertNotIn("weight_only", schema["required"])
        self.assertFalse({"python", "code", "shell", "url", "absolute_path"} & set(schema["properties"]))

    def test_client_forwards_explicit_weight_only_contract(self) -> None:
        client = BlenderAdapterClient.__new__(BlenderAdapterClient)
        captured: dict[str, object] = {}

        def fake_call(tool: str, arguments: dict[str, object]) -> dict[str, object]:
            captured["tool"] = tool
            captured["arguments"] = arguments
            return {"status": "pass"}

        client.call = fake_call  # type: ignore[method-assign]
        result = client.sanitize_runtime_candidate(
            "unit",
            "blender/checkpoints/rigged.blend",
            "blender/checkpoints/weights_only.blend",
            weight_only=True,
            max_influences_per_vertex=2,
        )
        self.assertEqual(result, {"status": "pass"})
        self.assertEqual(captured["tool"], TOOL)
        self.assertEqual(
            captured["arguments"],
            {
                "job_id": "unit",
                "blend_rel": "blender/checkpoints/rigged.blend",
                "output_blend_rel": "blender/checkpoints/weights_only.blend",
                "target_height_m": None,
                "weight_only": True,
                "max_influences_per_vertex": 2,
            },
        )

    def test_worker_has_narrow_preservation_dispatch(self) -> None:
        source = (PIPELINE_ROOT / "adapter" / "blender_worker.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        function = next(
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "sanitize_runtime_candidate"
        )
        function_source = ast.unparse(function)
        self.assertIn("payload.get('weight_only', False)", function_source)
        self.assertIn("preserve_skeleton_metadata=weight_only", function_source)
        self.assertIn("max_influences_per_vertex=max_influences_per_vertex", function_source)
        self.assertIn("'policy': 'preserve_checkpoint_materials'", function_source)
        self.assertIn("else sanitize_working_materials()", function_source)
        self.assertIn("weight_only cleanup cannot be combined with target_height_m", function_source)

    def test_synthetic_blender_scene_preserves_every_non_weight_surface(self) -> None:
        config = json.loads(
            (PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8")
        )
        blender = Path(config["blender_executable"])
        integration = PIPELINE_ROOT / "tests" / "blender_weight_only_sanitize_integration.py"
        completed = subprocess.run(
            [str(blender), "--background", "--factory-startup", "--python", str(integration)],
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
