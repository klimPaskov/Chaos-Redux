#!/usr/bin/env python3
"""Build review-only sheets for Event 015 Necessary Ground case cards.

This file never produces runtime art. It only lays out existing source,
processed, and decoded images with labels for human inspection.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from process_case_cards import trim_external_white_matte


STATES = (
	("no_target", "NO TARGET"),
	("target_eligible", "TARGET ELIGIBLE"),
	("target_selected", "TARGET SELECTED"),
	("offer_pending", "OFFER PENDING"),
	("counteroffer", "COUNTEROFFER"),
	("refusal", "REFUSAL"),
	("ultimatum_available", "ULTIMATUM AVAILABLE"),
	("expired", "CASE EXPIRED"),
	("stewardship_active", "STEWARDSHIP ACTIVE"),
	("associate_established", "ASSOCIATE ESTABLISHED"),
)

REJECTED = (
	(
		"TARGET SELECTED | REJECTED 2.5197:1",
		"utopia_ledger_case_target_selected_rejected_2_5197_source.png",
	),
	(
		"ULTIMATUM | REJECTED 2.5006:1",
		"utopia_ledger_case_ultimatum_available_rejected_2_5006_source.png",
	),
	(
		"TARGET SELECTED RETRY | REJECTED 2.5006:1",
		"utopia_ledger_case_target_selected_retry_rejected_2_5006_source.png",
	),
)

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CONTACT_DIR = PACKAGE_ROOT / "contact_sheets"
NATIVE_DIR = PACKAGE_ROOT / "native_size_review"
FONT = ImageFont.load_default()
BACKGROUND = (22, 22, 19, 255)
LABEL = (226, 215, 186, 255)


def make_two_column_sheet(
	items: list[tuple[str, Image.Image]],
	cell_size: tuple[int, int],
	output: Path,
) -> None:
	columns = 2
	rows = (len(items) + columns - 1) // columns
	margin = 16
	label_height = 22
	cell_width, cell_height = cell_size
	canvas = Image.new(
		"RGBA",
		(
			margin + columns * (cell_width + margin),
			margin + rows * (cell_height + label_height + margin),
		),
		BACKGROUND,
	)
	draw = ImageDraw.Draw(canvas)
	for index, (label, image) in enumerate(items):
		column = index % columns
		row = index // columns
		x = margin + column * (cell_width + margin)
		y = margin + row * (cell_height + label_height + margin)
		draw.text((x, y), label, fill=LABEL, font=FONT)
		thumb = ImageOps.contain(image.convert("RGBA"), cell_size, Image.Resampling.LANCZOS)
		paste_x = x + (cell_width - thumb.width) // 2
		paste_y = y + label_height + (cell_height - thumb.height) // 2
		canvas.alpha_composite(thumb, (paste_x, paste_y))
	output.parent.mkdir(parents=True, exist_ok=True)
	canvas.convert("RGB").save(output, format="PNG", optimize=True)


def make_native_plus_nearest_sheet(items: list[tuple[str, Image.Image]], output: Path) -> None:
	margin = 12
	label_height = 18
	native_width, native_height = (300, 96)
	scale = 2
	large_width, large_height = native_width * scale, native_height * scale
	cell_height = label_height + native_height + margin + large_height
	canvas = Image.new(
		"RGBA",
		(large_width + margin * 2, margin + len(items) * (cell_height + margin)),
		BACKGROUND,
	)
	draw = ImageDraw.Draw(canvas)
	for index, (label, image) in enumerate(items):
		y = margin + index * (cell_height + margin)
		draw.text((margin, y), f"{label} | 1x then 2x nearest", fill=LABEL, font=FONT)
		native = image.convert("RGBA")
		canvas.alpha_composite(native, (margin, y + label_height))
		nearest = native.resize((large_width, large_height), Image.Resampling.NEAREST)
		canvas.alpha_composite(nearest, (margin, y + label_height + native_height + margin))
	output.parent.mkdir(parents=True, exist_ok=True)
	canvas.convert("RGB").save(output, format="PNG", optimize=True)


def load_family(directory: Path, source_suffix: str = "") -> list[tuple[str, Image.Image]]:
	items: list[tuple[str, Image.Image]] = []
	for state, label in STATES:
		path = directory / f"utopia_ledger_case_{state}{source_suffix}.png"
		with Image.open(path) as image:
			items.append((label, image.convert("RGBA")))
	return items


def trim_family(items: list[tuple[str, Image.Image]]) -> list[tuple[str, Image.Image]]:
	return [(label, trim_external_white_matte(image)[0]) for label, image in items]


def load_rejected() -> list[tuple[str, Image.Image]]:
	items: list[tuple[str, Image.Image]] = []
	for label, filename in REJECTED:
		path = PACKAGE_ROOT / "sources" / "rejected" / filename
		with Image.open(path) as image:
			items.append((label, image.convert("RGBA")))
	return items


def main() -> int:
	CONTACT_DIR.mkdir(parents=True, exist_ok=True)
	NATIVE_DIR.mkdir(parents=True, exist_ok=True)

	sources = load_family(PACKAGE_ROOT / "sources", "_source")
	trimmed_sources = trim_family(sources)
	rejected = load_rejected()
	processed = load_family(PACKAGE_ROOT / "processed_png")
	decoded = load_family(PACKAGE_ROOT / "decoded_png")

	make_two_column_sheet(
		sources,
		(600, 220),
		CONTACT_DIR / "case_cards_source_contact_sheet.png",
	)
	make_two_column_sheet(
		trimmed_sources,
		(600, 220),
		CONTACT_DIR / "case_cards_post_matte_source_contact_sheet.png",
	)
	make_two_column_sheet(
		rejected,
		(600, 240),
		CONTACT_DIR / "case_cards_rejected_aspect_contact_sheet.png",
	)
	make_two_column_sheet(
		processed,
		(300, 96),
		CONTACT_DIR / "case_cards_processed_contact_sheet.png",
	)
	make_two_column_sheet(
		decoded,
		(300, 96),
		CONTACT_DIR / "case_cards_decoded_contact_sheet.png",
	)
	make_native_plus_nearest_sheet(
		decoded,
		NATIVE_DIR / "case_cards_native_plus_2x_nearest.png",
	)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
