"""Regression tests for the shared check contract in `.tools/lib/report.py` and `.tools/check.py`.

Each audit maps its finding categories onto error, warning and review levels. These tests seed
synthetic findings, so they prove the level, path-filter and exit-code decisions without scanning
the repository. Run from the mod root: `python -B .tools/tests/test_check_contract.py`.
"""

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import audit_asset_wiring_static as asset_audit
import audit_localisation_static as loc_audit
import audit_script_references_static as ref_audit
import check
from lib.report import Finding, exit_code, select, split_site


class LocalisationLevels(unittest.TestCase):
	def test_missing_bom_is_an_error(self):
		findings = loc_audit.Findings()
		findings.missing_bom.append("localisation\\english\\x_l_english.yml")
		rows = loc_audit.normalised_findings(findings)
		self.assertEqual([(r.rule, r.level, r.path) for r in rows], [("LOC-BOM", "error", "localisation/english/x_l_english.yml")])
		self.assertEqual(exit_code(rows, "error"), 1)
		self.assertEqual(exit_code(rows, "none"), 0)

	def test_review_candidates_never_fail(self):
		findings = loc_audit.Findings()
		findings.dead_keys.append(("unused_key", "localisation/english/x_l_english.yml"))
		findings.expanded_triggers.append("some_trigger")
		self.assertEqual(exit_code(loc_audit.normalised_findings(findings), "error"), 0)

	def test_ordinal_suffix_is_an_encoding_error(self):
		findings = loc_audit.Findings()
		findings.encoding_artifacts.append(("localisation/english/x_l_english.yml", 4, "ordinal suffix on key_a"))
		rows = loc_audit.normalised_findings(findings)
		self.assertEqual((rows[0].rule, rows[0].level, rows[0].line), ("LOC-ENCODING", "error", 4))


class AssetLevels(unittest.TestCase):
	def test_missing_file_is_an_error_and_dead_registration_is_not(self):
		findings = asset_audit.Findings()
		findings.missing_files.append({"file": "interface\\x.gfx", "reference": "gfx/interface/x.dds"})
		findings.dead_definitions.append({"name": "GFX_unused", "definitions": ["interface/x.gfx"], "count": 1})
		rows = asset_audit.normalised_findings(findings)
		self.assertEqual(sorted((r.rule, r.level) for r in rows), [("GFX-DEAD-REGISTRATION", "review"), ("GFX-MISSING-FILE", "error")])
		self.assertEqual(exit_code(rows, "error"), 1)
		self.assertEqual(exit_code([r for r in rows if r.level == "review"], "error"), 0)


class ReferenceLevels(unittest.TestCase):
	def test_reference_audit_has_no_errors(self):
		result = {"flags": {"checked_never_set": [{"flag": "f", "files": ["common/a.txt"]}], "set_never_checked": []}}
		rows = ref_audit.normalised_findings(result)
		self.assertEqual([(r.rule, r.level) for r in rows], [("REF-FLAG-NEVER-SET", "warning")])
		self.assertEqual(exit_code(rows, "error"), 0)


class PathSelection(unittest.TestCase):
	def rows(self):
		return [
			Finding("c", "R", "error", "localisation/english/b.yml", 2, "b"),
			Finding("c", "R", "error", "events/a.txt", 9, "a"),
			Finding("c", "R", "error", "", 0, "unlocated"),
		]

	def test_paths_keep_files_and_folders_and_drop_unlocated_findings(self):
		self.assertEqual([r.path for r in select(self.rows(), ["events/a.txt"])], ["events/a.txt"])
		self.assertEqual([r.path for r in select(self.rows(), ["localisation"])], ["localisation/english/b.yml"])
		self.assertEqual(len(select(self.rows(), None)), 3)

	def test_order_is_stable(self):
		self.assertEqual([r.path for r in select(self.rows(), None)], ["", "events/a.txt", "localisation/english/b.yml"])

	def test_split_site(self):
		self.assertEqual(split_site("common\\decisions\\x.txt:12"), ("common/decisions/x.txt", 12))
		self.assertEqual(split_site("common/decisions/x.txt"), ("common/decisions/x.txt", 0))


class QuickSelection(unittest.TestCase):
	def names(self, paths):
		return [c.name for c in check.selected_checks("quick", paths, None)]

	def test_localisation_change_runs_text_checks(self):
		self.assertEqual(self.names(["localisation/english/x_l_english.yml"]), ["localisation", "asset-wiring", "parchment"])

	def test_skill_change_runs_guidance_and_agent_mirror_checks(self):
		self.assertEqual(self.names([".claude/skills/x/SKILL.md"]), ["guidance", "generators", "quality"])

	def test_unrelated_change_runs_nothing(self):
		self.assertEqual(self.names(["README.md", "docs/plans/x.md"]), [])

	def test_sound_change_runs_runtime_binary_checks(self):
		self.assertEqual(self.names(["sound/x.wav"]), ["gfx"])

	def test_tool_change_runs_tests(self):
		self.assertIn("tests", self.names([".tools/lib/report.py"]))

	def test_full_runs_every_check_except_changed_file_validation(self):
		names = [c.name for c in check.selected_checks("full", [], None)]
		self.assertEqual(len(names), len(check.CHECKS) - len(check.QUICK_ONLY))
		self.assertNotIn("script-validate", names)

	def test_script_change_runs_syntax_and_mcp_validation(self):
		names = self.names(["events/x.txt"])
		self.assertIn("script-rules", names)
		self.assertIn("script-validate", names)


if __name__ == "__main__":
	unittest.main()
