"""Focused regression for saved humanoid normalization and PDX round-trip scale."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]
TARGET_HEIGHT = 7.351824


class PrepareScalePersistenceTests(unittest.TestCase):
    def test_humanoid_fbx_scale_survives_save_export_and_reimport(self) -> None:
        config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
        blender = Path(config["blender_executable"])
        integration = PIPELINE_ROOT / "tests" / "blender_prepare_scale_persistence_integration.py"
        result = subprocess.run(
            [str(blender), "--background", "--factory-startup", "--python", str(integration)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stdout + result.stderr)
        proof = next(
            json.loads(line)
            for line in result.stdout.splitlines()
            if line.startswith("{") and '"status"' in line
        )
        self.assertEqual(proof["status"], "pass")
        self.assertAlmostEqual(proof["persisted_height"], TARGET_HEIGHT, places=5)
        self.assertAlmostEqual(proof["reimported_height"], TARGET_HEIGHT, places=3)


if __name__ == "__main__":
    unittest.main()
