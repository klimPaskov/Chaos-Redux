#!/usr/bin/env python3
"""Validate and build review-only contact sheets for Ledger District assets.

This script never alters source, processed, decoded, or runtime art. Its drawn
labels, checkerboards, and review backgrounds exist only in contact sheets.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import struct
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


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

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def find_repo_root(start: Path) -> Path:
	for candidate in (start, *start.parents):
		if (candidate / "AGENTS.md").is_file():
			return candidate
	raise RuntimeError("Could not locate repository root")


REPO_ROOT = find_repo_root(PACKAGE_ROOT)
RUNTIME_ROOT = REPO_ROOT / "gfx/interface/015_utopia_manifesto/ledger"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
VALIDATION_ROOT = PACKAGE_ROOT / "validation"
FONT = ImageFont.load_default()


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def short_label(stem: str) -> str:
	return re.sub(r"^utopia_ledger_district_(?:role|state)_", "", stem).replace("_", " ")


def checkerboard(size: tuple[int, int], cell: int = 6) -> Image.Image:
	width, height = size
	y, x = np.indices((height, width))
	pattern = ((x // cell) + (y // cell)) % 2
	array = np.empty((height, width, 4), dtype=np.uint8)
	array[pattern == 0] = (51, 54, 51, 255)
	array[pattern == 1] = (86, 89, 86, 255)
	return Image.fromarray(array, mode="RGBA")


def on_checker(image: Image.Image, cell: int = 6) -> Image.Image:
	background = checkerboard(image.size, cell)
	background.alpha_composite(image.convert("RGBA"))
	return background.convert("RGB")


def uniform_thumbnail(image: Image.Image, limit: tuple[int, int]) -> Image.Image:
	copy = image.copy()
	copy.thumbnail(limit, Image.Resampling.LANCZOS)
	return copy


def make_role_source_runtime_contact() -> Path:
	row_height = 146
	canvas = Image.new("RGB", (750, 34 + row_height * len(ROLE_STEMS)), (21, 24, 22))
	draw = ImageDraw.Draw(canvas)
	draw.text((12, 10), "Event 015 Ledger District roles: independent source masters and 300x96 finals", fill=(235, 228, 205), font=FONT)
	for index, stem in enumerate(ROLE_STEMS):
		y = 34 + index * row_height
		draw.text((12, y + 4), short_label(stem), fill=(224, 212, 177), font=FONT)
		source = Image.open(PACKAGE_ROOT / f"source_png/roles/{stem}_source.png").convert("RGB")
		processed = Image.open(PACKAGE_ROOT / f"processed_png/roles/{stem}.png").convert("RGB")
		source_thumb = uniform_thumbnail(source, (390, 112))
		canvas.paste(source_thumb, (12, y + 24))
		canvas.paste(processed, (438, y + 24))
		draw.text((12, y + 132), "source master (uniform review scale)", fill=(151, 158, 150), font=FONT)
		draw.text((438, y + 124), "runtime PNG 300x96", fill=(151, 158, 150), font=FONT)
	path = CONTACT_ROOT / "district_roles_source_runtime_contact.png"
	canvas.save(path, optimize=True)
	return path


def make_state_source_runtime_contact() -> Path:
	row_height = 224
	canvas = Image.new("RGB", (720, 34 + row_height * len(STATE_STEMS)), (21, 24, 22))
	draw = ImageDraw.Draw(canvas)
	draw.text((12, 10), "Event 015 Ledger District states: independent source masters, native, and 4x review", fill=(235, 228, 205), font=FONT)
	for index, stem in enumerate(STATE_STEMS):
		y = 34 + index * row_height
		draw.text((12, y + 4), short_label(stem), fill=(224, 212, 177), font=FONT)
		source = Image.open(PACKAGE_ROOT / f"source_png/states/{stem}_source.png").convert("RGB")
		processed = Image.open(PACKAGE_ROOT / f"processed_png/states/{stem}.png").convert("RGBA")
		source_thumb = uniform_thumbnail(source, (190, 190))
		canvas.paste(source_thumb, (12, y + 24))
		native = on_checker(processed)
		canvas.paste(native, (252, y + 80))
		enlarged = on_checker(processed).resize((192, 192), Image.Resampling.NEAREST)
		canvas.paste(enlarged, (408, y + 24))
		draw.text((12, y + 212), "source master (uniform review scale)", fill=(151, 158, 150), font=FONT)
		draw.text((238, y + 136), "native 48x48", fill=(151, 158, 150), font=FONT)
		draw.text((408, y + 212), "nearest-neighbour 4x", fill=(151, 158, 150), font=FONT)
	path = CONTACT_ROOT / "district_states_source_runtime_contact.png"
	canvas.save(path, optimize=True)
	return path


def make_role_native_contact() -> Path:
	cell_width = 320
	cell_height = 126
	canvas = Image.new("RGB", (cell_width * 2, cell_height * 4 + 28), (21, 24, 22))
	draw = ImageDraw.Draw(canvas)
	draw.text((10, 8), "Native 1:1 review: each role image below is exactly 300x96", fill=(235, 228, 205), font=FONT)
	for index, stem in enumerate(ROLE_STEMS):
		column = index % 2
		row = index // 2
		x = column * cell_width + 10
		y = 28 + row * cell_height
		draw.text((x, y + 2), short_label(stem), fill=(224, 212, 177), font=FONT)
		image = Image.open(PACKAGE_ROOT / f"processed_png/roles/{stem}.png").convert("RGB")
		canvas.paste(image, (x, y + 22))
	path = CONTACT_ROOT / "district_roles_native_1x.png"
	canvas.save(path, optimize=True)
	return path


def make_state_native_contact() -> Path:
	cell_width = 86
	canvas = Image.new("RGB", (cell_width * len(STATE_STEMS), 104), (21, 24, 22))
	draw = ImageDraw.Draw(canvas)
	draw.text((8, 6), "Native 1:1 review: each overlay is exactly 48x48", fill=(235, 228, 205), font=FONT)
	for index, stem in enumerate(STATE_STEMS):
		x = index * cell_width + 19
		image = Image.open(PACKAGE_ROOT / f"processed_png/states/{stem}.png").convert("RGBA")
		canvas.paste(on_checker(image), (x, 28))
		label = short_label(stem)
		draw.text((index * cell_width + 4, 80), label, fill=(224, 212, 177), font=FONT)
	path = CONTACT_ROOT / "district_states_native_1x.png"
	canvas.save(path, optimize=True)
	return path


def make_state_nearest_contact() -> Path:
	cell_width = 220
	cell_height = 226
	canvas = Image.new("RGB", (cell_width * 3, cell_height * 2 + 28), (21, 24, 22))
	draw = ImageDraw.Draw(canvas)
	draw.text((8, 6), "Nearest-neighbour 4x review: geometry and keyed edges only; not runtime art", fill=(235, 228, 205), font=FONT)
	for index, stem in enumerate(STATE_STEMS):
		column = index % 3
		row = index // 3
		x = column * cell_width + 14
		y = 28 + row * cell_height
		draw.text((x, y + 2), short_label(stem), fill=(224, 212, 177), font=FONT)
		image = Image.open(PACKAGE_ROOT / f"processed_png/states/{stem}.png").convert("RGBA")
		enlarged = on_checker(image).resize((192, 192), Image.Resampling.NEAREST)
		canvas.paste(enlarged, (x, y + 22))
	path = CONTACT_ROOT / "district_states_nearest_4x.png"
	canvas.save(path, optimize=True)
	return path


def read_dds_header(path: Path) -> dict[str, int]:
	data = path.read_bytes()
	return {
		"magic_ok": int(data[:4] == b"DDS "),
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
		"byte_length": len(data),
	}


def dhash(image: Image.Image) -> int:
	gray = image.convert("L").resize((9, 8), Image.Resampling.LANCZOS)
	array = np.asarray(gray)
	bits = array[:, 1:] > array[:, :-1]
	value = 0
	for bit in bits.flatten():
		value = (value << 1) | int(bit)
	return value


def composite_for_metric(path: Path) -> Image.Image:
	image = Image.open(path).convert("RGBA")
	background = Image.new("RGBA", image.size, (27, 31, 28, 255))
	background.alpha_composite(image)
	return background.convert("RGB")


def pairwise_metrics(stems: tuple[str, ...], family: str) -> dict[str, object]:
	images = {
		stem: composite_for_metric(PACKAGE_ROOT / f"processed_png/{family}s/{stem}.png")
		for stem in stems
	}
	records = []
	for first, second in itertools.combinations(stems, 2):
		first_array = np.asarray(images[first], dtype=np.float32)
		second_array = np.asarray(images[second], dtype=np.float32)
		mean_absolute_difference = float(np.abs(first_array - second_array).mean() / 255.0)
		hamming = bin(dhash(images[first]) ^ dhash(images[second])).count("1")
		records.append(
			{
				"first": first,
				"second": second,
				"dhash_hamming": hamming,
				"normalized_mean_absolute_difference": mean_absolute_difference,
			}
		)
	return {
		"pairs": records,
		"minimum_dhash_hamming": min(record["dhash_hamming"] for record in records),
		"minimum_normalized_mean_absolute_difference": min(
			record["normalized_mean_absolute_difference"] for record in records
		),
	}


def magenta_fringe_pixels(image: Image.Image) -> int:
	rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
	r, g, b, a = [rgba[:, :, index] for index in range(4)]
	mask = (
		(a > 8)
		& (r > 120)
		& (b > 120)
		& (g < 80)
		& ((r.astype(np.int16) + b.astype(np.int16)) > 4 * g.astype(np.int16))
	)
	return int(mask.sum())


def validate_asset(stem: str, family: str, processing_record: dict[str, object]) -> dict[str, object]:
	expected_size = (300, 96) if family == "role" else (48, 48)
	source = PACKAGE_ROOT / f"source_png/{family}s/{stem}_source.png"
	processed = PACKAGE_ROOT / f"processed_png/{family}s/{stem}.png"
	decoded = PACKAGE_ROOT / f"decoded_png/{family}s/{stem}.png"
	runtime = RUNTIME_ROOT / f"{stem}.dds"

	processed_image = Image.open(processed).convert("RGBA")
	decoded_image = Image.open(decoded).convert("RGBA")
	processed_rgba = np.asarray(processed_image)
	decoded_rgba = np.asarray(decoded_image)
	alpha = processed_rgba[:, :, 3]
	header = read_dds_header(runtime)
	header_ok = (
		header["magic_ok"] == 1
		and header["header_size"] == 124
		and header["pixel_format_size"] == 32
		and header["pixel_format_flags"] == 0x41
		and header["fourcc"] == 0
		and header["bit_count"] == 32
		and header["red_mask"] == 0x00FF0000
		and header["green_mask"] == 0x0000FF00
		and header["blue_mask"] == 0x000000FF
		and header["alpha_mask"] == 0xFF000000
		and header["caps"] == 0x1000
		and header["width"] == expected_size[0]
		and header["height"] == expected_size[1]
		and header["pitch"] == expected_size[0] * 4
		and header["byte_length"] == 128 + expected_size[0] * expected_size[1] * 4
	)
	fit = processing_record["fit"]
	geometry_ok = not fit["nonuniform_stretch"]
	if family == "role":
		geometry_ok = geometry_ok and abs(fit["crop_aspect_ratio"] - (300 / 96)) < 1e-9
	else:
		content_ratio = fit["alpha_content_aspect_ratio"]
		scaled_ratio = fit["scaled_content_size"][0] / fit["scaled_content_size"][1]
		geometry_ok = geometry_ok and abs((scaled_ratio / content_ratio) - 1.0) < 0.03

	checks = {
		"source_exists": source.is_file(),
		"processed_exists": processed.is_file(),
		"runtime_exists": runtime.is_file(),
		"decoded_exists": decoded.is_file(),
		"processed_dimensions_ok": processed_image.size == expected_size,
		"decoded_dimensions_ok": decoded_image.size == expected_size,
		"decoded_pixel_match": bool(np.array_equal(processed_rgba, decoded_rgba)),
		"dds_header_ok": header_ok,
		"geometry_fit_ok": geometry_ok,
		"role_alpha_opaque": bool(alpha.min() == 255 and alpha.max() == 255) if family == "role" else True,
		"state_alpha_range_ok": bool(alpha.min() == 0 and alpha.max() == 255) if family == "state" else True,
		"state_corners_transparent": bool(
			alpha[0, 0] == 0 and alpha[0, -1] == 0 and alpha[-1, 0] == 0 and alpha[-1, -1] == 0
		) if family == "state" else True,
		"state_has_no_visible_magenta_fringe": magenta_fringe_pixels(processed_image) == 0 if family == "state" else True,
	}
	return {
		"stem": stem,
		"family": family,
		"expected_size": list(expected_size),
		"alpha_range": [int(alpha.min()), int(alpha.max())],
		"visible_magenta_fringe_pixels": magenta_fringe_pixels(processed_image) if family == "state" else 0,
		"dds_header": header,
		"fit": fit,
		"sha256": {
			"source": sha256(source),
			"processed": sha256(processed),
			"runtime_dds": sha256(runtime),
			"decoded": sha256(decoded),
		},
		"checks": checks,
		"pass": all(checks.values()),
	}


def wiring_checks(stems: tuple[str, ...]) -> dict[str, object]:
	gfx_path = REPO_ROOT / "interface/015_utopia_manifesto.gfx"
	gui_path = REPO_ROOT / "interface/015_utopia_manifesto_ledger.gui"
	scripted_gui_path = REPO_ROOT / "common/scripted_guis/015_utopia_manifesto_scripted_gui.txt"
	gfx = gfx_path.read_text(encoding="utf-8-sig")
	gui = gui_path.read_text(encoding="utf-8-sig")
	scripted_gui = scripted_gui_path.read_text(encoding="utf-8-sig")
	records = []
	for stem in stems:
		texture_path = f"gfx/interface/015_utopia_manifesto/ledger/{stem}.dds"
		record = {
			"stem": stem,
			"gfx_sprite_registered": f'name = "GFX_{stem}"' in gfx,
			"gfx_texture_path_registered": f'texturefile = "{texture_path}"' in gfx,
			"gui_consumer_present": f'name = "{stem}"' in gui and f'spriteType = "GFX_{stem}"' in gui,
			"scripted_gui_visibility_binding_present": f"{stem}_visible" in scripted_gui,
		}
		record["pass"] = all(value for key, value in record.items() if key not in {"stem", "pass"})
		records.append(record)
	return {
		"gfx_file": gfx_path.relative_to(REPO_ROOT).as_posix(),
		"gui_file": gui_path.relative_to(REPO_ROOT).as_posix(),
		"scripted_gui_file": scripted_gui_path.relative_to(REPO_ROOT).as_posix(),
		"records": records,
		"pass": all(record["pass"] for record in records),
	}


def write_checksum_file() -> Path:
	checksum_path = PACKAGE_ROOT / "metadata/checksums.sha256"
	paths = [
		path for path in PACKAGE_ROOT.rglob("*")
		if path.is_file() and path.resolve() != checksum_path.resolve()
	]
	paths.extend(RUNTIME_ROOT / f"{stem}.dds" for stem in (*ROLE_STEMS, *STATE_STEMS))
	paths = sorted(set(paths), key=lambda path: path.relative_to(REPO_ROOT).as_posix())
	lines = [f"{sha256(path)}  {path.relative_to(REPO_ROOT).as_posix()}" for path in paths]
	checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
	return checksum_path


def main() -> None:
	CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
	VALIDATION_ROOT.mkdir(parents=True, exist_ok=True)
	contact_paths = [
		make_role_source_runtime_contact(),
		make_state_source_runtime_contact(),
		make_role_native_contact(),
		make_state_native_contact(),
		make_state_nearest_contact(),
	]

	processing_report = json.loads((PACKAGE_ROOT / "metadata/processing_report.json").read_text(encoding="utf-8"))
	processing_records = {record["stem"]: record for record in processing_report["records"]}
	assets = [validate_asset(stem, "role", processing_records[stem]) for stem in ROLE_STEMS]
	assets.extend(validate_asset(stem, "state", processing_records[stem]) for stem in STATE_STEMS)

	role_metrics = pairwise_metrics(ROLE_STEMS, "role")
	state_metrics = pairwise_metrics(STATE_STEMS, "state")
	source_hashes = [asset["sha256"]["source"] for asset in assets]
	processed_hashes = [asset["sha256"]["processed"] for asset in assets]
	runtime_hashes = [asset["sha256"]["runtime_dds"] for asset in assets]
	uniqueness = {
		"source_hashes_unique": len(source_hashes) == len(set(source_hashes)) == 13,
		"processed_hashes_unique": len(processed_hashes) == len(set(processed_hashes)) == 13,
		"runtime_hashes_unique": len(runtime_hashes) == len(set(runtime_hashes)) == 13,
	}
	wiring = wiring_checks((*ROLE_STEMS, *STATE_STEMS))
	manual_review_path = PACKAGE_ROOT / "validation/native_size_visual_review.md"
	manual_review_present = manual_review_path.is_file()

	report = {
		"schema_version": 1,
		"scope": "Event 015 Ledger District role cards and state overlays",
		"counts": {"roles": len(ROLE_STEMS), "states": len(STATE_STEMS), "total": len(assets)},
		"assets": assets,
		"uniqueness": uniqueness,
		"pairwise_distinction": {"roles": role_metrics, "states": state_metrics},
		"wiring_read_only_audit": wiring,
		"contact_sheets": [path.relative_to(REPO_ROOT).as_posix() for path in contact_paths],
		"manual_review_record": manual_review_path.relative_to(REPO_ROOT).as_posix(),
		"manual_review_present": manual_review_present,
		"overall_pass": (
			all(asset["pass"] for asset in assets)
			and all(uniqueness.values())
			and wiring["pass"]
			and manual_review_present
		),
	}
	json_path = VALIDATION_ROOT / "validation_report.json"
	json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

	markdown_lines = [
		"# Ledger District Card Validation",
		"",
		f"Machine result: **{'PASS' if report['overall_pass'] else 'INCOMPLETE'}**",
		"",
		f"- Assets checked: `{len(assets)}` (`7` roles, `6` states).",
		f"- Asset records passing: `{sum(asset['pass'] for asset in assets)}/{len(assets)}`.",
		f"- Unique source/processed/runtime hashes: `{all(uniqueness.values())}`.",
		f"- Read-only GFX/GUI/scripted-GUI wiring audit: `{wiring['pass']}`.",
		f"- Role minimum pairwise dHash distance: `{role_metrics['minimum_dhash_hamming']}`.",
		f"- State minimum pairwise dHash distance: `{state_metrics['minimum_dhash_hamming']}`.",
		f"- Role minimum normalized pixel difference: `{role_metrics['minimum_normalized_mean_absolute_difference']:.6f}`.",
		f"- State minimum normalized pixel difference: `{state_metrics['minimum_normalized_mean_absolute_difference']:.6f}`.",
		f"- Native-size manual review record present: `{manual_review_present}`.",
		"",
		"The JSON report contains every DDS header field, exact length, dimensions, alpha range, decoded-pixel parity, fit geometry, magenta-fringe count, hashes, pairwise distinction metrics, and wiring record.",
	]
	(VALIDATION_ROOT / "validation_report.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")
	checksum_path = write_checksum_file()
	print(f"Validated {len(assets)} assets: overall_pass={report['overall_pass']}")
	print(json_path.relative_to(REPO_ROOT).as_posix())
	print(checksum_path.relative_to(REPO_ROOT).as_posix())


if __name__ == "__main__":
	main()
