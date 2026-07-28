"""Deterministically process approved Chaos Warfare achievement masters.

The source masters and chroma-key extraction are evidence artifacts. This script
only performs mechanical resizing and derives the grey and not-eligible states.
It does not create or alter the achievement subjects.
"""

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parent
ALPHA_DIR = ROOT / "archive" / "alpha_png"
PROCESSED_DIR = ROOT / "processed_png"
OVERLAY_PATH = (
    ROOT.parents[3]
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "vanilla_reference"
    / "icons"
    / "achievements"
    / "overlay.png"
)


def save_png(image: Image.Image, path: Path) -> None:
    image.save(path, format="PNG", optimize=True)


def scrub_residual_key_edge(image: Image.Image) -> Image.Image:
    """Remove subpixel green matte residue left by the chroma-key extraction."""
    pixels = []
    for red, green, blue, alpha in image.getdata():
        if red < 60 and green > 160 and blue < 60:
            pixels.append((red, green, blue, 0))
        else:
            pixels.append((red, green, blue, alpha))
    image.putdata(pixels)
    return image


def build_contact_sheet(asset_ids: list[str]) -> None:
    sheet_dir = ROOT / "contact_sheets"
    sheet_dir.mkdir(parents=True, exist_ok=True)
    row_height = 156
    cell_size = 128
    label_width = 330
    sheet = Image.new("RGBA", (label_width + cell_size * 3, row_height * len(asset_ids)), (28, 28, 28, 255))
    from PIL import ImageDraw

    draw = ImageDraw.Draw(sheet)
    for row, asset_id in enumerate(asset_ids):
        y = row * row_height
        draw.text((8, y + 66), asset_id, fill=(230, 230, 230, 255), anchor="lm")
        for column, suffix in enumerate(("", "_grey", "_not_eligible")):
            image = Image.open(PROCESSED_DIR / f"{asset_id}{suffix}.png").convert("RGBA")
            image = ImageOps.contain(image, (cell_size, cell_size), Image.Resampling.NEAREST)
            x = label_width + column * cell_size
            sheet.alpha_composite(image, (x, y + 4))
            draw.text((x + 4, y + 136), ("completed", "grey", "not eligible")[column], fill=(205, 205, 205, 255))
    save_png(sheet, sheet_dir / "achievement_triplets_contact_sheet.png")


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    overlay = Image.open(OVERLAY_PATH).convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS)

    masters = sorted(ALPHA_DIR.glob("*_alpha_master.png"))
    if len(masters) != 15:
        raise SystemExit(f"expected 15 alpha masters, found {len(masters)}")

    asset_ids = []
    for master_path in masters:
        asset_id = master_path.stem.removesuffix("_alpha_master")
        asset_ids.append(asset_id)
        completed = Image.open(master_path).convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS)
        completed = scrub_residual_key_edge(completed)
        grey = ImageOps.grayscale(completed.convert("RGB")).convert("RGBA")
        grey.putalpha(completed.getchannel("A"))
        not_eligible = Image.alpha_composite(grey, overlay)

        save_png(completed, PROCESSED_DIR / f"{asset_id}.png")
        save_png(grey, PROCESSED_DIR / f"{asset_id}_grey.png")
        save_png(not_eligible, PROCESSED_DIR / f"{asset_id}_not_eligible.png")

    build_contact_sheet(asset_ids)


if __name__ == "__main__":
    main()
