"""Regression tests for `.tools/sync/refresh_kit_3d.py`, which pins the kit's 3D unit tools in `.tools/kit_3d/`.

Every test builds a small kit repository and mod root in a temporary folder, so nothing tracked is written. The
last class checks the real snapshot. Run from the mod root: `python -B .tools/tests/test_kit_3d.py`.
"""

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS / "sync"))

import refresh_kit_3d

ENVIRONMENT = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.test",
	GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.test")
TOOL = "print('check')\r\n"


def write(path, data):
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)


def git(repository, *command):
	return subprocess.run(["git", "-C", str(repository), *command], check=True, capture_output=True, text=True, env=ENVIRONMENT).stdout


class KitSnapshotCase(unittest.TestCase):
	def setUp(self):
		self.temporary = tempfile.TemporaryDirectory()
		self.addCleanup(self.temporary.cleanup)
		self.root = Path(self.temporary.name) / "mod"
		self.kit = Path(self.temporary.name) / "kit"
		write(self.kit / ".tools/3d_pipeline/check_unit_files.py", TOOL)
		write(self.kit / ".tools/3d_pipeline/lib/pdx_deform.py", "x = 1\n")
		write(self.kit / ".tools/3d_pipeline/config/unit_types.json", "{}\n")
		write(self.kit / ".tools/3d_pipeline/run_pilot.py", "not listed\n")
		git(self.kit, "init", "-q")
		git(self.kit, "add", "-A")
		git(self.kit, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "kit")
		write(self.root / ".tools/kit_3d/mapping.json", json.dumps({"files": ["check_unit_files.py", "config/unit_types.json", "lib/pdx_deform.py"]}))

	def run_tool(self, *arguments):
		output = io.StringIO()
		with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
			status = refresh_kit_3d.main(["--root", str(self.root), *arguments])
		return status, output.getvalue()

	def test_refresh_copies_only_listed_files_with_lf_and_records_the_commit(self):
		status, output = self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		self.assertEqual(status, 0, output)
		snapshot = self.root / ".tools/kit_3d"
		self.assertEqual((snapshot / "check_unit_files.py").read_bytes(), b"print('check')\n")
		self.assertFalse((snapshot / "run_pilot.py").exists())
		manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
		self.assertEqual(manifest["kit_commit"], git(self.kit, "rev-parse", "HEAD").strip())
		self.assertEqual(sorted(manifest["files"]), ["check_unit_files.py", "config/unit_types.json", "lib/pdx_deform.py"])
		self.assertEqual(self.run_tool("--check")[0], 0)

	def test_check_refuses_edits_extra_files_and_missing_files(self):
		self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		snapshot = self.root / ".tools/kit_3d"
		write(snapshot / "lib/pdx_deform.py", "x = 2\n")
		status, output = self.run_tool("--check")
		self.assertEqual(status, 1)
		self.assertIn("lib/pdx_deform.py: edited", output)
		write(snapshot / "lib/local_helper.py", "y = 1\n")
		self.assertIn("lib/local_helper.py: not in the snapshot", self.run_tool("--check")[1])
		(snapshot / "check_unit_files.py").unlink()
		self.assertIn("check_unit_files.py: missing", self.run_tool("--check")[1])

	def test_a_crlf_checkout_keeps_its_digest(self):
		self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		path = self.root / ".tools/kit_3d/check_unit_files.py"
		path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
		self.assertEqual(self.run_tool("--check")[0], 0)

	def test_refresh_removes_files_dropped_from_the_mapping(self):
		self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		write(self.root / ".tools/kit_3d/mapping.json", json.dumps({"files": ["check_unit_files.py"]}))
		self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		self.assertFalse((self.root / ".tools/kit_3d/lib/pdx_deform.py").exists())
		self.assertEqual(self.run_tool("--check")[0], 0)

	def test_a_path_outside_the_pipeline_is_refused(self):
		write(self.root / ".tools/kit_3d/mapping.json", json.dumps({"files": ["../check.py"]}))
		status, output = self.run_tool("--kit", str(self.kit), "--commit", "HEAD")
		self.assertEqual(status, 2)
		self.assertIn("kit-relative", output)


class RealSnapshot(unittest.TestCase):
	def test_the_committed_snapshot_matches_its_manifest(self):
		root = TOOLS.parent
		if not (root / ".tools/kit_3d/manifest.json").exists():
			self.skipTest("no kit_3d snapshot yet")
		self.assertEqual(refresh_kit_3d.check(root), [])


if __name__ == "__main__":
	unittest.main()
