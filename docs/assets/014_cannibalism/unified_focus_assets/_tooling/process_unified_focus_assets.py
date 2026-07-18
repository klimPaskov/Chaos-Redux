#!/usr/bin/env python3
"""Finalize all 108 Event 014 unified-country focus icons."""

from __future__ import annotations

import csv
import hashlib
import math
import re
import shutil
import struct
import subprocess
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[5]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "unified_focus_asset_validation.tsv"
GFX_HANDOFF = PACKAGE / "validation" / "unified_focus_gfx_handoff.tsv"
LIVE = ROOT / "gfx" / "interface" / "goals" / "014_cannibalism"
FOCUS_FILE = ROOT / "common" / "national_focus" / "014_cannibalism_unified_focus.txt"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
CHROMA_HELPER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
SIZE = (94, 86)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def focus_names() -> list[str]:
	text = FOCUS_FILE.read_text(encoding="utf-8-sig")
	ids = re.findall(r"(?m)^\s*id\s*=\s*(CBL_[a-z0-9_]+)\s*$", text)
	if len(ids) != 108 or len(set(ids)) != 108:
		raise RuntimeError(f"Expected 108 unique unified focus ids, found {len(ids)} / {len(set(ids))}")
	return [f"goal_{focus_id}" for focus_id in ids]


def run_chroma(name: str) -> None:
	input_path = SOURCE / f"{name}_source.png"
	output_path = ALPHA / f"{name}_alpha.png"
	result = subprocess.run(
		[
			sys.executable, str(CHROMA_HELPER), "--input", str(input_path), "--out", str(output_path),
			"--auto-key", "border", "--soft-matte", "--transparent-threshold", "12",
			"--opaque-threshold", "220", "--despill", "--force",
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"Chroma cleanup failed for {name}:\n{result.stdout}\n{result.stderr}")


def trim_alpha(image: Image.Image) -> Image.Image:
	rgba = image.convert("RGBA")
	bbox = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0).getbbox()
	if bbox is None:
		raise RuntimeError("No visible pixels after chroma-key cleanup")
	return rgba.crop(bbox)


def fit_alpha(source: Path) -> Image.Image:
	scale, padding = 4, 3
	image = trim_alpha(Image.open(source))
	maximum = ((SIZE[0] - padding * 2 - 2) * scale, (SIZE[1] - padding * 2 - 2) * scale)
	ratio = min(maximum[0] / image.width, maximum[1] / image.height)
	resized = image.resize(
		(max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
		Image.Resampling.LANCZOS,
	)
	high_size = (SIZE[0] * scale, SIZE[1] * scale)
	x, y = (high_size[0] - resized.width) // 2, (high_size[1] - resized.height) // 2
	alpha = Image.new("L", high_size, 0)
	alpha.paste(resized.getchannel("A"), (x, y))
	shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=8)).point(lambda value: round(value * 0.42))
	shifted_shadow = Image.new("L", high_size, 0)
	shifted_shadow.paste(shadow_alpha, (4, 4))
	shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
	shadow.putalpha(shifted_shadow)
	outline_alpha = alpha.filter(ImageFilter.MaxFilter(9)).point(lambda value: round(value * 0.9))
	outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
	outline.putalpha(outline_alpha)
	subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
	subject.alpha_composite(resized, (x, y))
	return Image.alpha_composite(Image.alpha_composite(shadow, outline), subject).resize(SIZE, Image.Resampling.LANCZOS)


def convert(name: str) -> None:
	png = PROCESSED / f"{name}.png"
	package_dds = DDS_PACKAGE / f"{name}.dds"
	result = subprocess.run(
		[
			sys.executable, str(CONVERTER), "--input", str(png), "--output", str(package_dds),
			"--width", str(SIZE[0]), "--height", str(SIZE[1]),
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"DDS conversion failed for {name}:\n{result.stdout}\n{result.stderr}")
	shutil.copy2(package_dds, LIVE / f"{name}.dds")


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
	image = Image.new("RGBA", size, (72, 72, 72, 255))
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(116, 116, 116, 255))
	return image


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def make_contact(names: list[str], folder: Path, suffix: str, output: Path, source_mode: bool) -> None:
	columns, cell_w, cell_h = 9, 170, 155
	preview_size = (112, 112)
	rows = math.ceil(len(names) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
	draw = ImageDraw.Draw(sheet)
	label_font = font(9)
	for index, name in enumerate(names):
		x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
		draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(88, 92, 98))
		with Image.open(folder / f"{name}{suffix}") as opened:
			if source_mode:
				preview = ImageOps.contain(opened.convert("RGB"), preview_size, Image.Resampling.LANCZOS)
				plate = Image.new("RGB", preview_size, (48, 50, 54))
				plate.paste(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
			else:
				preview = ImageOps.contain(opened.convert("RGBA"), preview_size, Image.Resampling.NEAREST)
				plate_rgba = checker(preview_size, 10)
				plate_rgba.alpha_composite(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
				plate = plate_rgba.convert("RGB")
		sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 7))
		label = name.removeprefix("goal_CBL_")
		ly = y0 + 122
		for line in textwrap.wrap(label, width=25)[:2]:
			bbox = draw.textbbox((0, 0), line, font=label_font)
			draw.text((x0 + (cell_w - (bbox[2] - bbox[0])) // 2, ly), line, font=label_font, fill=(235, 235, 235))
			ly += 10
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def visible_key_green(image: Image.Image) -> int:
	data = image.convert("RGBA").tobytes()
	return sum(
		1 for index in range(0, len(data), 4)
		if data[index + 3] > 10
		and data[index + 1] > 190
		and data[index + 1] > data[index] * 1.55
		and data[index + 1] > data[index + 2] * 1.55
	)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) != 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	height = struct.unpack_from("<I", data, 12)[0]
	width = struct.unpack_from("<I", data, 16)[0]
	mip_count = struct.unpack_from("<I", data, 28)[0]
	masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
	return width, height, mip_count, masks


def main() -> None:
	names = focus_names()
	for directory in (ALPHA, PROCESSED, DDS_PACKAGE, CONTACT, VALIDATION.parent, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [name for name in names if not (SOURCE / f"{name}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing unified focus sources:\n" + "\n".join(missing))
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(run_chroma, names))
	for name in names:
		fit_alpha(ALPHA / f"{name}_alpha.png").save(PROCESSED / f"{name}.png", optimize=True)
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(convert, names))
	make_contact(names, SOURCE, "_source.png", CONTACT / "unified_focus_sources_contact_sheet.png", True)
	make_contact(names, PROCESSED, ".png", CONTACT / "unified_focus_processed_checker_contact_sheet.png", False)
	make_contact(names, LIVE, ".dds", CONTACT / "unified_focus_dds_decoded_contact_sheet.png", False)
	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	normalized_hashes: dict[str, str] = {}
	rows: list[list[str]] = []
	for name in names:
		source = SOURCE / f"{name}_source.png"
		alpha_path = ALPHA / f"{name}_alpha.png"
		processed = PROCESSED / f"{name}.png"
		package_dds = DDS_PACKAGE / f"{name}.dds"
		live_dds = LIVE / f"{name}.dds"
		image = Image.open(processed).convert("RGBA")
		alpha = image.getchannel("A")
		alpha_min, alpha_max = alpha.getextrema()
		corners = tuple(alpha.getpixel(point) for point in ((0, 0), (93, 0), (0, 85), (93, 85)))
		key_green = visible_key_green(image)
		if image.size != SIZE or alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0) or key_green:
			raise RuntimeError(f"Invalid processed icon {name}: size={image.size} alpha={(alpha_min, alpha_max)} corners={corners} key={key_green}")
		normalized = hashlib.sha256(image.tobytes()).hexdigest()
		if normalized in normalized_hashes:
			raise RuntimeError(f"Duplicate normalized artwork: {name} duplicates {normalized_hashes[normalized]}")
		normalized_hashes[normalized] = name
		width, height, mip_count, masks = dds_header(live_dds)
		if (width, height) != SIZE or mip_count not in (0, 1) or masks != expected_masks:
			raise RuntimeError(f"Invalid DDS for {name}: {(width, height)} mip={mip_count} masks={masks}")
		if sha256(package_dds) != sha256(live_dds):
			raise RuntimeError(f"Runtime DDS differs from package DDS for {name}")
		alpha_bytes = alpha.tobytes()
		transparent_pixels = alpha_bytes.count(0)
		partial_alpha_pixels = len(alpha_bytes) - transparent_pixels - alpha_bytes.count(255)
		rows.append([
			name, source.as_posix(), sha256(source), alpha_path.as_posix(), sha256(alpha_path),
			processed.as_posix(), sha256(processed), package_dds.as_posix(), sha256(package_dds),
			live_dds.relative_to(ROOT).as_posix(), sha256(live_dds), str(live_dds.stat().st_size),
			str(alpha_min), str(alpha_max), str(transparent_pixels), str(partial_alpha_pixels),
			normalized, "complete",
		])
	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow([
			"asset", "source", "source_sha256", "alpha_png", "alpha_sha256", "processed_png",
			"processed_sha256", "package_dds", "package_dds_sha256", "runtime_dds",
			"runtime_dds_sha256", "runtime_dds_bytes", "alpha_min", "alpha_max",
			"transparent_pixels", "partial_alpha_pixels", "normalized_rgba_sha256", "status",
		])
		writer.writerows(rows)
	with GFX_HANDOFF.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow(["focus_id", "sprite", "shine_sprite", "runtime_dds", "dimensions", "status"])
		for name in names:
			focus_id = name.removeprefix("goal_")
			writer.writerow([
				focus_id,
				f"GFX_goal_{focus_id}",
				f"GFX_goal_{focus_id}_shine",
				f"gfx/interface/goals/014_cannibalism/{name}.dds",
				"94x86",
				"ready",
			])
	print(f"Processed and validated {len(names)} Event 014 unified focus icons")


if __name__ == "__main__":
	main()
