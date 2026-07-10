#!/usr/bin/env python3
"""Build deterministic Repression Ledger chrome from the frozen GUI dimensions."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "docs/assets/system_camp_repression_rework/source/ui"
PROCESSED = ROOT / "docs/assets/system_camp_repression_rework/processed/ui"


INK = (17, 20, 20, 255)
PAPER = (62, 57, 48, 244)
PAPER_LIGHT = (89, 80, 64, 236)
BRASS = (151, 122, 67, 255)
BRASS_DARK = (83, 67, 39, 255)
RED = (124, 39, 34, 255)
PURPLE = (79, 55, 88, 255)
GREEN = (55, 91, 65, 255)
TRANSPARENT = (0, 0, 0, 0)


def grain(image: Image.Image, strength: int = 8) -> Image.Image:
	pixels = image.load()
	for y in range(image.height):
		for x in range(image.width):
			r, g, b, a = pixels[x, y]
			if not a:
				continue
			n = ((x * 37 + y * 73 + x * y * 3) % (strength * 2 + 1)) - strength
			pixels[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)), a)
	return image


def ledger_panel(size: tuple[int, int], inset: int = 5, accent=BRASS) -> Image.Image:
	img = Image.new("RGBA", size, TRANSPARENT)
	d = ImageDraw.Draw(img)
	d.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=7, fill=INK, outline=BRASS_DARK, width=2)
	d.rounded_rectangle((inset, inset, size[0] - inset - 1, size[1] - inset - 1), radius=5, fill=PAPER, outline=accent, width=1)
	for y in range(inset + 13, size[1] - inset, 17):
		d.line((inset + 8, y, size[0] - inset - 8, y), fill=(34, 33, 29, 35), width=1)
	return grain(img)


def button_sheet(size: tuple[int, int], accent=BRASS) -> Image.Image:
	w, h = size
	img = Image.new("RGBA", (w * 3, h), TRANSPARENT)
	for frame, (fill, edge) in enumerate(((PAPER_LIGHT, BRASS_DARK), ((104, 89, 65, 255), accent), ((43, 40, 35, 255), (72, 65, 54, 255)))):
		d = ImageDraw.Draw(img)
		x0 = frame * w
		d.rounded_rectangle((x0, 0, x0 + w - 1, h - 1), radius=5, fill=INK, outline=edge, width=2)
		d.rounded_rectangle((x0 + 3, 3, x0 + w - 4, h - 4), radius=4, fill=fill, outline=edge, width=1)
		d.line((x0 + 9, h - 7, x0 + w - 10, h - 7), fill=edge, width=2)
	return grain(img)


def seal(size: int, accent, glyph: str) -> Image.Image:
	img = Image.new("RGBA", (size, size), TRANSPARENT)
	d = ImageDraw.Draw(img)
	c = size // 2
	d.ellipse((5, 5, size - 6, size - 6), fill=(25, 24, 22, 235), outline=accent, width=4)
	d.ellipse((14, 14, size - 15, size - 15), fill=(51, 47, 40, 245), outline=accent, width=2)
	if glyph == "evidence":
		d.rectangle((c - 20, c - 24, c + 19, c + 23), fill=(210, 196, 165, 255), outline=INK, width=2)
		for y in range(c - 15, c + 16, 8):
			d.line((c - 13, y, c + 12, y), fill=PURPLE, width=2)
		d.ellipse((c + 4, c + 5, c + 24, c + 25), outline=PURPLE, width=4)
	elif glyph == "reform":
		d.polygon(((c, c - 27), (c + 9, c - 8), (c + 28, c - 5), (c + 14, c + 9), (c + 18, c + 29), (c, c + 18), (c - 18, c + 29), (c - 14, c + 9), (c - 28, c - 5), (c - 9, c - 8)), fill=GREEN, outline=(185, 206, 175, 255))
	return img.filter(ImageFilter.GaussianBlur(0.15))


def icon(size: int, kind: str, accent) -> Image.Image:
	img = Image.new("RGBA", (size, size), TRANSPARENT)
	d = ImageDraw.Draw(img)
	d.ellipse((2, 2, size - 3, size - 3), fill=(26, 28, 27, 250), outline=accent, width=2)
	c = size // 2
	if kind == "ledger":
		d.rectangle((c - 11, c - 13, c + 10, c + 13), fill=(202, 188, 155, 255), outline=INK, width=1)
		for y in range(c - 8, c + 10, 6):
			d.line((c - 7, y, c + 6, y), fill=accent, width=1)
	elif kind == "population":
		d.ellipse((c - 5, c - 11, c + 5, c - 1), fill=accent)
		d.polygon(((c - 13, c + 13), (c - 9, c + 1), (c, c - 2), (c + 9, c + 1), (c + 13, c + 13)), fill=accent)
	elif kind == "labor":
		d.line((c - 11, c + 11, c + 10, c - 10), fill=accent, width=5)
		d.rectangle((c + 4, c - 13, c + 13, c - 5), fill=accent)
	elif kind == "evidence":
		d.rectangle((c - 10, c - 12, c + 9, c + 12), fill=(204, 191, 161, 255), outline=accent, width=2)
		d.line((c - 6, c - 5, c + 5, c - 5), fill=accent, width=2)
		d.line((c - 6, c + 1, c + 5, c + 1), fill=accent, width=2)
	elif kind == "reform":
		d.arc((c - 13, c - 13, c + 13, c + 13), 30, 300, fill=accent, width=4)
		d.polygon(((c + 12, c - 8), (c + 14, c + 2), (c + 4, c - 1)), fill=accent)
	elif kind == "guard":
		d.polygon(((c, c - 14), (c + 11, c - 8), (c + 8, c + 8), (c, c + 14), (c - 8, c + 8), (c - 11, c - 8)), fill=accent, outline=(215, 204, 179, 255))
	elif kind == "rail":
		d.line((c - 9, c - 13, c - 9, c + 13), fill=accent, width=3)
		d.line((c + 9, c - 13, c + 9, c + 13), fill=accent, width=3)
		for y in range(c - 10, c + 11, 6):
			d.line((c - 12, y, c + 12, y), fill=accent, width=2)
	return img


def save(name: str, image: Image.Image) -> None:
	SOURCE.mkdir(parents=True, exist_ok=True)
	PROCESSED.mkdir(parents=True, exist_ok=True)
	image.save(SOURCE / f"{name}_source.png")
	image.save(PROCESSED / f"{name}.png")


def build_contact_sheet() -> None:
	files = sorted(PROCESSED.glob("*.png"))
	cell_w, cell_h, columns = 260, 170, 4
	rows = (len(files) + columns - 1) // columns
	sheet = Image.new("RGBA", (cell_w * columns, cell_h * rows), (25, 25, 23, 255))
	d = ImageDraw.Draw(sheet)
	for index, path in enumerate(files):
		asset = Image.open(path).convert("RGBA")
		asset.thumbnail((cell_w - 24, cell_h - 42), Image.Resampling.LANCZOS)
		x = (index % columns) * cell_w + (cell_w - asset.width) // 2
		y = (index // columns) * cell_h + 8
		sheet.alpha_composite(asset, (x, y))
		d.text(((index % columns) * cell_w + 8, (index // columns) * cell_h + cell_h - 27), path.stem, fill=(220, 208, 178, 255))
	contact_dir = ROOT / "docs/assets/system_camp_repression_rework/contact_sheets"
	contact_dir.mkdir(parents=True, exist_ok=True)
	sheet.convert("RGB").save(contact_dir / "repression_ledger_ui_contact_sheet.jpg", quality=92)


def main() -> None:
	save("GFX_repression_ledger_window_bg", ledger_panel((900, 560), 7, BRASS))
	save("GFX_repression_ledger_summary_strip", ledger_panel((864, 52), 4, BRASS))
	save("GFX_repression_ledger_card_bg", ledger_panel((344, 90), 4, BRASS_DARK))
	save("GFX_repression_ledger_country_card_bg", ledger_panel((710, 304), 5, BRASS_DARK))
	save("GFX_repression_ledger_tab_button", button_sheet((140, 42), BRASS))
	save("GFX_repression_ledger_action_button", button_sheet((136, 38), BRASS))
	save("GFX_repression_ledger_warning_frame_static", ledger_panel((710, 48), 2, RED))
	save("GFX_repression_ledger_selected_state_frame_static", ledger_panel((710, 38), 2, BRASS))
	save("GFX_repression_ledger_critical_frame_static", ledger_panel((710, 48), 2, (180, 36, 30, 255)))
	save("GFX_repression_ledger_evidence_seal_static", seal(112, PURPLE, "evidence"))
	save("GFX_repression_ledger_reform_seal_static", seal(112, GREEN, "reform"))
	save("GFX_decision_category_repression_ledger", icon(53, "ledger", BRASS))
	save("GFX_decision_open_repression_ledger", icon(32, "ledger", BRASS))
	for name, kind, accent in (
		("GFX_repression_ledger_tab_overview", "ledger", BRASS),
		("GFX_repression_ledger_tab_state_pools", "population", BRASS),
		("GFX_repression_ledger_tab_sites", "guard", RED),
		("GFX_repression_ledger_tab_country", "ledger", (94, 121, 145, 255)),
		("GFX_repression_ledger_tab_discovery", "evidence", PURPLE),
		("GFX_repression_ledger_population_pressure", "population", RED),
		("GFX_repression_ledger_labor_output", "labor", BRASS),
		("GFX_repression_ledger_evidence_risk", "evidence", PURPLE),
		("GFX_repression_ledger_reform_pressure", "reform", GREEN),
		("GFX_repression_ledger_guard_burden", "guard", (105, 126, 143, 255)),
		("GFX_repression_ledger_rail_burden", "rail", (121, 106, 79, 255)),
	):
		save(name, icon(32 if "tab_" in name else 24, kind, accent))
	build_contact_sheet()


if __name__ == "__main__":
	main()
