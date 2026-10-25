#!/usr/bin/env python3
"""Single read-only entry point for the Chaos Redux repository checks.

	python -B .tools/check.py quick                      # changed and untracked paths from git
	python -B .tools/check.py quick --paths events/x.txt localisation/english/x.yml
	python -B .tools/check.py full                       # whole repository
	python -B .tools/check.py full --json .tmp/checks/full.json

`quick` runs only the checks whose inputs the changed paths can affect and reports only
findings located in those paths. `full` runs every check over the whole repository. Both print
errors one per line (`path:line: level RULE message`), then one summary line per check;
`quick` and `--verbose` also print warnings. Review candidates are counted on the console and
listed only in the `--json` report.

Exit codes: 0 no errors, 1 errors found, 2 a check could not run or the arguments were invalid.
The command never edits tracked files; the checks it starts write only to `.tmp/` and to the
`--json` destination. Fixers such as `reindent_script_files.py --apply` are never run here.

Checks (rule ids and levels are defined by each tool; see `.tools/lib/report.py`):

- localisation   `audit_localisation_static.py`        localisation integrity and key wiring
- asset-wiring   `audit_asset_wiring_static.py`        sprite, texture and implicit GFX lookups
- parchment      `report_colour_audit.py`              colour codes in parchment report text
- guidance       `sync/sync_read_limits.py --check`    guidance size ceilings and read-limit drift
- tests          maintained regression tests in `.tools/` (full, or quick when `.tools/` changed)
- references     `audit_script_references_static.py`   dead code, flags and clones (full only; review)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Callable, Dict, List, NamedTuple, Optional, Sequence, Tuple

from lib.report import LEVELS, Finding, PathFilter, format_finding, relative, to_json

REPO_ROOT = Path(__file__).resolve().parents[1]
TOOLS = REPO_ROOT / ".tools"
TEST_TIMEOUT_SECONDS = 600
AUDIT_TIMEOUT_SECONDS = 900

# Maintained tests that need arguments; every other discovered test runs bare.
TEST_ARGUMENTS: Dict[str, List[str]] = {
	".tools/audit_event6_flags.py": ["--strict"],
	".tools/validation/validate_028_availability.py": [
		"--fixture", "docs/plans/028_asteroid_incoming_plans/availability_20261003/source_scenarios.json",
	],
}
TEST_PATTERNS = (
	".tools/test_*.py",
	".tools/gfx/test_*.py",
	".tools/audit_event6_*.py",
	".tools/check_planning_identifiers.py",
	".tools/validation/validate_*.py",
	".tools/validation/test_*.js",
	".tools/tests/test_*.py",
	".tools/tests/*.js",
)


class Check(NamedTuple):
	name: str
	inputs: Tuple[str, ...]  # path prefixes whose change makes `quick` run the check
	quick: bool
	run: Callable[[Optional[List[str]]], Tuple[List[Finding], Optional[str]]]


def run_report_tool(name: str, script: str, extra: Sequence[str] = ()) -> Callable:
	"""Run a tool that writes the shared `findings` JSON and return its findings."""

	def runner(paths: Optional[List[str]]) -> Tuple[List[Finding], Optional[str]]:
		with tempfile.TemporaryDirectory(prefix="chaosx_check_") as folder:
			destination = Path(folder) / "report.json"
			command = [sys.executable, "-B", str(TOOLS / script), "--json", str(destination), "--fail-on", "none", *extra]
			if paths:
				# A path list can exceed the Windows command-line limit, so it travels in a file.
				listing = Path(folder) / "paths.txt"
				listing.write_text("\n".join(paths), encoding="utf-8")
				command += ["--paths-from", str(listing)]
			try:
				completed = subprocess.run(command, cwd=REPO_ROOT, capture_output=True, text=True,
					encoding="utf-8", errors="replace", timeout=AUDIT_TIMEOUT_SECONDS)
			except subprocess.TimeoutExpired:
				return [], f"{script} timed out after {AUDIT_TIMEOUT_SECONDS} s"
			if completed.returncode != 0 or not destination.exists():
				tail = (completed.stderr or completed.stdout).strip().splitlines()[-3:]
				return [], f"{script} exited {completed.returncode}: {' | '.join(tail)}"
			payload = json.loads(destination.read_text(encoding="utf-8"))
		return [Finding(**row) for row in payload.get("findings", [])], None

	return runner


def run_guidance(paths: Optional[List[str]]) -> Tuple[List[Finding], Optional[str]]:
	"""Map `sync_read_limits.py --check` output onto findings."""
	completed = subprocess.run([sys.executable, "-B", str(TOOLS / "sync" / "sync_read_limits.py"), "--check"],
		cwd=REPO_ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
	findings = []
	for line in completed.stdout.splitlines():
		over = re.match(r"Over budget: (.+) is (\d+) bytes, ceiling (\d+)", line)
		drift = re.match(r"Would update (.+)", line)
		if over:
			findings.append(Finding("guidance", "GUIDE-SIZE", "error", relative(over.group(1)), 0,
				f"{over.group(2)} bytes exceeds the {over.group(3)}-byte ceiling in .tools/sync/read_limits.json"))
		elif drift:
			findings.append(Finding("guidance", "GUIDE-READ-LIMITS", "error", relative(drift.group(1)), 0,
				"read limits differ from .tools/sync/read_limits.json; run python .tools/sync/sync_read_limits.py"))
	if completed.returncode not in (0, 1) or (completed.returncode == 1 and not findings):
		tail = (completed.stderr or completed.stdout).strip().splitlines()[-3:]
		return findings, f"sync_read_limits.py exited {completed.returncode}: {' | '.join(tail)}"
	return findings, None


def discover_tests() -> List[str]:
	found = set()
	for pattern in TEST_PATTERNS:
		found.update(path.relative_to(REPO_ROOT).as_posix() for path in REPO_ROOT.glob(pattern) if path.is_file())
	return sorted(found)


def run_one_test(test: str) -> Optional[Finding]:
	interpreter = ["node"] if test.endswith(".js") else [sys.executable, "-B"]
	command = [*interpreter, test, *TEST_ARGUMENTS.get(test, [])]
	try:
		completed = subprocess.run(command, cwd=REPO_ROOT, capture_output=True, text=True,
			encoding="utf-8", errors="replace", timeout=TEST_TIMEOUT_SECONDS)
	except subprocess.TimeoutExpired:
		return Finding("tests", "TEST-TIMEOUT", "error", test, 0, f"did not finish within {TEST_TIMEOUT_SECONDS} s")
	if completed.returncode == 0:
		return None
	lines = [line for line in (completed.stderr + completed.stdout).strip().splitlines() if line.strip()]
	return Finding("tests", "TEST-FAILED", "error", test, 0, f"exit {completed.returncode}: {lines[-1].strip() if lines else 'no output'}")


def run_tests(paths: Optional[List[str]]) -> Tuple[List[Finding], Optional[str]]:
	tests = discover_tests()
	with ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 2)) as pool:
		results = list(pool.map(run_one_test, tests))
	return [finding for finding in results if finding], None


CHECKS = (
	Check("localisation", ("localisation/", "events/", "common/", "interface/", "history/", "map/"), True,
		run_report_tool("localisation", "audit_localisation_static.py")),
	Check("asset-wiring", ("gfx/", "interface/", "common/", "events/", "history/", "localisation/"), True,
		run_report_tool("asset-wiring", "audit_asset_wiring_static.py")),
	Check("parchment", ("events/", "localisation/", "common/scripted_localisation/"), True,
		run_report_tool("parchment", "report_colour_audit.py")),
	Check("guidance", ("CLAUDE.md", "AGENTS.md", ".claude/", ".codex/", ".opencode/", ".tools/sync/"), True,
		run_guidance),
	Check("tests", (".tools/",), True, run_tests),
	Check("references", (), False, run_report_tool("references", "audit_script_references_static.py")),
)


def changed_paths() -> List[str]:
	"""Return changed, staged and untracked paths reported by git."""
	completed = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "-z"], cwd=REPO_ROOT,
		capture_output=True, check=True)
	paths = []
	entries = completed.stdout.decode("utf-8", errors="replace").split("\0")
	index = 0
	while index < len(entries):
		entry = entries[index]
		index += 1
		if len(entry) < 4:
			continue
		paths.append(entry[3:])
		if entry[0] in "RC":
			index += 1  # the rename source follows as its own entry
	return sorted(set(paths))


def selected_checks(mode: str, paths: Sequence[str], only: Optional[Sequence[str]]) -> List[Check]:
	chosen = []
	for check in CHECKS:
		if only and check.name not in only:
			continue
		if mode == "full":
			chosen.append(check)
		elif check.quick and any(PathFilter(check.inputs).matches(path) for path in paths):
			chosen.append(check)
	return chosen


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
	parser.add_argument("mode", choices=("quick", "full"))
	parser.add_argument("--paths", nargs="+", metavar="PATH", help="quick: check these paths instead of the git changes")
	parser.add_argument("--only", nargs="+", choices=[check.name for check in CHECKS], help="run only these checks")
	parser.add_argument("--json", type=Path, help="write every finding, including review candidates, to this file")
	parser.add_argument("--verbose", action="store_true", help="also print warnings in full mode")
	arguments = parser.parse_args()

	if arguments.mode == "quick":
		paths = [relative(path) for path in arguments.paths] if arguments.paths else changed_paths()
		if not paths:
			print("quick: no changed paths")
			return 0
	else:
		if arguments.paths:
			parser.error("--paths applies to quick mode only")
		paths = []
	checks = selected_checks(arguments.mode, paths, arguments.only)
	if not checks:
		print(f"quick: no check reads the {len(paths)} changed path(s)")
		return 0

	report_paths = paths or None

	def run_check(check: Check) -> Tuple[List[Finding], Optional[str]]:
		try:
			return check.run(None if check.name == "tests" else report_paths)
		except Exception as error:  # a crashing check is reported as "could not run" (exit 2)
			return [], f"{type(error).__name__}: {error}"

	with ThreadPoolExecutor(max_workers=len(checks)) as pool:
		outcomes = list(pool.map(run_check, checks))

	all_findings: List[Finding] = []
	failures: List[str] = []
	# Tests and guidance limits are repository-wide contracts, so their findings are never path-filtered.
	for check, (findings, failure) in zip(checks, outcomes):
		all_findings.extend(findings)
		if failure:
			failures.append(f"{check.name}: could not run: {failure}")

	shown = ("error", "warning") if arguments.mode == "quick" or arguments.verbose else ("error",)
	for finding in sorted(all_findings, key=lambda f: (f.path, f.line, f.rule, f.message)):
		if finding.level in shown:
			print(format_finding(finding))
	for check, (findings, _) in zip(checks, outcomes):
		counts = {level: sum(1 for f in findings if f.level == level) for level in LEVELS}
		print(f"{check.name}: " + ", ".join(f"{counts[level]} {level}" for level in LEVELS))
	for failure in failures:
		print(failure)

	if arguments.json:
		arguments.json.parent.mkdir(parents=True, exist_ok=True)
		arguments.json.write_text(json.dumps({
			"mode": arguments.mode,
			"paths": paths,
			"checks": [check.name for check in checks],
			"failures": failures,
			"findings": to_json(sorted(all_findings, key=lambda f: (f.check, f.path, f.line, f.rule, f.message))),
		}, indent=2, sort_keys=True), encoding="utf-8")
	if failures:
		return 2
	return 1 if any(finding.level == "error" for finding in all_findings) else 0


if __name__ == "__main__":
	raise SystemExit(main())
