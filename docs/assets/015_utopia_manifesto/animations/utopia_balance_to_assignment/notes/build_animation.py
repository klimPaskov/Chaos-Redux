#!/usr/bin/env python3
"""Mechanically normalise ImageGen-authored frames into HOI4 animation assets."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


FRAME_SIZE = (158, 24)
PREVIEW_SIZE = (632, 96)
FRAME_COUNT = 8


def digest(path: Path) -> str:
	hasher = hashlib.sha256()
	with path.open("rb") as stream:
		for chunk in iter(lambda: stream.read(1024 * 1024), b""):
			hasher.update(chunk)
	return hasher.hexdigest()


def labelled_contact(images: list[Image.Image], labels: list[str], output: Path, scale: int) -> None:
	font = ImageFont.load_default()
	cell_width = FRAME_SIZE[0] * scale + 16
	cell_height = FRAME_SIZE[1] * scale + 34
	sheet = Image.new("RGBA", (cell_width * 4, cell_height * 2), (22, 24, 24, 255))
	draw = ImageDraw.Draw(sheet)
	for index, image in enumerate(images):
		x = (index % 4) * cell_width + 8
		y = (index // 4) * cell_height + 8
		enlarged = image.resize((FRAME_SIZE[0] * scale, FRAME_SIZE[1] * scale), Image.Resampling.NEAREST)
		sheet.alpha_composite(enlarged, (x, y))
		draw.text((x, y + FRAME_SIZE[1] * scale + 6), labels[index], fill=(225, 215, 184, 255), font=font)
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.convert("RGB").save(output, optimize=True)


def source_contact(images: list[Image.Image], labels: list[str], output: Path) -> None:
	font = ImageFont.load_default()
	thumb_width = 420
	thumbs: list[Image.Image] = []
	for image in images:
		height = max(1, round(image.height * thumb_width / image.width))
		thumbs.append(image.resize((thumb_width, height), Image.Resampling.LANCZOS))
	cell_width = thumb_width + 16
	cell_height = max(image.height for image in thumbs) + 34
	sheet = Image.new("RGBA", (cell_width * 4, cell_height * 2), (22, 24, 24, 255))
	draw = ImageDraw.Draw(sheet)
	for index, image in enumerate(thumbs):
		x = (index % 4) * cell_width + 8
		y = (index // 4) * cell_height + 8
		sheet.alpha_composite(image, (x, y))
		draw.text((x, y + image.height + 6), labels[index], fill=(225, 215, 184, 255), font=font)
	output.parent.mkdir(parents=True, exist_ok=True)
	sheet.convert("RGB").save(output, optimize=True)


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--root", required=True, type=Path)
	parser.add_argument("--slug", required=True)
	parser.add_argument("--crop-left", required=True, type=int)
	parser.add_argument("--crop-right-margin", required=True, type=int)
	parser.add_argument("--crop-top", required=True, type=int)
	parser.add_argument("--crop-bottom", required=True, type=int)
	args = parser.parse_args()

	root = args.root.resolve()
	source_dir = root / "source_frames"
	processed_dir = root / "processed_frames"
	sheets_dir = root / "sheets"
	previews_dir = root / "previews"
	metadata_dir = root / "metadata"
	for directory in (processed_dir, sheets_dir, previews_dir, metadata_dir):
		directory.mkdir(parents=True, exist_ok=True)

	sources = sorted(source_dir.glob(f"{args.slug}_???_source.png"))
	if len(sources) != FRAME_COUNT:
		raise SystemExit(f"expected {FRAME_COUNT} sources, found {len(sources)}")

	processed: list[Image.Image] = []
	source_images: list[Image.Image] = []
	records: list[dict[str, object]] = []
	for index, source_path in enumerate(sources):
		with Image.open(source_path) as opened:
			source = opened.convert("RGBA")
		source_images.append(source.copy())
		crop_box = (
			args.crop_left,
			args.crop_top,
			source.width - args.crop_right_margin,
			args.crop_bottom,
		)
		if crop_box[0] < 0 or crop_box[1] < 0 or crop_box[2] > source.width or crop_box[3] > source.height:
			raise SystemExit(f"invalid crop {crop_box} for {source_path.name} at {source.size}")
		frame = source.crop(crop_box)
		frame = frame.resize(FRAME_SIZE, Image.Resampling.LANCZOS)
		frame = frame.filter(ImageFilter.UnsharpMask(radius=0.55, percent=55, threshold=2))
		frame = frame.convert("RGBA")
		output_path = processed_dir / f"{args.slug}_{index:03d}.png"
		frame.save(output_path, optimize=True)
		processed.append(frame)
		records.append(
			{
				"frame": index,
				"source_file": source_path.as_posix(),
				"source_dimensions": list(source.size),
				"source_sha256": digest(source_path),
				"crop_box": list(crop_box),
				"processed_file": output_path.as_posix(),
				"processed_dimensions": list(frame.size),
				"processed_sha256": digest(output_path),
				"alpha_extrema": list(frame.getchannel("A").getextrema()),
			}
		)

	sheet = Image.new("RGBA", (FRAME_SIZE[0] * FRAME_COUNT, FRAME_SIZE[1]), (0, 0, 0, 255))
	for index, frame in enumerate(processed):
		sheet.alpha_composite(frame, (index * FRAME_SIZE[0], 0))
	sheet_path = sheets_dir / f"{args.slug}_sheet.png"
	sheet.save(sheet_path, optimize=True)

	static_path = sheets_dir / f"{args.slug}_static.png"
	processed[-1].save(static_path, optimize=True)

	preview_frames = [frame.resize(PREVIEW_SIZE, Image.Resampling.NEAREST).convert("P", palette=Image.Palette.ADAPTIVE) for frame in processed]
	preview_path = previews_dir / f"{args.slug}_preview.gif"
	preview_frames[0].save(
		preview_path,
		save_all=True,
		append_images=preview_frames[1:],
		duration=[200] * 7 + [700],
		loop=0,
		disposal=2,
		optimize=False,
	)

	labels = [f"frame {index:03d}" for index in range(FRAME_COUNT)]
	labelled_contact(processed, labels, previews_dir / f"{args.slug}_contact.png", scale=4)
	source_contact(source_images, labels, previews_dir / f"{args.slug}_source_contact.png")

	report = {
		"slug": args.slug,
		"frame_size": list(FRAME_SIZE),
		"frame_count": FRAME_COUNT,
		"sheet_size": list(sheet.size),
		"fps": 5,
		"runtime_looping": False,
		"play_on_show": True,
		"static_fallback_frame": 7,
		"processing": "fixed shared crop, direct Lanczos resize, mild shared resampling sharpen, RGBA export",
		"sheet_png": sheet_path.as_posix(),
		"sheet_png_sha256": digest(sheet_path),
		"static_png": static_path.as_posix(),
		"static_png_sha256": digest(static_path),
		"preview_gif": preview_path.as_posix(),
		"preview_gif_sha256": digest(preview_path),
		"frames": records,
	}
	report_path = metadata_dir / "processing_report.json"
	report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()

