#!/usr/bin/env python3
"""Process and validate Event 014 unified-decision icon rows 01-09 only."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import textwrap
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]
BRIEFS = PACKAGE / "prompts" / "icon_briefs_rows_01_09.tsv"
COMMON_PROMPT = PACKAGE / "prompts" / "common_prompt.md"
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACTS = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation"
LIVE = ROOT / "gfx" / "interface" / "decisions" / "014_cannibalism"
DECISIONS = ROOT / "common" / "decisions" / "014_cannibalism_unified_decisions.txt"
GFX = ROOT / "interface" / "014_cannibalism.gfx"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
CHROMA_HELPER = Path("C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
SIZE = (32, 32)
EXPECTED_COUNT = 9
EXPECTED_MASKS = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def load_rows() -> list[dict[str, str]]:
	with BRIEFS.open("r", encoding="utf-8", newline="") as handle:
		rows = list(csv.DictReader(handle, delimiter="\t"))
	ids = [row["decision_id"] for row in rows]
	if len(ids) != EXPECTED_COUNT or len(set(ids)) != EXPECTED_COUNT:
		raise RuntimeError(f"Expected {EXPECTED_COUNT} unique subset ids, found {len(ids)} / {len(set(ids))}")
	decision_text = DECISIONS.read_text(encoding="utf-8-sig")
	live_ids = re.findall(r"(?m)^\s*icon\s*=\s*GFX_decision_(cannibalism_unified_[a-z0-9_]+)\s*$", decision_text)
	if live_ids[:EXPECTED_COUNT] != ids:
		raise RuntimeError(f"Subset order no longer matches the first {EXPECTED_COUNT} live decisions")
	return rows


def registered_paths() -> dict[str, str]:
	text = GFX.read_text(encoding="utf-8-sig")
	return dict(re.findall(
		r'name\s*=\s*"GFX_decision_(cannibalism_unified_[a-z0-9_]+)"\s+texturefile\s*=\s*"([^"]+)"',
		text,
	))


def source_path(decision_id: str) -> Path:
	return SOURCE / f"decision_{decision_id}_source.png"


def alpha_path(decision_id: str) -> Path:
	return ALPHA / f"decision_{decision_id}_alpha.png"


def processed_path(decision_id: str) -> Path:
	return PROCESSED / f"decision_{decision_id}.png"


def package_dds_path(decision_id: str) -> Path:
	return DDS_PACKAGE / f"decision_{decision_id}.dds"


def live_dds_path(decision_id: str) -> Path:
	return LIVE / f"decision_{decision_id}.dds"


def run_chroma(decision_id: str) -> None:
	result = subprocess.run(
		[
			sys.executable,
			str(CHROMA_HELPER),
			"--input",
			str(source_path(decision_id)),
			"--out",
			str(alpha_path(decision_id)),
			"--auto-key",
			"border",
			"--soft-matte",
			"--transparent-threshold",
			"12",
			"--opaque-threshold",
			"220",
			"--despill",
			"--force",
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"Chroma cleanup failed for {decision_id}:\n{result.stdout}\n{result.stderr}")


def trim_alpha(image: Image.Image) -> Image.Image:
	rgba = image.convert("RGBA")
	bbox = rgba.getchannel("A").point(lambda value: 255 if value > 6 else 0).getbbox()
	if bbox is None:
		raise RuntimeError("No visible pixels after chroma-key cleanup")
	return rgba.crop(bbox)


def fit_icon(path: Path) -> Image.Image:
	scale = 8
	high_size = (SIZE[0] * scale, SIZE[1] * scale)
	maximum = ((SIZE[0] - 5) * scale, (SIZE[1] - 5) * scale)
	image = trim_alpha(Image.open(path))
	ratio = min(maximum[0] / image.width, maximum[1] / image.height)
	resized = image.resize(
		(max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
		Image.Resampling.LANCZOS,
	)
	x = (high_size[0] - resized.width) // 2
	y = (high_size[1] - resized.height) // 2 - 2
	alpha = Image.new("L", high_size, 0)
	alpha.paste(resized.getchannel("A"), (x, y))

	shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=5)).point(lambda value: round(value * 0.52))
	shifted_shadow = Image.new("L", high_size, 0)
	shifted_shadow.paste(shadow_alpha, (5, 6))
	shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
	shadow.putalpha(shifted_shadow)

	outline_alpha = alpha.filter(ImageFilter.MaxFilter(15)).point(lambda value: round(value * 0.88))
	outline = Image.new("RGBA", high_size, (18, 13, 11, 255))
	outline.putalpha(outline_alpha)

	subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
	subject.alpha_composite(resized, (x, y))
	composite = Image.alpha_composite(Image.alpha_composite(shadow, outline), subject)
	final = composite.resize(SIZE, Image.Resampling.LANCZOS)

	alpha_final = final.getchannel("A")
	rgb = final.convert("RGB").filter(ImageFilter.UnsharpMask(radius=0.55, percent=80, threshold=3))
	sharpened = rgb.convert("RGBA")
	sharpened.putalpha(alpha_final)
	return sharpened


def convert_to_dds(decision_id: str) -> None:
	result = subprocess.run(
		[
			sys.executable,
			str(CONVERTER),
			"--input",
			str(processed_path(decision_id)),
			"--output",
			str(package_dds_path(decision_id)),
			"--width",
			str(SIZE[0]),
			"--height",
			str(SIZE[1]),
		],
		text=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
	)
	if result.returncode:
		raise RuntimeError(f"DDS conversion failed for {decision_id}:\n{result.stdout}\n{result.stderr}")
	shutil.copy2(package_dds_path(decision_id), live_dds_path(decision_id))


def font(size: int) -> ImageFont.ImageFont:
	for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
		if path.exists():
			return ImageFont.truetype(str(path), size=size)
	return ImageFont.load_default()


def checker(size: tuple[int, int], tile: int = 12) -> Image.Image:
	image = Image.new("RGBA", size, (74, 74, 74, 255))
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], tile):
		for x in range(0, size[0], tile):
			if (x // tile + y // tile) % 2:
				draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(126, 126, 126, 255))
	return image


def wrap_label(draw: ImageDraw.ImageDraw, text: str, x0: int, y0: int, width: int) -> None:
	label_font = font(13)
	lines = textwrap.wrap(text.removeprefix("cannibalism_unified_"), width=31)[:3]
	y = y0
	for line in lines:
		bbox = draw.textbbox((0, 0), line, font=label_font)
		draw.text((x0 + (width - (bbox[2] - bbox[0])) // 2, y), line, font=label_font, fill=(238, 238, 238))
		y += 16


def make_source_contact(rows: list[dict[str, str]]) -> None:
	columns, cell_w, cell_h = 3, 390, 390
	rows_count = math.ceil(len(rows) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows_count * cell_h), (25, 27, 30))
	draw = ImageDraw.Draw(sheet)
	for index, row in enumerate(rows):
		x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
		draw.rectangle((x0 + 4, y0 + 4, x0 + cell_w - 5, y0 + cell_h - 5), outline=(91, 95, 101))
		with Image.open(source_path(row["decision_id"])) as opened:
			preview = ImageOps.contain(opened.convert("RGB"), (330, 330), Image.Resampling.LANCZOS)
		sheet.paste(preview, (x0 + (cell_w - preview.width) // 2, y0 + 12))
		wrap_label(draw, row["decision_id"], x0, y0 + 348, cell_w)
	CONTACTS.mkdir(parents=True, exist_ok=True)
	sheet.save(CONTACTS / "unified_decisions_rows_01_09_sources_contact.png", optimize=True)


def make_final_contact(rows: list[dict[str, str]], folder: Path, suffix: str, output_name: str) -> None:
	columns, cell_w, cell_h = 3, 390, 265
	rows_count = math.ceil(len(rows) / columns)
	sheet = Image.new("RGB", (columns * cell_w, rows_count * cell_h), (25, 27, 30))
	draw = ImageDraw.Draw(sheet)
	native_font = font(12)
	for index, row in enumerate(rows):
		x0, y0 = (index % columns) * cell_w, (index // columns) * cell_h
		draw.rectangle((x0 + 4, y0 + 4, x0 + cell_w - 5, y0 + cell_h - 5), outline=(91, 95, 101))
		with Image.open(folder / f"decision_{row['decision_id']}{suffix}") as opened:
			icon = opened.convert("RGBA")
		native_plate = checker((96, 96), 8)
		native_plate.alpha_composite(icon, (32, 32))
		large_plate = checker((160, 160), 16)
		large_plate.alpha_composite(icon.resize((128, 128), Image.Resampling.NEAREST), (16, 16))
		sheet.paste(native_plate.convert("RGB"), (x0 + 42, y0 + 18))
		sheet.paste(large_plate.convert("RGB"), (x0 + 185, y0 + 18))
		draw.text((x0 + 70, y0 + 118), "native", font=native_font, fill=(205, 205, 205))
		draw.text((x0 + 247, y0 + 181), "4x", font=native_font, fill=(205, 205, 205))
		wrap_label(draw, row["decision_id"], x0, y0 + 208, cell_w)
	sheet.save(CONTACTS / output_name, optimize=True)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
	data = path.read_bytes()[:128]
	if len(data) != 128 or data[:4] != b"DDS ":
		raise RuntimeError(f"Invalid DDS header: {path}")
	height = struct.unpack_from("<I", data, 12)[0]
	width = struct.unpack_from("<I", data, 16)[0]
	mip_count = struct.unpack_from("<I", data, 28)[0]
	masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
	return width, height, mip_count, masks


def visible_key_green(image: Image.Image) -> int:
	data = image.convert("RGBA").tobytes()
	return sum(
		1
		for index in range(0, len(data), 4)
		if data[index + 3] > 10
		and data[index + 1] > 205
		and data[index + 1] > data[index] * 1.65
		and data[index + 1] > data[index + 2] * 1.65
	)


def final_prompt(common: str, subject: str) -> str:
	return common.split("\n\nEvery row", 1)[0].replace("{{SUBJECT_BRIEF}}", subject).strip()


def write_ledgers(rows: list[dict[str, str]], validations: list[dict[str, object]]) -> None:
	common = COMMON_PROMPT.read_text(encoding="utf-8")
	validation_by_id = {entry["decision_id"]: entry for entry in validations}
	prompt_entries: list[dict[str, object]] = []
	for index, row in enumerate(rows, start=1):
		entry = validation_by_id[row["decision_id"]]
		prompt_entries.append({
			"row": index,
			"decision_id": row["decision_id"],
			"title": row["title"],
			"category": row["category"],
			"source_mode": "built-in image_gen, one call for this asset",
			"subject_brief": row["subject_brief"],
			"final_prompt": final_prompt(common, row["subject_brief"]),
			"generation_note": row["generation_note"],
			"source_png": entry["source_png"],
			"source_sha256": entry["source_sha256"],
			"status": "selected_and_processed",
		})
	(PACKAGE / "prompts" / "icon_prompt_ledger_rows_01_09.json").write_text(
		json.dumps(prompt_entries, indent=2, ensure_ascii=False) + "\n",
		encoding="utf-8",
	)

	with (VALIDATION / "icon_validation_rows_01_09.tsv").open("w", encoding="utf-8", newline="") as handle:
		writer = csv.DictWriter(handle, fieldnames=list(validations[0].keys()), delimiter="\t", lineterminator="\n")
		writer.writeheader()
		writer.writerows(validations)

	manifest_lines = [
		"# Event 014 unified decision icons — rows 01-09",
		"",
		"Nine individually generated decision-icon sources for the live unified command and opening Larder decisions. Each source was generated with a separate built-in image-generation call, keyed to transparency, composed specifically for 32x32 readability, and converted to one-level uncompressed BGRA DDS.",
		"",
		"- Asset type: decision icon",
		"- Source mode: built-in `image_gen`",
		"- Target size: 32x32",
		"- Registered GFX file: `interface/014_cannibalism.gfx`",
		"- Prompt ledger: `prompts/icon_prompt_ledger_rows_01_09.json`",
		"- Validation ledger: `validation/icon_validation_rows_01_09.tsv`",
		"- Contact sheets: `contact_sheets/unified_decisions_rows_01_09_{sources,processed_checker,dds_decoded_checker}_contact.png`",
		"",
		"| Row | Decision | Title | Source PNG | Processed PNG | Final DDS | Sprite | Status |",
		"|---:|---|---|---|---|---|---|---|",
	]
	for index, row in enumerate(rows, start=1):
		decision_id = row["decision_id"]
		manifest_lines.append(
			f"| {index} | `{decision_id}` | {row['title']} | `source_png/decision_{decision_id}_source.png` | "
			f"`processed_png/decision_{decision_id}.png` | `gfx/interface/decisions/014_cannibalism/decision_{decision_id}.dds` | "
			f"`GFX_decision_{decision_id}` | complete |"
		)
	manifest_lines += [
		"",
		"## Constraints",
		"",
		"The selected sources contain no real-person likeness, readable text, logo, living Indigenous motif, sacred borrowing, contemporary object, or ancient/classical-general imagery. Regeneration notes are preserved in the prompt ledger. No icon is a resized or repurposed focus, idea, category, or prior decision asset.",
	]
	(PACKAGE / "manifest_rows_01_09.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

	handoff_lines = [
		"# GFX handoff — unified decision icons rows 01-09",
		"",
		"The sprites and texture paths below were already registered in `interface/014_cannibalism.gfx`; no `.gfx` edit is required.",
		"",
		"| Sprite | Final DDS | Size |",
		"|---|---|---:|",
	]
	for row in rows:
		decision_id = row["decision_id"]
		handoff_lines.append(
			f"| `GFX_decision_{decision_id}` | `gfx/interface/decisions/014_cannibalism/decision_{decision_id}.dds` | 32x32 |"
		)
	(PACKAGE / "gfx_handoff_rows_01_09.md").write_text("\n".join(handoff_lines) + "\n", encoding="utf-8")


def main() -> None:
	rows = load_rows()
	ids = [row["decision_id"] for row in rows]
	registry = registered_paths()
	for directory in (ALPHA, PROCESSED, DDS_PACKAGE, CONTACTS, VALIDATION, LIVE):
		directory.mkdir(parents=True, exist_ok=True)
	missing_sources = [str(source_path(decision_id)) for decision_id in ids if not source_path(decision_id).exists()]
	if missing_sources:
		raise FileNotFoundError("Missing generated subset sources:\n" + "\n".join(missing_sources))

	with ThreadPoolExecutor(max_workers=4) as pool:
		list(pool.map(run_chroma, ids))
	for decision_id in ids:
		fit_icon(alpha_path(decision_id)).save(processed_path(decision_id), optimize=True)
	with ThreadPoolExecutor(max_workers=4) as pool:
		list(pool.map(convert_to_dds, ids))

	make_source_contact(rows)
	make_final_contact(rows, PROCESSED, ".png", "unified_decisions_rows_01_09_processed_checker_contact.png")
	make_final_contact(rows, LIVE, ".dds", "unified_decisions_rows_01_09_dds_decoded_checker_contact.png")

	source_hashes: dict[str, str] = {}
	processed_hashes: dict[str, str] = {}
	dds_hashes: dict[str, str] = {}
	validations: list[dict[str, object]] = []
	for index, row in enumerate(rows, start=1):
		decision_id = row["decision_id"]
		source = source_path(decision_id)
		processed = processed_path(decision_id)
		package_dds = package_dds_path(decision_id)
		live_dds = live_dds_path(decision_id)
		expected_runtime = f"gfx/interface/decisions/014_cannibalism/decision_{decision_id}.dds"
		if registry.get(decision_id) != expected_runtime:
			raise RuntimeError(f"Registered path mismatch for {decision_id}: {registry.get(decision_id)!r}")

		with Image.open(source) as opened:
			source_size = opened.size
		with Image.open(processed) as opened:
			processed_image = opened.convert("RGBA")
		with Image.open(live_dds) as opened:
			decoded = opened.convert("RGBA")
		alpha = processed_image.getchannel("A")
		corners = tuple(alpha.getpixel(point) for point in ((0, 0), (31, 0), (0, 31), (31, 31)))
		alpha_min, alpha_max = alpha.getextrema()
		key_green = visible_key_green(processed_image)
		if processed_image.size != SIZE or decoded.size != SIZE:
			raise RuntimeError(f"Dimension failure for {decision_id}: {processed_image.size} / {decoded.size}")
		if alpha_min != 0 or alpha_max != 255 or corners != (0, 0, 0, 0):
			raise RuntimeError(f"Transparency failure for {decision_id}: range={(alpha_min, alpha_max)} corners={corners}")
		if key_green:
			raise RuntimeError(f"Visible chroma-key pixels remain in {decision_id}: {key_green}")
		if processed_image.tobytes() != decoded.tobytes():
			raise RuntimeError(f"Decoded DDS pixel mismatch for {decision_id}")
		width, height, mip_count, masks = dds_header(live_dds)
		if (width, height) != SIZE or mip_count not in (0, 1) or masks != EXPECTED_MASKS:
			raise RuntimeError(f"DDS format failure for {decision_id}: {(width, height, mip_count, masks)}")
		if live_dds.stat().st_size != 4224:
			raise RuntimeError(f"DDS byte-size failure for {decision_id}: {live_dds.stat().st_size}")
		if sha256(package_dds) != sha256(live_dds):
			raise RuntimeError(f"Package/runtime DDS mismatch for {decision_id}")

		source_digest = sha256(source)
		processed_digest = sha256(processed)
		dds_digest = sha256(live_dds)
		for digest, mapping, label in (
			(source_digest, source_hashes, "source"),
			(processed_digest, processed_hashes, "processed"),
			(dds_digest, dds_hashes, "DDS"),
		):
			if digest in mapping:
				raise RuntimeError(f"Duplicate {label} hash: {decision_id} duplicates {mapping[digest]}")
			mapping[digest] = decision_id

		alpha_bytes = alpha.tobytes()
		transparent = alpha_bytes.count(0)
		partial = len(alpha_bytes) - transparent - alpha_bytes.count(255)
		validations.append({
			"row": index,
			"decision_id": decision_id,
			"title": row["title"],
			"source_png": source.relative_to(ROOT).as_posix(),
			"source_sha256": source_digest,
			"source_dimensions": f"{source_size[0]}x{source_size[1]}",
			"processed_png": processed.relative_to(ROOT).as_posix(),
			"processed_sha256": processed_digest,
			"processed_dimensions": "32x32",
			"package_dds": package_dds.relative_to(ROOT).as_posix(),
			"runtime_dds": live_dds.relative_to(ROOT).as_posix(),
			"runtime_dds_sha256": dds_digest,
			"runtime_dds_bytes": live_dds.stat().st_size,
			"dds_format": "uncompressed BGRA 8.8.8.8, one image level",
			"transparent_pixels": transparent,
			"partial_alpha_pixels": partial,
			"corner_alpha": ",".join(str(value) for value in corners),
			"decoded_pixel_parity": "yes",
			"registered_path": registry[decision_id],
			"status": "complete",
		})

	write_ledgers(rows, validations)
	report = {
		"scope": "Event 014 unified decision icons rows 01-09",
		"expected": EXPECTED_COUNT,
		"subset_source_count": len(ids),
		"subset_processed_count": sum(processed_path(decision_id).exists() for decision_id in ids),
		"subset_package_dds_count": sum(package_dds_path(decision_id).exists() for decision_id in ids),
		"subset_runtime_dds_count": sum(live_dds_path(decision_id).exists() for decision_id in ids),
		"unique_source_hashes": len(source_hashes),
		"unique_processed_hashes": len(processed_hashes),
		"unique_runtime_dds_hashes": len(dds_hashes),
		"transparent_corners": all(entry["corner_alpha"] == "0,0,0,0" for entry in validations),
		"decoded_dds_pixel_parity": all(entry["decoded_pixel_parity"] == "yes" for entry in validations),
		"missing_registered_subset_paths": [
			registry.get(decision_id, "<unregistered>")
			for decision_id in ids
			if not live_dds_path(decision_id).exists()
		],
		"contact_sheets": [
			"contact_sheets/unified_decisions_rows_01_09_sources_contact.png",
			"contact_sheets/unified_decisions_rows_01_09_processed_checker_contact.png",
			"contact_sheets/unified_decisions_rows_01_09_dds_decoded_checker_contact.png",
		],
		"status": "complete",
	}
	(VALIDATION / "validation_report_rows_01_09.json").write_text(
		json.dumps(report, indent=2) + "\n",
		encoding="utf-8",
	)
	print(json.dumps(report, indent=2))


if __name__ == "__main__":
	main()
