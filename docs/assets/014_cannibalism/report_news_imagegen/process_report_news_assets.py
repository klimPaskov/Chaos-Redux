#!/usr/bin/env python3
"""Finalize the eight Event 014 aftermath, Wendigo report, and news images."""

from __future__ import annotations

import csv
import hashlib
import math
import shutil
import struct
import subprocess
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACTS = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "report_news_asset_validation.tsv"
GFX_HANDOFF = PACKAGE / "validation" / "report_news_gfx_handoff.tsv"
LIVE = ROOT / "gfx" / "event_pictures" / "014_cannibalism"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"


@dataclass(frozen=True)
class Asset:
	stem: str
	asset_type: str
	size: tuple[int, int]
	sprite: str
	centering: tuple[float, float] = (0.5, 0.5)


ASSETS = (
	Asset("report_event_cannibalism_captured_warlord", "report", (210, 176), "GFX_report_event_cannibalism_captured_warlord", (0.5, 0.46)),
	Asset("report_event_cannibalism_captured_hannibal", "report", (210, 176), "GFX_report_event_cannibalism_captured_hannibal", (0.5, 0.44)),
	Asset("report_event_cannibalism_wendigo_reveal", "report", (210, 176), "GFX_report_event_cannibalism_wendigo_reveal", (0.5, 0.48)),
	Asset("report_event_cannibalism_wendigo_winter_network", "report", (210, 176), "GFX_report_event_cannibalism_wendigo_winter_network", (0.5, 0.5)),
	Asset("report_event_cannibalism_wendigo_countdown", "report", (210, 176), "GFX_report_event_cannibalism_wendigo_countdown", (0.5, 0.5)),
	Asset("report_event_cannibalism_wendigo_transformation_broken", "report", (210, 176), "GFX_report_event_cannibalism_wendigo_transformation_broken", (0.5, 0.51)),
	Asset("report_event_cannibalism_wendigo_anchor_assault", "report", (210, 176), "GFX_report_event_cannibalism_wendigo_anchor_assault", (0.5, 0.5)),
	Asset("news_cannibalism_wendigo_reveal", "news", (397, 153), "GFX_news_cannibalism_wendigo_reveal", (0.5, 0.48)),
)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def process(asset: Asset) -> Path:
	source = SOURCE / f"{asset.stem}_source.png"
	if not source.exists():
		raise FileNotFoundError(source)
	with Image.open(source) as opened:
		image = ImageOps.exif_transpose(opened).convert("RGB")
		image = ImageOps.fit(image, asset.size, method=Image.Resampling.LANCZOS, centering=asset.centering)
		if asset.asset_type == "news":
			image = ImageOps.grayscale(image)
			image = ImageEnhance.Contrast(image).enhance(1.08)
			image = image.convert("RGB")
		else:
			image = ImageEnhance.Contrast(image).enhance(1.035)
			image = ImageEnhance.Sharpness(image).enhance(1.08)
		image = image.convert("RGBA")
		image.putalpha(255)
	output = PROCESSED / f"{asset.stem}.png"
	image.save(output, optimize=True)
	return output


def convert(asset: Asset) -> None:
	input_path = PROCESSED / f"{asset.stem}.png"
	output_path = DDS_PACKAGE / f"{asset.stem}.dds"
	result = subprocess.run(
		[
			sys.executable,
			str(CONVERTER),
			"--input",
			str(input_path),
			"--output",
			str(output_path),
			"--width",
			str(asset.size[0]),
			"--height",
			str(asset.size[1]),
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"DDS conversion failed for {asset.stem}:\n{result.stdout}\n{result.stderr}")
	shutil.copy2(output_path, LIVE / output_path.name)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) != 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS: {path}")
	height = struct.unpack_from("<I", data, 12)[0]
	width = struct.unpack_from("<I", data, 16)[0]
	mip_count = struct.unpack_from("<I", data, 28)[0]
	masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
	return width, height, mip_count, masks


def make_contact(folder: Path, suffix: str, output: Path, source: bool = False) -> None:
	columns = 4
	cell_w, cell_h = 420, 275
	rows = math.ceil(len(ASSETS) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (22, 23, 25))
	draw = ImageDraw.Draw(sheet)
	label_font = font(15)
	meta_font = font(12)
	for index, asset in enumerate(ASSETS):
		x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
		draw.rectangle((x0 + 5, y0 + 5, x0 + cell_w - 6, y0 + cell_h - 6), outline=(88, 92, 98), width=2)
		path = folder / f"{asset.stem}{suffix}"
		with Image.open(path) as opened:
			image = opened.convert("RGB")
		preview_box = (392, 205)
		preview = ImageOps.contain(image, preview_box, Image.Resampling.LANCZOS)
		plate = Image.new("RGB", preview_box, (43, 45, 48))
		plate.paste(preview, ((preview_box[0] - preview.width) // 2, (preview_box[1] - preview.height) // 2))
		sheet.paste(plate, (x0 + 14, y0 + 13))
		label_y = y0 + 224
		for line in textwrap.wrap(asset.stem, width=48)[:2]:
			draw.text((x0 + 14, label_y), line, font=label_font, fill=(238, 238, 238))
			label_y += 17
		meta = f"{asset.asset_type} | {image.width}x{image.height}"
		draw.text((x0 + 14, y0 + 256), meta, font=meta_font, fill=(166, 170, 176))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def validate() -> None:
	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	rows: list[list[str]] = []
	source_hashes: dict[str, str] = {}
	pixel_hashes: dict[str, str] = {}
	for asset in ASSETS:
		source = SOURCE / f"{asset.stem}_source.png"
		processed = PROCESSED / f"{asset.stem}.png"
		package_dds = DDS_PACKAGE / f"{asset.stem}.dds"
		runtime_dds = LIVE / f"{asset.stem}.dds"
		source_hash = sha256(source)
		if source_hash in source_hashes:
			raise RuntimeError(f"Duplicate generated source: {asset.stem} duplicates {source_hashes[source_hash]}")
		source_hashes[source_hash] = asset.stem
		with Image.open(processed) as opened:
			image = opened.convert("RGBA")
		if image.size != asset.size or image.getchannel("A").getextrema() != (255, 255):
			raise RuntimeError(f"Invalid processed PNG dimensions or opacity: {asset.stem}")
		pixel_hash = hashlib.sha256(image.tobytes()).hexdigest()
		if pixel_hash in pixel_hashes:
			raise RuntimeError(f"Duplicate processed art: {asset.stem} duplicates {pixel_hashes[pixel_hash]}")
		pixel_hashes[pixel_hash] = asset.stem
		monochrome = "no"
		if asset.asset_type == "news":
			pixels = image.convert("RGB").tobytes()
			if any(pixels[index] != pixels[index + 1] or pixels[index + 1] != pixels[index + 2] for index in range(0, len(pixels), 3)):
				raise RuntimeError(f"News art is not true monochrome: {asset.stem}")
			monochrome = "yes"
		width, height, mip_count, masks = dds_header(runtime_dds)
		if (width, height) != asset.size or mip_count not in (0, 1) or masks != expected_masks:
			raise RuntimeError(f"Invalid runtime DDS: {asset.stem}")
		if sha256(package_dds) != sha256(runtime_dds):
			raise RuntimeError(f"Package/runtime DDS mismatch: {asset.stem}")
		rows.append([
			asset.stem,
			asset.asset_type,
			asset.sprite,
			f"{asset.size[0]}x{asset.size[1]}",
			source.relative_to(ROOT).as_posix(),
			source_hash,
			processed.relative_to(ROOT).as_posix(),
			sha256(processed),
			package_dds.relative_to(ROOT).as_posix(),
			sha256(package_dds),
			runtime_dds.relative_to(ROOT).as_posix(),
			sha256(runtime_dds),
			str(runtime_dds.stat().st_size),
			pixel_hash,
			monochrome,
			"complete",
		])
	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow([
			"asset_id",
			"asset_type",
			"sprite",
			"dimensions",
			"source",
			"source_sha256",
			"processed_png",
			"processed_sha256",
			"package_dds",
			"package_dds_sha256",
			"runtime_dds",
			"runtime_dds_sha256",
			"runtime_dds_bytes",
			"normalized_rgba_sha256",
			"true_monochrome",
			"status",
		])
		writer.writerows(rows)
	with GFX_HANDOFF.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow(["asset_id", "sprite", "runtime_texture", "dimensions", "registered_in", "status"])
		for asset in ASSETS:
			registered = "interface/014_cannibalism_aftermath_pictures.gfx" if asset.stem in {
				"report_event_cannibalism_captured_warlord",
				"report_event_cannibalism_captured_hannibal",
			} else "interface/chaosx_pictures.gfx"
			writer.writerow([
				asset.stem,
				asset.sprite,
				f"gfx/event_pictures/014_cannibalism/{asset.stem}.dds",
				f"{asset.size[0]}x{asset.size[1]}",
				registered,
				"ready",
			])


def main() -> None:
	for directory in (PROCESSED, DDS_PACKAGE, CONTACTS, VALIDATION.parent, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [asset.stem for asset in ASSETS if not (SOURCE / f"{asset.stem}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing generated sources:\n" + "\n".join(missing))
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(process, ASSETS))
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(convert, ASSETS))
	make_contact(SOURCE, "_source.png", CONTACTS / "report_news_source_contact_sheet.png", source=True)
	make_contact(PROCESSED, ".png", CONTACTS / "report_news_processed_contact_sheet.png")
	make_contact(LIVE, ".dds", CONTACTS / "report_news_dds_decoded_contact_sheet.png")
	validate()
	print(f"Processed and validated {len(ASSETS)} Event 014 report/news assets")


if __name__ == "__main__":
	main()
