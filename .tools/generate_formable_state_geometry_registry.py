#!/usr/bin/env python3
"""Rebuild the universal state geometry registry from an active HOI4 map.

This producer is deliberately independent of the runtime game. It resolves a
base installation plus explicit map/state overlays, reads the active province
bitmap and state history, and emits the canonical absolute-row-run source used
by ``build_formable_state_registry.py``. HOI4 cannot discover a changed map or
create unknown state textures at runtime, so this command must be rerun before
shipping a registry for a different combined map.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = TOOLS_DIR.parent
if str(TOOLS_DIR) not in sys.path:

	sys.path.insert(0, str(TOOLS_DIR))

from build_formable_state_registry import (  # noqa: E402
	CANONICAL_HASH_ALGORITHM,
	DEFAULT_GAME_ROOT,
	RegistryError,
	canonical_hash,
	sha256_file,
	state_files,
	strip_clausewitz_comments,
)


DEFAULT_OUTPUT = ROOT / "docs/formables/state_registry/generated/state_geometry_registry.json"
STATE_ID_RE = re.compile(r"\bid\s*=\s*(\d+)")
STATE_NAME_RE = re.compile(r"\bname\s*=\s*([\"'])(.*?)\1", re.DOTALL)
PROVINCES_RE = re.compile(r"\bprovinces\s*=\s*\{([^{}]*)\}", re.DOTALL)


def parse_state_history(path: Path, expected_id: int) -> tuple[str, list[int]]:
	text = strip_clausewitz_comments(path.read_text(encoding="utf-8-sig"))
	id_match = STATE_ID_RE.search(text)
	if id_match is None or int(id_match.group(1)) != expected_id:
		raise RegistryError(f"{path} does not declare its filename state id {expected_id}")
	name_match = STATE_NAME_RE.search(text)
	name_key = name_match.group(2).strip() if name_match else f"STATE_{expected_id}"
	provinces_match = PROVINCES_RE.search(text)
	if provinces_match is None:
		raise RegistryError(f"{path} is missing a provinces={{...}} block")
	province_ids = [int(value) for value in re.findall(r"\b\d+\b", provinces_match.group(1))]
	if not province_ids or len(set(province_ids)) != len(province_ids):
		raise RegistryError(f"{path} has no unique province list")
	return name_key, sorted(province_ids)


def parse_definition(path: Path) -> tuple[dict[int, tuple[int, int, int]], int]:
	colors: dict[int, tuple[int, int, int]] = {}
	province_by_color: dict[tuple[int, int, int], int] = {}
	definition_count = 0
	with path.open("r", encoding="utf-8-sig", newline="") as handle:
		for line_number, row in enumerate(csv.reader(handle, delimiter=";"), start=1):
			if not row or not row[0].strip():
				continue
			try:
				province_id = int(row[0].strip())
				rgb = tuple(int(row[index].strip()) for index in (1, 2, 3))
			except (ValueError, IndexError) as exc:
				raise RegistryError(f"invalid definition.csv row {line_number}") from exc
			if province_id < 0 or any(channel < 0 or channel > 255 for channel in rgb):
				raise RegistryError(f"invalid definition.csv values on row {line_number}")
			definition_count += 1
			if province_id == 0:
				continue
			if province_id in colors and colors[province_id] != rgb:
				raise RegistryError(f"province {province_id} has conflicting definition colors")
			other_province = province_by_color.get(rgb)
			if other_province is not None and other_province != province_id:
				raise RegistryError(
					f"definition color {rgb} is shared by provinces {other_province} and {province_id}"
				)
			colors[province_id] = rgb
			province_by_color[rgb] = province_id
	if not colors:
		raise RegistryError("definition.csv is empty")
	return colors, definition_count


def packed_rgb(rgb: tuple[int, int, int]) -> int:
	return (rgb[0] << 16) | (rgb[1] << 8) | rgb[2]


def circular_interval(columns: np.ndarray, width: int) -> dict[str, int | bool]:
	if columns.size == 0:
		raise RegistryError("cannot calculate a circular interval for empty geometry")
	gaps = np.diff(np.concatenate((columns, np.asarray([int(columns[0]) + width], dtype=columns.dtype)))) - 1
	max_gap = int(gaps.max())
	start = int(columns[(int(np.argmax(gaps)) + 1) % columns.size])
	length = width - max_gap
	end = start + length - 1
	wraps = end >= width
	return {
		"start_x": start,
		"length": length,
		"end_x_unwrapped": end,
		"wraps_x_seam": wraps,
		"unwrap_offset": start if wraps else 0,
	}


def state_geometry(
	state_image: np.ndarray,
	state_ids: list[int],
	state_metadata: dict[int, tuple[str, list[int], Path]],
	width: int,
	height: int,
) -> list[dict[str, Any]]:
	rows_by_state: dict[int, list[list[Any]]] = {state_id: [] for state_id in state_ids}
	pixel_counts = {state_id: 0 for state_id in state_ids}
	run_counts = {state_id: 0 for state_id in state_ids}
	bboxes: dict[int, list[int] | None] = {state_id: None for state_id in state_ids}
	columns = np.zeros((len(state_ids), width), dtype=np.bool_)
	index_by_id = {state_id: index for index, state_id in enumerate(state_ids)}

	for y in range(height):
		row = state_image[y]
		boundaries = np.flatnonzero(row[1:] != row[:-1]) + 1
		starts = np.concatenate((np.asarray([0], dtype=np.int64), boundaries))
		ends = np.concatenate((boundaries, np.asarray([width], dtype=np.int64)))
		for x_start, x_end in zip(starts.tolist(), ends.tolist()):
			state_id = int(row[x_start])
			if state_id not in index_by_id:
				continue
			length = x_end - x_start
			state_rows = rows_by_state[state_id]
			if state_rows and state_rows[-1][0] == y:
				state_rows[-1][1].extend([x_start, length])
			else:
				state_rows.append([y, [x_start, length]])
			pixel_counts[state_id] += length
			run_counts[state_id] += 1
			columns[index_by_id[state_id], x_start:x_end] = True
			bbox = bboxes[state_id]
			if bbox is None:
				bboxes[state_id] = [x_start, y, x_end - 1, y]
			else:
				bbox[0] = min(bbox[0], x_start)
				bbox[1] = min(bbox[1], y)
				bbox[2] = max(bbox[2], x_end - 1)
				bbox[3] = max(bbox[3], y)

	result: list[dict[str, Any]] = []
	for index, state_id in enumerate(state_ids):
		rows = rows_by_state[state_id]
		if not rows or pixel_counts[state_id] <= 0 or bboxes[state_id] is None:
			raise RegistryError(f"state {state_id} has no nonzero map geometry")
		name_key, province_ids, path = state_metadata[state_id]
		row_runs = rows
		interval = circular_interval(np.flatnonzero(columns[index]), width)
		result.append(
			{
				"state_id": state_id,
				"name_key": name_key,
				"source_state_file": f"history/states/{path.name}",
				"source_state_file_sha256": sha256_file(path),
				"province_ids": province_ids,
				"province_count": len(province_ids),
				"pixel_count": pixel_counts[state_id],
				"row_count": len(rows),
				"run_count": run_counts[state_id],
				"tight_bbox": bboxes[state_id],
				"circular_x_interval": interval,
				"geometry_sha256": hashlib.sha256(json.dumps(row_runs, ensure_ascii=True, separators=(",", ":")).encode("utf-8")).hexdigest(),
				"row_runs": row_runs,
			}
		)
	return result


def build_registry(
	game_root: Path,
	mod_roots: list[Path],
	*,
	replace_history: bool,
	registry_id: str,
	mcp_revision: str | None,
	mcp_artifacts: list[str] | None = None,
	mcp_post_qa_revision: str | None = None,
	mcp_revision_notes: str | None = None,
) -> dict[str, Any]:
	roots = [game_root.resolve(), *[root.resolve() for root in mod_roots]]
	for root in roots:
		if not root.is_dir():
			raise RegistryError(f"map root does not exist: {root}")
	map_rel = "map/provinces.bmp"
	definition_rel = "map/definition.csv"
	provinces_path = next((root / map_rel for root in reversed(roots) if (root / map_rel).is_file()), None)
	definition_path = next((root / definition_rel for root in reversed(roots) if (root / definition_rel).is_file()), None)
	if provinces_path is None or definition_path is None:
		raise RegistryError("active map requires map/provinces.bmp and map/definition.csv")
	active_files = state_files(roots, replace_history=replace_history)
	state_metadata: dict[int, tuple[str, list[int], Path]] = {}
	for state_id, path in active_files.items():
		name_key, province_ids = parse_state_history(path, state_id)
		state_metadata[state_id] = (name_key, province_ids, path)
	definition, definition_count = parse_definition(definition_path)
	with Image.open(provinces_path) as image:
		image = image.convert("RGB")
		rgb = np.asarray(image, dtype=np.uint8)
	height, width = rgb.shape[:2]
	packed = (rgb[:, :, 0].astype(np.uint32) << 16) | (rgb[:, :, 1].astype(np.uint32) << 8) | rgb[:, :, 2].astype(np.uint32)
	color_to_province: dict[int, int] = {}
	for province_id, color in definition.items():
		packed_color = packed_rgb(color)
		previous = color_to_province.get(packed_color)
		if previous is not None and previous != province_id:
			raise RegistryError(f"RGB color {color} is assigned to provinces {previous} and {province_id}")
		color_to_province[packed_color] = province_id
	lut = np.full(1 << 24, -1, dtype=np.int32)
	for color, province_id in color_to_province.items():
		lut[color] = province_id
	province_image = lut[packed]
	unknown_nonzero = int(np.count_nonzero((packed != 0) & (province_image < 0)))
	if unknown_nonzero:
		raise RegistryError(f"provinces.bmp contains {unknown_nonzero} nonzero pixels absent from definition.csv")
	observed_province_ids = {int(value) for value in np.unique(province_image) if int(value) > 0}
	all_state_history_reconstruction_matches = all(
		province_id in definition and province_id in observed_province_ids
		for _, (_, province_ids, _) in state_metadata.items()
		for province_id in province_ids
	)
	if not all_state_history_reconstruction_matches:
		raise RegistryError("state history references a province absent from definition.csv or provinces.bmp")
	province_to_state = np.zeros(max(max(definition), int(province_image.max(initial=0))) + 1, dtype=np.int32)
	for state_id, (_, province_ids, _) in state_metadata.items():
		for province_id in province_ids:
			if province_id not in definition or province_id >= province_to_state.size:
				raise RegistryError(f"state {state_id} references province {province_id} absent from definition.csv")
			if province_id not in observed_province_ids:
				raise RegistryError(f"state {state_id} references province {province_id} absent from provinces.bmp")
			if province_to_state[province_id] not in (0, state_id):
				raise RegistryError(f"province {province_id} belongs to multiple active states")
			province_to_state[province_id] = state_id
	state_image = np.zeros_like(province_image, dtype=np.int32)
	known = province_image >= 0
	state_image[known] = province_to_state[province_image[known]]
	state_ids = sorted(active_files)
	states = state_geometry(state_image, state_ids, state_metadata, width, height)
	unassigned_map_pixels = int(np.count_nonzero(state_image == 0))
	bundle_rows = [f"{state_id}|history/states/{active_files[state_id].name}|{sha256_file(active_files[state_id])}\n" for state_id in state_ids]
	bundle_hash = hashlib.sha256("".join(bundle_rows).encode("utf-8")).hexdigest()
	if mcp_revision is None:
		mcp_revision = f"local-{sha256_file(provinces_path)[:16]}-{sha256_file(definition_path)[:16]}"
	mcp_artifacts = list(mcp_artifacts or [])
	map_data = {
		"mcp_revision": mcp_revision,
		"mcp_artifact_uris": mcp_artifacts,
		"width": width,
		"height": height,
		"coordinate_system": {
			"x_origin": "left",
			"y_origin": "top",
			"x_range": [0, width - 1],
			"y_range": [0, height - 1],
			"x_wraps": True,
		},
		"provinces_bmp": {"path": map_rel, "sha256": sha256_file(provinces_path)},
		"definition_csv": {"path": definition_rel, "sha256": sha256_file(definition_path), "definition_count": definition_count},
		"state_history_root": "history/states",
		"state_history_bundle_sha256": bundle_hash,
	}
	if mcp_post_qa_revision:
		map_data["mcp_post_qa_revision"] = mcp_post_qa_revision
	if mcp_revision_notes:
		map_data["mcp_revision_notes"] = mcp_revision_notes
	document: dict[str, Any] = {
		"schema_version": "1.0.0",
		"registry_id": registry_id,
		"description": "Deterministic geometry registry for every installed HOI4 state; absolute map row runs are canonical and circular x intervals handle horizontal world wrapping.",
		"source_root_alias": "HOI4_INSTALL",
		"map": map_data,
		"geometry_encoding": {
			"type": "absolute_row_runs",
			"row_format": "[y, [x_start, length, x_start, length, ...]]",
			"x_start_inclusive": True,
			"length_positive": True,
			"y_ascending": True,
			"x_ascending": True,
			"runs_are_absolute_map_coordinates": True,
			"map_wrap": {
				"horizontal": True,
				"axis": "x",
				"world_width": width,
				"canonical_runs_do_not_unwrap": True,
				"unwrap_rule": "for circular interval, x_prime = x if x >= start_x else x + world_width",
			},
		},
		"counts": {
			"state_count": len(states),
			"state_id_range": [state_ids[0], state_ids[-1]],
			"province_definition_count": definition_count,
			"assigned_state_pixel_count": int(sum(state["pixel_count"] for state in states)),
			"unassigned_map_pixel_count": unassigned_map_pixels,
			"unknown_nonzero_pixel_count": unknown_nonzero,
			"total_row_run_count": int(sum(state["run_count"] for state in states)),
			"all_states_nonzero": True,
			"all_state_history_reconstruction_matches": all_state_history_reconstruction_matches,
			"horizontal_seam_crossing_state_count": int(sum(state["circular_x_interval"]["wraps_x_seam"] for state in states)),
		},
		"states": states,
		"registry_content_sha256_algorithm": CANONICAL_HASH_ALGORITHM,
		"wrap_analysis": {
			"horizontal_axis": "x",
			"world_width": width,
			"crossing_state_ids": [
				state["state_id"]
				for state in states
				if state["tight_bbox"][0] == 0 and state["tight_bbox"][2] == width - 1
			],
			"nearest_seam_state_rule": "min(min_x, world_width-1-max_x), then state_id",
			"note": "Absolute row runs remain canonical. Circular intervals are emitted for every state.",
		},
	}
	document["registry_content_sha256"] = canonical_hash(document)
	return document


def deterministic_core(document: dict[str, Any]) -> dict[str, Any]:
	"""Remove review-only metadata before comparing a rebuild with a handoff."""
	core = json.loads(json.dumps(document))
	for key in ("registry_content_sha256", "wrap_analysis"):
		core.pop(key, None)
	map_data = core.get("map")
	if isinstance(map_data, dict):
		for key in ("mcp_revision", "mcp_artifact_uris", "mcp_post_qa_revision", "mcp_revision_notes"):
			map_data.pop(key, None)
	geometry = core.get("geometry_encoding")
	if isinstance(geometry, dict) and isinstance(geometry.get("map_wrap"), dict):
		# ``axis: x`` is the original producer spelling; newer manifests also
		# expose the equivalent explicit ``horizontal: true`` flag.
		geometry["map_wrap"].pop("horizontal", None)
		geometry["map_wrap"].pop("axis", None)
	return core


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--game-root", type=Path, default=DEFAULT_GAME_ROOT)
	parser.add_argument("--mod-root", type=Path, action="append", default=[], help="map/state overlay root; repeat in load order")
	parser.add_argument("--replace-state-history", action="store_true", help="treat the last mod-root history/states as a complete replacement")
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	parser.add_argument("--registry-id", default="chaos_redux_universal_state_geometry")
	parser.add_argument("--mcp-revision", help="review/MCP revision to record in provenance metadata")
	parser.add_argument("--mcp-artifact", action="append", default=[], help="review/MCP artifact URI; repeat for each artifact")
	parser.add_argument("--mcp-post-qa-revision", help="post-generation MCP QA revision to record")
	parser.add_argument("--mcp-revision-notes", help="short provenance note for the recorded MCP revisions")
	parser.add_argument("--check", action="store_true", help="rebuild in memory and compare with the existing output")
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	try:
		document = build_registry(
			args.game_root,
			args.mod_root,
			replace_history=args.replace_state_history,
			registry_id=args.registry_id,
			mcp_revision=args.mcp_revision,
			mcp_artifacts=args.mcp_artifact,
			mcp_post_qa_revision=args.mcp_post_qa_revision,
			mcp_revision_notes=args.mcp_revision_notes,
		)
		output = args.output if args.output.is_absolute() else ROOT / args.output
		if args.check:
			if not output.is_file():
				raise RegistryError(f"cannot check missing output: {output}")
			existing = json.loads(output.read_text(encoding="utf-8"))
			if deterministic_core(existing) != deterministic_core(document):
				raise RegistryError(f"generated registry core differs from {output}; rerun without --check to rebuild it")
			print(f"Checked active map geometry against {output}; no files written.")
			return 0
		output.parent.mkdir(parents=True, exist_ok=True)
		output.write_text(json.dumps(document, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
		print(f"Generated {len(document['states'])} state geometries at {output}.")
		return 0
	except (OSError, json.JSONDecodeError, RegistryError) as exc:
		print(f"ERROR: {exc}", file=sys.stderr)
		return 2


if __name__ == "__main__":
	raise SystemExit(main())
