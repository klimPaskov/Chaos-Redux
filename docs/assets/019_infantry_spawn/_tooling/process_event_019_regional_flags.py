#!/usr/bin/env python3
"""Flatten, export, and validate the Event 019 regional flag matrix.

Every matrix row begins with its own unmodified built-in ImageGen full-flag
source.  The user-approved Event 019-only spot-colour pass performs a complete-
frame aspect normalisation, deterministic hue-family reduction without
dithering, and nearest-palette resizing.  It does not crop, draw, composite,
trace, relabel, or reuse another flag's geometry.

Outputs:

* one retained 820x520 spot-colour master per runtime tag;
* one opaque RGBA PNG at every vanilla HOI4 flag size;
* one bottom-left-origin, uncompressed 32-bit TGA at every runtime size;
* raw/master and three-size contact sheets;
* a machine-readable provenance/validation record and runtime checksums.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, __version__ as PILLOW_VERSION


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "019_infantry_spawn"
RAW_ROOT = PACKAGE / "source_png" / "flags" / "regional_full_flag_raw"
SPOT_MASTERS = PACKAGE / "processed_png" / "flags" / "regional_spot_colour_masters"
PROCESSED_FLAGS = PACKAGE / "processed_png" / "flags"
CONTACT = PACKAGE / "contact_sheets"
RUNTIME = ROOT / "gfx" / "flags"
FILE_EXE = Path("C:/Program Files/Git/usr/bin/file.exe")

IDENTITIES = (
	"CLAIMANT_BREAKAWAY",
	"ZOMBIE_BASE",
	"ZOMBIE_CLAIMANT",
	"ZOMBIE_COLLECTIVE",
	"ZOMBIE_SPECIES",
	"GHOST_BASE",
	"GHOST_CLAIMANT",
	"GHOST_COLLECTIVE",
	"GHOST_SPECIES",
	"GOLEM_BASE",
	"GOLEM_CLAIMANT",
	"GOLEM_COLLECTIVE",
	"GOLEM_SPECIES",
)

REGIONS = (
	"EUROPE",
	"MIDDLE_EAST",
	"AFRICA",
	"ASIA",
	"AUSTRALIA",
	"NORTH_AMERICA",
	"SOUTH_AMERICA",
)

REGION_DIRECTIONS = {
	"EUROPE": "split heraldic chevron",
	"MIDDLE_EAST": "eight-point interlaced knot",
	"AFRICA": "stepped sun and spearhead",
	"ASIA": "mountain-cloud open gate",
	"AUSTRALIA": "navigation star and waves",
	"NORTH_AMERICA": "broken star and rail chevron",
	"SOUTH_AMERICA": "condor-step and maize diamond",
}

SIZES = {
	"normal": (82, 52),
	"medium": (41, 26),
	"small": (10, 7),
}

DEFAULT_MASTER_SIZE = (820, 520)
DEFAULT_PALETTE_COLOURS = 8
DEFAULT_HUE_BINS = 16
DEFAULT_NEUTRAL_SATURATION = 64
DEFAULT_DARK_VALUE = 48
DEFAULT_MINIMUM_COLOUR_SHARE = 0.0005
DEFAULT_RUN_DATE = "2026-07-18"
REQUIRED_PYTHON = (3, 9, 12)
REQUIRED_PILLOW = "11.1.0"
REQUIRED_NUMPY = "2.0.2"
PROVENANCE_GLOB = "regional_full_flag_*_provenance_2026_07_18.md"


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"--palette-colours",
		type=int,
		default=DEFAULT_PALETTE_COLOURS,
		choices=range(6, 13),
		help="Fixed spot-colour palette size. Default: 8.",
	)
	parser.add_argument(
		"--master-width",
		type=int,
		default=DEFAULT_MASTER_SIZE[0],
		help="Flattened master width. Default: 820.",
	)
	parser.add_argument(
		"--master-height",
		type=int,
		default=DEFAULT_MASTER_SIZE[1],
		help="Flattened master height. Default: 520.",
	)
	parser.add_argument(
		"--hue-bins",
		type=int,
		default=DEFAULT_HUE_BINS,
		choices=range(12, 25),
		help="Circular chromatic hue-family count. Default: 16.",
	)
	parser.add_argument(
		"--neutral-saturation",
		type=int,
		default=DEFAULT_NEUTRAL_SATURATION,
		choices=range(32, 97),
		help="Pillow-HSV saturation below which a pixel is neutral. Default: 64.",
	)
	parser.add_argument(
		"--dark-value",
		type=int,
		default=DEFAULT_DARK_VALUE,
		choices=range(32, 81),
		help="Pillow-HSV value below which a pixel joins the dark family. Default: 48.",
	)
	parser.add_argument(
		"--minimum-colour-share",
		type=float,
		default=DEFAULT_MINIMUM_COLOUR_SHARE,
		help="Minimum source-pixel share for a retained spot family. Default: 0.0005.",
	)
	parser.add_argument(
		"--run-date",
		default=DEFAULT_RUN_DATE,
		help="Date token used in evidence filenames. Default: 2026-07-18.",
	)
	return parser.parse_args()


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
	for candidate in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if candidate.is_file():
			return ImageFont.truetype(str(candidate), size=size)
	return ImageFont.load_default()


def staged_path(final_path: Path, stage_root: Path) -> Path:
	try:
		relative = final_path.resolve().relative_to(ROOT.resolve())
	except ValueError as error:
		raise RuntimeError(f"Event 019 flag output escaped the repository root: {final_path}") from error
	return stage_root / relative


def ensure_stage_directories(stage_root: Path) -> None:
	for final_path in (
		SPOT_MASTERS,
		PROCESSED_FLAGS,
		CONTACT,
		RUNTIME,
		RUNTIME / "medium",
		RUNTIME / "small",
	):
		staged_path(final_path, stage_root).mkdir(parents=True, exist_ok=True)


def regional_tag(identity: str, region: str) -> str:
	return f"INFANTRY_SPAWN_{identity}_{region}"


def expected_tags() -> tuple[str, ...]:
	return tuple(regional_tag(identity, region) for identity in IDENTITIES for region in REGIONS)


def clean_markdown_value(value: str) -> str:
	return value.strip().strip("`").strip()


def parse_provenance_notes() -> dict[str, dict[str, object]]:
	note_paths = sorted((PACKAGE / "notes").glob(PROVENANCE_GLOB))
	if len(note_paths) != 3:
		raise RuntimeError(f"Expected three regional full-flag provenance notes, found {len(note_paths)}")
	records: dict[str, dict[str, object]] = {}
	section_pattern = re.compile(r"(?m)^### (INFANTRY_SPAWN_[A-Z0-9_]+)\s*$")
	field_pattern = re.compile(r"^- (.+?):\s*(.*)$")
	for note_path in note_paths:
		text = note_path.read_text(encoding="utf-8")
		matches = list(section_pattern.finditer(text))
		for index, match in enumerate(matches):
			tag = match.group(1)
			if tag in records:
				raise RuntimeError(f"Duplicate provenance record for {tag}")
			end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
			body = text[match.end() : end]
			fields: dict[str, str] = {}
			for line in body.splitlines():
				field_match = field_pattern.match(line)
				if field_match:
					field_name = field_match.group(1).strip().strip("*").strip()
					fields[field_name] = clean_markdown_value(field_match.group(2))

			raw_value = fields.get("Exact owned raw path", "")
			result_value = fields.get("Built-in ImageGen result handle/path", "")
			prompt_value = fields.get("Prompt-section reference", "")
			sha_value = fields.get("SHA-256", "")
			dimensions_value = fields.get("Dimensions and mode", "")
			disposition = fields.get("Disposition", "")
			visual_notes = fields.get("Visual survival notes", "")
			raw_match = re.search(r"docs/assets/019_infantry_spawn/[^\s`]+\.png", raw_value.replace("\\", "/"))
			handle_match = re.search(r"exec-[0-9a-f-]+\.png", result_value, flags=re.IGNORECASE)
			result_path_match = re.search(r"[A-Za-z]:/[^;\s`]+\.png", result_value.replace("\\", "/"))
			sha_match = re.search(r"\b[0-9a-fA-F]{64}\b", sha_value)
			dimensions_match = re.search(r"(\d+)\D+(\d+).*?\b(RGBA|RGB)\b", dimensions_value)
			prompt_path_match = re.search(r"regional_full_flag_[^\s()`]+_prompts_2026_07_18\.md", prompt_value)
			missing_fields = [
				name
				for name, present in (
					("raw path", raw_match),
					("ImageGen handle", handle_match),
					("ImageGen result path", result_path_match),
					("prompt reference", prompt_path_match),
					("SHA-256", sha_match),
					("dimensions/mode", dimensions_match),
					("disposition", disposition),
					("visual notes", visual_notes),
				)
				if not present
			]
			if missing_fields:
				raise RuntimeError(f"Incomplete ImageGen provenance for {tag}: {missing_fields}")

			raw_path = ROOT / Path(raw_match.group(0))
			result_path = Path(result_path_match.group(0))
			prompt_path = PACKAGE / "prompts" / prompt_path_match.group(0)
			records[tag] = {
				"source_mode": "built-in ImageGen, one distinct full-flag result",
				"provenance_note": note_path.relative_to(ROOT).as_posix(),
				"raw_path": raw_path,
				"result_handle": handle_match.group(0),
				"result_path": result_path,
				"prompt_path": prompt_path,
				"prompt_reference": prompt_value,
				"sha256": sha_match.group(0).lower(),
				"dimensions": [int(dimensions_match.group(1)), int(dimensions_match.group(2))],
				"mode": dimensions_match.group(3),
				"disposition": disposition,
				"visual_survival_notes": visual_notes,
			}
	return records


def index_raw_sources(provenance: dict[str, dict[str, object]]) -> dict[str, Path]:
	indexed: dict[str, Path] = {}
	for path in RAW_ROOT.rglob("*_imagegen_raw.png"):
		tag = path.name.removesuffix("_imagegen_raw.png")
		if tag in indexed:
			raise RuntimeError(f"Duplicate unmodified raw source for {tag}: {indexed[tag]} and {path}")
		indexed[tag] = path

	expected = set(expected_tags())
	missing = sorted(expected - set(indexed))
	extra = sorted(set(indexed) - expected)
	if missing or extra:
		raise RuntimeError(
			"Raw-source matrix mismatch: "
			f"missing={len(missing)} {missing}; extra={len(extra)} {extra}"
		)
	provenance_missing = sorted(expected - set(provenance))
	provenance_extra = sorted(set(provenance) - expected)
	if provenance_missing or provenance_extra:
		raise RuntimeError(
			"Provenance matrix mismatch: "
			f"missing={len(provenance_missing)} {provenance_missing}; "
			f"extra={len(provenance_extra)} {provenance_extra}"
		)
	if len({sha256(path) for path in indexed.values()}) != len(expected):
		raise RuntimeError("Every regional tag must retain a byte-distinct built-in ImageGen raw source")
	result_hashes: set[str] = set()
	for tag, path in indexed.items():
		record = provenance[tag]
		if Path(record["raw_path"]).resolve() != path.resolve():
			raise RuntimeError(f"Provenance raw path does not match indexed source: {tag}")
		if not Path(record["prompt_path"]).is_file():
			raise RuntimeError(f"Prompt record is missing for {tag}: {record['prompt_path']}")
		if tag not in Path(record["prompt_path"]).read_text(encoding="utf-8"):
			raise RuntimeError(f"Prompt record does not identify its regional tag: {tag}")
		result_path = Path(record["result_path"])
		if not result_path.is_file():
			raise RuntimeError(f"Built-in ImageGen result path is missing for {tag}: {result_path}")
		if result_path.name.lower() != str(record["result_handle"]).lower():
			raise RuntimeError(f"Built-in ImageGen handle/path mismatch for {tag}")
		raw_hash = sha256(path)
		result_hash = sha256(result_path)
		if raw_hash != record["sha256"] or result_hash != record["sha256"]:
			raise RuntimeError(f"Raw/ImageGen/provenance hashes do not match for {tag}")
		result_hashes.add(result_hash)
		with Image.open(path) as opened:
			if opened.format != "PNG" or opened.mode not in {"RGB", "RGBA"}:
				raise RuntimeError(f"Raw source is not an RGB/RGBA PNG: {path}")
			if opened.mode == "RGBA" and opened.getchannel("A").getextrema() != (255, 255):
				raise RuntimeError(f"Raw source is not fully opaque: {path}")
			if list(opened.size) != record["dimensions"] or opened.mode != record["mode"]:
				raise RuntimeError(f"Raw dimensions/mode do not match provenance for {tag}")
	if len(result_hashes) != len(expected):
		raise RuntimeError("Every regional tag must link to a byte-distinct built-in ImageGen result")
	return indexed


def flatten_raw(
	raw: Image.Image,
	master_size: tuple[int, int],
	palette_colours: int,
	hue_bins: int,
	neutral_saturation: int,
	dark_value: int,
	minimum_colour_share: float,
) -> tuple[Image.Image, list[tuple[int, int, int]], list[dict[str, object]], dict[str, object]]:
	# Preserve the complete full-flag frame.  Aspect normalisation is an explicit
	# full-frame resize rather than a crop, so no hoist/fly emblem or border is cut.
	rgb = raw.convert("RGB")
	normalized = rgb.resize(master_size, Image.Resampling.LANCZOS)
	rgb_array = np.asarray(normalized, dtype=np.uint8)
	hsv_array = np.asarray(normalized.convert("HSV"), dtype=np.uint16)
	hue = hsv_array[..., 0]
	saturation = hsv_array[..., 1]
	value = hsv_array[..., 2]
	family_codes = np.empty(hue.shape, dtype=np.int16)
	dark_mask = value < dark_value
	neutral_mask = (saturation < neutral_saturation) & ~dark_mask
	family_codes[dark_mask] = 0
	family_codes[neutral_mask & (value < 190)] = 1
	family_codes[neutral_mask & (value >= 190)] = 2
	chromatic_mask = ~dark_mask & ~neutral_mask
	hue_width = 256.0 / hue_bins
	hue_family = np.floor(((hue.astype(np.float32) + hue_width / 2.0) % 256.0) / hue_width).astype(np.int16)
	family_codes[chromatic_mask] = 3 + hue_family[chromatic_mask]

	flat_rgb = rgb_array.reshape(-1, 3)
	flat_saturation = saturation.reshape(-1)
	flat_codes = family_codes.reshape(-1)
	total_pixels = flat_codes.size
	groups: list[dict[str, object]] = []
	for code_value in np.unique(flat_codes):
		mask = flat_codes == code_value
		samples = flat_rgb[mask]
		mean = samples.astype(np.float64).mean(axis=0)
		distances = ((samples.astype(np.float64) - mean) ** 2).sum(axis=1)
		representative = samples[int(np.argmin(distances))].copy()
		count = int(mask.sum())
		mean_saturation = float(flat_saturation[mask].mean())
		kind = "chromatic" if int(code_value) >= 3 else ("dark" if int(code_value) == 0 else "neutral")
		family = f"hue_{int(code_value) - 3:02d}" if kind == "chromatic" else ("neutral_dark" if int(code_value) == 0 else f"neutral_{int(code_value)}")
		groups.append(
			{
				"code": int(code_value),
				"family": family,
				"kind": kind,
				"source_pixels": count,
				"source_share": count / total_pixels,
				"mean_saturation": mean_saturation,
				"representative": representative,
				"importance": count * (1.0 + 0.75 * mean_saturation / 255.0),
			}
		)

	eligible = [group for group in groups if group["source_share"] >= minimum_colour_share]
	if len(eligible) < 4:
		eligible = sorted(groups, key=lambda group: (-group["source_pixels"], group["code"]))[:4]
	chromatic = sorted(
		(group for group in eligible if group["kind"] == "chromatic"),
		key=lambda group: (-group["importance"], group["code"]),
	)
	reserved_chromatic_count = min(len(chromatic), max(2, palette_colours - 3))
	selected = chromatic[:reserved_chromatic_count]
	selected_codes = {group["code"] for group in selected}
	remaining = sorted(
		(group for group in eligible if group["code"] not in selected_codes),
		key=lambda group: (-group["importance"], group["code"]),
	)
	selected.extend(remaining[: max(0, palette_colours - len(selected))])
	if len(selected) < 4:
		raise RuntimeError("Spot-colour normalizer could not retain four source colour families")

	selected_by_code = {group["code"]: group for group in selected}
	mapping: dict[int, int] = {}
	for group in groups:
		code = int(group["code"])
		if code in selected_by_code:
			mapping[code] = code
			continue
		representative = group["representative"].astype(np.int32)
		mapping[code] = min(
			selected_by_code,
			key=lambda candidate: int(
				((representative - selected_by_code[candidate]["representative"].astype(np.int32)) ** 2).sum()
			),
		)

	selected_order = sorted(selected_by_code)
	palette_index_by_code = {code: index for index, code in enumerate(selected_order)}
	label_array = np.empty(family_codes.shape, dtype=np.uint8)
	for group in groups:
		code = int(group["code"])
		label_array[family_codes == code] = palette_index_by_code[mapping[code]]
	# One native-master 3x3 mode pass removes isolated shade/noise pixels caused
	# by ImageGen tonal falloff.  At 820x520 it does not redraw authored forms.
	label_array = np.asarray(
		Image.fromarray(label_array, mode="L").filter(ImageFilter.ModeFilter(3)),
		dtype=np.uint8,
	)
	selected_rgb = np.asarray(
		[selected_by_code[code]["representative"] for code in selected_order],
		dtype=np.uint8,
	)
	master_array = selected_rgb[label_array]
	master = Image.fromarray(master_array, mode="RGB")

	unique_rgb, unique_counts = np.unique(master_array.reshape(-1, 3), axis=0, return_counts=True)
	ordered_palette = sorted(
		((tuple(int(channel) for channel in rgb_value), int(count)) for rgb_value, count in zip(unique_rgb, unique_counts)),
		key=lambda item: (-item[1], item[0]),
	)
	palette = [rgb_value for rgb_value, _ in ordered_palette]
	palette_records = [
		{
			"index": index,
			"rgb": list(rgb_value),
			"hex": f"#{rgb_value[0]:02x}{rgb_value[1]:02x}{rgb_value[2]:02x}",
			"pixels": count,
			"share": count / total_pixels,
			"representative_is_exact_normalized_source_pixel": True,
		}
		for index, (rgb_value, count) in enumerate(ordered_palette)
	]
	if not 3 < len(palette) <= palette_colours:
		raise RuntimeError(f"Spot-colour master uses unsafe palette size: {len(palette)}")

	source_edges = np.asarray(normalized.convert("L").filter(ImageFilter.FIND_EDGES), dtype=np.uint8) >= 32
	master_edges = np.asarray(master.convert("L").filter(ImageFilter.FIND_EDGES), dtype=np.uint8) >= 24
	source_edges[[0, -1], :] = False
	source_edges[:, [0, -1]] = False
	master_edges[[0, -1], :] = False
	master_edges[:, [0, -1]] = False
	dilated_master_edges = np.asarray(
		Image.fromarray(master_edges.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(3)),
		dtype=np.uint8,
	) > 0
	source_edge_count = int(source_edges.sum())
	edge_recall = float((source_edges & dilated_master_edges).sum() / source_edge_count) if source_edge_count else 0.0
	if source_edge_count == 0 or edge_recall < 0.60:
		raise RuntimeError(f"Spot-colour geometry recall is unsafe: edges={source_edge_count}, recall={edge_recall:.4f}")

	group_records = []
	for group in sorted(groups, key=lambda item: item["code"]):
		mapped_group = selected_by_code[mapping[int(group["code"])]]
		group_records.append(
			{
				"family": group["family"],
				"kind": group["kind"],
				"source_pixels": group["source_pixels"],
				"source_share": group["source_share"],
				"mean_saturation": group["mean_saturation"],
				"source_sample_rgb": [int(channel) for channel in group["representative"]],
				"retained": int(group["code"]) in selected_by_code,
				"mapped_to_family": mapped_group["family"],
			}
		)
	geometry = {
		"normalisation": "full-frame non-uniform resize; no crop, pad, draw, composite, or trace",
		"source_dimensions": list(rgb.size),
		"master_dimensions": list(master_size),
		"source_aspect_ratio": rgb.width / rgb.height,
		"master_aspect_ratio": master_size[0] / master_size[1],
		"horizontal_scale": master_size[0] / rgb.width,
		"vertical_scale": master_size[1] / rgb.height,
		"source_strong_edge_pixels": source_edge_count,
		"master_strong_edge_pixels": int(master_edges.sum()),
		"source_edge_recall_with_one_pixel_tolerance": edge_recall,
		"family_records": group_records,
	}
	return master, palette, palette_records, geometry


def map_to_spot_palette(image: Image.Image, palette: list[tuple[int, int, int]]) -> Image.Image:
	lookup: dict[tuple[int, int, int], tuple[int, int, int]] = {}
	mapped: list[tuple[int, int, int, int]] = []
	for pixel in image.convert("RGB").getdata():
		if pixel not in lookup:
			lookup[pixel] = min(
				palette,
				key=lambda candidate: (
					(pixel[0] - candidate[0]) ** 2
					+ (pixel[1] - candidate[1]) ** 2
					+ (pixel[2] - candidate[2]) ** 2
				),
			)
		red, green, blue = lookup[pixel]
		mapped.append((red, green, blue, 255))
	result = Image.new("RGBA", image.size, (0, 0, 0, 255))
	result.putdata(mapped)
	return result


def write_tga_bottom_left(image: Image.Image, path: Path) -> None:
	image = image.convert("RGBA")
	width, height = image.size
	header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
	rgba = image.tobytes()
	row_bytes = width * 4
	path.parent.mkdir(parents=True, exist_ok=True)
	with path.open("wb") as handle:
		handle.write(header)
		for y in range(height - 1, -1, -1):
			row = rgba[y * row_bytes : (y + 1) * row_bytes]
			bgra = bytearray(row_bytes)
			for index in range(0, row_bytes, 4):
				red, green, blue, alpha = row[index : index + 4]
				bgra[index : index + 4] = bytes((blue, green, red, alpha))
			handle.write(bgra)


def runtime_path(tag: str, tier: str) -> Path:
	root = RUNTIME if tier == "normal" else RUNTIME / tier
	return root / f"{tag}.tga"


def processed_path(tag: str, tier: str) -> Path:
	return PROCESSED_FLAGS / f"{tag}_{tier}.png"


def spot_master_path(tag: str) -> Path:
	return SPOT_MASTERS / f"{tag}_spot_master.png"


def process(
	raw_sources: dict[str, Path],
	provenance: dict[str, dict[str, object]],
	master_size: tuple[int, int],
	palette_colours: int,
	hue_bins: int,
	neutral_saturation: int,
	dark_value: int,
	minimum_colour_share: float,
	stage_root: Path,
) -> list[dict[str, object]]:
	records: list[dict[str, object]] = []
	for identity in IDENTITIES:
		for region in REGIONS:
			tag = regional_tag(identity, region)
			raw_path = raw_sources[tag]
			with Image.open(raw_path) as opened:
				raw_size = opened.size
				raw_mode = opened.mode
				master, palette, palette_records, geometry = flatten_raw(
					opened,
					master_size,
					palette_colours,
					hue_bins,
					neutral_saturation,
					dark_value,
					minimum_colour_share,
				)
			master_final = spot_master_path(tag)
			master_stage = staged_path(master_final, stage_root)
			master.save(master_stage)

			tier_records: list[dict[str, object]] = []
			for tier, size in SIZES.items():
				resized = master.resize(size, Image.Resampling.LANCZOS)
				processed = map_to_spot_palette(resized, palette)
				png_final = processed_path(tag, tier)
				tga_final = runtime_path(tag, tier)
				png_stage = staged_path(png_final, stage_root)
				tga_stage = staged_path(tga_final, stage_root)
				processed.save(png_stage)
				write_tga_bottom_left(processed, tga_stage)
				tier_records.append(
					{
						"tier": tier,
						"dimensions": list(size),
						"processed_png": png_final.relative_to(ROOT).as_posix(),
						"processed_sha256": sha256(png_stage),
						"runtime_tga": tga_final.relative_to(ROOT).as_posix(),
						"runtime_sha256": sha256(tga_stage),
						"used_rgb_colours": len(processed.getcolors(maxcolors=size[0] * size[1]) or []),
					}
				)

			provenance_record = provenance[tag]
			records.append(
				{
					"tag": tag,
					"identity": identity,
					"region": region,
					"regional_motif": REGION_DIRECTIONS[region],
					"source_mode": provenance_record["source_mode"],
					"provenance_note": provenance_record["provenance_note"],
					"prompt_record": Path(provenance_record["prompt_path"]).relative_to(ROOT).as_posix(),
					"prompt_reference": provenance_record["prompt_reference"],
					"built_in_imagegen_result_handle": provenance_record["result_handle"],
					"built_in_imagegen_result_path": Path(provenance_record["result_path"]).as_posix(),
					"built_in_imagegen_result_sha256": sha256(Path(provenance_record["result_path"])),
					"raw_source": raw_path.relative_to(ROOT).as_posix(),
					"raw_sha256": sha256(raw_path),
					"raw_is_exact_byte_copy_of_built_in_result": True,
					"raw_dimensions": list(raw_size),
					"raw_mode": raw_mode,
					"raw_disposition": provenance_record["disposition"],
					"raw_visual_survival_notes": provenance_record["visual_survival_notes"],
					"spot_master": master_final.relative_to(ROOT).as_posix(),
					"spot_master_sha256": sha256(master_stage),
					"spot_master_dimensions": list(master_size),
					"spot_master_mode": "RGB",
					"spot_palette": palette_records,
					"geometry_and_colour_families": geometry,
					"tiers": tier_records,
				}
			)
	return records


def make_raw_spot_contact_sheet(raw_sources: dict[str, Path], palette_colours: int, stage_root: Path) -> None:
	row_label_width = 225
	header_height = 58
	cell_width, cell_height = 344, 152
	sheet = Image.new(
		"RGB",
		(row_label_width + len(REGIONS) * cell_width, header_height + len(IDENTITIES) * cell_height),
		(31, 33, 35),
	)
	draw = ImageDraw.Draw(sheet)
	header_font = font(13)
	row_font = font(13)
	note_font = font(10)
	for column, region in enumerate(REGIONS):
		x = row_label_width + column * cell_width
		draw.text((x + 6, 12), region.replace("_", " "), font=header_font, fill=(245, 240, 226))
	for row, identity in enumerate(IDENTITIES):
		y = header_height + row * cell_height
		draw.text((8, y + 60), identity, font=row_font, fill=(235, 236, 237))
		for column, region in enumerate(REGIONS):
			x = row_label_width + column * cell_width
			tag = regional_tag(identity, region)
			with Image.open(raw_sources[tag]) as opened:
				raw = opened.convert("RGB").resize((154, 98), Image.Resampling.LANCZOS)
			with Image.open(staged_path(spot_master_path(tag), stage_root)) as opened:
				spot = opened.convert("RGB").resize((154, 98), Image.Resampling.NEAREST)
			sheet.paste(raw, (x + 6, y + 20))
			sheet.paste(spot, (x + 170, y + 20))
			draw.text((x + 6, y + 122), "unmodified ImageGen raw", font=note_font, fill=(177, 181, 184))
			draw.text((x + 170, y + 122), f"max {palette_colours}-colour spot master", font=note_font, fill=(177, 181, 184))
		draw.line((0, y + cell_height - 1, sheet.width, y + cell_height - 1), fill=(67, 70, 73))
	sheet.save(staged_path(CONTACT / "event_019_regional_full_flag_raw_spot_contact_sheet.png", stage_root))


def make_matrix_contact_sheet(stage_root: Path) -> None:
	row_label_width = 225
	header_height = 58
	cell_width, cell_height = 304, 136
	sheet = Image.new(
		"RGB",
		(row_label_width + len(REGIONS) * cell_width, header_height + len(IDENTITIES) * cell_height),
		(31, 33, 35),
	)
	draw = ImageDraw.Draw(sheet)
	header_font = font(13)
	row_font = font(13)
	note_font = font(10)
	for column, region in enumerate(REGIONS):
		x = row_label_width + column * cell_width
		draw.text((x + 6, 12), region.replace("_", " "), font=header_font, fill=(245, 240, 226))
	for row, identity in enumerate(IDENTITIES):
		y = header_height + row * cell_height
		draw.text((8, y + 52), identity, font=row_font, fill=(235, 236, 237))
		for column, region in enumerate(REGIONS):
			x = row_label_width + column * cell_width
			tag = regional_tag(identity, region)
			with Image.open(staged_path(processed_path(tag, "normal"), stage_root)) as opened:
				normal = opened.convert("RGB").resize((164, 104), Image.Resampling.NEAREST)
			with Image.open(staged_path(processed_path(tag, "medium"), stage_root)) as opened:
				medium = opened.convert("RGB").resize((82, 52), Image.Resampling.NEAREST)
			with Image.open(staged_path(processed_path(tag, "small"), stage_root)) as opened:
				small = opened.convert("RGB").resize((50, 35), Image.Resampling.NEAREST)
			sheet.paste(normal, (x + 5, y + 12))
			sheet.paste(medium, (x + 174, y + 38))
			sheet.paste(small, (x + 255, y + 46))
			draw.text((x + 5, y + 119), "82x52", font=note_font, fill=(177, 181, 184))
			draw.text((x + 174, y + 94), "41x26", font=note_font, fill=(177, 181, 184))
			draw.text((x + 255, y + 84), "10x7", font=note_font, fill=(177, 181, 184))
		draw.line((0, y + cell_height - 1, sheet.width, y + cell_height - 1), fill=(67, 70, 73))
	sheet.save(staged_path(CONTACT / "event_019_regional_flag_contact_sheet.png", stage_root))


def make_small_readability_sheet(stage_root: Path) -> None:
	row_label_width = 225
	header_height = 54
	cell_width, cell_height = 118, 94
	sheet = Image.new(
		"RGB",
		(row_label_width + len(REGIONS) * cell_width, header_height + len(IDENTITIES) * cell_height),
		(31, 33, 35),
	)
	draw = ImageDraw.Draw(sheet)
	header_font = font(11)
	row_font = font(12)
	for column, region in enumerate(REGIONS):
		x = row_label_width + column * cell_width
		draw.text((x + 4, 12), region.replace("_", " "), font=header_font, fill=(245, 240, 226))
	for row, identity in enumerate(IDENTITIES):
		y = header_height + row * cell_height
		draw.text((8, y + 35), identity, font=row_font, fill=(235, 236, 237))
		for column, region in enumerate(REGIONS):
			x = row_label_width + column * cell_width
			with Image.open(staged_path(processed_path(regional_tag(identity, region), "small"), stage_root)) as opened:
				small = opened.convert("RGB").resize((100, 70), Image.Resampling.NEAREST)
			sheet.paste(small, (x + 9, y + 11))
		draw.line((0, y + cell_height - 1, sheet.width, y + cell_height - 1), fill=(67, 70, 73))
	sheet.save(staged_path(CONTACT / "event_019_regional_flag_small_readability_contact_sheet.png", stage_root))


def parse_tga(path: Path) -> dict[str, object]:
	data = path.read_bytes()
	if len(data) < 18:
		raise RuntimeError(f"Short TGA: {path}")
	header = struct.unpack("<BBBHHBHHHHBB", data[:18])
	(
		id_length,
		colour_map_type,
		image_type,
		colour_map_first,
		colour_map_length,
		colour_map_depth,
		x_origin,
		y_origin,
		width,
		height,
		depth,
		descriptor,
	) = header
	return {
		"id_length": id_length,
		"colour_map_type": colour_map_type,
		"image_type": image_type,
		"colour_map_first": colour_map_first,
		"colour_map_length": colour_map_length,
		"colour_map_depth": colour_map_depth,
		"x_origin": x_origin,
		"y_origin": y_origin,
		"width": width,
		"height": height,
		"depth": depth,
		"descriptor": descriptor,
		"byte_length": len(data),
		"alpha_range": [min(data[21::4]), max(data[21::4])],
	}


def file_description(path: Path) -> str:
	result = subprocess.run([str(FILE_EXE), "-b", str(path)], check=True, capture_output=True, text=True)
	return result.stdout.strip()


def validate(
	raw_sources: dict[str, Path],
	process_records: list[dict[str, object]],
	master_size: tuple[int, int],
	palette_colours: int,
	hue_bins: int,
	neutral_saturation: int,
	dark_value: int,
	minimum_colour_share: float,
	run_date: str,
	stage_root: Path,
) -> dict[str, object]:
	if not FILE_EXE.is_file():
		raise FileNotFoundError(f"Required file validator is missing: {FILE_EXE}")
	if len(process_records) != len(IDENTITIES) * len(REGIONS):
		raise RuntimeError("Processing record count does not match the 13x7 matrix")

	raw_hashes: set[str] = set()
	master_hashes: set[str] = set()
	tier_hashes: dict[str, set[str]] = {tier: set() for tier in SIZES}
	runtime_tier_hashes: dict[str, set[str]] = {tier: set() for tier in SIZES}
	checksums: list[str] = []
	for record in process_records:
		tag = str(record["tag"])
		raw_path = raw_sources[tag]
		master_final = spot_master_path(tag)
		master_path = staged_path(master_final, stage_root)
		raw_hashes.add(sha256(raw_path))
		master_hashes.add(sha256(master_path))
		with Image.open(master_path) as opened:
			if opened.size != master_size or opened.mode != "RGB":
				raise RuntimeError(f"Wrong flattened master contract: {master_path}")
			master_colours = opened.getcolors(maxcolors=master_size[0] * master_size[1]) or []
			if not 3 < len(master_colours) <= palette_colours:
				raise RuntimeError(f"Flattened master uses an unsafe spot-colour count: {master_path}")

		palette = {tuple(item["rgb"]) for item in record["spot_palette"]}
		if len(palette) != len(master_colours):
			raise RuntimeError(f"Recorded spot palette is incomplete: {tag}")

		for tier, size in SIZES.items():
			tier_record = next(item for item in record["tiers"] if item["tier"] == tier)
			png_final = processed_path(tag, tier)
			tga_final = runtime_path(tag, tier)
			png_path = staged_path(png_final, stage_root)
			tga_path = staged_path(tga_final, stage_root)
			with Image.open(png_path) as opened:
				if opened.size != size or opened.mode != "RGBA":
					raise RuntimeError(f"Wrong processed PNG contract: {png_path}")
				png = opened.convert("RGBA")
			if png.getchannel("A").getextrema() != (255, 255):
				raise RuntimeError(f"Flag PNG is not fully opaque RGBA: {png_path}")
			used_rgb = {pixel[:3] for pixel in png.getdata()}
			if not used_rgb.issubset(palette):
				raise RuntimeError(f"Processed flag escaped its recorded spot palette: {png_path}")
			minimum_used_colours = {"normal": 4, "medium": 3, "small": 2}[tier]
			if len(used_rgb) < minimum_used_colours:
				raise RuntimeError(f"Processed flag lost too many colour families at {tier}: {png_path}")
			png_hash = sha256(png_path)
			tier_hashes[tier].add(png_hash)

			header = parse_tga(tga_path)
			expected_length = 18 + size[0] * size[1] * 4
			contract = (
				header["id_length"] == 0
				and header["colour_map_type"] == 0
				and header["image_type"] == 2
				and header["colour_map_first"] == 0
				and header["colour_map_length"] == 0
				and header["colour_map_depth"] == 0
				and header["x_origin"] == 0
				and header["y_origin"] == 0
				and (header["width"], header["height"]) == size
				and header["depth"] == 32
				and header["descriptor"] == 8
				and header["byte_length"] == expected_length
				and header["alpha_range"] == [255, 255]
			)
			if not contract:
				raise RuntimeError(f"Invalid bottom-left 32-bit TGA contract: {tga_path} -> {header}")
			with Image.open(tga_path) as opened:
				decoded = opened.convert("RGBA")
			if ImageChops.difference(png, decoded).getbbox() is not None:
				raise RuntimeError(f"TGA pixels differ from processed PNG: {tga_path}")
			description = file_description(tga_path)
			if "Targa image data" not in description or " - top" in description:
				raise RuntimeError(f"Unexpected file(1) description: {tga_path} -> {description}")
			tier_record["used_rgb_colours"] = len(used_rgb)
			tier_record["tga_header"] = header
			tier_record["file_description"] = description
			tga_hash = sha256(tga_path)
			runtime_tier_hashes[tier].add(tga_hash)
			checksums.append(f"{tga_hash}  {tga_final.relative_to(ROOT).as_posix()}")

	expected_count = len(IDENTITIES) * len(REGIONS)
	if len(raw_hashes) != expected_count:
		raise RuntimeError("The 91 unmodified ImageGen raw sources are not byte-distinct")
	if len(master_hashes) != expected_count:
		raise RuntimeError("The 91 flattened masters are not byte-distinct")
	for tier, hashes in tier_hashes.items():
		if len(hashes) != expected_count:
			raise RuntimeError(f"The 91 regional outputs are not unique at {tier} size")
		if len(runtime_tier_hashes[tier]) != expected_count:
			raise RuntimeError(f"The 91 regional runtime TGAs are not unique at {tier} size")

	processor_path = Path(__file__).resolve()
	result = {
		"date": run_date,
		"status": "candidate_requires_independent_visual_review",
		"approval": {
			"scope": "Event 019 regional flags only",
			"approved_exception": "deterministic spot-colour flattening/normalisation of each independent full-flag ImageGen result",
			"unapproved_fallbacks": "none",
		},
		"matrix": {
			"identity_count": len(IDENTITIES),
			"region_count": len(REGIONS),
			"regional_tag_count": expected_count,
			"runtime_tga_count": expected_count * len(SIZES),
		},
		"processor": {
			"path": processor_path.relative_to(ROOT).as_posix(),
			"sha256": sha256(processor_path),
			"python": sys.version,
			"platform": platform.platform(),
			"pillow": PILLOW_VERSION,
			"numpy": np.__version__,
			"arguments": {
				"maximum_palette_colours": palette_colours,
				"master_width": master_size[0],
				"master_height": master_size[1],
				"hue_bins": hue_bins,
				"neutral_saturation": neutral_saturation,
				"dark_value": dark_value,
				"minimum_colour_share": minimum_colour_share,
				"run_date": run_date,
				"frame_normalisation": "complete-source non-uniform resize; no crop or pad",
				"master_resample": "Pillow LANCZOS before colour-family collapse",
				"normalizer": "deterministic Pillow-HSV hue families with exact normalized-source RGB representatives",
				"dither": "NONE",
				"runtime_resample": "Pillow LANCZOS then nearest recorded spot colour",
			},
			"command": " ".join([Path(sys.executable).as_posix(), "-B", processor_path.relative_to(ROOT).as_posix(), *sys.argv[1:]]),
		},
		"checks": {
			"all_91_rows_link_to_prompt_note_handle_and_existing_built_in_result": True,
			"all_91_raw_sources_are_exact_byte_copies_of_their_built_in_results": True,
			"all_91_raw_sources_are_byte_distinct": True,
			"all_91_spot_masters_are_byte_distinct": True,
			"every_spot_master_uses_only_exact_normalized_source_rgb_representatives": True,
			"every_spot_master_passes_strong_edge_recall": True,
			"all_processed_pngs_use_only_their_recorded_spot_palette": True,
			"all_91_tags_are_unique_at_normal_medium_and_small_sizes": True,
			"all_91_runtime_tgas_are_unique_at_normal_medium_and_small_sizes": True,
			"all_tgas_are_uncompressed_bottom_left_origin_32_bit_with_opaque_alpha": True,
			"all_tgas_decode_pixel_identically_to_processed_pngs": True,
			"file_reports_no_top_origin_markers": True,
		},
		"records": process_records,
	}
	date_token = run_date.replace("-", "_")
	validation_path = staged_path(PACKAGE / f"regional_flag_validation_{date_token}.json", stage_root)
	checksums_path = staged_path(PACKAGE / f"regional_flag_checksums_{date_token}.sha256", stage_root)
	validation_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
	checksums_path.write_text("\n".join(checksums) + "\n", encoding="utf-8")
	return result


def commit_staged_tree(stage_root: Path) -> None:
	staged_files = sorted(path for path in stage_root.rglob("*") if path.is_file())
	if not staged_files:
		raise RuntimeError("Event 019 flag transaction contains no staged artifacts")
	with tempfile.TemporaryDirectory(prefix="event19_regional_flag_backup_") as backup_name:
		backup_root = Path(backup_name)
		existed: set[Path] = set()
		for staged_file in staged_files:
			relative = staged_file.relative_to(stage_root)
			final_path = ROOT / relative
			if final_path.is_file():
				existed.add(relative)
				backup_path = backup_root / relative
				backup_path.parent.mkdir(parents=True, exist_ok=True)
				shutil.copy2(final_path, backup_path)

		committed: list[Path] = []
		try:
			for staged_file in staged_files:
				relative = staged_file.relative_to(stage_root)
				final_path = ROOT / relative
				final_path.parent.mkdir(parents=True, exist_ok=True)
				os.replace(staged_file, final_path)
				committed.append(relative)
		except Exception:
			for relative in reversed(committed):
				final_path = ROOT / relative
				if relative in existed:
					shutil.copy2(backup_root / relative, final_path)
				elif final_path.is_file():
					final_path.unlink()
			raise


def main() -> None:
	args = parse_args()
	if sys.version_info[:3] != REQUIRED_PYTHON:
		raise RuntimeError(f"Required Python runtime is {REQUIRED_PYTHON}, found {sys.version_info[:3]}")
	if PILLOW_VERSION != REQUIRED_PILLOW or np.__version__ != REQUIRED_NUMPY:
		raise RuntimeError(
			f"Required image runtime is Pillow {REQUIRED_PILLOW} / NumPy {REQUIRED_NUMPY}; "
			f"found Pillow {PILLOW_VERSION} / NumPy {np.__version__}"
		)
	if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.run_date):
		raise RuntimeError("--run-date must use the exact YYYY-MM-DD form")
	if args.master_width < 82 or args.master_height < 52:
		raise RuntimeError("Flattened master must be at least the vanilla normal flag size")
	if not 0.0 < args.minimum_colour_share < 0.01:
		raise RuntimeError("--minimum-colour-share must be greater than 0 and less than 0.01")
	provenance = parse_provenance_notes()
	raw_sources = index_raw_sources(provenance)
	master_size = (args.master_width, args.master_height)
	with tempfile.TemporaryDirectory(prefix="event19_regional_flag_stage_") as stage_name:
		stage_root = Path(stage_name)
		ensure_stage_directories(stage_root)
		records = process(
			raw_sources,
			provenance,
			master_size,
			args.palette_colours,
			args.hue_bins,
			args.neutral_saturation,
			args.dark_value,
			args.minimum_colour_share,
			stage_root,
		)
		make_raw_spot_contact_sheet(raw_sources, args.palette_colours, stage_root)
		make_matrix_contact_sheet(stage_root)
		make_small_readability_sheet(stage_root)
		result = validate(
			raw_sources,
			records,
			master_size,
			args.palette_colours,
			args.hue_bins,
			args.neutral_saturation,
			args.dark_value,
			args.minimum_colour_share,
			args.run_date,
			stage_root,
		)
		commit_staged_tree(stage_root)
	print(
		f"validated {result['matrix']['regional_tag_count']} independent full-flag sources, "
		f"{result['matrix']['regional_tag_count']} flattened masters, and "
		f"{result['matrix']['runtime_tga_count']} runtime TGAs"
	)


if __name__ == "__main__":
	main()
