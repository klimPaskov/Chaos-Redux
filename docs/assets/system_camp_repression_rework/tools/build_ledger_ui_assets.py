#!/usr/bin/env python3
"""Build the Repression Ledger sprites from frozen ImageGen source artwork."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance


ROOT = Path(__file__).resolve().parents[4]
IMAGEGEN_SOURCE = ROOT / "docs/assets/system_camp_repression_rework/source/ui_imagegen"
SOURCE = ROOT / "docs/assets/system_camp_repression_rework/source/ui"
PROCESSED = ROOT / "docs/assets/system_camp_repression_rework/processed/ui"
PACKAGE_DDS = ROOT / "docs/assets/system_camp_repression_rework/dds/ui"
LIVE_DDS = ROOT / "gfx/interface/camp_repression"
CONVERTER = ROOT / ".tools/convert_to_dds.py"
CONTACT_SHEET = ROOT / "docs/assets/system_camp_repression_rework/contact_sheets/repression_ledger_ui_contact_sheet.jpg"

WINDOW_SOURCE = IMAGEGEN_SOURCE / "repression_ledger_window_imagegen_source.png"
ATLAS_SOURCE = IMAGEGEN_SOURCE / "repression_ledger_icon_atlas_imagegen_source.png"

BRASS = (155, 116, 67, 255)
BRASS_DARK = (63, 45, 31, 255)
BURGUNDY = (126, 43, 36, 255)
PURPLE = (92, 62, 111, 255)
GREEN = (58, 99, 70, 255)
TRANSPARENT = (0, 0, 0, 0)


ASSET_SIZES = {
	"GFX_decision_category_repression_ledger": (53, 53),
	"GFX_decision_open_repression_ledger": (32, 32),
	"GFX_repression_ledger_window_bg": (900, 560),
	"GFX_repression_ledger_summary_strip": (864, 52),
	"GFX_repression_ledger_card_bg": (344, 90),
	"GFX_repression_ledger_country_card_bg": (710, 304),
	"GFX_repression_ledger_tab_button": (420, 42),
	"GFX_repression_ledger_action_button": (408, 38),
	"GFX_repression_ledger_tab_overview": (32, 32),
	"GFX_repression_ledger_tab_state_pools": (32, 32),
	"GFX_repression_ledger_tab_sites": (32, 32),
	"GFX_repression_ledger_tab_country": (32, 32),
	"GFX_repression_ledger_tab_discovery": (32, 32),
	"GFX_repression_ledger_population_pressure": (24, 24),
	"GFX_repression_ledger_labor_output": (24, 24),
	"GFX_repression_ledger_evidence_risk": (24, 24),
	"GFX_repression_ledger_reform_pressure": (24, 24),
	"GFX_repression_ledger_guard_burden": (24, 24),
	"GFX_repression_ledger_rail_burden": (24, 24),
	"GFX_repression_ledger_warning_frame_static": (710, 48),
	"GFX_repression_ledger_evidence_seal_static": (112, 112),
	"GFX_repression_ledger_reform_seal_static": (112, 112),
	"GFX_repression_ledger_selected_state_frame_static": (710, 38),
	"GFX_repression_ledger_critical_frame_static": (710, 48),
}


def cover(image: Image.Image, size: tuple[int, int], anchor: tuple[float, float] = (0.5, 0.5)) -> Image.Image:
	"""Resize and crop without distorting the ImageGen source."""
	target_w, target_h = size
	scale = max(target_w / image.width, target_h / image.height)
	resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
	left = round((resized.width - target_w) * anchor[0])
	top = round((resized.height - target_h) * anchor[1])
	return resized.crop((left, top, left + target_w, top + target_h))


def imagegen_panel(background: Image.Image, size: tuple[int, int], anchor: tuple[float, float], accent=BRASS) -> Image.Image:
	panel = cover(background, size, anchor).convert("RGBA")
	shade = Image.new("RGBA", size, (7, 7, 7, 88))
	panel = Image.alpha_composite(panel, shade)
	draw = ImageDraw.Draw(panel)
	draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=5, outline=BRASS_DARK, width=3)
	draw.rounded_rectangle((4, 4, size[0] - 5, size[1] - 5), radius=4, outline=accent, width=1)
	return panel


def button_sheet(background: Image.Image, frame_size: tuple[int, int], anchor: tuple[float, float], accent=BRASS) -> Image.Image:
	frame = imagegen_panel(background, frame_size, anchor, accent)
	frames = []
	for brightness, saturation, overlay in (
		(0.92, 0.85, (0, 0, 0, 18)),
		(1.16, 1.15, (110, 70, 25, 16)),
		(0.55, 0.55, (0, 0, 0, 92)),
	):
		state = ImageEnhance.Brightness(frame).enhance(brightness)
		state = ImageEnhance.Color(state).enhance(saturation)
		state = Image.alpha_composite(state, Image.new("RGBA", frame_size, overlay))
		frames.append(state)
	out = Image.new("RGBA", (frame_size[0] * 3, frame_size[1]), TRANSPARENT)
	for index, state in enumerate(frames):
		out.alpha_composite(state, (index * frame_size[0], 0))
	return out


def atlas_cell(atlas: Image.Image, index: int) -> Image.Image:
	column = index % 4
	row = index // 4
	x0 = round(column * atlas.width / 4)
	x1 = round((column + 1) * atlas.width / 4)
	y0 = round(row * atlas.height / 4)
	y1 = round((row + 1) * atlas.height / 4)
	margin_x = round((x1 - x0) * 0.055)
	margin_y = round((y1 - y0) * 0.055)
	return atlas.crop((x0 + margin_x, y0 + margin_y, x1 - margin_x, y1 - margin_y)).convert("RGBA")


def make_black_transparent(image: Image.Image) -> Image.Image:
	pixels = image.load()
	for y in range(image.height):
		for x in range(image.width):
			r, g, b, _ = pixels[x, y]
			light = max(r, g, b)
			alpha = max(0, min(255, (light - 5) * 5))
			pixels[x, y] = (r, g, b, alpha)
	bounds = image.getbbox()
	return image.crop(bounds) if bounds else image


def icon_from_atlas(atlas: Image.Image, index: int, size: tuple[int, int], padding: float = 0.06) -> Image.Image:
	art = make_black_transparent(atlas_cell(atlas, index))
	max_w = max(1, round(size[0] * (1 - padding * 2)))
	max_h = max(1, round(size[1] * (1 - padding * 2)))
	art.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
	out = Image.new("RGBA", size, TRANSPARENT)
	out.alpha_composite(art, ((size[0] - art.width) // 2, (size[1] - art.height) // 2))
	return out


def state_frame(background: Image.Image, atlas: Image.Image, size: tuple[int, int], icon_index: int, accent) -> Image.Image:
	frame = imagegen_panel(background, size, (0.62, 0.65), accent)
	frame = Image.alpha_composite(frame, Image.new("RGBA", size, (0, 0, 0, 42)))
	mark_size = min(size[1] - 8, 38)
	mark = icon_from_atlas(atlas, icon_index, (mark_size, mark_size), 0.02)
	frame.alpha_composite(mark, (8, (size[1] - mark_size) // 2))
	return frame


def save(name: str, image: Image.Image) -> None:
	SOURCE.mkdir(parents=True, exist_ok=True)
	PROCESSED.mkdir(parents=True, exist_ok=True)
	image.save(SOURCE / f"{name}_source.png")
	image.save(PROCESSED / f"{name}.png")


def convert_to_dds(name: str) -> None:
	PACKAGE_DDS.mkdir(parents=True, exist_ok=True)
	LIVE_DDS.mkdir(parents=True, exist_ok=True)
	width, height = ASSET_SIZES[name]
	processed = PROCESSED / f"{name}.png"
	package = PACKAGE_DDS / f"{name}.dds"
	command = [
		sys.executable,
		str(CONVERTER),
		"--input",
		str(processed),
		"--output",
		str(package),
		"--width",
		str(width),
		"--height",
		str(height),
	]
	subprocess.run(command, check=True)
	LIVE_DDS.joinpath(package.name).write_bytes(package.read_bytes())


def build_contact_sheet() -> None:
	files = sorted(PROCESSED.glob("*.png"))
	cell_w, cell_h, columns = 300, 190, 4
	rows = (len(files) + columns - 1) // columns
	sheet = Image.new("RGBA", (cell_w * columns, cell_h * rows), (19, 18, 17, 255))
	draw = ImageDraw.Draw(sheet)
	for index, path in enumerate(files):
		asset = Image.open(path).convert("RGBA")
		asset.thumbnail((cell_w - 24, cell_h - 46), Image.Resampling.LANCZOS)
		x = (index % columns) * cell_w + (cell_w - asset.width) // 2
		y = (index // columns) * cell_h + 8
		sheet.alpha_composite(asset, (x, y))
		draw.text(((index % columns) * cell_w + 8, (index // columns) * cell_h + cell_h - 29), path.stem, fill=(222, 205, 170, 255))
	CONTACT_SHEET.parent.mkdir(parents=True, exist_ok=True)
	sheet.convert("RGB").save(CONTACT_SHEET, quality=94)


def main() -> None:
	if not WINDOW_SOURCE.exists() or not ATLAS_SOURCE.exists():
		raise FileNotFoundError("The frozen ImageGen Ledger sources are missing")
	background = Image.open(WINDOW_SOURCE).convert("RGBA")
	atlas = Image.open(ATLAS_SOURCE).convert("RGBA")

	save("GFX_repression_ledger_window_bg", cover(background, (900, 560)))
	save("GFX_repression_ledger_summary_strip", imagegen_panel(background, (864, 52), (0.50, 0.24), BRASS))
	save("GFX_repression_ledger_card_bg", imagegen_panel(background, (344, 90), (0.38, 0.58), BRASS_DARK))
	save("GFX_repression_ledger_country_card_bg", imagegen_panel(background, (710, 304), (0.56, 0.55), BRASS_DARK))
	save("GFX_repression_ledger_tab_button", button_sheet(background, (140, 42), (0.23, 0.42), BRASS))
	save("GFX_repression_ledger_action_button", button_sheet(background, (136, 38), (0.72, 0.70), BRASS))
	save("GFX_repression_ledger_warning_frame_static", state_frame(background, atlas, (710, 48), 11, BURGUNDY))
	save("GFX_repression_ledger_selected_state_frame_static", state_frame(background, atlas, (710, 38), 1, BRASS))
	save("GFX_repression_ledger_critical_frame_static", state_frame(background, atlas, (710, 48), 15, (184, 43, 34, 255)))
	save("GFX_repression_ledger_evidence_seal_static", icon_from_atlas(atlas, 4, (112, 112), 0.01))
	save("GFX_repression_ledger_reform_seal_static", icon_from_atlas(atlas, 9, (112, 112), 0.01))

	save("GFX_decision_category_repression_ledger", icon_from_atlas(atlas, 0, (53, 53), 0.02))
	save("GFX_decision_open_repression_ledger", icon_from_atlas(atlas, 0, (32, 32), 0.01))
	icon_map = {
		"GFX_repression_ledger_tab_overview": (0, 32),
		"GFX_repression_ledger_tab_state_pools": (1, 32),
		"GFX_repression_ledger_tab_sites": (2, 32),
		"GFX_repression_ledger_tab_country": (3, 32),
		"GFX_repression_ledger_tab_discovery": (4, 32),
		"GFX_repression_ledger_population_pressure": (5, 24),
		"GFX_repression_ledger_labor_output": (6, 24),
		"GFX_repression_ledger_evidence_risk": (10, 24),
		"GFX_repression_ledger_reform_pressure": (9, 24),
		"GFX_repression_ledger_guard_burden": (7, 24),
		"GFX_repression_ledger_rail_burden": (8, 24),
	}
	for name, (index, size) in icon_map.items():
		save(name, icon_from_atlas(atlas, index, (size, size), 0.01))

	for name in ASSET_SIZES:
		convert_to_dds(name)
	build_contact_sheet()


if __name__ == "__main__":
	main()
