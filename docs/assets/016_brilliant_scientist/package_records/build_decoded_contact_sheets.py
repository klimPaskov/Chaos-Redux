"""Create decoded-DDS review sheets for the Event 016 icon package."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]
RUNTIME_D = ROOT / "gfx/interface/decisions/016_brilliant_scientist/decisions"
RUNTIME_C = ROOT / "gfx/interface/decisions/016_brilliant_scientist/categories"
OUT = ROOT / "docs/assets/016_brilliant_scientist/contact_sheets"
DECISION_NAMES = [p.stem.removeprefix("decision_") for p in sorted(RUNTIME_D.glob("*.dds"))]
CATEGORY_NAMES = [p.stem.removeprefix("decision_category_") for p in sorted(RUNTIME_C.glob("*.dds"))]

def sheet(names, folder, title, out, columns, size):
    cw, ch = 160, 150
    rows = (len(names) + columns - 1) // columns
    canvas = Image.new("RGBA", (columns * cw, rows * ch + 30), (26, 28, 30, 255))
    draw = ImageDraw.Draw(canvas)
    draw.text((10, 7), title, fill=(240, 240, 240, 255))
    for i, name in enumerate(names):
        image = Image.open(folder / f"{('decision_' if folder.name == 'decisions' else 'decision_category_')}{name}.dds").convert("RGBA")
        image.thumbnail((128, 112), Image.Resampling.NEAREST)
        row, col = divmod(i, columns)
        canvas.alpha_composite(image, (col * cw + (cw - image.width) // 2, row * ch + 31 + (112 - image.height) // 2))
        draw.text((col * cw + 4, row * ch + 137), name[:23], fill=(220, 220, 220, 255))
    canvas.convert("RGB").save(out)

sheet(DECISION_NAMES, RUNTIME_D, "Event 016 decision icons — decoded DDS 32x32", OUT / "decision_icons_016_decoded_dds_contact_sheet.png", 8, (32, 32))
sheet(CATEGORY_NAMES, RUNTIME_C, "Event 016 decision categories — decoded DDS 50x40", OUT / "decision_categories_016_decoded_dds_contact_sheet.png", 5, (50, 40))
print({"decision_dds": len(DECISION_NAMES), "category_dds": len(CATEGORY_NAMES)})
