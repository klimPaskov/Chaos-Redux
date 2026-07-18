#!/usr/bin/env python3
"""Finish Event 015 Necessary Ground case-card masters.

This processor is deliberately mechanical. It may trim external matte,
make a content-safe aspect crop, apply one restrained family-wide grade,
uniformly resize, export PNG/DDS, and decode the DDS for verification. It
does not draw, trace, reconstruct, composite, or otherwise author visible
game art.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageOps


TARGET_SIZE = (300, 96)
STEMS = (
	"utopia_ledger_case_no_target",
	"utopia_ledger_case_target_eligible",
	"utopia_ledger_case_target_selected",
	"utopia_ledger_case_offer_pending",
	"utopia_ledger_case_counteroffer",
	"utopia_ledger_case_refusal",
	"utopia_ledger_case_ultimatum_available",
	"utopia_ledger_case_expired",
	"utopia_ledger_case_stewardship_active",
	"utopia_ledger_case_associate_established",
)

DDSD_CAPS = 0x1
DDSD_HEIGHT = 0x2
DDSD_WIDTH = 0x4
DDSD_PITCH = 0x8
DDSD_PIXELFORMAT = 0x1000
DDPF_ALPHAPIXELS = 0x1
DDPF_RGB = 0x40
DDSCAPS_TEXTURE = 0x1000


def find_repo_root(start: Path) -> Path:
	for candidate in (start, *start.parents):
		if (candidate / "AGENTS.md").is_file() and (candidate / "gfx").is_dir():
			return candidate
	raise RuntimeError("Could not locate the Chaos Redux repository root")


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = find_repo_root(PACKAGE_ROOT)
SOURCE_DIR = PACKAGE_ROOT / "sources"
PROCESSED_DIR = PACKAGE_ROOT / "processed_png"
DECODED_DIR = PACKAGE_ROOT / "decoded_png"
METADATA_DIR = PACKAGE_ROOT / "metadata"
RUNTIME_DIR = REPO_ROOT / "gfx" / "interface" / "015_utopia_manifesto" / "ledger"


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as stream:
		for chunk in iter(lambda: stream.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def trim_external_white_matte(image: Image.Image) -> tuple[Image.Image, tuple[int, int, int, int]]:
	"""Trim only a near-white external matte, never interior card artwork."""
	rgba = image.convert("RGBA")
	rgb = rgba.convert("RGB")
	white = Image.new("RGB", rgb.size, (255, 255, 255))
	difference = ImageChops.difference(rgb, white).convert("L")
	content_mask = difference.point(lambda value: 255 if value > 12 else 0)
	bbox = content_mask.getbbox()
	if bbox is None:
		raise RuntimeError("Source appears to contain only a white matte")

	left, top, right, bottom = bbox
	left = max(0, left - 2)
	top = max(0, top - 2)
	right = min(rgba.width, right + 2)
	bottom = min(rgba.height, bottom + 2)
	trim_box = (left, top, right, bottom)

	# A generated card must occupy most of its source. This guard prevents an
	# interior light field from being mistaken for removable canvas.
	trimmed_area = (right - left) * (bottom - top)
	if trimmed_area < rgba.width * rgba.height * 0.55:
		trim_box = (0, 0, rgba.width, rgba.height)

	return rgba.crop(trim_box), trim_box


def geometry_preserving_cover_crop(
	image: Image.Image,
) -> tuple[Image.Image, tuple[int, int, int, int], dict[str, object]]:
	"""Crop to the runtime ratio before a single uniform resize.

	Every accepted master keeps its state emblem on the right and its quiet
	copy field on the left/centre. The crop therefore stays centred: the
	small crops only remove redundant outer-frame height, while the two tall
	masters retain their complete dossier/hourglass/gavel pictograms. No
	pixels are stretched independently along either axis.
	"""
	width, height = image.size
	target_ratio = TARGET_SIZE[0] / TARGET_SIZE[1]
	source_ratio = width / height
	if abs(source_ratio - target_ratio) < 1e-9:
		crop_box = (0, 0, width, height)
		axis = "none"
	elif source_ratio < target_ratio:
		crop_height = min(height, round(width / target_ratio))
		top = (height - crop_height) // 2
		crop_box = (0, top, width, top + crop_height)
		axis = "vertical"
	else:
		crop_width = min(width, round(height * target_ratio))
		left = (width - crop_width) // 2
		crop_box = (left, 0, left + crop_width, height)
		axis = "horizontal"

	cropped = image.crop(crop_box)
	post_ratio = cropped.width / cropped.height
	return cropped, crop_box, {
		"source_aspect_ratio": round(source_ratio, 6),
		"target_aspect_ratio": round(target_ratio, 6),
		"aspect_ratio_delta_percent": round(
			(source_ratio / target_ratio - 1.0) * 100.0,
			3,
		),
		"geometry_strategy": "content_safe_center_cover_crop_then_uniform_lanczos",
		"geometry_crop_axis": axis,
		"geometry_crop_box": list(crop_box),
		"geometry_crop_size": list(cropped.size),
		"geometry_crop_aspect_ratio": round(post_ratio, 6),
		"geometry_focus": "centered; complete right-side state pictogram retained",
		"nonuniform_scaling": False,
	}


def finish_master(source: Path) -> tuple[Image.Image, dict[str, object]]:
	with Image.open(source) as opened:
		opened = ImageOps.exif_transpose(opened)
		source_size = opened.size
		trimmed, crop_box = trim_external_white_matte(opened)
		geometry_cropped, _, geometry_details = geometry_preserving_cover_crop(
			trimmed
		)

	alpha = geometry_cropped.getchannel("A")
	rgb = geometry_cropped.convert("RGB")
	rgb = ImageEnhance.Color(rgb).enhance(0.96)
	rgb = ImageEnhance.Contrast(rgb).enhance(1.035)
	rgb = ImageEnhance.Brightness(rgb).enhance(0.985)
	graded = rgb.convert("RGBA")
	graded.putalpha(alpha)

	# The cover crop already has the target ratio, so this is a uniform scale.
	resized = graded.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
	resized = ImageEnhance.Sharpness(resized).enhance(1.10)

	return resized, {
		"source_size": list(source_size),
		"external_matte_crop_box": list(crop_box),
		"post_crop_size": list(trimmed.size),
		**geometry_details,
		"resize_mode": "uniform_lanczos_after_content_safe_cover_crop",
		"family_grade": {
			"color": 0.96,
			"contrast": 1.035,
			"brightness": 0.985,
			"post_resize_sharpness": 1.10,
		},
	}


def write_bgra_dds(output_path: Path, image: Image.Image) -> None:
	"""Mirror the event-assets skill's convert_to_dds.py legacy one-level BGRA layout."""
	rgba = image.convert("RGBA")
	width, height = rgba.size
	bgra_data = rgba.tobytes("raw", "BGRA")
	expected_size = width * height * 4
	if len(bgra_data) != expected_size:
		raise RuntimeError(
			f"Unexpected BGRA size for {output_path}: "
			f"{len(bgra_data)} != {expected_size}"
		)

	header = struct.pack(
		"<4s31I",
		b"DDS ",
		124,
		DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT | DDSD_PITCH,
		height,
		width,
		width * 4,
		0,
		0,
		*([0] * 11),
		32,
		DDPF_RGB | DDPF_ALPHAPIXELS,
		0,
		32,
		0x00FF0000,
		0x0000FF00,
		0x000000FF,
		0xFF000000,
		DDSCAPS_TEXTURE,
		0,
		0,
		0,
		0,
	)
	if len(header) != 128:
		raise RuntimeError(f"Unexpected DDS header length: {len(header)}")
	output_path.write_bytes(header + bgra_data)


def inspect_dds(path: Path) -> dict[str, object]:
	data = path.read_bytes()
	width, height = TARGET_SIZE
	expected_length = 128 + width * height * 4
	if len(data) != expected_length:
		raise RuntimeError(f"Unexpected DDS length for {path}: {len(data)}")
	if data[:4] != b"DDS ":
		raise RuntimeError(f"Missing DDS magic: {path}")
	if struct.unpack_from("<I", data, 4)[0] != 124:
		raise RuntimeError(f"Wrong DDS_HEADER size: {path}")
	if struct.unpack_from("<I", data, 12)[0] != height:
		raise RuntimeError(f"Wrong DDS height: {path}")
	if struct.unpack_from("<I", data, 16)[0] != width:
		raise RuntimeError(f"Wrong DDS width: {path}")
	if struct.unpack_from("<I", data, 20)[0] != width * 4:
		raise RuntimeError(f"Wrong DDS pitch: {path}")
	if struct.unpack_from("<I", data, 28)[0] != 0:
		raise RuntimeError(f"Unexpected mipmap count: {path}")
	if any(struct.unpack_from("<11I", data, 32)):
		raise RuntimeError(f"Reserved DDS dwords are not zero: {path}")

	pixel_format = struct.unpack_from("<8I", data, 76)
	expected_pixel_format = (
		32,
		DDPF_RGB | DDPF_ALPHAPIXELS,
		0,
		32,
		0x00FF0000,
		0x0000FF00,
		0x000000FF,
		0xFF000000,
	)
	if pixel_format != expected_pixel_format:
		raise RuntimeError(f"Malformed BGRA pixel-format block: {path}")
	if struct.unpack_from("<I", data, 108)[0] != DDSCAPS_TEXTURE:
		raise RuntimeError(f"Missing DDSCAPS_TEXTURE: {path}")

	alpha_bytes = data[128 + 3 :: 4]
	return {
		"magic": "DDS ",
		"header_size": 124,
		"total_header_bytes": 128,
		"width": width,
		"height": height,
		"pitch": width * 4,
		"pixel_format_offset": 76,
		"pixel_format_size": 32,
		"pixel_format_flags": DDPF_RGB | DDPF_ALPHAPIXELS,
		"four_cc": 0,
		"bit_count": 32,
		"masks": [
			"0x00FF0000",
			"0x0000FF00",
			"0x000000FF",
			"0xFF000000",
		],
		"caps": "0x00001000",
		"mipmap_count": 0,
		"file_length": len(data),
		"expected_file_length": expected_length,
		"alpha_min": min(alpha_bytes),
		"alpha_max": max(alpha_bytes),
	}


def main() -> int:
	for directory in (PROCESSED_DIR, DECODED_DIR, METADATA_DIR, RUNTIME_DIR):
		directory.mkdir(parents=True, exist_ok=True)

	records: list[dict[str, object]] = []
	for stem in STEMS:
		source = SOURCE_DIR / f"{stem}_source.png"
		processed = PROCESSED_DIR / f"{stem}.png"
		runtime = RUNTIME_DIR / f"{stem}.dds"
		decoded = DECODED_DIR / f"{stem}.png"
		if not source.is_file():
			raise FileNotFoundError(source)

		finished, details = finish_master(source)
		finished.save(processed, format="PNG", optimize=True, compress_level=9)
		write_bgra_dds(runtime, finished)

		with Image.open(runtime) as opened_dds:
			decoded_image = opened_dds.convert("RGBA")
		if decoded_image.size != TARGET_SIZE:
			raise RuntimeError(f"Decoded DDS has wrong size: {runtime}")
		if decoded_image.tobytes() != finished.convert("RGBA").tobytes():
			raise RuntimeError(f"Decoded DDS pixels differ from processed PNG: {runtime}")
		decoded_image.save(decoded, format="PNG", optimize=True, compress_level=9)

		records.append(
			{
				"stem": stem,
				"source": source.relative_to(REPO_ROOT).as_posix(),
				"processed_png": processed.relative_to(REPO_ROOT).as_posix(),
				"runtime_dds": runtime.relative_to(REPO_ROOT).as_posix(),
				"decoded_png": decoded.relative_to(REPO_ROOT).as_posix(),
				"target_size": list(TARGET_SIZE),
				**details,
				"source_sha256": sha256(source),
				"processed_sha256": sha256(processed),
				"runtime_sha256": sha256(runtime),
				"decoded_sha256": sha256(decoded),
				"rgba_pixel_sha256": hashlib.sha256(decoded_image.tobytes()).hexdigest(),
				"dds": inspect_dds(runtime),
			}
		)

	report_path = METADATA_DIR / "processing_report.json"
	report_path.write_text(
		json.dumps(
			{
				"package": "Event 015 Necessary Ground case cards",
				"processor_scope": [
					"external-matte crop",
					"content-safe aspect-ratio crop",
					"family-wide restrained colour grade",
					"uniform resize",
					"PNG export",
					"legacy one-level BGRA DDS export",
					"DDS decode verification",
				],
				"processor_does_not": [
					"draw visible art",
					"trace visible art",
					"reconstruct visible art",
					"composite unrelated icons",
					"author state symbols or borders",
				],
				"records": records,
			},
			indent=2,
		),
		encoding="utf-8",
	)
	print(report_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
