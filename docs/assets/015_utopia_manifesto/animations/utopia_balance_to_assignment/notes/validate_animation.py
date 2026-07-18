#!/usr/bin/env python3
"""Validate one Event 015 HOI4 animation package and its runtime DDS files."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageSequence, ImageStat


FRAME_SIZE = (158, 24)
FRAME_COUNT = 8
SHEET_SIZE = (1264, 24)


def digest(path: Path) -> str:
	return hashlib.sha256(path.read_bytes()).hexdigest()


def dds_info(path: Path, expected_size: tuple[int, int], png_path: Path) -> dict[str, object]:
	data = path.read_bytes()
	if data[:4] != b"DDS ":
		raise SystemExit(f"{path}: missing DDS magic")
	header = struct.unpack("<31I", data[4:128])
	size = header[0]
	flags = header[1]
	height = header[2]
	width = header[3]
	pitch = header[4]
	pf_size = header[18]
	pf_flags = header[19]
	fourcc = header[20]
	bit_count = header[21]
	r_mask, g_mask, b_mask, a_mask = header[22:26]
	caps = header[26]
	expected_length = 128 + width * height * 4
	checks = {
		"header_size_124": size == 124,
		"dimensions": (width, height) == expected_size,
		"pitch": pitch == width * 4,
		"pixel_format_offset_76_size_32": pf_size == 32,
		"pixel_format_flags_65": pf_flags == 65,
		"fourcc_zero": fourcc == 0,
		"bit_count_32": bit_count == 32,
		"bgra_masks": [r_mask, g_mask, b_mask, a_mask] == [0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000],
		"caps_texture": caps == 0x1000,
		"exact_length": len(data) == expected_length,
	}
	if not all(checks.values()):
		raise SystemExit(f"{path}: DDS validation failed: {checks}")
	pixels = data[128:]
	alpha = pixels[3::4]
	rgba = bytearray(len(pixels))
	for offset in range(0, len(pixels), 4):
		b, g, r, a = pixels[offset : offset + 4]
		rgba[offset : offset + 4] = bytes((r, g, b, a))
	with Image.open(png_path) as opened:
		png = opened.convert("RGBA")
		pixel_match = bytes(rgba) == png.tobytes()
	if not pixel_match:
		raise SystemExit(f"{path}: DDS pixel payload does not exactly match {png_path}")
	return {
		"path": path.as_posix(),
		"sha256": digest(path),
		"file_length": len(data),
		"declared_width": width,
		"declared_height": height,
		"header_flags": flags,
		"alpha_min": min(alpha),
		"alpha_max": max(alpha),
		"png_pixel_match": pixel_match,
		"checks": checks,
	}


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--root", required=True, type=Path)
	parser.add_argument("--slug", required=True)
	parser.add_argument("--runtime-dir", required=True, type=Path)
	args = parser.parse_args()

	root = args.root.resolve()
	sources = sorted((root / "source_frames").glob(f"{args.slug}_???_source.png"))
	processed_paths = sorted((root / "processed_frames").glob(f"{args.slug}_???.png"))
	if len(sources) != FRAME_COUNT or len(processed_paths) != FRAME_COUNT:
		raise SystemExit("source or processed frame count is not eight")

	source_hashes = [digest(path) for path in sources]
	processed_hashes = [digest(path) for path in processed_paths]
	if len(set(source_hashes)) != FRAME_COUNT or len(set(processed_hashes)) != FRAME_COUNT:
		raise SystemExit("duplicate source or processed frame detected")

	frames: list[Image.Image] = []
	for path in processed_paths:
		with Image.open(path) as opened:
			frame = opened.convert("RGBA")
		if frame.size != FRAME_SIZE:
			raise SystemExit(f"{path}: wrong frame size {frame.size}")
		if frame.getchannel("A").getextrema() != (255, 255):
			raise SystemExit(f"{path}: unexpected alpha range")
		frames.append(frame.copy())

	differences: list[dict[str, object]] = []
	for index in range(FRAME_COUNT - 1):
		diff = ImageChops.difference(frames[index].convert("RGB"), frames[index + 1].convert("RGB"))
		stat = ImageStat.Stat(diff)
		rms = [round(value, 4) for value in stat.rms]
		mean_rms = round(sum(stat.rms) / 3, 4)
		if mean_rms <= 2.0:
			raise SystemExit(f"frames {index} and {index + 1} are not visually distinct enough: {mean_rms}")
		differences.append({"from": index, "to": index + 1, "rgb_rms": rms, "mean_rms": mean_rms})

	sheet_path = root / "sheets" / f"{args.slug}_sheet.png"
	static_path = root / "sheets" / f"{args.slug}_static.png"
	with Image.open(sheet_path) as opened:
		sheet = opened.convert("RGBA")
	if sheet.size != SHEET_SIZE:
		raise SystemExit(f"wrong sheet size: {sheet.size}")
	for index, frame in enumerate(frames):
		if sheet.crop((index * FRAME_SIZE[0], 0, (index + 1) * FRAME_SIZE[0], FRAME_SIZE[1])).tobytes() != frame.tobytes():
			raise SystemExit(f"sheet segment {index} does not match processed frame")
	with Image.open(static_path) as opened:
		static = opened.convert("RGBA")
	if static.tobytes() != frames[7].tobytes():
		raise SystemExit("static fallback is not frame 007")

	gif_path = root / "previews" / f"{args.slug}_preview.gif"
	with Image.open(gif_path) as opened:
		gif_frames = [frame.copy() for frame in ImageSequence.Iterator(opened)]
		durations = [frame.info.get("duration") for frame in ImageSequence.Iterator(opened)]
		gif_size = opened.size
	if len(gif_frames) != FRAME_COUNT or gif_size != (632, 96):
		raise SystemExit(f"unexpected GIF frame count or size: {len(gif_frames)}, {gif_size}")

	runtime_dir = args.runtime_dir.resolve()
	sheet_dds = runtime_dir / f"{args.slug}_sheet.dds"
	static_dds = runtime_dir / f"{args.slug}_static.dds"
	report = {
		"slug": args.slug,
		"source_frame_count": len(sources),
		"processed_frame_count": len(processed_paths),
		"source_hashes_unique": True,
		"processed_hashes_unique": True,
		"frame_size": list(FRAME_SIZE),
		"sheet_size": list(SHEET_SIZE),
		"static_fallback_frame": 7,
		"gif_review_only": True,
		"gif_frame_count": len(gif_frames),
		"gif_size": list(gif_size),
		"gif_durations_ms": durations,
		"consecutive_frame_differences": differences,
		"dds": [
			dds_info(sheet_dds, SHEET_SIZE, sheet_path),
			dds_info(static_dds, FRAME_SIZE, static_path),
		],
	}
	output = root / "metadata" / "validation_report.json"
	output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
	main()

