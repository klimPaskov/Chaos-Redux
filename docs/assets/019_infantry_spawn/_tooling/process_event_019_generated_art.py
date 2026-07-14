#!/usr/bin/env python3
"""Process and validate the generated raster tranche for Event 019."""

from __future__ import annotations

import hashlib
import math
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "019_infantry_spawn"
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
ANIMATIONS = PACKAGE / "animations"

REPORT_RUNTIME = ROOT / "gfx" / "event_pictures" / "019_infantry_spawn"
LEADER_RUNTIME = ROOT / "gfx" / "leaders" / "019_infantry_spawn"
UI_RUNTIME = ROOT / "gfx" / "interface" / "019_infantry_spawn"

REPORT_PROCESSOR = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py"
REPORT_PROCESSOR_SHA256 = "5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9"
CHROMA_REMOVER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"

REPORT_STEMS = (
	"report_event_019_infantry_spawn_manifestation",
	"report_event_019_infantry_spawn_organized",
	"report_event_019_infantry_spawn_arsenal",
	"report_event_019_infantry_spawn_claimant",
	"report_event_019_infantry_spawn_anomalous",
	"report_event_019_infantry_spawn_zombie_release",
	"report_event_019_infantry_spawn_zombie_defeat",
	"report_event_019_infantry_spawn_ghost_release",
	"report_event_019_infantry_spawn_ghost_defeat",
	"report_event_019_infantry_spawn_golem_release",
	"report_event_019_infantry_spawn_golem_defeat",
)

CLAIMANT_STEMS = tuple(f"portrait_019_claimant_{index:02d}" for index in range(1, 21))
DERIVATIVE_STEMS = (
	"portrait_019_zombie_host_commander",
	"portrait_019_zombie_host_council",
	"portrait_019_ghost_host_commander",
	"portrait_019_ghost_host_council",
	"portrait_019_golem_master_builder",
	"portrait_019_golem_pattern_council",
)
PORTRAIT_STEMS = CLAIMANT_STEMS + DERIVATIVE_STEMS

ANIMATION_SPECS = {
	"muster_seal_pulse": {"frames": 8, "size": (64, 64), "fps": 8},
	"critical_command_border": {"frames": 8, "size": (156, 210), "fps": 6},
	"anomalous_registry_emblem": {"frames": 10, "size": (64, 64), "fps": 5},
}


def sha256(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure_prerequisites() -> None:
	if not REPORT_PROCESSOR.is_file() or sha256(REPORT_PROCESSOR) != REPORT_PROCESSOR_SHA256:
		raise RuntimeError("Verified report-card processor is missing or changed")
	if not CHROMA_REMOVER.is_file():
		raise RuntimeError(f"Official imagegen chroma remover is missing: {CHROMA_REMOVER}")
	if not CONVERTER.is_file():
		raise RuntimeError(f"Repository DDS converter is missing: {CONVERTER}")


def ensure_dirs() -> None:
	for path in (
		PROCESSED / "report",
		PROCESSED / "portraits" / "claimants",
		PROCESSED / "portraits" / "derivatives",
		CONTACT,
		REPORT_RUNTIME,
		LEADER_RUNTIME,
		UI_RUNTIME,
	):
		path.mkdir(parents=True, exist_ok=True)
	for slug in ANIMATION_SPECS:
		for child in ("keyed_frames", "processed_frames", "sheets", "previews"):
			(ANIMATIONS / slug / child).mkdir(parents=True, exist_ok=True)


def cover_crop(image: Image.Image, target_size: tuple[int, int]) -> Image.Image:
	target_width, target_height = target_size
	scale = max(target_width / image.width, target_height / image.height)
	resized = image.resize(
		(int(round(image.width * scale)), int(round(image.height * scale))),
		Image.Resampling.LANCZOS,
	)
	left = (resized.width - target_width) // 2
	top = (resized.height - target_height) // 2
	return resized.crop((left, top, left + target_width, top + target_height))


def process_reports() -> None:
	for index, stem in enumerate(REPORT_STEMS):
		source = SOURCE / "report" / f"{stem}_source.png"
		output = PROCESSED / "report" / f"{stem}.png"
		command = [
			sys.executable,
			str(REPORT_PROCESSOR),
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
			"--seed", str(19001 + index),
			"--rotate-supersample", "4",
			"--edge-soften", "0.35",
		]
		subprocess.run(command, cwd=ROOT, check=True)


def portrait_treatment(source: Path) -> Image.Image:
	image = Image.open(source).convert("RGB")
	image = cover_crop(image, (156, 210))
	image = ImageEnhance.Contrast(image).enhance(1.04)
	image = ImageEnhance.Color(image).enhance(0.90)
	image = ImageEnhance.Sharpness(image).enhance(1.04)
	return image


def process_portraits() -> None:
	for stem in CLAIMANT_STEMS:
		portrait_treatment(SOURCE / "portraits" / "claimants" / f"{stem}_source.png").save(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png"
		)
	for stem in DERIVATIVE_STEMS:
		portrait_treatment(SOURCE / "portraits" / "derivatives" / f"{stem}_source.png").save(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png"
		)


def remove_chroma(source: Path, output: Path) -> None:
	command = [
		sys.executable,
		str(CHROMA_REMOVER),
		"--input", str(source),
		"--out", str(output),
		"--auto-key", "border",
		"--soft-matte",
		"--transparent-threshold", "12",
		"--opaque-threshold", "220",
		"--despill",
		"--edge-contract", "1",
		"--force",
	]
	subprocess.run(command, cwd=ROOT, check=True)


def normalize_alpha_subject(image: Image.Image, target: tuple[int, int], padding: int) -> Image.Image:
	image = image.convert("RGBA")
	bbox = image.getchannel("A").getbbox()
	if bbox is None:
		raise RuntimeError("Chroma removal produced an empty frame")
	subject = image.crop(bbox)
	available_width = target[0] - (padding * 2)
	available_height = target[1] - (padding * 2)
	scale = min(available_width / subject.width, available_height / subject.height)
	subject = subject.resize(
		(max(1, int(round(subject.width * scale))), max(1, int(round(subject.height * scale)))),
		Image.Resampling.LANCZOS,
	)
	canvas = Image.new("RGBA", target, (0, 0, 0, 0))
	x = (target[0] - subject.width) // 2
	y = (target[1] - subject.height) // 2
	canvas.alpha_composite(subject, (x, y))
	return canvas


def process_animations() -> None:
	for slug, spec in ANIMATION_SPECS.items():
		animation = ANIMATIONS / slug
		frames: list[Image.Image] = []
		for index in range(spec["frames"]):
			source = animation / "source_frames" / f"{slug}_{index:03d}_source.png"
			keyed = animation / "keyed_frames" / f"{slug}_{index:03d}_keyed.png"
			processed = animation / "processed_frames" / f"{slug}_{index:03d}.png"
			remove_chroma(source, keyed)
			padding = 1 if slug == "critical_command_border" else 3
			frame = normalize_alpha_subject(Image.open(keyed), spec["size"], padding)
			frame.save(processed)
			frames.append(frame)

		sheet = Image.new("RGBA", (spec["size"][0] * spec["frames"], spec["size"][1]), (0, 0, 0, 0))
		for index, frame in enumerate(frames):
			sheet.alpha_composite(frame, (index * spec["size"][0], 0))
		sheet.save(animation / "sheets" / f"{slug}_sheet.png")
		frames[0].save(animation / "sheets" / f"{slug}_static.png")
		frames[0].save(
			animation / "previews" / f"{slug}_preview.gif",
			save_all=True,
			append_images=frames[1:],
			duration=int(round(1000 / spec["fps"])),
			loop=0,
			disposal=2,
		)


def checker_preview(image: Image.Image) -> Image.Image:
	image = image.convert("RGBA")
	checker = Image.new("RGB", image.size, (54, 54, 54))
	draw = ImageDraw.Draw(checker)
	cell = 8
	for y in range(0, image.height, cell):
		for x in range(0, image.width, cell):
			if ((x // cell) + (y // cell)) % 2:
				draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(94, 94, 94))
	checker.paste(image, mask=image.getchannel("A"))
	return checker


def make_contact_sheet(
	items: list[tuple[str, Path]],
	output: Path,
	columns: int,
	preview_size: tuple[int, int],
	checker: bool = False,
) -> None:
	rows = math.ceil(len(items) / columns)
	cell_width = preview_size[0] + 24
	cell_height = preview_size[1] + 48
	sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (24, 24, 24))
	draw = ImageDraw.Draw(sheet)
	for index, (label, path) in enumerate(items):
		image = Image.open(path).convert("RGBA")
		image.thumbnail(preview_size, Image.Resampling.LANCZOS)
		if checker:
			preview = checker_preview(image)
		else:
			preview = Image.new("RGB", image.size, (18, 18, 18))
			preview.paste(image, mask=image.getchannel("A"))
		x0 = (index % columns) * cell_width + (cell_width - preview.width) // 2
		y0 = (index // columns) * cell_height + 8
		sheet.paste(preview, (x0, y0))
		draw.text(((index % columns) * cell_width + 8, y0 + preview.height + 8), label, fill=(235, 235, 235))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def make_contacts() -> None:
	make_contact_sheet(
		[(stem, SOURCE / "report" / f"{stem}_source.png") for stem in REPORT_STEMS],
		CONTACT / "event_019_report_source_contact_sheet.png",
		columns=3,
		preview_size=(384, 256),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "report" / f"{stem}.png") for stem in REPORT_STEMS],
		CONTACT / "event_019_report_processed_contact_sheet.png",
		columns=4,
		preview_size=(315, 264),
		checker=True,
	)
	make_contact_sheet(
		[(stem, SOURCE / "portraits" / "claimants" / f"{stem}_source.png") for stem in CLAIMANT_STEMS],
		CONTACT / "event_019_claimant_source_contact_sheet.png",
		columns=5,
		preview_size=(234, 315),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "portraits" / "claimants" / f"{stem}.png") for stem in CLAIMANT_STEMS],
		CONTACT / "event_019_claimant_processed_contact_sheet.png",
		columns=5,
		preview_size=(156, 210),
	)
	make_contact_sheet(
		[(stem, PROCESSED / "portraits" / "derivatives" / f"{stem}.png") for stem in DERIVATIVE_STEMS],
		CONTACT / "event_019_derivative_portrait_contact_sheet.png",
		columns=3,
		preview_size=(234, 315),
	)
	for slug, spec in ANIMATION_SPECS.items():
		items = [
			(f"{slug}_{index:03d}", ANIMATIONS / slug / "processed_frames" / f"{slug}_{index:03d}.png")
			for index in range(spec["frames"])
		]
		make_contact_sheet(
			items,
			ANIMATIONS / slug / "previews" / f"{slug}_contact.png",
			columns=5 if spec["frames"] == 10 else 4,
			preview_size=spec["size"],
			checker=True,
		)


def convert_dds(source: Path, output: Path, size: tuple[int, int]) -> None:
	command = [
		sys.executable,
		str(CONVERTER),
		"--input", str(source),
		"--output", str(output),
		"--width", str(size[0]),
		"--height", str(size[1]),
	]
	subprocess.run(command, cwd=ROOT, check=True)


def convert_all() -> None:
	for stem in REPORT_STEMS:
		convert_dds(PROCESSED / "report" / f"{stem}.png", REPORT_RUNTIME / f"{stem}.dds", (210, 176))
	for stem in CLAIMANT_STEMS:
		convert_dds(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in DERIVATIVE_STEMS:
		convert_dds(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for slug, spec in ANIMATION_SPECS.items():
		convert_dds(
			ANIMATIONS / slug / "sheets" / f"{slug}_sheet.png",
			UI_RUNTIME / f"{slug}_sheet.dds",
			(spec["size"][0] * spec["frames"], spec["size"][1]),
		)
		convert_dds(
			ANIMATIONS / slug / "sheets" / f"{slug}_static.png",
			UI_RUNTIME / f"{slug}_static.dds",
			spec["size"],
		)


def parse_dds(path: Path) -> tuple[int, int, int, int, int, tuple[int, int, int, int], int]:
	data = path.read_bytes()
	if len(data) < 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	values = struct.unpack("<31I", data[4:128])
	return (
		values[3],
		values[2],
		values[6],
		values[19],
		values[21],
		(values[22], values[23], values[24], values[25]),
		len(data),
	)


def validate_dds_pair(png: Path, dds: Path, expected: tuple[int, int]) -> None:
	image = Image.open(png).convert("RGBA")
	if image.size != expected:
		raise RuntimeError(f"Wrong PNG size: {png} -> {image.size}; expected {expected}")
	width, height, mip_count, pixel_flags, bits, masks, file_length = parse_dds(dds)
	if (width, height) != expected:
		raise RuntimeError(f"Wrong DDS size: {dds} -> {(width, height)}; expected {expected}")
	if mip_count not in (0, 1):
		raise RuntimeError(f"Unexpected DDS mip count: {dds} -> {mip_count}")
	if pixel_flags != 65 or bits != 32:
		raise RuntimeError(f"Unexpected DDS pixel format: {dds} -> flags={pixel_flags}, bits={bits}")
	if masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
		raise RuntimeError(f"Unexpected DDS masks: {dds} -> {masks}")
	if file_length != 128 + expected[0] * expected[1] * 4:
		raise RuntimeError(f"Unexpected DDS file length: {dds} -> {file_length}")
	dds_image = Image.open(dds).convert("RGBA")
	if ImageChops.difference(image, dds_image).getbbox() is not None:
		raise RuntimeError(f"DDS pixels differ from processed PNG: {dds}")


def validate() -> None:
	for stem in REPORT_STEMS:
		png = PROCESSED / "report" / f"{stem}.png"
		image = Image.open(png).convert("RGBA")
		corners = [image.getpixel(point)[3] for point in ((0, 0), (209, 0), (0, 175), (209, 175))]
		if any(corners):
			raise RuntimeError(f"Report corners are not transparent: {png} -> {corners}")
		validate_dds_pair(png, REPORT_RUNTIME / f"{stem}.dds", (210, 176))

	for stem in CLAIMANT_STEMS:
		validate_dds_pair(
			PROCESSED / "portraits" / "claimants" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)
	for stem in DERIVATIVE_STEMS:
		validate_dds_pair(
			PROCESSED / "portraits" / "derivatives" / f"{stem}.png",
			LEADER_RUNTIME / f"{stem}.dds",
			(156, 210),
		)

	if len({sha256(SOURCE / "portraits" / "claimants" / f"{stem}_source.png") for stem in CLAIMANT_STEMS}) != 20:
		raise RuntimeError("Claimant source portraits are not all distinct")
	if len({sha256(SOURCE / "report" / f"{stem}_source.png") for stem in REPORT_STEMS}) != len(REPORT_STEMS):
		raise RuntimeError("Report sources are not all distinct")

	for slug, spec in ANIMATION_SPECS.items():
		source_frames = [ANIMATIONS / slug / "source_frames" / f"{slug}_{index:03d}_source.png" for index in range(spec["frames"])]
		processed_frames = [ANIMATIONS / slug / "processed_frames" / f"{slug}_{index:03d}.png" for index in range(spec["frames"])]
		if len({sha256(path) for path in source_frames}) != spec["frames"]:
			raise RuntimeError(f"Animation source frames are not distinct: {slug}")
		if len({sha256(path) for path in processed_frames}) != spec["frames"]:
			raise RuntimeError(f"Animation processed frames are not distinct: {slug}")
		for path in processed_frames:
			image = Image.open(path).convert("RGBA")
			if image.size != spec["size"]:
				raise RuntimeError(f"Wrong frame size: {path} -> {image.size}")
			alpha = image.getchannel("A")
			if alpha.getextrema()[0] != 0 or alpha.getextrema()[1] == 0:
				raise RuntimeError(f"Animation frame lacks useful transparency: {path} -> {alpha.getextrema()}")
		sheet_size = (spec["size"][0] * spec["frames"], spec["size"][1])
		validate_dds_pair(
			ANIMATIONS / slug / "sheets" / f"{slug}_sheet.png",
			UI_RUNTIME / f"{slug}_sheet.dds",
			sheet_size,
		)
		validate_dds_pair(
			ANIMATIONS / slug / "sheets" / f"{slug}_static.png",
			UI_RUNTIME / f"{slug}_static.dds",
			spec["size"],
		)
		gif = Image.open(ANIMATIONS / slug / "previews" / f"{slug}_preview.gif")
		if getattr(gif, "n_frames", 1) != spec["frames"]:
			raise RuntimeError(f"Wrong preview frame count: {slug}")

	print(f"validated {len(REPORT_STEMS)} report-event images")
	print(f"validated {len(CLAIMANT_STEMS)} claimant portraits and {len(DERIVATIVE_STEMS)} derivative portraits")
	print("validated three real-source-frame animations, static fallbacks, sheets, GIFs, alpha, and DDS headers")


def main() -> None:
	ensure_prerequisites()
	ensure_dirs()
	process_reports()
	process_portraits()
	process_animations()
	make_contacts()
	convert_all()
	validate()


if __name__ == "__main__":
	main()
