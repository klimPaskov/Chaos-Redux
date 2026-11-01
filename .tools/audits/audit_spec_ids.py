#!/usr/bin/env python3
"""Two-way gap audit for the stable spec item IDs of new Chaos Redux spec packages.

A new spec package gives each spec item an ID such as `E102-S014` (event 102, spec item 14) and an
origin tag, as the `chaos-redux-event-planning` skill describes in "Spec item IDs and origin tags".
Implementation handoffs and plans cite the IDs they implement or change. This audit compares the
two sides and reads only `.md` files under `docs/specs/` (definitions and references) and
`docs/plans/` (citations). Only the `E<event number>-S<sequence>` form is recognised, so older
packages with their own labels (such as the `PS-S001` source rows of the Event 117 package) are
never touched, and a repository where no package uses IDs is clean.

A definition is a line of a spec file that starts with an ID, after an optional list marker,
heading marker, table pipe or emphasis, and is followed by an origin tag: `E102-S014 [locked] ...`.
Any other mention of an ID, in a spec or in a plan, is a reference or citation. Ranges are not
expanded: cite every ID.

Rules under the `.tools/lib/report.py` contract:

- `SPECID-UNKNOWN` (error): an ID is mentioned in a spec or plan but no spec package defines it.
- `SPECID-DUPLICATE` (error): an ID is defined more than once; the finding names the first site.
- `SPECID-ORIGIN` (error): a definition has no origin tag, or a tag other than
  `[locked]`, `[derived]` or `[open]`.
- `SPECID-PACKAGE` (error): a definition sits in a package whose folder number
  (`docs/specs/102_<slug>_specs/`) differs from the event number in the ID.
- `SPECID-UNCITED` (review): a defined spec item that no file under `docs/plans/` cites.

Usage:
	python -B .tools/audits/audit_spec_ids.py
	python -B .tools/audits/audit_spec_ids.py --paths docs/specs/102_serial_killer_specs
	python -B .tools/audits/audit_spec_ids.py --json .tmp/spec_ids.json

`--paths` limits the report, not the scan: a citation can only be resolved against every
definition. Exit status: 0 no errors, 1 errors, 2 for a usage or input failure.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # .tools, for the shared lib package
from lib.report import Finding, add_arguments, exit_code, merge_json, print_findings, requested_paths, select

REPO_ROOT = Path(__file__).resolve().parents[2]
CHECK = "spec-ids"
LEVELS = {
	"SPECID-UNKNOWN": "error",
	"SPECID-DUPLICATE": "error",
	"SPECID-ORIGIN": "error",
	"SPECID-PACKAGE": "error",
	"SPECID-UNCITED": "review",
}
ORIGINS = ("locked", "derived", "open")

# `E102-S014`: `E` plus the three-digit event number, then `-S` and the sequence number.
ID_TEXT = r"E\d{3}-S\d{3,}"
MENTION = re.compile(r"(?<![A-Za-z0-9_-])" + ID_TEXT + r"(?![A-Za-z0-9_])")
# The ID must be the first token of the line, after a heading, list or table marker and emphasis.
DEFINITION = re.compile(
	r"^[ \t>]*(?:#{1,6}[ \t]+|[-*+][ \t]+|\d+[.)][ \t]+|\|[ \t]*)?[*_`]*"
	r"(?P<id>" + ID_TEXT + r")(?![A-Za-z0-9_])[*_`]*(?:[ \t]*\[(?P<origin>[^\]\n]*)\])?"
)


class Site(NamedTuple):
	path: str
	line: int


class Definition(NamedTuple):
	spec_id: str
	origin: str
	site: Site


class Mention(NamedTuple):
	spec_id: str
	site: Site
	in_plan: bool


def markdown_files(folder: Path) -> List[Path]:
	return sorted(folder.rglob("*.md")) if folder.is_dir() else []


def read_lines(path: Path) -> List[str]:
	return path.read_bytes().decode("utf-8-sig", errors="replace").splitlines()


def package_of(path: str) -> str:
	"""Return the `docs/specs/<package>` folder name of a spec path, or an empty string."""
	parts = path.split("/")
	return parts[2] if len(parts) > 3 and parts[:2] == ["docs", "specs"] else ""


def package_event(path: str) -> str:
	"""Return the event number a spec path's package folder starts with, or an empty string."""
	found = re.match(r"(\d{3})_", package_of(path))
	return found.group(1) if found else ""


def scan_spec_file(path: str, lines: Sequence[str]) -> Tuple[List[Definition], List[Mention], List[Finding]]:
	"""Split one spec file into definitions, other mentions and origin-tag findings."""
	definitions: List[Definition] = []
	mentions: List[Mention] = []
	findings: List[Finding] = []
	for number, text in enumerate(lines, 1):
		defined = DEFINITION.match(text)
		skip_start = -1
		if defined:
			spec_id = defined.group("id")
			origin = defined.group("origin")
			skip_start = defined.start("id")
			site = Site(path, number)
			if origin is None:
				findings.append(Finding(CHECK, "SPECID-ORIGIN", "error", path, number,
					f"{spec_id} has no origin tag; write [locked], [derived] or [open] right after the ID"))
			elif origin not in ORIGINS:
				findings.append(Finding(CHECK, "SPECID-ORIGIN", "error", path, number,
					f"{spec_id} has origin tag [{origin}]; use [locked], [derived] or [open]"))
			if package_event(path) != spec_id[1:4]:
				findings.append(Finding(CHECK, "SPECID-PACKAGE", "error", path, number,
					f"{spec_id} sits in package {package_of(path) or path}, whose number must equal the event number in the ID"))
			definitions.append(Definition(spec_id, origin or "", site))
		for found in MENTION.finditer(text):
			if found.start() != skip_start:
				mentions.append(Mention(found.group(0), Site(path, number), False))
	return definitions, mentions, findings


def scan_plan_file(path: str, lines: Sequence[str]) -> List[Mention]:
	return [Mention(found.group(0), Site(path, number), True)
		for number, text in enumerate(lines, 1) for found in MENTION.finditer(text)]


def audit(root: Path) -> Tuple[List[Finding], Dict[str, Definition]]:
	"""Scan `root/docs/specs` and `root/docs/plans`; return every finding and the defined items."""
	findings: List[Finding] = []
	defined: Dict[str, Definition] = {}
	mentions: List[Mention] = []
	for file in markdown_files(root / "docs" / "specs"):
		path = file.relative_to(root).as_posix()
		definitions, spec_mentions, origin_findings = scan_spec_file(path, read_lines(file))
		findings += origin_findings
		mentions += spec_mentions
		for definition in definitions:
			first = defined.get(definition.spec_id)
			if first is None:
				defined[definition.spec_id] = definition
			else:
				findings.append(Finding(CHECK, "SPECID-DUPLICATE", "error", definition.site.path, definition.site.line,
					f"{definition.spec_id} is already defined at {first.site.path}:{first.site.line}"))
	for file in markdown_files(root / "docs" / "plans"):
		mentions += scan_plan_file(file.relative_to(root).as_posix(), read_lines(file))

	cited: Set[str] = set()
	for mention in mentions:
		if mention.spec_id not in defined:
			where = "a plan or handoff cites" if mention.in_plan else "a spec mentions"
			findings.append(Finding(CHECK, "SPECID-UNKNOWN", "error", mention.site.path, mention.site.line,
				f"{where} {mention.spec_id}, which no spec package defines"))
		elif mention.in_plan:
			cited.add(mention.spec_id)
	for spec_id, definition in defined.items():
		if spec_id not in cited:
			findings.append(Finding(CHECK, "SPECID-UNCITED", "review", definition.site.path, definition.site.line,
				f"{spec_id} [{definition.origin or 'untagged'}] is cited by no plan or handoff under docs/plans/"))
	return findings, defined


def main(argv: Optional[Sequence[str]] = None) -> int:
	parser = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[0])
	parser.add_argument("--json", type=Path, help="also write the findings as JSON")
	parser.add_argument("--root", type=Path, default=REPO_ROOT, help="repository root to scan (default: this mod)")
	add_arguments(parser)
	arguments = parser.parse_args(argv)
	root: Path = arguments.root.resolve()
	if not root.is_dir():
		print(f"{CHECK}: root {root} is not a folder", file=sys.stderr)
		return 2
	findings, defined = audit(root)
	findings = select(findings, requested_paths(arguments))
	packages = {package_of(definition.site.path) for definition in defined.values()}
	print(f"{CHECK}: {len(defined)} spec items defined, {len(packages)} packages use IDs")
	print_findings(CHECK, findings)
	if arguments.json:
		merge_json(arguments.json, findings, LEVELS)
	return exit_code(findings, arguments.fail_on)


if __name__ == "__main__":
	raise SystemExit(main())
