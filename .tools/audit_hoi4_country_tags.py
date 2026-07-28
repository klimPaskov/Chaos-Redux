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
import zipfile
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
EVENT6_FORMABLE_COSMETIC_RE = re.compile(r'^([A-Z0-9]{3})\s*=\s*\{', re.MULTILINE)
EVENT6_SET_COSMETIC_RE = re.compile(r'\bset_cosmetic_tag\s*=\s*([A-Z0-9]{3})\b')
SET_COSMETIC_ANY_RE = re.compile(rb'\bset_cosmetic_tag\s*=\s*([A-Za-z0-9_]+)\b')
BASE_LOC_ANY_RE = re.compile(r'(?m)^\s*([A-Za-z0-9_]+)\s*:\d*\s*["\']')
LOC_RE = re.compile(r'^\s*([A-Z0-9]{3})(?:_(?:DEF|ADJ|democratic|communism|fascism|neutrality))?\s*:\d*\s*["\'](.+?)["\']\s*$', re.MULTILINE)
LOC_KEY_VALUE_RE = re.compile(r'^\s*([A-Za-z0-9_]+)\s*:\d*\s*["\'](.+?)["\']\s*$', re.MULTILINE)
COSMETIC_DEFINITION_RE = re.compile(r'^([A-Za-z0-9_]+)\s*=\s*\{', re.MULTILINE)
ALIAS_RE = re.compile(r'^\s*([A-Z0-9]{3})\s*=\s*\{', re.MULTILINE)
COSMETIC_BYTES_RE = re.compile(rb'\bset_cosmetic_tag\s*=\s*([A-Z0-9]{3})\b')
BASE_LOC_BYTES_RE = re.compile(rb'(?m)^\s*([A-Z0-9]{3})\s*:\d*\s*["\']')
FLAG_RE = re.compile(r'^([A-Z0-9]{3})(?:_(?:communism|democratic|fascism|neutrality))?\.tga$', re.IGNORECASE)
HISTORY_COUNTRY_RE = re.compile(r'^([A-Z0-9]{3}).*\.txt$', re.IGNORECASE)
ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES = {
	"AND": "offline HOI4 wiki forbidden country-tag token",
	"GFX": "HOI4 sprite and interface graphics identifier namespace",
	"AUX": "Windows reserved DOS device basename; country, history, localisation, and flag files cannot be opened reliably",
	"CON": "Windows reserved DOS device basename",
	"LOG": "offline HOI4 wiki forbidden country-tag token",
	"NOT": "offline HOI4 wiki forbidden country-tag token",
	"NUM": "offline HOI4 wiki forbidden country-tag token",
	"NUL": "Windows reserved DOS device basename",
	"OOB": "offline HOI4 wiki forbidden country-tag token",
	"PRN": "Windows reserved DOS device basename",
	"RED": "offline HOI4 wiki forbidden country-tag token",
	"TAG": "offline HOI4 wiki forbidden country-tag token",
}
EVENT6_FORMABLE_COSMETIC_IDENTITIES = {
	"KCX": ("FORM-01", "Celtic Congress"),
	"NUX": ("FORM-02", "North Atlantic Union"),
	"LCX": ("FORM-03", "Confederation of the Low Countries"),
	"RLX": ("FORM-04", "Rhenish League"),
	"MIX": ("FORM-05", "Mediterranean Island League"),
	"PFX": ("FORM-48", "Pacific Regional Federation"),
	"MFX": ("FORM-39", "Melanesian Federation"),
}
REQUIRED_MANUAL_IDENTITY_PACKAGES = {
	"IW-011",
	"IW-018",
	"IW-019",
	"IW-037",
	"IW-061",
	"IW-064",
	"IW-100",
	"IW-117",
	"IW-144",
	"IW-159",
	"IW-163",
	"IW-169",
	"IW-174",
	"IW-190",
	"IW-193",
	"IW-203",
	"IW-205",
	"IW-206",
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
GENERIC_IDENTITY_TOKENS = {
	"island",
	"islands",
}


@dataclass(frozen=True)
class TagDefinition:
	tag: str
	root_kind: str
	root_name: str
	use_kind: str
	file: str
	country_path: str


def decode_bytes(data: bytes) -> str:
	for encoding in ("utf-8-sig", "utf-8", "cp1252"):
		try:
			return data.decode(encoding)
		except UnicodeDecodeError:
			continue
	return data.decode("utf-8", errors="replace")


def decode_text(path: Path) -> str:
	return decode_bytes(path.read_bytes())


def file_sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def stable_rows_sha256(rows: list[dict[str, object]]) -> str:
	"""Hash a normalized evidence inventory independent of traversal order."""
	normalized = json.dumps(
		sorted(rows, key=lambda row: json.dumps(row, sort_keys=True, ensure_ascii=False)),
		sort_keys=True,
		ensure_ascii=False,
		separators=(",", ":"),
	).encode("utf-8")
	return hashlib.sha256(normalized).hexdigest()


def definition_inventory_sha256(definitions: list[TagDefinition]) -> str:
	return stable_rows_sha256([definition.__dict__ for definition in definitions])


def archive_inventory_sha256(paths: list[Path]) -> str:
	rows: list[dict[str, object]] = []
	for path in sorted({candidate.resolve() for candidate in paths}, key=lambda candidate: str(candidate).lower()):
		rows.append(
			{
				"path": str(path),
				"size": path.stat().st_size,
				"sha256": file_sha256(path),
			}
		)
	return stable_rows_sha256(rows)


def file_inventory_sha256(paths: list[Path]) -> str:
	"""Hash a fixed group of source files with their resolved paths."""
	rows = [
		{
			"path": str(path.resolve()),
			"size": path.stat().st_size,
			"sha256": file_sha256(path),
		}
		for path in sorted(paths, key=lambda candidate: str(candidate.resolve()).lower())
	]
	return stable_rows_sha256(rows)


def matching_surface_files(root: Path, subtrees: tuple[str, ...], pattern: str, glob: str) -> list[Path]:
	"""Return text files matching a surface regex without broad file reads."""
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


def scan_event6_custom_cosmetic_surfaces(
	root: Path,
	root_kind: str,
	root_name: str,
	identifiers: set[str],
) -> list[TagDefinition]:
	"""Scan exact all-length Event 006 cosmetic IDs without changing 3-char metrics."""
	definitions: list[TagDefinition] = []
	seen: set[tuple[str, str, str]] = set()

	def add(tag: str, use_kind: str, file: str, detail: str) -> None:
		if tag not in identifiers:
			return
		key = (tag, use_kind, file)
		if key in seen:
			return
		seen.add(key)
		definitions.append(TagDefinition(tag, root_kind, root_name, use_kind, file, detail))

	for subtree in ("common/country_tag_aliases", "common/countries"):
		directory = root / subtree
		if not directory.is_dir():
			continue
		for path in sorted(directory.rglob("*.txt")):
			for match in COSMETIC_DEFINITION_RE.finditer(decode_text(path)):
				use_kind = "country_tag_alias" if subtree.endswith("country_tag_aliases") else "cosmetic_country_definition"
				add(match.group(1), use_kind, str(path), "exact Event 006 custom cosmetic definition")

	set_pattern = r"\bset_cosmetic_tag\s*=\s*[A-Za-z0-9_]+\b"
	for path in matching_surface_files((root), ("common", "events", "history"), set_pattern, "*.txt"):
		for match in SET_COSMETIC_ANY_RE.finditer(path.read_bytes()):
			add(match.group(1).decode("ascii"), "set_cosmetic_tag", str(path), "exact Event 006 custom cosmetic call site")

	loc_pattern = r"(?m)^\s*[A-Za-z0-9_]+\s*:\d*\s*[\"']"
	for glob in ("*.yml", "*.yaml"):
		for path in matching_surface_files(root, ("localisation", "localization"), loc_pattern, glob):
			for match in BASE_LOC_ANY_RE.finditer(decode_text(path)):
				add(match.group(1), "base_localisation_key", str(path), "exact Event 006 custom cosmetic localisation key")

	flag_dir = root / "gfx" / "flags"
	if flag_dir.is_dir():
		flag_patterns = {
			identifier: re.compile(
				rf"^{re.escape(identifier)}(?:_(?:communism|democratic|fascism|neutrality))?$",
				re.IGNORECASE,
			)
			for identifier in identifiers
		}
		for path in sorted(flag_dir.rglob("*.tga")):
			stem = path.stem
			for identifier, pattern in flag_patterns.items():
				if pattern.fullmatch(stem):
					add(identifier, "flag_asset", str(path), "exact Event 006 custom cosmetic flag asset")

	return definitions


def scan_zip_tag_surfaces(
	archive_path: Path,
	root_kind: str,
	root_name: str,
) -> tuple[list[TagDefinition], list[TagDefinition]]:
	"""Scan standard HOI4 tag-bearing paths inside one ZIP without extraction."""
	country_definitions: list[TagDefinition] = []
	extended_definitions: list[TagDefinition] = []
	seen: set[tuple[str, str, str]] = set()

	def in_tree(member_path: str, tree: str) -> bool:
		return member_path.startswith(f"{tree}/") or f"/{tree}/" in member_path

	def add_extended(tag: str, use_kind: str, member_file: str, detail: str) -> None:
		key = (tag, use_kind, member_file)
		if key in seen:
			return
		seen.add(key)
		extended_definitions.append(
			TagDefinition(tag, root_kind, root_name, use_kind, member_file, detail)
		)

	with zipfile.ZipFile(archive_path) as archive:
		for info in archive.infolist():
			if info.is_dir():
				continue
			member_name = info.filename.replace("\\", "/").lstrip("/")
			member_lower = member_name.lower()
			member_file = f"{archive_path}!/{member_name}"
			is_txt = member_lower.endswith(".txt")
			is_yml = member_lower.endswith((".yml", ".yaml"))
			needs_text = (
				is_txt
				and (
					in_tree(member_lower, "common/country_tags")
					or in_tree(member_lower, "common/country_tag_aliases")
					or in_tree(member_lower, "common/countries")
					or in_tree(member_lower, "common")
					or in_tree(member_lower, "events")
					or in_tree(member_lower, "history")
				)
			) or (
				is_yml
				and (
					in_tree(member_lower, "localisation")
					or in_tree(member_lower, "localization")
				)
			)
			data = archive.read(info) if needs_text else b""
			text = decode_bytes(data) if data else ""

			if is_txt and in_tree(member_lower, "common/country_tags"):
				for match in TAG_DEFINITION_RE.finditer(text):
					country_definitions.append(
						TagDefinition(
							tag=match.group(1),
							root_kind=root_kind,
							root_name=root_name,
							use_kind="country_tag_definition",
							file=member_file,
							country_path=match.group(2).replace("\\", "/"),
						)
					)

			if is_txt and in_tree(member_lower, "common/country_tag_aliases"):
				for match in ALIAS_RE.finditer(text):
					add_extended(match.group(1), "country_tag_alias", member_file, "archived alias block")

			if is_txt and in_tree(member_lower, "common/countries"):
				for match in COSMETIC_DEFINITION_RE.finditer(text):
					tag = match.group(1)
					if re.fullmatch(r"[A-Z0-9]{3}", tag):
						add_extended(tag, "cosmetic_country_definition", member_file, "archived top-level country cosmetic block")

			if is_txt and (
				in_tree(member_lower, "common")
				or in_tree(member_lower, "events")
				or in_tree(member_lower, "history")
			):
				for match in COSMETIC_BYTES_RE.finditer(data):
					add_extended(
						match.group(1).decode("ascii"),
						"set_cosmetic_tag",
						member_file,
						"archived effect call site",
					)

			if is_yml and (
				in_tree(member_lower, "localisation")
				or in_tree(member_lower, "localization")
			):
				for match in BASE_LOC_BYTES_RE.finditer(data):
					add_extended(
						match.group(1).decode("ascii"),
						"base_localisation_key",
						member_file,
						"archived three-character base localisation key",
					)

			if is_txt and in_tree(member_lower, "history/countries"):
				match = HISTORY_COUNTRY_RE.fullmatch(Path(member_name).name)
				if match:
					add_extended(
						match.group(1).upper(),
						"country_history_filename",
						member_file,
						"archived HOI4 country history file",
					)

			if in_tree(member_lower, "gfx/flags"):
				match = FLAG_RE.fullmatch(Path(member_name).name)
				if match:
					add_extended(
						match.group(1).upper(),
						"flag_asset",
						member_file,
						"archived HOI4 flag asset",
					)

	return country_definitions, extended_definitions


def scan_zip_event6_custom_cosmetic_surfaces(
	archive_path: Path,
	root_kind: str,
	root_name: str,
	identifiers: set[str],
) -> list[TagDefinition]:
	"""Scan exact all-length Event 006 cosmetic IDs in an embedded ZIP."""
	definitions: list[TagDefinition] = []
	seen: set[tuple[str, str, str]] = set()

	def in_tree(member_path: str, tree: str) -> bool:
		return member_path.startswith(f"{tree}/") or f"/{tree}/" in member_path

	def add(tag: str, use_kind: str, member_file: str, detail: str) -> None:
		if tag not in identifiers:
			return
		key = (tag, use_kind, member_file)
		if key in seen:
			return
		seen.add(key)
		definitions.append(TagDefinition(tag, root_kind, root_name, use_kind, member_file, detail))

	with zipfile.ZipFile(archive_path) as archive:
		for info in archive.infolist():
			if info.is_dir():
				continue
			member_name = info.filename.replace("\\", "/").lstrip("/")
			member_lower = member_name.lower()
			member_file = f"{archive_path}!/{member_name}"
			is_txt = member_lower.endswith(".txt")
			is_yml = member_lower.endswith((".yml", ".yaml"))
			needs_text = (is_txt and (
				in_tree(member_lower, "common/country_tag_aliases")
				or in_tree(member_lower, "common/countries")
				or in_tree(member_lower, "common")
				or in_tree(member_lower, "events")
				or in_tree(member_lower, "history")
			)) or (is_yml and (in_tree(member_lower, "localisation") or in_tree(member_lower, "localization")))
			data = archive.read(info) if needs_text else b""
			text = decode_bytes(data) if data else ""

			if is_txt and in_tree(member_lower, "common/country_tag_aliases"):
				for match in COSMETIC_DEFINITION_RE.finditer(text):
					add(match.group(1), "country_tag_alias", member_file, "archived exact Event 006 custom cosmetic definition")

			if is_txt and in_tree(member_lower, "common/countries"):
				for match in COSMETIC_DEFINITION_RE.finditer(text):
					add(match.group(1), "cosmetic_country_definition", member_file, "archived exact Event 006 custom cosmetic definition")

			if is_txt and (in_tree(member_lower, "common") or in_tree(member_lower, "events") or in_tree(member_lower, "history")):
				for match in SET_COSMETIC_ANY_RE.finditer(data):
					add(match.group(1).decode("ascii"), "set_cosmetic_tag", member_file, "archived exact Event 006 custom cosmetic call site")

			if is_yml and (in_tree(member_lower, "localisation") or in_tree(member_lower, "localization")):
				for match in BASE_LOC_ANY_RE.finditer(text):
					add(match.group(1), "base_localisation_key", member_file, "archived exact Event 006 custom cosmetic localisation key")

			if in_tree(member_lower, "gfx/flags"):
				stem = Path(member_name).stem
				for identifier in identifiers:
					pattern = re.compile(
						rf"^{re.escape(identifier)}(?:_(?:communism|democratic|fascism|neutrality))?$",
						re.IGNORECASE,
					)
					if pattern.fullmatch(stem):
						add(identifier, "flag_asset", member_file, "archived exact Event 006 custom cosmetic flag asset")

	return definitions


def scan_archives_under_root(
	root: Path,
	root_kind: str,
	root_name: str,
) -> tuple[list[Path], int, list[TagDefinition], list[TagDefinition]]:
	"""Scan ZIP archives and fail closed when an unsupported archive is present."""
	rg = shutil.which("rg")
	if rg:
		result = subprocess.run(
			[
				rg,
				"--files",
				"-g",
				"*.zip",
				"-g",
				"*.ZIP",
				"-g",
				"*.7z",
				"-g",
				"*.7Z",
				"-g",
				"*.rar",
				"-g",
				"*.RAR",
				str(root),
			],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True,
			encoding="utf-8",
			errors="replace",
		)
		if result.returncode not in (0, 1):
			raise RuntimeError(f"ripgrep failed while locating archives under {root}: {result.stderr}")
		archive_candidates = [Path(line) for line in result.stdout.splitlines() if line.strip()]
	else:
		archive_candidates = [
			path
			for path in root.rglob("*")
			if path.is_file() and path.suffix.lower() in {".zip", ".7z", ".rar"}
		]
	zip_paths = sorted(path for path in archive_candidates if path.suffix.lower() == ".zip")
	unsupported_paths = sorted(path for path in archive_candidates if path.suffix.lower() != ".zip")
	if unsupported_paths:
		raise RuntimeError(
			"Unsupported installed-mod archives prevent a complete tag audit: "
			+ ", ".join(str(path) for path in unsupported_paths)
		)

	country_definitions: list[TagDefinition] = []
	extended_definitions: list[TagDefinition] = []
	archives_with_tag_surfaces = 0
	for archive_path in zip_paths:
		archive_country_definitions, archive_extended_definitions = scan_zip_tag_surfaces(
			archive_path,
			root_kind,
			root_name,
		)
		if archive_country_definitions or archive_extended_definitions:
			archives_with_tag_surfaces += 1
		country_definitions.extend(archive_country_definitions)
		extended_definitions.extend(archive_extended_definitions)

	return zip_paths, archives_with_tag_surfaces, country_definitions, extended_definitions


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


def scan_current_repo_non_event6_extended(
	repo_root: Path,
	event6_tags: set[str],
	event6_history_paths: set[str],
) -> list[TagDefinition]:
	"""Return extended Chaos Redux surfaces that do not belong to Event 006."""
	definitions: list[TagDefinition] = []
	for definition in scan_extended_tag_surfaces(repo_root, "chaos_redux_non_event6", "chaos_redux"):
		path = Path(definition.file)
		try:
			relative = path.resolve().relative_to(repo_root.resolve()).as_posix().lower()
		except ValueError:
			relative = path.as_posix().lower()
		if definition.use_kind == "country_history_filename":
			# Only exact current Event 006 filenames whose normalized stem matches the
			# registry identity are owned. Any same-tag filename with another identity
			# remains collision evidence, including files under an Event 006-looking path.
			if relative in event6_history_paths:
				continue
		elif "006_independence_wave" in relative or "event 006 country shell" in relative:
			continue
		if definition.use_kind == "flag_asset" and definition.tag in event6_tags:
			continue
		definitions.append(definition)
	return definitions


def scan_current_repo_non_event6_custom_cosmetic_surfaces(
	repo_root: Path,
	identifiers: set[str],
	event6_history_paths: set[str],
) -> list[TagDefinition]:
	"""Return exact custom cosmetic surfaces outside Event 006-owned files."""
	definitions: list[TagDefinition] = []
	owned_flag_paths: set[str] = set()
	flag_dir = repo_root / "gfx" / "flags"
	if flag_dir.is_dir():
		flag_patterns = {
			identifier: re.compile(
				rf"^{re.escape(identifier)}(?:_(?:communism|democratic|fascism|neutrality))?$",
				re.IGNORECASE,
			)
			for identifier in identifiers
		}
		for path in flag_dir.rglob("*.tga"):
			if any(pattern.fullmatch(path.stem) for pattern in flag_patterns.values()):
				owned_flag_paths.add(path.resolve().relative_to(repo_root.resolve()).as_posix().lower())
	for definition in scan_event6_custom_cosmetic_surfaces(repo_root, "chaos_redux_non_event6", "chaos_redux", identifiers):
		path = Path(definition.file)
		try:
			relative = path.resolve().relative_to(repo_root.resolve()).as_posix().lower()
		except ValueError:
			relative = path.as_posix().lower()
		if definition.use_kind == "country_history_filename":
			if relative in event6_history_paths:
				continue
		elif definition.use_kind == "flag_asset" and relative in owned_flag_paths:
			continue
		elif "006_independence_wave" in relative or "event 006 country shell" in relative:
			continue
		definitions.append(definition)
	return definitions


def parse_event6_tags(path: Path) -> list[dict[str, str]]:
	rows: list[dict[str, str]] = []
	for match in EVENT6_TAG_RE.finditer(decode_text(path)):
		rows.append({"tag": match.group(1), "package_id": match.group(2), "identity": match.group(3).strip()})
	return rows


def parse_event6_formable_cosmetics(path: Path) -> list[dict[str, str]]:
	rows: list[dict[str, str]] = []
	for tag in EVENT6_FORMABLE_COSMETIC_RE.findall(decode_text(path)):
		if tag not in EVENT6_FORMABLE_COSMETIC_IDENTITIES:
			raise RuntimeError(f"Unreviewed Event 006 formable or cosmetic identity in {path}: {tag}")
		package_id, identity = EVENT6_FORMABLE_COSMETIC_IDENTITIES[tag]
		rows.append({"tag": tag, "package_id": package_id, "identity": identity})
	return rows


def parse_event6_custom_cosmetic_identifiers(path: Path) -> list[str]:
	"""Parse every all-length custom cosmetic identifier owned by Event 006."""
	identifiers = COSMETIC_DEFINITION_RE.findall(decode_text(path))
	if not identifiers:
		raise RuntimeError(f"Event 006 custom cosmetic registry is empty: {path}")
	if len(identifiers) != len(set(identifiers)):
		raise RuntimeError(f"Event 006 custom cosmetic registry contains duplicate identifiers: {path}")
	return identifiers


def parse_event6_custom_cosmetic_calls(repo_root: Path, identifiers: set[str]) -> set[str]:
	"""Return custom cosmetic identifiers used by Event 006 effects/events."""
	calls: set[str] = set()
	paths = list((repo_root / "common" / "scripted_effects").glob("006_independence_wave*.txt"))
	paths.extend((repo_root / "events").glob("006_independence_wave*.txt"))
	for path in sorted(paths):
		for match in SET_COSMETIC_ANY_RE.finditer(path.read_bytes()):
			identifier = match.group(1).decode("ascii")
			if identifier in identifiers:
				calls.add(identifier)
	return calls


def parse_event6_owned_history_filenames(
	repo_root: Path,
	event6_rows: list[dict[str, str]],
) -> tuple[set[str], list[dict[str, str]]]:
	"""Resolve the exact current Event 006 history filenames by tag and identity."""
	expected_identity = {row["tag"]: normalize_name(row["identity"]) for row in event6_rows}
	owned_paths: set[str] = set()
	owned_rows: list[dict[str, str]] = []
	history_dir = repo_root / "history" / "countries"
	if not history_dir.is_dir():
		return owned_paths, owned_rows
	for path in sorted(history_dir.rglob("*.txt")):
		match = HISTORY_COUNTRY_RE.fullmatch(path.name)
		if not match:
			continue
		tag = match.group(1).upper()
		if tag not in expected_identity:
			continue
		identity = path.stem[3:].lstrip(" -_")
		if normalize_name(identity) != expected_identity[tag]:
			# A same-tag history file with another identity is not owned by Event 006
			# and must remain collision evidence in the non-Event6 scan.
			continue
		relative = path.resolve().relative_to(repo_root.resolve()).as_posix().lower()
		owned_paths.add(relative)
		owned_rows.append({"tag": tag, "identity": identity, "file": relative})
	return owned_paths, owned_rows


def parse_event6_set_cosmetic_calls(repo_root: Path) -> set[str]:
	tags: set[str] = set()
	for path in sorted((repo_root / "common" / "scripted_effects").glob("006_independence_wave*.txt")):
		tags.update(EVENT6_SET_COSMETIC_RE.findall(decode_text(path)))
	return tags


def parse_manual_identity_dispositions(path: Path) -> list[dict[str, str]]:
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		rows = list(csv.DictReader(handle))
	required_columns = {
		"package_id",
		"proposed_identity",
		"proposed_tag",
		"vanilla_candidate",
		"disposition",
		"readiness_effect",
		"rationale",
		"required_action",
	}
	if not rows or not required_columns.issubset(rows[0]):
		raise RuntimeError(f"Manual identity disposition source has missing columns: {path}")
	package_ids = [row.get("package_id", "") for row in rows]
	if len(package_ids) != len(set(package_ids)):
		raise RuntimeError("Manual identity disposition source contains duplicate package ids")
	if not REQUIRED_MANUAL_IDENTITY_PACKAGES.issubset(package_ids):
		missing = ", ".join(sorted(REQUIRED_MANUAL_IDENTITY_PACKAGES - set(package_ids)))
		raise RuntimeError(f"Manual identity disposition source is missing required packages: {missing}")
	return rows


def extract_named_script_block(text: str, name: str) -> str:
	match = re.search(rf'(?m)^\s*{re.escape(name)}\s*=\s*\{{', text)
	if not match:
		raise RuntimeError(f"Required scripted block is missing: {name}")
	start = text.find("{", match.start())
	depth = 0
	for index in range(start, len(text)):
		if text[index] == "{":
			depth += 1
		elif text[index] == "}":
			depth -= 1
			if depth == 0:
				return text[start + 1:index]
	raise RuntimeError(f"Unclosed scripted block: {name}")


def parse_runtime_attested_package_ids(path: Path) -> set[str]:
	block = extract_named_script_block(
		decode_text(path),
		"has_independence_wave_runtime_package_content_attestation_for_execution_id",
	)
	return {
		f"IW-{numeric_id}"
		for numeric_id in re.findall(r'independence_wave_package_id\.iw_(\d{3})', block)
	}


def parse_registry(path: Path) -> list[dict[str, str]]:
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		return list(csv.DictReader(handle))


def parse_event6_formable_localisations(paths: list[Path]) -> dict[str, str]:
	values: dict[str, str] = {}
	for path in paths:
		for match in LOC_KEY_VALUE_RE.finditer(decode_text(path)):
			key = match.group(1)
			if key not in EVENT6_FORMABLE_COSMETIC_IDENTITIES:
				continue
			value = match.group(2).strip()
			if key in values and values[key] != value:
				raise RuntimeError(f"Conflicting base localisation for Event 006 formable tag {key}")
			values[key] = value
	return values


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
			long_core_tokens = {token for token in core_tokens if len(token) > 5 and token not in GENERIC_IDENTITY_TOKENS}
			long_vanilla_tokens = {token for token in vanilla_tokens if len(token) > 5 and token not in GENERIC_IDENTITY_TOKENS}
			long_token_overlap = bool(long_core_tokens & long_vanilla_tokens)
			long_token_similarity = max(
				(
					SequenceMatcher(None, event6_token, vanilla_token).ratio()
					for event6_token in long_core_tokens
					for vanilla_token in long_vanilla_tokens
				),
				default=0.0,
			)
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
			elif score >= 0.82 or long_token_overlap or long_token_similarity >= 0.88:
				confidence = "manual_review"
				score = max(score, long_token_similarity)
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
		f"- Reserved Event 006 country tags scanned: **{data['event6_country_tag_count']}**.",
		f"- Event 006 formable/cosmetic identity tags scanned: **{data['event6_formable_cosmetic_tag_count']}**.",
		f"- Unique Event 006-owned identifiers checked together: **{data['event6_owned_identifier_count']}**.",
		f"- All-length Event 006 custom cosmetic identifiers checked separately: **{data['event6_custom_cosmetic_identifier_count']}**.",
		f"- Exact Event 006-owned history filenames retained from the non-Event 006 scan: **{data['event6_history_owned_filename_count']}**.",
		f"- Registered vanilla-tag reuse rows: **{data['reused_registry_count']}**, using **{data['reused_unique_tag_count']}** unique vanilla tags.",
		f"- Non-selectable vanilla route-overlay rows: **{data['overlay_registry_count']}**.",
		f"- Engine-, offline-wiki-, or OS-reserved three-character namespaces excluded: **{', '.join(data['engine_reserved_namespaces'])}**.",
		f"- Installed Workshop directories scanned: **{data['workshop_directory_count']}**.",
		f"- Workshop directories containing country-tag definitions: **{data['workshop_roots_with_tags']}**.",
		f"- Embedded ZIP archives scanned without extraction: **{data['archive_file_count']}**.",
		f"- Embedded ZIP archives containing tag-bearing surfaces: **{data['archive_files_with_tag_surfaces']}**.",
		f"- Country-tag definitions parsed from embedded ZIP archives: **{data['archive_definition_count']}**.",
		f"- Alias/cosmetic/history/localisation/flag surfaces parsed from embedded ZIP archives: **{data['archive_extended_surface_count']}**.",
		f"- Sibling local mod directories scanned: **{data['local_mod_directory_count']}** ({', '.join(data['local_mod_directory_names']) or 'none'}).",
		f"- Sibling local mods containing country-tag or extended tag surfaces: **{data['local_mod_roots_with_tag_surfaces']}**.",
		f"- Literal country-tag definitions parsed from sibling local mods: **{data['local_mod_definition_count']}**.",
		f"- Alias/cosmetic/history/localisation/flag surfaces parsed from sibling local mods: **{data['local_mod_extended_surface_count']}**.",
		f"- External and vanilla country-tag definitions parsed: **{data['external_definition_count']}**.",
		f"- External and vanilla alias/cosmetic/history/localisation/flag tag uses parsed: **{data['external_alias_cosmetic_definition_count']}**.",
		f"- Other Chaos Redux country-tag definitions parsed: **{data['chaos_redux_non_event6_definition_count']}**.",
		f"- Other Chaos Redux alias/cosmetic/history/localisation/flag tag uses parsed: **{data['chaos_redux_non_event6_extended_surface_count']}**.",
		f"- Reserved-tag collisions: **{len(data['collisions'])}**.",
		f"- Packages with exact or state-word-normalized vanilla identity matches requiring reuse review: **{data['binding_identity_package_count']}**.",
		f"- Packages with fuzzy identity matches requiring manual review: **{data['manual_identity_package_count']}**.",
		f"- Recorded manual identity dispositions: **{data['manual_identity_disposition_count']}**.",
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
		lines.extend(("## Reserved-tag collisions", "", "No Event 006-owned country, formable, or cosmetic identifier collides with the scanned installed registries.", ""))

	lines.extend(("## Event 006 formable and cosmetic identities", "", "| Family | Identity | Tag |", "| --- | --- | --- |"))
	for row in data["event6_formable_cosmetic_rows"]:
		lines.append(f"| {row['package_id']} | {row['identity']} | `{row['tag']}` |")
	formable_count = len(data["event6_formable_cosmetic_rows"])
	reserved_count = data["event6_reserved_tag_count"]
	lines.extend(("", f"All {formable_count} tags are X-ending, unique against the {reserved_count} country reservations, present in the reviewed cosmetic registry, and used by an exact Event 006 `set_cosmetic_tag` adapter.", ""))

	lines.extend(("## All-length custom cosmetic coverage", "", f"Event 006 defines {data['event6_custom_cosmetic_identifier_count']} custom cosmetic identifiers, including the six three-character family colors and route identifiers longer than three characters.", "", "`" + " ".join(data["event6_custom_cosmetic_identifiers"]) + "`", "", f"Exact custom cosmetic surfaces parsed from vanilla, Workshop, archives, sibling mods, and non-Event 006 Chaos Redux: **{data['event6_custom_cosmetic_external_surface_count'] + data['event6_custom_cosmetic_non_event6_surface_count']}**.", ""))
	if data["event6_custom_cosmetic_collisions"]:
		lines.extend(("Custom cosmetic identifier collisions", "", "| Identifier | Conflicting registry | Definition |", "| --- | --- | --- |"))
		for collision in data["event6_custom_cosmetic_collisions"]:
			for definition in collision["definitions"]:
				lines.append(
					f"| `{collision['identifier']}` | {definition['root_kind']} `{definition['root_name']}` / {definition['use_kind']} | `{definition['file']}` |"
				)
		lines.append("")
	else:
		lines.extend(("Custom cosmetic identifier collisions", "", "No Event 006 custom cosmetic identifier collides with the scanned installed registries.", ""))

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
			"## Manual vanilla-identity dispositions",
			"",
		)
	)
	for row in data["manual_identity_dispositions"]:
		lines.append(
			f"- **{row['package_id']} {row['proposed_identity']} / `{row['proposed_tag']}`** against {row['vanilla_candidate']}: "
			f"`{row['disposition']}` / `{row['readiness_effect']}`. {row['rationale']} Required action: {row['required_action']}"
		)
	lines.extend(
		(
			"",
			"The binding curated cases remain disabled: IW-169 must be distinct from SIK and vanilla Turkestan content, IW-174 from NZL's Aotearoa route, IW-193 from MEX's indigenous route, and IW-203 from WLA and Araucania-and-Patagonia identities. If that proof cannot be made, their separate tags must be retired in favor of additive vanilla-carrier content.",
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
	lines.extend(("## Shared BIA and CHU readiness review", "", "| Tag | Package | Reservation group | Exact wrapper | Content attested | Scenario blocked | Runtime status |", "| --- | --- | --- | --- | --- | --- | --- |"))
	for row in data["shared_reused_tag_reviews"]:
		lines.append(
			f"| `{row['tag']}` | {row['package_id']} {row['identity']} | `{row['reservation_group']}` | "
			f"{row['exact_package_wrapper']} | {row['content_attested']} | {row['scenario_blocked']} | `{row['runtime_status']}` |"
		)
	attested_shared = [row["package_id"] for row in data["shared_reused_tag_reviews"] if row["runtime_status"] == "attested"]
	fail_closed_shared = [row["package_id"] for row in data["shared_reused_tag_reviews"] if row["runtime_status"] != "attested"]
	lines.extend(
		(
			"",
			"Both shared-tag pairs use one reservation group per tag, so the frozen planner cannot select both identities together. "
			+ (f"Exact wrapper plus static content attestation admits: {', '.join(attested_shared)}. " if attested_shared else "No shared-tag row is admitted. ")
			+ (f"Fail-closed rows: {', '.join(fail_closed_shared)}. " if fail_closed_shared else "No shared-tag row remains fail-closed. ")
			+ "The legacy generic content-ready flag has zero grants.",
			"",
		)
	)
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
			"- The existing country/tag metrics parse country definitions, `common/country_tag_aliases`, top-level three-character cosmetic-country blocks, concrete three-character `set_cosmetic_tag` call sites, country-history filenames, exact three-character base localisation keys, and three-character HOI4 flag filenames.",
			"- Event 006 custom cosmetic identifiers are also scanned separately at exact all-length definition, alias, call-site, localisation, and flag surfaces; this coverage does not change the existing three-character metrics.",
			"- Event 006 history ownership is path-backed: only current `history/countries` filenames whose three-character tag and normalized stem identity match the Event 006 registry are excluded from the non-Event 006 scan. A same-tag filename with another identity remains collision evidence.",
			"- Engine-, wiki-, and OS-reserved three-character namespaces are excluded before collision scoring or replacement-pool generation. The offline wiki forbids `NOT`, `AND`, `TAG`, `OOB`, `LOG`, `NUM`, and `RED`; `GFX` is reserved for sprite/interface identifiers; `AUX`, `CON`, `NUL`, and `PRN` are Windows DOS device basenames.",
			"- The scan is intentionally over-inclusive: it audits every installed Workshop directory, not only enabled playset mods, plus every sibling local mod directory beside Chaos Redux.",
			"- ZIP members under standard HOI4 tag, alias, country, event, history, localisation, and flag paths are scanned in memory without extraction. The audit fails closed if an installed `.7z` or `.rar` archive is present.",
			"- Identity comparison uses vanilla country-definition basenames and English localisation. Exact matches block acceptance; fuzzy matches require historical/manual review and may represent related but distinct polities.",
			"- Cosmetic tags have no single engine registry, so call sites, localisation, and flags are treated as collision evidence. A localisation-only hit can be over-inclusive but is safer than silently taking another mod's route identity.",
			"- Tags constructed dynamically through meta effects, scripted localisation, non-text archives, or filenames outside the standard HOI4 folders require manual review; no such construction should be assumed collision-free.",
			"- This report does not rename tags. It is the evidence gate for a reviewed repository-wide migration.",
			"",
			"## Input fingerprints",
			"",
			f"- Audit script SHA-256: `{data['audit_script_sha256']}`",
			f"- Event 006 tag registry SHA-256: `{data['event6_tag_file_sha256']}`",
			f"- Event 006 formable/cosmetic registry SHA-256: `{data['event6_formable_cosmetic_file_sha256']}`",
			f"- Candidate matrix SHA-256: `{data['registry_sha256']}`",
			f"- Formable-family matrix SHA-256: `{data['formable_family_registry_sha256']}`",
			f"- Formable base-localisation inventory SHA-256: `{data['formable_localisation_inventory_sha256']}`",
			f"- Manual identity dispositions SHA-256: `{data['manual_identity_file_sha256']}`",
			f"- Vanilla `00_countries.txt` SHA-256: `{data['vanilla_country_tag_file_sha256']}`",
			f"- Vanilla country localisation SHA-256: `{data['vanilla_country_localisation_file_sha256']}`",
			f"- Vanilla checksum manifest SHA-256: `{data['vanilla_checksum_manifest_sha256']}`",
			f"- Parsed vanilla tag-surface inventory SHA-256: `{data['vanilla_tag_surface_inventory_sha256']}`",
			f"- Parsed Workshop tag-surface inventory SHA-256: `{data['workshop_tag_surface_inventory_sha256']}`",
			f"- Parsed sibling-mod tag-surface inventory SHA-256: `{data['local_mod_tag_surface_inventory_sha256']}`",
			f"- Parsed non-Event 006 Chaos Redux tag-surface inventory SHA-256: `{data['chaos_redux_non_event6_tag_surface_inventory_sha256']}`",
			f"- ZIP archive content inventory SHA-256: `{data['archive_inventory_sha256']}`",
			f"- Runtime attestation source SHA-256: `{data['dispatch_attestation_file_sha256']}`",
			f"- Package-origin wrapper source inventory SHA-256: `{data['package_trigger_inventory_sha256']}`",
			f"- Scenario block source SHA-256: `{data['scenario_effect_file_sha256']}`",
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
	formable_cosmetic_file = repo_root / "common" / "countries" / "006_independence_wave_formable_cosmetics.txt"
	registry_file = repo_root / "docs" / "specs" / "006_independence_wave_specs" / "matrices" / "006_candidate_country_registry.csv"
	formable_family_registry_file = repo_root / "docs" / "specs" / "006_independence_wave_specs" / "matrices" / "006_formable_family_registry.csv"
	formable_localisation_files = [
		repo_root / "localisation" / "english" / "006_independence_wave_form01_02_04_l_english.yml",
		repo_root / "localisation" / "english" / "006_independence_wave_form05_l_english.yml",
		repo_root / "localisation" / "english" / "006_independence_wave_pacific_l_english.yml",
		repo_root / "localisation" / "english" / "006_independence_wave_formable_registry_l_english.yml",
	]
	manual_identity_file = repo_root / "docs" / "plans" / "006_independence_wave_plans" / "tag_audit" / "006_vanilla_identity_manual_dispositions_2026_07_16.csv"
	vanilla_country_tag_file = args.game_root / "common" / "country_tags" / "00_countries.txt"
	vanilla_country_localisation_file = args.game_root / "localisation" / "english" / "countries_l_english.yml"
	vanilla_checksum_manifest = args.game_root / "checksum_manifest.txt"
	required_inputs = (
		event6_tag_file,
		formable_cosmetic_file,
		registry_file,
		formable_family_registry_file,
		*formable_localisation_files,
		manual_identity_file,
		vanilla_country_tag_file,
		vanilla_country_localisation_file,
		vanilla_checksum_manifest,
	)
	missing_inputs = [str(path) for path in required_inputs if not path.is_file()]
	if missing_inputs:
		raise FileNotFoundError(f"Required Event 006 tag-audit inputs are missing: {', '.join(missing_inputs)}")

	event6_rows = parse_event6_tags(event6_tag_file)
	formable_cosmetic_rows = parse_event6_formable_cosmetics(formable_cosmetic_file)
	event6_custom_cosmetic_identifiers = parse_event6_custom_cosmetic_identifiers(formable_cosmetic_file)
	event6_custom_cosmetic_identifier_set = set(event6_custom_cosmetic_identifiers)
	event6_custom_cosmetic_calls = parse_event6_custom_cosmetic_calls(repo_root, event6_custom_cosmetic_identifier_set)
	if event6_custom_cosmetic_calls != event6_custom_cosmetic_identifier_set:
		missing = sorted(event6_custom_cosmetic_identifier_set - event6_custom_cosmetic_calls)
		extra = sorted(event6_custom_cosmetic_calls - event6_custom_cosmetic_identifier_set)
		raise RuntimeError(f"Event 006 custom cosmetic definitions/call sites mismatch: missing={missing} extra={extra}")
	registry_rows = parse_registry(registry_file)
	formable_family_rows = parse_registry(formable_family_registry_file)
	formable_localisations = parse_event6_formable_localisations(formable_localisation_files)
	manual_identity_rows = parse_manual_identity_dispositions(manual_identity_file)
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
	formable_cosmetic_tags = {row["tag"] for row in formable_cosmetic_rows}
	if formable_cosmetic_tags != set(EVENT6_FORMABLE_COSMETIC_IDENTITIES):
		missing = sorted(set(EVENT6_FORMABLE_COSMETIC_IDENTITIES) - formable_cosmetic_tags)
		extra = sorted(formable_cosmetic_tags - set(EVENT6_FORMABLE_COSMETIC_IDENTITIES))
		raise RuntimeError(f"Event 006 formable/cosmetic registry mismatch: missing={missing} extra={extra}")
	expected_formable_family_names = {
		family_id: identity
		for family_id, identity in EVENT6_FORMABLE_COSMETIC_IDENTITIES.values()
	}
	actual_formable_family_names = {
		row.get("formable_id", ""): row.get("working_name_not_final_localisation", "")
		for row in formable_family_rows
		if row.get("formable_id", "") in expected_formable_family_names
	}
	if actual_formable_family_names != expected_formable_family_names:
		raise RuntimeError(
			"Event 006 promoted formable family names do not match the reviewed cosmetic identities: "
			f"expected={expected_formable_family_names} actual={actual_formable_family_names}"
		)
	expected_formable_localisations = {
		tag: identity
		for tag, (_, identity) in EVENT6_FORMABLE_COSMETIC_IDENTITIES.items()
	}
	if formable_localisations != expected_formable_localisations:
		raise RuntimeError(
			"Event 006 formable base localisation does not match the reviewed cosmetic identities: "
			f"expected={expected_formable_localisations} actual={formable_localisations}"
		)
	set_cosmetic_calls = parse_event6_set_cosmetic_calls(repo_root)
	if set_cosmetic_calls != formable_cosmetic_tags:
		missing = sorted(formable_cosmetic_tags - set_cosmetic_calls)
		extra = sorted(set_cosmetic_calls - formable_cosmetic_tags)
		raise RuntimeError(f"Event 006 set_cosmetic_tag call sites mismatch the reviewed identity registry: missing={missing} extra={extra}")
	if custom_registry_tags & formable_cosmetic_tags:
		raise RuntimeError("An Event 006 formable/cosmetic tag overlaps an Event 006 country reservation")
	event6_owned_rows = event6_rows + formable_cosmetic_rows
	event6_owned_tags = {row["tag"] for row in event6_owned_rows}
	if len(event6_owned_tags) != len(event6_owned_rows):
		raise RuntimeError("Event 006 country and formable/cosmetic identifiers are not unique")
	if any(not re.fullmatch(r"[A-Z0-9]{2}X", tag) for tag in event6_owned_tags):
		raise RuntimeError("An Event 006-owned country or formable/cosmetic identifier does not end in X")
	reserved_namespace_tags = sorted(event6_owned_tags & ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES.keys())
	if reserved_namespace_tags:
		details = ", ".join(
			f"{tag} ({ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES[tag]})"
			for tag in reserved_namespace_tags
		)
		raise RuntimeError(f"Event 006 consumes engine- or OS-reserved namespace tags: {details}")
	overlay_rows = [row for row in registry_rows if row.get("automatic_pool_disposition") == "vanilla_route_overlay_only"]
	if any(row.get("resolved_tag") for row in overlay_rows):
		raise RuntimeError("A vanilla route overlay has a standalone resolved tag")
	event6_history_paths, event6_history_rows = parse_event6_owned_history_filenames(repo_root, event6_rows)
	registry_rows_by_id = {row.get("package_id", ""): row for row in registry_rows}
	for manual_row in manual_identity_rows:
		registry_row = registry_rows_by_id.get(manual_row["package_id"])
		if not registry_row:
			raise RuntimeError(f"Manual identity disposition references unknown package {manual_row['package_id']}")
		if manual_row["proposed_tag"] != registry_row.get("resolved_tag"):
			raise RuntimeError(f"Manual identity disposition tag mismatch for {manual_row['package_id']}")
		if normalize_name(manual_row["proposed_identity"]) != normalize_name(registry_row.get("working_name_not_final_localisation", "")):
			raise RuntimeError(f"Manual identity disposition name mismatch for {manual_row['package_id']}")

	vanilla_defs = scan_tag_directory(args.game_root, "vanilla", "Hearts of Iron IV")
	vanilla_extended_defs = scan_extended_tag_surfaces(args.game_root, "vanilla", "Hearts of Iron IV")
	external_defs: list[TagDefinition] = list(vanilla_defs)
	external_extended_defs: list[TagDefinition] = list(vanilla_extended_defs)
	external_custom_cosmetic_defs: list[TagDefinition] = scan_event6_custom_cosmetic_surfaces(
		args.game_root,
		"vanilla",
		"Hearts of Iron IV",
		event6_custom_cosmetic_identifier_set,
	)
	workshop_dirs = sorted(path for path in args.workshop_root.iterdir() if path.is_dir()) if args.workshop_root.is_dir() else []
	workshop_roots_with_tags = 0
	archive_file_count = 0
	archive_files_with_tag_surfaces = 0
	archive_definition_count = 0
	archive_extended_surface_count = 0
	all_archive_paths: list[Path] = []
	for mod_root in workshop_dirs:
		archive_paths, archive_surface_count, archive_definitions, archive_extended_definitions = scan_archives_under_root(
			mod_root,
			"workshop_archive",
			mod_root.name,
		)
		archive_file_count += len(archive_paths)
		all_archive_paths.extend(archive_paths)
		archive_files_with_tag_surfaces += archive_surface_count
		archive_definition_count += len(archive_definitions)
		archive_extended_surface_count += len(archive_extended_definitions)
		for archive_path in archive_paths:
			external_custom_cosmetic_defs.extend(
				scan_zip_event6_custom_cosmetic_surfaces(
					archive_path,
					"workshop_archive",
					mod_root.name,
					event6_custom_cosmetic_identifier_set,
				)
			)
		definitions = scan_tag_directory(mod_root, "workshop", mod_root.name) + archive_definitions
		extended_definitions = scan_extended_tag_surfaces(mod_root, "workshop", mod_root.name) + archive_extended_definitions
		external_custom_cosmetic_defs.extend(
			scan_event6_custom_cosmetic_surfaces(
				mod_root,
				"workshop",
				mod_root.name,
				event6_custom_cosmetic_identifier_set,
			)
		)
		if definitions:
			workshop_roots_with_tags += 1
		external_defs.extend(definitions)
		external_extended_defs.extend(extended_definitions)

	local_mod_dirs: list[Path] = []
	local_mod_roots_with_tag_surfaces = 0
	local_mod_definition_count = 0
	local_mod_extended_surface_count = 0
	if local_mod_root.is_dir():
		local_mod_dirs = [
			path
			for path in sorted(local_mod_root.iterdir())
			if path.is_dir() and path.resolve() != repo_root
		]
	for mod_root in local_mod_dirs:
		archive_paths, archive_surface_count, archive_definitions, archive_extended_definitions = scan_archives_under_root(
			mod_root,
			"local_mod_archive",
			mod_root.name,
		)
		archive_file_count += len(archive_paths)
		all_archive_paths.extend(archive_paths)
		archive_files_with_tag_surfaces += archive_surface_count
		archive_definition_count += len(archive_definitions)
		archive_extended_surface_count += len(archive_extended_definitions)
		for archive_path in archive_paths:
			external_custom_cosmetic_defs.extend(
				scan_zip_event6_custom_cosmetic_surfaces(
					archive_path,
					"local_mod_archive",
					mod_root.name,
					event6_custom_cosmetic_identifier_set,
				)
			)
		definitions = scan_tag_directory(mod_root, "local_mod", mod_root.name) + archive_definitions
		extended_definitions = scan_extended_tag_surfaces(mod_root, "local_mod", mod_root.name) + archive_extended_definitions
		external_custom_cosmetic_defs.extend(
			scan_event6_custom_cosmetic_surfaces(
				mod_root,
				"local_mod",
				mod_root.name,
				event6_custom_cosmetic_identifier_set,
			)
		)
		if definitions or extended_definitions:
			local_mod_roots_with_tag_surfaces += 1
		local_mod_definition_count += len(definitions)
		local_mod_extended_surface_count += len(extended_definitions)
		external_defs.extend(definitions)
		external_extended_defs.extend(extended_definitions)

	non_event6_defs = scan_current_repo_non_event6(repo_root, event6_tag_file)
	non_event6_extended_defs = scan_current_repo_non_event6_extended(repo_root, event6_owned_tags, event6_history_paths)
	non_event6_custom_cosmetic_defs = scan_current_repo_non_event6_custom_cosmetic_surfaces(
		repo_root,
		event6_custom_cosmetic_identifier_set,
		event6_history_paths,
	)
	all_conflict_defs = external_defs + external_extended_defs + non_event6_defs + non_event6_extended_defs
	definitions_by_tag: dict[str, list[TagDefinition]] = defaultdict(list)
	for definition in all_conflict_defs:
		definitions_by_tag[definition.tag].append(definition)

	collisions: list[dict[str, object]] = []
	for row in event6_owned_rows:
		definitions = definitions_by_tag.get(row["tag"], [])
		if definitions:
			collisions.append(
				{
					**row,
					"definitions": [definition.__dict__ for definition in definitions],
				}
			)
	custom_cosmetic_definitions_by_identifier: dict[str, list[TagDefinition]] = defaultdict(list)
	for definition in external_custom_cosmetic_defs + non_event6_custom_cosmetic_defs:
		custom_cosmetic_definitions_by_identifier[definition.tag].append(definition)
	custom_cosmetic_collisions: list[dict[str, object]] = []
	for identifier in event6_custom_cosmetic_identifiers:
		definitions = custom_cosmetic_definitions_by_identifier.get(identifier, [])
		if definitions:
			custom_cosmetic_collisions.append(
				{
					"identifier": identifier,
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
	manual_disposition_by_package = {row["package_id"]: row for row in manual_identity_rows}
	undisposed_manual_packages = sorted(set(manual_packages) - set(manual_disposition_by_package))
	if undisposed_manual_packages:
		raise RuntimeError(
			"Generated vanilla-identity review leads lack manual dispositions: "
			+ ", ".join(undisposed_manual_packages)
		)

	dispatch_trigger_file = repo_root / "common" / "scripted_triggers" / "006_independence_wave_package_dispatch_triggers.txt"
	package_trigger_file = repo_root / "common" / "scripted_triggers" / "006_independence_wave_package_triggers.txt"
	package_trigger_files = sorted(
		(repo_root / "common" / "scripted_triggers").glob("006_independence_wave*package*triggers.txt")
	)
	scenario_effect_file = repo_root / "common" / "scripted_effects" / "006_independence_wave_scenario_effects.txt"
	for runtime_source in (dispatch_trigger_file, package_trigger_file, scenario_effect_file):
		if not runtime_source.is_file():
			raise FileNotFoundError(f"Required Event 006 runtime evidence source is missing: {runtime_source}")
	if not package_trigger_files:
		raise FileNotFoundError("No Event 006 package trigger sources were found")
	attested_package_ids = parse_runtime_attested_package_ids(dispatch_trigger_file)
	package_trigger_text = "\n".join(decode_text(path) for path in package_trigger_files)
	exact_wrapper_ids = {
		f"IW-{numeric_id}"
		for numeric_id in re.findall(
			r'is_independence_wave_exact_package_iw_(\d{3})_tag_available',
			package_trigger_text,
		)
	}
	scenario_blocked_ids = {
		f"IW-{numeric_id}"
		for numeric_id in re.findall(
			r'independence_wave_scenario_blocked_package_ids[^}\n]*\bvalue\s*=\s*constant:independence_wave_package_id\.iw_(\d{3})',
			decode_text(scenario_effect_file),
		)
	}
	legacy_content_ready_grants: list[str] = []
	legacy_grant_re = re.compile(r'\bset_country_flag\s*=\s*independence_wave_package_content_ready\b')
	for root in (repo_root / "common", repo_root / "events", repo_root / "history"):
		if not root.is_dir():
			continue
		for path in sorted(root.rglob("*.txt")):
			if legacy_grant_re.search(decode_text(path)):
				legacy_content_ready_grants.append(str(path))
	if legacy_content_ready_grants:
		raise RuntimeError("Legacy independence_wave_package_content_ready grants bypass static package attestation")
	shared_reused_tag_reviews: list[dict[str, object]] = []
	for shared_tag in ("BIA", "CHU"):
		for row in registry_rows:
			if row.get("resolved_tag") != shared_tag:
				continue
			package_id = row.get("package_id", "")
			shared_reused_tag_reviews.append(
				{
					"tag": shared_tag,
					"package_id": package_id,
					"identity": row.get("working_name_not_final_localisation", ""),
					"reservation_group": row.get("reservation_group", ""),
					"content_attested": package_id in attested_package_ids,
					"exact_package_wrapper": package_id in exact_wrapper_ids,
					"scenario_blocked": package_id in scenario_blocked_ids,
					"runtime_status": "attested" if package_id in attested_package_ids and package_id in exact_wrapper_ids else "fail_closed",
				}
			)
		shared_rows = [row for row in shared_reused_tag_reviews if row["tag"] == shared_tag]
		if len(shared_rows) != 2 or len({row["reservation_group"] for row in shared_rows}) != 1:
			raise RuntimeError(f"Shared Event 006 tag {shared_tag} lacks a two-row mutual reservation group")

	vanilla_tags = {definition.tag for definition in vanilla_defs}
	all_used_tags = {definition.tag for definition in all_conflict_defs}
	all_used_tags.update(event6_owned_tags)
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
	workshop_inventory = [
		definition
		for definition in external_defs + external_extended_defs
		if definition.root_kind.startswith("workshop")
	]
	local_mod_inventory = [
		definition
		for definition in external_defs + external_extended_defs
		if definition.root_kind.startswith("local_mod")
	]
	vanilla_inventory = [
		definition
		for definition in external_defs + external_extended_defs
		if definition.root_kind == "vanilla"
	]

	data: dict[str, object] = {
		"audit_date": date.today().isoformat(),
		"registry_package_count": len(registry_rows),
		"event6_reserved_tag_count": len(event6_rows),
		"event6_country_tag_count": len(event6_rows),
		"event6_formable_cosmetic_tag_count": len(formable_cosmetic_rows),
		"event6_owned_identifier_count": len(event6_owned_rows),
		"event6_formable_cosmetic_rows": formable_cosmetic_rows,
		"event6_owned_identifiers": sorted(event6_owned_tags),
		"event6_custom_cosmetic_identifier_count": len(event6_custom_cosmetic_identifiers),
		"event6_custom_cosmetic_identifiers": event6_custom_cosmetic_identifiers,
		"event6_custom_cosmetic_call_count": len(event6_custom_cosmetic_calls),
		"event6_custom_cosmetic_external_surface_count": len(external_custom_cosmetic_defs),
		"event6_custom_cosmetic_non_event6_surface_count": len(non_event6_custom_cosmetic_defs),
		"event6_custom_cosmetic_collisions": custom_cosmetic_collisions,
		"event6_custom_cosmetic_external_surface_inventory_sha256": definition_inventory_sha256(external_custom_cosmetic_defs),
		"event6_custom_cosmetic_non_event6_surface_inventory_sha256": definition_inventory_sha256(non_event6_custom_cosmetic_defs),
		"event6_history_owned_filename_count": len(event6_history_rows),
		"event6_history_owned_filenames": event6_history_rows,
		"event6_history_owned_filename_inventory_sha256": stable_rows_sha256(event6_history_rows),
		"overlay_registry_count": len(overlay_rows),
		"engine_reserved_namespaces": sorted(ENGINE_RESERVED_THREE_CHARACTER_NAMESPACES),
		"workshop_directory_count": len(workshop_dirs),
		"workshop_roots_with_tags": workshop_roots_with_tags,
		"archive_file_count": archive_file_count,
		"archive_files_with_tag_surfaces": archive_files_with_tag_surfaces,
		"archive_definition_count": archive_definition_count,
		"archive_extended_surface_count": archive_extended_surface_count,
		"local_mod_directory_count": len(local_mod_dirs),
		"local_mod_directory_names": [path.name for path in local_mod_dirs],
		"local_mod_roots_with_tag_surfaces": local_mod_roots_with_tag_surfaces,
		"local_mod_definition_count": local_mod_definition_count,
		"local_mod_extended_surface_count": local_mod_extended_surface_count,
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
		"manual_identity_disposition_count": len(manual_identity_rows),
		"manual_identity_dispositions": manual_identity_rows,
		"reused_registry_count": len(reused_rows),
		"reused_unique_tag_count": len({row.get("resolved_tag", "") for row in reused_rows}),
		"reused_in_vanilla_count": len(reused_in_vanilla),
		"reused_not_in_vanilla": reused_not_in_vanilla,
		"vanilla_cosmetic_identity_count": len(names_by_cosmetic),
		"duplicate_resolved_tags": duplicate_resolved_tags,
		"shared_reused_tag_reviews": shared_reused_tag_reviews,
		"runtime_attested_package_ids": sorted(attested_package_ids),
		"legacy_content_ready_grant_count": len(legacy_content_ready_grants),
		"safe_x_tag_pool": safe_pool,
		"event6_tag_file_sha256": file_sha256(event6_tag_file),
		"event6_formable_cosmetic_file_sha256": file_sha256(formable_cosmetic_file),
		"registry_sha256": file_sha256(registry_file),
		"formable_family_registry_sha256": file_sha256(formable_family_registry_file),
		"formable_localisation_inventory_sha256": file_inventory_sha256(formable_localisation_files),
		"manual_identity_file_sha256": file_sha256(manual_identity_file),
		"audit_script_sha256": file_sha256(Path(__file__).resolve()),
		"vanilla_country_tag_file_sha256": file_sha256(vanilla_country_tag_file),
		"vanilla_country_localisation_file_sha256": file_sha256(vanilla_country_localisation_file),
		"vanilla_checksum_manifest_sha256": file_sha256(vanilla_checksum_manifest),
		"vanilla_tag_surface_inventory_sha256": definition_inventory_sha256(vanilla_inventory),
		"workshop_tag_surface_inventory_sha256": definition_inventory_sha256(workshop_inventory),
		"local_mod_tag_surface_inventory_sha256": definition_inventory_sha256(local_mod_inventory),
		"chaos_redux_non_event6_tag_surface_inventory_sha256": definition_inventory_sha256(non_event6_defs + non_event6_extended_defs),
		"archive_inventory_sha256": archive_inventory_sha256(all_archive_paths),
		"dispatch_attestation_file_sha256": file_sha256(dispatch_trigger_file),
		"package_trigger_inventory_sha256": file_inventory_sha256(package_trigger_files),
		"scenario_effect_file_sha256": file_sha256(scenario_effect_file),
		"scan_roots": {
			"game_root": str(args.game_root),
			"workshop_root": str(args.workshop_root),
			"local_mod_root": str(local_mod_root),
			"repo_root": str(repo_root),
		},
	}

	print(json.dumps({key: value for key, value in data.items() if key not in {"safe_x_tag_pool", "collisions", "identity_matches", "event6_custom_cosmetic_collisions"}}, indent=2))
	print(
		f"collisions={len(collisions)} custom_cosmetic_collisions={len(custom_cosmetic_collisions)} "
		f"identity_matches={len(matches)} safe_x_tags={len(safe_pool)}"
	)

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
		with (report_dir / f"006_installed_custom_cosmetic_collisions_{report_slug}.csv").open("w", encoding="utf-8-sig", newline="") as handle:
			writer = csv.DictWriter(handle, fieldnames=("identifier", "tag", "root_kind", "root_name", "use_kind", "file", "country_path"))
			writer.writeheader()
			for collision in custom_cosmetic_collisions:
				for definition in collision["definitions"]:
					writer.writerow({"identifier": collision["identifier"], **definition})
		with (report_dir / f"006_vanilla_identity_review_{report_slug}.csv").open("w", encoding="utf-8-sig", newline="") as handle:
			writer = csv.DictWriter(handle, fieldnames=("package_id", "identity", "proposed_tag", "vanilla_kind", "vanilla_identifier", "vanilla_name", "confidence", "similarity"))
			writer.writeheader()
			writer.writerows(matches)


if __name__ == "__main__":
	main()
