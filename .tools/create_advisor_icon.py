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
import math
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps


CARD_SIZE = (65, 67)
PORTRAIT_WINDOW = ((10, 8), (40, 8), (40, 56), (11, 57))
DEFAULT_PORTRAIT_CENTER = (25.0, 32.5)
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
		"--portrait-center",
		type=float,
		nargs=2,
		metavar=("X", "Y"),
		default=DEFAULT_PORTRAIT_CENTER,
		help="Stable center of the frame opening (default: 25 32.5).",
	)
	parser.add_argument(
		"--portrait-size",
		type=int,
		nargs=2,
		default=None,
		metavar=("MIN_WIDTH", "MIN_HEIGHT"),
		help=(
			"Optional minimum cover box before rotation. The automatic "
			"corner-to-corner frame fit remains active and aspect ratio is "
			"always preserved."
		),
	)
	parser.add_argument("--rotation", type=float, default=-3.0)
	parser.add_argument(
		"--portrait-zoom",
		type=float,
		default=1.02,
		help="Extra proportional cover margin after corner fitting (default: 1.02).",
	)
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


def calculate_corner_cover_scale(
	source_size: tuple[int, int],
	minimum_size: tuple[int, int] | None,
	center: tuple[float, float],
	rotation: float,
	zoom: float,
) -> float:
	if zoom < 1.0:
		raise ValueError("--portrait-zoom must be at least 1.0")

	angle = math.radians(rotation)
	cosine = math.cos(angle)
	sine = math.sin(angle)
	max_local_x = 0.0
	max_local_y = 0.0
	for corner_x, corner_y in PORTRAIT_WINDOW:
		delta_x = corner_x - center[0]
		delta_y = corner_y - center[1]
		local_x = cosine * delta_x + sine * delta_y
		local_y = -sine * delta_x + cosine * delta_y
		max_local_x = max(max_local_x, abs(local_x))
		max_local_y = max(max_local_y, abs(local_y))

	scale = max(
		(2.0 * max_local_x) / source_size[0],
		(2.0 * max_local_y) / source_size[1],
	)
	if minimum_size is not None:
		minimum_width, minimum_height = minimum_size
		if minimum_width < 1 or minimum_height < 1:
			raise ValueError("--portrait-size values must be positive")
		scale = max(
			scale,
			minimum_width / source_size[0],
			minimum_height / source_size[1],
		)
	return scale * zoom


def prepare_portrait(
	source: Image.Image,
	crop: tuple[int, int, int, int] | None,
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
	return portrait


def render_portrait_layer(
	portrait: Image.Image,
	minimum_size: tuple[int, int] | None,
	center: tuple[float, float],
	rotation: float,
	zoom: float,
) -> Image.Image:
	scale = calculate_corner_cover_scale(
		portrait.size,
		minimum_size,
		center,
		rotation,
		zoom,
	)
	angle = math.radians(rotation)
	cosine = math.cos(angle)
	sine = math.sin(angle)
	inverse_scale = 1.0 / scale
	a = cosine * inverse_scale
	b = sine * inverse_scale
	d = -sine * inverse_scale
	e = cosine * inverse_scale
	c = portrait.width / 2.0 - a * center[0] - b * center[1]
	f = portrait.height / 2.0 - d * center[0] - e * center[1]
	return portrait.transform(
		CARD_SIZE,
		Image.Transform.AFFINE,
		(a, b, c, d, e, f),
		resample=Image.Resampling.BICUBIC,
		fillcolor=(0, 0, 0, 0),
	)


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
	center: tuple[float, float],
	minimum_size: tuple[int, int] | None,
	rotation: float,
	zoom: float,
	sepia_strength: float,
) -> Image.Image:
	card = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
	card.alpha_composite(frame)

	portrait = prepare_portrait(source, crop, sepia_strength)
	portrait_layer = render_portrait_layer(
		portrait,
		minimum_size,
		center,
		rotation,
		zoom,
	)
	window = Image.new("L", CARD_SIZE, 0)
	ImageDraw.Draw(window).polygon(PORTRAIT_WINDOW, fill=255)
	frame_footprint = frame.getchannel("A").point(
		lambda alpha: 255 if alpha > 0 else 0
	)
	paper_footprint = paper.getchannel("A").point(
		lambda alpha: 255 if alpha > 8 else 0
	)
	paper_footprint = paper_footprint.filter(ImageFilter.MaxFilter(3))
	portrait_visibility = ImageChops.subtract(
		window,
		ImageChops.lighter(frame_footprint, paper_footprint),
	)
	portrait_layer.putalpha(
		ImageChops.multiply(
			portrait_layer.getchannel("A"),
			portrait_visibility,
		)
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
		tuple(args.portrait_center),
		tuple(args.portrait_size) if args.portrait_size is not None else None,
		args.rotation,
		args.portrait_zoom,
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
