#!/usr/bin/env python3
"""Static audit of Chaos Redux English localisation against the script tree.

This tool answers four source-only questions without running the game:

1. Does every localisation file parse as `key: "value"` under an `l_english:`
   header, and does it keep its UTF-8 BOM?
2. Are any keys duplicated, either inside one file or across the localisation
   set? The engine keeps one definition per key, so duplicates mean the wiring
   is non-deterministic.
3. Which localisation keys are referenced by script or localisation but never
   defined here? Those render as raw key names in game.
4. Which defined keys are never referenced by any script token or
   `[bracket]` command? Those are candidates for removal.

The token test is deliberately conservative. A key counts as live when its
exact name appears as a token anywhere in the non-localisation tree, so a key
that is only built dynamically still survives the sweep and is reported as
`dynamic_candidate` instead of dead.

Usage:
	python .tools/audit_localisation_static.py                # report to stdout
	python .tools/audit_localisation_static.py --json out.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
LOCALISATION_DIR = REPO_ROOT / "localisation" / "english"

# Directories that are documentation, archived history, or tooling rather than
# engine-parsed mod content. They must not contribute "live" token evidence.
EXCLUDED_TOP_LEVEL = {
	".git",
	".tools",
	".tmp",
	".agents",
	".claude",
	".codex",
	".cursor",
	".opencode",
	".qoder",
	"docs",
	"history",
	"paradox_wiki",
	"localisation",
}

SCRIPT_SUFFIXES = {".txt", ".gui", ".gfx", ".asset", ".json", ".md", ".yml"}

# `key: "value"`, optionally followed by an inline comment. The value is
# greedy up to the last quote on the line so that a `#` inside a quoted string
# (for example a `§Y...§!` colour span) is never mistaken for a comment.
LOC_LINE = re.compile(
	r'^(?P<key>[A-Za-z0-9_.\-]+)\s*:\s*(?P<ordinal>\d+)?\s*"(?P<value>.*)"\s*(?:#.*)?$'
)
HEADER_LINE = re.compile(r"^l_english\s*:\s*(?:#.*)?$")

# Tokens we treat as script references. Keeps letters, digits, underscore, dot.
TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_.\-]*")

# `[Some.Getter]` and `[?var]` references inside localisation values.
BRACKET_REF = re.compile(r"\[([^\]]+)\]")

BOM = b"\xef\xbb\xbf"


class Findings:
	def __init__(self) -> None:
		self.parse_errors: List[str] = []
		self.missing_bom: List[str] = []
		self.no_header: List[str] = []
		self.duplicates: List[Tuple[str, str, int, str, int]] = []
		self.missing_event_roots: List[Tuple[str, List[str]]] = []
		self.missing_prefixed: List[Tuple[str, List[str]]] = []
		self.literal_names: List[Tuple[str, List[str]]] = []
		self.missing_event_content: List[Tuple[str, str, List[str]]] = []
		self.dynamic_candidates: List[Tuple[str, str]] = []
		self.dead_keys: List[Tuple[str, str]] = []
		self.encoding_artifacts: List[Tuple[str, int, str]] = []
		self.key_count = 0
		self.file_count = 0


def iter_script_files() -> Iterable[Path]:
	"""Yield engine-parsed mod files that can reference a localisation key."""
	for path in REPO_ROOT.rglob("*"):
		if not path.is_file():
			continue
		parts = path.relative_to(REPO_ROOT).parts
		if not parts or parts[0] in EXCLUDED_TOP_LEVEL:
			continue
		if path.suffix.lower() not in SCRIPT_SUFFIXES:
			continue
		yield path


def read_text(path: Path) -> str:
	"""Decode a file as UTF-8, tolerating a BOM and stray legacy bytes."""
	raw = path.read_bytes()
	if raw.startswith(BOM):
		raw = raw[3:]
	return raw.decode("utf-8", errors="replace")


def collect_script_tokens() -> Tuple[Set[str], Set[str], Dict[str, Set[str]]]:
	"""Return every identifier token, every bracket ref, and token->file index."""
	tokens: Set[str] = set()
	bracket_refs: Set[str] = set()
	per_file: Dict[str, Set[str]] = defaultdict(set)

	for path in iter_script_files():
		try:
			text = read_text(path)
		except OSError as error:
			print(f"warning: cannot read {path}: {error}", file=sys.stderr)
			continue
		rel = str(path.relative_to(REPO_ROOT))
		for match in TOKEN.finditer(text):
			value = match.group(0)
			tokens.add(value)
			per_file[value].add(rel)
		for match in BRACKET_REF.finditer(text):
			# `[ROOT.GetName]` -> add the whole command and each dotted part.
			inner = match.group(1).lstrip("?")
			bracket_refs.add(inner)
			for part in inner.split("."):
				bracket_refs.add(part.strip())

	return tokens, bracket_refs, per_file


def collect_dynamic_scripted_localisation() -> Set[str]:
	"""Return loc-key prefixes that scripted localisation builds at runtime.

	`common/scripted_localisation/` deliberately assembles keys such as
	`chaosx.event_name.100.t` from data, so a key with one of these prefixes is
	live even when no literal reference to it exists.
	"""
	prefixes: Set[str] = set()
	directory = REPO_ROOT / "common" / "scripted_localisation"
	if not directory.is_dir():
		return prefixes

	for path in sorted(directory.glob("*.txt")):
		text = read_text(path)
		for match in re.finditer(r'(?:localisation_key|text)\s*=\s*"([^"]+)"', text):
			value = match.group(1)
			if value:
				prefixes.add(value)
				# Also register the dotted root so `a.b.1.t` matches on `a.b`.
				parts = value.split(".")
				for length in range(1, len(parts)):
					prefixes.add(".".join(parts[:length]))
	return prefixes


def parse_localisation(findings: Findings) -> Dict[str, List[Tuple[str, int]]]:
	"""Parse every localisation file, recording keys and structural problems."""
	definitions: Dict[str, List[Tuple[str, int]]] = defaultdict(list)

	for path in sorted(LOCALISATION_DIR.glob("*.yml")):
		findings.file_count += 1
		rel = str(path.relative_to(REPO_ROOT))
		raw = path.read_bytes()
		if not raw.startswith(BOM):
			findings.missing_bom.append(rel)
		text = read_text(path)
		lines = text.splitlines()

		# The `l_english:` header may sit below a banner comment block, so find
		# the first content line rather than assuming it is line 1.
		header_index = None
		for number, line in enumerate(lines, start=1):
			stripped = line.strip()
			if not stripped or stripped.startswith("#"):
				continue
			header_index = number
			break
		if header_index is None or not HEADER_LINE.match(lines[header_index - 1].strip()):
			findings.no_header.append(rel)

		for number, line in enumerate(lines, start=1):
			stripped = line.strip()
			if not stripped or stripped.startswith("#"):
				continue
			if number == header_index and HEADER_LINE.match(stripped):
				continue
			match = LOC_LINE.match(stripped)
			if match is None:
				findings.parse_errors.append(f"{rel}:{number}: {stripped[:120]}")
				continue

			key = match.group("key")
			value = match.group("value")
			findings.key_count += 1
			definitions[key].append((rel, number))

			if match.group("ordinal"):
				findings.encoding_artifacts.append((rel, number, f"ordinal suffix on {key}"))
			if "\ufffd" in value:
				findings.encoding_artifacts.append((rel, number, f"replacement character in {key}"))

	return definitions


def classify(
	definitions: Dict[str, List[Tuple[str, int]]],
	tokens: Set[str],
	bracket_refs: Set[str],
) -> None:
	"""Split defined keys into live, dynamic-only, and dead."""
	findings = AUDIT_FINDINGS
	for key, sites in sorted(definitions.items()):
		if len(sites) > 1:
			first = sites[0]
			for other in sites[1:]:
				findings.duplicates.append((key, first[0], first[1], other[0], other[1]))

		if key in tokens or key in bracket_refs:
			continue

		# Event-style keys are referenced by their numeric root, never verbatim:
		# `chaosx.nr6.1.t` is produced by the engine from event id `chaosx.nr6.1`.
		parts = key.rsplit(".", 1)
		if len(parts) == 2 and len(parts[1]) <= 3 and parts[0] in tokens:
			continue

		# A dynamic key may be assembled from a token prefix plus a variable, so
		# keep anything whose longest dot-prefix is a live token.
		prefix = key
		matched = False
		while "." in prefix:
			prefix = prefix.rsplit(".", 1)[0]
			if prefix in tokens:
				findings.dynamic_candidates.append((key, prefix))
				matched = True
				break
		if not matched:
			findings.dead_keys.append((key, sites[0][0]))


def collect_scripted_identifiers() -> Set[str]:
	"""Return registered scripted effect, trigger, and scripted-loc names."""
	identifiers: Set[str] = set()
	roots = [
		REPO_ROOT / "common" / "scripted_effects",
		REPO_ROOT / "common" / "scripted_triggers",
		REPO_ROOT / "common" / "scripted_localisation",
		REPO_ROOT / "common" / "scripted_guis",
	]
	definition = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{")

	for root in roots:
		if not root.is_dir():
			continue
		for path in sorted(root.rglob("*.txt")):
			for line in read_text(path).splitlines():
				match = definition.match(line)
				if match:
					identifiers.add(match.group(1))
	return identifiers


class EventRecord:
	"""What an event block declares about its own text bindings."""

	__slots__ = ("file", "hidden", "explicit_title", "explicit_desc")

	def __init__(self, file: str) -> None:
		self.file = file
		self.hidden = False
		self.explicit_title: Optional[str] = None
		self.explicit_desc: Optional[str] = None


def collect_event_roots() -> Dict[str, EventRecord]:
	"""Return every declared event with the text bindings it actually declares.

	An event either follows the `<id>.t` / `<id>.d` convention or binds its text
	explicitly with `title =` / `desc =`. Both forms are used across this
	repository, so the localisation check must read the binding rather than
	assume the convention. A `hidden = yes` event shows no window text at all
	and is excluded from the requirement.

	Event blocks are recognised by their distinctive markers (`is_triggered_only`,
	`option =`, `mean_time_to_happen`, ...) plus brace depth measured relative to
	each candidate's own block, which keeps `id =` keys inside options, power
	balances, and characters out of the event set.
	"""
	events: Dict[str, EventRecord] = {}
	declaration = re.compile(r"^\s*id\s*=\s*([A-Za-z_][A-Za-z0-9_.]*)\s*$")
	hidden_flag = re.compile(r"^\s*hidden\s*=\s*yes\s*$")
	title_binding = re.compile(r"^\s*title\s*=\s*([A-Za-z_][A-Za-z0-9_.]*)\s*$")
	desc_binding = re.compile(r"^\s*desc\s*=\s*([A-Za-z_][A-Za-z0-9_.]*)\s*$")
	quoted_text = re.compile(r'^\s*(?:title|desc)\s*=\s*"')
	# Markers that only an event block carries. `trigger` and `immediate` are
	# excluded because options, decisions, and characters also use them.
	markers = (
		re.compile(r"^\s*is_triggered_only\s*="),
		re.compile(r"^\s*fire_only_once\s*="),
		re.compile(r"^\s*is_fire_only_once\s*="),
		re.compile(r"^\s*mean_time_to_happen\s*="),
		re.compile(r"^\s*option\s*=\s*\{"),
		re.compile(r"^\s*major\s*="),
		re.compile(r"^\s*news\s*="),
		re.compile(r"^\s*timeout_days\s*="),
	)
	# Engine scope keywords can appear as an `id` value but are not event ids.
	scopes = {
		"ROOT", "THIS", "PREV", "FROM", "OWNER", "CONTROLLER", "OVERLORD", "CAPITAL",
	}

	events_dir = REPO_ROOT / "events"
	if not events_dir.is_dir():
		return events

	for path in sorted(events_dir.rglob("*.txt")):
		rel = str(path.relative_to(REPO_ROOT))
		record: Optional[EventRecord] = None
		candidate_depth: Optional[int] = None
		qualified = False
		depth = 0

		def resolve() -> None:
			nonlocal record, candidate_depth, qualified
			if record is not None and qualified:
				events[record_id[0]] = record
			record = None
			candidate_depth = None
			qualified = False

		record_id: List[str] = [""]

		for line in read_text(path).splitlines():
			match = declaration.match(line)
			if match:
				candidate = match.group(1)
				if candidate not in scopes:
					resolve()
					record = EventRecord(rel)
					record_id[0] = candidate
				depth += line.count("{") - line.count("}")
				continue

			if record is not None:
				# Attributes before the opening brace sit at the current depth,
				# so they are checked both before and after this line's braces
				# are counted. HOI4 events put `is_triggered_only = yes` and
				# friends between the `id` line and the `{`.
				def note(text: str) -> None:
					nonlocal qualified
					if hidden_flag.match(text):
						record.hidden = True
					elif quoted_text.match(text):
						# The text is supplied inline, so no key is required for
						# that field; a quoted desc is legal HOI4 script.
						record.explicit_desc = record.explicit_desc or ""
						record.explicit_title = record.explicit_title or ""
					else:
						title = title_binding.match(text)
						if title:
							record.explicit_title = title.group(1)
						else:
							desc = desc_binding.match(text)
							if desc:
								record.explicit_desc = desc.group(1)
					if any(marker.match(text) for marker in markers):
						qualified = True

				if candidate_depth is None:
					note(line)

				if candidate_depth is None and "{" in line:
					candidate_depth = depth + 1

				if candidate_depth is not None and depth == candidate_depth:
					note(line)

			depth += line.count("{") - line.count("}")

			if candidate_depth is not None and depth < candidate_depth:
				resolve()

		resolve()

	return events


def audit_event_loc_keys(
	events: Dict[str, EventRecord],
	definitions: Dict[str, List[Tuple[str, int]]],
) -> None:
	"""Check every visible event's title and description against localisation.

	An event that binds `title =` or `desc =` is checked against that exact key;
	otherwise the `<id>.t` / `<id>.d` convention is expected. A missing key
	renders as a raw key name in the event window.
	"""
	findings = AUDIT_FINDINGS

	for event_id, record in sorted(events.items()):
		if record.hidden:
			continue
		required = (
			("title", record.explicit_title or f"{event_id}.t"),
			("description", record.explicit_desc or f"{event_id}.d"),
		)
		for role, key in required:
			# An empty binding means the value was supplied inline as a quoted
			# string, which needs no localisation key.
			if not key:
				continue
			if key not in definitions:
				findings.missing_event_content.append((key, role, [record.file]))


def collect_quoted_keys() -> Tuple[Dict[str, Set[str]], Dict[str, Set[str]]]:
	"""Index localisation bindings from localisation-consuming definitions.

	Two binding forms are collected separately because only one is a
	localisation reference:

	- Quoted values (`name = "Some Name"`) are literal strings. The engine uses
	  them verbatim, so they must NOT be reported as missing keys. This is the
	  documented `set_province_name = { id = <id> name = <string> }` form.
	- Bare identifiers (`name = SOME_KEY`) are localisation references.

	Only specific field names consume localisation, and only inside definition
	folders that bind them, so unit type names, equipment archetypes, mesh
	names, and sound names are excluded by construction.
	"""
	quoted: Dict[str, Set[str]] = defaultdict(set)
	bare: Dict[str, Set[str]] = defaultdict(set)
	shape = re.compile(r"^[A-Za-z_][A-Za-z0-9_.\-]*$")

	# Folders whose definitions bind localisation keys by name.
	SCAN_DIRS = (
		"events",
		"common/decisions",
		"common/ideas",
		"common/national_focus",
		"common/characters",
		"common/missions",
		"common/scripted_guis",
		"common/operations",
		"common/units",
		"common/technologies",
		"common/doctrines",
		"common/continuous_focus",
		"common/decisions/categories",
		"common/achievements",
		"common/dynamic_modifiers",
		"common/opinion_modifiers",
		"common/raids",
		"common/special_projects",
		"common/abilities",
		"common/combat_tactics",
	)

	# Field names whose value is looked up in localisation.
	LOC_FIELDS = (
		"name",
		"desc",
		"title",
		"text",
		"tooltip",
		"localisation_key",
		"custom_effect_tooltip",
		"custom_trigger_tooltip",
		"custom_idea_tooltip",
		"complete_effect_tooltip",
		"available_tooltip",
		"effect_tooltip",
		"select_effect_tooltip",
		"visible_tooltip",
		"mission_text",
		"description",
	)
	# A loc field may only be matched as a whole token, which needs a guard on
	# both sides. The lookbehind rejects a preceding word character or
	# underscore, so `mutually_exclusive` no longer matches `text`+`t`+`name`.
	# The lookahead rejects a following word character, so the literal `name`
	# inside identifiers such as `ICE_advanced_technology` is not a match.
	# Both produced phantom keys before these guards.
	guard = r"(?<![\w_])"
	tail = r"(?![\w])"
	field = guard + r"(?:" + "|".join(LOC_FIELDS) + r")" + tail + r"\s*="
	quoted_pattern = re.compile(field + r'\s*"([^"\n]{1,120})"')
	bare_pattern = re.compile(field + r"\s*([A-Za-z_][A-Za-z0-9_.\-]*)")

	for relative in SCAN_DIRS:
		root = REPO_ROOT / relative
		if not root.is_dir():
			continue
		for path in sorted(root.rglob("*.txt")):
			try:
				text = read_text(path)
			except OSError:
				continue
			rel = str(path.relative_to(REPO_ROOT))
			for match in quoted_pattern.finditer(text):
				value = match.group(1).strip()
				if value and shape.match(value):
					quoted[value].add(rel)
			for match in bare_pattern.finditer(text):
				value = match.group(1).strip()
				if value and shape.match(value):
					bare[value].add(rel)

	return quoted, bare


def collect_referenced_keys(
	tokens: Set[str],
	definitions: Dict[str, List[Tuple[str, int]]],
	quoted: Dict[str, Set[str]],
	bare: Dict[str, Set[str]],
	dynamic_prefixes: Set[str],
	scripted_tokens: Set[str],
) -> None:
	"""Flag loc keys that script references but localisation never defines.

	Evidence is a bare identifier bound to a localisation-consuming field, which
	is the form the engine resolves as a key. A quoted value is a literal string
	and is never reported.

	Two shapes are reported separately because they fail differently in game:

	- Event roots (`chaosx.nr6.1`) never appear verbatim in localisation; the
	  engine builds `<root>.t`, `.d`, `.a`, `.b`, ... so the test is whether any
	  defined key carries the root as a dotted prefix.
	- Flat keys are checked literally, excluding values that scripted
	  localisation assembles at runtime.
	"""
	findings = AUDIT_FINDINGS

	dotted_roots: Set[str] = set()
	for key in definitions:
		parts = key.split(".")
		for length in range(2, len(parts)):
			dotted_roots.add(".".join(parts[:length]))

	event_root = re.compile(r"^chaosx\.[A-Za-z0-9_]+\.[0-9]+$")
	# Effect/trigger and engine keywords are registered in common/, not
	# localisation, and are frequently written in the same `x = y` shape.
	keyword_shapes = re.compile(
		r"^(?:set_|add_|remove_|has_|is_|get_|clear_|every_|any_|random_|all_|count_|clamp_)"
	)
	# Engine-owned tokens that appear as values but are never loc keys.
	reserved = {
		"yes",
		"no",
		"ROOT",
		"THIS",
		"PREV",
		"FROM",
		"OWNER",
		"CONTROLLER",
		"OVERLORD",
		"CAPITAL",
		"no",
		"undefined",
	}

	for literal in sorted(bare):
		if literal in definitions or literal in dynamic_prefixes:
			continue
		if literal in scripted_tokens or literal in reserved:
			continue
		if keyword_shapes.match(literal):
			continue

		if event_root.match(literal):
			if literal in dotted_roots:
				continue
			findings.missing_event_roots.append((literal, sorted(bare[literal])[:3]))
			continue

		findings.missing_prefixed.append((literal, sorted(bare[literal])[:3]))

	# A quoted value that is never defined is still worth surfacing as context
	# for review, but it is not a defect, so it is reported separately.
	for literal in sorted(quoted):
		if literal in definitions or literal in dynamic_prefixes:
			continue
		if literal in scripted_tokens:
			continue
		if re.match(r"^[A-Z][a-z]+$", literal):
			findings.literal_names.append((literal, sorted(quoted[literal])[:2]))


def emit_report(findings: Findings) -> None:
	print("=" * 78)
	print("Chaos Redux static localisation audit")
	print("=" * 78)
	print(f"files parsed            : {findings.file_count}")
	print(f"key definitions         : {findings.key_count}")
	print(f"duplicate keys          : {len(findings.duplicates)}")
	print(f"parse errors            : {len(findings.parse_errors)}")
	print(f"missing BOM             : {len(findings.missing_bom)}")
	print(f"missing l_english header: {len(findings.no_header)}")
	print(f"encoding artifacts      : {len(findings.encoding_artifacts)}")
	print(f"undefined event roots   : {len(findings.missing_event_roots)}")
	print(f"undefined key bindings  : {len(findings.missing_prefixed)}")
	print(f"literal (non-key) names : {len(findings.literal_names)}")
	print(f"missing event t/d keys  : {len(findings.missing_event_content)}")
	print(f"dead keys               : {len(findings.dead_keys)}")

	def section(title: str, rows: List[str], limit: int = 40) -> None:
		print()
		print(f"--- {title} ({len(rows)}) ---")
		for row in rows[:limit]:
			print(f"  {row}")
		if len(rows) > limit:
			print(f"  ... {len(rows) - limit} more")

	section("parse errors", findings.parse_errors)
	section("missing BOM", findings.missing_bom)
	section("missing l_english header", findings.no_header)
	section("encoding artifacts", [f"{f}:{n}: {m}" for f, n, m in findings.encoding_artifacts])
	section(
		"duplicate keys",
		[f"{k}  {f1}:{n1}  then  {f2}:{n2}" for k, f1, n1, f2, n2 in findings.duplicates],
	)
	section("undefined event roots", [f"{k}  ({', '.join(src)})" for k, src in findings.missing_event_roots])
	section(
		"undefined key bindings",
		[f"{k}  ({', '.join(src)})" for k, src in findings.missing_prefixed],
	)
	section(
		"missing event title/description keys",
		[f"{k}  ({role})  {', '.join(src)}" for k, role, src in findings.missing_event_content],
		limit=60,
	)
	section(
		"literal (non-key) names",
		[f"{k}  ({', '.join(src)})" for k, src in findings.literal_names],
		limit=20,
	)
	section("dead keys", [f"{k}  ({src})" for k, src in findings.dead_keys], limit=80)


def write_json(findings: Findings, destination: Path) -> None:
	payload = {
		"key_count": findings.key_count,
		"file_count": findings.file_count,
		"parse_errors": findings.parse_errors,
		"missing_bom": findings.missing_bom,
		"no_header": findings.no_header,
		"encoding_artifacts": [
			{"file": f, "line": n, "detail": m} for f, n, m in findings.encoding_artifacts
		],
		"duplicates": [
			{"key": k, "file": f1, "line": n1, "other_file": f2, "other_line": n2}
			for k, f1, n1, f2, n2 in findings.duplicates
		],
		"missing_event_roots": [
			{"key": k, "sources": s} for k, s in findings.missing_event_roots
		],
		"missing_prefixed": [{"key": k, "sources": s} for k, s in findings.missing_prefixed],
		"literal_names": [{"value": k, "sources": s} for k, s in findings.literal_names],
		"missing_event_content": [
			{"key": k, "role": r, "sources": s} for k, r, s in findings.missing_event_content
		],
		"dead_keys": [{"key": k, "file": f} for k, f in findings.dead_keys],
	}
	destination.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
	print(f"\nwrote {destination}")


AUDIT_FINDINGS = Findings()


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--json", type=Path, help="also write the findings as JSON")
	arguments = parser.parse_args()

	findings = AUDIT_FINDINGS
	print("indexing script tokens ...", file=sys.stderr)
	tokens, bracket_refs, token_sources = collect_script_tokens()
	print(f"  {len(tokens)} distinct tokens", file=sys.stderr)

	print("parsing localisation ...", file=sys.stderr)
	definitions = parse_localisation(findings)
	print(f"  {len(definitions)} distinct keys", file=sys.stderr)

	dynamic_prefixes = collect_dynamic_scripted_localisation()
	print(f"  {len(dynamic_prefixes)} dynamic key prefixes", file=sys.stderr)

	scripted_tokens = collect_scripted_identifiers()
	print(f"  {len(scripted_tokens)} scripted identifiers", file=sys.stderr)

	quoted, bare = collect_quoted_keys()
	print(f"  {len(quoted)} quoted literals, {len(bare)} bare bindings", file=sys.stderr)

	classify(definitions, tokens, bracket_refs)
	collect_referenced_keys(
		tokens, definitions, quoted, bare, dynamic_prefixes, scripted_tokens
	)

	events = collect_event_roots()
	hidden = sum(1 for record in events.values() if record.hidden)
	print(
		f"  {len(events)} events ({hidden} hidden, {len(events) - hidden} visible)",
		file=sys.stderr,
	)
	audit_event_loc_keys(events, definitions)

	emit_report(findings)
	if arguments.json:
		write_json(findings, arguments.json)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
