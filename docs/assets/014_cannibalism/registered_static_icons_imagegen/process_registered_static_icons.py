from __future__ import annotations

import csv
import hashlib
import math
import shutil
import struct
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "registered_static_icons_validation.tsv"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
LIVE_DECISIONS = ROOT / "gfx" / "interface" / "decisions" / "014_cannibalism"
LIVE_IDEAS = ROOT / "gfx" / "interface" / "ideas" / "014_cannibalism"


CATEGORY_ICON = ["decision_category_cannibalism_containment"]
CATEGORY_PANEL = ["cannibalism_containment_category_panel"]
DECISIONS = [
    "decision_cannibalism_ration_audit",
    "decision_cannibalism_restore_supply_corridor",
    "decision_cannibalism_supply_corridor_mission",
    "decision_cannibalism_rotate_formations",
    "decision_cannibalism_rotation_mission",
    "decision_cannibalism_forensic_recovery",
    "decision_cannibalism_search_burial_party",
    "decision_cannibalism_protect_burial_details",
    "decision_cannibalism_public_court_martial",
    "decision_cannibalism_conditional_amnesty",
    "decision_cannibalism_seal_transfer_records",
    "decision_cannibalism_terror_battalion",
]
IDEAS = [
    "idea_cannibalism_field_disappearances",
    "idea_cannibalism_emergency_logistics_command",
    "idea_cannibalism_formation_screening",
    "idea_cannibalism_terror_battalion",
    "idea_cannibalism_silent_garrison",
    "idea_cannibalism_hunting_ground",
    "idea_cannibalism_empty_village_reports",
    "idea_cannibalism_night_transfer_zone",
    "idea_cannibalism_public_truth",
    "idea_cannibalism_exploitation_scandal",
    "idea_cannibalism_council_obedience",
    "idea_cannibalism_ritual_hunger",
    "idea_cannibalism_closed_muster_rolls",
    "idea_cannibalism_archipelago_hunt",
    "idea_cannibalism_city_that_eats",
    "idea_cannibalism_moving_front",
]


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Imagegen source has no visible pixels after chroma-key removal")
    return rgba.crop(bbox)


def fit_alpha(
    source: Path,
    size: tuple[int, int],
    padding: int,
    outline_width: float,
    shadow_offset: float,
) -> Image.Image:
    scale = 4
    target_w, target_h = size
    image = trim_alpha(Image.open(source))
    maximum = (
        max(1, (target_w - padding * 2 - math.ceil(outline_width * 2)) * scale),
        max(1, (target_h - padding * 2 - math.ceil(outline_width * 2)) * scale),
    )
    ratio = min(maximum[0] / image.width, maximum[1] / image.height)
    resized = image.resize(
        (max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    high_size = (target_w * scale, target_h * scale)
    x = (high_size[0] - resized.width) // 2
    y = (high_size[1] - resized.height) // 2
    subject_alpha = Image.new("L", high_size, 0)
    subject_alpha.paste(resized.getchannel("A"), (x, y))

    shadow_alpha = subject_alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale))
    shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.42))
    shifted_shadow = Image.new("L", high_size, 0)
    shifted_shadow.paste(
        shadow_alpha,
        (round(shadow_offset * scale), round(shadow_offset * scale)),
    )
    shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
    shadow.putalpha(shifted_shadow)

    outline_pixels = max(1, round(outline_width * scale))
    outline_alpha = subject_alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1))
    outline_alpha = outline_alpha.point(lambda value: round(value * 0.9))
    outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
    outline.putalpha(outline_alpha)

    subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
    subject.alpha_composite(resized, (x, y))
    canvas = Image.alpha_composite(shadow, outline)
    canvas = Image.alpha_composite(canvas, subject)
    return canvas.resize(size, Image.Resampling.LANCZOS)


def cover_opaque(source: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(source).convert("RGB")
    return ImageOps.fit(
        image,
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    ).convert("RGBA")


def convert_to_dds(png: Path, package_dds: Path, live_dds: Path, size: tuple[int, int]) -> None:
    package_dds.parent.mkdir(parents=True, exist_ok=True)
    live_dds.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "python",
            str(CONVERTER),
            "--input",
            str(png),
            "--output",
            str(package_dds),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        check=True,
    )
    shutil.copy2(package_dds, live_dds)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
    data = path.read_bytes()[:128]
    if len(data) != 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS magic/header: {path}")
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mip_count = struct.unpack_from("<I", data, 28)[0]
    masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
    return width, height, mip_count, masks


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    image = Image.new("RGBA", size, (67, 67, 67, 255))
    draw = ImageDraw.Draw(image)
    colors = ((72, 72, 72, 255), (116, 116, 116, 255))
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            draw.rectangle(
                (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                fill=colors[((x // tile) + (y // tile)) % 2],
            )
    return image


def font(size: int) -> ImageFont.ImageFont:
    for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def make_contact(
    entries: list[tuple[str, Image.Image]],
    output: Path,
    columns: int = 5,
    source_mode: bool = False,
) -> None:
    cell_w, cell_h = 250, 205
    preview_size = (144, 144)
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    for index, (name, image) in enumerate(entries):
        col, row = index % columns, index // columns
        x0, y0 = col * cell_w, row * cell_h
        draw.rectangle((x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4), outline=(88, 92, 98), width=1)
        if source_mode:
            preview = ImageOps.contain(image.convert("RGB"), preview_size, Image.Resampling.LANCZOS)
            plate = Image.new("RGB", preview_size, (48, 50, 54))
            plate.paste(preview, ((preview_size[0] - preview.width) // 2, (preview_size[1] - preview.height) // 2))
        else:
            scaled = ImageOps.contain(image.convert("RGBA"), preview_size, Image.Resampling.NEAREST)
            plate = checker(preview_size, 12)
            plate.alpha_composite(scaled, ((preview_size[0] - scaled.width) // 2, (preview_size[1] - scaled.height) // 2))
            plate = plate.convert("RGB")
        sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 10))
        lines = textwrap.wrap(name, width=30)[:3]
        ly = y0 + 160
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=label_font)
            draw.text((x0 + (cell_w - (bbox[2] - bbox[0])) // 2, ly), line, font=label_font, fill=(235, 235, 235))
            ly += 15
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, optimize=True)


def visible_key_green(image: Image.Image) -> int:
    rgba = image.convert("RGBA")
    return sum(
        1
        for red, green, blue, alpha in rgba.getdata()
        if alpha > 10 and green > 190 and green > red * 1.55 and green > blue * 1.55
    )


def main() -> None:
    for directory in (PROCESSED, DDS_PACKAGE, CONTACT, LIVE_DECISIONS, LIVE_IDEAS, VALIDATION.parent):
        directory.mkdir(parents=True, exist_ok=True)

    processed: dict[str, Image.Image] = {}
    metadata: dict[str, tuple[str, tuple[int, int], Path]] = {}

    for name in CATEGORY_ICON + DECISIONS:
        alpha_source = ALPHA / f"{name}_alpha.png"
        if not alpha_source.exists():
            raise FileNotFoundError(alpha_source)
        image = fit_alpha(alpha_source, (32, 32), 2, 0.85, 0.75)
        processed[name] = image
        metadata[name] = ("decision/category icon", (32, 32), LIVE_DECISIONS / f"{name}.dds")

    for name in IDEAS:
        alpha_source = ALPHA / f"{name}_alpha.png"
        if not alpha_source.exists():
            raise FileNotFoundError(alpha_source)
        image = fit_alpha(alpha_source, (64, 64), 3, 1.0, 1.0)
        processed[name] = image
        metadata[name] = ("idea/state-spirit icon", (64, 64), LIVE_IDEAS / f"{name}.dds")

    panel_name = CATEGORY_PANEL[0]
    panel_source = SOURCE / f"{panel_name}_source.png"
    if not panel_source.exists():
        raise FileNotFoundError(panel_source)
    processed[panel_name] = cover_opaque(panel_source, (114, 101))
    metadata[panel_name] = ("decision category picture", (114, 101), LIVE_DECISIONS / f"{panel_name}.dds")

    for name, image in processed.items():
        png = PROCESSED / f"{name}.png"
        image.save(png, optimize=True)
        _, size, live_dds = metadata[name]
        convert_to_dds(png, DDS_PACKAGE / f"{name}.dds", live_dds, size)

    source_entries = [
        (name, Image.open(SOURCE / f"{name}_source.png").convert("RGBA"))
        for name in CATEGORY_ICON + CATEGORY_PANEL + DECISIONS + IDEAS
    ]
    ordered_names = CATEGORY_ICON + CATEGORY_PANEL + DECISIONS + IDEAS
    processed_entries = [(name, processed[name]) for name in ordered_names]
    dds_entries = [(name, Image.open(metadata[name][2]).convert("RGBA")) for name in ordered_names]
    make_contact(source_entries, CONTACT / "registered_sources_contact_sheet.png", source_mode=True)
    make_contact(processed_entries, CONTACT / "registered_processed_checker_contact_sheet.png")
    make_contact(dds_entries, CONTACT / "registered_dds_decoded_contact_sheet.png")
    make_contact(
        [(name, processed[name]) for name in CATEGORY_ICON + CATEGORY_PANEL + DECISIONS],
        CONTACT / "registered_category_decision_processed_checker_contact_sheet.png",
        columns=4,
    )
    make_contact(
        [(name, processed[name]) for name in IDEAS],
        CONTACT / "registered_idea_processed_checker_contact_sheet.png",
        columns=4,
    )

    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    hashes: dict[str, str] = {}
    rows: list[list[str]] = []
    for name in ordered_names:
        asset_type, expected_size, live_dds = metadata[name]
        png = PROCESSED / f"{name}.png"
        image = Image.open(png).convert("RGBA")
        if image.size != expected_size:
            raise RuntimeError(f"Wrong processed size for {name}: {image.size}, expected {expected_size}")
        alpha = image.getchannel("A")
        alpha_min, alpha_max = alpha.getextrema()
        transparent = sum(1 for value in alpha.getdata() if value == 0)
        partial = sum(1 for value in alpha.getdata() if 0 < value < 255)
        corner_alpha = tuple(
            alpha.getpixel(point)
            for point in ((0, 0), (expected_size[0] - 1, 0), (0, expected_size[1] - 1), (expected_size[0] - 1, expected_size[1] - 1))
        )
        if asset_type != "decision category picture" and alpha_min != 0:
            raise RuntimeError(f"Transparent icon lost transparent pixels: {name}")
        if asset_type != "decision category picture" and corner_alpha != (0, 0, 0, 0):
            raise RuntimeError(f"Transparent icon has non-transparent corners: {name} {corner_alpha}")
        if asset_type == "decision category picture" and (alpha_min, alpha_max) != (255, 255):
            raise RuntimeError(f"Category picture should remain opaque: {name}")
        key_green = visible_key_green(image)
        if key_green:
            raise RuntimeError(f"Visible chroma-key green remains in {name}: {key_green} pixels")
        digest = hashlib.sha256(image.tobytes()).hexdigest()
        if digest in hashes:
            raise RuntimeError(f"Duplicate normalized artwork: {name} duplicates {hashes[digest]}")
        hashes[digest] = name

        width, height, mip_count, masks = dds_header(live_dds)
        if (width, height) != expected_size:
            raise RuntimeError(f"Wrong DDS size for {name}: {(width, height)}, expected {expected_size}")
        if mip_count not in (0, 1):
            raise RuntimeError(f"DDS should have one mip: {name} reports {mip_count}")
        if masks != expected_masks:
            raise RuntimeError(f"DDS is not BGRA8 for {name}: {masks}")
        rows.append(
            [
                name,
                asset_type,
                f"{expected_size[0]}x{expected_size[1]}",
                str(alpha_min),
                str(alpha_max),
                str(transparent),
                str(partial),
                "/".join(str(value) for value in corner_alpha),
                str(key_green),
                digest,
                "0x00ff0000/0x0000ff00/0x000000ff/0xff000000",
                "complete",
            ]
        )

    with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "asset",
                "asset_type",
                "dimensions",
                "alpha_min",
                "alpha_max",
                "transparent_pixels",
                "partial_alpha_pixels",
                "corner_alpha_tl_tr_bl_br",
                "visible_key_green_pixels",
                "processed_rgba_sha256",
                "dds_channel_masks",
                "status",
            ]
        )
        writer.writerows(rows)

    print(f"processed and validated {len(ordered_names)} registered Event 014 static assets")


if __name__ == "__main__":
    main()
