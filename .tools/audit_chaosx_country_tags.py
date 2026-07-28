#!/usr/bin/env python3
"""Audit the reusable Event 006 and Soviet Collapse country-tag namespace.

Only engine country definitions under ``common/country_tags`` are considered.
Event text, localisation, flags, portraits, and other incidental mentions are
not competing country tags. The Random Events Mod is deliberately excluded
because it is an event-only compatibility surface, not part of the installed
country-tag namespace this audit protects.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TAG_DEFINITION_RE = re.compile(
	r'^\s*([A-Z0-9]{3})\s*=\s*["\']([^"\']*countries[\\/][^"\']+)["\']'
)
EVENT6_TAG_RE = re.compile(r'^\s*([A-Z0-9]{3})\s*=\s*["\']', re.MULTILINE)

RANDOM_EVENTS_WORKSHOP_ID = "3199436992"
RANDOM_EVENTS_NAMES = {"random events mod", "random_events_mod"}

# Event 005's registered custom tags. Existing registered carriers are kept;
# only the seven colliding tags were remapped to the X-suffixed IDs below.
SOVIET_COLLAPSE_TAGS = {
	"CFR",
	"MFR",
	"IJX",
	"INX",
	"SOG",
	"ANX",
	"ABX",
	"AOX",
	"FTH",
	"BBH",
	"AEX",
	"IKX",
	"DSC",
	"UWR",
	"KMB",
	"NRF",
	"TNC",
	"AAX",
	"UDC",
	"SDZ",
	"GAC",
	"DHC",
	"KHC",
	"FEV",
	"SZA",
	"UWD",
	"IMX",
	"IUL",
	"ADX",
	"PRA",
	"ILX",
	"ICD",
	"ARD",
	"NLC",
}

LEGACY_REMAP = {
	# Original Soviet Collapse ids and the five later extended-surface ids
	# retired by the focused installed-mod rescan. APX is retained here as an
	# intermediate id so stale pre-migration references cannot resurrect it.
	"ALA": "AAX",
	"ALN": "ABX",
	"BAC": "ADX",
	"BSC": "AEX",
	"KHW": "ANX",
	"KRS": "AOX",
	"KZR": "INX",
	"OGB": "IJX",
	"RMC": "IKX",
	"TSC": "ILX",
	"APX": "INX",
	"MRC": "IMX",
}


@dataclass(frozen=True)
class Definition:
	tag: str
	path: Path
	line: int
	root_kind: str
	root_name: str


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
	parser.add_argument(
		"--game-root",
		type=Path,
		default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"),
	)
	parser.add_argument(
		"--workshop-root",
		type=Path,
		default=Path(r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360"),
	)
	parser.add_argument("--local-mod-root", type=Path)
	parser.add_argument("--write-report", action="store_true")
	return parser.parse_args()


def parse_definitions(path: Path, root_kind: str, root_name: str) -> list[Definition]:
	try:
		lines = path.read_text(encoding="utf-8-sig", errors="ignore").splitlines()
	except OSError:
		return []
	definitions: list[Definition] = []
	for line_number, line in enumerate(lines, 1):
		match = TAG_DEFINITION_RE.match(line)
		if match:
			definitions.append(Definition(match.group(1), path, line_number, root_kind, root_name))
	return definitions


def tag_files(root: Path) -> list[Path]:
	base = root / "common" / "country_tags"
	return sorted(base.rglob("*.txt")) if base.is_dir() else []


def descriptor_name(root: Path) -> str:
	for descriptor in (root / "descriptor.mod", *sorted(root.glob("*.mod"))):
		if descriptor.is_file():
			try:
				text = descriptor.read_text(encoding="utf-8-sig", errors="ignore")
			except OSError:
				continue
			name_match = re.search(r"(?m)^\s*name\s*=\s*[\"']([^\"']+)", text)
			if name_match:
				return name_match.group(1).strip()
	return root.name


def is_random_events_mod(root: Path) -> bool:
	if root.name.lower() in RANDOM_EVENTS_NAMES or root.name == RANDOM_EVENTS_WORKSHOP_ID:
		return True
	return descriptor_name(root).lower() in RANDOM_EVENTS_NAMES


def collect_external_roots(
	repo_root: Path,
	game_root: Path,
	workshop_root: Path,
	local_mod_root: Path,
) -> tuple[list[tuple[str, Path]], list[str]]:
	roots: list[tuple[str, Path]] = []
	skipped: list[str] = []
	if game_root.is_dir():
		roots.append(("vanilla", game_root))
	for root in sorted(workshop_root.iterdir()) if workshop_root.is_dir() else []:
		if not root.is_dir():
			continue
		if is_random_events_mod(root):
			skipped.append(f"workshop/{root.name} ({descriptor_name(root)})")
			continue
		roots.append(("workshop", root))
	for root in sorted(local_mod_root.iterdir()) if local_mod_root.is_dir() else []:
		if not root.is_dir() or root.resolve() == repo_root.resolve():
			continue
		if is_random_events_mod(root):
			skipped.append(f"local/{root.name} ({descriptor_name(root)})")
			continue
		roots.append(("local", root))
	return roots, skipped


def parse_event6_tags(repo_root: Path) -> set[str]:
	path = repo_root / "common" / "country_tags" / "006_independence_wave_countries.txt"
	return {
		match.group(1)
		for match in EVENT6_TAG_RE.finditer(path.read_text(encoding="utf-8-sig", errors="ignore"))
		if not match.group(1).startswith("#")
	}


def write_report(path: Path, data: dict[str, object]) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	lines = [
		"# ChaosX Event 006/Soviet country-tag collision audit",
		"",
		f"- Event 006 tags: **{len(data['event6_tags'])}**.",
		f"- Soviet Collapse tags: **{len(data['soviet_tags'])}**.",
		f"- Protected tags: **{len(data['protected_tags'])}**.",
		f"- External country-definition collisions: **{len(data['collisions'])}**.",
		"- Random Events Mod definitions skipped by policy: **" + str(len(data["skipped_random_events"])) + "**.",
		"",
	]
	if data["collisions"]:
		lines.extend(["## Collisions", "", "| Tag | Source | File | Line |", "| --- | --- | --- | --- |"])
		for collision in data["collisions"]:
			lines.append(
				f"| `{collision['tag']}` | {collision['root_kind']} {collision['root_name']} | "
				f"`{collision['path']}` | {collision['line']} |"
			)
	else:
		lines.extend(["## Collisions", "", "No protected Event 006 or Soviet Collapse tag is defined by the scanned external country-tag registries."])
	lines.extend(["", "## Remap table", "", "| Legacy | Current |", "| --- | --- |"])
	lines.extend(f"| `{old}` | `{new}` |" for old, new in sorted(LEGACY_REMAP.items()))
	lines.extend(["", "## Exclusions", ""])
	lines.extend(f"- `{entry}`" for entry in data["skipped_random_events"])
	path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
	args = parse_args()
	repo_root = args.repo_root.resolve()
	local_mod_root = (args.local_mod_root or repo_root.parent).resolve()
	event6_tags = parse_event6_tags(repo_root)
	soviet_tags = set(SOVIET_COLLAPSE_TAGS)
	protected_tags = event6_tags | soviet_tags
	chaos_definitions = [
		definition
		for path in tag_files(repo_root)
		for definition in parse_definitions(path, "chaosx", "chaos_redux")
	]
	chaos_tags = {definition.tag for definition in chaos_definitions}
	missing_soviet = sorted(soviet_tags - chaos_tags)
	if missing_soviet:
		print("Missing Soviet Collapse registrations: " + ", ".join(missing_soviet), file=sys.stderr)
		return 2
	roots, skipped = collect_external_roots(repo_root, args.game_root.resolve(), args.workshop_root.resolve(), local_mod_root)
	definitions: list[Definition] = []
	for root_kind, root in roots:
		definitions.extend(
			definition
			for path in tag_files(root)
			for definition in parse_definitions(path, root_kind, descriptor_name(root))
		)
	external_by_tag: dict[str, list[Definition]] = {}
	for definition in definitions:
		if definition.tag in protected_tags:
			external_by_tag.setdefault(definition.tag, []).append(definition)
	collisions = [definition for tag in sorted(external_by_tag) for definition in external_by_tag[tag]]
	legacy_still_registered = sorted(set(LEGACY_REMAP) & chaos_tags)
	data = {
		"event6_tags": sorted(event6_tags),
		"soviet_tags": sorted(soviet_tags),
		"protected_tags": sorted(protected_tags),
		"collisions": [
			{
				"tag": definition.tag,
				"root_kind": definition.root_kind,
				"root_name": definition.root_name,
				"path": str(definition.path),
				"line": definition.line,
			}
			for definition in collisions
		],
		"skipped_random_events": skipped,
		"legacy_still_registered": legacy_still_registered,
	}
	print(
		f"Protected Event 006/Soviet tags: {len(protected_tags)}; "
		f"external country-definition collisions: {len(collisions)}; "
		f"random-event roots skipped: {len(skipped)}"
	)
	if legacy_still_registered:
		print("Legacy Soviet tags still registered: " + ", ".join(legacy_still_registered), file=sys.stderr)
	if collisions:
		for collision in data["collisions"]:
			print(
				f"{collision['tag']} -> {collision['root_kind']} {collision['root_name']} "
				f"{collision['path']}:{collision['line']}",
				file=sys.stderr,
			)
	if args.write_report:
		write_report(
			repo_root / "docs" / "plans" / "006_independence_wave_plans" / "tag_audit" / "006_chaosx_country_tag_collision_audit.md",
			data,
		)
	return 1 if collisions or legacy_still_registered else 0


if __name__ == "__main__":
	raise SystemExit(main())
