"""Process the IW-051 Sakha route flag masters into HOI4 ladders.

The native ImageGen files are retained unchanged.  Their usable flat flag is
the documented upper-left 768x512 rectangle; the remaining canvas is an
unintended red field and is never copied into a runtime flag.  Processing is
mechanical: crop, fixed-palette resize, TGA/DDS encoding, and evidence.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
MOD_ROOT = PACKAGE_ROOT.parents[3]
SOURCE_ROOT = PACKAGE_ROOT / "source_png" / "imagegen_raw"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
FINAL_TGA_ROOT = PACKAGE_ROOT / "final_tga"
FINAL_DDS_ROOT = PACKAGE_ROOT / "final_dds"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
COMPARISON_ROOT = PACKAGE_ROOT / "comparison"
METADATA_ROOT = PACKAGE_ROOT / "metadata"

FLAG_SIZES = {
	"normal": (82, 52),
	"medium": (41, 26),
	"small": (10, 7),
}

# The raw masters place the flag in the upper-left, but the accidental red
# remainder starts at a different edge in each native output.  These boxes
# are recorded per route rather than silently trimming the source.
CROP_BOXES = {
	"YAK_INDEPENDENCE_WAVE_CIVICX": (0, 0, 768, 394),
	"YAK_INDEPENDENCE_WAVE_ARCTICX": (0, 0, 692, 512),
	"YAK_INDEPENDENCE_WAVE_SOCIALISTX": (0, 0, 688, 592),
	"YAK_INDEPENDENCE_WAVE_EMERGENCYX": (0, 0, 768, 576),
}

FLAGS = {
	"YAK_INDEPENDENCE_WAVE_CIVICX": {
		"source": "YAK_INDEPENDENCE_WAVE_CIVICX_imagegen_raw.png",
		"crop_box": CROP_BOXES["YAK_INDEPENDENCE_WAVE_CIVICX"],
		"route": "Civic constitutional autonomy",
		"classification": "alternate-history generated civic synthesis; not an attested universal 1936 Yakut flag",
		"motif": "light-blue field with green and violet Aurora ribbons and a gold interlaced Sakha civic knot",
		"palette": [(170, 216, 239), (44, 143, 104), (96, 60, 155), (211, 165, 32), (255, 249, 220)],
	},
	"YAK_INDEPENDENCE_WAVE_ARCTICX": {
		"source": "YAK_INDEPENDENCE_WAVE_ARCTICX_imagegen_raw.png",
		"crop_box": CROP_BOXES["YAK_INDEPENDENCE_WAVE_ARCTICX"],
		"route": "Arctic council and river security",
		"classification": "alternate-history generated arctic synthesis; the 1926 Aurora/light-blue research motif is not a copied runtime flag",
		"motif": "light-blue field with green-violet Aurora band, gold stepped mountain and river geometry, and white civic knot",
		"palette": [(170, 216, 239), (44, 143, 104), (96, 60, 155), (205, 160, 31), (255, 250, 223)],
	},
	"YAK_INDEPENDENCE_WAVE_SOCIALISTX": {
		"source": "YAK_INDEPENDENCE_WAVE_SOCIALISTX_imagegen_raw.png",
		"crop_box": CROP_BOXES["YAK_INDEPENDENCE_WAVE_SOCIALISTX"],
		"route": "Popular socialist councils",
		"classification": "alternate-history generated socialist synthesis; not an attested 1936 Yakut ASSR flag",
		"motif": "light-blue field with green-violet Aurora band, gold river-settlement emblem, and white civic outlines",
		"palette": [(170, 216, 239), (44, 143, 104), (96, 60, 155), (205, 160, 31), (255, 250, 223), (24, 76, 142)],
	},
	"YAK_INDEPENDENCE_WAVE_EMERGENCYX": {
		"source": "YAK_INDEPENDENCE_WAVE_EMERGENCYX_imagegen_raw.png",
		"crop_box": CROP_BOXES["YAK_INDEPENDENCE_WAVE_EMERGENCYX"],
		"route": "Emergency frontier command",
		"classification": "alternate-history generated emergency-command synthesis; no historical 1936 emergency flag is claimed",
		"motif": "light-blue field with green-violet Aurora band, gold fortified river gate, navy water bars, and white outlines",
		"palette": [(170, 216, 239), (44, 143, 104), (96, 60, 155), (205, 160, 31), (255, 250, 223), (24, 76, 142)],
	},
}


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest().upper()


def fixed_palette_image(colors: list[tuple[int, int, int]]) -> Image.Image:
	palette = Image.new("P", (1, 1))
	flat = [channel for color in colors for channel in color]
	flat.extend([0] * (768 - len(flat)))
	palette.putpalette(flat)
	return palette


def flatten_to_palette(image: Image.Image, size: tuple[int, int], colors: list[tuple[int, int, int]]) -> Image.Image:
	resized = image.convert("RGB").resize(size, Image.Resampling.LANCZOS)
	indexed = resized.quantize(palette=fixed_palette_image(colors), dither=Image.Dither.NONE)
	return indexed.convert("RGBA")


def write_bottom_origin_tga(image: Image.Image, path: Path, descriptor: int) -> None:
	rgba = image.convert("RGBA")
	width, height = rgba.size
	payload = bytearray()
	pixels = rgba.load()
	for y in range(height - 1, -1, -1):
		for x in range(width):
			red, green, blue, alpha = pixels[x, y]
			payload.extend((blue, green, red, alpha))
	header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, descriptor)
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_bytes(header + payload)


def write_bgra_dds(image: Image.Image, path: Path) -> None:
	rgba = image.convert("RGBA")
	width, height = rgba.size
	# DDS_HEADER followed by an uncompressed BGRA payload in top-origin order.
	header = bytearray(124)
	struct.pack_into("<I", header, 0, 124)
	struct.pack_into("<I", header, 4, 0x0002100F)  # caps|height|width|pixel format
	struct.pack_into("<II", header, 8, height, width)
	struct.pack_into("<II", header, 16, width * height * 4, 0)
	# Offsets below are relative to DDS_HEADER (the four-byte magic is outside
	# this byte array): the pixel-format block begins at 72 and caps at 104.
	struct.pack_into("<I", header, 72, 32)
	struct.pack_into("<I", header, 76, 65)  # RGB + alpha pixels
	struct.pack_into("<I", header, 84, 32)
	struct.pack_into("<IIII", header, 88, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	struct.pack_into("<I", header, 104, 0x1000)
	payload = bytearray()
	for red, green, blue, alpha in rgba.getdata():
		payload.extend((blue, green, red, alpha))
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_bytes(b"DDS " + header + payload)


def inspect_tga(path: Path, expected: tuple[int, int]) -> dict[str, object]:
	data = path.read_bytes()
	fields = struct.unpack("<BBBHHBHHHHBB", data[:18])
	width, height, depth, descriptor = fields[8:12]
	decoded = Image.open(path).convert("RGBA")
	checks = {
		"dimensions": (width, height) == expected,
		"true_color": fields[2] == 2,
		"depth_32": depth == 32,
		"bottom_origin": descriptor & 0x20 == 0,
		"alpha_bits": descriptor & 0x0F in (0, 8),
		"opaque": decoded.getchannel("A").getextrema() == (255, 255),
		"length": len(data) == 18 + width * height * 4,
	}
	return {
		"path": path.relative_to(MOD_ROOT).as_posix(),
		"width": width,
		"height": height,
		"descriptor": descriptor,
		"sha256": sha256(path),
		"checks": checks,
		"valid": all(checks.values()),
	}


def inspect_dds(path: Path, png_path: Path, expected: tuple[int, int]) -> dict[str, object]:
	data = path.read_bytes()
	header_size = struct.unpack_from("<I", data, 4)[0]
	height, width = struct.unpack_from("<II", data, 12)
	pixel_format_size, pixel_flags, fourcc, bit_count, r_mask, g_mask, b_mask, a_mask = struct.unpack_from("<IIIIIIII", data, 76)
	caps = struct.unpack_from("<I", data, 108)[0]
	decoded = Image.frombytes("RGBA", (width, height), data[128:], "raw", "BGRA")
	source = Image.open(png_path).convert("RGBA")
	checks = {
		"magic": data[:4] == b"DDS ",
		"header": header_size == 124,
		"dimensions": (width, height) == expected,
		"pixel_format": (pixel_format_size, pixel_flags, fourcc, bit_count) == (32, 65, 0, 32),
		"masks": (r_mask, g_mask, b_mask, a_mask) == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000),
		"caps": caps == 0x1000,
		"length": len(data) == 128 + width * height * 4,
		"roundtrip": decoded.tobytes() == source.tobytes(),
	}
	return {
		"path": path.relative_to(MOD_ROOT).as_posix(),
		"png": png_path.relative_to(MOD_ROOT).as_posix(),
		"sha256": sha256(path),
		"checks": checks,
		"valid": all(checks.values()),
	}


def font(size: int) -> ImageFont.ImageFont:
	for candidate in (Path("C:/Windows/Fonts/arial.ttf"), Path("C:/Windows/Fonts/segoeui.ttf")):
		if candidate.exists():
			return ImageFont.truetype(str(candidate), size)
	return ImageFont.load_default()


def display(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
	scale = min(max_width / image.width, max_height / image.height)
	return image.resize((max(1, round(image.width * scale)), max(1, round(image.height * scale))), Image.Resampling.NEAREST)


def main() -> None:
	for root in (PROCESSED_ROOT, FINAL_TGA_ROOT, FINAL_DDS_ROOT, CONTACT_ROOT, COMPARISON_ROOT, METADATA_ROOT):
		root.mkdir(parents=True, exist_ok=True)
	rows: dict[str, dict[str, Image.Image]] = {}
	metadata: dict[str, object] = {
		"package": "006_iw051_sakha_flags_2026_08_15",
		"carrier_tag": "YAK",
		"mode": "alternate_history_generated_route_cosmetics",
		"neutral_1936_flag_attested": False,
		"vanilla_yak_files_modified": False,
		"runtime_lookup": "route-specific basenames only; no YAK base override",
		"crop_boxes_xyxy": {name: list(box) for name, box in CROP_BOXES.items()},
		"prompt_archive": "not present in the supplied source directory; retain source hashes and require parent review",
		"flags": {},
	}

	for name, spec in FLAGS.items():
		source_path = SOURCE_ROOT / spec["source"]
		source = Image.open(source_path).convert("RGBA")
		crop_box = spec["crop_box"]
		crop = source.crop(crop_box)
		master = flatten_to_palette(crop, (820, 520), spec["palette"])
		master_path = PROCESSED_ROOT / f"{name}_flat_master_820x520.png"
		master.save(master_path, optimize=True)
		entry: dict[str, object] = {
			"route": spec["route"],
			"classification": spec["classification"],
			"motif": spec["motif"],
			"source": source_path.relative_to(MOD_ROOT).as_posix(),
			"source_sha256": sha256(source_path),
			"source_dimensions": list(source.size),
			"crop_box_xyxy": list(crop_box),
			"crop_dimensions": list(crop.size),
			"master": master_path.relative_to(MOD_ROOT).as_posix(),
			"master_sha256": sha256(master_path),
			"ladder": {},
		}
		images: dict[str, Image.Image] = {"source": crop, "master": master}
		for size_name, dimensions in FLAG_SIZES.items():
			ladder = flatten_to_palette(master, dimensions, spec["palette"])
			png_path = PROCESSED_ROOT / size_name / f"{name}.png"
			png_path.parent.mkdir(parents=True, exist_ok=True)
			ladder.save(png_path, optimize=True)
			tga_path = MOD_ROOT / "gfx" / "flags" / (f"{name}.tga" if size_name == "normal" else f"{size_name}/{name}.tga")
			descriptor = 0 if size_name == "small" else 8
			write_bottom_origin_tga(ladder, tga_path, descriptor)
			package_tga = FINAL_TGA_ROOT / f"{name}_{size_name}_{dimensions[0]}x{dimensions[1]}.tga"
			package_tga.write_bytes(tga_path.read_bytes())
			tga_info = inspect_tga(tga_path, dimensions)
			if not tga_info["valid"]:
				raise RuntimeError(f"TGA validation failed: {tga_path}")
			dds_path = FINAL_DDS_ROOT / f"{name}_{size_name}_{dimensions[0]}x{dimensions[1]}.dds"
			write_bgra_dds(ladder, dds_path)
			dds_info = inspect_dds(dds_path, png_path, dimensions)
			if not dds_info["valid"]:
				raise RuntimeError(f"DDS validation failed: {dds_path}")
			entry["ladder"][size_name] = {
				"processed_png": png_path.relative_to(MOD_ROOT).as_posix(),
				"processed_png_sha256": sha256(png_path),
				"runtime_tga": tga_info,
				"package_tga": package_tga.relative_to(MOD_ROOT).as_posix(),
				"package_tga_sha256": sha256(package_tga),
				"dds": dds_info,
			}
			images[size_name] = Image.open(tga_path).convert("RGBA")
		rows[name] = images
		metadata["flags"][name] = entry

	# Contact sheet keeps raw crop, processed master, and all runtime sizes visible.
	label_width, cell_width, cell_height, margin = 460, 220, 175, 20
	columns = ["source crop", "flat master", "normal", "medium", "small"]
	width = margin * 2 + label_width + cell_width * len(columns)
	height = 85 + cell_height * len(rows) + margin
	sheet = Image.new("RGB", (width, height), (31, 35, 42))
	draw = ImageDraw.Draw(sheet)
	draw.text((margin, 14), "IW-051 Sakha generated route flag ladders", fill=(245, 245, 245), font=font(26))
	for col, title in enumerate(columns):
		draw.text((margin + label_width + col * cell_width + 6, 56), title, fill=(215, 219, 225), font=font(14))
	for row, (name, images) in enumerate(rows.items()):
		top = 85 + row * cell_height
		draw.rectangle((margin, top, width - margin, top + cell_height - 8), fill=(46, 50, 58) if row % 2 == 0 else (39, 43, 50))
		draw.text((margin + 10, top + 40), name, fill=(250, 250, 250), font=font(15))
		draw.text((margin + 10, top + 73), FLAGS[name]["route"], fill=(205, 209, 216), font=font(12))
		for col, key in enumerate(("source", "master", "normal", "medium", "small")):
			thumb = display(images[key], cell_width - 14, cell_height - 55).convert("RGB")
			x = margin + label_width + col * cell_width
			sheet.paste(thumb, (x + (cell_width - thumb.width) // 2, top + (cell_height - thumb.height) // 2 + 8))
	contact = CONTACT_ROOT / "iw051_sakha_flag_ladders_contact_sheet.png"
	sheet.save(contact, optimize=True)
	metadata["contact_sheet"] = contact.relative_to(MOD_ROOT).as_posix()
	metadata["contact_sheet_sha256"] = sha256(contact)
	(METADATA_ROOT / "flag_validation.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
	(METADATA_ROOT / "dds_validation.json").write_text(json.dumps({name: data["ladder"] for name, data in metadata["flags"].items()}, indent=2) + "\n", encoding="utf-8")
	(METADATA_ROOT / "generation_evidence.json").write_text(json.dumps({
		"package": metadata["package"],
		"native_imagegen_sources": {name: metadata["flags"][name]["source"] for name in metadata["flags"]},
		"source_hashes": {name: metadata["flags"][name]["source_sha256"] for name in metadata["flags"]},
		"crop_boxes_xyxy": {name: list(box) for name, box in CROP_BOXES.items()},
		"crop_rationale": "The supplied 1536x1024 masters contain a flat flag in the upper-left 768x512 rectangle and an unintended red remainder; only the documented rectangle is processed.",
		"neutral_1936_flag_attested": False,
		"prompt_archive": "not present",
	}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
