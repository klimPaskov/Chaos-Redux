"""Place a processed portrait beneath the canonical HOI4 advisor template.

The portrait is center-cropped without distortion, sampled to the requested
fractional size, rotated around the advisor opening center, and offset from
that center. The supplied template is then composited unchanged over the
portrait. The script writes a review PNG and a one-level 32-bit BGRA DDS.
"""

from __future__ import annotations

import argparse
import math
import struct
from pathlib import Path

from PIL import Image, ImageOps


CARD_SIZE = (65, 67)
TEMPLATE_OPENING_CENTER = (25.0, 32.5)
DEFAULT_PORTRAIT_SIZE = (25.03, 31.38)
DEFAULT_PORTRAIT_OFFSET = (7.0, -2.0)
DEFAULT_ROTATION = -3.75
MOD_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = (
	MOD_ROOT
	/ ".agents"
	/ "skills"
	/ "chaos-redux-event-assets"
	/ "assets"
	/ "vanilla_reference"
	/ "portraits"
	/ "advisors"
	/ "advisor_template.png"
)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source", type=Path, required=True)
	parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
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
		"--template-center",
		type=float,
		nargs=2,
		metavar=("X", "Y"),
		default=TEMPLATE_OPENING_CENTER,
		help="Center of the portrait opening in the template (default: 25 32.5).",
	)
	parser.add_argument(
		"--portrait-size",
		type=float,
		nargs=2,
		metavar=("WIDTH", "HEIGHT"),
		default=DEFAULT_PORTRAIT_SIZE,
		help="Pre-rotation portrait size in pixels (default: 25.03 31.38).",
	)
	parser.add_argument(
		"--portrait-offset",
		type=float,
		nargs=2,
		metavar=("RIGHT", "DOWN"),
		default=DEFAULT_PORTRAIT_OFFSET,
		help="Offset from template center (default: 7 right, 2 up).",
	)
	parser.add_argument(
		"--rotation",
		type=float,
		default=DEFAULT_ROTATION,
		help="Portrait rotation in degrees (default: -3.75).",
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


def calculate_center_crop(
	source_size: tuple[int, int],
	target_size: tuple[float, float],
) -> tuple[float, float, float, float]:
	source_width, source_height = source_size
	target_width, target_height = target_size
	if target_width <= 0.0 or target_height <= 0.0:
		raise ValueError("--portrait-size values must be positive")

	target_aspect = target_width / target_height
	source_aspect = source_width / source_height
	if source_aspect < target_aspect:
		crop_width = float(source_width)
		crop_height = crop_width / target_aspect
	else:
		crop_height = float(source_height)
		crop_width = crop_height * target_aspect
	left = (source_width - crop_width) / 2.0
	top = (source_height - crop_height) / 2.0
	return left, top, left + crop_width, top + crop_height


def render_portrait_layer(
	portrait: Image.Image,
	target_size: tuple[float, float],
	center: tuple[float, float],
	rotation: float,
) -> Image.Image:
	left, top, right, bottom = calculate_center_crop(portrait.size, target_size)
	crop_width = right - left
	crop_height = bottom - top
	scale_x = target_size[0] / crop_width
	scale_y = target_size[1] / crop_height
	if not math.isclose(scale_x, scale_y, rel_tol=0.0, abs_tol=1e-12):
		raise AssertionError("Portrait transform would distort the source aspect ratio")

	scale = scale_x
	angle = math.radians(rotation)
	cosine = math.cos(angle)
	sine = math.sin(angle)
	inverse_scale = 1.0 / scale
	a = cosine * inverse_scale
	b = sine * inverse_scale
	d = -sine * inverse_scale
	e = cosine * inverse_scale
	source_center_x = (left + right) / 2.0
	source_center_y = (top + bottom) / 2.0
	c = source_center_x - a * center[0] - b * center[1]
	f = source_center_y - d * center[0] - e * center[1]
	return portrait.transform(
		CARD_SIZE,
		Image.Transform.AFFINE,
		(a, b, c, d, e, f),
		resample=Image.Resampling.BICUBIC,
		fillcolor=(0, 0, 0, 0),
	)


def load_template(path: Path) -> Image.Image:
	template = Image.open(path).convert("RGBA")
	if template.size != CARD_SIZE:
		raise ValueError(
			f"Template must be {CARD_SIZE[0]}x{CARD_SIZE[1]}, got "
			f"{template.width}x{template.height}"
		)
	return template


def compose(
	source: Image.Image,
	template: Image.Image,
	crop: tuple[int, int, int, int] | None,
	template_center: tuple[float, float],
	portrait_size: tuple[float, float],
	portrait_offset: tuple[float, float],
	rotation: float,
	sepia_strength: float,
) -> Image.Image:
	portrait = prepare_portrait(source, crop, sepia_strength)
	portrait_center = (
		template_center[0] + portrait_offset[0],
		template_center[1] + portrait_offset[1],
	)
	card = render_portrait_layer(
		portrait,
		portrait_size,
		portrait_center,
		rotation,
	)
	card.alpha_composite(template)
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
	template = load_template(args.template)
	card = compose(
		source,
		template,
		tuple(args.crop) if args.crop is not None else None,
		tuple(args.template_center),
		tuple(args.portrait_size),
		tuple(args.portrait_offset),
		args.rotation,
		args.sepia_strength,
	)
	preview = args.preview.resolve()
	output = args.output.resolve()
	preview.parent.mkdir(parents=True, exist_ok=True)
	card.save(preview)
	write_bgra_dds(card, output)

	reopened = Image.open(output).convert("RGBA")
	if reopened.size != CARD_SIZE:
		raise ValueError(f"DDS reopened at {reopened.size}, expected {CARD_SIZE}")
	if reopened.tobytes() != card.tobytes():
		raise ValueError("DDS decoded pixels differ from the preview")
	expected_length = 128 + CARD_SIZE[0] * CARD_SIZE[1] * 4
	if output.stat().st_size != expected_length:
		raise ValueError("DDS length does not match one-level BGRA layout")


if __name__ == "__main__":
	main()
