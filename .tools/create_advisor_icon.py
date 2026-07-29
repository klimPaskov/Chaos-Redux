"""Create one HOI4 advisor card from a portrait and a vanilla card template.

This is a standalone maintenance utility. It is intentionally not registered by
any repository skill or asset workflow.

The template supplies the existing HOI4 frame and paper artwork. The utility
replaces only the portrait window, preserves the template alpha and paper, and
writes a legacy one-level 32-bit BGRA DDS.
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance


CARD_SIZE = (65, 67)
PORTRAIT_WINDOW = ((10, 8), (40, 8), (40, 56), (11, 57))
PAPER_REGION = (27, 22, 61, 61)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source", type=Path, required=True)
	parser.add_argument("--template", type=Path, required=True)
	parser.add_argument("--preview", type=Path, required=True)
	parser.add_argument("--output", type=Path, required=True)
	parser.add_argument(
		"--crop",
		type=int,
		nargs=4,
		metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
		required=True,
	)
	parser.add_argument(
		"--portrait-offset",
		type=int,
		nargs=2,
		metavar=("X", "Y"),
		default=(8, 6),
	)
	parser.add_argument("--portrait-size", type=int, nargs=2, default=(34, 54))
	parser.add_argument("--rotation", type=float, default=-2.5)
	return parser.parse_args()


def validate_crop(image: Image.Image, crop: tuple[int, int, int, int]) -> None:
	left, top, right, bottom = crop
	if left < 0 or top < 0 or right > image.width or bottom > image.height:
		raise ValueError(f"Crop {crop} is outside {image.width}x{image.height}")
	if left >= right or top >= bottom:
		raise ValueError(f"Crop has no area: {crop}")


def prepare_portrait(
	source: Image.Image,
	crop: tuple[int, int, int, int],
	size: tuple[int, int],
	rotation: float,
) -> Image.Image:
	validate_crop(source, crop)
	portrait = source.crop(crop).convert("RGBA")
	portrait = ImageEnhance.Color(portrait).enhance(0.86)
	portrait = ImageEnhance.Contrast(portrait).enhance(1.06)
	portrait = portrait.resize(size, Image.Resampling.LANCZOS)
	return portrait.rotate(rotation, Image.Resampling.BICUBIC, expand=True)


def build_template_overlay(template: Image.Image) -> Image.Image:
	overlay = template.convert("RGBA")
	if overlay.size != CARD_SIZE:
		raise ValueError(f"Template must be {CARD_SIZE[0]}x{CARD_SIZE[1]}")

	window = Image.new("L", CARD_SIZE, 0)
	ImageDraw.Draw(window).polygon(PORTRAIT_WINDOW, fill=255)

	rgb = overlay.convert("RGB")
	paper = Image.new("L", CARD_SIZE, 0)
	paper_pixels = paper.load()
	rgb_pixels = rgb.load()
	alpha_pixels = overlay.getchannel("A").load()
	left, top, right, bottom = PAPER_REGION
	for y in range(top, bottom):
		for x in range(left, right):
			red, green, blue = rgb_pixels[x, y]
			luminance = (red * 299 + green * 587 + blue * 114) // 1000
			chroma = max(red, green, blue) - min(red, green, blue)
			if alpha_pixels[x, y] > 24 and luminance > 132 and chroma < 90:
				paper_pixels[x, y] = 255

	clear_window = ImageChops.subtract(window, paper)
	alpha = overlay.getchannel("A")
	alpha = ImageChops.subtract(alpha, clear_window)
	overlay.putalpha(alpha)
	return overlay


def compose(
	source: Image.Image,
	template: Image.Image,
	crop: tuple[int, int, int, int],
	offset: tuple[int, int],
	size: tuple[int, int],
	rotation: float,
) -> Image.Image:
	card = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
	portrait = prepare_portrait(source, crop, size, rotation)
	portrait_layer = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
	portrait_layer.alpha_composite(portrait, offset)
	window = Image.new("L", CARD_SIZE, 0)
	ImageDraw.Draw(window).polygon(PORTRAIT_WINDOW, fill=255)
	portrait_layer.putalpha(
		ImageChops.multiply(portrait_layer.getchannel("A"), window)
	)
	card.alpha_composite(portrait_layer)
	card.alpha_composite(build_template_overlay(template))
	return card


def write_bgra_dds(image: Image.Image, output: Path) -> None:
	image = image.convert("RGBA")
	width, height = image.size
	flags = 0x1 | 0x2 | 0x4 | 0x8 | 0x1000
	pixel_format = struct.pack(
		"<IIIIIIII",
		32,
		0x41,
		0,
		32,
		0x00FF0000,
		0x0000FF00,
		0x000000FF,
		0xFF000000,
	)
	header = struct.pack(
		"<IIIIIII11I",
		124,
		flags,
		height,
		width,
		width * 4,
		0,
		0,
		*([0] * 11),
	)
	header += pixel_format
	header += struct.pack("<IIIII", 0x1000, 0, 0, 0, 0)
	if len(header) != 124:
		raise AssertionError(f"Unexpected DDS header size: {len(header)}")

	raw = bytearray()
	for red, green, blue, alpha in image.getdata():
		raw.extend((blue, green, red, alpha))

	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_bytes(b"DDS " + header + raw)


def main() -> None:
	args = parse_args()
	source = Image.open(args.source)
	template = Image.open(args.template)
	card = compose(
		source,
		template,
		tuple(args.crop),
		tuple(args.portrait_offset),
		tuple(args.portrait_size),
		args.rotation,
	)
	args.preview.parent.mkdir(parents=True, exist_ok=True)
	card.save(args.preview)
	write_bgra_dds(card, args.output)

	reopened = Image.open(args.output).convert("RGBA")
	if reopened.size != CARD_SIZE:
		raise ValueError(f"DDS reopened at {reopened.size}, expected {CARD_SIZE}")
	if reopened.tobytes() != card.tobytes():
		raise ValueError("DDS decoded pixels differ from the preview")
	expected_length = 128 + CARD_SIZE[0] * CARD_SIZE[1] * 4
	if args.output.stat().st_size != expected_length:
		raise ValueError("DDS length does not match one-level BGRA layout")


if __name__ == "__main__":
	main()
