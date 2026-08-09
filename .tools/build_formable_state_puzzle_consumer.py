#!/usr/bin/env python3
"""Compile a state-puzzle consumer spec into exact geometry assets and a manifest.

The compiler consumes the fixed candidate state set from the universal registry,
projects canonical row runs with explicit horizontal-wrap handling, writes
unresolved/qualifying PNG and HOI4 BGRA DDS pairs, and emits the manifest read by
``generate_formable_state_puzzle_runtime.mjs``. Runtime qualification remains a
live scripted-trigger decision; this command only builds the finite candidate
geometry and records the helper hooks.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import subprocess
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
	RegistryError,
	canonical_hash,
	registry_map,
	source_state_entries,
	validate_content_hash,
	validate_geometry,
)


CONSUMER_SCHEMA = "chaos-redux-formable-state-puzzle-consumer/v1"
DEFAULT_REGISTRY = ROOT / "docs/formables/state_registry/generated/state_geometry_registry.json"
DEFAULT_DDS_CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
POLICY_SUFFIXES = {
	"controlled_by_root": "controlled_by_root",
	"owned_by_root": "owned_by_root",
	"owned_and_controlled_by_root": "owned_and_controlled_by_root",
	"controlled_by_root_or_subject": "controlled_by_root_or_subject",
	"owned_by_root_or_subject": "owned_by_root_or_subject",
}
SCRIPT_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def script_identifier(value: Any, *, field: str) -> str:
	if not isinstance(value, str) or not SCRIPT_IDENTIFIER_RE.fullmatch(value):
		raise RegistryError(f"{field} must be a Clausewitz scripted identifier matching [A-Za-z_][A-Za-z0-9_]*: {value!r}")
	return value


def script_token(value: Any, *, field: str = "id") -> str:
	if not isinstance(value, str) or not value.strip():
		raise RegistryError(f"{field} must be a non-empty string")
	token = re.sub(r"[^A-Za-z0-9_]", "_", value).lower().strip("_")
	if not token or not re.search(r"[a-z0-9]", token):
		raise RegistryError(f"{field} normalises to an empty scripted token: {value!r}")
	return token


def sha256_file(path: Path) -> str:
	hash_obj = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			hash_obj.update(chunk)
	return hash_obj.hexdigest()


def portable(value: str) -> str:
	return value.replace("\\", "/")


def resolve_workspace(value: str | Path) -> Path:
	path = Path(value)
	return path if path.is_absolute() else ROOT / path


def read_spec(path: Path) -> dict[str, Any]:
	spec = json.loads(path.read_text(encoding="utf-8-sig"))
	if not isinstance(spec, dict) or spec.get("schema") != CONSUMER_SCHEMA:
		raise RegistryError(f"unsupported consumer spec schema in {path}")
	for key in ("category_id", "formable_id", "registry", "projection", "state_ids"):
		if key not in spec:
			raise RegistryError(f"consumer spec is missing {key}")
	for key in ("category_id", "formable_id"):
		if not isinstance(spec[key], str) or not spec[key].strip():
			raise RegistryError(f"consumer spec {key} must be a non-empty string")
		script_token(spec[key], field=key)
	if not isinstance(spec["registry"], str) or not spec["registry"].strip():
		raise RegistryError("consumer spec registry must be a non-empty path")
	projection_data = spec["projection"]
	if not isinstance(projection_data, dict):
		raise RegistryError("projection must be an object")
	canvas = projection_data.get("canvas")
	padding = projection_data.get("padding")
	if not isinstance(canvas, list) or len(canvas) != 2 or any(not isinstance(value, int) or value <= 0 for value in canvas):
		raise RegistryError("projection.canvas must contain two positive integers")
	if not isinstance(padding, int) or padding < 0 or padding * 2 >= min(canvas):
		raise RegistryError("projection.padding must leave a positive drawing area")
	state_ids = spec.get("state_ids")
	if not isinstance(state_ids, list) or not state_ids or any(type(value) is not int or value < 1 for value in state_ids):
		raise RegistryError("state_ids must be a non-empty list of positive integers")
	if len(set(state_ids)) != len(state_ids):
		raise RegistryError("state_ids must be unique")
	declared_state_ids = set(state_ids)
	groups = spec.get("state_groups", [])
	if not isinstance(groups, list):
		raise RegistryError("state_groups must be a list")
	for group in groups:
		if not isinstance(group, dict) or not isinstance(group.get("state_ids"), list):
			raise RegistryError("state_groups entries require a state_ids list")
		if "group_id" in group:
			script_token(group["group_id"], field="state_groups.group_id")
		if any(type(value) is not int or value < 1 for value in group["state_ids"]):
			raise RegistryError("state_groups state_ids must contain positive integers")
		unknown_group_ids = sorted(set(group["state_ids"]) - declared_state_ids)
		if unknown_group_ids:
			raise RegistryError(f"state group {group.get('group_id', '<unnamed>')} names undeclared ids: {unknown_group_ids}")
	assets = spec.get("assets", {})
	if not isinstance(assets, dict):
		raise RegistryError("assets must be an object")
	for key in ("unresolved_rgba", "qualifying_rgba"):
		if key not in assets:
			continue
		value = assets[key]
		if not isinstance(value, list) or len(value) != 4 or any(not isinstance(channel, int) or channel < 0 or channel > 255 for channel in value):
			raise RegistryError(f"assets.{key} must contain four integer channels in 0..255")
	for key in ("qualification_policy", "visibility_policy", "territory_helper"):
		if key in spec and spec[key] is not None and not isinstance(spec[key], str):
			raise RegistryError(f"consumer spec {key} must be a string when supplied")
	if spec.get("territory_helper") is not None:
		script_identifier(spec["territory_helper"], field="territory_helper")
	if "output" in spec and not isinstance(spec["output"], dict):
		raise RegistryError("output must be an object")
	overrides = spec.get("state_overrides", [])
	if not isinstance(overrides, list):
		raise RegistryError("state_overrides must be a list")
	for override in overrides:
		if not isinstance(override, dict):
			raise RegistryError("state_overrides entries must be objects")
		for key in ("qualification_helper", "visibility_helper"):
			if key in override and override[key] is not None:
				script_identifier(override[key], field=f"state_overrides.{key}")
		if "required" in override and type(override["required"]) is not bool:
			raise RegistryError("state_overrides.required must be boolean")
	return spec


def load_registry(path: Path) -> tuple[dict[str, Any], dict[int, dict[str, Any]]]:
	document = json.loads(path.read_text(encoding="utf-8-sig"))
	if not isinstance(document, dict):
		raise RegistryError("registry root must be an object")
	entries = source_state_entries(document)
	validate_geometry(document, entries)
	validate_content_hash(document)
	return document, {entry["state_id"]: entry for entry in entries}


def global_x_segments(x_start: int, length: int, wrap_start: int, world_width: int) -> list[tuple[int, int]]:
	"""Split one absolute run at the global projection cut and unwrap once."""
	end = x_start + length
	if end <= wrap_start:
		return [(x_start + world_width, length)] if wrap_start else [(x_start, length)]
	if x_start >= wrap_start:
		return [(x_start, length)]
	left_length = wrap_start - x_start
	return [(wrap_start, end - wrap_start), (x_start + world_width, left_length)]


def state_source_bounds(state: dict[str, Any], wrap_start: int, world_width: int) -> tuple[int, int, int, int]:
	min_x = world_width * 2
	max_x = -1
	rows = state["row_runs"]
	min_y = rows[0][0]
	max_y = rows[-1][0]
	for y, values in rows:
		min_y = min(min_y, y)
		max_y = max(max_y, y)
		for index in range(0, len(values), 2):
			for x0, length in global_x_segments(values[index], values[index + 1], wrap_start, world_width):
				min_x = min(min_x, x0)
				max_x = max(max_x, x0 + length - 1)
	return min_x, min_y, max_x, max_y


def candidate_wrap_frame(states: list[dict[str, Any]], world_width: int) -> tuple[int, int, bool]:
	"""Choose one circular cut from the union of all candidate columns."""
	occupied = np.zeros(world_width, dtype=np.bool_)
	for state in states:
		for _, values in state["row_runs"]:
			for index in range(0, len(values), 2):
				x_start, length = values[index : index + 2]
				occupied[x_start : x_start + length] = True
	columns = np.flatnonzero(occupied)
	if columns.size == 0:
		raise RegistryError("candidate set has no occupied map columns")
	gaps = np.diff(np.concatenate((columns, np.asarray([int(columns[0]) + world_width], dtype=columns.dtype)))) - 1
	max_gap = int(gaps.max())
	wrap_start = int(columns[(int(np.argmax(gaps)) + 1) % columns.size])
	length = world_width - max_gap
	return wrap_start, length, wrap_start + length - 1 >= world_width


def helper_for_policy(state_id: int, policy: str | None, explicit: str | None, *, field: str) -> str | None:
	if explicit is not None:
		return script_identifier(explicit, field=f"state {state_id}.{field}_helper")
	if policy is not None and not isinstance(policy, str):
		raise RegistryError(f"state {state_id} has non-string {field} policy {policy!r}")
	if policy in (None, "required_by_consumer", "always", "none"):
		return None
	if policy in POLICY_SUFFIXES:
		return f"chaosx_state_registry_state_{state_id}_{POLICY_SUFFIXES[policy]}"
	if policy.startswith("chaosx_"):
		return script_identifier(policy, field=f"state {state_id}.{field} policy")
	raise RegistryError(f"state {state_id} has unsupported {field} policy {policy!r}; provide an explicit helper")


def state_options(spec: dict[str, Any], state_ids: list[int]) -> dict[int, dict[str, Any]]:
	global_qualification = spec.get("qualification_policy", "controlled_by_root")
	global_visibility = spec.get("visibility_policy", "required_by_consumer")
	overrides: dict[int, dict[str, Any]] = {}
	for raw in spec.get("state_overrides", []):
		if not isinstance(raw, dict) or type(raw.get("state_id")) is not int:
			raise RegistryError("state_overrides entries require numeric state_id")
		state_id = raw["state_id"]
		if state_id in overrides:
			raise RegistryError(f"duplicate state override {state_id}")
		overrides[state_id] = raw
	unknown_overrides = sorted(set(overrides) - set(state_ids))
	if unknown_overrides:
		raise RegistryError(f"state overrides name ids outside state_ids: {unknown_overrides}")
	result: dict[int, dict[str, Any]] = {}
	for state_id in state_ids:
		override = overrides.get(state_id, {})
		qualification_policy = override.get("qualification_policy", global_qualification)
		visibility_policy = override.get("visibility_policy", global_visibility)
		qualification_helper = helper_for_policy(state_id, qualification_policy, override.get("qualification_helper"), field="qualification")
		if not qualification_helper:
			raise RegistryError(f"state {state_id} must resolve a qualification_helper")
		visibility_helper = helper_for_policy(state_id, visibility_policy, override.get("visibility_helper"), field="visibility")
		required = override.get("required", True)
		if type(required) is not bool:
			raise RegistryError(f"state {state_id}.required must be boolean")
		if not required and not visibility_helper:
			raise RegistryError(f"optional state {state_id} requires a visibility_helper")
		result[state_id] = {
			"required": required,
			"qualification_policy": qualification_policy,
			"visibility_policy": visibility_policy,
			"qualification_helper": qualification_helper,
			"visibility_helper": visibility_helper,
		}
	return result


def projection(spec: dict[str, Any], states: list[dict[str, Any]], world_width: int) -> dict[str, Any]:
	canvas_width, canvas_height = spec["projection"]["canvas"]
	padding = spec["projection"]["padding"]
	wrap_start, wrap_length, wraps_x_seam = candidate_wrap_frame(states, world_width)
	bounds = [state_source_bounds(state, wrap_start, world_width) for state in states]
	source_bbox = [min(item[0] for item in bounds), min(item[1] for item in bounds), max(item[2] for item in bounds), max(item[3] for item in bounds)]
	source_width = source_bbox[2] - source_bbox[0] + 1
	source_height = source_bbox[3] - source_bbox[1] + 1
	available_width = canvas_width - 2 * padding
	available_height = canvas_height - 2 * padding
	scale = float(spec["projection"].get("scale") or min(available_width / source_width, available_height / source_height))
	if scale <= 0:
		raise RegistryError("projection scale must be positive")
	used_width = source_width * scale
	used_height = source_height * scale
	left = float(spec["projection"].get("offset", [padding + (available_width - used_width) / 2, padding + (available_height - used_height) / 2])[0])
	top = float(spec["projection"].get("offset", [padding + (available_width - used_width) / 2, padding + (available_height - used_height) / 2])[1])
	return {
		"canvas": [canvas_width, canvas_height],
		"source_bbox": source_bbox,
		"scale": scale,
		"offset": [left, top],
		"wrap_start": wrap_start,
		"wrap_length": wrap_length,
		"wraps_x_seam": wraps_x_seam,
		"world_width": world_width,
	}


def render_state(state: dict[str, Any], projection_data: dict[str, Any], world_width: int, colour: tuple[int, int, int, int]) -> tuple[Image.Image, list[int]]:
	canvas_width, canvas_height = projection_data["canvas"]
	min_x, min_y, _, _ = projection_data["source_bbox"]
	scale = projection_data["scale"]
	left, top = projection_data["offset"]
	wrap_start = projection_data["wrap_start"]
	mask = np.zeros((canvas_height, canvas_width), dtype=np.bool_)
	for y, values in state["row_runs"]:
		y0 = max(0, int(math.floor((y - min_y) * scale + top)))
		y1 = min(canvas_height - 1, int(math.ceil((y + 1 - min_y) * scale + top) - 1))
		if y1 < y0:
			continue
		for index in range(0, len(values), 2):
			for x_start, length in global_x_segments(values[index], values[index + 1], wrap_start, world_width):
				x0 = max(0, int(math.floor((x_start - min_x) * scale + left)))
				x1 = min(canvas_width - 1, int(math.ceil((x_start + length - min_x) * scale + left) - 1))
				if x1 >= x0:
					mask[y0 : y1 + 1, x0 : x1 + 1] = True
	alpha = np.zeros((canvas_height, canvas_width, 4), dtype=np.uint8)
	alpha[mask] = np.asarray(colour, dtype=np.uint8)
	image = Image.fromarray(alpha, mode="RGBA")
	bbox = image.getbbox()
	if bbox is None:
		raise RegistryError(f"state {state['state_id']} rendered to an empty projection")
	return image.crop(bbox), [bbox[0], bbox[1], bbox[2] - 1, bbox[3] - 1]


def path_from_spec(spec: dict[str, Any], key: str, default: str) -> tuple[str, Path]:
	relative = spec.get("output", {}).get(key, default)
	if not isinstance(relative, str) or not relative:
		raise RegistryError(f"output.{key} must be a non-empty relative path")
	path = Path(relative)
	if path.is_absolute() or path.drive or ".." in path.parts:
		raise RegistryError(f"output.{key} must remain inside the mod workspace: {relative!r}")
	relative = portable(relative)
	resolved = (ROOT / relative).resolve()
	if not resolved.is_relative_to(ROOT.resolve()):
		raise RegistryError(f"output.{key} escapes the mod workspace: {relative!r}")
	return relative, resolved


def run_dds_converter(converter: Path, source: Path, output: Path) -> None:
	output.parent.mkdir(parents=True, exist_ok=True)
	command = [sys.executable, str(converter), "--input", str(source), "--output", str(output)]
	completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if completed.returncode != 0 or not output.is_file():
		raise RegistryError(f"DDS conversion failed for {source}: {completed.stderr.strip()}")


def aggregate_territory_trigger(formable_id: str, category_id: str, state_records: list[dict[str, Any]]) -> tuple[str, str]:
	token = script_token(category_id or formable_id)
	helper = f"chaosx_state_registry_consumer_{token}_territory_qualifies"
	lines = [
		"# ============================================================================",
		"# CHAOS REDUX - GENERATED CONSUMER TERRITORY CONTRACT",
		"# Live state helpers only; no scans, caches, event targets, or on_actions.",
		f"# Consumer: {category_id} ({formable_id})",
		"# ============================================================================",
		"",
		f"{helper} = {{",
		"\tAND = {",
	]
	for state in state_records:
		qualification = state.get("qualification_helper")
		if not qualification:
			raise RegistryError(f"state {state['state_id']} has no qualification helper for territory contract")
		visibility = state.get("visibility_helper")
		if state.get("required") or not visibility:
			lines.append(f"\t\t{qualification} = yes")
		else:
			lines.append("\t\tOR = {")
			lines.append(f"\t\t\tNOT = {{ {visibility} = yes }}")
			lines.append(f"\t\t\t{qualification} = yes")
			lines.append("\t\t}")
	lines.extend(["\t}", "}", ""])
	return helper, "\n".join(lines)


def png_bytes(image: Image.Image) -> bytes:
	buffer = io.BytesIO()
	image.save(buffer, format="PNG", optimize=False)
	return buffer.getvalue()


def compile_consumer(spec: dict[str, Any], *, dry_run: bool, convert_dds: bool, converter: Path) -> dict[str, Any]:
	registry_path = resolve_workspace(spec.get("registry", DEFAULT_REGISTRY))
	document, by_id = load_registry(registry_path)
	state_ids = list(spec["state_ids"])
	unknown = sorted(set(state_ids) - set(by_id))
	if unknown:
		raise RegistryError(f"consumer names unknown registry state ids: {unknown}")
	state_ids = sorted(state_ids)
	states = [by_id[state_id] for state_id in state_ids]
	map_data = registry_map(document)
	world_width = document.get("geometry_encoding", {}).get("map_wrap", {}).get("world_width") or map_data.get("width") or document.get("width")
	if not isinstance(world_width, int) or world_width <= 0:
		raise RegistryError("registry does not expose a positive horizontal world width")
	projection_data = projection(spec, states, world_width)
	options = state_options(spec, state_ids)
	canvas_width, canvas_height = projection_data["canvas"]
	default_assets = spec.get("assets", {})
	unresolved_colour = tuple(default_assets.get("unresolved_rgba", [190, 150, 40, 230]))
	qualifying_colour = tuple(default_assets.get("qualifying_rgba", [40, 180, 80, 255]))
	category = spec["category_id"]
	formable = spec["formable_id"]
	manifest_rel, manifest_path = path_from_spec(spec, "manifest", f"docs/formables/state_puzzles/{category}/manifest.json")
	source_dir_rel, source_dir = path_from_spec(spec, "source_dir", f"docs/formables/state_puzzles/{category}/source")
	processed_dir_rel, processed_dir = path_from_spec(spec, "processed_dir", f"docs/formables/state_puzzles/{category}/processed")
	dds_dir_rel, dds_dir = path_from_spec(spec, "dds_dir", f"gfx/interface/formables/state_puzzles/{category}/states")
	preview_dir_rel, preview_dir = path_from_spec(spec, "preview_dir", f"docs/formables/state_puzzles/{category}")
	preview_unresolved = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
	preview_qualifying = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
	assets: list[dict[str, Any]] = []
	state_records: list[dict[str, Any]] = []
	for state in states:
		state_id = state["state_id"]
		sprite_base = f"{formable}_state_{state_id}"
		variant_records: dict[str, dict[str, Any]] = {}
		for variant, colour in (("unresolved", unresolved_colour), ("qualifying", qualifying_colour)):
			image, bbox = render_state(state, projection_data, world_width, colour)
			position = [bbox[0], bbox[1]]
			sprite_name = f"{sprite_base}_{variant}"
			source_rel = portable(f"{source_dir_rel}/{sprite_name}.png")
			processed_rel = portable(f"{processed_dir_rel}/{sprite_name}.png")
			dds_rel = portable(f"{dds_dir_rel}/{sprite_name}.dds")
			source_path = ROOT / source_rel
			processed_path = ROOT / processed_rel
			dds_path = ROOT / dds_rel
			payload = png_bytes(image)
			png_hash = hashlib.sha256(payload).hexdigest()
			if not dry_run:
				source_path.parent.mkdir(parents=True, exist_ok=True)
				processed_path.parent.mkdir(parents=True, exist_ok=True)
				source_path.write_bytes(payload)
				processed_path.write_bytes(payload)
				if convert_dds:
					run_dds_converter(converter, processed_path, dds_path)
				preview = preview_unresolved if variant == "unresolved" else preview_qualifying
				preview.alpha_composite(image, dest=tuple(position))
			asset = {
				"state_id": state_id,
				"variant": variant,
				"sprite_name": sprite_name,
				"source_png": source_rel,
				"processed_png": processed_rel,
				"dds": dds_rel,
				"bbox": bbox,
				"png_sha256": png_hash,
			}
			if not dry_run and convert_dds:
				asset["dds_sha256"] = sha256_file(dds_path)
			assets.append(asset)
			variant_records[variant] = asset
		state_records.append(
			{
				"state_id": state_id,
				"canvas_position": [variant_records["unresolved"]["bbox"][0], variant_records["unresolved"]["bbox"][1]],
				"qualification_policy": options[state_id]["qualification_policy"],
				"visibility_policy": options[state_id]["visibility_policy"],
				"qualification_helper": options[state_id]["qualification_helper"],
				"visibility_helper": options[state_id]["visibility_helper"],
				"sprite_names": {"unresolved": variant_records["unresolved"]["sprite_name"], "qualifying": variant_records["qualifying"]["sprite_name"]},
				"runtime_dds": {"unresolved": variant_records["unresolved"]["dds"], "qualifying": variant_records["qualifying"]["dds"]},
				"runtime_png": {"unresolved": variant_records["unresolved"]["processed_png"], "qualifying": variant_records["qualifying"]["processed_png"]},
				"required": options[state_id]["required"],
			}
		)
	if not dry_run:
		preview_dir.mkdir(parents=True, exist_ok=True)
		preview_unresolved.save(preview_dir / f"{category}_projection_{canvas_width}x{canvas_height}.png", format="PNG", optimize=False)
		preview_qualifying.save(preview_dir / f"{category}_projection_{canvas_width}x{canvas_height}_qualifying.png", format="PNG", optimize=False)
	geometry_artifact = {
		"schema": "chaos-redux-formable-state-puzzle-geometry/v1",
		"registry_id": document.get("registry_id"),
		"registry_content_sha256": document.get("registry_content_sha256"),
		"state_ids": state_ids,
		"projection": projection_data,
		"states": [{"state_id": state["state_id"], "geometry_sha256": state["geometry_sha256"], "circular_x_interval": state["circular_x_interval"]} for state in states],
	}
	geometry_artifact_rel = portable(f"{preview_dir_rel}/{category}_geometry_artifact.json")
	if not dry_run:
		(preview_dir / f"{category}_geometry_artifact.json").write_text(json.dumps(geometry_artifact, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
	state_groups = spec.get("state_groups") or [{"group_id": "required", "state_ids": state_ids}]
	territory_helper = spec.get("territory_helper")
	if territory_helper is not None:
		territory_helper = script_identifier(territory_helper, field="territory_helper")
	territory_source_rel = None
	if not territory_helper:
		territory_helper, territory_source = aggregate_territory_trigger(formable, category, state_records)
		territory_source_rel = portable(f"common/scripted_triggers/chaosx_state_registry_consumer_{script_token(category)}.txt")
		if not dry_run:
			(ROOT / territory_source_rel).write_text(territory_source, encoding="utf-8")
	manifest: dict[str, Any] = {
		# A --no-dds pass is an intentionally staged asset build.  Runtime
		# discovery only accepts complete manifests, so it cannot ingest paths
		# whose DDS files have not been emitted yet.
		"status": "complete" if convert_dds else "assets_pending",
		"schema": "chaos-redux-formable-state-puzzle/v1",
		"category_id": category,
		"decision_category": category,
		"formable_id": formable,
		"registry_source": portable(str(registry_path.relative_to(ROOT))) if registry_path.is_relative_to(ROOT) else portable(str(registry_path)),
		"registry_content_sha256": document.get("registry_content_sha256"),
		"map_revision": map_data.get("mcp_revision"),
		"map_file_sha256": map_data.get("provinces_bmp", {}).get("sha256"),
		"geometry_artifact": geometry_artifact_rel,
		"projection": projection_data,
		"state_groups": state_groups,
		"state_policy": {
			"required_state_ids": [state_id for state_id in state_ids if options[state_id]["required"]],
			"candidate_state_ids": state_ids,
		},
		"qualification_policy": spec.get("qualification_policy", "controlled_by_root"),
		"visibility_policy": spec.get("visibility_policy", "required_by_consumer"),
		"territory_helper": territory_helper,
		"territory_helper_source": territory_source_rel,
		"states": state_records,
		"assets": assets,
		"previews": [
			portable(f"{preview_dir_rel}/{category}_projection_{canvas_width}x{canvas_height}.png"),
			portable(f"{preview_dir_rel}/{category}_projection_{canvas_width}x{canvas_height}_qualifying.png"),
			geometry_artifact_rel,
		],
	}
	manifest["manifest_sha256"] = canonical_hash(manifest)
	if not dry_run:
		manifest_path.parent.mkdir(parents=True, exist_ok=True)
		manifest_path.write_text(json.dumps(manifest, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
	return manifest


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--spec", type=Path, required=True)
	parser.add_argument("--registry", type=Path, help="override registry path from spec")
	parser.add_argument("--dds-converter", type=Path, default=DEFAULT_DDS_CONVERTER)
	parser.add_argument("--dry-run", action="store_true", help="validate/project in memory without writing PNG, DDS, previews, or manifest")
	parser.add_argument("--no-dds", action="store_true", help="write PNGs/manifest but leave DDS conversion to a later asset pass")
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	try:
		spec_path = args.spec if args.spec.is_absolute() else ROOT / args.spec
		spec = read_spec(spec_path)
		if args.registry:
			spec["registry"] = portable(str(args.registry))
		if not args.dry_run and spec.get("status") != "complete":
			raise RegistryError("non-dry consumer builds require spec.status=complete")
		manifest = compile_consumer(spec, dry_run=args.dry_run, convert_dds=not args.no_dds, converter=resolve_workspace(args.dds_converter))
		print(f"Compiled consumer {manifest['category_id']} with {len(manifest['states'])} fixed state candidates.")
		print(f"Qualification hooks: {sum(1 for state in manifest['states'] if state.get('qualification_helper'))}; visibility hooks: {sum(1 for state in manifest['states'] if state.get('visibility_helper'))}.")
		if args.dry_run:
			print("Dry run: no files written.")
		return 0
	except (OSError, json.JSONDecodeError, RegistryError, ValueError) as exc:
		print(f"ERROR: {exc}", file=sys.stderr)
		return 2


if __name__ == "__main__":
	raise SystemExit(main())
