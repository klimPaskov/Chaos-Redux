#!/usr/bin/env python3
"""Finish a style-approved portrait master for HOI4 leader or advisor use.

This tool is a deterministic finishing and presentation step. It does not
invent a person's face and it is not a substitute for source research or the
required visual review against the canonical event-assets skill references in
``assets/vanilla_reference/portraits/leaders`` and
``assets/vanilla_reference/portraits/advisors``.

Real people must start from an attributed archival image. Pass an explicit
head-and-shoulders crop, preserve the person's recognisable features, and
reject the result if the source is too weak to survive the HOI4 finish.
Fictional portraits may start from an approved imagegen master.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


LEADER_SIZE = (156, 210)
ADVISOR_SIZE = (65, 67)
PROCESSOR_VERSION = "1.1"
REFERENCE_ROOT = Path(
	".agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits"
)


def parse_crop(values: list[int], image: Image.Image) -> tuple[int, int, int, int]:
	left, top, right, bottom = values
	if left < 0 or top < 0 or right > image.width or bottom > image.height:
		raise ValueError(f"Crop {values} is outside the {image.width}x{image.height} source")
	if right <= left or bottom <= top:
		raise ValueError(f"Crop must have positive width and height: {values}")
	return left, top, right, bottom


def deterministic_noise(size: tuple[int, int], seed_text: str) -> Image.Image:
	seed = int(hashlib.sha256(seed_text.encode("utf-8")).hexdigest()[:8], 16)
	state = seed
	pixels: list[int] = []
	for _ in range(size[0] * size[1]):
		state = (1664525 * state + 1013904223) & 0xFFFFFFFF
		pixels.append(118 + ((state >> 24) % 21))
	noise = Image.new("L", size)
	noise.putdata(pixels)
	return noise.filter(ImageFilter.GaussianBlur(0.35))


def vignette_mask(size: tuple[int, int]) -> Image.Image:
	width, height = size
	mask = Image.new("L", size)
	pixels: list[int] = []
	for y in range(height):
		vertical = (y - height * 0.43) / (height * 0.62)
		for x in range(width):
			horizontal = (x - width * 0.5) / (width * 0.68)
			distance = math.sqrt(horizontal * horizontal + vertical * vertical)
			pixels.append(max(0, min(255, round((distance - 0.50) * 145))))
	mask.putdata(pixels)
	return mask.filter(ImageFilter.GaussianBlur(max(2, width // 24)))


def hoi4_finish(image: Image.Image, source_kind: str, seed_text: str) -> Image.Image:
	alpha = image.getchannel("A")
	rgb = image.convert("RGB")
	rgb = ImageEnhance.Contrast(rgb).enhance(1.075)
	rgb = ImageEnhance.Color(rgb).enhance(0.88 if source_kind == "real" else 0.94)

	# A restrained edge-preserving blend softens photographic micro-detail while
	# retaining the face, eyes, hairline, uniform edges, and other identity cues.
	smoothed = rgb.filter(ImageFilter.MedianFilter(3))
	rgb = Image.blend(rgb, smoothed, 0.14 if source_kind == "real" else 0.10)
	rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.15, percent=72, threshold=4))

	# Warm highlights and cool charcoal shadows mirror the restrained painted
	# palette of the bundled vanilla references without colourising a new face.
	luma = ImageOps.grayscale(rgb)
	warm = Image.new("RGB", rgb.size, (126, 91, 59))
	cool = Image.new("RGB", rgb.size, (40, 47, 53))
	warm_mask = luma.point(lambda value: max(0, min(31, round((value - 108) * 0.19))))
	cool_mask = luma.point(lambda value: max(0, min(23, round((112 - value) * 0.17))))
	rgb = Image.composite(warm, rgb, warm_mask)
	rgb = Image.composite(cool, rgb, cool_mask)

	grain = deterministic_noise(rgb.size, seed_text)
	grain_rgb = Image.merge("RGB", (grain, grain, grain))
	rgb = Image.blend(rgb, grain_rgb, 0.035)

	dark = Image.new("RGB", rgb.size, (22, 25, 27))
	rgb = Image.composite(dark, rgb, vignette_mask(rgb.size))
	result = rgb.convert("RGBA")
	result.putalpha(alpha)
	return result


def make_leader(source_crop: Image.Image, source_kind: str, seed_text: str) -> Image.Image:
	resized = ImageOps.fit(
		source_crop,
		LEADER_SIZE,
		method=Image.Resampling.LANCZOS,
		centering=(0.5, 0.44),
	)
	return hoi4_finish(resized, source_kind, seed_text)


def vertical_gradient(size: tuple[int, int], top: tuple[int, ...], bottom: tuple[int, ...]) -> Image.Image:
	image = Image.new("RGBA", size)
	draw = ImageDraw.Draw(image)
	for y in range(size[1]):
		ratio = y / max(1, size[1] - 1)
		colour = tuple(round(top[index] * (1 - ratio) + bottom[index] * ratio) for index in range(4))
		draw.line((0, y, size[0], y), fill=colour)
	return image


def make_advisor(source_crop: Image.Image, source_kind: str, seed_text: str) -> Image.Image:
	canvas = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))

	shadow = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	shadow_draw = ImageDraw.Draw(shadow)
	shadow_draw.rounded_rectangle((3, 3, 54, 65), radius=4, fill=(0, 0, 0, 178))
	shadow = shadow.filter(ImageFilter.GaussianBlur(2.1))
	canvas.alpha_composite(shadow)

	outer = vertical_gradient((53, 65), (74, 73, 68, 255), (20, 22, 23, 255))
	outer_mask = Image.new("L", outer.size, 0)
	ImageDraw.Draw(outer_mask).rounded_rectangle((0, 0, 52, 64), radius=4, fill=255)
	outer.putalpha(outer_mask)
	canvas.alpha_composite(outer, (1, 0))

	frame_draw = ImageDraw.Draw(canvas)
	frame_draw.rounded_rectangle((2, 1, 52, 64), radius=4, outline=(144, 132, 108, 230), width=1)
	frame_draw.rounded_rectangle((4, 3, 50, 62), radius=2, outline=(8, 10, 11, 245), width=2)

	portrait = ImageOps.fit(
		source_crop,
		(43, 56),
		method=Image.Resampling.LANCZOS,
		centering=(0.5, 0.39),
	)
	portrait = hoi4_finish(portrait, source_kind, seed_text + ":advisor")
	portrait_mask = Image.new("L", portrait.size, 0)
	ImageDraw.Draw(portrait_mask).rounded_rectangle((0, 0, 42, 55), radius=1, fill=255)
	portrait.putalpha(ImageChops.multiply(portrait.getchannel("A"), portrait_mask))
	canvas.alpha_composite(portrait, (5, 5))

	# The vanilla advisor surface presents the portrait as a dossier card. This
	# original paper overlay reproduces that UI grammar without copying a vanilla
	# advisor asset or adding readable/generated text.
	paper = Image.new("RGBA", (27, 38), (0, 0, 0, 0))
	paper_shadow = Image.new("RGBA", paper.size, (0, 0, 0, 0))
	ImageDraw.Draw(paper_shadow).rounded_rectangle((3, 3, 25, 36), radius=1, fill=(0, 0, 0, 155))
	paper_shadow = paper_shadow.filter(ImageFilter.GaussianBlur(1.2))
	paper.alpha_composite(paper_shadow)
	paper_draw = ImageDraw.Draw(paper)
	paper_draw.polygon(((1, 1), (22, 0), (25, 33), (4, 36)), fill=(220, 207, 171, 255))
	paper_draw.line(((2, 2), (22, 1), (24, 32)), fill=(245, 235, 207, 220), width=1)
	for y, width in ((9, 13), (13, 16), (17, 12), (22, 15), (26, 10)):
		paper_draw.line((7, y, 7 + width, y - 1), fill=(102, 89, 68, 150), width=1)
	paper_draw.ellipse((7, 28, 13, 34), fill=(112, 45, 36, 205), outline=(61, 34, 28, 220), width=1)
	paper = paper.rotate(-3.5, resample=Image.Resampling.BICUBIC, expand=False)
	canvas.alpha_composite(paper, (37, 24))

	return canvas


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
	background = Image.new("RGBA", size, (92, 92, 92, 255))
	draw = ImageDraw.Draw(background)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)), fill=(132, 132, 132, 255))
	return background


def make_review_sheet(
	source_crop: Image.Image,
	finished: Image.Image,
	mode: str,
	reference_dir: Path,
	output: Path,
) -> None:
	if mode == "leader":
		reference_names = ("den_thorvald_stauning.png", "fin_carl_mannerheim.png")
		display_size = LEADER_SIZE
		scale = 2
	else:
		reference_names = ("generic_europe_1.png", "generic_asia_1.png")
		display_size = ADVISOR_SIZE
		scale = 4

	items: list[tuple[str, Image.Image]] = [
		("explicit source crop", ImageOps.fit(source_crop, display_size, Image.Resampling.LANCZOS)),
		("processed candidate", finished),
	]
	for name in reference_names:
		path = reference_dir / name
		if not path.is_file():
			raise FileNotFoundError(f"Missing review reference: {path}")
		with Image.open(path) as image:
			items.append((name.removeprefix("vanilla_").removesuffix(".png"), image.convert("RGBA")))

	cell_width = display_size[0] * scale + 24
	cell_height = display_size[1] * scale + 44
	sheet = Image.new("RGBA", (cell_width * len(items), cell_height), (28, 30, 32, 255))
	draw = ImageDraw.Draw(sheet)
	for index, (label, image) in enumerate(items):
		preview = ImageOps.fit(image, display_size, Image.Resampling.LANCZOS).resize(
			(display_size[0] * scale, display_size[1] * scale),
			Image.Resampling.NEAREST if mode == "advisor" else Image.Resampling.LANCZOS,
		)
		base = checker(preview.size)
		base.alpha_composite(preview)
		x = index * cell_width + 12
		sheet.alpha_composite(base, (x, 10))
		draw.text((x, preview.height + 20), label, fill=(236, 236, 232, 255))
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.save(output)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("mode", choices=("leader", "advisor"))
	parser.add_argument("source", type=Path)
	parser.add_argument("output", type=Path)
	parser.add_argument(
		"--crop",
		nargs=4,
		type=int,
		metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
		required=True,
		help="Required head-and-shoulders crop in source pixels",
	)
	parser.add_argument("--source-kind", choices=("real", "fictional", "collective"), required=True)
	parser.add_argument("--review-sheet", type=Path, required=True)
	parser.add_argument("--metadata", type=Path)
	parser.add_argument("--reference-dir", type=Path)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	if not args.source.is_file():
		raise FileNotFoundError(args.source)
	with Image.open(args.source) as image:
		source = image.convert("RGBA")
	crop_box = parse_crop(args.crop, source)
	source_crop = source.crop(crop_box)
	seed_text = f"{args.source.resolve()}:{crop_box}:{args.source_kind}:{PROCESSOR_VERSION}"
	if args.mode == "leader":
		finished = make_leader(source_crop, args.source_kind, seed_text)
		reference_dir = args.reference_dir or Path(__file__).resolve().parents[1] / REFERENCE_ROOT / "leaders"
	else:
		finished = make_advisor(source_crop, args.source_kind, seed_text)
		reference_dir = args.reference_dir or Path(__file__).resolve().parents[1] / REFERENCE_ROOT / "advisors"

	args.output.parent.mkdir(parents=True, exist_ok=True)
	finished.save(args.output)
	make_review_sheet(source_crop, finished, args.mode, reference_dir, args.review_sheet)

	metadata_path = args.metadata or args.output.with_suffix(args.output.suffix + ".json")
	metadata_path.parent.mkdir(parents=True, exist_ok=True)
	metadata = {
		"processor": ".tools/process_hoi4_portrait.py",
		"processor_version": PROCESSOR_VERSION,
		"mode": args.mode,
		"source": str(args.source),
		"source_kind": args.source_kind,
		"crop": list(crop_box),
		"output": str(args.output),
		"size": list(finished.size),
		"review_sheet": str(args.review_sheet),
		"reference_dir": str(reference_dir),
		"status": "candidate_requires_visual_approval",
	}
	metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
