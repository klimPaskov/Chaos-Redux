#!/usr/bin/env python3
"""Build and validate the generated camp-repression report and super-event art."""

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
PACKAGE = ROOT / "docs" / "assets" / "system_camp_repression_rework"
SOURCE = PACKAGE / "source" / "report_super_event"
PROCESSED = PACKAGE / "processed" / "report_super_event"
CONTACT = PACKAGE / "contact_sheets"
REPORT_RUNTIME = ROOT / "gfx" / "event_pictures" / "system_camp_repression_rework"
SUPER_RUNTIME = ROOT / "gfx" / "super_events" / "system_camp_repression_rework"

REPORT_PROCESSOR_SHA256 = "5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9"
REPORT_PROCESSOR_CANDIDATES = (
	ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py",
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/7654/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
)

REPORT_STEMS = (
	"report_event_auschwitz_discovery",
	"report_event_pingfang_authority",
	"report_event_kwantung_medical_bypass",
	"report_event_pingfang_outbreak",
	"report_event_pingfang_discovery",
	"report_event_pingfang_retreat",
	"report_event_pingfang_tribunal",
	"report_event_soviet_famine_warning",
	"report_event_soviet_famine_crisis",
	"report_event_soviet_administrative_breakdown",
	"report_event_soviet_famine_relief",
	"report_event_soviet_records_discovered",
)

SUPER_STEMS = (
	"super_event_angel_of_death_directorate_revolt",
	"super_event_global_discovery",
	"super_event_soviet_famine_catastrophe",
	"super_event_pingfang_exposure",
	"super_event_colonial_reckoning",
)


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def find_verified_report_processor() -> Path:
	for path in REPORT_PROCESSOR_CANDIDATES:
		if path.is_file() and sha256(path) == REPORT_PROCESSOR_SHA256:
			return path
	raise RuntimeError(
		"The verified report-card processor is unavailable or has the wrong SHA-256; "
		"refusing to substitute another treatment."
	)


def ensure_dirs() -> None:
	for path in (PROCESSED, CONTACT, REPORT_RUNTIME, SUPER_RUNTIME):
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
			"--seed", str(4201 + index),
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


def process_super_events() -> None:
	for index, stem in enumerate(SUPER_STEMS):
		source = Image.open(SOURCE / f"{stem}_source.png").convert("RGB")
		image = cover_crop(source, (457, 328))
		image = ImageOps.autocontrast(image, cutoff=1)
		image = ImageEnhance.Contrast(image).enhance(1.08)
		image = ImageEnhance.Brightness(image).enhance(0.98)
		image = ImageEnhance.Sharpness(image).enhance(1.04)
		image = add_monochrome_grain(image, strength=2, seed=5201 + index).convert("RGB")
		image.save(PROCESSED / f"{stem}.png")


def checker(size: tuple[int, int], tile: int = 16) -> Image.Image:
	canvas = Image.new("RGB", size, (212, 212, 212))
	draw = ImageDraw.Draw(canvas)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if ((x // tile) + (y // tile)) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(239, 239, 239))
	return canvas


def make_contact_sheet(
	items: list[tuple[str, Path]],
	output: Path,
	columns: int,
	preview_size: tuple[int, int],
	checkerboard: bool,
) -> None:
	label_height = 34
	padding = 16
	cell_width = preview_size[0] + padding * 2
	cell_height = preview_size[1] + label_height + padding * 2
	rows = math.ceil(len(items) / columns)
	sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (24, 24, 24))
	draw = ImageDraw.Draw(sheet)
	for index, (label, path) in enumerate(items):
		image = Image.open(path).convert("RGBA")
		image.thumbnail(preview_size, Image.Resampling.LANCZOS)
		col = index % columns
		row = index // columns
		x0 = col * cell_width + padding
		y0 = row * cell_height + padding
		background = checker(preview_size) if checkerboard else Image.new("RGB", preview_size, (226, 226, 226))
		background.paste(image, ((preview_size[0] - image.width) // 2, (preview_size[1] - image.height) // 2), image)
		sheet.paste(background, (x0, y0))
		draw.text((x0, y0 + preview_size[1] + 8), label, fill=(245, 245, 245))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def make_review_files() -> None:
	source_items = [
		(stem.removesuffix("_source"), SOURCE / f"{stem}_source.png")
		for stem in (*REPORT_STEMS, *SUPER_STEMS)
	]
	make_contact_sheet(
		source_items,
		CONTACT / "report_super_event_source_contact_sheet.png",
		columns=3,
		preview_size=(480, 320),
		checkerboard=False,
	)

	report_items = [(f"{stem} (210x176)", PROCESSED / f"{stem}.png") for stem in REPORT_STEMS]
	make_contact_sheet(
		report_items,
		CONTACT / "report_event_processed_contact_sheet.png",
		columns=3,
		preview_size=(420, 352),
		checkerboard=True,
	)

	super_items = [(f"{stem} (457x328)", PROCESSED / f"{stem}.png") for stem in SUPER_STEMS]
	make_contact_sheet(
		super_items,
		CONTACT / "super_event_processed_contact_sheet.png",
		columns=2,
		preview_size=(457, 328),
		checkerboard=False,
	)

	template = Image.open(ROOT / "gfx" / "super_events" / "super_event_template.psd").convert("RGB")
	preview_items: list[tuple[str, Path]] = []
	for stem in SUPER_STEMS:
		preview = template.copy()
		image = Image.open(PROCESSED / f"{stem}.png").convert("RGB")
		preview.paste(image.resize((455, 326), Image.Resampling.LANCZOS), (409, 106))
		path = CONTACT / f"{stem}_ui_mask_preview.png"
		preview.save(path)
		preview_items.append((stem, path))
	make_contact_sheet(
		preview_items,
		CONTACT / "super_event_ui_mask_preview_contact_sheet.png",
		columns=2,
		preview_size=(645, 272),
		checkerboard=False,
	)


def convert_dds() -> None:
	converter = ROOT / ".tools" / "convert_to_dds.py"
	jobs = [
		(PROCESSED / f"{stem}.png", REPORT_RUNTIME / f"{stem}.dds", (210, 176))
		for stem in REPORT_STEMS
	]
	jobs.extend(
		(PROCESSED / f"{stem}.png", SUPER_RUNTIME / f"{stem}.dds", (457, 328))
		for stem in SUPER_STEMS
	)
	for source, output, size in jobs:
		command = [
			sys.executable,
			str(converter),
			"--input", str(source),
			"--output", str(output),
			"--width", str(size[0]),
			"--height", str(size[1]),
		]
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


def validate() -> None:
	jobs = [
		(PROCESSED / f"{stem}.png", REPORT_RUNTIME / f"{stem}.dds", (210, 176), True)
		for stem in REPORT_STEMS
	]
	jobs.extend(
		(PROCESSED / f"{stem}.png", SUPER_RUNTIME / f"{stem}.dds", (457, 328), False)
		for stem in SUPER_STEMS
	)
	for png, dds, expected, report in jobs:
		image = Image.open(png).convert("RGBA")
		if image.size != expected:
			raise RuntimeError(f"{png} is {image.size}; expected {expected}")
		if report:
			alpha = image.getchannel("A")
			corners = [
				alpha.getpixel((0, 0)),
				alpha.getpixel((expected[0] - 1, 0)),
				alpha.getpixel((0, expected[1] - 1)),
				alpha.getpixel((expected[0] - 1, expected[1] - 1)),
			]
			if any(corners):
				raise RuntimeError(f"Report-card corners are not transparent: {png} -> {corners}")
		width, height, _flags, bits, masks = parse_dds(dds)
		if (width, height) != expected or bits != 32 or masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
			raise RuntimeError(f"Unexpected DDS format for {dds}: {(width, height, bits, masks)}")
		dds_image = Image.open(dds).convert("RGBA")
		if ImageChops.difference(image, dds_image).getbbox() is not None:
			raise RuntimeError(f"DDS pixels differ from the processed PNG: {dds}")

	source_paths = [SOURCE / f"{stem}_source.png" for stem in (*REPORT_STEMS, *SUPER_STEMS)]
	if len({sha256(path) for path in source_paths}) != len(source_paths):
		raise RuntimeError("Generated source artwork is not unique across all 17 identities")
	processed_paths = [PROCESSED / f"{stem}.png" for stem in (*REPORT_STEMS, *SUPER_STEMS)]
	if len({sha256(path) for path in processed_paths}) != len(processed_paths):
		raise RuntimeError("Processed artwork is not unique across all 17 identities")

	print(f"validated {len(REPORT_STEMS)} report cards and {len(SUPER_STEMS)} super-event images")
	print("all DDS outputs are one-mip 32-bit BGRA with pixel identity to processed PNG")
	print("all report-card corner pixels are transparent")
	print("all 17 source and processed SHA-256 hashes are unique")


def main() -> None:
	ensure_dirs()
	processor = find_verified_report_processor()
	run_report_processing(processor)
	process_super_events()
	make_review_files()
	convert_dds()
	validate()
	print(f"verified report processor: {processor}")
	print(f"report processor sha256: {sha256(processor)}")


if __name__ == "__main__":
	main()
