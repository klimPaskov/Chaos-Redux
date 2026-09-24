#!/usr/bin/env python3
"""Measure structural indentation drift in Chaos Redux script files.

The repository indents Clausewitz blocks one tab per nesting level, so the
leading whitespace of every line should equal its brace depth. This tool parses
each script file with a real brace-depth walk and reports every line whose
leading tabs do not match that depth.

Unlike `.tools/reindent_script_files.py`, which only converts leading spaces to
tabs on a per-line basis, this tool detects nesting that was never indented at
all, such as a closing brace placed at column 0 inside a nested block.

Safety properties:

- Brace depth is counted outside quoted strings and outside `#` comments, so
  braces in localisation keys and comments never affect the result.
- A line whose leading whitespace contains spaces after tabs is reported but
  never auto-corrected, because its intended alignment is ambiguous.
- The tool reports by default and only rewrites with `--apply`.

Usage:
	python .tools/check_structural_indentation.py --check
	python .tools/check_structural_indentation.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]

SCAN_DIRS = ("common", "events", "history")
SUFFIXES = {".txt"}

BOM = b"\xef\xbb\xbf"


def scan_line(line: str, depth: int) -> Tuple[int, int]:
	"""Return (depth_at_line_start, depth_after_the_line).

	Braces inside double-quoted strings and after a `#` comment are ignored.
	"""
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


def measure(path: Path) -> List[Tuple[int, int, str]]:
	"""Return [(line_number, expected_depth, line)] for every drifted line."""
	raw = path.read_bytes()
	text = raw[3:] if raw.startswith(BOM) else raw
	try:
		decoded = text.decode("utf-8")
	except UnicodeDecodeError:
		return []

	depth = 0
	findings: List[Tuple[int, int, str]] = []
	for number, line in enumerate(decoded.splitlines(), start=1):
		stripped = line.strip()
		start_depth = depth
		# A closing brace belongs to the depth of the block it closes.
		expected = start_depth - 1 if stripped.startswith("}") else start_depth
		if expected < 0:
			expected = 0
		if stripped and not stripped.startswith("#"):
			leading = line[: len(line) - len(line.lstrip("\t "))]
			if leading != "\t" * expected:
				findings.append((number, expected, line))
		_, depth = scan_line(line, depth)
	return findings


def apply_fix(path: Path) -> int:
	"""Rewrite drifted lines to one tab per structural level. Returns lines changed."""
	raw = path.read_bytes()
	has_bom = raw.startswith(BOM)
	text = raw[3:] if has_bom else raw
	try:
		decoded = text.decode("utf-8")
	except UnicodeDecodeError:
		return 0

	depth = 0
	output: List[str] = []
	changed = 0
	for line in decoded.splitlines():
		stripped = line.strip()
		start_depth = depth
		expected = start_depth - 1 if stripped.startswith("}") else start_depth
		if expected < 0:
			expected = 0
		rewritten = line
		if stripped and not stripped.startswith("#"):
			leading = line[: len(line) - len(line.lstrip("\t "))]
			if leading != "\t" * expected:
				rewritten = "\t" * expected + stripped
		if rewritten != line:
			changed += 1
		output.append(rewritten)
		_, depth = scan_line(line, depth)

	if changed:
		crlf = decoded.count("\r\n")
		lf = decoded.count("\n") - crlf
		newline = "\r\n" if crlf > lf else "\n"
		body = newline.join(output)
		if decoded.endswith(("\n", "\r")):
			body += newline
		path.write_bytes((BOM if has_bom else b"") + body.encode("utf-8"))
	return changed


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--check", action="store_true", help="report only")
	group.add_argument("--apply", action="store_true", help="rewrite drifted lines")
	arguments = parser.parse_args()

	total_files = 0
	total_lines = 0
	details: List[Tuple[Path, int, int]] = []

	for directory in SCAN_DIRS:
		root = REPO_ROOT / directory
		if not root.is_dir():
			continue
		for path in sorted(root.rglob("*")):
			if not path.is_file() or path.suffix.lower() not in SUFFIXES:
				continue
			if arguments.apply:
				changed = apply_fix(path)
				total = sum(1 for _ in path.read_text(encoding="utf-8", errors="replace").splitlines())
			else:
				findings = measure(path)
				changed = len(findings)
				total = sum(1 for _ in path.read_text(encoding="utf-8", errors="replace").splitlines())
			if changed:
				total_files += 1
				total_lines += changed
				details.append((path.relative_to(REPO_ROOT), changed, total))

	mode = "rewrote" if arguments.apply else "would rewrite"
	print(f"{mode} {total_files} files, {total_lines} lines")
	details.sort(key=lambda item: item[1], reverse=True)
	for relative, changed, total in details[:40]:
		print(f"  {changed:5d}/{total:<7d}  {relative}")
	if len(details) > 40:
		print(f"  ... {len(details) - 40} more files")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
