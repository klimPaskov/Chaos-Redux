#!/usr/bin/env python3
"""Mechanical processing, contact-sheet assembly, and validation for this asset package."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageChops, ImageDraw, ImageFont


FOCUS_SIZE = (94, 86)
IDEA_SIZE = (64, 64)
REPORT_SIZE = (210, 176)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
	for candidate in (
		Path("C:/Windows/Fonts/arial.ttf"),
		Path("C:/Windows/Fonts/segoeui.ttf"),
	):
		if candidate.exists():
			return ImageFont.truetype(str(candidate), size=size)
	return ImageFont.load_default()


def sanitize_transparent_rgb(image: Image.Image) -> Image.Image:
	image = image.convert("RGBA")
	pixels = image.load()
	for y in range(image.height):
		for x in range(image.width):
			r, g, b, a = pixels[x, y]
			if a == 0:
				pixels[x, y] = (0, 0, 0, 0)
	return image


def process_icon(source: Path, output: Path, target_size: tuple[int, int], margin: int) -> None:
	image = Image.open(source).convert("RGBA")
	alpha = image.getchannel("A")
	mask = alpha.point(lambda value: 255 if value > 5 else 0)
	bbox = mask.getbbox()
	if bbox is None:
		raise ValueError(f"No opaque subject found in {source}")
	image = image.crop(bbox)
	max_width = target_size[0] - margin * 2
	max_height = target_size[1] - margin * 2
	scale = min(max_width / image.width, max_height / image.height)
	resized_size = (
		max(1, round(image.width * scale)),
		max(1, round(image.height * scale)),
	)
	# Premultiplied resize prevents hidden chroma-key RGB from bleeding into alpha edges.
	image = image.convert("RGBa").resize(resized_size, Image.Resampling.LANCZOS).convert("RGBA")
	image = sanitize_transparent_rgb(image)
	canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
	x = (target_size[0] - image.width) // 2
	y = (target_size[1] - image.height) // 2
	canvas.alpha_composite(image, (x, y))
	output.parent.mkdir(parents=True, exist_ok=True)
	canvas.save(output, format="PNG", optimize=True)


def process_icon_folder(input_dir: Path, output_dir: Path, kind: str) -> None:
	target_size, margin = (FOCUS_SIZE, 3) if kind == "focus" else (IDEA_SIZE, 3)
	inputs = sorted(input_dir.glob("*.png"))
	if not inputs:
		raise ValueError(f"No PNG inputs found in {input_dir}")
	for source in inputs:
		process_icon(source, output_dir / source.name, target_size, margin)


def checker_tile(size: tuple[int, int], tile: int = 8) -> Image.Image:
	image = Image.new("RGB", size, (86, 86, 86))
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(126, 126, 126))
	return image


def wrap_label(label: str, max_chars: int = 31) -> list[str]:
	words = label.split("_")
	lines: list[str] = []
	current = ""
	for word in words:
		candidate = word if not current else f"{current}_{word}"
		if len(candidate) <= max_chars:
			current = candidate
		else:
			if current:
				lines.append(current)
			current = word
	if current:
		lines.append(current)
	return lines[:3]


def build_contact_sheet(
	images: Iterable[Path],
	output: Path,
	title: str,
	columns: int,
	scale: int,
) -> None:
	paths = list(images)
	if not paths:
		raise ValueError(f"No images supplied for contact sheet {output}")
	font = load_font(17)
	title_font = load_font(24)
	max_width = max(Image.open(path).width for path in paths) * scale
	max_height = max(Image.open(path).height for path in paths) * scale
	cell_width = max(270, max_width + 34)
	cell_height = max_height + 88
	rows = (len(paths) + columns - 1) // columns
	margin = 22
	header = 48
	sheet = Image.new(
		"RGB",
		(margin * 2 + cell_width * columns, margin * 2 + header + cell_height * rows),
		(27, 29, 31),
	)
	draw = ImageDraw.Draw(sheet)
	draw.text((margin, margin), title, font=title_font, fill=(240, 240, 240))
	for index, path in enumerate(paths):
		row, column = divmod(index, columns)
		left = margin + column * cell_width
		top = margin + header + row * cell_height
		image = Image.open(path).convert("RGBA")
		preview = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
		checker = checker_tile((max_width, max_height), tile=max(4, scale * 2))
		px = (max_width - preview.width) // 2
		py = (max_height - preview.height) // 2
		checker.paste(preview, (px, py), preview)
		sheet.paste(checker, (left + (cell_width - max_width) // 2, top))
		label_y = top + max_height + 9
		for line in wrap_label(path.stem):
			draw.text((left + 7, label_y), line, font=font, fill=(232, 232, 232))
			label_y += 18
		draw.text((left + 7, top + max_height + 63), f"{image.width}x{image.height} RGBA", font=font, fill=(164, 190, 214))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, format="PNG", optimize=True)


def sha256(path: Path) -> str:
	hash_object = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			hash_object.update(chunk)
	return hash_object.hexdigest()


def average_hash(path: Path) -> int:
	image = Image.open(path).convert("RGB").resize((16, 16), Image.Resampling.LANCZOS)
	values = [sum(pixel) / 3 for pixel in image.getdata()]
	mean = sum(values) / len(values)
	result = 0
	for value in values:
		result = (result << 1) | int(value >= mean)
	return result


def image_record(path: Path) -> dict[str, object]:
	image = Image.open(path).convert("RGBA")
	alpha = image.getchannel("A")
	alpha_min, alpha_max = alpha.getextrema()
	alpha_values = list(alpha.getdata())
	return {
		"path": path.as_posix(),
		"sha256": sha256(path),
		"dimensions": [image.width, image.height],
		"mode": image.mode,
		"alpha_min": alpha_min,
		"alpha_max": alpha_max,
		"alpha_nonzero_fraction": round(sum(value > 0 for value in alpha_values) / len(alpha_values), 6),
		"corner_alpha": [
			alpha.getpixel((0, 0)),
			alpha.getpixel((image.width - 1, 0)),
			alpha.getpixel((0, image.height - 1)),
			alpha.getpixel((image.width - 1, image.height - 1)),
		],
	}


def dds_record(path: Path) -> dict[str, object]:
	data = path.read_bytes()
	if len(data) < 128:
		raise ValueError(f"DDS is shorter than the legacy header: {path}")
	magic = data[:4]
	header_size = struct.unpack_from("<I", data, 4)[0]
	height = struct.unpack_from("<I", data, 12)[0]
	width = struct.unpack_from("<I", data, 16)[0]
	pf_size, pf_flags, fourcc, bit_count, r_mask, g_mask, b_mask, a_mask = struct.unpack_from("<8I", data, 76)
	caps = struct.unpack_from("<I", data, 108)[0]
	pixel_data = data[128:]
	alpha_values = pixel_data[3::4]
	expected_length = 128 + width * height * 4
	checks = {
		"magic": magic == b"DDS ",
		"header_size_124": header_size == 124,
		"pixel_format_size_32": pf_size == 32,
		"pixel_format_flags_65": pf_flags == 65,
		"fourcc_zero": fourcc == 0,
		"bit_count_32": bit_count == 32,
		"bgra_masks": [r_mask, g_mask, b_mask, a_mask] == [0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000],
		"dds_caps_texture": bool(caps & 0x1000),
		"exact_length": len(data) == expected_length,
	}
	return {
		"path": path.as_posix(),
		"sha256": sha256(path),
		"dimensions": [width, height],
		"file_length": len(data),
		"expected_length": expected_length,
		"alpha_min": min(alpha_values) if alpha_values else None,
		"alpha_max": max(alpha_values) if alpha_values else None,
		"checks": checks,
		"valid": all(checks.values()),
	}


def validate(package_root: Path, mod_root: Path, output: Path) -> None:
	source_paths = sorted((package_root / "source_png").glob("*/*.png"))
	processed_paths = sorted((package_root / "processed_png").glob("*/*.png"))
	final_paths = sorted((mod_root / "gfx/interface/goals/006_independence_wave/rhineland_bavaria").glob("*.dds"))
	final_paths += sorted((mod_root / "gfx/interface/ideas/006_independence_wave/rhineland_bavaria").glob("*.dds"))
	final_paths += sorted((mod_root / "gfx/event_pictures/006_independence_wave/rhineland_bavaria").glob("*.dds"))
	processed_by_stem = {path.stem: path for path in processed_paths}
	final_by_stem = {path.stem: path for path in final_paths}
	roundtrip = []
	for stem in sorted(set(processed_by_stem) | set(final_by_stem)):
		processed_path = processed_by_stem.get(stem)
		final_path = final_by_stem.get(stem)
		dimensions_match = False
		rgba_exact_match = False
		if processed_path is not None and final_path is not None:
			processed_image = Image.open(processed_path).convert("RGBA")
			final_image = Image.open(final_path).convert("RGBA")
			dimensions_match = processed_image.size == final_image.size
			rgba_exact_match = dimensions_match and ImageChops.difference(processed_image, final_image).getbbox() is None
		roundtrip.append({
			"stem": stem,
			"processed_png": processed_path.as_posix() if processed_path else None,
			"final_dds": final_path.as_posix() if final_path else None,
			"dimensions_match": dimensions_match,
			"rgba_exact_match": rgba_exact_match,
		})
	source_hashes = {path.as_posix(): average_hash(path) for path in source_paths}
	pairwise = []
	items = list(source_hashes.items())
	for index, (left_path, left_hash) in enumerate(items):
		for right_path, right_hash in items[index + 1 :]:
			pairwise.append({
				"left": left_path,
				"right": right_path,
				"hamming_distance": bin(left_hash ^ right_hash).count("1"),
			})
	report = {
		"expected_counts": {"source_png": 26, "processed_png": 26, "final_dds": 26},
		"actual_counts": {
			"source_png": len(source_paths),
			"processed_png": len(processed_paths),
			"final_dds": len(final_paths),
		},
		"source_png": [image_record(path) for path in source_paths],
		"processed_png": [image_record(path) for path in processed_paths],
		"final_dds": [dds_record(path) for path in final_paths],
		"source_sha256_unique": len({sha256(path) for path in source_paths}) == len(source_paths),
		"source_perceptual_hash": {
			"algorithm": "16x16 RGB average hash; hamming distances are review evidence, not a visual-quality substitute",
			"minimum_pairwise_distance": min((row["hamming_distance"] for row in pairwise), default=None),
			"pairs": pairwise,
		},
		"dds_roundtrip": {
			"all_match": all(row["rgba_exact_match"] for row in roundtrip),
			"pairs": roundtrip,
		},
	}
	report["all_dds_valid"] = all(record["valid"] for record in report["final_dds"])
	report["counts_match"] = report["actual_counts"] == report["expected_counts"]
	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def main() -> None:
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="command", required=True)
	icons = subparsers.add_parser("icons")
	icons.add_argument("--kind", choices=("focus", "idea"), required=True)
	icons.add_argument("--input-dir", type=Path, required=True)
	icons.add_argument("--output-dir", type=Path, required=True)
	contact = subparsers.add_parser("contact")
	contact.add_argument("--input-dir", type=Path, required=True)
	contact.add_argument("--pattern", default="*.png")
	contact.add_argument("--output", type=Path, required=True)
	contact.add_argument("--title", required=True)
	contact.add_argument("--columns", type=int, default=4)
	contact.add_argument("--scale", type=int, default=3)
	validation = subparsers.add_parser("validate")
	validation.add_argument("--package-root", type=Path, required=True)
	validation.add_argument("--mod-root", type=Path, required=True)
	validation.add_argument("--output", type=Path, required=True)
	args = parser.parse_args()
	if args.command == "icons":
		process_icon_folder(args.input_dir, args.output_dir, args.kind)
	elif args.command == "contact":
		build_contact_sheet(
			sorted(args.input_dir.glob(args.pattern)),
			args.output,
			args.title,
			args.columns,
			args.scale,
		)
	else:
		validate(args.package_root, args.mod_root, args.output)


if __name__ == "__main__":
	main()
