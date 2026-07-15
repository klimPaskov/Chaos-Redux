#!/usr/bin/env python3
"""Normalize Event 014 imagegen sources into 68x68 transparent idea icons.

Input files are already chroma-keyed to real alpha by the installed imagegen
helper. This script crops only transparent margin, fits each painted emblem to
the shared native-size safe area, adds a restrained one-pixel UI shadow, and
builds the review contact sheet. It does not draw or substitute source art.
"""

from __future__ import annotations

import argparse
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ICON_SIZE = 68
SUBJECT_BOX = 62
SHEET_COLUMNS = 4
SHEET_CELL_WIDTH = 300
SHEET_CELL_HEIGHT = 194

ASSETS = (
    "cannibalism_wendigo_conjoined_hunger",
    "cannibalism_wendigo_winter_feeding_network",
    "cannibalism_wendigo_locked_terminal_form",
    "cannibalism_liberated_feeding_states",
    "cannibalism_identification_and_burial_emergency",
    "cannibalism_broken_military_trust",
    "cannibalism_rebuilt_supply_discipline",
    "cannibalism_permanent_vigilance",
)


def checkerboard(size: tuple[int, int], tile: int = 8) -> Image.Image:
    image = Image.new("RGBA", size, (214, 214, 214, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if (x // tile + y // tile) % 2:
                draw.rectangle(
                    (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                    fill=(166, 166, 166, 255),
                )
    return image


def normalize(source: Path, destination: Path) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    alpha_bbox = image.getchannel("A").getbbox()
    if alpha_bbox is None:
        raise ValueError(f"No opaque pixels in {source}")

    subject = image.crop(alpha_bbox)
    scale = min(SUBJECT_BOX / subject.width, SUBJECT_BOX / subject.height)
    target = (
        max(1, round(subject.width * scale)),
        max(1, round(subject.height * scale)),
    )
    subject = subject.resize(target, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (ICON_SIZE, ICON_SIZE), (0, 0, 0, 0))
    x = (ICON_SIZE - subject.width) // 2
    y = (ICON_SIZE - subject.height) // 2 - 1

    shadow_alpha = subject.getchannel("A").filter(ImageFilter.GaussianBlur(0.65))
    shadow = Image.new("RGBA", subject.size, (0, 0, 0, 0))
    shadow.putalpha(shadow_alpha.point(lambda value: round(value * 0.48)))
    canvas.alpha_composite(shadow, (x + 1, y + 2))
    canvas.alpha_composite(subject, (x, y))
    canvas.putalpha(canvas.getchannel("A").point(lambda value: 0 if value < 4 else value))

    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)
    return canvas


def build_contact_sheet(processed_dir: Path, destination: Path) -> None:
    rows = (len(ASSETS) + SHEET_COLUMNS - 1) // SHEET_COLUMNS
    sheet = Image.new(
        "RGBA",
        (SHEET_COLUMNS * SHEET_CELL_WIDTH, rows * SHEET_CELL_HEIGHT),
        (30, 33, 36, 255),
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, asset in enumerate(ASSETS):
        column = index % SHEET_COLUMNS
        row = index // SHEET_COLUMNS
        left = column * SHEET_CELL_WIDTH
        top = row * SHEET_CELL_HEIGHT

        icon = Image.open(processed_dir / f"idea_{asset}.png").convert("RGBA")
        native = checkerboard((ICON_SIZE, ICON_SIZE), tile=6)
        native.alpha_composite(icon)
        enlarged = native.resize((136, 136), Image.Resampling.NEAREST)

        sheet.alpha_composite(native, (left + 8, top + 8))
        sheet.alpha_composite(enlarged, (left + 86, top + 8))

        label = asset.removeprefix("cannibalism_")
        label_lines = textwrap.wrap(label, width=42, break_long_words=True)
        draw.multiline_text(
            (left + 8, top + 148),
            "\n".join(label_lines[:2]),
            fill=(242, 242, 242, 255),
            font=font,
            spacing=1,
        )
        draw.text((left + 8, top + 176), "national spirit | 68x68 | native + 2x", fill=(182, 196, 207, 255), font=font)

    destination.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination, optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    transparent_dir = root / "key_removed_png"
    processed_dir = root / "processed_png"
    for asset in ASSETS:
        normalize(
            transparent_dir / f"{asset}_transparent.png",
            processed_dir / f"idea_{asset}.png",
        )

    build_contact_sheet(
        processed_dir,
        root / "contact_sheets" / "event014_idea_icon_repair_contact_sheet.png",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
