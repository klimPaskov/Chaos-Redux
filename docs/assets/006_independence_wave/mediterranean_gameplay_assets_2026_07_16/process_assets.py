#!/usr/bin/env python3
"""Build and validate Event 006 Mediterranean gameplay art.

Owned runtime surface:
- eight package focus icons (plus registrations for their shine sprites)
- eight package decision icons
- eight shared Mediterranean lifecycle idea icons
- one shared Mediterranean island-incidents report card

The FORM05 maritime-congress focus/decision pair is a shared bridge owned here.
Dedicated FORM05 charter, shipping, defence, customs, proclamation, emblem, flag,
and report assets are deliberately outside this package.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
NOTES_ROOT = PACKAGE_ROOT / "notes"
CHROMA_HELPER = (
	Path.home()
	/ ".codex"
	/ "skills"
	/ ".system"
	/ "imagegen"
	/ "scripts"
	/ "remove_chroma_key.py"
)
DDS_CONVERTER = (
	REPO_ROOT
	/ ".agents"
	/ "skills"
	/ "chaos-redux-event-assets"
	/ "tools"
	/ "convert_to_dds.py"
)
REPORT_PROCESSOR = (
	REPO_ROOT
	/ ".agents"
	/ "skills"
	/ "chaos-redux-event-assets"
	/ "tools"
	/ "process_report_event_image.py"
)
INTERFACE_FILE = REPO_ROOT / "interface" / "006_independence_wave_mediterranean_assets.gfx"


@dataclass(frozen=True)
class Family:
	name: str
	width: int
	height: int
	max_width: int
	max_height: int
	runtime_dir: Path
	source_count: int
	columns: int
	scale: int


FAMILIES = {
	"focus": Family(
		"focus",
		94,
		86,
		90,
		82,
		REPO_ROOT / "gfx" / "interface" / "goals" / "006_independence_wave" / "mediterranean",
		8,
		4,
		2,
	),
	"decision": Family(
		"decision",
		32,
		32,
		30,
		30,
		REPO_ROOT / "gfx" / "interface" / "decisions" / "006_independence_wave" / "mediterranean",
		8,
		8,
		4,
	),
	"idea": Family(
		"idea",
		64,
		64,
		60,
		60,
		REPO_ROOT / "gfx" / "interface" / "ideas" / "006_independence_wave" / "mediterranean",
		8,
		4,
		2,
	),
}
REPORT_SIZE = (210, 176)
REPORT_RUNTIME_DIR = REPO_ROOT / "gfx" / "event_pictures" / "006_independence_wave" / "mediterranean"

FOCUS_TOKENS = (
	"independence_wave_cor_customs",
	"independence_wave_cor_mountain_communes",
	"independence_wave_arx_shipping",
	"independence_wave_arx_mountain_guards",
	"independence_wave_asx_port",
	"independence_wave_asx_grain_straits",
	"independence_wave_asx_two_sicilies",
	"independence_wave_form05_maritime_congress",
)
DECISION_TOKENS = FOCUS_TOKENS
IDEA_TOKENS = (
	"independence_wave_mediterranean_island_crisis",
	"independence_wave_mediterranean_state_compact",
	"independence_wave_mediterranean_constitutional_assembly",
	"independence_wave_mediterranean_mountain_communes",
	"independence_wave_mediterranean_labor_compact",
	"independence_wave_mediterranean_crown_council",
	"independence_wave_mediterranean_island_guard",
	"independence_wave_mediterranean_patron_customs",
)
REPORT_TOKEN = "report_event_006_mediterranean_island_incidents"


def run(command: list[str]) -> None:
	completed = subprocess.run(command, check=False, text=True, capture_output=True)
	if completed.returncode != 0:
		raise RuntimeError(
			f"Command failed ({completed.returncode}): {' '.join(command)}\n"
			f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
		)


def sha256(path: Path) -> str:
	digest = hashlib.sha256()
	with path.open("rb") as source:
		for chunk in iter(lambda: source.read(1024 * 1024), b""):
			digest.update(chunk)
	return digest.hexdigest()


def relative(path: Path) -> str:
	return path.relative_to(REPO_ROOT).as_posix()


def remove_chroma(source: Path, destination: Path) -> None:
	run(
		[
			sys.executable,
			str(CHROMA_HELPER),
			"--input",
			str(source),
			"--out",
			str(destination),
			"--auto-key",
			"border",
			"--soft-matte",
			"--transparent-threshold",
			"12",
			"--opaque-threshold",
			"220",
			"--edge-contract",
			"1",
			"--despill",
			"--force",
		]
	)


def alpha_bbox(image: Image.Image) -> tuple[int, int, int, int]:
	bbox = image.getchannel("A").getbbox()
	if bbox is None:
		raise ValueError("Chroma removal produced a fully transparent image")
	return bbox


def fit_icon(keyed: Image.Image, family: Family) -> Image.Image:
	cropped = keyed.convert("RGBA").crop(alpha_bbox(keyed))
	scale = min(family.max_width / cropped.width, family.max_height / cropped.height)
	resized_size = (
		max(1, round(cropped.width * scale)),
		max(1, round(cropped.height * scale)),
	)
	subject = cropped.resize(resized_size, Image.Resampling.LANCZOS)
	canvas = Image.new("RGBA", (family.width, family.height), (0, 0, 0, 0))
	x = (family.width - subject.width) // 2
	y = (family.height - subject.height) // 2

	alpha = subject.getchannel("A")
	outline = alpha.filter(ImageFilter.MaxFilter(3))
	outline_only = ImageChops.subtract(outline, alpha)
	outline_layer = Image.new("RGBA", subject.size, (14, 12, 10, 0))
	outline_layer.putalpha(outline_only.point(lambda value: min(220, value)))
	canvas.alpha_composite(outline_layer, (x, y))

	shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
	shadow.putalpha(
		alpha.filter(ImageFilter.GaussianBlur(0.55)).point(lambda value: round(value * 0.45))
	)
	canvas.alpha_composite(shadow, (x + 1, y + 1))
	canvas.alpha_composite(subject, (x, y))
	return canvas


def convert_to_dds(png: Path, dds: Path, width: int, height: int) -> None:
	dds.parent.mkdir(parents=True, exist_ok=True)
	run(
		[
			sys.executable,
			str(DDS_CONVERTER),
			"--input",
			str(png),
			"--output",
			str(dds),
			"--width",
			str(width),
			"--height",
			str(height),
		]
	)


def validate_png(path: Path, width: int, height: int) -> dict[str, object]:
	with Image.open(path) as source:
		image = source.convert("RGBA")
	if image.size != (width, height):
		raise ValueError(f"Unexpected PNG dimensions for {path}: {image.size}")
	alpha = image.getchannel("A")
	alpha_values = list(alpha.getdata())
	corners = [alpha.getpixel((0, 0)), alpha.getpixel((width - 1, 0)), alpha.getpixel((0, height - 1)), alpha.getpixel((width - 1, height - 1))]
	if min(alpha_values) != 0 or max(alpha_values) != 255 or any(corners):
		raise ValueError(f"Invalid alpha clearance for {path}: min/max={min(alpha_values)}/{max(alpha_values)}, corners={corners}")
	magenta_pixels = sum(
		1
		for red, green, blue, a in image.getdata()
		if a > 16 and red > 230 and green < 45 and blue > 210
	)
	if magenta_pixels:
		raise ValueError(f"Visible chroma spill remains in {path}: {magenta_pixels} pixels")
	return {
		"path": relative(path),
		"width": width,
		"height": height,
		"alpha_min": min(alpha_values),
		"alpha_max": max(alpha_values),
		"transparent_corners": corners,
		"visible_magenta_pixels": magenta_pixels,
		"sha256": sha256(path),
	}


def decode_and_validate_dds(path: Path, expected_png: Path, width: int, height: int) -> tuple[dict[str, object], Image.Image]:
	payload = path.read_bytes()
	if payload[:4] != b"DDS ":
		raise ValueError(f"Missing DDS magic: {path}")
	fields = {
		"header_size": int.from_bytes(payload[4:8], "little"),
		"flags": int.from_bytes(payload[8:12], "little"),
		"height": int.from_bytes(payload[12:16], "little"),
		"width": int.from_bytes(payload[16:20], "little"),
		"pitch": int.from_bytes(payload[20:24], "little"),
		"pixel_format_size": int.from_bytes(payload[76:80], "little"),
		"pixel_format_flags": int.from_bytes(payload[80:84], "little"),
		"bit_count": int.from_bytes(payload[88:92], "little"),
		"red_mask": int.from_bytes(payload[92:96], "little"),
		"green_mask": int.from_bytes(payload[96:100], "little"),
		"blue_mask": int.from_bytes(payload[100:104], "little"),
		"alpha_mask": int.from_bytes(payload[104:108], "little"),
		"caps": int.from_bytes(payload[108:112], "little"),
	}
	expected_fields = {
		"header_size": 124,
		"height": height,
		"width": width,
		"pitch": width * 4,
		"pixel_format_size": 32,
		"bit_count": 32,
		"red_mask": 0x00FF0000,
		"green_mask": 0x0000FF00,
		"blue_mask": 0x000000FF,
		"alpha_mask": 0xFF000000,
		"caps": 0x1000,
	}
	for key, expected in expected_fields.items():
		if fields[key] != expected:
			raise ValueError(f"Unexpected DDS {key} for {path}: {fields[key]} != {expected}")
	expected_length = 128 + width * height * 4
	if len(payload) != expected_length:
		raise ValueError(f"Unexpected DDS payload length for {path}: {len(payload)} != {expected_length}")

	decoded = Image.frombytes("RGBA", (width, height), payload[128:], "raw", "BGRA")
	with Image.open(expected_png) as source:
		expected_image = source.convert("RGBA")
	difference = ImageChops.difference(decoded, expected_image)
	pixel_exact = difference.getbbox() is None
	if not pixel_exact:
		raise ValueError(f"DDS pixels do not exactly match processed PNG: {path}")
	alpha_values = list(decoded.getchannel("A").getdata())
	return (
		{
			"path": relative(path),
			**fields,
			"bytes": len(payload),
			"alpha_min": min(alpha_values),
			"alpha_max": max(alpha_values),
			"pixel_exact_to_processed_png": pixel_exact,
			"sha256": sha256(path),
		},
		decoded,
	)


def process_icons(temporary_root: Path) -> tuple[list[dict[str, object]], dict[str, list[Path]]]:
	records: list[dict[str, object]] = []
	processed_by_family: dict[str, list[Path]] = {}
	for family_name, family in FAMILIES.items():
		sources = sorted((SOURCE_ROOT / family_name).glob("*_source.png"))
		if len(sources) != family.source_count:
			raise ValueError(f"Expected {family.source_count} {family_name} sources, found {len(sources)}")
		processed_by_family[family_name] = []
		for source in sources:
			stem = source.stem.removesuffix("_source")
			keyed = temporary_root / f"{stem}_keyed.png"
			remove_chroma(source, keyed)
			with Image.open(keyed) as keyed_source:
				final = fit_icon(keyed_source, family)
			processed = PROCESSED_ROOT / family_name / f"{stem}.png"
			processed.parent.mkdir(parents=True, exist_ok=True)
			final.save(processed, "PNG", optimize=True)
			runtime = family.runtime_dir / f"{stem}.dds"
			convert_to_dds(processed, runtime, family.width, family.height)
			processed_by_family[family_name].append(processed)
			records.append(
				{
					"family": family_name,
					"source": relative(source),
					"source_sha256": sha256(source),
					"processed": validate_png(processed, family.width, family.height),
					"runtime_path": relative(runtime),
				}
			)
	return records, processed_by_family


def process_report() -> tuple[dict[str, object], Path]:
	sources = sorted((SOURCE_ROOT / "report").glob("*_source.png"))
	if len(sources) != 1:
		raise ValueError(f"Expected one report source, found {len(sources)}")
	source = sources[0]
	stem = source.stem.removesuffix("_source")
	processed = PROCESSED_ROOT / "report" / f"{stem}.png"
	processed.parent.mkdir(parents=True, exist_ok=True)
	run(
		[
			sys.executable,
			str(REPORT_PROCESSOR),
			str(source),
			str(processed),
			"--canvas-size",
			"210x176",
			"--card-size",
			"192x153",
			"--angle",
			"3.4",
			"--shadow-offset",
			"4",
			"5",
			"--shadow-blur",
			"4.5",
			"--shadow-opacity",
			"0.50",
			"--grain",
			"6",
			"--seed",
			"6005",
		]
	)
	runtime = REPORT_RUNTIME_DIR / f"{stem}.dds"
	convert_to_dds(processed, runtime, *REPORT_SIZE)
	return (
		{
			"family": "report",
			"source": relative(source),
			"source_sha256": sha256(source),
			"processed": validate_png(processed, *REPORT_SIZE),
			"runtime_path": relative(runtime),
		},
		processed,
	)


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
	candidates = [
		Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
		Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
	]
	for candidate in candidates:
		if candidate.exists():
			return ImageFont.truetype(str(candidate), size)
	return ImageFont.load_default()


def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
	image = Image.new("RGBA", size, (62, 66, 72, 255))
	draw = ImageDraw.Draw(image)
	for y in range(0, size[1], cell):
		for x in range(0, size[0], cell):
			if (x // cell + y // cell) % 2:
				draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(102, 107, 115, 255))
	return image


def compact_label(path: Path) -> str:
	label = path.stem
	for prefix in (
		"goal_independence_wave_",
		"decision_independence_wave_",
		"idea_independence_wave_mediterranean_",
		"report_event_006_mediterranean_",
	):
		label = label.removeprefix(prefix)
	return label.replace("_", " ")


def make_contact_sheet(
	processed_by_family: dict[str, list[Path]],
	report: Path,
	output: Path,
	decoded_images: dict[Path, Image.Image] | None = None,
) -> None:
	title_font = load_font(22, bold=True)
	section_font = load_font(17, bold=True)
	label_font = load_font(12)
	canvas_width = 1120
	sections: list[tuple[str, list[Path], int, int]] = [
		("Focus icons — 94×86", processed_by_family["focus"], 4, 2),
		("Decision icons — 32×32", processed_by_family["decision"], 8, 4),
		("Lifecycle ideas — 64×64", processed_by_family["idea"], 4, 2),
		("Incident report — 210×176", [report], 1, 2),
	]
	height = 54
	geometry: list[tuple[str, list[Path], int, int, int, int]] = []
	for name, files, columns, scale in sections:
		thumb_w = max(1, max(Image.open(path).width for path in files) * scale)
		thumb_h = max(1, max(Image.open(path).height for path in files) * scale)
		cell_width = canvas_width // columns
		cell_height = thumb_h + 48
		rows = math.ceil(len(files) / columns)
		geometry.append((name, files, columns, scale, cell_height, rows))
		height += 34 + cell_height * rows + 12

	canvas = Image.new("RGBA", (canvas_width, height), (27, 30, 35, 255))
	draw = ImageDraw.Draw(canvas)
	draw.text((18, 14), "Event 006 Mediterranean gameplay art — target-size review", font=title_font, fill=(239, 232, 210, 255))
	y = 54
	for name, files, columns, scale, cell_height, rows in geometry:
		draw.rectangle((0, y, canvas_width, y + 31), fill=(42, 47, 55, 255))
		draw.text((18, y + 6), name, font=section_font, fill=(226, 220, 198, 255))
		y += 34
		cell_width = canvas_width // columns
		for index, path in enumerate(files):
			row = index // columns
			column = index % columns
			left = column * cell_width
			top = y + row * cell_height
			if decoded_images is None:
				with Image.open(path) as source:
					icon = source.convert("RGBA")
			else:
				icon = decoded_images[path].copy()
			enlarged = icon.resize((icon.width * scale, icon.height * scale), Image.Resampling.NEAREST)
			board = checker(enlarged.size, max(4, scale * 2))
			board.alpha_composite(enlarged)
			x = left + (cell_width - board.width) // 2
			canvas.alpha_composite(board, (x, top))
			label_lines = textwrap.wrap(compact_label(path), width=max(12, 28 if columns <= 4 else 16))[:2]
			for line_index, line in enumerate(label_lines):
				bbox = draw.textbbox((0, 0), line, font=label_font)
				line_width = bbox[2] - bbox[0]
				draw.text((left + (cell_width - line_width) // 2, top + board.height + 5 + line_index * 14), line, font=label_font, fill=(224, 226, 230, 255))
		y += rows * cell_height + 12
	output.parent.mkdir(parents=True, exist_ok=True)
	canvas.convert("RGB").save(output, "PNG", optimize=True)


def validate_consumers_and_interface() -> dict[str, object]:
	focus_file = REPO_ROOT / "common" / "national_focus" / "006_independence_wave_focus.txt"
	decision_file = REPO_ROOT / "common" / "decisions" / "006_independence_wave_mediterranean_decisions.txt"
	idea_file = REPO_ROOT / "common" / "ideas" / "006_independence_wave_mediterranean_ideas.txt"
	event_file = REPO_ROOT / "events" / "006_independence_wave_mediterranean.txt"
	texts = {
		"focus": focus_file.read_text(encoding="utf-8-sig"),
		"decision": decision_file.read_text(encoding="utf-8-sig"),
		"idea": idea_file.read_text(encoding="utf-8-sig"),
		"event": event_file.read_text(encoding="utf-8-sig"),
		"interface": INTERFACE_FILE.read_text(encoding="utf-8-sig"),
	}
	checks: dict[str, dict[str, int]] = {"focus": {}, "decision": {}, "idea": {}, "report": {}}
	for token in FOCUS_TOKENS:
		needle = f"icon = GFX_goal_{token}"
		count = texts["focus"].count(needle)
		if count < 1 or texts["interface"].count(f'name = "GFX_goal_{token}"') != 1 or texts["interface"].count(f'name = "GFX_goal_{token}_shine"') != 1:
			raise ValueError(f"Focus consumer/registration mismatch: {token}")
		checks["focus"][token] = count
	for token in DECISION_TOKENS:
		needle = f"icon = GFX_decision_{token}"
		count = texts["decision"].count(needle)
		if count < 1 or texts["interface"].count(f'name = "GFX_decision_{token}"') != 1:
			raise ValueError(f"Decision consumer/registration mismatch: {token}")
		checks["decision"][token] = count
	for token in IDEA_TOKENS:
		needle = f"picture = {token}"
		count = texts["idea"].count(needle)
		if count < 1 or texts["interface"].count(f'name = "GFX_idea_{token}"') != 1:
			raise ValueError(f"Idea consumer/registration mismatch: {token}")
		checks["idea"][token] = count
	report_needle = f"picture = GFX_{REPORT_TOKEN}"
	report_count = texts["event"].count(report_needle)
	if report_count < 1 or texts["interface"].count(f'name = "GFX_{REPORT_TOKEN}"') != 1:
		raise ValueError("Report consumer/registration mismatch")
	checks["report"][REPORT_TOKEN] = report_count
	for forbidden in ("form05_charter", "form05_shipping", "form05_defense", "form05_customs", "form05_proclamation"):
		if forbidden in texts["interface"].lower():
			raise ValueError(f"Out-of-scope registration found: {forbidden}")
	return {
		"consumer_occurrences": checks,
		"interface": relative(INTERFACE_FILE),
		"dedicated_form05_references": 0,
	}


def main() -> None:
	for required in (CHROMA_HELPER, DDS_CONVERTER, REPORT_PROCESSOR, INTERFACE_FILE):
		if not required.exists():
			raise FileNotFoundError(f"Missing required tool or registration: {required}")

	with tempfile.TemporaryDirectory(prefix="chaosx_006_mediterranean_") as temporary:
		icon_records, processed_by_family = process_icons(Path(temporary))
	report_record, processed_report = process_report()
	all_records = icon_records + [report_record]

	processed_hashes: dict[str, list[str]] = {}
	for family_name in (*FAMILIES, "report"):
		family_records = [record for record in all_records if record["family"] == family_name]
		processed_hashes[family_name] = [record["processed"]["sha256"] for record in family_records]
		if len(processed_hashes[family_name]) != len(set(processed_hashes[family_name])):
			raise ValueError(f"Byte-identical processed images found in {family_name}")

	dds_audit: list[dict[str, object]] = []
	decoded_images: dict[Path, Image.Image] = {}
	for record in all_records:
		processed = REPO_ROOT / record["processed"]["path"]
		runtime = REPO_ROOT / record["runtime_path"]
		if record["family"] == "report":
			width, height = REPORT_SIZE
		else:
			family = FAMILIES[str(record["family"])]
			width, height = family.width, family.height
		audit, decoded = decode_and_validate_dds(runtime, processed, width, height)
		dds_audit.append(audit)
		decoded_images[processed] = decoded

	make_contact_sheet(
		processed_by_family,
		processed_report,
		CONTACT_ROOT / "006_mediterranean_gameplay_contact_sheet.png",
	)
	make_contact_sheet(
		processed_by_family,
		processed_report,
		CONTACT_ROOT / "006_mediterranean_dds_decode_contact_sheet.png",
		decoded_images=decoded_images,
	)

	consumer_audit = validate_consumers_and_interface()
	report = {
		"expected_counts": {"focus": 8, "decision": 8, "idea": 8, "report": 1},
		"actual_counts": {
			family: sum(record["family"] == family for record in all_records)
			for family in ("focus", "decision", "idea", "report")
		},
		"assets": all_records,
		"dds_audit": dds_audit,
		"consumer_and_registration_audit": consumer_audit,
		"processed_hashes_unique_within_family": True,
		"official_imagegen_sources": 25,
		"fallbacks_used": [],
	}
	NOTES_ROOT.mkdir(parents=True, exist_ok=True)
	validation_path = NOTES_ROOT / "runtime_validation.json"
	validation_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
	print(json.dumps({"counts": report["actual_counts"], "dds_files": len(dds_audit), "validation": relative(validation_path)}, indent=2))


if __name__ == "__main__":
	main()
