#!/usr/bin/env python3
"""Build Event 006 northern/western Europe source previews.

The script performs documentary symbol processing and assembles contact sheets
from separately approved real-person portrait outputs. Real portraits are
finished only through ``.tools/process_hoi4_portrait.py``; this helper must not
reconstruct a face or overwrite those reviewed outputs with archival crops.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_PORTRAITS = ASSET_ROOT / "source_png" / "portraits"
SOURCE_SYMBOLS = ASSET_ROOT / "source_png" / "country_symbols"
PROCESSED_PORTRAITS = ASSET_ROOT / "processed_png" / "portraits"
PROCESSED_SYMBOLS = ASSET_ROOT / "processed_png" / "country_symbols"
CONTACT_SHEETS = ASSET_ROOT / "contact_sheets"
DDS_ROOT = ROOT / "gfx" / "leaders" / "006_independence_wave"

# Debeauvais is deliberately absent: the identified 1928 group photograph is
# too weak for an identity-safe final, while sharper candidates lack defensible
# United States rights. Keep his sprite id reserved in the handoff, but do not
# restore the rejected low-fidelity processed PNG or runtime DDS here.
PORTRAITS = (
    "rhi_josef_friedrich_matthes",
    "bay_rupprecht_of_bavaria",
)

SYMBOLS = {
    "acx_st_pirans_cross": "Cornwall: historical community motif only",
    "aex_flemish_lion_arms": "Flanders: historical lion-arms motif only",
    "afx_walloon_rooster": "Wallonia: 1913 motif via CC0 modern vector",
    "agx_west_frisian_flag": "Frisia: West Frisian provincial motif only",
    "ajx_saar_territory_1920_1935": "Saar: exact 1920-35 territory flag",
}

PORTRAIT_LABELS = {
    "bri_francois_debeauvais": "BRI: Francois Debeauvais, 1928 (nationalist route)",
    "rhi_josef_friedrich_matthes": "RHI: Josef F. Matthes, 1923 (separatist route)",
    "bay_rupprecht_of_bavaria": "BAY: Rupprecht, c. 1916 (restoration route)",
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidates = [
        Path("C:/Windows/Fonts") / filename,
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def prepare_directories() -> None:
    for directory in (PROCESSED_PORTRAITS, PROCESSED_SYMBOLS, CONTACT_SHEETS):
        directory.mkdir(parents=True, exist_ok=True)


def process_symbol(stem: str) -> Path:
    source = Image.open(SOURCE_SYMBOLS / f"{stem}_source.png").convert("RGBA")
    bbox = source.getbbox()
    if bbox:
        source = source.crop(bbox)
    source.thumbnail((520, 320), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (600, 400), "#eeeae1")
    x = (canvas.width - source.width) // 2
    y = (canvas.height - source.height) // 2
    canvas.alpha_composite(source, (x, y))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, canvas.width - 1, canvas.height - 1), outline="#615d55", width=2)
    output = PROCESSED_SYMBOLS / f"{stem}.png"
    canvas.save(output)
    return output


def draw_contain(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> None:
    left, top, right, bottom = box
    target = image.copy().convert("RGBA")
    target.thumbnail((right - left, bottom - top), Image.Resampling.LANCZOS)
    x = left + ((right - left) - target.width) // 2
    y = top + ((bottom - top) - target.height) // 2
    canvas.alpha_composite(target, (x, y))


def draw_label(draw: ImageDraw.ImageDraw, label: str, x: int, y: int, width: int) -> None:
    label_font = font(17, bold=True)
    lines = wrap(label, width=39)
    for line in lines[:3]:
        bbox = draw.textbbox((0, 0), line, font=label_font)
        draw.text((x + (width - (bbox[2] - bbox[0])) // 2, y), line, fill="#f4f0e8", font=label_font)
        y += 21


def build_contact_sheet(symbol_paths: dict[str, Path], portrait_paths: dict[str, Path]) -> Path:
    cards: list[tuple[str, Path, str]] = []
    cards.extend((stem, path, SYMBOLS[stem]) for stem, path in symbol_paths.items())
    cards.extend((stem, path, PORTRAIT_LABELS[stem]) for stem, path in portrait_paths.items())

    card_w, card_h = 360, 330
    cols = 4
    rows = (len(cards) + cols - 1) // cols
    header_h = 82
    sheet = Image.new("RGBA", (card_w * cols, header_h + card_h * rows), "#171b21")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 18), "Event 006 - Northern & Western Europe sourced assets", fill="#f4f0e8", font=font(28, bold=True))
    draw.text((29, 51), "Historical evidence and approved route-owned real portraits; BRI remains blocked", fill="#b8c1cc", font=font(16))

    for index, (_, path, label) in enumerate(cards):
        col = index % cols
        row = index // cols
        x = col * card_w
        y = header_h + row * card_h
        draw.rectangle((x + 8, y + 8, x + card_w - 8, y + card_h - 8), fill="#242a32", outline="#55606e", width=2)
        image = Image.open(path).convert("RGBA")
        draw_contain(sheet, image, (x + 28, y + 22, x + card_w - 28, y + 244))
        draw_label(draw, label, x + 18, y + 259, card_w - 36)

    output = CONTACT_SHEETS / "006_northern_western_europe_sourced_assets.png"
    sheet.convert("RGB").save(output, quality=95)
    return output


def build_dds_contact_sheet() -> Path | None:
    dds_paths = {
        stem: DDS_ROOT / f"portrait_{stem.split('_', 1)[0].upper()}_{stem.split('_', 1)[1]}.dds"
        for stem in PORTRAITS
    }
    if not all(path.exists() for path in dds_paths.values()):
        return None

    card_w, card_h = 360, 320
    header_h = 76
    sheet = Image.new("RGBA", (card_w * len(dds_paths), header_h + card_h), "#171b21")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 16), "Event 006 - Final portrait DDS decode", fill="#f4f0e8", font=font(28, bold=True))
    draw.text((29, 49), "156x210 uncompressed BGRA runtime files", fill="#b8c1cc", font=font(16))

    for index, (stem, path) in enumerate(dds_paths.items()):
        x = index * card_w
        y = header_h
        draw.rectangle((x + 8, y + 8, x + card_w - 8, y + card_h - 8), fill="#242a32", outline="#55606e", width=2)
        image = Image.open(path).convert("RGBA")
        draw_contain(sheet, image, (x + 92, y + 22, x + card_w - 92, y + 242))
        draw_label(draw, PORTRAIT_LABELS[stem], x + 18, y + 258, card_w - 36)

    output = CONTACT_SHEETS / "006_northern_western_europe_final_dds_decoded.png"
    sheet.convert("RGB").save(output, quality=95)
    return output


def main() -> None:
    prepare_directories()
    portrait_paths: dict[str, Path] = {}
    for stem in PORTRAITS:
        output = PROCESSED_PORTRAITS / f"portrait_{stem}.png"
        if not output.exists():
            raise FileNotFoundError(
                f"Missing approved portrait output: {output}. Run the required "
                ".tools/process_hoi4_portrait.py workflow first."
            )
        portrait_paths[stem] = output
    symbol_paths = {stem: process_symbol(stem) for stem in SYMBOLS}
    build_contact_sheet(symbol_paths, portrait_paths)
    build_dds_contact_sheet()


if __name__ == "__main__":
    main()
