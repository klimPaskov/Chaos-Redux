#!/usr/bin/env python3
"""Audit Event 006 tags against vanilla and every installed local mod.

The audit is read-only with respect to gameplay files. It writes evidence
under ``docs/plans/006_independence_wave_plans`` when ``--write-reports`` is
passed. Collision-free replacement candidates are suggestions only; tag
remaps still require a reviewed, repository-wide migration.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path


TAG_DEFINITION_RE = re.compile(
	r'^\s*([A-Z0-9]{3})\s*=\s*["\']([^"\']*countries[\\/][^"\']+)["\']',
	re.MULTILINE,
)
EVENT6_TAG_RE = re.compile(
	r'^\s*([A-Z0-9]{3})\s*=\s*["\'][^"\']+["\']\s*#\s*(IW-\d{3})\s*:\s*(.+?)\.?\s*$',
	re.MULTILINE,
)
LOC_RE = re.compile(r'^\s*([A-Z0-9]{3})(?:_(?:DEF|ADJ|democratic|communism|fascism|neutrality))?\s*:\d*\s*["\'](.+?)["\']\s*$', re.MULTILINE)
LOC_KEY_VALUE_RE = re.compile(r'^\s*([A-Za-z0-9_]+)\s*:\d*\s*["\'](.+?)["\']\s*$', re.MULTILINE)
COSMETIC_DEFINITION_RE = re.compile(r'^([A-Za-z0-9_]+)\s*=\s*\{', re.MULTILINE)
ALIAS_RE = re.compile(r'^\s*([A-Z0-9]{3})\s*=\s*\{', re.MULTILINE)
COSMETIC_BYTES_RE = re.compile(rb'\bset_cosmetic_tag\s*=\s*([A-Z0-9]{3})\b')
BASE_LOC_BYTES_RE = re.compile(rb'(?m)^\s*([A-Z0-9]{3})\s*:\d*\s*["\']')
FLAG_RE = re.compile(r'^([A-Z0-9]{3})(?:_(?:communism|democratic|fascism|neutrality))?\.tga$', re.IGNORECASE)
HISTORY_COUNTRY_RE = re.compile(r'^([A-Z0-9]{3}).*\.txt$', re.IGNORECASE)
ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES = {
	"GFX": "HOI4 sprite and interface graphics identifier namespace",
	"AUX": "Windows reserved DOS device basename; country, history, localisation, and flag files cannot be opened reliably",
	"CON": "Windows reserved DOS device basename",
	"NUL": "Windows reserved DOS device basename",
	"PRN": "Windows reserved DOS device basename",
}
LOC_MARKUP_RE = re.compile(r'(?:§.|£[^£\s]+£|\$[^$]+\$|\[[^\]]+\])')
STATE_WORDS = {
	"autonomous",
	"commonwealth",
	"confederacy",
	"confederation",
	"democratic",
	"duchy",
	"emirate",
	"empire",
	"federal",
	"federation",
	"free",
	"grand",
	"neo",
	"kingdom",
	"national",
	"of",
	"people",
	"peoples",
	"provisional",
	"protectorate",
	"regional",
	"republic",
	"restoration",
	"socialist",
	"sultanate",
	"state",
	"the",
	"unitary",
	"united",
	"union",
}


@dataclass(frozen=True)
class TagDefinition:
	tag: str
	root_kind: str
	root_name: str
	use_kind: str
	file: str
	country_path: str


def decode_text(path: Path) -> str:
	data = path.read_bytes()
	for encoding in ("utf-8-sig", "utf-8", "cp1252"):
		try:
			return data.decode(encoding)
		except UnicodeDecodeError:
			continue
	return data.decode("utf-8", errors="replace")


def file_sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def normalize_name(value: str, remove_state_words: bool = False) -> str:
	value = LOC_MARKUP_RE.sub(" ", value)
	value = value.replace("&", " and ")
	value = unicodedata.normalize("NFKD", value)
	value = "".join(character for character in value if not unicodedata.combining(character))
	words = [word for word in re.findall(r"[a-z0-9]+", value.lower()) if len(word) > 1 or word.isdigit()]
	if remove_state_words:
		words = [word for word in words if word not in STATE_WORDS]
	return " ".join(words)


def scan_tag_directory(root: Path, root_kind: str, root_name: str) -> list[TagDefinition]:
	tag_dir = root / "common" / "country_tags"
	if not tag_dir.is_dir():
		return []
	definitions: list[TagDefinition] = []
	for path in sorted(tag_dir.rglob("*.txt")):
		text = decode_text(path)
		for match in TAG_DEFINITION_RE.finditer(text):
			definitions.append(
				TagDefinition(
					tag=match.group(1),
					root_kind=root_kind,
					root_name=root_name,
					use_kind="country_tag_definition",
					file=str(path),
					country_path=match.group(2).replace("\\", "/"),
				)
			)
	return definitions


def scan_extended_tag_surfaces(root: Path, root_kind: str, root_name: str) -> list[TagDefinition]:
	"""Scan alias, cosmetic, history, localisation, and flag tag surfaces."""
	definitions: list[TagDefinition] = []
	seen: set[tuple[str, str, str]] = set()

	alias_dir = root / "common" / "country_tag_aliases"
	if alias_dir.is_dir():
		for path in sorted(alias_dir.rglob("*.txt")):
			for match in ALIAS_RE.finditer(decode_text(path)):
				key = (match.group(1), "country_tag_alias", str(path))
				if key in seen:
					continue
				seen.add(key)
				definitions.append(
					TagDefinition(match.group(1), root_kind, root_name, "country_tag_alias", str(path), "alias block")
				)

	countries_dir = root / "common" / "countries"
	if countries_dir.is_dir():
		for path in sorted(countries_dir.rglob("*.txt")):
			for match in COSMETIC_DEFINITION_RE.finditer(decode_text(path)):
				tag = match.group(1)
				if not re.fullmatch(r"[A-Z0-9]{3}", tag):
					continue
				key = (tag, "cosmetic_country_definition", str(path))
				if key in seen:
					continue
				seen.add(key)
				definitions.append(
					TagDefinition(tag, root_kind, root_name, "cosmetic_country_definition", str(path), "top-level country cosmetic block")
				)

	def matching_files(subtrees: tuple[str, ...], pattern: str, glob: str) -> list[Path]:
		paths = [root / name for name in subtrees if (root / name).is_dir()]
		rg = shutil.which("rg")
		if rg and paths:
			result = subprocess.run(
				[rg, "--files-with-matches", "--pcre2", pattern, "-g", glob, *(str(path) for path in paths)],
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				text=True,
				encoding="utf-8",
				errors="replace",
			)
			if result.returncode not in (0, 1):
				raise RuntimeError(f"ripgrep failed while auditing {root}: {result.stderr}")
			return [Path(line) for line in result.stdout.splitlines() if line.strip()]
		files: list[Path] = []
		for path in paths:
			files.extend(path.rglob(glob))
		return files

	for path in matching_files(
		("common", "events", "history"),
		r"\bset_cosmetic_tag\s*=\s*[A-Z0-9]{3}\b",
		"*.txt",
	):
			data = path.read_bytes()
			for match in COSMETIC_BYTES_RE.finditer(data):
				tag = match.group(1).decode("ascii")
				key = (tag, "set_cosmetic_tag", str(path))
				if key in seen:
					continue
				seen.add(key)
				definitions.append(TagDefinition(tag, root_kind, root_name, "set_cosmetic_tag", str(path), "effect call site"))

	for path in matching_files(
		("localisation", "localization"),
		r"(?m)^\s*[A-Z0-9]{3}\s*:\d*\s*[\"']",
		"*.yml",
	):
			data = path.read_bytes()
			for match in BASE_LOC_BYTES_RE.finditer(data):
				tag = match.group(1).decode("ascii")
				key = (tag, "base_localisation_key", str(path))
				if key in seen:
					continue
				seen.add(key)
				definitions.append(TagDefinition(tag, root_kind, root_name, "base_localisation_key", str(path), "three-character base localisation key"))

	history_dir = root / "history" / "countries"
	if history_dir.is_dir():
		for path in sorted(history_dir.rglob("*.txt")):
			match = HISTORY_COUNTRY_RE.fullmatch(path.name)
			if not match:
				continue
			tag = match.group(1).upper()
			key = (tag, "country_history_filename", str(path))
			if key in seen:
				continue
			seen.add(key)
			definitions.append(TagDefinition(tag, root_kind, root_name, "country_history_filename", str(path), "HOI4 country history file"))

	flag_dir = root / "gfx" / "flags"
	if flag_dir.is_dir():
		for path in flag_dir.rglob("*.tga"):
			match = FLAG_RE.fullmatch(path.name)
			if not match:
				continue
			tag = match.group(1).upper()
			key = (tag, "flag_asset", str(path))
			if key in seen:
				continue
			seen.add(key)
			definitions.append(TagDefinition(tag, root_kind, root_name, "flag_asset", str(path), "HOI4 flag asset"))

	return definitions


def scan_current_repo_non_event6(repo_root: Path, event6_tag_file: Path) -> list[TagDefinition]:
	tag_dir = repo_root / "common" / "country_tags"
	definitions: list[TagDefinition] = []
	for path in sorted(tag_dir.rglob("*.txt")):
		if path.resolve() == event6_tag_file.resolve():
			continue
		text = decode_text(path)
		for match in TAG_DEFINITION_RE.finditer(text):
			definitions.append(
				TagDefinition(
					tag=match.group(1),
					root_kind="chaos_redux_non_event6",
					root_name="chaos_redux",
					use_kind="country_tag_definition",
					file=str(path),
					country_path=match.group(2).replace("\\", "/"),
				)
			)
	return definitions


def scan_current_repo_non_event6_extended(repo_root: Path, event6_tags: set[str]) -> list[TagDefinition]:
	"""Return extended Chaos Redux surfaces that do not belong to Event 006."""
	definitions: list[TagDefinition] = []
	for definition in scan_extended_tag_surfaces(repo_root, "chaos_redux_non_event6", "chaos_redux"):
		path = Path(definition.file)
		try:
			relative = path.resolve().relative_to(repo_root.resolve()).as_posix().lower()
		except ValueError:
			relative = path.as_posix().lower()
		if "006_independence_wave" in relative or "event 006 country shell" in relative:
			continue
		if definition.use_kind == "flag_asset" and definition.tag in event6_tags:
			continue
		definitions.append(definition)
	return definitions


def parse_event6_tags(path: Path) -> list[dict[str, str]]:
	rows: list[dict[str, str]] = []
	for match in EVENT6_TAG_RE.finditer(decode_text(path)):
		rows.append({"tag": match.group(1), "package_id": match.group(2), "identity": match.group(3).strip()})
	return rows


def parse_registry(path: Path) -> list[dict[str, str]]:
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		return list(csv.DictReader(handle))


def vanilla_names(game_root: Path, definitions: list[TagDefinition]) -> dict[str, set[str]]:
	names: dict[str, set[str]] = defaultdict(set)
	for definition in definitions:
		stem = Path(definition.country_path).stem
		stem = re.sub(r"^[A-Z0-9]{3}[-_ ]+", "", stem)
		names[definition.tag].add(stem.replace("_", " "))

	english = game_root / "localisation" / "english"
	if english.is_dir():
		known_tags = {definition.tag for definition in definitions}
		for path in sorted(english.rglob("*.yml")):
			text = decode_text(path)
			for match in LOC_RE.finditer(text):
				if match.group(1) in known_tags:
					value = match.group(2).strip()
					if value and "$" not in value and "[" not in value:
						names[match.group(1)].add(value)
	return names


def strip_country_loc_suffix(key: str) -> str:
	for suffix in (
		"_democratic_DEF",
		"_democratic_ADJ",
		"_communism_DEF",
		"_communism_ADJ",
		"_fascism_DEF",
		"_fascism_ADJ",
		"_neutrality_DEF",
		"_neutrality_ADJ",
		"_democratic",
		"_communism",
		"_fascism",
		"_neutrality",
		"_DEF",
		"_ADJ",
	):
		if key.endswith(suffix):
			return key[: -len(suffix)]
	return key


def vanilla_cosmetic_names(game_root: Path) -> dict[str, set[str]]:
	"""Return English names for every vanilla cosmetic-country identity."""
	cosmetic_ids: set[str] = set()
	countries_dir = game_root / "common" / "countries"
	if countries_dir.is_dir():
		for path in sorted(countries_dir.glob("*cosmetic*.txt")):
			cosmetic_ids.update(COSMETIC_DEFINITION_RE.findall(decode_text(path)))

	names: dict[str, set[str]] = defaultdict(set)
	english = game_root / "localisation" / "english"
	if english.is_dir() and cosmetic_ids:
		for path in sorted(english.rglob("*.yml")):
			for match in LOC_KEY_VALUE_RE.finditer(decode_text(path)):
				base_key = strip_country_loc_suffix(match.group(1))
				if base_key not in cosmetic_ids:
					continue
				value = match.group(2).strip()
				if value and "$" not in value and "[" not in value:
					names[base_key].add(value)
	return names


def identity_matches(
	registry_rows: list[dict[str, str]],
	names_by_tag: dict[str, set[str]],
	names_by_cosmetic: dict[str, set[str]],
) -> list[dict[str, object]]:
	flat: list[tuple[str, str, str, str, str]] = []
	for tag, names in names_by_tag.items():
		for name in names:
			normal = normalize_name(name)
			core = normalize_name(name, remove_state_words=True)
			if normal:
				flat.append(("country_tag", tag, name, normal, core))
	for cosmetic, names in names_by_cosmetic.items():
		for name in names:
			normal = normalize_name(name)
			core = normalize_name(name, remove_state_words=True)
			if normal:
				flat.append(("cosmetic_tag", cosmetic, name, normal, core))

	results: list[dict[str, object]] = []
	for row in registry_rows:
		if row.get("tag_resolution") != "reserve_new_event6_X_tag":
			continue
		identity = row.get("working_name_not_final_localisation", "")
		normal = normalize_name(identity)
		core = normalize_name(identity, remove_state_words=True)
		candidates: list[tuple[float, str, str, str, str]] = []
		for vanilla_kind, vanilla_identifier, vanilla_name, vanilla_normal, vanilla_core in flat:
			exact = normal == vanilla_normal
			core_exact = bool(core and vanilla_core and core == vanilla_core)
			score = max(
				SequenceMatcher(None, normal, vanilla_normal).ratio(),
				SequenceMatcher(None, core, vanilla_core).ratio() if core and vanilla_core else 0.0,
			)
			core_tokens = set(core.split())
			vanilla_tokens = set(vanilla_core.split())
			multi_token_subset = (
				len(core_tokens) > 1
				and len(vanilla_tokens) > 1
				and (core_tokens.issubset(vanilla_tokens) or vanilla_tokens.issubset(core_tokens))
			)
			if exact:
				confidence = "exact"
				score = 1.0
			elif core_exact or multi_token_subset:
				confidence = "exact_after_state_words"
				score = 0.99
			elif score >= 0.82:
				confidence = "manual_review"
			else:
				continue
			candidates.append((score, vanilla_kind, vanilla_identifier, vanilla_name, confidence))
		for score, vanilla_kind, vanilla_identifier, vanilla_name, confidence in sorted(candidates, reverse=True)[:8]:
			results.append(
				{
					"package_id": row.get("package_id", ""),
					"identity": identity,
					"proposed_tag": row.get("resolved_tag", ""),
					"vanilla_kind": vanilla_kind,
					"vanilla_identifier": vanilla_identifier,
					"vanilla_name": vanilla_name,
					"confidence": confidence,
					"similarity": round(score, 4),
				}
			)
	return results


def markdown_report(data: dict[str, object]) -> str:
	lines = [
		"# Event 006 installed country-tag and vanilla-reuse audit",
		"",
		f"Audit date: {data['audit_date']}",
		"",
		"## Binding result",
		"",
		f"- Candidate registry rows: **{data['registry_package_count']}**.",
		f"- Reserved Event 006 tags scanned: **{data['event6_reserved_tag_count']}**.",
		f"- Registered vanilla-tag reuse rows: **{data['reused_registry_count']}**.",
		f"- Non-selectable vanilla route-overlay rows: **{data['overlay_registry_count']}**.",
		f"- Engine- or OS-reserved three-character namespaces excluded: **{', '.join(data['engine_reserved_namespaces'])}**.",
		f"- Installed Workshop directories scanned: **{data['workshop_directory_count']}**.",
		f"- Workshop directories containing country-tag definitions: **{data['workshop_roots_with_tags']}**.",
		f"- External and vanilla country-tag definitions parsed: **{data['external_definition_count']}**.",
		f"- External and vanilla alias/cosmetic/history/localisation/flag tag uses parsed: **{data['external_alias_cosmetic_definition_count']}**.",
		f"- Other Chaos Redux country-tag definitions parsed: **{data['chaos_redux_non_event6_definition_count']}**.",
		f"- Other Chaos Redux alias/cosmetic/history/localisation/flag tag uses parsed: **{data['chaos_redux_non_event6_extended_surface_count']}**.",
		f"- Reserved-tag collisions: **{len(data['collisions'])}**.",
		f"- Packages with exact or state-word-normalized vanilla identity matches requiring reuse review: **{data['binding_identity_package_count']}**.",
		f"- Packages with fuzzy identity matches requiring manual review: **{data['manual_identity_package_count']}**.",
		f"- Collision-free unused `??X` replacement candidates: **{len(data['safe_x_tag_pool'])}**.",
		"",
	]

	if data["collisions"]:
		lines.extend(("## Reserved-tag collisions", "", "| Event 006 | Identity | Conflicting registry | Definition |", "| --- | --- | --- | --- |"))
		for collision in data["collisions"]:
			for definition in collision["definitions"]:
				lines.append(
					f"| `{collision['tag']}` / {collision['package_id']} | {collision['identity']} | "
					f"{definition['root_kind']} `{definition['root_name']}` / {definition['use_kind']} | `{definition['file']}` |"
				)
		lines.append("")
	else:
		lines.extend(("## Reserved-tag collisions", "", "No reserved Event 006 tag collides with the scanned installed registries.", ""))

	lines.extend(("## Vanilla identity comparison", ""))
	if data["identity_matches"]:
		lines.extend(("| Event 006 package | Proposed identity/tag | Vanilla candidate | Confidence |", "| --- | --- | --- | --- |"))
		for match in data["identity_matches"]:
			lines.append(
				f"| {match['package_id']} | {match['identity']} / `{match['proposed_tag']}` | "
				f"{match['vanilla_name']} / {match['vanilla_kind']} `{match['vanilla_identifier']}` | {match['confidence']} ({match['similarity']}) |"
			)
		lines.append("")
	else:
		lines.extend(("No name-level vanilla reuse candidates were found.", ""))

	lines.extend(
		(
			"Exact and `exact_after_state_words` matches are binding blockers until the identity is either switched to the vanilla tag or documented as a distinct polity. `manual_review` matches are discovery leads, not automatic remaps.",
			"",
			"## Reused-tag validation",
			"",
			f"- Registry rows already marked as reused: **{data['reused_registry_count']}**.",
			f"- Reused rows whose tag is present in vanilla: **{data['reused_in_vanilla_count']}**.",
			f"- Reused rows absent from vanilla but registered by Chaos Redux or installed mods: **{len(data['reused_not_in_vanilla'])}**.",
			"",
		)
	)
	if data["duplicate_resolved_tags"]:
		lines.extend(("## Shared resolved-tag review", ""))
		for tag, rows in data["duplicate_resolved_tags"].items():
			packages = ", ".join(f"{row['package_id']} {row['identity']}" for row in rows)
			lines.append(f"- `{tag}`: {packages}")
		lines.extend(("", "Shared tags require mutually exclusive package reservation and package-specific readiness/origin gates.", ""))
	if data["reused_not_in_vanilla"]:
		for row in data["reused_not_in_vanilla"]:
			lines.append(f"- {row['package_id']} {row['identity']}: `{row['resolved_tag']}`")
		lines.append("")

	lines.extend(
		(
			"## Safe replacement pool",
			"",
			"The following tags end in `X` and were unused by vanilla, Chaos Redux, and every scanned installed mod at audit time. They are candidates only; a remap must update every gameplay, localisation, history, asset, manifest, scenario, specification, documentation, and catalog reference together.",
			"",
			"`" + " ".join(data["safe_x_tag_pool"]) + "`",
			"",
			"## Scope and limitations",
			"",
			"- The audit parses country definitions, `common/country_tag_aliases`, top-level three-character cosmetic-country blocks, concrete `set_cosmetic_tag` call sites, country-history filenames, exact three-character base localisation keys, and three-character HOI4 flag filenames.",
			"- Engine- and OS-reserved three-character namespaces are excluded before collision scoring or replacement-pool generation. `GFX` is reserved for HOI4 sprite/interface identifiers; `AUX`, `CON`, `NUL`, and `PRN` are reserved Windows DOS device basenames and cannot safely back country, history, localisation, or flag filenames.",
			"- The scan is intentionally over-inclusive: it audits every installed Workshop directory, not only enabled playset mods.",
			"- Identity comparison uses vanilla country-definition basenames and English localisation. Exact matches block acceptance; fuzzy matches require historical/manual review and may represent related but distinct polities.",
			"- Cosmetic tags have no single engine registry, so call sites, localisation, and flags are treated as collision evidence. A localisation-only hit can be over-inclusive but is safer than silently taking another mod's route identity.",
			"- Tags constructed dynamically through meta effects, scripted localisation, non-text archives, or filenames outside the standard HOI4 folders require manual review; no such construction should be assumed collision-free.",
			"- This report does not rename tags. It is the evidence gate for a reviewed repository-wide migration.",
			"",
			"## Input fingerprints",
			"",
			f"- Event 006 tag registry SHA-256: `{data['event6_tag_file_sha256']}`",
			f"- Candidate matrix SHA-256: `{data['registry_sha256']}`",
			"",
		)
	)
	return "\n".join(lines)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
	parser.add_argument("--game-root", type=Path, default=Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"))
	parser.add_argument("--workshop-root", type=Path, default=Path(r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360"))
	parser.add_argument("--local-mod-root", type=Path)
	parser.add_argument("--write-reports", action="store_true")
	parser.add_argument("--report-dir", type=Path)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	repo_root = args.repo_root.resolve()
	local_mod_root = (args.local_mod_root or repo_root.parent).resolve()
	event6_tag_file = repo_root / "common" / "country_tags" / "006_independence_wave_countries.txt"
	registry_file = repo_root / "docs" / "specs" / "006_independence_wave_specs" / "matrices" / "006_candidate_country_registry.csv"
	if not event6_tag_file.is_file() or not registry_file.is_file():
		raise FileNotFoundError("Event 006 tag file or candidate registry is missing")

	event6_rows = parse_event6_tags(event6_tag_file)
	registry_rows = parse_registry(registry_file)
	if len(registry_rows) != 206:
		raise RuntimeError(f"Expected 206 candidate rows, parsed {len(registry_rows)}")
	expected_reserved = sum(row.get("tag_resolution") == "reserve_new_event6_X_tag" for row in registry_rows)
	if len(event6_rows) != expected_reserved:
		raise RuntimeError(f"Expected {expected_reserved} reserved Event 006 tags from the matrix, parsed {len(event6_rows)}")
	custom_registry_mapping = {
		row.get("package_id", ""): row.get("resolved_tag", "")
		for row in registry_rows
		if row.get("tag_resolution") == "reserve_new_event6_X_tag"
	}
	parsed_event6_mapping = {row["package_id"]: row["tag"] for row in event6_rows}
	if len(custom_registry_mapping) != expected_reserved or len(parsed_event6_mapping) != len(event6_rows):
		raise RuntimeError("Duplicate or missing Event 006 package ids prevent tag mapping validation")
	if custom_registry_mapping != parsed_event6_mapping:
		raise RuntimeError("The Event 006 tag file and candidate registry package-to-tag mappings differ")
	custom_registry_tags = set(custom_registry_mapping.values())
	parsed_event6_tags = set(parsed_event6_mapping.values())
	if any(not re.fullmatch(r"[A-Z0-9]{2}X", tag) for tag in custom_registry_tags):
		raise RuntimeError("A custom Event 006 tag does not end in X")
	reserved_namespace_tags = sorted(custom_registry_tags & ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES.keys())
	if reserved_namespace_tags:
		details = ", ".join(
			f"{tag} ({ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES[tag]})"
			for tag in reserved_namespace_tags
		)
		raise RuntimeError(f"Event 006 consumes engine- or OS-reserved namespace tags: {details}")
	overlay_rows = [row for row in registry_rows if row.get("automatic_pool_disposition") == "vanilla_route_overlay_only"]
	if any(row.get("resolved_tag") for row in overlay_rows):
		raise RuntimeError("A vanilla route overlay has a standalone resolved tag")

	vanilla_defs = scan_tag_directory(args.game_root, "vanilla", "Hearts of Iron IV")
	vanilla_extended_defs = scan_extended_tag_surfaces(args.game_root, "vanilla", "Hearts of Iron IV")
	external_defs: list[TagDefinition] = list(vanilla_defs)
	external_extended_defs: list[TagDefinition] = list(vanilla_extended_defs)
	workshop_dirs = sorted(path for path in args.workshop_root.iterdir() if path.is_dir()) if args.workshop_root.is_dir() else []
	workshop_roots_with_tags = 0
	for mod_root in workshop_dirs:
		definitions = scan_tag_directory(mod_root, "workshop", mod_root.name)
		if definitions:
			workshop_roots_with_tags += 1
		external_defs.extend(definitions)
		external_extended_defs.extend(scan_extended_tag_surfaces(mod_root, "workshop", mod_root.name))

	if local_mod_root.is_dir():
		for mod_root in sorted(path for path in local_mod_root.iterdir() if path.is_dir()):
			if mod_root.resolve() == repo_root:
				continue
			external_defs.extend(scan_tag_directory(mod_root, "local_mod", mod_root.name))
			external_extended_defs.extend(scan_extended_tag_surfaces(mod_root, "local_mod", mod_root.name))

	non_event6_defs = scan_current_repo_non_event6(repo_root, event6_tag_file)
	non_event6_extended_defs = scan_current_repo_non_event6_extended(repo_root, parsed_event6_tags)
	all_conflict_defs = external_defs + external_extended_defs + non_event6_defs + non_event6_extended_defs
	definitions_by_tag: dict[str, list[TagDefinition]] = defaultdict(list)
	for definition in all_conflict_defs:
		definitions_by_tag[definition.tag].append(definition)

	collisions: list[dict[str, object]] = []
	for row in event6_rows:
		definitions = definitions_by_tag.get(row["tag"], [])
		if definitions:
			collisions.append(
				{
					**row,
					"definitions": [definition.__dict__ for definition in definitions],
				}
			)

	names_by_tag = vanilla_names(args.game_root, vanilla_defs)
	names_by_cosmetic = vanilla_cosmetic_names(args.game_root)
	matches = identity_matches(registry_rows, names_by_tag, names_by_cosmetic)
	binding_matches = [match for match in matches if match["confidence"] != "manual_review"]
	manual_matches = [match for match in matches if match["confidence"] == "manual_review"]
	binding_packages = sorted({str(match["package_id"]) for match in binding_matches})
	manual_packages = sorted({str(match["package_id"]) for match in manual_matches})

	vanilla_tags = {definition.tag for definition in vanilla_defs}
	all_used_tags = {definition.tag for definition in all_conflict_defs}
	all_used_tags.update(row["tag"] for row in event6_rows)
	all_used_tags.update(ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES)
	all_used_tags.update(
		row.get("provisional_new_tag", "")
		for row in registry_rows
		if re.fullmatch(r"[A-Z0-9]{3}", row.get("provisional_new_tag", ""))
	)
	safe_pool = [f"{first}{second}X" for first in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for second in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if f"{first}{second}X" not in all_used_tags]

	reused_rows = [row for row in registry_rows if row.get("tag_resolution") == "reuse_registered_tag"]
	reused_in_vanilla = [row for row in reused_rows if row.get("resolved_tag") in vanilla_tags]
	reused_not_in_vanilla = [
		{
			"package_id": row.get("package_id", ""),
			"identity": row.get("working_name_not_final_localisation", ""),
			"resolved_tag": row.get("resolved_tag", ""),
		}
		for row in reused_rows
		if row.get("resolved_tag") not in vanilla_tags
	]
	resolved_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
	for row in registry_rows:
		resolved_tag = row.get("resolved_tag", "")
		if resolved_tag:
			resolved_rows[resolved_tag].append(
				{
					"package_id": row.get("package_id", ""),
					"identity": row.get("working_name_not_final_localisation", ""),
					"tag_resolution": row.get("tag_resolution", ""),
					"automatic_pool_disposition": row.get("automatic_pool_disposition", ""),
				}
			)
	duplicate_resolved_tags = {tag: rows for tag, rows in sorted(resolved_rows.items()) if len(rows) > 1}

	data: dict[str, object] = {
		"audit_date": date.today().isoformat(),
		"registry_package_count": len(registry_rows),
		"event6_reserved_tag_count": len(event6_rows),
		"overlay_registry_count": len(overlay_rows),
		"engine_reserved_namespaces": sorted(ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES),
		"workshop_directory_count": len(workshop_dirs),
		"workshop_roots_with_tags": workshop_roots_with_tags,
		"external_definition_count": len(external_defs),
		"external_alias_cosmetic_definition_count": len(external_extended_defs),
		"chaos_redux_non_event6_definition_count": len(non_event6_defs),
		"chaos_redux_non_event6_extended_surface_count": len(non_event6_extended_defs),
		"collisions": collisions,
		"identity_matches": matches,
		"binding_identity_match_count": len(binding_matches),
		"manual_identity_match_count": len(manual_matches),
		"binding_identity_package_count": len(binding_packages),
		"manual_identity_package_count": len(manual_packages),
		"reused_registry_count": len(reused_rows),
		"reused_in_vanilla_count": len(reused_in_vanilla),
		"reused_not_in_vanilla": reused_not_in_vanilla,
		"vanilla_cosmetic_identity_count": len(names_by_cosmetic),
		"duplicate_resolved_tags": duplicate_resolved_tags,
		"safe_x_tag_pool": safe_pool,
		"event6_tag_file_sha256": file_sha256(event6_tag_file),
		"registry_sha256": file_sha256(registry_file),
		"scan_roots": {
			"game_root": str(args.game_root),
			"workshop_root": str(args.workshop_root),
			"local_mod_root": str(local_mod_root),
			"repo_root": str(repo_root),
		},
	}

	print(json.dumps({key: value for key, value in data.items() if key not in {"safe_x_tag_pool", "collisions", "identity_matches"}}, indent=2))
	print(f"collisions={len(collisions)} identity_matches={len(matches)} safe_x_tags={len(safe_pool)}")

	if args.write_reports:
		report_dir = args.report_dir or repo_root / "docs" / "plans" / "006_independence_wave_plans" / "tag_audit"
		report_dir.mkdir(parents=True, exist_ok=True)
		report_slug = date.today().strftime("%Y_%m_%d")
		(report_dir / f"006_installed_tag_collision_audit_{report_slug}.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
		(report_dir / f"006_installed_tag_collision_audit_{report_slug}.md").write_text(markdown_report(data), encoding="utf-8")
		with (report_dir / f"006_installed_tag_collisions_{report_slug}.csv").open("w", encoding="utf-8-sig", newline="") as handle:
			writer = csv.DictWriter(handle, fieldnames=("tag", "package_id", "identity", "root_kind", "root_name", "use_kind", "file", "country_path"))
			writer.writeheader()
			for collision in collisions:
				for definition in collision["definitions"]:
					writer.writerow({"tag": collision["tag"], "package_id": collision["package_id"], "identity": collision["identity"], **definition})
		with (report_dir / f"006_vanilla_identity_review_{report_slug}.csv").open("w", encoding="utf-8-sig", newline="") as handle:
			writer = csv.DictWriter(handle, fieldnames=("package_id", "identity", "proposed_tag", "vanilla_kind", "vanilla_identifier", "vanilla_name", "confidence", "similarity"))
			writer.writeheader()
			writer.writerows(matches)


if __name__ == "__main__":
	main()
