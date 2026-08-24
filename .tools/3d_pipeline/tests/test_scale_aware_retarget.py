"""Focused contract test for scale-aware hierarchy retargeting."""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]


class ScaleAwareRetargetTests(unittest.TestCase):
    def test_blender_integration_bounds_inverse_scale_retarget(self) -> None:
        config = json.loads(
            (PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8")
        )
        blender = Path(config["blender_executable"])
        integration = PIPELINE_ROOT / "tests" / "blender_scale_aware_retarget_integration.py"
        result = subprocess.run(
            [str(blender), "--background", "--factory-startup", "--python", str(integration)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=120,
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
        self.assertAlmostEqual(proof["location_scale"], 1.0, places=6)
        self.assertIn('"status": "pass"', result.stdout)


if __name__ == "__main__":
    unittest.main()
