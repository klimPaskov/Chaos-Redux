#!/usr/bin/env python3
"""Indentation checks and explicit fixers for Chaos Redux script files (CLAUDE.md section 1, rule 1).

Two rules, both reported at `warning` level under the `.tools/lib/report.py` contract, one finding
per file and rule:

- `INDENT-SPACES`: lines indented with four or more leading spaces instead of tabs, in `.txt`,
  `.gui`, `.gfx` and `.asset` files under `common/`, `events/`, `interface/`, `history/`, `map/`
  and `localisation/`.
- `INDENT-DEPTH`: lines whose leading tabs differ from their brace depth, in `.txt` files under
  `common/`, `events/` and `history/`. Braces inside quoted strings and after `#` are ignored, and
  a closing brace belongs to the depth of the block it closes.

The checks are read-only. The fixers are separate and explicit:

	python -B .tools/audits/indentation.py                          # report (default)
	python -B .tools/audits/indentation.py --paths events/x.txt     # report for selected files
	python -B .tools/audits/indentation.py --apply-tabs --paths events/x.txt
	python -B .tools/audits/indentation.py --apply-depth --paths events/x.txt

`--apply-tabs` rewrites only the leading space run (one tab per four spaces, keeping any
remainder) and leaves lines that already start with a tab alone. `--apply-depth` rewrites drifted
lines to one tab per structural level, except lines that mix spaces after tabs, whose intended
alignment is ambiguous. Both keep each file's line endings and UTF-8 BOM state. Because drift is a
warning, the report never fails; run a fixer only on files you own.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # .tools, for the shared lib package
from lib.report import Finding, PathFilter, add_arguments, exit_code, merge_json, print_findings, requested_paths

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECK = "indentation"
LEVELS = {"INDENT-SPACES": "warning", "INDENT-DEPTH": "warning"}
SPACE_SCAN = (("common", "events", "interface", "history", "map", "localisation"), {".txt", ".gui", ".gfx", ".asset"})
DEPTH_SCAN = (("common", "events", "history"), {".txt"})
BOM = b"\xef\xbb\xbf"


def decode(path: Path) -> Optional[Tuple[bool, str]]:
	"""Return (has_bom, text) for a UTF-8 file, or None when it is not UTF-8."""
	raw = path.read_bytes()
	has_bom = raw.startswith(BOM)
	try:
		return has_bom, (raw[3:] if has_bom else raw).decode("utf-8")
	except UnicodeDecodeError:
		return None


def write(path: Path, has_bom: bool, decoded: str, lines: List[str]) -> None:
	"""Write lines back with the file's dominant line ending and its BOM state."""
	crlf = decoded.count("\r\n")
	newline = "\r\n" if crlf > decoded.count("\n") - crlf else "\n"
	body = newline.join(lines)
	if decoded.endswith(("\n", "\r")):
		body += newline
	path.write_bytes((BOM if has_bom else b"") + body.encode("utf-8"))


def leading_space_run(line: str) -> int:
	"""Return the length of the leading run of spaces, or 0 if none."""
	count = 0
	for character in line:
		if character == " ":
			count += 1
		else:
			break
	return count


def convert_line(line: str) -> str:
	"""Convert a line's leading spaces to tabs, preserving any remainder."""
	run = leading_space_run(line)
	if run < 4:
		return line
	# A leading tab means the file is already tab-indented on this line.
	if line[:1] == "\t":
		return line
	tabs, remainder = divmod(run, 4)
	if tabs == 0:
		return line
	return "\t" * tabs + " " * remainder + line[run:]


def scan_line(line: str, depth: int) -> Tuple[int, int]:
	"""Return (depth_at_line_start, depth_after_the_line), ignoring quoted and commented braces."""
	start_depth = depth
	in_string = False
	escaped = False
	for character in line:
		if in_string:
			if escaped:
				escaped = False
			elif character == "\\":
				escaped = True
			elif character == '"':
				in_string = False
			continue
		if character == '"':
			in_string = True
		elif character == "#":
			break
		elif character == "{":
			depth += 1
		elif character == "}":
			depth -= 1
	return start_depth, depth


def depth_lines(decoded: str) -> List[Tuple[int, int, str]]:
	"""Return [(line_number, expected_depth, line)] for every line whose indentation drifts."""
	depth = 0
	drifted: List[Tuple[int, int, str]] = []
	for number, line in enumerate(decoded.splitlines(), start=1):
		stripped = line.strip()
		# A closing brace belongs to the depth of the block it closes.
		expected = max(0, depth - 1 if stripped.startswith("}") else depth)
		if stripped and not stripped.startswith("#"):
			leading = line[: len(line) - len(line.lstrip("\t "))]
			if leading != "\t" * expected:
				drifted.append((number, expected, line))
		_, depth = scan_line(line, depth)
	return drifted


def files(scan: Tuple[Sequence[str], Set[str]], paths: Optional[List[str]]) -> List[Path]:
	folders, suffixes = scan
	selector = PathFilter(paths)
	found = []
	for folder in folders:
		base = REPO_ROOT / folder
		if base.is_dir():
			found += [p for p in base.rglob("*") if p.is_file() and p.suffix.lower() in suffixes
				and selector.matches(p.relative_to(REPO_ROOT).as_posix())]
	return sorted(found)


def check(paths: Optional[List[str]]) -> List[Finding]:
	findings = []
	for path in files(SPACE_SCAN, paths):
		content = decode(path)
		if content is None:
			continue
		lines = content[1].splitlines()
		changed = [n for n, line in enumerate(lines, 1) if convert_line(line) != line]
		if changed:
			findings.append(Finding(CHECK, "INDENT-SPACES", "warning", path.relative_to(REPO_ROOT).as_posix(), changed[0],
				f"{len(changed)} of {len(lines)} lines are indented with spaces instead of tabs"))
	for path in files(DEPTH_SCAN, paths):
		content = decode(path)
		if content is None:
			continue
		drifted = depth_lines(content[1])
		if drifted:
			findings.append(Finding(CHECK, "INDENT-DEPTH", "warning", path.relative_to(REPO_ROOT).as_posix(), drifted[0][0],
				f"{len(drifted)} of {len(content[1].splitlines())} lines do not match their brace depth"))
	return sorted(findings, key=lambda f: (f.path, f.line, f.rule))


def apply_tabs(path: Path) -> int:
	content = decode(path)
	if content is None:
		return 0
	lines = content[1].splitlines()
	output = [convert_line(line) for line in lines]
	changed = sum(a != b for a, b in zip(lines, output))
	if changed:
		write(path, content[0], content[1], output)
	return changed


def apply_depth(path: Path) -> int:
	content = decode(path)
	if content is None:
		return 0
	lines = content[1].splitlines()
	output = list(lines)
	for number, expected, line in depth_lines(content[1]):
		leading = line[: len(line) - len(line.lstrip("\t "))]
		if " " not in leading or not leading.startswith("\t"):
			output[number - 1] = "\t" * expected + line.strip()
	changed = sum(a != b for a, b in zip(lines, output))
	if changed:
		write(path, content[0], content[1], output)
	return changed


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
	parser.add_argument("--json", type=Path, help="also write the findings as JSON")
	fixers = parser.add_mutually_exclusive_group()
	fixers.add_argument("--apply-tabs", action="store_true", help="rewrite leading spaces as tabs in the selected files")
	fixers.add_argument("--apply-depth", action="store_true", help="re-indent drifted lines to their brace depth in the selected files")
	add_arguments(parser)
	arguments = parser.parse_args()
	paths = requested_paths(arguments)
	if arguments.apply_tabs or arguments.apply_depth:
		if not paths:
			parser.error("a fixer needs --paths or --paths-from; it never rewrites the whole repository")
		scan, fixer = (SPACE_SCAN, apply_tabs) if arguments.apply_tabs else (DEPTH_SCAN, apply_depth)
		counts: Dict[str, int] = {p.relative_to(REPO_ROOT).as_posix(): fixer(p) for p in files(scan, paths)}
		for path, changed in sorted(counts.items()):
			if changed:
				print(f"rewrote {changed} lines in {path}")
		print(f"{CHECK}: rewrote {sum(counts.values())} lines in {sum(1 for c in counts.values() if c)} files")
		return 0
	findings = check(paths)
	print_findings(CHECK, findings)
	if arguments.json:
		merge_json(arguments.json, findings, LEVELS)
	return exit_code(findings, arguments.fail_on)


if __name__ == "__main__":
	raise SystemExit(main())
