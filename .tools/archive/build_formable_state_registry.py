#!/usr/bin/env python3
"""Build the deterministic runtime contract for the universal state registry.

The geometry producer owns the source registry under
``docs/formables/state_registry/generated/state_geometry_registry.json``.  This
builder never edits that source.  It validates the source against an active
HOI4 installation (and optional mod overlays), writes a portable index for
review, and emits the per-state scripted-trigger wrappers consumed by future
formable/event GUI packages.

The builder is intentionally build-time only.  HOI4 cannot discover new state
ids or create their textures during a game, so map changes require rebuilding
the geometry registry, this index, and the consumers against the active
combined map before distribution.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs/formables/state_registry/generated/state_geometry_registry.json"
DEFAULT_INDEX = ROOT / "docs/formables/state_registry/state_registry_index.json"
DEFAULT_TRIGGERS = ROOT / "common/scripted_triggers/chaosx_universal_state_registry_triggers.txt"
DEFAULT_GAME_ROOT = Path(r"C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
REGISTRY_SCHEMA = "chaos-redux-state-geometry-registry/v1"
INDEX_SCHEMA = "chaos-redux-formable-state-registry/v1"
CANONICAL_HASH_ALGORITHM = "sha256-canonical-json-v1"
STATE_FILENAME_RE = re.compile(r"^(?P<id>\d+)(?:\s*-\s*.+)?\.txt$", re.IGNORECASE)
STATE_ID_RE = re.compile(r"\bid\s*=\s*(\d+)")
PORTABLE_PATH_RE = re.compile(r"^[A-Za-z0-9_./\\ -]+$")


class RegistryError(ValueError):
	"""Raised when the source registry or active map cannot be trusted."""


def sha256_bytes(value: bytes) -> str:
	return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
	hash_obj = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			hash_obj.update(chunk)
	return hash_obj.hexdigest()


def strip_clausewitz_comments(text: str) -> str:
	"""Remove Clausewitz comments without touching a quoted ``#`` character."""
	result: list[str] = []
	in_quote = False
	in_comment = False
	escaped = False
	for character in text:
		if in_comment:
			if character in "\r\n":
				in_comment = False
				result.append(character)
				escaped = False
			continue
		if character == '"' and not escaped:
			in_quote = not in_quote
		if character == "#" and not in_quote:
			in_comment = True
			continue
		result.append(character)
		if character == "\\" and in_quote and not escaped:
			escaped = True
		else:
			escaped = False
	return "".join(result)


def declared_state_id(path: Path) -> int:
	"""Read one unambiguous numeric state id from a history file."""
	text = strip_clausewitz_comments(path.read_text(encoding="utf-8-sig"))
	declared = {int(value) for value in STATE_ID_RE.findall(text)}
	filename_match = STATE_FILENAME_RE.match(path.name)
	filename_id = int(filename_match.group("id")) if filename_match else None
	if len(declared) > 1:
		raise RegistryError(f"{path} declares multiple state ids: {sorted(declared)}")
	if declared:
		state_id = next(iter(declared))
		if filename_id is not None and filename_id != state_id:
			raise RegistryError(f"{path} filename state id {filename_id} disagrees with declared id {state_id}")
		return state_id
	if filename_id is not None:
		return filename_id
	raise RegistryError(f"{path} does not declare a numeric state id")


def canonical_hash(value: Any) -> str:
	encoded = json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
	return sha256_bytes(encoded)


def portable_path(value: Any, *, field: str) -> str:
	if not isinstance(value, str) or not value:
		raise RegistryError(f"{field} must be a non-empty portable path")
	if Path(value).is_absolute() or re.match(r"^[A-Za-z]:", value):
		raise RegistryError(f"{field} must use a portable relative path, got {value!r}")
	if ".." in Path(value).parts:
		raise RegistryError(f"{field} may not escape the registry root: {value!r}")
	return value.replace("\\", "/")


def numeric_state_id(raw: dict[str, Any], *, fallback: str | None = None) -> int:
	for key in ("state_id", "id"):
		value = raw.get(key)
		if value is not None:
			try:
				state_id = int(value)
			except (TypeError, ValueError) as exc:
				raise RegistryError(f"state entry has a non-numeric {key}: {value!r}") from exc
			if state_id < 1:
				raise RegistryError(f"state id must be positive, got {state_id}")
			return state_id
	if fallback is not None:
		try:
			state_id = int(fallback)
		except ValueError as exc:
			raise RegistryError(f"state key is not numeric: {fallback!r}") from exc
		if state_id > 0:
			return state_id
	raise RegistryError("state entry is missing state_id")


def source_state_entries(document: dict[str, Any]) -> list[dict[str, Any]]:
	raw_states: Any = document.get("states")
	if raw_states is None:
		raw_states = document.get("state_entries", document.get("state_geometry"))
	if isinstance(raw_states, dict):
		items: Iterable[tuple[str | None, Any]] = ((str(key), value) for key, value in raw_states.items())
	elif isinstance(raw_states, list):
		items = ((None, value) for value in raw_states)
	else:
		raise RegistryError("source registry must expose a states list or state mapping")

	entries: list[dict[str, Any]] = []
	seen: set[int] = set()
	for fallback, value in items:
		if not isinstance(value, dict):
			raise RegistryError(f"state entry {fallback or '<unknown>'} is not an object")
		state = dict(value)
		state_id = numeric_state_id(state, fallback=fallback)
		if state_id in seen:
			raise RegistryError(f"duplicate state id {state_id} in source registry")
		seen.add(state_id)
		state["state_id"] = state_id
		name_key = state.get("name_key") or state.get("state_name") or state.get("name")
		if not isinstance(name_key, str) or not name_key:
			name_key = f"STATE_{state_id}"
		state["name_key"] = name_key
		entries.append(state)
	return sorted(entries, key=lambda item: item["state_id"])


def registry_map(document: dict[str, Any]) -> dict[str, Any]:
	map_data = document.get("map")
	if not isinstance(map_data, dict):
		# The adapter keeps compatibility with the old reviewed manifests while
		# requiring the universal source to carry a portable map description.
		legacy = document.get("source_files")
		if not isinstance(legacy, dict):
			raise RegistryError("source registry is missing the top-level map object")
		map_data = {
			"provinces_bmp": {
				"path": "map/provinces.bmp",
				"sha256": legacy.get("provinces_bmp_sha256"),
			},
			"definition_csv": {
				"path": "map/definition.csv",
				"sha256": legacy.get("definition_csv_sha256"),
			},
		}
	return dict(map_data)


def map_source_path(map_data: dict[str, Any], key: str, default: str) -> tuple[str, str | None]:
	value = map_data.get(key)
	if isinstance(value, dict):
		path_value = value.get("path", default)
		hash_value = value.get("sha256")
	else:
		path_value = value or default
		hash_value = None
	return portable_path(path_value, field=f"map.{key}.path"), hash_value


def overlay_file(relative_path: str, roots: list[Path]) -> Path:
	selected: Path | None = None
	for root in roots:
		candidate = root / relative_path
		if candidate.is_file():
			selected = candidate
	if selected is None:
		raise RegistryError(f"active map is missing {relative_path}")
	return selected


def state_files(roots: list[Path], *, replace_history: bool) -> dict[int, Path]:
	if replace_history and len(roots) < 2:
		raise RegistryError("--replace-state-history requires at least one --mod-root")
	history_roots = [roots[-1]] if replace_history else roots
	selected: dict[int, Path] = {}
	for root in history_roots:
		files = sorted((root / "history/states").glob("*.txt"))
		local: dict[int, Path] = {}
		for path in files:
			state_id = declared_state_id(path)
			if state_id in local:
				raise RegistryError(f"duplicate state id {state_id} inside {root / 'history/states'}")
			local[state_id] = path
		# Later roots override earlier roots by numeric state id, matching the
		# explicit load-order contract used by the builder.
		selected.update(local)
	if not selected:
		raise RegistryError("no active state-history files were found")
	return dict(sorted(selected.items()))


def registry_state_file(state: dict[str, Any]) -> str | None:
	for key in ("source_state_file", "history_file", "state_file"):
		value = state.get(key)
		if value:
			try:
				return portable_path(value, field=f"state {state['state_id']}.{key}")
			except RegistryError:
				# Older geometry manifests occasionally carried absolute provenance
				# paths.  The active-map check falls back to the canonical id file.
				return None
	return None


def active_state_ids_hash(state_ids: Iterable[int]) -> str:
	return sha256_bytes(",".join(str(state_id) for state_id in state_ids).encode("ascii"))


def state_history_bundle_hash(files: dict[int, Path]) -> str:
	rows = []
	for state_id, path in files.items():
		relative = f"history/states/{path.name}"
		rows.append(f"{state_id}|{relative}|{sha256_file(path)}\n")
	return sha256_bytes("".join(rows).encode("utf-8"))


def parse_row_runs(raw: Any, state_id: int) -> list[tuple[int, list[int]]]:
	if not isinstance(raw, list):
		raise RegistryError(f"state {state_id} row_runs must be a list")
	rows: list[tuple[int, list[int]]] = []
	previous_y: int | None = None
	for row in raw:
		if not isinstance(row, list) or len(row) != 2 or not isinstance(row[0], int) or not isinstance(row[1], list):
			raise RegistryError(f"state {state_id} row_runs must use [y,[x_start,length,...]] rows")
		y, values = row
		if y < 0 or (previous_y is not None and y <= previous_y):
			raise RegistryError(f"state {state_id} row y values must be positive and ascending")
		previous_y = y
		if len(values) == 0 or len(values) % 2:
			raise RegistryError(f"state {state_id} row {y} has an invalid start/length list")
		last_end = -1
		for offset in range(0, len(values), 2):
			x_start, length = values[offset : offset + 2]
			if not isinstance(x_start, int) or not isinstance(length, int) or x_start < 0 or length <= 0:
				raise RegistryError(f"state {state_id} row {y} contains a non-positive run")
			if x_start <= last_end:
				raise RegistryError(f"state {state_id} row {y} runs overlap or are not ascending")
			last_end = x_start + length - 1
		rows.append((y, values))
	return rows


def validate_geometry(document: dict[str, Any], entries: list[dict[str, Any]]) -> None:
	map_data = registry_map(document)
	dimensions = map_data.get("dimensions")
	width = map_data.get("width") or document.get("width")
	height = map_data.get("height") or document.get("height")
	if isinstance(dimensions, list) and len(dimensions) >= 2:
		width = width or dimensions[0]
		height = height or dimensions[1]
	if not isinstance(width, int) or width <= 0 or not isinstance(height, int) or height <= 0:
		raise RegistryError("map width and height must be positive integers")
	geometry_encoding = document.get("geometry_encoding")
	if not isinstance(geometry_encoding, dict) or geometry_encoding.get("type") != "absolute_row_runs":
		raise RegistryError("geometry_encoding.type must be absolute_row_runs")
	wrap = geometry_encoding.get("map_wrap")
	if not isinstance(wrap, dict) or wrap.get("world_width") != width:
		raise RegistryError("geometry_encoding.map_wrap must declare wrapping at the map width")
	if wrap.get("horizontal") is not True and wrap.get("axis") != "x":
		raise RegistryError("geometry_encoding.map_wrap must declare horizontal x wrapping")
	row_format = geometry_encoding.get("row_format")
	if row_format not in ("[y,[x_start,length,...]]", "[y, [x_start, length, x_start, length, ...]]"):
		raise RegistryError(f"unsupported geometry row_format: {row_format!r}")

	for state in entries:
		state_id = state["state_id"]
		source_file = state.get("source_state_file")
		source_hash = state.get("source_state_file_sha256")
		if not isinstance(source_file, str) or not source_file.startswith("history/states/"):
			raise RegistryError(f"state {state_id} must carry a portable source_state_file")
		if not isinstance(source_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", source_hash):
			raise RegistryError(f"state {state_id} must carry source_state_file_sha256")
		province_ids = state.get("province_ids")
		if not isinstance(province_ids, list) or not province_ids or len(set(province_ids)) != len(province_ids):
			raise RegistryError(f"state {state_id} must carry unique province_ids")
		if state.get("province_count") != len(province_ids):
			raise RegistryError(f"state {state_id} province_count disagrees with province_ids")
		rows = parse_row_runs(state.get("row_runs"), state_id)
		row_count = state.get("row_count")
		run_count = state.get("run_count")
		pixel_count = state.get("pixel_count")
		if not isinstance(row_count, int) or row_count <= 0:
			raise RegistryError(f"state {state_id} row_count must be positive")
		if not isinstance(run_count, int) or run_count <= 0:
			raise RegistryError(f"state {state_id} run_count must be positive")
		if not isinstance(pixel_count, int) or pixel_count <= 0:
			raise RegistryError(f"state {state_id} pixel_count must be positive")
		if row_count != len(rows):
			raise RegistryError(f"state {state_id} row_count disagrees with row_runs")
		actual_runs = sum(len(values) // 2 for _, values in rows)
		actual_pixels = sum(values[offset + 1] for _, values in rows for offset in range(0, len(values), 2))
		if run_count != actual_runs:
			raise RegistryError(f"state {state_id} run_count disagrees with row_runs")
		if pixel_count != actual_pixels:
			raise RegistryError(f"state {state_id} pixel_count disagrees with row_runs")
		geometry_hash = state.get("geometry_sha256")
		if not isinstance(geometry_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", geometry_hash):
			raise RegistryError(f"state {state_id} must carry geometry_sha256")
		if geometry_hash != canonical_hash(state["row_runs"]):
			raise RegistryError(f"state {state_id} geometry_sha256 disagrees with canonical row_runs")
		interval = state.get("circular_x_interval")
		if not isinstance(interval, dict):
			raise RegistryError(f"state {state_id} is missing circular_x_interval")
		start = interval.get("start_x")
		length = interval.get("length")
		end = interval.get("end_x_unwrapped")
		if not all(isinstance(value, int) for value in (start, length, end)) or length <= 0 or end != start + length - 1:
			raise RegistryError(f"state {state_id} circular interval must satisfy end_unwrapped = start + length - 1")
		if start < 0 or start >= width or length > width:
			raise RegistryError(f"state {state_id} circular interval exceeds map width")
		wraps = interval.get("wraps_x_seam")
		if not isinstance(wraps, bool):
			raise RegistryError(f"state {state_id} circular_x_interval.wraps_x_seam must be boolean")
		if wraps != (end >= width):
			raise RegistryError(f"state {state_id} circular_x_interval.wraps_x_seam disagrees with end_x_unwrapped")
		offset = interval.get("unwrap_offset")
		if not isinstance(offset, int):
			raise RegistryError(f"state {state_id} circular_x_interval.unwrap_offset must be an integer")
		if (wraps and offset != start) or (not wraps and offset != 0):
			raise RegistryError(f"state {state_id} circular_x_interval.unwrap_offset disagrees with wraps_x_seam")
		all_x: list[int] = []
		all_y: list[int] = []
		for y, values in rows:
			if y >= height:
				raise RegistryError(f"state {state_id} row {y} exceeds map height {height}")
			for index in range(0, len(values), 2):
				x_start, run_length = values[index : index + 2]
				if x_start >= width or x_start + run_length > width:
					raise RegistryError(f"state {state_id} row {y} run exceeds map width {width}")
				all_x.extend(range(x_start, x_start + run_length))
				all_y.append(y)
		if not all_x:
			raise RegistryError(f"state {state_id} geometry is empty")
		# Canonical seam rule: absolute row-run coordinates stay in [0,width),
		# and only columns before start_x move into the unwrapped interval.
		unwrapped = [x if x >= start else x + width for x in all_x] if wraps else list(all_x)
		if min(unwrapped) < start or max(unwrapped) > end:
			raise RegistryError(f"state {state_id} row-run x values fall outside circular_x_interval")
		bbox = state.get("tight_bbox")
		if isinstance(bbox, list) and len(bbox) == 4:
			min_x, min_y, max_x, max_y = bbox
			expected_bbox = [min(all_x), min(all_y), max(all_x), max(all_y)]
			if bbox != expected_bbox:
				raise RegistryError(
					f"state {state_id} tight_bbox={bbox} disagrees with exact row-run bounds {expected_bbox}"
				)


def validate_source_hash(document: dict[str, Any], entries: list[dict[str, Any]], *, game_roots: list[Path], replace_history: bool, expected_count: int | None) -> dict[str, Any]:
	map_data = registry_map(document)
	provinces_path, provinces_hash = map_source_path(map_data, "provinces_bmp", "map/provinces.bmp")
	definition_path, definition_hash = map_source_path(map_data, "definition_csv", "map/definition.csv")
	provinces = overlay_file(provinces_path, game_roots)
	definition = overlay_file(definition_path, game_roots)
	if provinces_hash and sha256_file(provinces) != provinces_hash:
		raise RegistryError(f"provinces.bmp hash mismatch: registry={provinces_hash} active={sha256_file(provinces)}")
	if definition_hash and sha256_file(definition) != definition_hash:
		raise RegistryError(f"definition.csv hash mismatch: registry={definition_hash} active={sha256_file(definition)}")

	active_files = state_files(game_roots, replace_history=replace_history)
	active_ids = sorted(active_files)
	registry_ids = [state["state_id"] for state in entries]
	if expected_count is not None and len(active_ids) != expected_count:
		raise RegistryError(f"active map has {len(active_ids)} states, expected {expected_count}")
	if active_ids != registry_ids:
		missing = sorted(set(active_ids) - set(registry_ids))
		extra = sorted(set(registry_ids) - set(active_ids))
		raise RegistryError(f"state id set mismatch: missing_from_registry={missing[:20]} extra_in_registry={extra[:20]}")

	counts = document.get("counts") if isinstance(document.get("counts"), dict) else {}
	state_id_range = counts.get("state_id_range")
	if isinstance(state_id_range, list) and len(state_id_range) == 2:
		if state_id_range != [active_ids[0], active_ids[-1]]:
			raise RegistryError(f"counts.state_id_range={state_id_range} disagrees with active ids [{active_ids[0]}, {active_ids[-1]}]")
	for key in ("state_count", "states"):
		if key in counts:
			try:
				expected = int(counts[key])
			except (TypeError, ValueError) as exc:
				raise RegistryError(f"counts.{key} is not numeric") from exc
			if expected != len(active_ids):
				raise RegistryError(f"counts.{key}={expected} disagrees with active state count {len(active_ids)}")
	if counts.get("state_ids_sha256") and counts["state_ids_sha256"] != active_state_ids_hash(active_ids):
		raise RegistryError("counts.state_ids_sha256 does not match the active state id list")

	map_wrap = document.get("geometry_encoding", {}).get("map_wrap", {})
	if not isinstance(map_wrap, dict) or (map_wrap.get("horizontal") is not True and map_wrap.get("axis") != "x"):
		raise RegistryError("geometry_encoding.map_wrap must declare horizontal x wrapping")
	map_width = map_data.get("width") or document.get("width")
	if map_width is None:
		map_width = map_data.get("dimensions", [None, None])[0] if isinstance(map_data.get("dimensions"), list) else None
	world_width = map_wrap.get("world_width", map_width)
	if map_width is not None and world_width != map_width:
		raise RegistryError(f"horizontal wrap width {world_width!r} disagrees with map width {map_width!r}")

	bundle_hash = state_history_bundle_hash(active_files)
	registry_bundle_hash = map_data.get("state_history_bundle_sha256")
	if registry_bundle_hash and bundle_hash != registry_bundle_hash:
		raise RegistryError(f"state-history bundle hash mismatch: registry={registry_bundle_hash} active={bundle_hash}")

	for state in entries:
		candidate = active_files[state["state_id"]]
		state_hash = state.get("source_state_file_sha256")
		if state_hash and sha256_file(candidate) != state_hash:
			raise RegistryError(f"state {state['state_id']} history hash mismatch: active file {candidate.name}")

	return {
		"provinces_bmp": {
			"path": provinces_path,
			"sha256": sha256_file(provinces),
		},
		"definition_csv": {
			"path": definition_path,
			"sha256": sha256_file(definition),
		},
		"state_history_root": "history/states",
		"state_history_bundle_sha256": bundle_hash,
		"active_state_count": len(active_ids),
		"active_state_ids_sha256": active_state_ids_hash(active_ids),
		"replace_state_history": replace_history,
	}


def validate_content_hash(document: dict[str, Any]) -> str:
	provided = document.get("registry_content_sha256")
	algorithm = document.get("registry_content_sha256_algorithm")
	if provided and algorithm not in (None, CANONICAL_HASH_ALGORITHM):
		raise RegistryError(f"unsupported registry_content_sha256_algorithm: {algorithm!r}")
	without_hash = dict(document)
	without_hash.pop("registry_content_sha256", None)
	computed = canonical_hash(without_hash)
	if provided and computed != provided:
		raise RegistryError(f"registry_content_sha256 mismatch: registry={provided} computed={computed}")
	return computed


def helper_names(state_id: int) -> dict[str, str]:
	prefix = f"chaosx_state_registry_state_{state_id}"
	return {
		"controlled_by_root": f"{prefix}_controlled_by_root",
		"owned_by_root": f"{prefix}_owned_by_root",
		"owned_and_controlled_by_root": f"{prefix}_owned_and_controlled_by_root",
		"controlled_by_root_or_subject": f"{prefix}_controlled_by_root_or_subject",
		"owned_by_root_or_subject": f"{prefix}_owned_by_root_or_subject",
	}


def generate_triggers(entries: list[dict[str, Any]], source: str, *, map_wrap_width: int | None) -> str:
	lines = [
		"# ============================================================================",
		"# CHAOS REDUX - UNIVERSAL STATE REGISTRY LIVE TRIGGERS",
		"# Generated by .tools/build_formable_state_registry.py; do not hand-edit.",
		f"# Source: {source}",
		f"# Registered state entries: {len(entries)}",
		"# Runtime evaluation is live and state-scoped; no cache, event target,",
		"# periodic world scan, or broad country iterator is used here.",
		"# Horizontal wrap is handled by build-time geometry metadata, not script.",
		"# ============================================================================",
		"",
		"# State-scope primitives. ROOT is the prospective carrier country.",
		"chaosx_state_registry_controlled_by_root = {",
		"\tis_controlled_by = ROOT",
		"}",
		"",
		"chaosx_state_registry_owned_by_root = {",
		"\tis_owned_by = ROOT",
		"}",
		"",
		"chaosx_state_registry_owned_and_controlled_by_root = {",
		"\tis_owned_and_controlled_by = ROOT",
		"}",
		"",
		"chaosx_state_registry_controlled_by_root_or_subject = {",
		"\t# State-scope controller check; no country iterator is required.",
		"\tOR = {",
		"\t\tis_controlled_by = ROOT",
		"\t\tcontroller = { is_subject_of = ROOT }",
		"\t}",
		"}",
		"",
		"chaosx_state_registry_owned_by_root_or_subject = {",
		"\t# State-scope owner check; no country iterator is required.",
		"\tOR = {",
		"\t\tis_owned_by = ROOT",
		"\t\towner = { is_subject_of = ROOT }",
		"\t}",
		"}",
		"",
	]
	if map_wrap_width is not None:
		lines.insert(6, f"# World-width for projection consumers: {map_wrap_width}")
	for state in entries:
		state_id = state["state_id"]
		names = helper_names(state_id)
		lines.extend(
			[
				f"# State {state_id}: {state.get('name_key', f'STATE_{state_id}')}",
				f"{names['controlled_by_root']} = {{",
				f"\t{state_id} = {{ chaosx_state_registry_controlled_by_root = yes }}",
				"}",
				"",
				f"{names['owned_by_root']} = {{",
				f"\t{state_id} = {{ chaosx_state_registry_owned_by_root = yes }}",
				"}",
				"",
				f"{names['owned_and_controlled_by_root']} = {{",
				f"\t{state_id} = {{ chaosx_state_registry_owned_and_controlled_by_root = yes }}",
				"}",
				"",
				f"{names['controlled_by_root_or_subject']} = {{",
				f"\t{state_id} = {{ chaosx_state_registry_controlled_by_root_or_subject = yes }}",
				"}",
				"",
				f"{names['owned_by_root_or_subject']} = {{",
				f"\t{state_id} = {{ chaosx_state_registry_owned_by_root_or_subject = yes }}",
				"}",
				"",
			]
		)
	return "\n".join(lines)


def build_index(document: dict[str, Any], entries: list[dict[str, Any]], provenance: dict[str, Any], source_path: Path, content_hash: str) -> dict[str, Any]:
	map_data = registry_map(document)
	map_width = map_data.get("width") or document.get("width")
	map_height = map_data.get("height") or document.get("height")
	if map_width is None and isinstance(map_data.get("dimensions"), list):
		map_width, map_height = map_data["dimensions"][:2]
	geometry_encoding = document.get("geometry_encoding", {})
	map_wrap = geometry_encoding.get("map_wrap", {}) if isinstance(geometry_encoding, dict) else {}
	index_states: list[dict[str, Any]] = []
	for state in entries:
		# Keep the index portable and review-friendly without duplicating the
		# canonical row-run payload. Consumers read row_runs from the source
		# geometry registry after validating its content hash.
		state_copy = {
			key: state[key]
			for key in (
				"state_id",
				"name_key",
				"source_state_file",
				"source_state_file_sha256",
				"province_ids",
				"province_count",
				"pixel_count",
				"row_count",
				"run_count",
				"tight_bbox",
				"circular_x_interval",
				"geometry_sha256",
			)
			if key in state
		}
		state_copy["runtime_helpers"] = helper_names(state["state_id"])
		# State-specific policy metadata is declarative.  A consumer may point at
		# an existing helper or compile a dedicated policy, but it cannot invent
		# dynamic state ids at runtime.
		state_copy.setdefault("qualification_policy", "controlled_by_root")
		state_copy.setdefault("visibility_policy", "required_by_consumer")
		index_states.append(state_copy)
	index: dict[str, Any] = {
		"schema": INDEX_SCHEMA,
		"registry_source_schema": document.get("schema_version", REGISTRY_SCHEMA),
		"registry_id": document.get("registry_id", "chaosx_universal_state_registry"),
		"source_geometry_registry": source_path.relative_to(ROOT).as_posix() if source_path.is_relative_to(ROOT) else source_path.as_posix(),
		"registry_content_sha256_algorithm": CANONICAL_HASH_ALGORITHM,
		"registry_content_sha256": content_hash,
		"map": {
			"mcp_revision": map_data.get("mcp_revision"),
			"width": map_width,
			"height": map_height,
			"horizontal_wrap": bool(map_wrap.get("horizontal") is True or map_wrap.get("axis") == "x"),
			"world_width": map_wrap.get("world_width", map_width),
			"source": provenance,
		},
		"counts": {
			"states": len(index_states),
			"state_id_range": [index_states[0]["state_id"], index_states[-1]["state_id"]],
			"state_ids_sha256": active_state_ids_hash(state["state_id"] for state in index_states),
		},
		"runtime_contract": {
			"controlled_by_root": "live state controller equals ROOT",
			"owned_by_root": "live state owner equals ROOT",
			"owned_and_controlled_by_root": "live state owner and controller equal ROOT",
			"controlled_by_root_or_subject": "live state controller equals ROOT or is a subject of ROOT",
			"qualification_policy": "consumer-declared; defaults to controlled_by_root",
			"subject_policy": "use controlled_by_root_or_subject or an explicit carrier-scoped helper; never any_country",
		},
		"states": index_states,
	}
	return index


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--input", "--registry", dest="input_path", type=Path, default=DEFAULT_INPUT, help="geometry registry JSON (read-only)")
	parser.add_argument("--output-index", type=Path, default=DEFAULT_INDEX, help="portable normalized registry index")
	parser.add_argument("--output-triggers", type=Path, default=DEFAULT_TRIGGERS, help="generated scripted-trigger file")
	parser.add_argument("--game-root", type=Path, default=DEFAULT_GAME_ROOT, help="base HOI4 installation used for provenance checks")
	parser.add_argument("--mod-root", type=Path, action="append", default=[], help="map/state overlay root; repeat in load order")
	parser.add_argument("--replace-state-history", action="store_true", help="treat the last mod-root history/states as a complete replacement")
	parser.add_argument("--expected-state-count", type=int, default=None, help="optional expected active state count; defaults to the source registry count")
	parser.add_argument("--skip-provenance", action="store_true", help="skip active map hash/id checks; source registry validation still runs")
	parser.add_argument("--check", action="store_true", help="validate and report without writing outputs")
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	try:
		source_path = args.input_path if args.input_path.is_absolute() else ROOT / args.input_path
		if not source_path.is_file():
			raise RegistryError(f"geometry registry is missing: {source_path}. Run the geometry producer first.")
		document = json.loads(source_path.read_text(encoding="utf-8"))
		if not isinstance(document, dict):
			raise RegistryError("source registry root must be an object")
		schema = document.get("schema") or document.get("schema_id")
		if schema not in (None, REGISTRY_SCHEMA, "chaos-redux-state-geometry-registry/v1") and document.get("schema_version") != "1.0.0":
			raise RegistryError(f"unsupported source registry schema: {schema!r}")
		entries = source_state_entries(document)
		counts = document.get("counts") if isinstance(document.get("counts"), dict) else {}
		source_count_value = counts.get("state_count", counts.get("states", len(entries)))
		try:
			source_expected_count = int(source_count_value)
		except (TypeError, ValueError) as exc:
			raise RegistryError("source registry count must be numeric") from exc
		if source_expected_count != len(entries):
			raise RegistryError(f"source registry count={source_expected_count} disagrees with {len(entries)} state entries")
		expected_count = args.expected_state_count if args.expected_state_count is not None else source_expected_count
		if len(entries) != expected_count:
			raise RegistryError(f"source registry has {len(entries)} states, expected {expected_count}")
		state_id_range = counts.get("state_id_range")
		if state_id_range is not None:
			if not isinstance(state_id_range, list) or len(state_id_range) != 2 or state_id_range != [entries[0]["state_id"], entries[-1]["state_id"]]:
				raise RegistryError("counts.state_id_range must match the sorted source state ids")
		geometry_encoding = document.get("geometry_encoding", {})
		if geometry_encoding and geometry_encoding.get("type") != "absolute_row_runs":
			raise RegistryError("geometry_encoding.type must be absolute_row_runs")
		validate_geometry(document, entries)
		content_hash = validate_content_hash(document)

		roots = [args.game_root.resolve(), *[Path(value).resolve() for value in args.mod_root]]
		for root in roots:
			if not root.is_dir():
				raise RegistryError(f"map root does not exist: {root}")
		if args.skip_provenance:
			provenance = {"skipped": True, "reason": "--skip-provenance"}
		else:
			provenance = validate_source_hash(
				document,
				entries,
				game_roots=roots,
				replace_history=args.replace_state_history,
				expected_count=expected_count,
			)
		map_data = registry_map(document)
		map_wrap = document.get("geometry_encoding", {}).get("map_wrap", {})
		map_width = map_wrap.get("world_width") or map_data.get("width") or document.get("width")
		index = build_index(document, entries, provenance, source_path, content_hash)
		triggers = generate_triggers(entries, source_path.relative_to(ROOT).as_posix() if source_path.is_relative_to(ROOT) else source_path.as_posix(), map_wrap_width=map_width)
		if args.check:
			print(f"Validated {len(entries)} states against {len(roots)} map root(s); no files written.")
			return 0
		args.output_index.parent.mkdir(parents=True, exist_ok=True)
		args.output_triggers.parent.mkdir(parents=True, exist_ok=True)
		args.output_index.write_text(json.dumps(index, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
		args.output_triggers.write_text(triggers, encoding="utf-8")
		print(f"Built universal registry for {len(entries)} states.")
		print(f"Index: {args.output_index}")
		print(f"Triggers: {args.output_triggers}")
		return 0
	except (OSError, json.JSONDecodeError, RegistryError) as exc:
		print(f"ERROR: {exc}", file=sys.stderr)
		return 2


if __name__ == "__main__":
	raise SystemExit(main())
