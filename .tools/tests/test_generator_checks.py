"""Tests for the generator `--check` modes used by `.tools/check.py`.

The catalog exporter's check compares a fresh export with an output folder. These tests point it
at a temporary copy of the tracked CSV files, so nothing tracked is written.
Run from the mod root: `python -B .tools/tests/test_generator_checks.py`.
"""

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import export_event_catalog_csv as exporter

SPREADSHEETS = TOOLS.parent / "docs" / "spreadsheets"


class CatalogExportCheck(unittest.TestCase):
	def run_check(self, folder):
		output = io.StringIO()
		with contextlib.redirect_stdout(output):
			status = exporter.check_exports(exporter.DEFAULT_WORKBOOK, folder)
		return status, output.getvalue()

	def test_current_exports_pass_and_a_changed_cell_fails(self):
		with tempfile.TemporaryDirectory() as temporary:
			folder = Path(temporary)
			for name in exporter.SHEET_EXPORTS.values():
				shutil.copy2(SPREADSHEETS / name, folder / name)
			self.assertEqual(self.run_check(folder)[0], 0)

			clusters = folder / exporter.SHEET_EXPORTS["Clusters"]
			clusters.write_bytes(clusters.read_bytes().replace(b"Natural Disasters", b"Natural Disaster", 1))
			status, output = self.run_check(folder)
			self.assertEqual(status, 1)
			self.assertIn("Would update", output)
			self.assertIn(exporter.SHEET_EXPORTS["Clusters"], output)

	def test_missing_export_fails(self):
		with tempfile.TemporaryDirectory() as temporary:
			self.assertEqual(self.run_check(Path(temporary))[0], 1)


if __name__ == "__main__":
	unittest.main()
