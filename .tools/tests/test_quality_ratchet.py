"""Fixture tests for the quality ratchet in `.tools/quality.py`.

Synthetic ruff rows stand in for real output, so no linter runs.
Run from the mod root: `python -B .tools/tests/test_quality_ratchet.py`.
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import quality


def row(path, code, message, line=1):
	return {"filename": str(quality.REPO_ROOT / path), "code": code, "message": message, "location": {"row": line}}


class Ratchet(unittest.TestCase):
	def setUp(self):
		folder = tempfile.TemporaryDirectory(dir=quality.REPO_ROOT / ".tmp")
		self.addCleanup(folder.cleanup)
		self.relative = Path(folder.name).relative_to(quality.REPO_ROOT).as_posix()
		self.legacy = f"{self.relative}/legacy.py"
		(quality.REPO_ROOT / self.legacy).write_text("import os\n\ndef busy():\n    pass\n", encoding="utf-8")

	def levels(self, rows, baseline):
		findings, _ = quality.evaluate(rows, baseline)
		return [(f.rule, f.level) for f in findings]

	def test_recorded_defect_is_review_and_an_extra_copy_is_an_error(self):
		unused = row(self.legacy, "F401", "`os` imported but unused")
		baseline = {self.legacy: {"F401 `os` imported but unused": 1}}
		self.assertEqual(self.levels([unused], baseline), [("QUALITY-BASELINE", "review")])
		self.assertEqual(self.levels([unused, unused], baseline),
			[("QUALITY-BASELINE", "review"), ("QUALITY-RUFF", "error")])

	def test_complexity_may_shrink_but_not_grow(self):
		baseline = {self.legacy: {"C901 busy": 20}}
		self.assertEqual(self.levels([row(self.legacy, "C901", "`busy` is too complex (18 > 15)", 3)], baseline),
			[("QUALITY-BASELINE", "review")])
		self.assertEqual(self.levels([row(self.legacy, "C901", "`busy` is too complex (21 > 15)", 3)], baseline),
			[("QUALITY-COMPLEXITY", "error")])
		self.assertEqual(self.levels([row(self.legacy, "PLR0915", "Too many statements (60 > 50)", 3)], baseline),
			[("QUALITY-COMPLEXITY", "error")])

	def test_strict_files_never_use_the_baseline_for_defects(self):
		with mock.patch.object(quality, "STRICT_FILES", (self.relative + "/",)):
			unused = row(self.legacy, "F401", "`os` imported but unused")
			self.assertEqual(self.levels([unused], {self.legacy: {"F401 `os` imported but unused": 1}}),
				[("QUALITY-RUFF", "error")])


if __name__ == "__main__":
	unittest.main()
