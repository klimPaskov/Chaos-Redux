from __future__ import annotations

import csv
import hashlib
import math
import struct
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "focus_icon_validation.tsv"
LIVE = ROOT / "gfx" / "interface" / "goals" / "012_africa"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
CHROMA_HELPER = Path.home() / ".codex" / "skills" / ".system" / "imagegen" / "scripts" / "remove_chroma_key.py"
SIZE = (94, 86)

NAMES = [
	"goal_africa_focus_family_host_proclamation",
	"goal_africa_focus_family_host_legitimacy",
	"goal_africa_focus_family_charter_law",
	"goal_africa_focus_family_continental_representation",
	"goal_africa_focus_family_protection_guarantee",
	"goal_africa_focus_family_volunteer_intervention",
	"goal_africa_focus_family_aid_and_relief",
	"goal_africa_focus_family_regional_congress",
	"goal_africa_focus_family_road_corridor",
	"goal_africa_focus_family_rail_corridor",
	"goal_africa_focus_family_army_common_reserve",
	"goal_africa_focus_family_resource_sovereignty",
	"goal_africa_focus_family_rival_bloc",
]


def run_chroma(name: str) -> None:
	result = subprocess.run(
		[
			sys.executable,
			str(CHROMA_HELPER),
			"--input",
			str(SOURCE / f"{name}_source.png"),
			"--out",
			str(ALPHA / f"{name}_alpha.png"),
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
	outline_width = 1
	image = trim_alpha(Image.open(source))
	maximum = (
		(SIZE[0] - padding * 2 - outline_width * 2) * scale,
		(SIZE[1] - padding * 2 - outline_width * 2) * scale,
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

	shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=2 * scale))
	shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.38))
	shifted_shadow = Image.new("L", high_size, 0)
	shifted_shadow.paste(shadow_alpha, (scale, scale))
	shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
	shadow.putalpha(shifted_shadow)

	outline_pixels = outline_width * scale
	outline_alpha = alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1))
	outline_alpha = outline_alpha.point(lambda value: round(value * 0.9))
	outline = Image.new("RGBA", high_size, (19, 16, 13, 255))
	outline.putalpha(outline_alpha)

	subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
	subject.alpha_composite(resized, (x, y))
	canvas = Image.alpha_composite(shadow, outline)
	canvas = Image.alpha_composite(canvas, subject)
	return canvas.resize(SIZE, Image.Resampling.LANCZOS)


def convert(name: str) -> None:
	result = subprocess.run(
		[
			sys.executable,
			str(CONVERTER),
			"--input",
			str(PROCESSED / f"{name}.png"),
			"--output",
			str(LIVE / f"{name}.dds"),
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


def make_contact(folder: Path, suffix: str, output: Path, source_mode: bool) -> None:
	columns = 4
	cell_w, cell_h = 250, 220
	preview_size = (180, 160)
	rows = math.ceil(len(NAMES) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
	draw = ImageDraw.Draw(sheet)
	label_font = font(11)
	for index, name in enumerate(NAMES):
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
		label_y = y0 + 173
		for line in textwrap.wrap(name.removeprefix("goal_africa_focus_family_"), width=30)[:3]:
			bbox = draw.textbbox((0, 0), line, font=label_font)
			draw.text((x0 + (cell_w - (bbox[2] - bbox[0])) // 2, label_y), line, font=label_font, fill=(235, 235, 235))
			label_y += 13
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def visible_key_color(image: Image.Image) -> int:
	return sum(
		1
		for red, green, blue, alpha in image.convert("RGBA").getdata()
		if alpha > 10 and red > 210 and blue > 180 and green < 80
	)


def dds_header(path: Path) -> dict[str, int | tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) != 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	return {
		"header_size": struct.unpack_from("<I", data, 4)[0],
		"flags": struct.unpack_from("<I", data, 8)[0],
		"height": struct.unpack_from("<I", data, 12)[0],
		"width": struct.unpack_from("<I", data, 16)[0],
		"pitch": struct.unpack_from("<I", data, 20)[0],
		"depth": struct.unpack_from("<I", data, 24)[0],
		"mipmaps": struct.unpack_from("<I", data, 28)[0],
		"pixel_format_size": struct.unpack_from("<I", data, 76)[0],
		"pixel_format_flags": struct.unpack_from("<I", data, 80)[0],
		"fourcc": struct.unpack_from("<I", data, 84)[0],
		"rgb_bits": struct.unpack_from("<I", data, 88)[0],
		"masks": tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104)),
		"caps": struct.unpack_from("<I", data, 108)[0],
		"caps2": struct.unpack_from("<I", data, 112)[0],
		"caps3": struct.unpack_from("<I", data, 116)[0],
		"caps4": struct.unpack_from("<I", data, 120)[0],
		"reserved2": struct.unpack_from("<I", data, 124)[0],
	}


def main() -> None:
	for directory in (ALPHA, PROCESSED, CONTACT, VALIDATION.parent, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [name for name in NAMES if not (SOURCE / f"{name}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing focus sources:\n" + "\n".join(missing))

	for name in NAMES:
		run_chroma(name)
		fit_alpha(ALPHA / f"{name}_alpha.png").save(PROCESSED / f"{name}.png", optimize=True)
		convert(name)

	make_contact(SOURCE, "_source.png", CONTACT / "focus_icon_sources_contact_sheet.png", True)
	make_contact(PROCESSED, ".png", CONTACT / "focus_icon_processed_checker_contact_sheet.png", False)
	make_contact(LIVE, ".dds", CONTACT / "focus_icon_dds_decoded_contact_sheet.png", False)

	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	rows: list[list[str]] = []
	pixel_hashes: dict[str, str] = {}
	for name in NAMES:
		png_path = PROCESSED / f"{name}.png"
		dds_path = LIVE / f"{name}.dds"
		image = Image.open(png_path).convert("RGBA")
		decoded = Image.open(dds_path).convert("RGBA")
		if image.size != SIZE or decoded.size != SIZE or image.tobytes() != decoded.tobytes():
			raise RuntimeError(f"PNG/DDS mismatch for {name}")
		alpha = image.getchannel("A")
		alpha_min, alpha_max = alpha.getextrema()
		corners = tuple(alpha.getpixel(point) for point in ((0, 0), (SIZE[0] - 1, 0), (0, SIZE[1] - 1), (SIZE[0] - 1, SIZE[1] - 1)))
		if alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0):
			raise RuntimeError(f"Invalid alpha for {name}: extrema={(alpha_min, alpha_max)} corners={corners}")
		key_pixels = visible_key_color(image)
		if key_pixels:
			raise RuntimeError(f"Visible key-color pixels remain in {name}: {key_pixels}")
		pixel_hash = hashlib.sha256(image.tobytes()).hexdigest()
		if pixel_hash in pixel_hashes:
			raise RuntimeError(f"Duplicate normalized artwork: {name} duplicates {pixel_hashes[pixel_hash]}")
		pixel_hashes[pixel_hash] = name
		header = dds_header(dds_path)
		expected_length = 128 + SIZE[0] * SIZE[1] * 4
		if (
			(header["width"], header["height"]) != SIZE
			or header["header_size"] != 124
			or header["flags"] != 0x100F
			or header["pitch"] != SIZE[0] * 4
			or header["depth"] != 0
			or header["mipmaps"] != 0
			or header["pixel_format_size"] != 32
			or header["pixel_format_flags"] != 65
			or header["fourcc"] != 0
			or header["rgb_bits"] != 32
			or header["masks"] != expected_masks
			or header["caps"] != 0x1000
			or any(header[key] != 0 for key in ("caps2", "caps3", "caps4", "reserved2"))
			or dds_path.stat().st_size != expected_length
		):
			raise RuntimeError(f"Invalid legacy BGRA DDS for {name}")
		rows.append([
			name,
			"focus_icon",
			f"{SIZE[0]}x{SIZE[1]}",
			str(alpha_min),
			str(alpha_max),
			str(sum(1 for value in alpha.getdata() if value == 0)),
			str(sum(1 for value in alpha.getdata() if 0 < value < 255)),
			"/".join(str(value) for value in corners),
			str(key_pixels),
			hashlib.sha256((SOURCE / f"{name}_source.png").read_bytes()).hexdigest(),
			hashlib.sha256(png_path.read_bytes()).hexdigest(),
			pixel_hash,
			hashlib.sha256(dds_path.read_bytes()).hexdigest(),
			"yes",
			"handed_off",
		])

	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow([
			"asset",
			"asset_type",
			"dimensions",
			"alpha_min",
			"alpha_max",
			"transparent_pixels",
			"partial_alpha_pixels",
			"corner_alpha_tl_tr_bl_br",
			"visible_key_color_pixels",
			"source_sha256",
			"processed_sha256",
			"processed_rgba_sha256",
			"dds_sha256",
			"png_dds_pixel_equal",
			"status",
		])
		writer.writerows(rows)
	print(f"Processed and validated {len(NAMES)} Event 012 focus icons")


if __name__ == "__main__":
	main()
