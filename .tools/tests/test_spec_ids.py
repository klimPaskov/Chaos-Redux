"""Fixture tests for `.tools/audits/audit_spec_ids.py`.

Run from the mod root: `python -B .tools/tests/test_spec_ids.py`.
"""

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS / "audits"))

import audit_spec_ids as spec_ids

FIXTURES = TOOLS / "tests" / "fixtures" / "spec_ids"
BROKEN_SPEC = "docs/specs/888_broken_specs/888_broken_spec_part_1_core.md"
BROKEN_PLAN = "docs/plans/888_broken_plans/888_broken_handoff.md"
WRONG_EVENT = "docs/specs/888_broken_specs/888_broken_spec_part_2_wrong_event.md"


def audit(name):
	return spec_ids.audit(FIXTURES / name)


def run_main(*arguments):
	"""Run the command line and return (exit code, printed text)."""
	output = io.StringIO()
	with contextlib.redirect_stdout(output):
		code = spec_ids.main([str(a) for a in arguments])
	return code, output.getvalue()


def write(root, relative, text):
	path = Path(root) / relative
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(text, encoding="utf-8", newline="\n")


class Fixtures(unittest.TestCase):
	def test_valid_fixture_is_clean_in_both_directions(self):
		findings, defined = audit("valid")
		self.assertEqual(findings, [])
		self.assertEqual(sorted(defined), [f"E777-S00{n}" for n in range(1, 7)])
		self.assertEqual({d.origin for d in defined.values()}, {"locked", "derived", "open"})

	def test_invalid_fixture_reports_every_rule_at_its_site(self):
		findings, _ = audit("invalid")
		found = [(f.path, f.line, f.rule, f.level) for f in spec_ids.select(findings, None)]
		self.assertEqual(found, [
			(BROKEN_PLAN, 4, "SPECID-UNKNOWN", "error"),
			(BROKEN_SPEC, 4, "SPECID-UNCITED", "review"),
			(BROKEN_SPEC, 5, "SPECID-ORIGIN", "error"),
			(BROKEN_SPEC, 6, "SPECID-ORIGIN", "error"),
			(BROKEN_SPEC, 7, "SPECID-DUPLICATE", "error"),
			(BROKEN_SPEC, 9, "SPECID-UNKNOWN", "error"),
			(WRONG_EVENT, 3, "SPECID-PACKAGE", "error"),
		])

	def test_unknown_citation_names_the_missing_id(self):
		findings, _ = audit("invalid")
		unknown = {spec_ids.MENTION.search(f.message).group(0) for f in findings if f.rule == "SPECID-UNKNOWN"}
		self.assertEqual(unknown, {"E888-S005", "E888-S099"})

	def test_package_without_ids_is_not_scanned_for_gaps(self):
		findings, defined = audit("legacy")
		self.assertEqual((findings, defined), ([], {}))


class Edges(unittest.TestCase):
	def test_no_packages_and_no_folders_are_clean(self):
		with tempfile.TemporaryDirectory() as folder:
			self.assertEqual(spec_ids.audit(Path(folder)), ([], {}))
			write(folder, "docs/plans/x/note.md", "No IDs here.\n")
			self.assertEqual(spec_ids.audit(Path(folder)), ([], {}))

	def test_citation_without_any_package_using_ids_is_unknown(self):
		with tempfile.TemporaryDirectory() as folder:
			write(folder, "docs/plans/x/note.md", "Implements E123-S001.\n")
			findings, defined = spec_ids.audit(Path(folder))
			self.assertEqual(defined, {})
			self.assertEqual([(f.rule, f.level, f.line) for f in findings], [("SPECID-UNKNOWN", "error", 1)])

	def test_system_package_without_an_event_number_cannot_define_ids(self):
		with tempfile.TemporaryDirectory() as folder:
			write(folder, "docs/specs/famine_system_specs/part.md", "- E102-S001 [locked] One.\n")
			findings, _ = spec_ids.audit(Path(folder))
			self.assertEqual([(f.rule, f.level) for f in findings if f.level == "error"], [("SPECID-PACKAGE", "error")])

	def test_ranges_are_not_expanded(self):
		with tempfile.TemporaryDirectory() as folder:
			write(folder, "docs/specs/123_x_specs/part.md",
				"- E123-S001 [locked] One.\n- E123-S002 [derived] Two.\n- E123-S003 [open] Three.\n")
			write(folder, "docs/plans/123_x_plans/h.md", "Implements E123-S001..S003.\n")
			findings, _ = spec_ids.audit(Path(folder))
			self.assertEqual([(f.rule, f.line) for f in spec_ids.select(findings, None)],
				[("SPECID-UNCITED", 2), ("SPECID-UNCITED", 3)])

	def test_a_spec_cross_reference_does_not_count_as_a_citation(self):
		with tempfile.TemporaryDirectory() as folder:
			write(folder, "docs/specs/123_x_specs/part.md",
				"- E123-S001 [locked] One.\n- E123-S002 [derived] Depends on E123-S001.\n")
			findings, _ = spec_ids.audit(Path(folder))
			self.assertEqual(sorted(f.line for f in findings if f.rule == "SPECID-UNCITED"), [1, 2])


class CommandLine(unittest.TestCase):
	def test_valid_tree_exits_zero(self):
		code, output = run_main("--root", FIXTURES / "valid")
		self.assertEqual(code, 0)
		self.assertIn("spec-ids: 6 spec items defined, 1 packages use IDs", output)
		self.assertIn("spec-ids: 0 error, 0 warning, 0 review", output)

	def test_invalid_tree_exits_one_unless_told_not_to(self):
		self.assertEqual(run_main("--root", FIXTURES / "invalid")[0], 1)
		self.assertEqual(run_main("--root", FIXTURES / "invalid", "--fail-on", "none")[0], 0)

	def test_empty_root_exits_zero_and_missing_root_exits_two(self):
		with tempfile.TemporaryDirectory() as folder:
			code, output = run_main("--root", folder)
			self.assertEqual(code, 0)
			self.assertIn("spec-ids: 0 spec items defined, 0 packages use IDs", output)
			missing = Path(folder) / "absent"
			stderr = io.StringIO()
			with contextlib.redirect_stderr(stderr):
				self.assertEqual(run_main("--root", missing)[0], 2)

	def test_json_report_uses_the_shared_contract_and_paths_filter(self):
		with tempfile.TemporaryDirectory() as folder:
			destination = Path(folder) / "report.json"
			code, _ = run_main("--root", FIXTURES / "invalid", "--json", destination, "--paths", BROKEN_PLAN)
			self.assertEqual(code, 1)
			payload = json.loads(destination.read_text(encoding="utf-8"))
			self.assertEqual([(r["rule"], r["level"], r["path"], r["line"]) for r in payload["findings"]],
				[("SPECID-UNKNOWN", "error", BROKEN_PLAN, 4)])
			self.assertEqual(payload["levels"]["SPECID-UNCITED"], "review")

	def test_paths_filter_hides_errors_outside_the_paths(self):
		code, output = run_main("--root", FIXTURES / "invalid", "--paths", "docs/specs/does_not_exist")
		self.assertEqual(code, 0)
		self.assertIn("spec-ids: 0 error, 0 warning, 0 review", output)


if __name__ == "__main__":
	unittest.main()
