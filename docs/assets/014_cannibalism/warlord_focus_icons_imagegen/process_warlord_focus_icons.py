from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "warlord_focus_icon_validation.tsv"
LEDGER = PACKAGE / "prompts" / "focus_icon_prompt_ledger.json"
LIVE = ROOT / "gfx" / "interface" / "goals" / "014_cannibalism"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
CHROMA_HELPER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
SIZE = (94, 86)


def run_chroma(name: str) -> None:
	input_path = SOURCE / f"{name}_source.png"
	output_path = ALPHA / f"{name}_alpha.png"
	result = subprocess.run(
		[
			sys.executable,
			str(CHROMA_HELPER),
			"--input",
			str(input_path),
			"--out",
			str(output_path),
			"--auto-key",
			"border",
			"--soft-matte",
			"--transparent-threshold",
			"12",
			"--opaque-threshold",
			"220",
			"--despill",
			"--force",
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
	scale = 4
	padding = 3
	outline_width = 1.0
	shadow_offset = 1.0
	image = trim_alpha(Image.open(source))
	maximum = (
		max(1, (SIZE[0] - padding * 2 - math.ceil(outline_width * 2)) * scale),
		max(1, (SIZE[1] - padding * 2 - math.ceil(outline_width * 2)) * scale),
	)
	ratio = min(maximum[0] / image.width, maximum[1] / image.height)
	resized = image.resize(
		(max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
		Image.Resampling.LANCZOS,
	)
	high_size = (SIZE[0] * scale, SIZE[1] * scale)
	x = (high_size[0] - resized.width) // 2
	y = (high_size[1] - resized.height) // 2
	alpha = Image.new("L", high_size, 0)
	alpha.paste(resized.getchannel("A"), (x, y))

	shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale))
	shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.42))
	shifted_shadow = Image.new("L", high_size, 0)
	shifted_shadow.paste(shadow_alpha, (round(shadow_offset * scale), round(shadow_offset * scale)))
	shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
	shadow.putalpha(shifted_shadow)

	outline_pixels = max(1, round(outline_width * scale))
	outline_alpha = alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1))
	outline_alpha = outline_alpha.point(lambda value: round(value * 0.9))
	outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
	outline.putalpha(outline_alpha)

	subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
	subject.alpha_composite(resized, (x, y))
	canvas = Image.alpha_composite(shadow, outline)
	canvas = Image.alpha_composite(canvas, subject)
	return canvas.resize(SIZE, Image.Resampling.LANCZOS)


def convert(name: str) -> None:
	png = PROCESSED / f"{name}.png"
	package_dds = DDS_PACKAGE / f"{name}.dds"
	result = subprocess.run(
		[
			sys.executable,
			str(CONVERTER),
			"--input",
			str(png),
			"--output",
			str(package_dds),
			"--width",
			str(SIZE[0]),
			"--height",
			str(SIZE[1]),
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
	colors = ((72, 72, 72, 255), (116, 116, 116, 255))
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			draw.rectangle(
				(x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
				fill=colors[((x // tile) + (y // tile)) % 2],
			)
	return image


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def make_contact(names: list[str], folder: Path, suffix: str, output: Path, source_mode: bool) -> None:
	columns = 8
	cell_w, cell_h = 190, 170
	preview_size = (118, 118)
	rows = math.ceil(len(names) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
	draw = ImageDraw.Draw(sheet)
	label_font = font(10)
	for index, name in enumerate(names):
		col, row = index % columns, index // columns
		x0, y0 = col * cell_w, row * cell_h
		draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(88, 92, 98), width=1)
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
		sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 8))
		ly = y0 + 130
		for line in textwrap.wrap(name, width=28)[:3]:
			bbox = draw.textbbox((0, 0), line, font=label_font)
			draw.text((x0 + (cell_w - (bbox[2] - bbox[0])) // 2, ly), line, font=label_font, fill=(235, 235, 235))
			ly += 11
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def visible_key_green(image: Image.Image) -> int:
	return sum(
		1
		for red, green, blue, alpha in image.convert("RGBA").getdata()
		if alpha > 10 and green > 190 and green > red * 1.55 and green > blue * 1.55
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
	assets = json.loads(LEDGER.read_text(encoding="utf-8"))["assets"]
	names = [asset["name"] for asset in assets]
	if len(names) != 68 or len(set(names)) != 68:
		raise RuntimeError(f"Expected 68 unique focus assets, found {len(names)}")
	for directory in (ALPHA, PROCESSED, DDS_PACKAGE, CONTACT, VALIDATION.parent, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [name for name in names if not (SOURCE / f"{name}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing focus sources:\n" + "\n".join(missing))

	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(run_chroma, names))
	for name in names:
		fit_alpha(ALPHA / f"{name}_alpha.png").save(PROCESSED / f"{name}.png", optimize=True)
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(convert, names))

	make_contact(names, SOURCE, "_source.png", CONTACT / "warlord_focus_sources_contact_sheet.png", True)
	make_contact(names, PROCESSED, ".png", CONTACT / "warlord_focus_processed_checker_contact_sheet.png", False)
	make_contact(names, LIVE, ".dds", CONTACT / "warlord_focus_dds_decoded_contact_sheet.png", False)

	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	hashes: dict[str, str] = {}
	rows: list[list[str]] = []
	for name in names:
		png = PROCESSED / f"{name}.png"
		image = Image.open(png).convert("RGBA")
		if image.size != SIZE:
			raise RuntimeError(f"Wrong processed size for {name}: {image.size}")
		alpha = image.getchannel("A")
		alpha_min, alpha_max = alpha.getextrema()
		corners = tuple(alpha.getpixel(point) for point in ((0, 0), (SIZE[0] - 1, 0), (0, SIZE[1] - 1), (SIZE[0] - 1, SIZE[1] - 1)))
		if alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0):
			raise RuntimeError(f"Invalid focus alpha for {name}: extrema={(alpha_min, alpha_max)} corners={corners}")
		key_green = visible_key_green(image)
		if key_green:
			raise RuntimeError(f"Visible key-green pixels remain in {name}: {key_green}")
		digest = hashlib.sha256(image.tobytes()).hexdigest()
		if digest in hashes:
			raise RuntimeError(f"Duplicate normalized artwork: {name} duplicates {hashes[digest]}")
		hashes[digest] = name
		width, height, mip_count, masks = dds_header(LIVE / f"{name}.dds")
		if (width, height) != SIZE or mip_count not in (0, 1) or masks != expected_masks:
			raise RuntimeError(f"Invalid DDS for {name}: {(width, height)} mip={mip_count} masks={masks}")
		rows.append([
			name,
			"focus_icon",
			f"{SIZE[0]}x{SIZE[1]}",
			str(alpha_min),
			str(alpha_max),
			str(sum(1 for value in alpha.getdata() if value == 0)),
			str(sum(1 for value in alpha.getdata() if 0 < value < 255)),
			"/".join(str(value) for value in corners),
			str(key_green),
			digest,
			"0x00ff0000/0x0000ff00/0x000000ff/0xff000000",
			"complete",
		])
	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow(["asset", "asset_type", "dimensions", "alpha_min", "alpha_max", "transparent_pixels", "partial_alpha_pixels", "corner_alpha_tl_tr_bl_br", "visible_key_green_pixels", "processed_rgba_sha256", "dds_channel_masks", "status"])
		writer.writerows(rows)
	print(f"processed and validated {len(names)} Event 014 warlord focus icons")


if __name__ == "__main__":
	main()
