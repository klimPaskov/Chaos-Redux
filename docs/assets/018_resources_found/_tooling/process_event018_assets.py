#!/usr/bin/env python3
"""Process Event 018 generated masters into HOI4-ready PNG and DDS assets.

The script deliberately keeps source, keyed-alpha, processed, and runtime files
separate.  Chroma removal imports the canonical imagegen helper; DDS writing
imports the repository converter's uncompressed BGRA writer.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import importlib.util
import math
from pathlib import Path
import struct
import sys
from typing import Iterable

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps


REPO = Path(__file__).resolve().parents[4]
ASSET_ROOT = REPO / "docs/assets/018_resources_found"
SOURCE = ASSET_ROOT / "source_png"
KEYED = ASSET_ROOT / "keyed_alpha"
PROCESSED = ASSET_ROOT / "processed_png"
CONTACTS = ASSET_ROOT / "contact_sheets"
PREVIEWS = ASSET_ROOT / "previews"
CHROMA_HELPER = Path.home() / ".codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
DDS_HELPER = REPO / ".tools/convert_to_dds.py"
ACHIEVEMENT_OVERLAY = REPO / ".agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png"


def load_module(name: str, path: Path):
	spec = importlib.util.spec_from_file_location(name, path)
	if spec is None or spec.loader is None:
		raise RuntimeError(f"Cannot import {path}")
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


def chroma_one(job: tuple[str, str]) -> str:
	src_raw, out_raw = job
	src = Path(src_raw)
	out = Path(out_raw)
	chroma = load_module("event018_chroma", CHROMA_HELPER)
	with Image.open(src) as opened:
		rgba = opened.convert("RGBA")
	chroma._apply_alpha_to_image(
		rgba,
		key=(0, 255, 0),
		tolerance=12,
		spill_cleanup=True,
		soft_matte=True,
		transparent_threshold=12.0,
		opaque_threshold=96.0,
	)
	rgba = chroma._contract_alpha(rgba, 0)
	rgba = chroma._apply_edge_feather(rgba, 0.35)
	out.parent.mkdir(parents=True, exist_ok=True)
	rgba.save(out, "PNG", optimize=True)
	return str(out)


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
	alpha = image.getchannel("A")
	bbox = alpha.getbbox()
	if bbox is None:
		raise ValueError("Transparent source has no visible pixels")
	return bbox


def fit_transparent(image: Image.Image, size: tuple[int, int], padding: int, outline: float, shadow: float) -> Image.Image:
	scale = 4
	tw, th = size
	work = image.convert("RGBA").crop(alpha_bbox(image.convert("RGBA")))
	max_w = max(1, tw * scale - padding * scale * 2)
	max_h = max(1, th * scale - padding * scale * 2)
	ratio = min(max_w / work.width, max_h / work.height)
	work = work.resize((max(1, round(work.width * ratio)), max(1, round(work.height * ratio))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGBA", (tw * scale, th * scale), (0, 0, 0, 0))
	x = (canvas.width - work.width) // 2
	y = (canvas.height - work.height) // 2
	alpha = work.getchannel("A")

	if shadow > 0:
		shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=max(1.0, shadow * scale)))
		shadow_layer = Image.new("RGBA", work.size, (0, 0, 0, 0))
		shadow_layer.putalpha(shadow_alpha.point(lambda p: round(p * 0.72)))
		black = Image.new("RGBA", work.size, (3, 5, 6, 255))
		black.putalpha(shadow_layer.getchannel("A"))
		canvas.alpha_composite(black, (x + scale, y + scale))

	if outline > 0:
		radius = max(1, round(outline * scale))
		kernel = radius * 2 + 1
		if kernel % 2 == 0:
			kernel += 1
		dilated = alpha.filter(ImageFilter.MaxFilter(kernel))
		outline_alpha = ImageChops.subtract(dilated, alpha)
		outline_layer = Image.new("RGBA", work.size, (5, 8, 8, 255))
		outline_layer.putalpha(outline_alpha)
		canvas.alpha_composite(outline_layer, (x, y))

	canvas.alpha_composite(work, (x, y))
	return canvas.resize(size, Image.Resampling.LANCZOS)


def cover_opaque(image: Image.Image, size: tuple[int, int]) -> Image.Image:
	return ImageOps.fit(image.convert("RGB"), size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def write_dds(image: Image.Image, path: Path) -> None:
	dds = load_module("event018_dds", DDS_HELPER)
	rgba = image.convert("RGBA")
	path.parent.mkdir(parents=True, exist_ok=True)
	dds.write_bgra_dds(path, rgba.width, rgba.height, rgba.tobytes("raw", "BGRA"))


def process_transparent_family(
	family: str,
	size: tuple[int, int],
	runtime_dir: Path,
	padding: int,
	outline: float,
	shadow: float,
) -> list[Path]:
	src_dir = SOURCE / family
	files = sorted(src_dir.glob("*_source.png"))
	if not files:
		return []
	key_dir = KEYED / family
	jobs = [(str(src), str(key_dir / src.name.replace("_source.png", "_alpha.png"))) for src in files]
	# Keep peak memory/temp-file pressure low on the asset volume.
	workers = min(4, max(1, len(jobs)))
	with ProcessPoolExecutor(max_workers=workers) as pool:
		list(pool.map(chroma_one, jobs))
	outputs: list[Path] = []
	for src, (_, keyed_raw) in zip(files, jobs):
		keyed = Path(keyed_raw)
		name = src.name.replace("_source.png", "")
		with Image.open(keyed) as opened:
			final = fit_transparent(opened, size, padding, outline, shadow)
		out = PROCESSED / family / f"{name}.png"
		out.parent.mkdir(parents=True, exist_ok=True)
		final.save(out, "PNG", optimize=True)
		write_dds(final, runtime_dir / f"{name}.dds")
		outputs.append(out)
	return outputs


def process_category_pictures() -> list[Path]:
	files = sorted((SOURCE / "category_pictures").glob("*_source.png"))
	outputs: list[Path] = []
	for src in files:
		name = src.name.replace("_source.png", "")
		with Image.open(src) as opened:
			final = cover_opaque(opened, (114, 101))
		out = PROCESSED / "category_pictures" / f"{name}.png"
		out.parent.mkdir(parents=True, exist_ok=True)
		final.save(out, "PNG", optimize=True)
		write_dds(final, REPO / "gfx/interface/decisions/018_resources_found" / f"{name}.dds")
		outputs.append(out)
	return outputs


def process_achievements() -> list[Path]:
	files = sorted((SOURCE / "achievements").glob("*_source.png"))
	if not ACHIEVEMENT_OVERLAY.exists():
		raise FileNotFoundError(f"Canonical achievement overlay missing: {ACHIEVEMENT_OVERLAY}")
	overlay_hash = hashlib.sha256(ACHIEVEMENT_OVERLAY.read_bytes()).hexdigest().upper()
	expected = "89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD"
	if overlay_hash != expected:
		raise ValueError(f"Canonical overlay hash mismatch: {overlay_hash}")
	with Image.open(ACHIEVEMENT_OVERLAY) as opened:
		overlay = opened.convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS)
	outputs: list[Path] = []
	for src in files:
		name = src.name.replace("_source.png", "").removeprefix("achievement_")
		with Image.open(src) as opened:
			normal = cover_opaque(opened, (64, 64))
		grey_rgb = ImageOps.grayscale(normal.convert("RGB")).convert("RGB")
		grey = Image.merge("RGBA", (*grey_rgb.split(), normal.getchannel("A")))
		not_eligible = Image.alpha_composite(grey, overlay)
		for suffix, image in (("", normal), ("_grey", grey), ("_not_eligible", not_eligible)):
			out = PROCESSED / "achievements" / f"{name}{suffix}.png"
			out.parent.mkdir(parents=True, exist_ok=True)
			image.save(out, "PNG", optimize=True)
			write_dds(image, REPO / "gfx/achievements" / f"{name}{suffix}.dds")
			outputs.append(out)
	return outputs


def process_panel() -> list[Path]:
	src = SOURCE / "interface/resource_field_panel_source.png"
	if not src.exists():
		return []
	with Image.open(src) as opened:
		final = cover_opaque(opened, (470, 304))
	out = PROCESSED / "interface/resource_field_panel.png"
	out.parent.mkdir(parents=True, exist_ok=True)
	final.save(out, "PNG", optimize=True)
	write_dds(final, REPO / "gfx/interface/018_resources_found/resource_field_panel.dds")
	return [out]


FIELD_COUNTS = {"seal": 10, "unsafe": 10, "disturbance": 12, "breach": 12, "sealing": 12}
FIELD_FPS = {"seal": 8, "unsafe": 8, "disturbance": 9, "breach": 10, "sealing": 8}


def process_field_animation(state: str) -> list[Path]:
	count = FIELD_COUNTS[state]
	src_dir = SOURCE / f"animations/{state}"
	files = sorted(src_dir.glob("frame_*_source.png"))
	if len(files) != count:
		raise ValueError(f"{state}: expected {count} source frames, found {len(files)}")
	key_dir = KEYED / f"animations/{state}"
	jobs = [(str(src), str(key_dir / src.name.replace("_source.png", "_alpha.png"))) for src in files]
	with ProcessPoolExecutor(max_workers=min(4, count)) as pool:
		list(pool.map(chroma_one, jobs))
	frames: list[Image.Image] = []
	outputs: list[Path] = []
	for src, (_, keyed_raw) in zip(files, jobs):
		with Image.open(keyed_raw) as opened:
			frame = fit_transparent(opened, (128, 128), 4, 0.7, 0.65)
		name = src.name.replace("_source.png", "")
		out = PROCESSED / f"animations/{state}/{name}.png"
		out.parent.mkdir(parents=True, exist_ok=True)
		frame.save(out, "PNG", optimize=True)
		frames.append(frame)
		outputs.append(out)
	sheet = Image.new("RGBA", (128 * count, 128), (0, 0, 0, 0))
	for index, frame in enumerate(frames):
		sheet.alpha_composite(frame, (index * 128, 0))
	sheet_png = PROCESSED / f"animations/{state}/resource_field_{state}_sheet.png"
	sheet.save(sheet_png, "PNG", optimize=True)
	write_dds(sheet, REPO / f"gfx/interface/animated/018_resources_found/resource_field_{state}_sheet.dds")
	static = frames[0]
	static_png = PROCESSED / f"animations/{state}/resource_field_{state}_static.png"
	static.save(static_png, "PNG", optimize=True)
	write_dds(static, REPO / f"gfx/interface/animated/018_resources_found/resource_field_{state}_static.dds")
	preview = PREVIEWS / f"resource_field_{state}_preview.gif"
	preview.parent.mkdir(parents=True, exist_ok=True)
	frames[0].save(preview, save_all=True, append_images=frames[1:], duration=round(1000 / FIELD_FPS[state]), loop=0, disposal=2)
	outputs.extend([sheet_png, static_png, preview])
	return outputs


def process_field_static_states() -> list[Path]:
	files = sorted((SOURCE / "interface").glob("resource_field_*_source.png"))
	files = [p for p in files if p.stem in {"resource_field_suspended_source", "resource_field_closed_source"}]
	if not files:
		return []
	jobs = [(str(src), str(KEYED / "interface" / src.name.replace("_source.png", "_alpha.png"))) for src in files]
	with ProcessPoolExecutor(max_workers=len(jobs)) as pool:
		list(pool.map(chroma_one, jobs))
	outputs: list[Path] = []
	for src, (_, keyed_raw) in zip(files, jobs):
		name = src.name.replace("_source.png", "")
		with Image.open(keyed_raw) as opened:
			final = fit_transparent(opened, (128, 128), 4, 0.7, 0.65)
		out = PROCESSED / "interface" / f"{name}.png"
		out.parent.mkdir(parents=True, exist_ok=True)
		final.save(out, "PNG", optimize=True)
		write_dds(final, REPO / "gfx/interface/018_resources_found" / f"{name}.dds")
		outputs.append(out)
	return outputs


def make_contact(name: str, files: Iterable[Path], cell: tuple[int, int] = (150, 145), columns: int = 5) -> Path | None:
	paths = [p for p in files if p.suffix.lower() == ".png" and p.exists()]
	if not paths:
		return None
	cw, ch = cell
	rows = math.ceil(len(paths) / columns)
	canvas = Image.new("RGB", (columns * cw, rows * ch), (28, 30, 30))
	draw = ImageDraw.Draw(canvas)
	font = ImageFont.load_default()
	for i, path in enumerate(paths):
		x = (i % columns) * cw
		y = (i // columns) * ch
		with Image.open(path) as opened:
			preview = opened.convert("RGBA")
			preview.thumbnail((cw - 12, ch - 34), Image.Resampling.LANCZOS)
		checker = Image.new("RGBA", (cw - 8, ch - 30), (52, 54, 54, 255))
		checker.alpha_composite(preview, ((checker.width - preview.width) // 2, (checker.height - preview.height) // 2))
		canvas.paste(checker.convert("RGB"), (x + 4, y + 4))
		label = path.stem[:26]
		draw.text((x + 5, y + ch - 22), label, fill=(230, 223, 198), font=font)
	out = CONTACTS / f"{name}_contact_sheet.png"
	out.parent.mkdir(parents=True, exist_ok=True)
	canvas.save(out, "PNG", optimize=True)
	return out


def dds_info(path: Path) -> tuple[int, int, tuple[int, int, int, int]]:
	raw = path.read_bytes()
	if raw[:4] != b"DDS ":
		raise ValueError(f"Not a DDS: {path}")
	height, width = struct.unpack_from("<II", raw, 12)
	masks = struct.unpack_from("<IIII", raw, 92)
	return width, height, masks


def validate_dds_files() -> list[str]:
	errors: list[str] = []
	expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
	owned_roots = [
		REPO / "gfx/interface/goals/018_resources_found",
		REPO / "gfx/interface/ideas/018_resources_found",
		REPO / "gfx/interface/decisions/018_resources_found",
		REPO / "gfx/interface/animated/018_resources_found",
		REPO / "gfx/interface/018_resources_found",
	]
	files = [p for root in owned_roots if root.exists() for p in root.glob("*.dds")]
	files.extend((REPO / "gfx/achievements").glob("018_resources_found_*.dds"))
	for path in files:
		try:
			_, _, masks = dds_info(path)
			if masks != expected_masks:
				errors.append(f"{path}: masks {masks!r}")
		except Exception as exc:
			errors.append(f"{path}: {exc}")
	return errors


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument("--family", choices=["focus", "ideas", "decisions", "category_pictures", "achievements", "panel", "field", "all", "validate"], default="all")
	args = parser.parse_args()
	produced: dict[str, list[Path]] = {}
	if args.family in {"focus", "all"}:
		produced["focus"] = process_transparent_family("focus", (94, 86), REPO / "gfx/interface/goals/018_resources_found", 2, 0.85, 0.75)
	if args.family in {"ideas", "all"}:
		produced["ideas"] = process_transparent_family("ideas", (64, 64), REPO / "gfx/interface/ideas/018_resources_found", 3, 1.0, 0.8)
	if args.family in {"decisions", "all"}:
		produced["decisions"] = process_transparent_family("decisions", (32, 32), REPO / "gfx/interface/decisions/018_resources_found", 1, 0.85, 0.7)
	if args.family in {"category_pictures", "all"}:
		produced["category_pictures"] = process_category_pictures()
	if args.family in {"achievements", "all"}:
		produced["achievements"] = process_achievements()
	if args.family in {"panel", "all"}:
		produced["panel"] = process_panel()
	if args.family in {"field", "all"}:
		for state in FIELD_COUNTS:
			produced[f"field_{state}"] = process_field_animation(state)
		produced["field_static"] = process_field_static_states()
	for family, files in produced.items():
		pngs = [p for p in files if p.suffix.lower() == ".png" and "sheet" not in p.stem]
		make_contact(family, pngs, columns=5)
		print(f"{family}: {len(files)} outputs")
	errors = validate_dds_files()
	if errors:
		print("DDS validation failures:", file=sys.stderr)
		for error in errors:
			print(f"- {error}", file=sys.stderr)
		return 1
	print("DDS validation: all owned files use canonical BGRA masks")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
