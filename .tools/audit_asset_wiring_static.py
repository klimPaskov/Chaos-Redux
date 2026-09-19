#!/usr/bin/env python3
"""Static audit of Chaos Redux sprite, entity, and asset wiring.

Answers three source-only questions:

1. Which `GFX_` names are referenced by script or GUI but registered in no
   `.gfx` file here and in no vanilla `.gfx` file? Those render as a missing
   sprite or log an error at load.
2. Which `GFX_` names are registered in this mod's `.gfx` files but referenced
   nowhere? Those are dead sprite definitions.
3. Which sprite, entity, or texture definitions point at a file that does not
   exist on disk?
4. Which mod-referenced vanilla GFX definitions point at a file that does not
   exist in the installed vanilla tree? This catches broken DLC reach-through
   such as a declared portrait sprite whose backing DDS is absent.

Vanilla reach-through is expected in places, so question 1 consults the vanilla
install before reporting a name as unresolved.

Usage:
	python .tools/audit_asset_wiring_static.py
	python .tools/audit_asset_wiring_static.py --json out.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

REPO_ROOT = Path(__file__).resolve().parents[1]
VANILLA_ROOT = Path(
	"C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV"
)

EXCLUDED_TOP_LEVEL = {
	".git", ".tools", ".tmp", ".agents", ".claude", ".codex", ".cursor",
	".opencode", ".qoder", "docs", "history", "paradox_wiki",
}

NAME_DEF = re.compile(r'name\s*=\s*"?(GFX_[A-Za-z0-9_]+)"?')
GFX_REF = re.compile(r"\bGFX_[A-Za-z0-9_]+")
TEXTURE_REF = re.compile(r'(?:texturefile|texture_diffuse|texture|fontfile)\s*=\s*"([^"]+)"')

# Clausewitz resolves entity textures and meshes by filename, searching the
# model folders recursively, not by the literal quoted path. A reference is
# therefore present when a file of that name exists anywhere under the model
# trees. Resolving the quoted string as a literal path reported every entity
# texture as missing.
ASSET_SEARCH_DIRS = (
	REPO_ROOT / "gfx",
	REPO_ROOT / "sound",
	REPO_ROOT / "music",
	VANILLA_ROOT / "gfx",
	VANILLA_ROOT / "sound",
	VANILLA_ROOT / "music",
	# DLC packages keep their engine-facing textures below their own package
	# roots. Include those trees so a vanilla sprite declaration is not
	# incorrectly reported as broken merely because its texture is supplied by
	# an installed DLC rather than the base game root.
	VANILLA_ROOT / "dlc",
	VANILLA_ROOT / "integrated_dlc",
)

_ASSET_INDEX: Dict[str, int] = {}


def build_asset_index() -> Dict[str, int]:
	"""Index every asset basename under the mod and vanilla asset trees."""
	if _ASSET_INDEX:
		return _ASSET_INDEX
	suffixes = {".dds", ".tga", ".png", ".bmp", ".jpg", ".mesh", ".anim", ".wav", ".ogg"}
	for root in ASSET_SEARCH_DIRS:
		if not root.is_dir():
			continue
		for path in root.rglob("*"):
			if path.is_file() and path.suffix.lower() in suffixes:
				key = path.name.lower()
				_ASSET_INDEX[key] = _ASSET_INDEX.get(key, 0) + 1
	return _ASSET_INDEX


def resolve_asset(reference: str) -> bool:
	"""Return True when an asset reference resolves to a real file."""
	if not reference:
		return True
	normalised = reference.replace("\\", "/")
	if "/" in normalised:
		for root in (REPO_ROOT, VANILLA_ROOT):
			if (root / normalised).is_file():
				return True
	basename = normalised.rsplit("/", 1)[-1].lower()
	return build_asset_index().get(basename, 0) > 0
FILE_REF = re.compile(r'"[^"]*?\.(?:dds|tga|png|bmp|jpg)"', re.IGNORECASE)


class Findings:
	def __init__(self) -> None:
		self.unresolved_refs: List[Dict[str, object]] = []
		self.dead_definitions: List[Dict[str, object]] = []
		self.missing_files: List[Dict[str, str]] = []
		self.missing_vanilla_files: List[Dict[str, str]] = []
		self.registered_count = 0
		self.vanilla_registered = 0


def read_text(path: Path) -> str:
	raw = path.read_bytes()
	if raw.startswith(b"\xef\xbb\xbf"):
		raw = raw[3:]
	return raw.decode("utf-8", errors="replace")


def collect_registered(root: Path, excluded: Set[str]) -> Dict[str, List[str]]:
	"""Return GFX names registered by `.gfx` files under root."""
	registered: Dict[str, List[str]] = defaultdict(list)
	if not root.is_dir():
		return registered
	for path in root.rglob("*.gfx"):
		parts = path.relative_to(root).parts
		if parts and parts[0] in excluded:
			continue
		try:
			text = read_text(path)
		except OSError:
			continue
		rel = str(path)
		try:
			rel = str(path.relative_to(REPO_ROOT))
		except ValueError:
			pass
		for match in NAME_DEF.finditer(text):
			registered[match.group(1)].append(rel)
	return registered


def collect_references() -> Tuple[Dict[str, Set[str]], Set[str]]:
	"""Return GFX names referenced, and the names each `.gfx` file defines.

	A `.gfx` file mentions every sprite it defines via `name = "GFX_..."`, so a
	registration would otherwise count as its own reference and no registration
	could ever be dead. The defining files are returned so the caller can
	discount a name that appears only in its own definition.
	"""
	references: Dict[str, Set[str]] = defaultdict(set)
	defined_in: Dict[str, Set[str]] = defaultdict(set)
	for path in REPO_ROOT.rglob("*"):
		if not path.is_file():
			continue
		parts = path.relative_to(REPO_ROOT).parts
		if not parts or parts[0] in EXCLUDED_TOP_LEVEL:
			continue
		if path.suffix.lower() not in {".txt", ".gui", ".gfx", ".asset", ".yml", ".md"}:
			continue
		try:
			text = read_text(path)
		except OSError:
			continue
		rel = str(path.relative_to(REPO_ROOT))
		for match in GFX_REF.finditer(text):
			references[match.group(0)].add(rel)
		if path.suffix.lower() == ".gfx":
			for match in NAME_DEF.finditer(text):
				defined_in[match.group(1)].add(rel)
	return references, defined_in


def audit_definitions(findings: Findings) -> None:
	"""Check that every texture or sprite file reference exists on disk."""
	for path in REPO_ROOT.rglob("*.gfx"):
		parts = path.relative_to(REPO_ROOT).parts
		if parts and parts[0] in EXCLUDED_TOP_LEVEL:
			continue
		try:
			text = read_text(path)
		except OSError:
			continue
		rel = str(path.relative_to(REPO_ROOT))
		for match in TEXTURE_REF.finditer(text):
			target = match.group(1)
			if target.startswith(("gfx/", "GFX_")) and "/" not in target:
				continue
			if resolve_asset(target):
				continue
			findings.missing_files.append({"file": rel, "reference": target})


def audit_entities(findings: Findings) -> None:
	"""Check `.gfx` entity blocks for mesh and texture files that are absent."""
	for path in REPO_ROOT.rglob("*.gfx"):
		parts = path.relative_to(REPO_ROOT).parts
		if parts and parts[0] in EXCLUDED_TOP_LEVEL:
			continue
		try:
			text = read_text(path)
		except OSError:
			continue
		rel = str(path.relative_to(REPO_ROOT))
		for match in re.finditer(r'\bmeshfile\s*=\s*"([^"]+)"', text):
			target = match.group(1)
			if resolve_asset(target):
				continue
			findings.missing_files.append({"file": rel, "reference": target})


def audit_referenced_vanilla_definitions(
	findings: Findings, referenced_names: Set[str]
) -> None:
	"""Check backing files for vanilla GFX definitions used by the mod.

	The normal missing-file pass intentionally scans mod-owned `.gfx` files only.
	Vanilla reach-through is usually safe, but a declared vanilla sprite can still
	be unusable when its DLC declaration survives while the backing texture is
	absent from the installed tree. Restrict this pass to GFX names referenced by
	the mod so it does not turn the audit into a full vanilla-install linter.
	"""
	if not VANILLA_ROOT.is_dir() or not referenced_names:
		return
	for path in VANILLA_ROOT.rglob("*.gfx"):
		try:
			text = read_text(path)
		except OSError:
			continue
		matches = list(NAME_DEF.finditer(text))
		if not matches:
			continue
		for index, match in enumerate(matches):
			name = match.group(1)
			if name not in referenced_names:
				continue
			end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
			definition = text[match.end():end]
			for texture in TEXTURE_REF.finditer(definition):
				target = texture.group(1)
				if resolve_asset(target):
					continue
				findings.missing_vanilla_files.append(
					{
						"file": str(path.relative_to(VANILLA_ROOT)),
						"reference": target,
						"name": name,
					}
				)


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--json", type=Path, help="also write the findings as JSON")
	arguments = parser.parse_args()

	findings = Findings()

	print("indexing mod gfx registrations ...", file=sys.stderr)
	mod_registered = collect_registered(REPO_ROOT, EXCLUDED_TOP_LEVEL)
	findings.registered_count = len(mod_registered)
	print(f"  {len(mod_registered)} GFX names registered here", file=sys.stderr)

	print("indexing vanilla gfx registrations ...", file=sys.stderr)
	vanilla_registered = collect_registered(VANILLA_ROOT, set())
	findings.vanilla_registered = len(vanilla_registered)
	print(f"  {len(vanilla_registered)} GFX names registered in vanilla", file=sys.stderr)

	print("indexing references ...", file=sys.stderr)
	references, defined_in = collect_references()
	print(f"  {len(references)} distinct GFX names referenced", file=sys.stderr)

	for name, sources in sorted(references.items()):
		if name in mod_registered or name in vanilla_registered:
			continue
		findings.unresolved_refs.append(
			{"name": name, "sources": sorted(sources)[:4], "count": len(sources)}
		)

	for name, definitions in sorted(mod_registered.items()):
		# Discount the file that defines the sprite: its own `name = "GFX_..."`
		# line is not a use of the sprite.
		external = references.get(name, set()) - set(definitions)
		if external:
			continue
		findings.dead_definitions.append(
			{"name": name, "definitions": definitions[:3], "count": len(definitions)}
		)

	print("indexing asset filenames ...", file=sys.stderr)
	index = build_asset_index()
	print(f"  {len(index)} distinct asset filenames", file=sys.stderr)

	audit_definitions(findings)
	audit_entities(findings)
	audit_referenced_vanilla_definitions(findings, set(references))

	print()
	print("=" * 78)
	print("Chaos Redux static asset wiring audit")
	print("=" * 78)
	print(f"GFX registered here      : {findings.registered_count}")
	print(f"GFX referenced           : {len(references)}")
	print(f"unresolved references    : {len(findings.unresolved_refs)}")
	print(f"dead registrations       : {len(findings.dead_definitions)}")
	print(f"missing files on disk    : {len(findings.missing_files)}")
	print(f"missing vanilla files    : {len(findings.missing_vanilla_files)}")

	def section(title: str, rows: List[str], limit: int = 40) -> None:
		print()
		print(f"--- {title} ({len(rows)}) ---")
		for row in rows[:limit]:
			print(f"  {row}")
		if len(rows) > limit:
			print(f"  ... {len(rows) - limit} more")

	section(
		"unresolved GFX references",
		[f"{r['name']}  ({r['count']} sites)  {', '.join(r['sources'][:2])}" for r in findings.unresolved_refs],
	)
	section(
		"missing files on disk",
		[f"{m['reference']}  <- {m['file']}" for m in findings.missing_files],
	)
	section(
		"missing files in referenced vanilla GFX",
		[
			f"{m['reference']}  <- {m['file']} ({m['name']})"
			for m in findings.missing_vanilla_files
		],
	)
	section(
		"dead registrations",
		[f"{d['name']}  <- {', '.join(d['definitions'][:1])}" for d in findings.dead_definitions],
		limit=60,
	)

	if arguments.json:
		payload = {
			"registered_count": findings.registered_count,
			"vanilla_registered": findings.vanilla_registered,
			"referenced_count": len(references),
			"unresolved_refs": findings.unresolved_refs,
			"dead_definitions": findings.dead_definitions,
			"missing_files": findings.missing_files,
			"missing_vanilla_files": findings.missing_vanilla_files,
		}
		arguments.json.write_text(
			json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
		)
		print(f"\nwrote {arguments.json}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
