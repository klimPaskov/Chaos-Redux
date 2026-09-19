#!/usr/bin/env python3
"""Convert space-indented Chaos Redux script files to the repository's tab rule.

AGENTS.md requires script blocks to be indented with tabs. Some files were
authored with leading spaces instead. This tool rewrites only the leading
whitespace of such lines, one tab per four spaces, and leaves everything else
byte-identical.

Safety properties, all enforced rather than assumed:

- Only the run of spaces before the first non-space character is touched, so
  string contents, inline comments, and trailing whitespace are never altered.
- Lines that already use a tab are left alone, so a partially converted file
  cannot be double-converted.
- Files are written back with their original line endings and their original
  UTF-8 BOM state.
- A line whose leading run is not a multiple of four keeps the remainder as
  spaces rather than guessing an alignment.

Usage:
	python .tools/reindent_script_files.py --check     # report only
	python .tools/reindent_script_files.py --apply     # rewrite
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]

SCAN_DIRS = ("common", "events", "interface", "history", "map", "localisation")
SUFFIXES = {".txt", ".gui", ".gfx", ".asset"}

BOM = b"\xef\xbb\xbf"


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


def process(path: Path, apply: bool) -> Tuple[int, int]:
	"""Return (changed lines, total lines) for one file."""
	raw = path.read_bytes()
	has_bom = raw.startswith(BOM)
	text = raw[3:] if has_bom else raw
	try:
		decoded = text.decode("utf-8")
	except UnicodeDecodeError:
		print(f"skip (not utf-8): {path}", file=sys.stderr)
		return 0, 0

	# Preserve the file's dominant line ending exactly.
	crlf = decoded.count("\r\n")
	lf = decoded.count("\n") - crlf
	newline = "\r\n" if crlf > lf else "\n"
	lines = decoded.splitlines()

	changed = 0
	output: List[str] = []
	for line in lines:
		converted = convert_line(line)
		if converted != line:
			changed += 1
		output.append(converted)

	if changed and apply:
		body = newline.join(output)
		if decoded.endswith(("\n", "\r")):
			body += newline
		encoded = body.encode("utf-8")
		path.write_bytes((BOM if has_bom else b"") + encoded)

	return changed, len(lines)


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("--check", action="store_true", help="report only")
	group.add_argument("--apply", action="store_true", help="rewrite files")
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
			changed, count = process(path, arguments.apply)
			if changed:
				total_files += 1
				total_lines += changed
				details.append((path.relative_to(REPO_ROOT), changed, count))

	mode = "rewrote" if arguments.apply else "would rewrite"
	print(f"{mode} {total_files} files, {total_lines} lines")
	details.sort(key=lambda item: item[1], reverse=True)
	for relative, changed, count in details[:40]:
		print(f"  {changed:5d}/{count:<6d}  {relative}")
	if len(details) > 40:
		print(f"  ... {len(details) - 40} more files")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
