#!/usr/bin/env python3
"""Finalize the 18 current Event 014 achievement icon triplets."""

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

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "achievement_icon_validation.tsv"
GFX_HANDOFF = PACKAGE / "validation" / "achievement_gfx_handoff.tsv"
LIVE = ROOT / "gfx" / "achievements"
GFX_FILE = ROOT / "interface" / "014_cannibalism_achievements.gfx"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
CHROMA_HELPER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
NOT_ELIGIBLE_OVERLAY = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "assets" / "achievements" / "overlay.png"
SIZE = (64, 64)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def achievement_ids() -> list[str]:
	text = GFX_FILE.read_text(encoding="utf-8-sig")
	paths = re.findall(r'texturefile\s*=\s*"gfx/achievements/([^"]+)\.dds"', text)
	if len(paths) != 54 or len(set(paths)) != 54:
		raise RuntimeError(f"Expected 54 unique registered achievement textures, found {len(paths)} / {len(set(paths))}")
	bases = {re.sub(r"_(?:grey|not_eligible)$", "", path) for path in paths}
	if len(bases) != 18:
		raise RuntimeError(f"Expected 18 current achievement ids, found {len(bases)}")
	for base in bases:
		expected = {base, f"{base}_grey", f"{base}_not_eligible"}
		if not expected.issubset(paths):
			raise RuntimeError(f"Incomplete registered triplet for {base}")
	# Preserve definition order by taking each base at its first registered occurrence.
	ordered: list[str] = []
	for path in paths:
		base = re.sub(r"_(?:grey|not_eligible)$", "", path)
		if base not in ordered:
			ordered.append(base)
	return ordered


def run_chroma(achievement_id: str) -> None:
	source = SOURCE / f"{achievement_id}_source.png"
	alpha = ALPHA / f"{achievement_id}_alpha.png"
	result = subprocess.run(
		[
			sys.executable, str(CHROMA_HELPER), "--input", str(source), "--out", str(alpha),
			"--auto-key", "border", "--soft-matte", "--transparent-threshold", "12",
			"--opaque-threshold", "220", "--despill", "--force",
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"Chroma cleanup failed for {achievement_id}:\n{result.stdout}\n{result.stderr}")


def trim_alpha(image: Image.Image) -> Image.Image:
	rgba = image.convert("RGBA")
	bbox = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0).getbbox()
	if bbox is None:
		raise RuntimeError("No visible achievement artwork after chroma cleanup")
	return rgba.crop(bbox)


def completed_icon(alpha_path: Path) -> Image.Image:
	scale = 4
	size = (SIZE[0] * scale, SIZE[1] * scale)
	# Opaque dark field treatment keeps the generated composition legible at 64 px.
	background = Image.new("RGBA", size, (10, 10, 12, 255))
	pixels = background.load()
	cx, cy = size[0] / 2, size[1] / 2
	for y in range(size[1]):
		for x in range(size[0]):
			distance = min(1.0, math.hypot((x - cx) / cx, (y - cy) / cy))
			red = round(40 - 27 * distance)
			green = round(24 - 13 * distance)
			blue = round(24 - 12 * distance)
			pixels[x, y] = (red, green, blue, 255)
	subject = trim_alpha(Image.open(alpha_path))
	maximum = (232, 232)
	ratio = min(maximum[0] / subject.width, maximum[1] / subject.height)
	subject = subject.resize(
		(max(1, round(subject.width * ratio)), max(1, round(subject.height * ratio))),
		Image.Resampling.LANCZOS,
	)
	x, y = (size[0] - subject.width) // 2, (size[1] - subject.height) // 2
	shadow_alpha = subject.getchannel("A").filter(ImageFilter.GaussianBlur(7)).point(lambda value: round(value * 0.58))
	shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
	shadow.putalpha(shadow_alpha)
	background.alpha_composite(shadow, (x + 4, y + 5))
	background.alpha_composite(subject, (x, y))
	draw = ImageDraw.Draw(background, "RGBA")
	draw.rectangle((0, 0, 255, 255), outline=(4, 4, 5, 255), width=9)
	draw.rectangle((8, 8, 247, 247), outline=(128, 93, 51, 255), width=4)
	draw.rectangle((13, 13, 242, 242), outline=(25, 21, 18, 255), width=4)
	return background.resize(SIZE, Image.Resampling.LANCZOS).convert("RGBA")


def grey_icon(completed: Image.Image) -> Image.Image:
	grey = ImageOps.grayscale(completed.convert("RGB"))
	grey = ImageEnhance.Contrast(grey).enhance(1.08)
	return grey.convert("RGBA")


def load_not_eligible_overlay() -> Image.Image:
	if not NOT_ELIGIBLE_OVERLAY.is_file():
		raise FileNotFoundError(f"Missing mandatory achievement overlay: {NOT_ELIGIBLE_OVERLAY}")
	with Image.open(NOT_ELIGIBLE_OVERLAY) as opened:
		if opened.size != SIZE:
			raise RuntimeError(f"Mandatory achievement overlay must be {SIZE[0]}x{SIZE[1]}: {NOT_ELIGIBLE_OVERLAY}")
		if opened.mode != "RGBA":
			raise RuntimeError(f"Mandatory achievement overlay must be RGBA: {NOT_ELIGIBLE_OVERLAY}")
		return opened.copy()


def not_eligible_icon(grey: Image.Image, overlay: Image.Image) -> Image.Image:
	grey_copy = grey.copy()
	if grey_copy.size != SIZE or grey_copy.mode != "RGBA":
		raise RuntimeError("Grey achievement variant must be a 64x64 RGBA image before overlay compositing")
	return Image.alpha_composite(grey_copy, overlay)


def convert(path: Path) -> None:
	output = DDS_PACKAGE / f"{path.stem}.dds"
	result = subprocess.run(
		[
			sys.executable, str(CONVERTER), "--input", str(path), "--output", str(output),
			"--width", "64", "--height", "64",
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"DDS conversion failed for {path.stem}:\n{result.stdout}\n{result.stderr}")
	shutil.copy2(output, LIVE / output.name)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) != 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS: {path}")
	height = struct.unpack_from("<I", data, 12)[0]
	width = struct.unpack_from("<I", data, 16)[0]
	mip_count = struct.unpack_from("<I", data, 28)[0]
	masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
	return width, height, mip_count, masks


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def make_contact(ids: list[str], folder: Path, suffixes: list[str], output: Path, source: bool = False) -> None:
	columns = 6
	cell_w, cell_h = 215, 165 if source else 135
	preview_size = (112, 112) if source else (76 * len(suffixes), 76)
	rows = math.ceil(len(ids) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (24, 25, 28))
	draw = ImageDraw.Draw(sheet)
	label_font = font(10)
	for index, achievement_id in enumerate(ids):
		x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
		draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(88, 92, 98))
		if source:
			opened = Image.open(folder / f"{achievement_id}_source.png").convert("RGB")
			preview = ImageOps.contain(opened, preview_size, Image.Resampling.LANCZOS)
			plate = Image.new("RGB", preview_size, (45, 47, 50))
			plate.paste(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
			sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 7))
		else:
			strip = Image.new("RGB", preview_size, (45, 47, 50))
			for suffix_index, suffix in enumerate(suffixes):
				image = Image.open(folder / f"{achievement_id}{suffix}").convert("RGB").resize((64, 64), Image.Resampling.NEAREST)
				strip.paste(image, (suffix_index * 76 + 6, 6))
			sheet.paste(strip, (x0 + (cell_w - preview_size[0]) // 2, y0 + 7))
		label = achievement_id.removeprefix("014_cannibalism_")
		ly = y0 + (123 if source else 88)
		for line in textwrap.wrap(label, width=28)[:3]:
			draw.text((x0 + 8, ly), line, font=label_font, fill=(235, 235, 235))
			ly += 11
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def main() -> None:
	ids = achievement_ids()
	overlay = load_not_eligible_overlay()
	for directory in (ALPHA, PROCESSED, DDS_PACKAGE, CONTACT, VALIDATION.parent, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [achievement_id for achievement_id in ids if not (SOURCE / f"{achievement_id}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing achievement sources:\n" + "\n".join(missing))
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(run_chroma, ids))
	for achievement_id in ids:
		completed = completed_icon(ALPHA / f"{achievement_id}_alpha.png")
		grey = grey_icon(completed)
		not_eligible = not_eligible_icon(grey, overlay)
		if not_eligible.tobytes() != Image.alpha_composite(grey.copy(), overlay).tobytes():
			raise RuntimeError(f"Not-eligible variant is not an exact grey-copy overlay composite: {achievement_id}")
		completed.save(PROCESSED / f"{achievement_id}.png", optimize=True)
		grey.save(PROCESSED / f"{achievement_id}_grey.png", optimize=True)
		not_eligible.save(PROCESSED / f"{achievement_id}_not_eligible.png", optimize=True)
	processed_paths = sorted(PROCESSED.glob("*.png"))
	if len(processed_paths) != 54:
		raise RuntimeError(f"Expected 54 processed variants, found {len(processed_paths)}")
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(convert, processed_paths))
	make_contact(ids, SOURCE, [], CONTACT / "achievement_source_contact_sheet.png", source=True)
	make_contact(ids, PROCESSED, [".png", "_grey.png", "_not_eligible.png"], CONTACT / "achievement_final_variants_contact_sheet.png")
	make_contact(ids, LIVE, [".dds", "_grey.dds", "_not_eligible.dds"], CONTACT / "achievement_dds_decoded_contact_sheet.png")
	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	completed_hashes: dict[str, str] = {}
	rows: list[list[str]] = []
	for achievement_id in ids:
		for variant in ("", "_grey", "_not_eligible"):
			stem = f"{achievement_id}{variant}"
			png = PROCESSED / f"{stem}.png"
			package_dds = DDS_PACKAGE / f"{stem}.dds"
			live_dds = LIVE / f"{stem}.dds"
			image = Image.open(png).convert("RGBA")
			if image.size != SIZE or image.getchannel("A").getextrema() != (255, 255):
				raise RuntimeError(f"Invalid opaque achievement PNG: {stem}")
			if variant == "_grey":
				rgb_bytes = image.convert("RGB").tobytes()
				for index in range(0, len(rgb_bytes), 3):
					if rgb_bytes[index] != rgb_bytes[index + 1] or rgb_bytes[index + 1] != rgb_bytes[index + 2]:
						raise RuntimeError(f"Grey variant is not monochrome: {stem}")
			if variant == "_not_eligible":
				rgba_bytes = image.tobytes()
				red_pixels = sum(
					1 for index in range(0, len(rgba_bytes), 4)
					if rgba_bytes[index] > 130
					and rgba_bytes[index] > rgba_bytes[index + 1] * 1.55
					and rgba_bytes[index] > rgba_bytes[index + 2] * 1.45
				)
				if red_pixels < 120:
					raise RuntimeError(f"Not-eligible overlay is not visibly red: {stem}")
			else:
				red_pixels = 0
			if variant == "":
				normalized = hashlib.sha256(image.tobytes()).hexdigest()
				if normalized in completed_hashes:
					raise RuntimeError(f"Duplicate completed icon: {achievement_id} duplicates {completed_hashes[normalized]}")
				completed_hashes[normalized] = achievement_id
			else:
				normalized = "derived"
			width, height, mip_count, masks = dds_header(live_dds)
			if (width, height) != SIZE or mip_count not in (0, 1) or masks != expected_masks:
				raise RuntimeError(f"Invalid achievement DDS: {stem}")
			if sha256(package_dds) != sha256(live_dds):
				raise RuntimeError(f"Runtime DDS differs from package DDS: {stem}")
			rows.append([
				achievement_id, variant or "completed", SOURCE.joinpath(f"{achievement_id}_source.png").as_posix(),
				sha256(SOURCE / f"{achievement_id}_source.png"), png.as_posix(), sha256(png),
				package_dds.as_posix(), sha256(package_dds), live_dds.relative_to(ROOT).as_posix(),
				sha256(live_dds), str(live_dds.stat().st_size), str(red_pixels), normalized, "complete",
			])
	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow([
			"achievement_id", "variant", "source", "source_sha256", "processed_png", "processed_sha256",
			"package_dds", "package_dds_sha256", "runtime_dds", "runtime_dds_sha256",
			"runtime_dds_bytes", "red_overlay_pixels", "normalized_rgba_sha256", "status",
		])
		writer.writerows(rows)
	with GFX_HANDOFF.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow(["achievement_id", "completed_sprite", "grey_sprite", "not_eligible_sprite", "runtime_stem", "status"])
		for achievement_id in ids:
			writer.writerow([
				achievement_id,
				f"GFX_achievement_{achievement_id}",
				f"GFX_achievement_{achievement_id}_grey",
				f"GFX_achievement_{achievement_id}_not_eligible",
				f"gfx/achievements/{achievement_id}",
				"ready",
			])
	print(f"Processed and validated {len(ids)} achievement masters and {len(rows)} runtime variants")


if __name__ == "__main__":
	main()
