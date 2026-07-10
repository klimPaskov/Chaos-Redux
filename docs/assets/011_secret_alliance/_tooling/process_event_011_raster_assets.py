#!/usr/bin/env python3
"""Deterministically process the Event 011 report, news, and super-event raster package."""

from __future__ import annotations

import hashlib
import math
import random
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "011_secret_alliance"
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
NOTES = PACKAGE / "notes"

REPORT_PROCESSOR_SHA256 = "5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9"
REPORT_PROCESSOR_CANDIDATES = (
	ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py",
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/7654/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
)

REPORT_STEMS = (
	"report_event_first_pattern",
	"report_event_missing_courier",
	"report_event_machine_sabotage",
	"report_event_safehouse_raid",
	"report_event_border_survey",
	"report_event_political_attack",
	"report_event_turned_channel",
)


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def find_verified_report_processor() -> Path:
	for path in REPORT_PROCESSOR_CANDIDATES:
		if path.is_file() and sha256(path) == REPORT_PROCESSOR_SHA256:
			return path
	raise RuntimeError(
		"The verified report-card processor is unavailable or its SHA-256 does not match "
		f"{REPORT_PROCESSOR_SHA256}. Refusing to substitute another workflow."
	)


def ensure_dirs() -> None:
	for path in (PROCESSED, CONTACT, NOTES, ROOT / "gfx" / "event_pictures" / "011_secret_alliance", ROOT / "gfx" / "super_events" / "011_secret_alliance"):
		path.mkdir(parents=True, exist_ok=True)


def run_report_processing(processor: Path) -> None:
	for index, stem in enumerate(REPORT_STEMS):
		source = SOURCE / f"{stem}_source.png"
		output = PROCESSED / f"{stem}.png"
		command = [
			sys.executable,
			str(processor),
			str(source),
			str(output),
			"--canvas-size", "210x176",
			"--card-size", "192x153",
			"--border", "0",
			"--angle", "4.0",
			"--shadow-offset", "4", "5",
			"--shadow-blur", "4.5",
			"--shadow-opacity", "0.50",
			"--grain", "7",
			"--paper-grain", "0",
			"--seed", str(1337 + index),
			"--rotate-supersample", "4",
			"--edge-soften", "0.35",
		]
		subprocess.run(command, cwd=ROOT, check=True)


def cover_crop(image: Image.Image, target_size: tuple[int, int]) -> Image.Image:
	target_width, target_height = target_size
	source_width, source_height = image.size
	scale = max(target_width / source_width, target_height / source_height)
	resized = image.resize(
		(int(round(source_width * scale)), int(round(source_height * scale))),
		Image.Resampling.LANCZOS,
	)
	left = (resized.width - target_width) // 2
	top = (resized.height - target_height) // 2
	return resized.crop((left, top, left + target_width, top + target_height))


def add_monochrome_grain(image: Image.Image, strength: int, seed: int) -> Image.Image:
	gray = image.convert("L")
	rng = random.Random(seed)
	pixels = gray.load()
	for y in range(gray.height):
		for x in range(gray.width):
			pixels[x, y] = max(0, min(255, pixels[x, y] + rng.randint(-strength, strength)))
	return gray


def process_news() -> None:
	source = Image.open(SOURCE / "news_event_public_coalition_source.png").convert("RGB")
	news = cover_crop(source, (397, 153))
	news = ImageOps.autocontrast(news, cutoff=1)
	news = ImageEnhance.Contrast(news).enhance(1.12)
	news = ImageEnhance.Sharpness(news).enhance(1.05)
	news = add_monochrome_grain(news, strength=3, seed=2117)
	news.save(PROCESSED / "news_event_public_coalition.png")


def process_super_event() -> None:
	source = Image.open(SOURCE / "super_event_public_reveal_source.png").convert("RGB")
	image = cover_crop(source, (457, 328))
	image = ImageOps.autocontrast(image, cutoff=1)
	image = ImageEnhance.Contrast(image).enhance(1.08)
	image = ImageEnhance.Brightness(image).enhance(0.98)
	image = ImageEnhance.Sharpness(image).enhance(1.04)
	image = add_monochrome_grain(image, strength=2, seed=3011).convert("RGB")
	image.save(PROCESSED / "super_event_public_reveal.png")


def checker(size: tuple[int, int], tile: int = 16) -> Image.Image:
	canvas = Image.new("RGB", size, (212, 212, 212))
	draw = ImageDraw.Draw(canvas)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if ((x // tile) + (y // tile)) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(239, 239, 239))
	return canvas


def make_contact_sheet(items: list[tuple[str, Path]], output: Path, source_sheet: bool) -> None:
	columns = 3
	cell_width = 520
	cell_height = 390 if source_sheet else 390
	rows = math.ceil(len(items) / columns)
	sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (24, 24, 24))
	draw = ImageDraw.Draw(sheet)
	for index, (label, path) in enumerate(items):
		image = Image.open(path).convert("RGBA")
		max_size = (480, 315 if source_sheet else 320)
		image.thumbnail(max_size, Image.Resampling.LANCZOS)
		col = index % columns
		row = index // columns
		x0 = col * cell_width
		y0 = row * cell_height
		background = checker((480, 320)) if not source_sheet else Image.new("RGB", (480, 320), (236, 232, 222))
		background.paste(image, ((480 - image.width) // 2, (320 - image.height) // 2), image)
		sheet.paste(background, (x0 + 20, y0 + 22))
		draw.text((x0 + 20, y0 + 350), label, fill=(245, 245, 245))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def make_review_files() -> None:
	source_items = [(stem, SOURCE / f"{stem}_source.png") for stem in REPORT_STEMS]
	source_items.extend([
		("news_event_public_coalition", SOURCE / "news_event_public_coalition_source.png"),
		("super_event_public_reveal", SOURCE / "super_event_public_reveal_source.png"),
	])
	processed_items = [(f"{stem} (210x176)", PROCESSED / f"{stem}.png") for stem in REPORT_STEMS]
	processed_items.extend([
		("news_event_public_coalition (397x153)", PROCESSED / "news_event_public_coalition.png"),
		("super_event_public_reveal (457x328)", PROCESSED / "super_event_public_reveal.png"),
	])
	make_contact_sheet(source_items, CONTACT / "event_011_raster_source_contact_sheet.png", source_sheet=True)
	make_contact_sheet(processed_items, CONTACT / "event_011_raster_processed_contact_sheet.png", source_sheet=False)

	template = Image.open(ROOT / "gfx" / "super_events" / "super_event_template.psd").convert("RGB")
	super_event = Image.open(PROCESSED / "super_event_public_reveal.png").convert("RGB")
	# The verified flattened template's white image aperture is x=409..863, y=106..431.
	template.paste(super_event.resize((455, 326), Image.Resampling.LANCZOS), (409, 106))
	template.save(CONTACT / "super_event_public_reveal_ui_mask_preview.png")


def convert_dds() -> None:
	converter = ROOT / ".tools" / "convert_to_dds.py"
	jobs = [(PROCESSED / f"{stem}.png", ROOT / "gfx" / "event_pictures" / "011_secret_alliance" / f"{stem}.dds", (210, 176)) for stem in REPORT_STEMS]
	jobs.extend([
		(PROCESSED / "news_event_public_coalition.png", ROOT / "gfx" / "event_pictures" / "011_secret_alliance" / "news_event_public_coalition.dds", (397, 153)),
		(PROCESSED / "super_event_public_reveal.png", ROOT / "gfx" / "super_events" / "011_secret_alliance" / "super_event_public_reveal.dds", (457, 328)),
	])
	for source, output, size in jobs:
		command = [sys.executable, str(converter), "--input", str(source), "--output", str(output), "--width", str(size[0]), "--height", str(size[1])]
		subprocess.run(command, cwd=ROOT, check=True)


def parse_dds(path: Path) -> tuple[int, int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) < 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	values = struct.unpack("<31I", data[4:128])
	height = values[2]
	width = values[3]
	pixel_flags = values[19]
	rgb_bits = values[21]
	masks = (values[22], values[23], values[24], values[25])
	return width, height, pixel_flags, rgb_bits, masks


def validate(processor: Path) -> None:
	lines = [
		"# Event 011 raster validation",
		"",
		f"Verified report processor: `{processor}`",
		f"Report processor SHA-256: `{sha256(processor)}`",
		"",
	]
	jobs = [(PROCESSED / f"{stem}.png", ROOT / "gfx" / "event_pictures" / "011_secret_alliance" / f"{stem}.dds", (210, 176), True) for stem in REPORT_STEMS]
	jobs.extend([
		(PROCESSED / "news_event_public_coalition.png", ROOT / "gfx" / "event_pictures" / "011_secret_alliance" / "news_event_public_coalition.dds", (397, 153), False),
		(PROCESSED / "super_event_public_reveal.png", ROOT / "gfx" / "super_events" / "011_secret_alliance" / "super_event_public_reveal.dds", (457, 328), False),
	])
	for png, dds, expected, report in jobs:
		image = Image.open(png)
		if image.size != expected:
			raise RuntimeError(f"{png} is {image.size}; expected {expected}")
		if report:
			alpha = image.convert("RGBA").getchannel("A")
			corners = [alpha.getpixel((0, 0)), alpha.getpixel((expected[0] - 1, 0)), alpha.getpixel((0, expected[1] - 1)), alpha.getpixel((expected[0] - 1, expected[1] - 1))]
			if any(corners):
				raise RuntimeError(f"Report-card corners are not transparent: {png} -> {corners}")
		width, height, flags, bits, masks = parse_dds(dds)
		if (width, height) != expected or bits != 32 or masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
			raise RuntimeError(f"Unexpected DDS format for {dds}: {(width, height, flags, bits, masks)}")
		dds_image = Image.open(dds).convert("RGBA")
		if ImageChops.difference(image.convert("RGBA"), dds_image).getbbox() is not None:
			raise RuntimeError(f"DDS pixels differ from the processed PNG: {dds}")
		lines.append(f"- `{png.relative_to(ROOT)}`: {image.size[0]}x{image.size[1]}, mode {image.mode}; `{dds.relative_to(ROOT)}`: 32-bit BGRA masks and pixel identity verified")
	news = Image.open(PROCESSED / "news_event_public_coalition.png")
	if news.mode != "L":
		raise RuntimeError(f"News image is not true grayscale mode L: {news.mode}")
	source_hashes = {sha256(path) for path in SOURCE.glob("report_event_*_source.png")}
	source_hashes.add(sha256(SOURCE / "news_event_public_coalition_source.png"))
	source_hashes.add(sha256(SOURCE / "super_event_public_reveal_source.png"))
	if len(source_hashes) != 9:
		raise RuntimeError("The nine Event 011 raster sources are not byte-distinct")
	lines.extend([
		"",
		"- All seven report cards have transparent corner pixels.",
		"- The public-coalition news image is true grayscale (`L`) before DDS conversion.",
		"- The reveal image was reviewed through `gfx/super_events/super_event_template.psd` at the verified aperture.",
		"- All nine source rasters have distinct SHA-256 hashes; no source raster is reused.",
	])
	(NOTES / "validation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
	ensure_dirs()
	processor = find_verified_report_processor()
	run_report_processing(processor)
	process_news()
	process_super_event()
	make_review_files()
	convert_dds()
	validate(processor)
	print(f"processed reports with {processor}")
	print(f"report processor sha256={sha256(processor)}")


if __name__ == "__main__":
	main()
