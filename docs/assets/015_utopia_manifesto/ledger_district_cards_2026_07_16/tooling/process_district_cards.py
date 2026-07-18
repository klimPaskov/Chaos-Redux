#!/usr/bin/env python3
"""Process Event 015 Ledger District card masters without drawing visible art.

Allowed operations in this pipeline are limited to content-safe cropping,
restrained colour grading, chroma keying, aspect-preserving resizing, transparent
padding for keyed overlays, PNG export, and one-level BGRA DDS export/decoding.
The role scenes, badge frames, papers, seals, buildings, instruments, and all
other visible artwork come from the retained built-in ImageGen masters.
"""

from __future__ import annotations

import hashlib
import json
import math
import struct
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance


ROLE_STEMS = (
	"utopia_ledger_district_role_market_garden",
	"utopia_ledger_district_role_industrial_housing",
	"utopia_ledger_district_role_rail_junction",
	"utopia_ledger_district_role_port_town",
	"utopia_ledger_district_role_research_town",
	"utopia_ledger_district_role_refugee_municipality",
	"utopia_ledger_district_role_inland_island_ring",
)

STATE_STEMS = (
	"utopia_ledger_district_state_surveyed",
	"utopia_ledger_district_state_planned",
	"utopia_ledger_district_state_building",
	"utopia_ledger_district_state_blocked",
	"utopia_ledger_district_state_complete",
	"utopia_ledger_district_state_disputed",
)

ROLE_SIZE = (300, 96)
STATE_SIZE = (48, 48)
STATE_INNER_SIZE = (44, 44)

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def find_repo_root(start: Path) -> Path:
	for candidate in (start, *start.parents):
		if (candidate / "AGENTS.md").is_file():
			return candidate
	raise RuntimeError("Could not locate repository root from processing script")


REPO_ROOT = find_repo_root(PACKAGE_ROOT)
RUNTIME_ROOT = REPO_ROOT / "gfx/interface/015_utopia_manifesto/ledger"


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def aspect_preserving_cover_crop(
	image: Image.Image,
	target_size: tuple[int, int],
) -> tuple[Image.Image, dict[str, object]]:
	"""Crop minimally to target aspect ratio; never rescale axes separately."""
	source_width, source_height = image.size
	target_width, target_height = target_size
	source_ratio = source_width / source_height
	target_ratio = target_width / target_height

	# Use the largest exact integer rectangle with the reduced target ratio.
	# This avoids even sub-pixel aspect drift and makes nonuniform stretch
	# mathematically impossible. For 300x96 the reduced ratio is 25x8.
	common_divisor = math.gcd(target_width, target_height)
	ratio_width = target_width // common_divisor
	ratio_height = target_height // common_divisor
	scale_units = min(source_width // ratio_width, source_height // ratio_height)
	if scale_units < 1:
		raise RuntimeError(f"Source {image.size} is too small for target ratio {target_size}")
	crop_width = ratio_width * scale_units
	crop_height = ratio_height * scale_units
	left = (source_width - crop_width) // 2
	top = (source_height - crop_height) // 2
	box = (left, top, left + crop_width, top + crop_height)

	cropped = image.crop(box)
	crop_width, crop_height = cropped.size
	if abs((crop_width / crop_height) - target_ratio) > 1e-9:
		raise RuntimeError(f"Crop ratio mismatch: {cropped.size} -> {target_size}")

	resized = cropped.resize(target_size, Image.Resampling.LANCZOS)
	metadata = {
		"fit_mode": "centered_aspect_preserving_cover_crop",
		"source_size": [source_width, source_height],
		"source_aspect_ratio": source_ratio,
		"target_size": list(target_size),
		"target_aspect_ratio": target_ratio,
		"crop_box": list(box),
		"crop_size": [crop_width, crop_height],
		"crop_aspect_ratio": crop_width / crop_height,
		"retained_source_area_fraction": (crop_width * crop_height) / (source_width * source_height),
		"uniform_scale": target_width / crop_width,
		"nonuniform_stretch": False,
		"content_safety_note": "Minimal centered trim preserves the full focal district and generated frame geometry.",
	}
	return resized, metadata


def grade_role(image: Image.Image) -> Image.Image:
	"""Restrained grade only; no compositing, masks, shapes, frames, or overlays."""
	graded = ImageEnhance.Color(image.convert("RGB")).enhance(0.94)
	graded = ImageEnhance.Contrast(graded).enhance(1.04)
	graded = ImageEnhance.Sharpness(graded).enhance(1.08)
	return graded.convert("RGBA")


def sample_key_color(image: Image.Image, patch: int = 12) -> np.ndarray:
	rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
	patches = np.concatenate(
		(
			rgb[:patch, :patch].reshape(-1, 3),
			rgb[:patch, -patch:].reshape(-1, 3),
			rgb[-patch:, :patch].reshape(-1, 3),
			rgb[-patch:, -patch:].reshape(-1, 3),
		),
		axis=0,
	)
	return np.median(patches, axis=0)


def chroma_key(image: Image.Image) -> tuple[Image.Image, dict[str, object]]:
	"""Mechanically key the flat ImageGen magenta and recover antialiased edges."""
	rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
	key = sample_key_color(image)
	if np.linalg.norm(key - np.array([255.0, 0.0, 255.0], dtype=np.float32)) > 30.0:
		raise RuntimeError(f"Unexpected chroma key colour: {key.tolist()}")

	distance = np.linalg.norm(rgb - key, axis=2)
	transparent_distance = 22.0
	opaque_distance = 122.0
	alpha = np.clip(
		(distance - transparent_distance) / (opaque_distance - transparent_distance),
		0.0,
		1.0,
	)

	# Reverse the flat-key contribution for partially covered edge pixels. This
	# is colour recovery only and does not invent or draw visible edge artwork.
	recovered = rgb.copy()
	partial = (alpha > 0.02) & (alpha < 0.999)
	for channel in range(3):
		channel_data = recovered[:, :, channel]
		channel_data[partial] = (
			channel_data[partial] - (1.0 - alpha[partial]) * key[channel]
		) / alpha[partial]
		recovered[:, :, channel] = channel_data
	recovered = np.clip(recovered, 0.0, 255.0)
	recovered[alpha <= 0.02] = 0.0

	rgba = np.dstack((recovered, np.rint(alpha * 255.0))).astype(np.uint8)
	keyed = Image.fromarray(rgba, mode="RGBA")
	key_metadata = {
		"sampled_key_rgb": [round(float(value), 3) for value in key],
		"transparent_distance": transparent_distance,
		"opaque_distance": opaque_distance,
		"alpha_min": int(rgba[:, :, 3].min()),
		"alpha_max": int(rgba[:, :, 3].max()),
		"key_operation": "flat-magenta distance matte plus edge-colour recovery",
	}
	return keyed, key_metadata


def aspect_preserving_alpha_contain(
	image: Image.Image,
	target_size: tuple[int, int],
	inner_size: tuple[int, int],
) -> tuple[Image.Image, dict[str, object]]:
	"""Contain keyed content proportionally and pad only with transparency."""
	alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
	y_positions, x_positions = np.where(alpha > 8)
	if not len(x_positions):
		raise RuntimeError("Chroma key produced no visible subject")

	left = int(x_positions.min())
	top = int(y_positions.min())
	right = int(x_positions.max()) + 1
	bottom = int(y_positions.max()) + 1
	bbox = (left, top, right, bottom)
	cropped = image.crop(bbox)
	crop_width, crop_height = cropped.size
	inner_width, inner_height = inner_size
	scale = min(inner_width / crop_width, inner_height / crop_height)
	resized_width = max(1, round(crop_width * scale))
	resized_height = max(1, round(crop_height * scale))
	resized = cropped.resize((resized_width, resized_height), Image.Resampling.LANCZOS)

	target_width, target_height = target_size
	offset_x = (target_width - resized_width) // 2
	offset_y = (target_height - resized_height) // 2
	canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
	canvas.alpha_composite(resized, dest=(offset_x, offset_y))
	# Resampling may create a handful of sub-3%-opacity key-colour pixels.
	# Clearing those mechanically prevents a visible magenta fringe at 48x48.
	canvas_rgba = np.asarray(canvas, dtype=np.uint8).copy()
	near_transparent = canvas_rgba[:, :, 3] <= 8
	canvas_rgba[near_transparent] = 0
	canvas = Image.fromarray(canvas_rgba, mode="RGBA")

	metadata = {
		"fit_mode": "alpha_bbox_aspect_preserving_contain_with_transparent_padding",
		"source_size": list(image.size),
		"source_aspect_ratio": image.width / image.height,
		"alpha_content_bbox": list(bbox),
		"alpha_content_size": [crop_width, crop_height],
		"alpha_content_aspect_ratio": crop_width / crop_height,
		"target_size": list(target_size),
		"inner_limit": list(inner_size),
		"uniform_scale": scale,
		"scaled_content_size": [resized_width, resized_height],
		"transparent_offset": [offset_x, offset_y],
		"nonuniform_stretch": False,
		"content_safety_note": "The complete keyed emblem is contained; only transparent pixels are added around it.",
	}
	return canvas, metadata


def write_bgra_dds(image: Image.Image, output_path: Path) -> None:
	"""Write a legacy, one-level, uncompressed 32-bit BGRA DDS."""
	rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
	height, width = rgba.shape[:2]
	pitch = width * 4

	header = b"".join(
		(
			struct.pack("<7I", 124, 0x100F, height, width, pitch, 0, 0),
			struct.pack("<11I", *([0] * 11)),
			struct.pack(
				"<8I",
				32,
				0x41,
				0,
				32,
				0x00FF0000,
				0x0000FF00,
				0x000000FF,
				0xFF000000,
			),
			struct.pack("<5I", 0x1000, 0, 0, 0, 0),
		)
	)
	if len(header) != 124:
		raise RuntimeError(f"Malformed DDS header length: {len(header)}")

	bgra = rgba[:, :, [2, 1, 0, 3]].tobytes(order="C")
	output_path.parent.mkdir(parents=True, exist_ok=True)
	output_path.write_bytes(b"DDS " + header + bgra)
	expected_length = 128 + width * height * 4
	if output_path.stat().st_size != expected_length:
		raise RuntimeError(f"Unexpected DDS length for {output_path}: expected {expected_length}")


def decode_bgra_dds(input_path: Path) -> tuple[Image.Image, dict[str, int]]:
	data = input_path.read_bytes()
	if data[:4] != b"DDS ":
		raise RuntimeError(f"Missing DDS magic in {input_path}")
	fields = {
		"header_size": struct.unpack_from("<I", data, 4)[0],
		"flags": struct.unpack_from("<I", data, 8)[0],
		"height": struct.unpack_from("<I", data, 12)[0],
		"width": struct.unpack_from("<I", data, 16)[0],
		"pitch": struct.unpack_from("<I", data, 20)[0],
		"pixel_format_size": struct.unpack_from("<I", data, 76)[0],
		"pixel_format_flags": struct.unpack_from("<I", data, 80)[0],
		"fourcc": struct.unpack_from("<I", data, 84)[0],
		"bit_count": struct.unpack_from("<I", data, 88)[0],
		"red_mask": struct.unpack_from("<I", data, 92)[0],
		"green_mask": struct.unpack_from("<I", data, 96)[0],
		"blue_mask": struct.unpack_from("<I", data, 100)[0],
		"alpha_mask": struct.unpack_from("<I", data, 104)[0],
		"caps": struct.unpack_from("<I", data, 108)[0],
	}
	expected = {
		"header_size": 124,
		"pixel_format_size": 32,
		"pixel_format_flags": 0x41,
		"fourcc": 0,
		"bit_count": 32,
		"red_mask": 0x00FF0000,
		"green_mask": 0x0000FF00,
		"blue_mask": 0x000000FF,
		"alpha_mask": 0xFF000000,
		"caps": 0x1000,
	}
	for key, expected_value in expected.items():
		if fields[key] != expected_value:
			raise RuntimeError(f"Malformed {key} in {input_path}: {fields[key]:#x}")
	if fields["pitch"] != fields["width"] * 4:
		raise RuntimeError(f"Malformed pitch in {input_path}")
	if len(data) != 128 + fields["width"] * fields["height"] * 4:
		raise RuntimeError(f"Malformed byte length in {input_path}")

	bgra = np.frombuffer(data, dtype=np.uint8, offset=128).reshape(
		(fields["height"], fields["width"], 4)
	)
	rgba = bgra[:, :, [2, 1, 0, 3]].copy()
	return Image.fromarray(rgba, mode="RGBA"), fields


def process_role(stem: str) -> dict[str, object]:
	source = PACKAGE_ROOT / f"source_png/roles/{stem}_source.png"
	processed = PACKAGE_ROOT / f"processed_png/roles/{stem}.png"
	runtime = RUNTIME_ROOT / f"{stem}.dds"
	decoded = PACKAGE_ROOT / f"decoded_png/roles/{stem}.png"

	master = Image.open(source).convert("RGBA")
	resized, fit = aspect_preserving_cover_crop(master, ROLE_SIZE)
	final = grade_role(resized)
	processed.parent.mkdir(parents=True, exist_ok=True)
	final.save(processed, format="PNG", optimize=True)
	write_bgra_dds(final, runtime)
	decoded_image, dds_header = decode_bgra_dds(runtime)
	decoded.parent.mkdir(parents=True, exist_ok=True)
	decoded_image.save(decoded, format="PNG", optimize=True)
	pixel_match = np.array_equal(np.asarray(final), np.asarray(decoded_image))
	if not pixel_match:
		raise RuntimeError(f"Decoded DDS differs from processed PNG for {stem}")

	return {
		"stem": stem,
		"family": "role",
		"source": source.relative_to(REPO_ROOT).as_posix(),
		"processed": processed.relative_to(REPO_ROOT).as_posix(),
		"runtime_dds": runtime.relative_to(REPO_ROOT).as_posix(),
		"decoded": decoded.relative_to(REPO_ROOT).as_posix(),
		"fit": fit,
		"grade": {"color": 0.94, "contrast": 1.04, "sharpness": 1.08},
		"alpha_range": [int(np.asarray(final)[:, :, 3].min()), int(np.asarray(final)[:, :, 3].max())],
		"dds_header": dds_header,
		"decoded_pixel_match": pixel_match,
		"sha256": {
			"source": sha256(source),
			"processed": sha256(processed),
			"runtime_dds": sha256(runtime),
			"decoded": sha256(decoded),
		},
	}


def process_state(stem: str) -> dict[str, object]:
	source = PACKAGE_ROOT / f"source_png/states/{stem}_source.png"
	processed = PACKAGE_ROOT / f"processed_png/states/{stem}.png"
	runtime = RUNTIME_ROOT / f"{stem}.dds"
	decoded = PACKAGE_ROOT / f"decoded_png/states/{stem}.png"

	master = Image.open(source).convert("RGBA")
	keyed, key_metadata = chroma_key(master)
	final, fit = aspect_preserving_alpha_contain(keyed, STATE_SIZE, STATE_INNER_SIZE)
	processed.parent.mkdir(parents=True, exist_ok=True)
	final.save(processed, format="PNG", optimize=True)
	write_bgra_dds(final, runtime)
	decoded_image, dds_header = decode_bgra_dds(runtime)
	decoded.parent.mkdir(parents=True, exist_ok=True)
	decoded_image.save(decoded, format="PNG", optimize=True)
	pixel_match = np.array_equal(np.asarray(final), np.asarray(decoded_image))
	if not pixel_match:
		raise RuntimeError(f"Decoded DDS differs from processed PNG for {stem}")

	alpha = np.asarray(final)[:, :, 3]
	return {
		"stem": stem,
		"family": "state",
		"source": source.relative_to(REPO_ROOT).as_posix(),
		"processed": processed.relative_to(REPO_ROOT).as_posix(),
		"runtime_dds": runtime.relative_to(REPO_ROOT).as_posix(),
		"decoded": decoded.relative_to(REPO_ROOT).as_posix(),
		"key": key_metadata,
		"fit": fit,
		"alpha_range": [int(alpha.min()), int(alpha.max())],
		"visible_pixel_fraction": float(np.count_nonzero(alpha > 8) / alpha.size),
		"corner_alpha": [int(alpha[0, 0]), int(alpha[0, -1]), int(alpha[-1, 0]), int(alpha[-1, -1])],
		"dds_header": dds_header,
		"decoded_pixel_match": pixel_match,
		"sha256": {
			"source": sha256(source),
			"processed": sha256(processed),
			"runtime_dds": sha256(runtime),
			"decoded": sha256(decoded),
		},
	}


def main() -> None:
	RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)
	records = [process_role(stem) for stem in ROLE_STEMS]
	records.extend(process_state(stem) for stem in STATE_STEMS)
	report = {
		"schema_version": 1,
		"processor": Path(__file__).relative_to(REPO_ROOT).as_posix(),
		"visible_art_policy": "No visible art is drawn locally; only crop, grade, key, aspect-preserving resize, transparent pad, and export operations are used.",
		"role_target": list(ROLE_SIZE),
		"state_target": list(STATE_SIZE),
		"state_inner_limit": list(STATE_INNER_SIZE),
		"records": records,
	}
	report_path = PACKAGE_ROOT / "metadata/processing_report.json"
	report_path.parent.mkdir(parents=True, exist_ok=True)
	report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
	print(f"Processed {len(ROLE_STEMS)} role cards and {len(STATE_STEMS)} state badges")
	print(report_path.relative_to(REPO_ROOT).as_posix())


if __name__ == "__main__":
	main()
