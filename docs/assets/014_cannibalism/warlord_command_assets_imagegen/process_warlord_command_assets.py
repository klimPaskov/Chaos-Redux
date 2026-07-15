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
VALIDATION = PACKAGE / "validation" / "warlord_command_asset_validation.tsv"
LEDGER = PACKAGE / "prompts" / "warlord_command_prompt_ledger.json"
LIVE_DECISIONS = ROOT / "gfx" / "interface" / "decisions" / "014_cannibalism"
LIVE_IDEAS = ROOT / "gfx" / "interface" / "ideas" / "014_cannibalism"
LIVE_REPORTS = ROOT / "gfx" / "event_pictures" / "014_cannibalism"
CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
REPORT_PROCESSOR = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "process_report_event_image.py"
CHROMA_HELPER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
TRANSPARENT_TYPES = {"decision_category_icon", "decision_icon", "idea_icon"}


def parse_size(text: str) -> tuple[int, int]:
	width, height = text.lower().split("x", 1)
	return int(width), int(height)


def live_path(asset: dict[str, str]) -> Path:
	name = asset["name"]
	if asset["type"] == "idea_icon":
		return LIVE_IDEAS / f"{name}.dds"
	if asset["type"] == "report_event":
		return LIVE_REPORTS / f"{name}.dds"
	return LIVE_DECISIONS / f"{name}.dds"


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


def fit_alpha(source: Path, size: tuple[int, int], padding: int, outline_width: float, shadow_offset: float) -> Image.Image:
	scale = 4
	image = trim_alpha(Image.open(source))
	maximum = (
		max(1, (size[0] - padding * 2 - math.ceil(outline_width * 2)) * scale),
		max(1, (size[1] - padding * 2 - math.ceil(outline_width * 2)) * scale),
	)
	ratio = min(maximum[0] / image.width, maximum[1] / image.height)
	resized = image.resize((max(1, round(image.width * ratio)), max(1, round(image.height * ratio))), Image.Resampling.LANCZOS)
	high_size = (size[0] * scale, size[1] * scale)
	x = (high_size[0] - resized.width) // 2
	y = (high_size[1] - resized.height) // 2
	alpha = Image.new("L", high_size, 0)
	alpha.paste(resized.getchannel("A"), (x, y))

	shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale)).point(lambda value: round(value * 0.42))
	shifted_shadow = Image.new("L", high_size, 0)
	shifted_shadow.paste(shadow_alpha, (round(shadow_offset * scale), round(shadow_offset * scale)))
	shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
	shadow.putalpha(shifted_shadow)

	outline_pixels = max(1, round(outline_width * scale))
	outline_alpha = alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1)).point(lambda value: round(value * 0.9))
	outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
	outline.putalpha(outline_alpha)

	subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
	subject.alpha_composite(resized, (x, y))
	canvas = Image.alpha_composite(shadow, outline)
	canvas = Image.alpha_composite(canvas, subject)
	result = canvas.resize(size, Image.Resampling.LANCZOS)
	final_alpha = result.getchannel("A")
	alpha_pixels = final_alpha.load()
	for x_pos in range(size[0]):
		alpha_pixels[x_pos, 0] = 0
		alpha_pixels[x_pos, size[1] - 1] = 0
	for y_pos in range(size[1]):
		alpha_pixels[0, y_pos] = 0
		alpha_pixels[size[0] - 1, y_pos] = 0
	result.putalpha(final_alpha)
	return result


def cover_opaque(source: Path, size: tuple[int, int]) -> Image.Image:
	return ImageOps.fit(Image.open(source).convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def process_report(asset: dict[str, str]) -> None:
	name = asset["name"]
	result = subprocess.run(
		[sys.executable, str(REPORT_PROCESSOR), str(SOURCE / f"{name}_source.png"), str(PROCESSED / f"{name}.png")],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"Report processing failed for {name}:\n{result.stdout}\n{result.stderr}")


def convert(asset: dict[str, str]) -> None:
	name = asset["name"]
	size = parse_size(asset["final_size"])
	package_dds = DDS_PACKAGE / f"{name}.dds"
	result = subprocess.run(
		[
			sys.executable,
			str(CONVERTER),
			"--input",
			str(PROCESSED / f"{name}.png"),
			"--output",
			str(package_dds),
			"--width",
			str(size[0]),
			"--height",
			str(size[1]),
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"DDS conversion failed for {name}:\n{result.stdout}\n{result.stderr}")
	destination = live_path(asset)
	destination.parent.mkdir(parents=True, exist_ok=True)
	shutil.copy2(package_dds, destination)


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
	image = Image.new("RGBA", size, (72, 72, 72, 255))
	draw = ImageDraw.Draw(image)
	colors = ((72, 72, 72, 255), (116, 116, 116, 255))
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			draw.rectangle((x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)), fill=colors[((x // tile) + (y // tile)) % 2])
	return image


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def make_contact(assets: list[dict[str, str]], mode: str, output: Path) -> None:
	columns = 6
	cell_w, cell_h = 230, 190
	preview_size = (150, 140)
	rows = math.ceil(len(assets) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
	draw = ImageDraw.Draw(sheet)
	label_font = font(11)
	for index, asset in enumerate(assets):
		name = asset["name"]
		col, row = index % columns, index // columns
		x0, y0 = col * cell_w, row * cell_h
		draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(88, 92, 98), width=1)
		if mode == "source":
			path = SOURCE / f"{name}_source.png"
		else:
			path = PROCESSED / f"{name}.png" if mode == "processed" else live_path(asset)
		with Image.open(path) as opened:
			if mode == "source":
				preview = ImageOps.contain(opened.convert("RGB"), preview_size, Image.Resampling.LANCZOS)
				plate = Image.new("RGB", preview_size, (48, 50, 54))
				plate.paste(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
			else:
				preview = ImageOps.contain(opened.convert("RGBA"), preview_size, Image.Resampling.NEAREST)
				plate_rgba = checker(preview_size, 10)
				plate_rgba.alpha_composite(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
				plate = plate_rgba.convert("RGB")
		sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 8))
		ly = y0 + 151
		for line in textwrap.wrap(name, width=31)[:3]:
			bbox = draw.textbbox((0, 0), line, font=label_font)
			draw.text((x0 + (cell_w - (bbox[2] - bbox[0])) // 2, ly), line, font=label_font, fill=(235, 235, 235))
			ly += 12
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output, optimize=True)


def visible_key_green(image: Image.Image) -> int:
	return sum(1 for red, green, blue, alpha in image.convert("RGBA").getdata() if alpha > 10 and green > 190 and green > red * 1.55 and green > blue * 1.55)


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
	if len(names) != 34 or len(set(names)) != 34:
		raise RuntimeError(f"Expected 34 unique command assets, found {len(names)}")
	for directory in (ALPHA, PROCESSED, DDS_PACKAGE, CONTACT, VALIDATION.parent, LIVE_DECISIONS, LIVE_IDEAS, LIVE_REPORTS):
		directory.mkdir(parents=True, exist_ok=True)
	missing = [name for name in names if not (SOURCE / f"{name}_source.png").exists()]
	if missing:
		raise FileNotFoundError("Missing command sources:\n" + "\n".join(missing))

	transparent_assets = [asset for asset in assets if asset["type"] in TRANSPARENT_TYPES]
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(run_chroma, [asset["name"] for asset in transparent_assets]))
	for asset in assets:
		name = asset["name"]
		size = parse_size(asset["final_size"])
		if asset["type"] in {"decision_category_icon", "decision_icon"}:
			image = fit_alpha(ALPHA / f"{name}_alpha.png", size, 2, 0.85, 0.75)
			image.save(PROCESSED / f"{name}.png", optimize=True)
		elif asset["type"] == "idea_icon":
			image = fit_alpha(ALPHA / f"{name}_alpha.png", size, 3, 1.0, 1.0)
			image.save(PROCESSED / f"{name}.png", optimize=True)
		elif asset["type"] == "decision_category_panel":
			cover_opaque(SOURCE / f"{name}_source.png", size).save(PROCESSED / f"{name}.png", optimize=True)
	with ThreadPoolExecutor(max_workers=2) as pool:
		list(pool.map(process_report, [asset for asset in assets if asset["type"] == "report_event"]))
	with ThreadPoolExecutor(max_workers=8) as pool:
		list(pool.map(convert, assets))

	make_contact(assets, "source", CONTACT / "warlord_command_sources_contact_sheet.png")
	make_contact(assets, "processed", CONTACT / "warlord_command_processed_checker_contact_sheet.png")
	make_contact(assets, "dds", CONTACT / "warlord_command_dds_decoded_contact_sheet.png")
	for asset_type in ("decision_category_icon", "decision_category_panel", "decision_icon", "idea_icon", "report_event"):
		subset = [asset for asset in assets if asset["type"] == asset_type]
		make_contact(subset, "processed", CONTACT / f"warlord_command_{asset_type}_processed_checker_contact_sheet.png")

	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	hashes: dict[str, str] = {}
	rows: list[list[str]] = []
	for asset in assets:
		name = asset["name"]
		asset_type = asset["type"]
		size = parse_size(asset["final_size"])
		image = Image.open(PROCESSED / f"{name}.png").convert("RGBA")
		if image.size != size:
			raise RuntimeError(f"Wrong processed size for {name}: {image.size}, expected {size}")
		alpha = image.getchannel("A")
		alpha_min, alpha_max = alpha.getextrema()
		corners = tuple(alpha.getpixel(point) for point in ((0, 0), (size[0] - 1, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1)))
		if asset_type in TRANSPARENT_TYPES and (alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0)):
			raise RuntimeError(f"Invalid icon alpha for {name}: extrema={(alpha_min, alpha_max)} corners={corners}")
		if asset_type == "decision_category_panel" and (alpha_min, alpha_max) != (255, 255):
			raise RuntimeError(f"Category panel is not opaque: {name}")
		if asset_type == "report_event" and (alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0)):
			raise RuntimeError(f"Invalid report-card alpha for {name}: extrema={(alpha_min, alpha_max)} corners={corners}")
		key_green = visible_key_green(image) if asset_type in TRANSPARENT_TYPES else 0
		if key_green:
			raise RuntimeError(f"Visible key-green pixels remain in {name}: {key_green}")
		digest = hashlib.sha256(image.tobytes()).hexdigest()
		if digest in hashes:
			raise RuntimeError(f"Duplicate normalized artwork: {name} duplicates {hashes[digest]}")
		hashes[digest] = name
		width, height, mip_count, masks = dds_header(live_path(asset))
		if (width, height) != size or mip_count not in (0, 1) or masks != expected_masks:
			raise RuntimeError(f"Invalid DDS for {name}: {(width, height)} mip={mip_count} masks={masks}")
		rows.append([
			name,
			asset_type,
			f"{size[0]}x{size[1]}",
			str(alpha_min),
			str(alpha_max),
			str(sum(1 for value in alpha.getdata() if value == 0)),
			str(sum(1 for value in alpha.getdata() if 0 < value < 255)),
			"/".join(str(value) for value in corners),
			str(key_green),
			digest,
			"0x00ff0000/0x0000ff00/0x000000ff/0xff000000",
			str(live_path(asset).relative_to(ROOT)).replace("\\", "/"),
			"complete",
		])
	with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
		writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
		writer.writerow(["asset", "asset_type", "dimensions", "alpha_min", "alpha_max", "transparent_pixels", "partial_alpha_pixels", "corner_alpha_tl_tr_bl_br", "visible_key_green_pixels", "processed_rgba_sha256", "dds_channel_masks", "live_path", "status"])
		writer.writerows(rows)
	print(f"processed and validated {len(assets)} Event 014 warlord command assets")


if __name__ == "__main__":
	main()
