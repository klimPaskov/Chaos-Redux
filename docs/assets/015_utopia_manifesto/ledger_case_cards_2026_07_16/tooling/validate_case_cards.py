#!/usr/bin/env python3
"""Validate Event 015 Necessary Ground case-card package and runtime DDS files."""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import statistics
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


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
TARGET_SIZE = (300, 96)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = next(
	candidate
	for candidate in (PACKAGE_ROOT, *PACKAGE_ROOT.parents)
	if (candidate / "AGENTS.md").is_file()
)
RUNTIME_DIR = REPO_ROOT / "gfx" / "interface" / "015_utopia_manifesto" / "ledger"
GFX_FILE = REPO_ROOT / "interface" / "015_utopia_manifesto.gfx"
GUI_FILE = REPO_ROOT / "interface" / "015_utopia_manifesto_ledger.gui"
METADATA_DIR = PACKAGE_ROOT / "metadata"


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as stream:
		for chunk in iter(lambda: stream.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def require(condition: bool, message: str) -> None:
	if not condition:
		raise RuntimeError(message)


def validate_dds_header(path: Path) -> dict[str, object]:
	data = path.read_bytes()
	width, height = TARGET_SIZE
	require(len(data) == 128 + width * height * 4, f"Unexpected DDS length: {path}")
	require(data[:4] == b"DDS ", f"Missing DDS magic: {path}")
	require(struct.unpack_from("<I", data, 4)[0] == 124, f"Bad DDS header size: {path}")
	require(struct.unpack_from("<I", data, 12)[0] == height, f"Bad DDS height: {path}")
	require(struct.unpack_from("<I", data, 16)[0] == width, f"Bad DDS width: {path}")
	require(struct.unpack_from("<I", data, 20)[0] == width * 4, f"Bad DDS pitch: {path}")
	require(struct.unpack_from("<I", data, 28)[0] == 0, f"DDS has mipmaps: {path}")
	require(not any(struct.unpack_from("<11I", data, 32)), f"DDS reserved words used: {path}")
	require(
		struct.unpack_from("<8I", data, 76)
		== (
			32,
			0x41,
			0,
			32,
			0x00FF0000,
			0x0000FF00,
			0x000000FF,
			0xFF000000,
		),
		f"DDS is not one-level uncompressed BGRA: {path}",
	)
	require(struct.unpack_from("<I", data, 108)[0] == 0x1000, f"Bad DDS caps: {path}")
	alpha = data[131::4]
	require(min(alpha) == 255 and max(alpha) == 255, f"DDS is not fully opaque: {path}")
	return {
		"file_length": len(data),
		"header_bytes": 128,
		"pixel_format": "uncompressed BGRA8",
		"mipmap_count": 0,
		"alpha_min": min(alpha),
		"alpha_max": max(alpha),
	}


def validate_wiring() -> dict[str, object]:
	gfx = GFX_FILE.read_text(encoding="utf-8-sig")
	gui = GUI_FILE.read_text(encoding="utf-8-sig")
	for stem in STEMS:
		sprite = f"GFX_{stem}"
		texture = f"gfx/interface/015_utopia_manifesto/ledger/{stem}.dds"
		require(gfx.count(f'name = "{sprite}"') == 1, f"Missing or duplicate GFX name: {sprite}")
		require(gfx.count(f'texturefile = "{texture}"') == 1, f"Missing or duplicate texture: {texture}")
		block_pattern = re.compile(
			r"iconType\s*=\s*\{(?:(?!iconType\s*=).)*?"
			+ rf'name\s*=\s*"{re.escape(stem)}"'
			+ r"(?:(?!iconType\s*=).)*?"
			+ rf'spriteType\s*=\s*"{re.escape(sprite)}"'
			+ r"(?:(?!iconType\s*=).)*?position\s*=\s*\{\s*x\s*=\s*8\s+y\s*=\s*4\s*\}",
			re.S,
		)
		require(block_pattern.search(gui) is not None, f"GUI block or stable position missing: {stem}")
	return {
		"gfx_file": GFX_FILE.relative_to(REPO_ROOT).as_posix(),
		"gui_file": GUI_FILE.relative_to(REPO_ROOT).as_posix(),
		"sprite_count": len(STEMS),
		"position": [8, 4],
	}


def main() -> int:
	processing = json.loads((METADATA_DIR / "processing_report.json").read_text(encoding="utf-8"))
	provenance = json.loads((METADATA_DIR / "source_handles.json").read_text(encoding="utf-8"))
	records_by_stem = {record["stem"]: record for record in processing["records"]}
	require(tuple(records_by_stem) == STEMS, "Processing record order or membership differs")
	accepted_provenance = [record for record in provenance["records"] if record["status"] == "accepted"]
	rejected_provenance = [record for record in provenance["records"] if record["status"] == "rejected"]
	require(len(accepted_provenance) == 10, "Expected ten accepted ImageGen records")
	require(len(rejected_provenance) == 3, "Expected three rejected ImageGen records")
	require(len({record["handle"] for record in provenance["records"]}) == 13, "Duplicate ImageGen handles")

	accepted_hashes = {
		"source": [],
		"processed": [],
		"runtime": [],
		"rgba_pixels": [],
	}
	images: dict[str, Image.Image] = {}
	asset_records: list[dict[str, object]] = []
	for stem in STEMS:
		record = records_by_stem[stem]
		source = REPO_ROOT / record["source"]
		processed = REPO_ROOT / record["processed_png"]
		runtime = REPO_ROOT / record["runtime_dds"]
		decoded = REPO_ROOT / record["decoded_png"]
		for path in (source, processed, runtime, decoded):
			require(path.is_file(), f"Missing artifact: {path}")

		require(b"c2pa" in source.read_bytes(), f"Accepted source lacks C2PA assertion: {source}")
		require(abs(float(record["aspect_ratio_delta_percent"])) <= 4.001, f"Material aspect mismatch: {stem}")
		require(record["nonuniform_scaling"] is False, f"Nonuniform scaling recorded: {stem}")
		geometry_size = record["geometry_crop_size"]
		geometry_ratio = geometry_size[0] / geometry_size[1]
		require(abs(geometry_ratio - TARGET_RATIO) < 0.002, f"Geometry crop ratio mismatch: {stem}")

		with Image.open(processed) as opened:
			processed_image = opened.convert("RGBA")
		require(processed_image.size == TARGET_SIZE, f"Processed dimensions wrong: {processed}")
		with Image.open(runtime) as opened:
			runtime_image = opened.convert("RGBA")
		require(runtime_image.size == TARGET_SIZE, f"DDS decode dimensions wrong: {runtime}")
		require(runtime_image.tobytes() == processed_image.tobytes(), f"DDS pixels differ: {stem}")
		with Image.open(decoded) as opened:
			decoded_image = opened.convert("RGBA")
		require(decoded_image.tobytes() == processed_image.tobytes(), f"Decoded PNG pixels differ: {stem}")

		rgb = processed_image.convert("RGB")
		quiet = rgb.crop((12, 14, 205, 82)).convert("L")
		right = rgb.crop((225, 8, 296, 88)).convert("L")
		quiet_stats = ImageStat.Stat(quiet)
		right_stats = ImageStat.Stat(right)
		quiet_mean = float(quiet_stats.mean[0])
		quiet_stddev = float(quiet_stats.stddev[0])
		right_stddev = float(right_stats.stddev[0])
		require(quiet_mean <= 35.0, f"Overlay field too bright: {stem}")
		require(quiet_stddev <= 6.0, f"Overlay field too busy: {stem}")
		require(right_stddev >= 15.0, f"Right-state pictogram too weak: {stem}")

		dds = validate_dds_header(runtime)
		accepted_hashes["source"].append(sha256(source))
		accepted_hashes["processed"].append(sha256(processed))
		accepted_hashes["runtime"].append(sha256(runtime))
		accepted_hashes["rgba_pixels"].append(hashlib.sha256(processed_image.tobytes()).hexdigest())
		images[stem] = rgb
		asset_records.append(
			{
				"stem": stem,
				"source_size": record["source_size"],
				"post_matte_size": record["post_crop_size"],
				"post_matte_aspect_ratio": record["source_aspect_ratio"],
				"aspect_ratio_delta_percent": record["aspect_ratio_delta_percent"],
				"geometry_strategy": record["geometry_strategy"],
				"geometry_crop_box": record["geometry_crop_box"],
				"geometry_crop_size": geometry_size,
				"nonuniform_scaling": record["nonuniform_scaling"],
				"quiet_field_luminance_mean": round(quiet_mean, 3),
				"quiet_field_luminance_stddev": round(quiet_stddev, 3),
				"right_pictogram_luminance_stddev": round(right_stddev, 3),
				"source_sha256": sha256(source),
				"processed_sha256": sha256(processed),
				"runtime_sha256": sha256(runtime),
				"decoded_sha256": sha256(decoded),
				"dds": dds,
			}
		)

	for group, hashes in accepted_hashes.items():
		require(len(set(hashes)) == 10, f"Accepted {group} artifacts are not all distinct")

	pairwise: list[tuple[float, str, str]] = []
	for first, second in itertools.combinations(STEMS, 2):
		difference = ImageChops.difference(
			images[first].crop((215, 0, 300, 96)),
			images[second].crop((215, 0, 300, 96)),
		)
		mae = statistics.mean(ImageStat.Stat(difference).mean)
		pairwise.append((float(mae), first, second))
	minimum_mae, minimum_first, minimum_second = min(pairwise)
	require(minimum_mae >= 15.0, "Two right-side state treatments are insufficiently distinct")

	wiring = validate_wiring()
	review_files = [
		*sorted((PACKAGE_ROOT / "contact_sheets").glob("*.png")),
		*sorted((PACKAGE_ROOT / "native_size_review").glob("*.png")),
	]
	require(len(review_files) == 6, f"Expected six review images, found {len(review_files)}")

	binary_files = [
		*sorted((PACKAGE_ROOT / "sources").glob("*.png")),
		*sorted((PACKAGE_ROOT / "sources" / "rejected").glob("*.png")),
		*sorted((PACKAGE_ROOT / "processed_png").glob("*.png")),
		*sorted((PACKAGE_ROOT / "decoded_png").glob("*.png")),
		*sorted(RUNTIME_DIR.glob("utopia_ledger_case_*.dds")),
		*review_files,
	]
	checksum_lines = [f"{sha256(path)}  {path.relative_to(REPO_ROOT).as_posix()}" for path in binary_files]
	(METADATA_DIR / "binary_checksums.sha256").write_text(
		"\n".join(checksum_lines) + "\n",
		encoding="utf-8",
	)

	validation = {
		"package": "Event 015 Necessary Ground case cards",
		"status": "pass",
		"accepted_count": 10,
		"rejected_count": 3,
		"target_size": list(TARGET_SIZE),
		"accepted_source_hashes_distinct": True,
		"processed_hashes_distinct": True,
		"runtime_hashes_distinct": True,
		"decoded_pixels_match_processed": True,
		"all_sources_have_c2pa_assertion": True,
		"all_geometry_uses_uniform_scaling": True,
		"maximum_absolute_post_matte_ratio_delta_percent": max(
			abs(float(record["aspect_ratio_delta_percent"])) for record in processing["records"]
		),
		"right_region_pairwise_minimum_mae": round(minimum_mae, 3),
		"closest_right_region_pair": [minimum_first, minimum_second],
		"overlay_safe_field_thresholds": {
			"luminance_mean_max": 35.0,
			"luminance_stddev_max": 6.0,
			"right_pictogram_stddev_min": 15.0,
		},
		"runtime_wiring": wiring,
		"review_image_count": len(review_files),
		"asset_records": asset_records,
	}
	(METADATA_DIR / "validation_report.json").write_text(
		json.dumps(validation, indent=2),
		encoding="utf-8",
	)
	print(METADATA_DIR / "validation_report.json")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
