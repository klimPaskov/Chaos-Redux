#!/usr/bin/env python3
"""Process and validate the complete generated raster package for Event 018."""

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
PACKAGE = ROOT / "docs" / "assets" / "018_resources_found"
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
ANIMATION = PACKAGE / "animations" / "portrait_dho_vhorruk"

REPORT_RUNTIME = ROOT / "gfx" / "event_pictures" / "018_resources_found"
NEWS_RUNTIME = ROOT / "gfx" / "event_pictures" / "news" / "018_resources_found"
SUPER_RUNTIME = ROOT / "gfx" / "super_events" / "018_resources_found"
LEADER_RUNTIME = ROOT / "gfx" / "leaders" / "018_resources_found"
FLAG_RUNTIME = ROOT / "gfx" / "flags"

REPORT_PROCESSOR_SHA256 = "5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9"
REPORT_PROCESSOR_CANDIDATES = (
	ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py",
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/360d/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
	Path("C:/Users/klimp/.codex.broken-20260627-113153/worktrees/7654/chaos_redux/.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"),
)

REPORT_STEMS = (
	"report_event_018_resource_discovery",
	"report_event_018_compound_field",
	"report_event_018_sick_workings",
	"report_event_018_missing_shift",
	"report_event_018_first_evidence",
	"report_event_018_perimeter_breach",
	"report_event_018_evacuation",
	"report_event_018_monster_hunt",
	"report_event_018_full_seal",
	"report_event_018_anchor_cleanup",
)

NEWS_STEMS = (
	"news_event_018_global_resource_field",
	"news_event_018_border_crisis",
	"news_event_018_public_attack",
	"news_event_018_cave_country_emergence",
	"news_event_018_regional_containment",
	"news_event_018_global_defeat",
)

SUPER_STEMS = (
	"super_event_018_cave_emergence",
	"super_event_018_world_end",
	"super_event_018_global_defeat",
)

PORTRAIT_STEMS = (
	"portrait_DHO_vhorruk",
	"portrait_DHO_thessik",
	"portrait_DHO_orrukesh",
	"portrait_DHO_khalvek",
)

COMMANDER_STEMS = (
	"portrait_DHO_thessik",
	"portrait_DHO_orrukesh",
	"portrait_DHO_khalvek",
)

FLAG_STEMS = (
	"DHO",
	"DHO_democratic",
	"DHO_fascism",
	"DHO_communism",
	"DHO_neutrality",
	"DHO_WORLD_BELOW",
)

FLAG_SIZES = {
	"root": (82, 52),
	"medium": (41, 26),
	"small": (10, 7),
}


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def find_verified_report_processor() -> Path:
	for path in REPORT_PROCESSOR_CANDIDATES:
		if path.is_file() and sha256(path) == REPORT_PROCESSOR_SHA256:
			return path
	raise RuntimeError(
		"The verified report-card processor is unavailable or its SHA-256 differs; "
		"refusing to substitute a fallback workflow."
	)


def ensure_dirs() -> None:
	paths = (
		PROCESSED / "report",
		PROCESSED / "news",
		PROCESSED / "super_events",
		PROCESSED / "portraits",
		PROCESSED / "flags",
		CONTACT,
		ANIMATION / "processed_frames",
		ANIMATION / "sheets",
		ANIMATION / "previews",
		REPORT_RUNTIME,
		NEWS_RUNTIME,
		SUPER_RUNTIME,
		LEADER_RUNTIME,
		FLAG_RUNTIME,
		FLAG_RUNTIME / "medium",
		FLAG_RUNTIME / "small",
	)
	for path in paths:
		path.mkdir(parents=True, exist_ok=True)


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


def run_report_processing(processor: Path) -> None:
	for index, stem in enumerate(REPORT_STEMS):
		source = SOURCE / "report" / f"{stem}_source.png"
		output = PROCESSED / "report" / f"{stem}.png"
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
			"--seed", str(18101 + index),
			"--rotate-supersample", "4",
			"--edge-soften", "0.35",
		]
		subprocess.run(command, cwd=ROOT, check=True)


def process_news() -> None:
	for index, stem in enumerate(NEWS_STEMS):
		source = Image.open(SOURCE / "news" / f"{stem}_source.png").convert("RGB")
		image = cover_crop(source, (397, 153))
		image = ImageOps.autocontrast(image, cutoff=1)
		image = ImageEnhance.Contrast(image).enhance(1.12)
		image = ImageEnhance.Sharpness(image).enhance(1.05)
		image = add_monochrome_grain(image, strength=3, seed=18201 + index)
		image.save(PROCESSED / "news" / f"{stem}.png")


def process_super_events() -> None:
	for index, stem in enumerate(SUPER_STEMS):
		source = Image.open(SOURCE / "super_events" / f"{stem}_source.png").convert("RGB")
		image = cover_crop(source, (457, 328))
		image = ImageOps.autocontrast(image, cutoff=1)
		image = ImageEnhance.Contrast(image).enhance(1.08)
		image = ImageEnhance.Brightness(image).enhance(0.98)
		image = ImageEnhance.Sharpness(image).enhance(1.04)
		image = add_monochrome_grain(image, strength=2, seed=18301 + index).convert("RGB")
		image.save(PROCESSED / "super_events" / f"{stem}.png")


def portrait_treatment(source: Path) -> Image.Image:
	image = Image.open(source).convert("RGB")
	image = cover_crop(image, (156, 210))
	image = ImageEnhance.Contrast(image).enhance(1.04)
	image = ImageEnhance.Color(image).enhance(0.92)
	image = ImageEnhance.Sharpness(image).enhance(1.04)
	return image


def process_portraits() -> None:
	for stem in PORTRAIT_STEMS:
		image = portrait_treatment(SOURCE / "portraits" / f"{stem}_source.png")
		image.save(PROCESSED / "portraits" / f"{stem}.png")
		if stem in COMMANDER_STEMS:
			small = image.resize((50, 67), Image.Resampling.LANCZOS)
			small.save(PROCESSED / "portraits" / f"{stem}_small.png")


def process_animation() -> None:
	frames: list[Image.Image] = []
	for frame_number in range(1, 9):
		source = ANIMATION / "source_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}_source.png"
		frame = portrait_treatment(source)
		output = ANIMATION / "processed_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}.png"
		frame.save(output)
		frames.append(frame)

	sheet = Image.new("RGB", (156 * len(frames), 210), (0, 0, 0))
	for index, frame in enumerate(frames):
		sheet.paste(frame, (156 * index, 0))
	sheet.save(ANIMATION / "sheets" / "portrait_DHO_vhorruk_sheet.png")

	gif_frames = [frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=256) for frame in frames]
	gif_frames[0].save(
		ANIMATION / "previews" / "portrait_DHO_vhorruk_preview.gif",
		save_all=True,
		append_images=gif_frames[1:],
		duration=250,
		loop=0,
		disposal=2,
		optimize=False,
	)


def process_flags() -> None:
	for stem in FLAG_STEMS:
		source = Image.open(SOURCE / "flags" / f"{stem}_source.png").convert("RGB")
		root = cover_crop(source, FLAG_SIZES["root"])
		root = ImageOps.autocontrast(root, cutoff=0.25)
		root = ImageEnhance.Contrast(root).enhance(1.08)
		root.save(PROCESSED / "flags" / f"{stem}_82x52.png")
		medium = root.resize(FLAG_SIZES["medium"], Image.Resampling.LANCZOS)
		medium.save(PROCESSED / "flags" / f"{stem}_41x26.png")
		small = root.resize(FLAG_SIZES["small"], Image.Resampling.LANCZOS)
		small.save(PROCESSED / "flags" / f"{stem}_10x7.png")


def write_tga(path: Path, image: Image.Image) -> None:
	"""Write an uncompressed 32-bit BGRA TGA with bottom-left origin."""
	image = image.convert("RGBA")
	header = struct.pack(
		"<BBBHHBHHHHBB",
		0,
		0,
		2,
		0,
		0,
		0,
		0,
		0,
		image.width,
		image.height,
		32,
		8,
	)
	pixels = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).tobytes("raw", "BGRA")
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_bytes(header + pixels)


def export_flags() -> None:
	for stem in FLAG_STEMS:
		root = Image.open(PROCESSED / "flags" / f"{stem}_82x52.png")
		medium = Image.open(PROCESSED / "flags" / f"{stem}_41x26.png")
		small = Image.open(PROCESSED / "flags" / f"{stem}_10x7.png")
		write_tga(FLAG_RUNTIME / f"{stem}.tga", root)
		write_tga(FLAG_RUNTIME / "medium" / f"{stem}.tga", medium)
		write_tga(FLAG_RUNTIME / "small" / f"{stem}.tga", small)


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
	checkerboard: bool = False,
) -> None:
	padding = 16
	label_height = 34
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
		background = checker(preview_size) if checkerboard else Image.new("RGB", preview_size, (224, 224, 224))
		background.paste(image, ((preview_size[0] - image.width) // 2, (preview_size[1] - image.height) // 2), image)
		sheet.paste(background, (x0, y0))
		draw.text((x0, y0 + preview_size[1] + 8), label, fill=(245, 245, 245))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def make_flag_contact_sheet() -> None:
	cell_width = 360
	cell_height = 170
	sheet = Image.new("RGB", (cell_width * 3, cell_height * len(FLAG_STEMS)), (24, 24, 24))
	draw = ImageDraw.Draw(sheet)
	for row, stem in enumerate(FLAG_STEMS):
		for col, (size_name, dimensions) in enumerate(FLAG_SIZES.items()):
			path = PROCESSED / "flags" / f"{stem}_{dimensions[0]}x{dimensions[1]}.png"
			image = Image.open(path).convert("RGB")
			scale = min(12, 280 // image.width, 110 // image.height)
			preview = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
			x0 = col * cell_width
			y0 = row * cell_height
			sheet.paste(preview, (x0 + (cell_width - preview.width) // 2, y0 + 12))
			draw.text((x0 + 14, y0 + 138), f"{stem} / {size_name} / {dimensions[0]}x{dimensions[1]}", fill=(245, 245, 245))
	sheet.save(CONTACT / "event_018_flag_final_sizes_contact_sheet.png")


def make_review_files() -> None:
	make_contact_sheet(
		[(stem, SOURCE / "report" / f"{stem}_source.png") for stem in REPORT_STEMS],
		CONTACT / "event_018_report_source_contact_sheet.png",
		columns=3,
		preview_size=(480, 320),
	)
	make_contact_sheet(
		[(f"{stem} / 210x176", PROCESSED / "report" / f"{stem}.png") for stem in REPORT_STEMS],
		CONTACT / "event_018_report_processed_contact_sheet.png",
		columns=3,
		preview_size=(420, 352),
		checkerboard=True,
	)
	make_contact_sheet(
		[(stem, SOURCE / "news" / f"{stem}_source.png") for stem in NEWS_STEMS],
		CONTACT / "event_018_news_source_contact_sheet.png",
		columns=2,
		preview_size=(640, 320),
	)
	make_contact_sheet(
		[(f"{stem} / 397x153", PROCESSED / "news" / f"{stem}.png") for stem in NEWS_STEMS],
		CONTACT / "event_018_news_processed_contact_sheet.png",
		columns=2,
		preview_size=(596, 230),
	)
	make_contact_sheet(
		[(stem, SOURCE / "super_events" / f"{stem}_source.png") for stem in SUPER_STEMS],
		CONTACT / "event_018_super_event_source_contact_sheet.png",
		columns=3,
		preview_size=(457, 328),
	)
	make_contact_sheet(
		[(f"{stem} / 457x328", PROCESSED / "super_events" / f"{stem}.png") for stem in SUPER_STEMS],
		CONTACT / "event_018_super_event_processed_contact_sheet.png",
		columns=3,
		preview_size=(457, 328),
	)
	make_contact_sheet(
		[(stem, SOURCE / "portraits" / f"{stem}_source.png") for stem in PORTRAIT_STEMS],
		CONTACT / "event_018_portrait_source_contact_sheet.png",
		columns=4,
		preview_size=(260, 390),
	)
	portrait_items = [(f"{stem} / 156x210", PROCESSED / "portraits" / f"{stem}.png") for stem in PORTRAIT_STEMS]
	portrait_items.extend((f"{stem}_small / 50x67", PROCESSED / "portraits" / f"{stem}_small.png") for stem in COMMANDER_STEMS)
	make_contact_sheet(
		portrait_items,
		CONTACT / "event_018_portrait_processed_contact_sheet.png",
		columns=4,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(f"frame {frame_number:02d} source", ANIMATION / "source_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}_source.png") for frame_number in range(1, 9)],
		CONTACT / "event_018_vhorruk_animation_source_contact_sheet.png",
		columns=4,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(f"frame {frame_number:02d} / 156x210", ANIMATION / "processed_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}.png") for frame_number in range(1, 9)],
		CONTACT / "event_018_vhorruk_animation_processed_contact_sheet.png",
		columns=4,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(stem, SOURCE / "flags" / f"{stem}_source.png") for stem in FLAG_STEMS],
		CONTACT / "event_018_flag_source_contact_sheet.png",
		columns=2,
		preview_size=(615, 390),
	)
	make_flag_contact_sheet()

	template_path = ROOT / "gfx" / "super_events" / "super_event_template.psd"
	if template_path.is_file():
		preview_items: list[tuple[str, Path]] = []
		template = Image.open(template_path).convert("RGB")
		for stem in SUPER_STEMS:
			preview = template.copy()
			image = Image.open(PROCESSED / "super_events" / f"{stem}.png").convert("RGB")
			preview.paste(image.resize((455, 326), Image.Resampling.LANCZOS), (409, 106))
			path = CONTACT / f"{stem}_ui_mask_preview.png"
			preview.save(path)
			preview_items.append((stem, path))
		make_contact_sheet(
			preview_items,
			CONTACT / "event_018_super_event_ui_mask_preview_contact_sheet.png",
			columns=2,
			preview_size=(645, 272),
		)


def convert_dds() -> None:
	converter = ROOT / ".tools" / "convert_to_dds.py"
	jobs: list[tuple[Path, Path, tuple[int, int]]] = []
	jobs.extend((PROCESSED / "report" / f"{stem}.png", REPORT_RUNTIME / f"{stem}.dds", (210, 176)) for stem in REPORT_STEMS)
	jobs.extend((PROCESSED / "news" / f"{stem}.png", NEWS_RUNTIME / f"{stem}.dds", (397, 153)) for stem in NEWS_STEMS)
	jobs.extend((PROCESSED / "super_events" / f"{stem}.png", SUPER_RUNTIME / f"{stem}.dds", (457, 328)) for stem in SUPER_STEMS)
	jobs.extend((PROCESSED / "portraits" / f"{stem}.png", LEADER_RUNTIME / f"{stem}.dds", (156, 210)) for stem in PORTRAIT_STEMS)
	jobs.extend((PROCESSED / "portraits" / f"{stem}_small.png", LEADER_RUNTIME / f"{stem}_small.dds", (50, 67)) for stem in COMMANDER_STEMS)
	jobs.append((ANIMATION / "sheets" / "portrait_DHO_vhorruk_sheet.png", LEADER_RUNTIME / "portrait_DHO_vhorruk_animated.dds", (1248, 210)))
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


def parse_dds(path: Path) -> tuple[int, int, int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) < 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	values = struct.unpack("<31I", data[4:128])
	return values[3], values[2], values[6], values[19], values[21], (values[22], values[23], values[24], values[25])


def validate_dds_pair(png: Path, dds: Path, expected: tuple[int, int]) -> None:
	image = Image.open(png).convert("RGBA")
	if image.size != expected:
		raise RuntimeError(f"{png} is {image.size}; expected {expected}")
	width, height, mip_count, _pixel_flags, bits, masks = parse_dds(dds)
	if (width, height) != expected:
		raise RuntimeError(f"Unexpected DDS size for {dds}: {(width, height)}")
	if mip_count not in (0, 1):
		raise RuntimeError(f"Unexpected DDS mip count for {dds}: {mip_count}")
	if bits != 32 or masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
		raise RuntimeError(f"Unexpected DDS pixel format for {dds}: bits={bits}, masks={masks}")
	dds_image = Image.open(dds).convert("RGBA")
	if ImageChops.difference(image, dds_image).getbbox() is not None:
		raise RuntimeError(f"DDS pixels differ from processed PNG: {dds}")


def parse_tga(path: Path) -> tuple[int, int, int, int, int]:
	header = path.read_bytes()[:18]
	if len(header) != 18:
		raise RuntimeError(f"Invalid TGA header: {path}")
	values = struct.unpack("<BBBHHBHHHHBB", header)
	return values[2], values[8], values[9], values[10], values[11]


def validate_tga_pair(png: Path, tga: Path, expected: tuple[int, int]) -> None:
	image_type, width, height, bits, descriptor = parse_tga(tga)
	if (image_type, width, height, bits) != (2, expected[0], expected[1], 32):
		raise RuntimeError(f"Unexpected TGA format for {tga}: {(image_type, width, height, bits)}")
	if descriptor != 8 or descriptor & 0x20:
		raise RuntimeError(f"TGA must have 8 alpha bits and bottom-left origin: {tga}, descriptor={descriptor}")
	png_image = Image.open(png).convert("RGBA")
	tga_image = Image.open(tga).convert("RGBA")
	if ImageChops.difference(png_image, tga_image).getbbox() is not None:
		raise RuntimeError(f"TGA pixels differ from processed PNG: {tga}")


def validate(processor: Path) -> None:
	if sha256(processor) != REPORT_PROCESSOR_SHA256:
		raise RuntimeError("Verified report processor hash changed during processing")

	for stem in REPORT_STEMS:
		png = PROCESSED / "report" / f"{stem}.png"
		image = Image.open(png).convert("RGBA")
		if image.size != (210, 176):
			raise RuntimeError(f"Wrong report dimensions: {png} -> {image.size}")
		alpha = image.getchannel("A")
		corners = [alpha.getpixel((0, 0)), alpha.getpixel((209, 0)), alpha.getpixel((0, 175)), alpha.getpixel((209, 175))]
		if any(corners):
			raise RuntimeError(f"Report corners are not transparent: {png} -> {corners}")
		validate_dds_pair(png, REPORT_RUNTIME / f"{stem}.dds", (210, 176))

	for stem in NEWS_STEMS:
		png = PROCESSED / "news" / f"{stem}.png"
		image = Image.open(png)
		if image.mode != "L" or image.size != (397, 153):
			raise RuntimeError(f"News must be true grayscale L at 397x153: {png} -> {image.mode}, {image.size}")
		validate_dds_pair(png, NEWS_RUNTIME / f"{stem}.dds", (397, 153))

	for stem in SUPER_STEMS:
		validate_dds_pair(PROCESSED / "super_events" / f"{stem}.png", SUPER_RUNTIME / f"{stem}.dds", (457, 328))

	for stem in PORTRAIT_STEMS:
		validate_dds_pair(PROCESSED / "portraits" / f"{stem}.png", LEADER_RUNTIME / f"{stem}.dds", (156, 210))
	for stem in COMMANDER_STEMS:
		validate_dds_pair(PROCESSED / "portraits" / f"{stem}_small.png", LEADER_RUNTIME / f"{stem}_small.dds", (50, 67))
	validate_dds_pair(ANIMATION / "sheets" / "portrait_DHO_vhorruk_sheet.png", LEADER_RUNTIME / "portrait_DHO_vhorruk_animated.dds", (1248, 210))

	for stem in FLAG_STEMS:
		for size_name, expected in FLAG_SIZES.items():
			png = PROCESSED / "flags" / f"{stem}_{expected[0]}x{expected[1]}.png"
			tga_dir = FLAG_RUNTIME if size_name == "root" else FLAG_RUNTIME / size_name
			validate_tga_pair(png, tga_dir / f"{stem}.tga", expected)

	scene_sources = [SOURCE / "report" / f"{stem}_source.png" for stem in REPORT_STEMS]
	scene_sources.extend(SOURCE / "news" / f"{stem}_source.png" for stem in NEWS_STEMS)
	scene_sources.extend(SOURCE / "super_events" / f"{stem}_source.png" for stem in SUPER_STEMS)
	scene_sources.extend(SOURCE / "portraits" / f"{stem}_source.png" for stem in PORTRAIT_STEMS)
	scene_sources.extend(SOURCE / "flags" / f"{stem}_source.png" for stem in FLAG_STEMS)
	if len({sha256(path) for path in scene_sources}) != len(scene_sources):
		raise RuntimeError("A distinct Event 018 scene, portrait, or flag identity reuses source pixels")

	animation_sources = [ANIMATION / "source_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}_source.png" for frame_number in range(1, 9)]
	animation_processed = [ANIMATION / "processed_frames" / f"portrait_DHO_vhorruk_frame_{frame_number:02d}.png" for frame_number in range(1, 9)]
	if len({sha256(path) for path in animation_sources}) != 8:
		raise RuntimeError("Vhorruk animation source frames are not all distinct")
	if len({sha256(path) for path in animation_processed}) != 8:
		raise RuntimeError("Vhorruk processed frames are not all distinct")
	static = Image.open(PROCESSED / "portraits" / "portrait_DHO_vhorruk.png").convert("RGB")
	frame_one = Image.open(animation_processed[0]).convert("RGB")
	if ImageChops.difference(static, frame_one).getbbox() is not None:
		raise RuntimeError("Vhorruk static fallback does not match animation frame 1")

	flag_root_hashes = {sha256(PROCESSED / "flags" / f"{stem}_82x52.png") for stem in FLAG_STEMS}
	if len(flag_root_hashes) != len(FLAG_STEMS):
		raise RuntimeError("DHO flag identities are not visually distinct at 82x52")
	if any((FLAG_RUNTIME / folder / "DHO_WORLD_END.tga").exists() for folder in ("", "medium", "small")):
		raise RuntimeError("Obsolete DHO_WORLD_END final identity remains; expected DHO_WORLD_BELOW")

	preview = Image.open(ANIMATION / "previews" / "portrait_DHO_vhorruk_preview.gif")
	if getattr(preview, "n_frames", 1) != 8:
		raise RuntimeError("Vhorruk preview GIF does not contain 8 frames")

	print(f"validated {len(REPORT_STEMS)} reports, {len(NEWS_STEMS)} news images, {len(SUPER_STEMS)} super-event images")
	print(f"validated {len(PORTRAIT_STEMS)} large portraits, {len(COMMANDER_STEMS)} commander small portraits, and one 8-frame Vhorruk sheet")
	print(f"validated {len(FLAG_STEMS)} flag identities across root/medium/small with 32-bit bottom-origin TGA headers")
	print("all DDS outputs are one-mip 32-bit BGRA and pixel-identical to processed PNG sources")
	print("all 8 Vhorruk source and processed animation frames are distinct; static fallback matches frame 1")


def main() -> None:
	ensure_dirs()
	processor = find_verified_report_processor()
	run_report_processing(processor)
	process_news()
	process_super_events()
	process_portraits()
	process_animation()
	process_flags()
	export_flags()
	make_review_files()
	convert_dds()
	validate(processor)
	print(f"verified report processor: {processor}")
	print(f"report processor sha256: {sha256(processor)}")


if __name__ == "__main__":
	main()
