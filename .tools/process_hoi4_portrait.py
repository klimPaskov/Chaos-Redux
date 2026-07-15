#!/usr/bin/env python3
"""Finish a style-approved portrait master for HOI4 leader or advisor use.

This tool is a deterministic finishing and presentation step. It does not
invent a person's face or draw advisor-card artwork, and it is not a substitute
for source research or the required visual review against the canonical
event-assets skill references in ``assets/vanilla_reference/portraits/leaders``
and ``assets/vanilla_reference/portraits/advisors``.

Real people must start from an attributed archival image. Pass an explicit
head-and-shoulders crop, preserve the person's recognisable features, and
reject the result if the source is too weak to survive the HOI4 finish.
Fictional portraits may start from an approved ImageGen master. Advisor mode
also requires separately generated, alpha-processed frame and paper overlays.
The script only crops, grades, angles, shadows, composites, validates, and
exports those approved sources.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps


LEADER_SIZE = (156, 210)
ADVISOR_SIZE = (65, 67)
PROCESSOR_VERSION = "2.0"
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


def sha256_file(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def load_generated_overlay(path: Path, label: str) -> Image.Image:
	if not path.is_file():
		raise FileNotFoundError(f"Missing {label} overlay: {path}")
	with Image.open(path) as image:
		overlay = image.convert("RGBA")
	alpha = overlay.getchannel("A")
	minimum, maximum = alpha.getextrema()
	if minimum != 0 or maximum == 0:
		raise ValueError(
			f"{label} overlay must contain real transparent and visible pixels; "
			f"alpha extrema were {(minimum, maximum)} for {path}"
		)
	visible = sum(1 for value in alpha.getdata() if value > 8)
	coverage = visible / (overlay.width * overlay.height)
	if coverage < 0.01 or coverage > 0.92:
		raise ValueError(
			f"{label} overlay has implausible visible coverage {coverage:.3f}: {path}"
		)
	return overlay


def trim_transparent(image: Image.Image, label: str) -> Image.Image:
	box = image.getchannel("A").getbbox()
	if box is None:
		raise ValueError(f"{label} overlay has no visible bounds")
	return image.crop(box)


def fit_overlay(image: Image.Image, size: tuple[int, int], label: str) -> Image.Image:
	trimmed = trim_transparent(image, label)
	contained = ImageOps.contain(trimmed, size, Image.Resampling.LANCZOS)
	result = Image.new("RGBA", size, (0, 0, 0, 0))
	result.alpha_composite(
		contained,
		((size[0] - contained.width) // 2, (size[1] - contained.height) // 2),
	)
	return result


def alpha_shadow(layer: Image.Image, opacity: float, blur: float) -> Image.Image:
	alpha = layer.getchannel("A").point(lambda value: round(value * opacity))
	shadow = Image.new("RGBA", layer.size, (0, 0, 0, 255))
	shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(blur)))
	return shadow


def composite_with_shadow(
	canvas: Image.Image,
	layer: Image.Image,
	position: tuple[int, int],
	shadow_offset: tuple[int, int],
	opacity: float,
	blur: float,
) -> None:
	shadow = alpha_shadow(layer, opacity, blur)
	canvas.alpha_composite(
		shadow,
		(position[0] + shadow_offset[0], position[1] + shadow_offset[1]),
	)
	canvas.alpha_composite(layer, position)


def make_advisor(
	source_crop: Image.Image,
	source_kind: str,
	seed_text: str,
	frame_overlay: Image.Image,
	paper_overlay: Image.Image,
) -> Image.Image:
	# The portrait panel is an explicit crop/grade only. Its rectangular bounds
	# sit beneath the generated frame, whose irregular alpha supplies the visible
	# card silhouette and transparent outer corners.
	portrait = ImageOps.fit(
		source_crop,
		(48, 59),
		method=Image.Resampling.LANCZOS,
		centering=(0.5, 0.38),
	)
	portrait = hoi4_finish(portrait, source_kind, seed_text + ":advisor")

	card = Image.new("RGBA", (56, 65), (0, 0, 0, 0))
	card.alpha_composite(portrait, (3, 3))
	card.alpha_composite(fit_overlay(frame_overlay, card.size, "frame"))
	card = card.rotate(
		-0.85,
		resample=Image.Resampling.BICUBIC,
		expand=True,
		fillcolor=(0, 0, 0, 0),
	)

	canvas = Image.new("RGBA", ADVISOR_SIZE, (0, 0, 0, 0))
	card_x = max(0, (ADVISOR_SIZE[0] - card.width) // 2 - 3)
	card_y = max(0, (ADVISOR_SIZE[1] - card.height) // 2)
	composite_with_shadow(canvas, card, (card_x, card_y), (2, 2), 0.58, 1.45)

	# The paper, patina, seal, and illegible dossier marks all originate in the
	# generated overlay. The script only sizes, angles, shadows, and composites it.
	paper = fit_overlay(paper_overlay, (27, 39), "paper")
	paper = paper.rotate(
		-4.25,
		resample=Image.Resampling.BICUBIC,
		expand=True,
		fillcolor=(0, 0, 0, 0),
	)
	composite_with_shadow(canvas, paper, (37, 24), (1, 2), 0.50, 1.0)
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
	parser.add_argument(
		"--source-kind",
		choices=("real", "fictional", "collective", "symbolic"),
		required=True,
	)
	parser.add_argument("--review-sheet", type=Path, required=True)
	parser.add_argument("--metadata", type=Path)
	parser.add_argument("--reference-dir", type=Path)
	parser.add_argument(
		"--advisor-frame-overlay",
		type=Path,
		help="Required ImageGen-authored transparent frame overlay for advisor mode",
	)
	parser.add_argument(
		"--advisor-paper-overlay",
		type=Path,
		help="Required ImageGen-authored transparent dossier-paper overlay for advisor mode",
	)
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
		overlay_metadata = None
	else:
		if args.advisor_frame_overlay is None or args.advisor_paper_overlay is None:
			raise ValueError(
				"advisor mode requires --advisor-frame-overlay and --advisor-paper-overlay; "
				"the processor never draws fallback dossier artwork"
			)
		frame_overlay = load_generated_overlay(args.advisor_frame_overlay, "frame")
		paper_overlay = load_generated_overlay(args.advisor_paper_overlay, "paper")
		finished = make_advisor(
			source_crop,
			args.source_kind,
			seed_text,
			frame_overlay,
			paper_overlay,
		)
		reference_dir = args.reference_dir or Path(__file__).resolve().parents[1] / REFERENCE_ROOT / "advisors"
		overlay_metadata = {
			"frame": {
				"path": str(args.advisor_frame_overlay),
				"sha256": sha256_file(args.advisor_frame_overlay),
				"size": list(frame_overlay.size),
				"alpha_extrema": list(frame_overlay.getchannel("A").getextrema()),
			},
			"paper": {
				"path": str(args.advisor_paper_overlay),
				"sha256": sha256_file(args.advisor_paper_overlay),
				"size": list(paper_overlay.size),
				"alpha_extrema": list(paper_overlay.getchannel("A").getextrema()),
			},
		}

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
		"source_sha256": sha256_file(args.source),
		"generated_overlays": overlay_metadata,
		"composition_contract": (
			"crop_grade_angle_alpha_shadow_composite_export_only; "
			"no programmatically drawn advisor-card artwork"
			if args.mode == "advisor"
			else "crop_grade_export_only; no programmatically drawn leader subject, emblem, or institutional scene"
		),
		"status": "candidate_requires_visual_approval",
	}
	metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()
