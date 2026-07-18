#!/usr/bin/env python3
"""Build and validate the bounded Event 006 FORM-48 visual package.

The retained flag and emblem sources were created with official ImageGen. This
tool performs deterministic post-processing only: exact spot-colour cleanup of
the generated flag geometry, target-size rasterisation, bottom-origin
uncompressed TGA writing, transparent emblem fitting, official legacy DDS
conversion, contact-sheet assembly, validation, and checksum generation.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


PACKAGE_ROOT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
NOTES_ROOT = PACKAGE_ROOT / "notes"
FLAGS_ROOT = ROOT / "gfx" / "flags"
DDS_CONVERTER = (
	ROOT
	/ ".agents"
	/ "skills"
	/ "chaos-redux-event-assets"
	/ "tools"
	/ "convert_to_dds.py"
)
EMBLEM_RUNTIME = (
	ROOT
	/ "gfx"
	/ "interface"
	/ "006_independence_wave"
	/ "emblems"
	/ "independence_wave_formable_form_48.dds"
)
HANDOFF_FILE = (
	ROOT
	/ "docs"
	/ "plans"
	/ "006_independence_wave_plans"
	/ "subagent_handoffs"
	/ "006_form48_pacific_visual_assets_2026_07_17.md"
)
ROOT_MANIFEST = ROOT / "docs" / "assets" / "006_independence_wave" / "manifest.md"
ROOT_GFX_HANDOFF = ROOT / "docs" / "assets" / "006_independence_wave" / "gfx_handoff.md"

FLAG_SIZES = {
	"normal": (82, 52),
	"medium": (41, 26),
	"small": (10, 7),
}
FLAG_SUFFIXES = ("", "_democratic", "_communism", "_fascism", "_neutrality")
MASTER_SIZE = (1536, 1024)

FLAGS = {
	"HBX": {
		"label": "California civic carrier — 1911 Bear Flag with CALIFORNIA REPUBLIC legend",
		"source": SOURCE_ROOT / "flags" / "HBX_california_civic_imagegen_selected.png",
		"master": SOURCE_ROOT / "flags" / "HBX_california_civic_flat_master.png",
		"reference": PACKAGE_ROOT / "reference_inputs" / "california_flag_public_domain_960px.png",
		"palette": (
			(247, 245, 236),  # warm white field
			(186, 12, 47),    # California red
			(0, 132, 61),     # grass green
			(199, 139, 78),   # bear highlight
			(145, 96, 50),    # bear midtone
			(91, 65, 37),     # bear shadow
			(47, 39, 27),     # outline/detail
		),
		"small_groups": {
			"red": ((186, 12, 47),),
			"green": ((0, 132, 61),),
			"bear": ((199, 139, 78), (145, 96, 50), (91, 65, 37), (47, 39, 27)),
		},
	},
	"PFX": {
		"label": "Pacific Federation — three currents and compass",
		"source": SOURCE_ROOT / "flags" / "PFX_pacific_federation_imagegen_selected.png",
		"master": SOURCE_ROOT / "flags" / "PFX_pacific_federation_flat_master.png",
		"reference": None,
		"palette": (
			(11, 45, 77),     # deep Pacific navy
			(21, 154, 156),   # turquoise current
			(228, 179, 59),   # gold
			(245, 241, 222),  # ivory wave
		),
		"small_groups": {},
	},
}


def rel(path: Path) -> str:
	return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
	name = "arialbd.ttf" if bold else "arial.ttf"
	candidate = Path("C:/Windows/Fonts") / name
	if candidate.exists():
		return ImageFont.truetype(str(candidate), size=size)
	return ImageFont.load_default()


def fixed_palette_image(colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
	palette = Image.new("P", (1, 1))
	values: list[int] = []
	for color in colors:
		values.extend(color)
	while len(values) < 768:
		values.extend(colors[-1])
	palette.putpalette(values[:768])
	return palette


def quantize(image: Image.Image, colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
	"""Map existing generated geometry to the package's exact spot colours."""
	return image.convert("RGB").quantize(
		palette=fixed_palette_image(colors),
		dither=Image.Dither.NONE,
	).convert("RGBA")


def normalize_flag_masters() -> None:
	for config in FLAGS.values():
		source = Image.open(config["source"]).convert("RGB")
		if source.size != MASTER_SIZE:
			source = source.resize(MASTER_SIZE, Image.Resampling.LANCZOS)
		master = quantize(source, config["palette"])
		config["master"].parent.mkdir(parents=True, exist_ok=True)
		master.save(config["master"])
		validate_palette(master, config["palette"], MASTER_SIZE, config["master"])


def resized_palette(
	image: Image.Image,
	size: tuple[int, int],
	colors: tuple[tuple[int, int, int], ...],
) -> Image.Image:
	return quantize(image.resize(size, Image.Resampling.LANCZOS), colors)


def sample_small_hbx(image: Image.Image, config: dict[str, object]) -> Image.Image:
	"""Area-sample HBX while retaining the star, bear, grass, and red stripe."""
	source = image.convert("RGB")
	groups = config["small_groups"]
	output = Image.new("RGBA", FLAG_SIZES["small"])
	width, height = output.size
	for target_y in range(height):
		top = target_y * source.height // height
		bottom = (target_y + 1) * source.height // height
		for target_x in range(width):
			left = target_x * source.width // width
			right = (target_x + 1) * source.width // width
			cell = list(source.crop((left, top, right, bottom)).getdata())
			counts = {color: cell.count(color) for color in config["palette"]}
			coverage = {
				name: sum(counts[color] for color in colors) / len(cell)
				for name, colors in groups.items()
			}
			if coverage["red"] >= 0.055:
				selected = groups["red"][0]
			elif coverage["green"] >= 0.06:
				selected = groups["green"][0]
			elif coverage["bear"] >= 0.075:
				selected = max(groups["bear"], key=lambda color: counts[color])
			else:
				selected = max(config["palette"], key=lambda color: counts[color])
			output.putpixel((target_x, target_y), (*selected, 255))
	return output


def sample_small_pfx(image: Image.Image, config: dict[str, object]) -> Image.Image:
	"""Area-sample PFX and retain its thin gold and ivory federal mark."""
	source = image.convert("RGB")
	navy, turquoise, gold, ivory = config["palette"]
	output = Image.new("RGBA", FLAG_SIZES["small"])
	width, height = output.size
	for target_y in range(height):
		top = target_y * source.height // height
		bottom = (target_y + 1) * source.height // height
		for target_x in range(width):
			left = target_x * source.width // width
			right = (target_x + 1) * source.width // width
			cell = list(source.crop((left, top, right, bottom)).getdata())
			counts = {color: cell.count(color) for color in config["palette"]}
			area = len(cell)
			if counts[gold] / area >= 0.04:
				selected = gold
			elif counts[ivory] / area >= 0.045:
				selected = ivory
			elif counts[turquoise] / area >= 0.18:
				selected = turquoise
			else:
				selected = navy
			output.putpixel((target_x, target_y), (*selected, 255))
	return output


def write_bottom_origin_tga(image: Image.Image, output: Path) -> None:
	rgba = image.convert("RGBA")
	width, height = rgba.size
	header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
	source = rgba.tobytes()
	stride = width * 4
	payload = bytearray()
	for y in range(height - 1, -1, -1):
		row = source[y * stride : (y + 1) * stride]
		for index in range(0, len(row), 4):
			r, g, b, a = row[index : index + 4]
			payload.extend((b, g, r, a))
	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_bytes(header + payload)


def runtime_flag(tag: str, suffix: str, size_name: str) -> Path:
	directory = FLAGS_ROOT if size_name == "normal" else FLAGS_ROOT / size_name
	return directory / f"{tag}{suffix}.tga"


def build_flags() -> None:
	normalize_flag_masters()
	for tag, config in FLAGS.items():
		master = Image.open(config["master"]).convert("RGBA")
		for size_name, size in FLAG_SIZES.items():
			if size_name == "small" and tag == "HBX":
				image = sample_small_hbx(master, config)
			elif size_name == "small":
				image = sample_small_pfx(master, config)
			else:
				image = resized_palette(master, size, config["palette"])
			validate_palette(image, config["palette"], size, Path(f"{tag}/{size_name}"))
			processed = PROCESSED_ROOT / "flags" / size_name / f"{tag}.png"
			processed.parent.mkdir(parents=True, exist_ok=True)
			image.save(processed)
			base_runtime = runtime_flag(tag, "", size_name)
			write_bottom_origin_tga(image, base_runtime)
			for suffix in FLAG_SUFFIXES[1:]:
				shutil.copyfile(base_runtime, runtime_flag(tag, suffix, size_name))


def validate_palette(
	image: Image.Image,
	palette: tuple[tuple[int, int, int], ...],
	size: tuple[int, int],
	path: Path,
) -> dict[str, object]:
	rgba = image.convert("RGBA")
	if rgba.size != size:
		raise ValueError(f"Unexpected dimensions for {path}: {rgba.size}")
	actual = set(rgba.getdata())
	expected = {(*color, 255) for color in palette}
	if not actual or not actual.issubset(expected):
		raise ValueError(f"Non-flat pixels in {path}: {sorted(actual - expected)[:8]}")
	return {
		"dimensions": list(size),
		"palette_rgb": [list(pixel[:3]) for pixel in sorted(actual)],
		"unique_colour_count": len(actual),
		"opaque": True,
		"gradients_present": False,
	}


def process_emblem() -> dict[str, object]:
	source = SOURCE_ROOT / "emblems" / "independence_wave_formable_form_48_alpha_master.png"
	processed = PROCESSED_ROOT / "emblems" / "independence_wave_formable_form_48.png"
	image = Image.open(source).convert("RGBA")
	bbox = image.getchannel("A").getbbox()
	if bbox is None:
		raise ValueError("FORM-48 alpha master contains no visible pixels")
	cropped = image.crop(bbox)
	fitted = ImageOps.contain(cropped, (116, 116), Image.Resampling.LANCZOS)
	canvas = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
	canvas.alpha_composite(fitted, ((128 - fitted.width) // 2, (128 - fitted.height) // 2))
	processed.parent.mkdir(parents=True, exist_ok=True)
	canvas.save(processed)
	EMBLEM_RUNTIME.parent.mkdir(parents=True, exist_ok=True)
	subprocess.run(
		[
			sys.executable,
			"-B",
			str(DDS_CONVERTER),
			"--input",
			str(processed),
			"--output",
			str(EMBLEM_RUNTIME),
			"--width",
			"128",
			"--height",
			"128",
		],
		cwd=ROOT,
		check=True,
	)
	return {
		"source": source,
		"processed": processed,
		"runtime": EMBLEM_RUNTIME,
		"sprite": "GFX_independence_wave_formable_form_48",
	}


def validate_tga(path: Path, size: tuple[int, int], processed: Path) -> dict[str, object]:
	raw = path.read_bytes()
	expected_length = 18 + size[0] * size[1] * 4
	values = struct.unpack("<BBBHHBHHHHBB", raw[:18])
	if len(raw) != expected_length:
		raise ValueError(f"Unexpected TGA payload length: {path}")
	if values[0:3] != (0, 0, 2):
		raise ValueError(f"TGA is not uncompressed true-colour: {path}")
	if (values[8], values[9]) != size or values[10] != 32:
		raise ValueError(f"Unexpected TGA dimensions/depth: {path}")
	if values[11] & 0x20 or values[11] & 0x0F != 8:
		raise ValueError(f"TGA is not bottom-left origin with 8-bit alpha: {path}")
	decoded = Image.open(path).convert("RGBA")
	expected = Image.open(processed).convert("RGBA")
	if decoded.tobytes() != expected.tobytes():
		raise ValueError(f"TGA decode differs from processed PNG: {path}")
	return {
		"dimensions": list(size),
		"image_type": 2,
		"pixel_depth": 32,
		"origin": "bottom-left",
		"alpha_bits": 8,
		"bytes": len(raw),
		"sha256": sha256(path),
		"decode_matches_processed_png": True,
	}


def validate_dds(record: dict[str, object]) -> dict[str, object]:
	path = record["runtime"]
	processed = record["processed"]
	raw = path.read_bytes()
	if len(raw) != 128 + 128 * 128 * 4 or raw[:4] != b"DDS ":
		raise ValueError(f"Unexpected DDS framing: {path}")
	header_size = struct.unpack_from("<I", raw, 4)[0]
	height, width = struct.unpack_from("<II", raw, 12)
	pf_size, pf_flags, fourcc, bits, r_mask, g_mask, b_mask, a_mask = struct.unpack_from(
		"<IIIIIIII", raw, 76
	)
	caps = struct.unpack_from("<I", raw, 108)[0]
	if header_size != 124 or (width, height) != (128, 128):
		raise ValueError(f"Unexpected DDS header/size: {path}")
	if (pf_size, pf_flags, fourcc, bits) != (32, 65, 0, 32):
		raise ValueError(f"DDS is not legacy uncompressed BGRA: {path}")
	if (r_mask, g_mask, b_mask, a_mask) != (
		0x00FF0000,
		0x0000FF00,
		0x000000FF,
		0xFF000000,
	) or caps != 0x1000:
		raise ValueError(f"Unexpected DDS masks/caps: {path}")
	decoded = Image.open(path).convert("RGBA")
	expected = Image.open(processed).convert("RGBA")
	if decoded.tobytes() != expected.tobytes():
		raise ValueError(f"DDS decode differs from processed PNG: {path}")
	alpha_min, alpha_max = expected.getchannel("A").getextrema()
	visible_chroma = sum(
		1
		for r, g, b, a in expected.getdata()
		if a > 16 and r > 230 and b > 230 and g < 70
	)
	if alpha_min != 0 or alpha_max != 255:
		raise ValueError("FORM-48 emblem does not retain a full transparent/opaque range")
	if visible_chroma:
		raise ValueError(f"Visible magenta chroma contamination remains: {visible_chroma} pixels")
	return {
		"sprite": record["sprite"],
		"source_alpha_master": rel(record["source"]),
		"processed_png": rel(processed),
		"runtime_dds": rel(path),
		"dimensions": [128, 128],
		"format": "legacy uncompressed BGRA8888",
		"bytes": len(raw),
		"sha256": sha256(path),
		"alpha_min": alpha_min,
		"alpha_max": alpha_max,
		"visible_magenta_pixels": visible_chroma,
		"decode_matches_processed_png": True,
	}


def checker(size: tuple[int, int], cell: int = 10) -> Image.Image:
	image = Image.new("RGBA", size)
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], cell):
		for x in range(0, size[0], cell):
			shade = 222 if (x // cell + y // cell) % 2 == 0 else 176
			draw.rectangle(
				(x, y, min(x + cell - 1, size[0] - 1), min(y + cell - 1, size[1] - 1)),
				fill=(shade, shade, shade, 255),
			)
	return image


def place_contain(
	canvas: Image.Image,
	source: Image.Image,
	box: tuple[int, int, int, int],
	*,
	nearest: bool = False,
) -> None:
	left, top, right, bottom = box
	fitted = ImageOps.contain(
		source.convert("RGBA"),
		(right - left, bottom - top),
		Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS,
	)
	canvas.alpha_composite(
		fitted,
		(left + (right - left - fitted.width) // 2, top + (bottom - top - fitted.height) // 2),
	)


def contact_sheets(record: dict[str, object]) -> None:
	CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
	title_font = font(25, bold=True)
	label_font = font(16, bold=True)
	small_font = font(14)

	flags = Image.new("RGBA", (1740, 830), (234, 231, 222, 255))
	draw = ImageDraw.Draw(flags)
	draw.text(
		(30, 18),
		"Event 006 FORM-48 — researched source, ImageGen geometry, flat master, runtime ladders",
		fill=(20, 25, 31, 255),
		font=title_font,
	)
	for row, (tag, config) in enumerate(FLAGS.items()):
		top = 78 + row * 360
		draw.text((30, top), f"{tag} — {config['label']}", fill=(20, 25, 31, 255), font=label_font)
		if config["reference"]:
			reference = Image.open(config["reference"])
		else:
			reference = Image.new("RGBA", (300, 200), (247, 244, 236, 255))
			reference_draw = ImageDraw.Draw(reference)
			reference_draw.multiline_text(
				(20, 42),
				"Original alternate-history\nfederal identity.\nNo third-party visual copied.",
				fill=(45, 51, 60, 255),
				font=small_font,
				spacing=7,
			)
		columns = [
			("historical/reference context", reference, False, 260),
			("official ImageGen selected source", Image.open(config["source"]), False, 310),
			("exact spot-colour master", Image.open(config["master"]), False, 300),
			("82x52 runtime", Image.open(PROCESSED_ROOT / "flags" / "normal" / f"{tag}.png"), True, 240),
			("41x26 runtime", Image.open(PROCESSED_ROOT / "flags" / "medium" / f"{tag}.png"), True, 220),
			("10x7 runtime", Image.open(PROCESSED_ROOT / "flags" / "small" / f"{tag}.png"), True, 180),
		]
		x = 30
		for label, image, nearest, width in columns:
			draw.rectangle((x, top + 34, x + width, top + 270), fill=(249, 247, 241, 255), outline=(69, 75, 83, 255), width=2)
			place_contain(flags, image, (x + 8, top + 42, x + width - 8, top + 262), nearest=nearest)
			draw.text((x, top + 279), label, fill=(37, 43, 51, 255), font=small_font)
			x += width + 18
		draw.text(
			(30, top + 315),
			"Base, democratic, communism, fascism, and neutrality filenames intentionally share this constitutional/civic design.",
			fill=(52, 58, 67, 255),
			font=small_font,
		)
	flags.convert("RGB").save(CONTACT_ROOT / "006_form48_flag_sources_and_ladders.png")

	emblem = Image.new("RGBA", (1450, 500), (232, 229, 220, 255))
	draw = ImageDraw.Draw(emblem)
	draw.text((28, 18), "Event 006 FORM-48 Pacific federation emblem — source through decoded DDS", fill=(20, 25, 31, 255), font=title_font)
	raw = Image.open(SOURCE_ROOT / "emblems" / "independence_wave_formable_form_48_imagegen_raw.png")
	alpha = Image.open(record["source"]).convert("RGBA")
	processed = Image.open(record["processed"]).convert("RGBA")
	decoded = Image.open(record["runtime"]).convert("RGBA")
	items = [
		("official ImageGen chroma source", raw, False),
		("alpha master", alpha, False),
		("final 128x128 PNG", processed, True),
		("decoded runtime DDS", decoded, True),
	]
	for index, (label, image, nearest) in enumerate(items):
		left = 28 + index * 350
		panel = checker((318, 342), 14)
		place_contain(panel, image, (9, 9, 309, 333), nearest=nearest)
		emblem.alpha_composite(panel, (left, 74))
		draw.rectangle((left, 74, left + 317, 415), outline=(59, 65, 73, 255), width=2)
		draw.text((left, 426), label, fill=(36, 42, 50, 255), font=small_font)
	emblem.convert("RGB").save(CONTACT_ROOT / "006_form48_emblem_source_and_runtime.png")


def validation(record: dict[str, object]) -> dict[str, object]:
	report: dict[str, object] = {
		"pipeline": "official ImageGen source -> deterministic exact spot-colour flag cleanup / chroma removal -> target PNG -> custom bottom-origin uncompressed TGA writer or official legacy DDS converter",
		"expected_runtime_counts": {"flags_tga": 30, "emblem_dds": 1},
		"protected_asset_boundary": "No BAY/RHI portrait, portrait, commander, or advisor-icon path is produced or modified by this package.",
		"flags": {},
	}
	tga_count = 0
	base_hashes: dict[str, str] = {}
	for tag, config in FLAGS.items():
		sizes: dict[str, object] = {}
		for size_name, size in FLAG_SIZES.items():
			processed = PROCESSED_ROOT / "flags" / size_name / f"{tag}.png"
			palette_result = validate_palette(Image.open(processed), config["palette"], size, processed)
			variants: dict[str, object] = {}
			base_hash = None
			for suffix in FLAG_SUFFIXES:
				path = runtime_flag(tag, suffix, size_name)
				result = validate_tga(path, size, processed)
				if base_hash is None:
					base_hash = result["sha256"]
				else:
					if result["sha256"] != base_hash:
						raise ValueError(f"Intentional shared ideology ladder differs: {path}")
				variants[path.name] = result
				tga_count += 1
			if size_name == "normal":
				base_hashes[tag] = base_hash
			sizes[size_name] = {
				"processed_png": {"path": rel(processed), **palette_result},
				"runtime_variants": variants,
				"intentional_byte_identical_ideology_family": True,
			}
		report["flags"][tag] = {
			"imagegen_source": rel(config["source"]),
			"flat_master": rel(config["master"]),
			"master": validate_palette(Image.open(config["master"]), config["palette"], MASTER_SIZE, config["master"]),
			"sizes": sizes,
		}
	if tga_count != 30:
		raise ValueError(f"Expected 30 FORM-48 TGA files, got {tga_count}")
	if base_hashes["HBX"] == base_hashes["PFX"]:
		raise ValueError("HBX and PFX normal flags unexpectedly have identical hashes")
	report["tag_designs_are_distinct"] = True
	report["emblem"] = validate_dds(record)
	NOTES_ROOT.mkdir(parents=True, exist_ok=True)
	(NOTES_ROOT / "validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
	return report


def write_hashes(record: dict[str, object]) -> None:
	paths: set[Path] = set()
	for path in PACKAGE_ROOT.rglob("*"):
		if path.is_file() and path.name != "hashes.sha256":
			paths.add(path)
	for tag in FLAGS:
		for size_name in FLAG_SIZES:
			for suffix in FLAG_SUFFIXES:
				paths.add(runtime_flag(tag, suffix, size_name))
	paths.add(record["runtime"])
	for path in (HANDOFF_FILE, ROOT_MANIFEST, ROOT_GFX_HANDOFF):
		if path.exists():
			paths.add(path)
	lines = [f"{sha256(path)}  {rel(path)}" for path in sorted(paths, key=lambda item: rel(item))]
	(PACKAGE_ROOT / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
	build_flags()
	record = process_emblem()
	contact_sheets(record)
	validation(record)
	write_hashes(record)
	print("Built and validated 30 fixed-palette TGA flags plus one 128x128 legacy BGRA DDS emblem.")


if __name__ == "__main__":
	main()
