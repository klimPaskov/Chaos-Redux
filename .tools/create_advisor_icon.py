"""Create a HOI4 advisor icon from three explicit image layers.

The bottom-to-top layer order is:

1. advisor frame
2. resized, rotated, lightly sepia-treated portrait
3. advisor paper

The portrait is clipped to the frame opening so it cannot cover the visible
frame. The script writes both a review PNG and a legacy one-level 32-bit BGRA
DDS.
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps


CARD_SIZE = (65, 67)
PORTRAIT_WINDOW = ((10, 8), (40, 8), (40, 56), (11, 57))
MOD_ROOT = Path(__file__).resolve().parent.parent
ADVISOR_REFERENCE_ROOT = (
	MOD_ROOT
	/ ".agents"
	/ "skills"
	/ "chaos-redux-event-assets"
	/ "assets"
	/ "vanilla_reference"
	/ "portraits"
	/ "advisors"
)
DEFAULT_FRAME = ADVISOR_REFERENCE_ROOT / "advisor_frame.png"
DEFAULT_PAPER = ADVISOR_REFERENCE_ROOT / "advisor_paper.png"


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source", type=Path, required=True)
	parser.add_argument("--frame", type=Path, default=DEFAULT_FRAME)
	parser.add_argument("--paper", type=Path, default=DEFAULT_PAPER)
	parser.add_argument("--preview", type=Path, required=True)
	parser.add_argument("--output", type=Path, required=True)
	parser.add_argument(
		"--crop",
		type=int,
		nargs=4,
		metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
		default=None,
	)
	parser.add_argument(
		"--portrait-offset",
		type=int,
		nargs=2,
		metavar=("X", "Y"),
		default=None,
		help="Optional top-left override after rotation.",
	)
	parser.add_argument(
		"--portrait-center",
		type=float,
		nargs=2,
		metavar=("X", "Y"),
		default=(24.5, 35.5),
		help="Stable portrait center inside the frame (default: 24.5 35.5).",
	)
	parser.add_argument("--portrait-size", type=int, nargs=2, default=(34, 57))
	parser.add_argument("--rotation", type=float, default=-1.5)
	parser.add_argument(
		"--sepia-strength",
		type=float,
		default=0.18,
		help="Portrait-only sepia blend from 0.0 to 1.0 (default: 0.18).",
	)
	return parser.parse_args()


def validate_crop(image: Image.Image, crop: tuple[int, int, int, int]) -> None:
	left, top, right, bottom = crop
	if left < 0 or top < 0 or right > image.width or bottom > image.height:
		raise ValueError(f"Crop {crop} is outside {image.width}x{image.height}")
	if left >= right or top >= bottom:
		raise ValueError(f"Crop has no area: {crop}")


def prepare_portrait(
	source: Image.Image,
	crop: tuple[int, int, int, int] | None,
	size: tuple[int, int],
	rotation: float,
	sepia_strength: float,
) -> Image.Image:
	if crop is None:
		portrait = source.convert("RGBA")
	else:
		validate_crop(source, crop)
		portrait = source.crop(crop).convert("RGBA")
	if not 0.0 <= sepia_strength <= 1.0:
		raise ValueError("--sepia-strength must be between 0.0 and 1.0")

	alpha = portrait.getchannel("A")
	sepia = ImageOps.colorize(
		ImageOps.grayscale(portrait),
		black=(24, 18, 12),
		white=(244, 224, 188),
	)
	portrait = Image.blend(portrait.convert("RGB"), sepia, sepia_strength)
	portrait.putalpha(alpha)
	portrait = portrait.resize(size, Image.Resampling.LANCZOS)
	return portrait.rotate(rotation, Image.Resampling.BICUBIC, expand=True)


def load_layer(path: Path, label: str) -> Image.Image:
	layer = Image.open(path).convert("RGBA")
	if layer.size != CARD_SIZE:
		raise ValueError(
			f"{label} must be {CARD_SIZE[0]}x{CARD_SIZE[1]}, got "
			f"{layer.width}x{layer.height}"
		)
	return layer


def compose(
	source: Image.Image,
	frame: Image.Image,
	paper: Image.Image,
	crop: tuple[int, int, int, int] | None,
	offset: tuple[int, int] | None,
	center: tuple[float, float],
	size: tuple[int, int],
	rotation: float,
	sepia_strength: float,
) -> Image.Image:
	card = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
	card.alpha_composite(frame)

	portrait = prepare_portrait(source, crop, size, rotation, sepia_strength)
	if offset is None:
		offset = (
			round(center[0] - portrait.width / 2),
			round(center[1] - portrait.height / 2),
		)
	portrait_layer = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
	portrait_layer.alpha_composite(portrait, offset)
	window = Image.new("L", CARD_SIZE, 0)
	ImageDraw.Draw(window).polygon(PORTRAIT_WINDOW, fill=255)
	portrait_layer.putalpha(
		ImageChops.multiply(portrait_layer.getchannel("A"), window)
	)
	card.alpha_composite(portrait_layer)
	card.alpha_composite(paper)
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
	for red, green, blue, alpha in image.get_flattened_data():
		raw.extend((blue, green, red, alpha))

	output.parent.mkdir(parents=True, exist_ok=True)
	output.write_bytes(b"DDS " + header + raw)


def main() -> None:
	args = parse_args()
	source = Image.open(args.source)
	frame = load_layer(args.frame, "Frame")
	paper = load_layer(args.paper, "Paper")
	card = compose(
		source,
		frame,
		paper,
		tuple(args.crop) if args.crop is not None else None,
		tuple(args.portrait_offset) if args.portrait_offset is not None else None,
		tuple(args.portrait_center),
		tuple(args.portrait_size),
		args.rotation,
		args.sepia_strength,
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
