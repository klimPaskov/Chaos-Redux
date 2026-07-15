#!/usr/bin/env python3
"""Build Event 006 real-person source/candidate/canonical review sheets.

This is an evidence-only helper. It does not alter portrait masters, processed
PNGs, DDS files, or a person's face. The sheets keep the attributed archival
source, the explicit identity crop, each accepted or rejected candidate, and
the canonical vanilla leader references visible in one place.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_ROOT = ASSET_ROOT / "source_png" / "portraits"
PROCESSED_ROOT = ASSET_ROOT / "processed_png" / "portraits"
OUTPUT_ROOT = ASSET_ROOT / "contact_sheets" / "portraits"
DDS_ROOT = ROOT / "gfx" / "leaders" / "006_independence_wave"
REFERENCE_ROOT = (
    ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "vanilla_reference"
    / "portraits"
    / "leaders"
)

CANONICAL_REFERENCES = (
    ("Canonical: Thorvald Stauning", REFERENCE_ROOT / "den_thorvald_stauning.png"),
    ("Canonical: Carl Mannerheim", REFERENCE_ROOT / "fin_carl_mannerheim.png"),
    ("Canonical: Eamon de Valera", REFERENCE_ROOT / "ire_eamon_de_valera.png"),
)


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidate = Path("C:/Windows/Fonts") / filename
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def contain(image: Image.Image, width: int, height: int) -> Image.Image:
    preview = image.convert("RGBA")
    preview.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (width, height), "#11151b")
    x = (width - preview.width) // 2
    y = (height - preview.height) // 2
    canvas.alpha_composite(preview, (x, y))
    return canvas


def card_image(path: Path, crop: tuple[int, int, int, int] | None = None) -> Image.Image:
    image = Image.open(path).convert("RGBA")
    if crop is not None:
        image = image.crop(crop)
    return contain(image, 238, 256)


def draw_wrapped_label(
    draw: ImageDraw.ImageDraw,
    label: str,
    left: int,
    top: int,
    width: int,
    *,
    blocked: bool = False,
) -> None:
    label_font = font(15, bold=True)
    color = "#f0ad9e" if blocked else "#f4f0e8"
    for line in wrap(label, width=31)[:3]:
        bounds = draw.textbbox((0, 0), line, font=label_font)
        text_width = bounds[2] - bounds[0]
        draw.text((left + (width - text_width) // 2, top), line, fill=color, font=label_font)
        top += 19


def build_sheet(
    filename: str,
    title: str,
    subtitle: str,
    cards: list[tuple[str, Path, tuple[int, int, int, int] | None, bool]],
) -> Path:
    card_width = 270
    card_height = 340
    header_height = 92
    sheet = Image.new("RGBA", (card_width * len(cards), header_height + card_height), "#171b21")
    draw = ImageDraw.Draw(sheet)
    draw.text((26, 15), title, fill="#f4f0e8", font=font(28, bold=True))
    draw.text((27, 51), subtitle, fill="#b8c1cc", font=font(16))

    for index, (label, path, crop, blocked) in enumerate(cards):
        left = index * card_width
        top = header_height
        draw.rectangle(
            (left + 8, top + 8, left + card_width - 8, top + card_height - 8),
            fill="#242a32",
            outline="#945d55" if blocked else "#55606e",
            width=2,
        )
        preview = card_image(path, crop)
        sheet.alpha_composite(preview, (left + 16, top + 18))
        draw_wrapped_label(draw, label, left + 12, top + 282, card_width - 24, blocked=blocked)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_ROOT / filename
    sheet.convert("RGB").save(output, quality=96)
    return output


def main() -> None:
    matthes_source = SOURCE_ROOT / "rhi_josef_friedrich_matthes_source.jpg"
    matthes_cards = [
        ("1923 Bain source (full frame)", matthes_source, None, False),
        ("1923 archival identity crop", matthes_source, (174, 57, 558, 574), False),
        (
            "ImageGen identity-preserving master",
            SOURCE_ROOT / "imagegen_edits" / "portrait_rhi_josef_friedrich_matthes_imagegen_master.png",
            None,
            False,
        ),
        ("Approved 156x210 processed PNG", PROCESSED_ROOT / "portrait_rhi_josef_friedrich_matthes.png", None, False),
        ("Decoded runtime DDS", DDS_ROOT / "portrait_RHI_josef_friedrich_matthes.dds", None, False),
        *[(label, path, None, False) for label, path in CANONICAL_REFERENCES],
    ]
    build_sheet(
        "portrait_rhi_josef_friedrich_matthes_source_candidate_canonical.png",
        "Event 006 — Josef Friedrich Matthes real-person portrait review",
        "Attributed archival identity source → identity-preserving candidate → processed final → canonical vanilla references",
        matthes_cards,
    )

    rupprecht_source = SOURCE_ROOT / "bay_rupprecht_of_bavaria_source.jpg"
    rupprecht_cards = [
        ("c.1916 Grainer source (full frame)", rupprecht_source, None, False),
        ("c.1916 archival identity crop", rupprecht_source, (410, 145, 1762, 1967), False),
        (
            "ImageGen first pass (rejected moustache)",
            SOURCE_ROOT / "imagegen_edits" / "portrait_bay_rupprecht_of_bavaria_imagegen_candidate_01.png",
            None,
            True,
        ),
        (
            "Corrected identity-preserving master",
            SOURCE_ROOT / "imagegen_edits" / "portrait_bay_rupprecht_of_bavaria_imagegen_master.png",
            None,
            False,
        ),
        ("Approved 156x210 processed PNG", PROCESSED_ROOT / "portrait_bay_rupprecht_of_bavaria.png", None, False),
        ("Decoded runtime DDS", DDS_ROOT / "portrait_BAY_rupprecht_of_bavaria.dds", None, False),
        *[(label, path, None, False) for label, path in CANONICAL_REFERENCES],
    ]
    build_sheet(
        "portrait_bay_rupprecht_of_bavaria_source_candidate_canonical.png",
        "Event 006 — Rupprecht of Bavaria real-person portrait review",
        "Attributed archival identity source → corrected candidate → processed final → canonical vanilla references",
        rupprecht_cards,
    )

    debeauvais_source = SOURCE_ROOT / "bri_francois_debeauvais_group_source.jpg"
    debeauvais_cards = [
        ("1928 Breiz Atao source (full group)", debeauvais_source, None, False),
        ("1928 identity crop — insufficient detail", debeauvais_source, (246, 54, 392, 251), True),
        (
            "1932 Ouest-Eclair candidate — US rights unproved",
            SOURCE_ROOT / "candidates" / "bri_francois_debeauvais_1932_ouest_eclair_rejected_us_rights.png",
            None,
            True,
        ),
        (
            "1933 Breiz Atao candidate — rights record contradictory",
            SOURCE_ROOT / "candidates" / "bri_francois_debeauvais_1933_breiz_atao_rejected_rights_record.png",
            None,
            True,
        ),
        *[(label, path, None, False) for label, path in CANONICAL_REFERENCES],
    ]
    build_sheet(
        "portrait_bri_francois_debeauvais_source_candidate_canonical_blocked.png",
        "Event 006 — Francois Debeauvais source review — BLOCKED",
        "The rights-cleared 1928 face is too weak for identity-safe editing; sharper 1932/1933 candidates fail US-rights review",
        debeauvais_cards,
    )


if __name__ == "__main__":
    main()
