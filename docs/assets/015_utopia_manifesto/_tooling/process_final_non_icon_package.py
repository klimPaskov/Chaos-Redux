#!/usr/bin/env python3
"""Build the final fictional non-icon package for Event 015.

The script performs deterministic local crop, grade, alpha extraction, UI slicing,
HOI4 DDS/TGA export, decode verification, hash recording, and contact-sheet
assembly.  Its source inputs are distinct image_gen masters recorded in
generated_event_art_final_prompts.md.  It does not generate substitute artwork.
"""

from __future__ import annotations

import hashlib
import json
import math
import shutil
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


REPO = Path(__file__).resolve().parents[4]
BASE = REPO / "docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14"
SOURCE = BASE / "source_png"
PROCESSED = BASE / "processed_png"
DDS = BASE / "dds"
TGA = BASE / "tga/flags"
DECODED = BASE / "decoded_png"
CONTACT = BASE / "contact_sheets"
CONVERTER = REPO / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
REPORT_PROCESSOR = REPO / ".agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py"

REPORTS = [
    "report_event_utopia_manifesto_found",
    "report_event_utopia_manifesto_ledger",
    "report_event_utopia_manifesto_calling",
    "report_event_utopia_manifesto_store",
    "report_event_utopia_manifesto_settlement",
    "report_event_utopia_manifesto_island",
    "report_event_utopia_manifesto_defense",
    "report_event_utopia_manifesto_foreign_commonwealth",
    "report_event_utopia_manifesto_necessary_ground",
    "report_event_utopia_manifesto_stewardship",
    "report_event_utopia_manifesto_league",
    "report_event_utopia_manifesto_formation",
    "report_event_utopia_manifesto_contradiction",
    "report_event_utopia_manifesto_evolution",
]

NEWS = [
    "news_event_utopia_manifesto_league",
    "news_event_utopia_manifesto_necessary_ground_war",
    "news_event_utopia_manifesto_colony_revolt",
]

SUPERS = [
    "super_event_015_consent_of_households",
    "super_event_015_common_table",
    "super_event_015_guardians_of_measure",
    "super_event_015_closed_island",
    "super_event_015_joke_understood",
]

FLAGS = [
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH",
    "UTOPIA_MANIFESTO_COUNCIL_UNION",
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA",
    "UTOPIA_MANIFESTO_CLOSED_ISLAND",
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH",
]

EMBLEMS = [
    "household_congress_emblem",
    "congress_of_common_tables_emblem",
    "network_directorate_emblem",
    "island_hierarchy_emblem",
    "plural_compact_emblem",
]

PORTRAITS = [
    "leader_household_assembly",
    "leader_council_of_callings",
    "leader_board_of_measure",
    "leader_stewardship_council",
]

FORMATIONS = [
    "formation_ready_voluntary_commonwealth",
    "formation_ready_council_union",
    "formation_ready_planned_utopia",
    "formation_ready_closed_island",
    "formation_ready_practical_commonwealth",
]

LEDGER_STATES = {
    "utopia_ledger_tab_normal": ((154, 44), (48, 69, 68), (180, 157, 102)),
    "utopia_ledger_tab_selected": ((154, 44), (64, 88, 82), (229, 199, 119)),
    "utopia_ledger_tab_locked": ((154, 44), (42, 43, 41), (108, 104, 91)),
    "utopia_ledger_case_normal": ((240, 96), (48, 67, 64), (176, 151, 103)),
    "utopia_ledger_case_selected": ((240, 96), (62, 84, 76), (229, 196, 116)),
    "utopia_ledger_case_warning": ((240, 96), (94, 62, 38), (222, 150, 76)),
    "utopia_ledger_case_crisis": ((240, 96), (91, 38, 35), (223, 101, 81)),
    "utopia_ledger_district_normal": ((240, 96), (43, 64, 68), (155, 150, 111)),
    "utopia_ledger_district_selected": ((240, 96), (53, 81, 84), (207, 193, 126)),
    "utopia_ledger_district_locked": ((240, 96), (40, 43, 44), (104, 107, 103)),
    "utopia_ledger_district_warning": ((240, 96), (93, 65, 36), (218, 154, 77)),
    "utopia_ledger_formation_locked": ((240, 96), (43, 43, 47), (112, 108, 103)),
    "utopia_ledger_formation_available": ((240, 96), (50, 68, 78), (186, 172, 112)),
    "utopia_ledger_formation_ready": ((240, 96), (39, 82, 68), (227, 197, 110)),
}

REPORT_ANGLES = [-2.3, 1.8, -1.2, 2.5, -2.0, 1.4, -2.7, 2.0, -1.6, 2.6, -1.0, 1.7, -2.1, 1.1]


def ensure_dirs() -> None:
    for path in (PROCESSED, DDS, TGA, DECODED, CONTACT):
        path.mkdir(parents=True, exist_ok=True)
    for family in ("reports", "news", "super_events", "ledger", "league_emblems", "portraits", "formation"):
        (PROCESSED / family).mkdir(parents=True, exist_ok=True)
        (DDS / family).mkdir(parents=True, exist_ok=True)
    (PROCESSED / "flags").mkdir(parents=True, exist_ok=True)
    (TGA / "medium").mkdir(parents=True, exist_ok=True)
    (TGA / "small").mkdir(parents=True, exist_ok=True)


def require(path: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def cover(im: Image.Image, size: tuple[int, int], focal: tuple[float, float] = (0.5, 0.5)) -> Image.Image:
    im = ImageOps.exif_transpose(im).convert("RGBA")
    target_ratio = size[0] / size[1]
    source_ratio = im.width / im.height
    if source_ratio > target_ratio:
        crop_w = round(im.height * target_ratio)
        max_left = im.width - crop_w
        left = round(max_left * focal[0])
        box = (left, 0, left + crop_w, im.height)
    else:
        crop_h = round(im.width / target_ratio)
        max_top = im.height - crop_h
        top = round(max_top * focal[1])
        box = (0, top, im.width, top + crop_h)
    return im.crop(box).resize(size, Image.Resampling.LANCZOS)


def sepia(im: Image.Image) -> Image.Image:
    gray = ImageOps.grayscale(im.convert("RGB"))
    gray = ImageEnhance.Contrast(gray).enhance(1.10)
    return ImageOps.colorize(gray, black=(29, 24, 20), white=(218, 198, 158)).convert("RGBA")


def vignette(im: Image.Image, strength: int = 62) -> Image.Image:
    im = im.convert("RGBA")
    w, h = im.size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    inset = max(1, min(w, h) // 7)
    draw.ellipse((-inset, -inset, w + inset, h + inset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(max(8, min(w, h) // 6)))
    darkness = Image.new("RGBA", (w, h), (5, 8, 8, strength))
    alpha = ImageOps.invert(mask).point(lambda p: p * strength // 255)
    darkness.putalpha(alpha)
    return Image.alpha_composite(im, darkness)


def process_report(source: Path, output: Path, angle: float) -> None:
    photo = cover(Image.open(source), (180, 140), (0.5, 0.47))
    photo = sepia(photo)
    photo = ImageEnhance.Sharpness(photo).enhance(1.22)
    card = Image.new("RGBA", (190, 150), (212, 194, 154, 255))
    card.paste(photo, (5, 5), photo)
    draw = ImageDraw.Draw(card)
    draw.rectangle((2, 2, 187, 147), outline=(91, 73, 49, 255), width=1)
    rotated = card.rotate(angle, Image.Resampling.BICUBIC, expand=True)
    shadow = Image.new("RGBA", rotated.size, (0, 0, 0, 0))
    shadow.putalpha(rotated.getchannel("A").filter(ImageFilter.GaussianBlur(3)))
    shadow_color = Image.new("RGBA", rotated.size, (14, 11, 9, 105))
    shadow_color.putalpha(shadow.getchannel("A").point(lambda p: p * 105 // 255))
    canvas = Image.new("RGBA", (210, 176), (0, 0, 0, 0))
    x = (210 - rotated.width) // 2
    y = (176 - rotated.height) // 2
    canvas.alpha_composite(shadow_color, (x + 3, y + 4))
    canvas.alpha_composite(rotated, (x, y))
    canvas.save(output)


def process_news(source: Path, output: Path) -> None:
    im = cover(Image.open(source), (397, 153), (0.5, 0.5)).convert("RGB")
    gray = ImageOps.grayscale(im)
    gray = ImageEnhance.Contrast(gray).enhance(1.18)
    gray = ImageEnhance.Sharpness(gray).enhance(1.18)
    gray.convert("RGBA").save(output)


def process_super(source: Path, output: Path) -> None:
    im = cover(Image.open(source), (457, 328), (0.5, 0.5)).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.72)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = ImageEnhance.Sharpness(im).enhance(1.14)
    vignette(im.convert("RGBA"), 54).save(output)


def process_portrait(source: Path, output: Path) -> None:
    im = cover(Image.open(source), (156, 210), (0.5, 0.46)).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.76)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Sharpness(im).enhance(1.12)
    vignette(im.convert("RGBA"), 48).save(output)


def remove_green(source: Path) -> Image.Image:
    im = ImageOps.exif_transpose(Image.open(source)).convert("RGBA")
    pixels = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, _ = pixels[x, y]
            dominance = g - max(r, b)
            distance = math.sqrt((r - 0) ** 2 + (g - 255) ** 2 + (b - 0) ** 2)
            if dominance > 70 and g > 120:
                alpha = 0
            elif dominance > 28 and g > 95:
                alpha = max(0, min(255, round((70 - dominance) * 255 / 42)))
            elif distance < 155:
                alpha = max(0, min(255, round((distance - 45) * 255 / 110)))
            else:
                alpha = 255
            if alpha < 255:
                # Suppress green fringe in partially transparent edge pixels.
                g = min(g, max(r, b) + 16)
            pixels[x, y] = (r, g, b, alpha)
    return im


def fit_transparent(im: Image.Image, size: tuple[int, int], margin: int) -> Image.Image:
    bbox = im.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("transparent extraction produced no subject")
    subject = im.crop(bbox)
    max_size = (size[0] - margin * 2, size[1] - margin * 2)
    subject.thumbnail(max_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    canvas.alpha_composite(subject, ((size[0] - subject.width) // 2, (size[1] - subject.height) // 2))
    return canvas


def process_emblem(source: Path, output: Path, size: tuple[int, int]) -> None:
    im = remove_green(source)
    fit_transparent(im, size, 3 if size[0] <= 64 else 5).save(output)


def process_flag(source: Path, output: Path) -> None:
    im = cover(Image.open(source), (820, 520), (0.5, 0.5)).convert("RGB")
    im = ImageEnhance.Color(im).enhance(1.02)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im.resize((82, 52), Image.Resampling.LANCZOS).save(output)


def ledger_grade(source: Image.Image, size: tuple[int, int], tint: tuple[int, int, int], border: tuple[int, int, int]) -> Image.Image:
    im = cover(source, size, (0.5, 0.54)).convert("RGBA")
    overlay = Image.new("RGBA", size, (*tint, 108))
    im = Image.alpha_composite(im, overlay)
    im = ImageEnhance.Contrast(im).enhance(0.94)
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle((1, 1, size[0] - 2, size[1] - 2), radius=max(4, min(size) // 8), outline=(*border, 255), width=2)
    draw.rounded_rectangle((5, 5, size[0] - 6, size[1] - 6), radius=max(2, min(size) // 10), outline=(*border, 150), width=1)
    return im


def process_ledger(source_path: Path) -> list[str]:
    source = Image.open(source_path).convert("RGBA")
    names: list[str] = []
    background = cover(source, (700, 500), (0.5, 0.52))
    background = ImageEnhance.Color(background).enhance(0.78)
    background = ImageEnhance.Contrast(background).enhance(0.96)
    background = vignette(background, 46)
    background.save(PROCESSED / "ledger/utopia_ledger_background_panel.png")
    names.append("utopia_ledger_background_panel")

    header = cover(source, (700, 96), (0.5, 0.18))
    header = ImageEnhance.Color(header).enhance(0.80)
    header = ImageEnhance.Contrast(header).enhance(1.02)
    ImageDraw.Draw(header).line((0, 94, 699, 94), fill=(212, 178, 99, 255), width=2)
    header.save(PROCESSED / "ledger/utopia_ledger_header_plate.png")
    names.append("utopia_ledger_header_plate")

    warning = ledger_grade(source, (320, 128), (91, 39, 31), (224, 127, 78))
    warning.save(PROCESSED / "ledger/utopia_ledger_warning_panel.png")
    names.append("utopia_ledger_warning_panel")

    for name, (size, tint, border) in LEDGER_STATES.items():
        ledger_grade(source, size, tint, border).save(PROCESSED / f"ledger/{name}.png")
        names.append(name)
    return names


def convert_dds(source: Path, package_output: Path, runtime_output: Path) -> None:
    package_output.parent.mkdir(parents=True, exist_ok=True)
    runtime_output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, str(CONVERTER), "--input", str(source), "--output", str(package_output)],
        cwd=REPO,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    shutil.copy2(package_output, runtime_output)


def write_tga_bottom_left(im: Image.Image, path: Path) -> None:
    """Write uncompressed 32-bit BGRA TGA with a bottom-left origin."""
    im = im.convert("RGBA")
    w, h = im.size
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, w, h, 32, 8)
    rgba = im.tobytes()
    row_bytes = w * 4
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        handle.write(header)
        for y in range(h - 1, -1, -1):
            row = rgba[y * row_bytes : (y + 1) * row_bytes]
            bgra = bytearray(row_bytes)
            for i in range(0, row_bytes, 4):
                r, g, b, a = row[i : i + 4]
                bgra[i : i + 4] = bytes((b, g, r, a))
            handle.write(bgra)


def validate_tga(path: Path, expected: tuple[int, int]) -> None:
    data = path.read_bytes()
    if len(data) < 18:
        raise ValueError(f"short TGA: {path}")
    image_type = data[2]
    width = int.from_bytes(data[12:14], "little")
    height = int.from_bytes(data[14:16], "little")
    depth = data[16]
    descriptor = data[17]
    expected_length = 18 + width * height * 4
    if (image_type, width, height, depth, descriptor & 0x20, len(data)) != (2, expected[0], expected[1], 32, 0, expected_length):
        raise ValueError(f"invalid TGA contract: {path}")


def validate_dds(path: Path, expected: tuple[int, int]) -> None:
    data = path.read_bytes()
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError(f"invalid DDS header: {path}")
    header_size = int.from_bytes(data[4:8], "little")
    height = int.from_bytes(data[12:16], "little")
    width = int.from_bytes(data[16:20], "little")
    mipmaps = int.from_bytes(data[28:32], "little")
    pixel_format_size = int.from_bytes(data[76:80], "little")
    pixel_format_flags = int.from_bytes(data[80:84], "little")
    fourcc = data[84:88]
    rgb_bits = int.from_bytes(data[88:92], "little")
    red_mask = int.from_bytes(data[92:96], "little")
    green_mask = int.from_bytes(data[96:100], "little")
    blue_mask = int.from_bytes(data[100:104], "little")
    alpha_mask = int.from_bytes(data[104:108], "little")
    caps = int.from_bytes(data[108:112], "little")
    expected_length = 128 + width * height * 4
    contract = (
        header_size == 124
        and (width, height) == expected
        and mipmaps in (0, 1)
        and pixel_format_size == 32
        and pixel_format_flags == 65
        and fourcc == b"\x00\x00\x00\x00"
        and rgb_bits == 32
        and red_mask == 0x00FF0000
        and green_mask == 0x0000FF00
        and blue_mask == 0x000000FF
        and alpha_mask == 0xFF000000
        and caps == 0x1000
        and len(data) == expected_length
    )
    if not contract:
        raise ValueError(f"invalid uncompressed one-level DDS contract: {path}")


def validate_alpha(path: Path, expected: tuple[int, int]) -> None:
    with Image.open(path) as im:
        alpha_range = im.convert("RGBA").getchannel("A").getextrema()
    if alpha_range != expected:
        raise ValueError(f"unexpected alpha range {alpha_range}, expected {expected}: {path}")


def decode_dds(path: Path, output: Path) -> None:
    with Image.open(path) as im:
        im.convert("RGBA").save(output)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dimensions(path: Path) -> list[int]:
    with Image.open(path) as im:
        return [im.width, im.height]


def make_contact_sheet(items: list[tuple[str, Path]], output: Path, columns: int, cell: tuple[int, int]) -> None:
    font = ImageFont.load_default()
    label_h = 32
    rows = math.ceil(len(items) / columns)
    sheet = Image.new("RGBA", (columns * cell[0], rows * (cell[1] + label_h)), (36, 37, 38, 255))
    draw = ImageDraw.Draw(sheet)
    for index, (label, path) in enumerate(items):
        x = (index % columns) * cell[0]
        y = (index // columns) * (cell[1] + label_h)
        with Image.open(path) as raw:
            preview = raw.convert("RGBA")
        checker = Image.new("RGBA", cell, (66, 67, 68, 255))
        cd = ImageDraw.Draw(checker)
        block = 12
        for cy in range(0, cell[1], block):
            for cx in range(0, cell[0], block):
                if (cx // block + cy // block) % 2:
                    cd.rectangle((cx, cy, cx + block - 1, cy + block - 1), fill=(87, 88, 89, 255))
        preview.thumbnail((cell[0] - 10, cell[1] - 10), Image.Resampling.LANCZOS)
        checker.alpha_composite(preview, ((cell[0] - preview.width) // 2, (cell[1] - preview.height) // 2))
        sheet.alpha_composite(checker, (x, y))
        short = label if len(label) <= 34 else label[:31] + "..."
        draw.text((x + 5, y + cell[1] + 6), short, fill=(238, 232, 216, 255), font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(output)


def record(kind: str, stem: str, source: Path, processed: Path, final: Path) -> dict[str, object]:
    return {
        "kind": kind,
        "stem": stem,
        "source": str(source.relative_to(REPO)).replace("\\", "/"),
        "source_dimensions": dimensions(source),
        "source_sha256": sha256(source),
        "processed": str(processed.relative_to(REPO)).replace("\\", "/"),
        "processed_dimensions": dimensions(processed),
        "processed_sha256": sha256(processed),
        "final": str(final.relative_to(REPO)).replace("\\", "/"),
        "final_dimensions": dimensions(final),
        "final_sha256": sha256(final),
        "provenance": "OpenAI image_gen original; deterministic local crop/grade/export",
        "license": "Original generated fictional asset; no third-party source or character reference",
    }


def main() -> None:
    ensure_dirs()
    records: list[dict[str, object]] = []

    for index, stem in enumerate(REPORTS):
        src = require(SOURCE / f"reports/{stem}_source.png")
        processed = PROCESSED / f"reports/{stem}.png"
        package = DDS / f"reports/{stem}.dds"
        runtime = REPO / f"gfx/event_pictures/015_utopia_manifesto/{stem}.dds"
        subprocess.run(
            [
                sys.executable,
                str(REPORT_PROCESSOR),
                str(src),
                str(processed),
                "--angle",
                str(REPORT_ANGLES[index]),
                "--seed",
                str(1500 + index),
            ],
            cwd=REPO,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (210, 176))
        validate_alpha(runtime, (0, 255))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("report", stem, src, processed, runtime))

    for stem in NEWS:
        src = require(SOURCE / f"news/{stem}_source.png")
        processed = PROCESSED / f"news/{stem}.png"
        package = DDS / f"news/{stem}.dds"
        runtime = REPO / f"gfx/event_pictures/015_utopia_manifesto/{stem}.dds"
        process_news(src, processed)
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (397, 153))
        validate_alpha(runtime, (255, 255))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("news", stem, src, processed, runtime))

    for stem in SUPERS:
        src = require(SOURCE / f"super_events/{stem}_source.png")
        processed = PROCESSED / f"super_events/{stem}.png"
        package = DDS / f"super_events/{stem}.dds"
        runtime = REPO / f"gfx/super_events/015_utopia_manifesto/{stem}.dds"
        process_super(src, processed)
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (457, 328))
        validate_alpha(runtime, (255, 255))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("super_event", stem, src, processed, runtime))

    (BASE / "asset_records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")

    report_labels = [(s.removeprefix("report_event_utopia_manifesto_"), PROCESSED / f"reports/{s}.png") for s in REPORTS]
    news_labels = [(s.removeprefix("news_event_utopia_manifesto_"), PROCESSED / f"news/{s}.png") for s in NEWS]
    super_labels = [(s.removeprefix("super_event_015_"), PROCESSED / f"super_events/{s}.png") for s in SUPERS]
    make_contact_sheet(report_labels, CONTACT / "event_015_report_finals.png", 4, (230, 190))
    make_contact_sheet(news_labels, CONTACT / "event_015_news_finals.png", 1, (420, 170))
    make_contact_sheet(super_labels, CONTACT / "event_015_super_event_finals.png", 3, (330, 250))
    make_contact_sheet(
        [(s.removeprefix("report_event_utopia_manifesto_"), SOURCE / f"reports/{s}_source.png") for s in REPORTS],
        CONTACT / "event_015_report_source_masters.png",
        4,
        (280, 190),
    )
    make_contact_sheet(
        [(s.removeprefix("news_event_utopia_manifesto_"), SOURCE / f"news/{s}_source.png") for s in NEWS],
        CONTACT / "event_015_news_source_masters.png",
        1,
        (440, 190),
    )
    make_contact_sheet(
        [(s.removeprefix("super_event_015_"), SOURCE / f"super_events/{s}_source.png") for s in SUPERS],
        CONTACT / "event_015_super_event_source_masters.png",
        3,
        (350, 250),
    )
    rejected = sorted((SOURCE / "rejected_initial").glob("*.png"))
    if rejected:
        make_contact_sheet(
            [(p.stem.removeprefix("report_event_utopia_manifesto_").removesuffix("_source"), p) for p in rejected],
            CONTACT / "event_015_rejected_report_sources.png",
            3,
            (280, 190),
        )

    # No two finals within a primary event-art family may be byte-identical.
    for family in (REPORTS, NEWS, SUPERS):
        hashes = [next(row for row in records if row["stem"] == stem)["final_sha256"] for stem in family]
        if len(hashes) != len(set(hashes)):
            raise ValueError(f"duplicate final detected in family: {family}")

    print(f"built {len(records)} final event-art records")
    return

    ledger_source = require(SOURCE / "ledger/utopia_ledger_final_master_source.png")
    for stem in process_ledger(ledger_source):
        processed = PROCESSED / f"ledger/{stem}.png"
        package = DDS / f"ledger/{stem}.dds"
        runtime = REPO / f"gfx/interface/015_utopia_manifesto/{stem}.dds"
        convert_dds(processed, package, runtime)
        expected = dimensions(processed)
        validate_dds(runtime, (expected[0], expected[1]))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("ledger", stem, ledger_source, processed, runtime))

    for stem in FLAGS:
        src = require(SOURCE / f"flags/{stem}_source.png")
        processed = PROCESSED / f"flags/{stem}.png"
        process_flag(src, processed)
        full = TGA / f"{stem}.tga"
        medium = TGA / f"medium/{stem}.tga"
        small = TGA / f"small/{stem}.tga"
        with Image.open(processed) as base_flag:
            full_im = base_flag.convert("RGBA")
            medium_im = full_im.resize((41, 26), Image.Resampling.LANCZOS)
            small_im = full_im.resize((10, 7), Image.Resampling.LANCZOS)
        write_tga_bottom_left(full_im, full)
        write_tga_bottom_left(medium_im, medium)
        write_tga_bottom_left(small_im, small)
        for path, expected in ((full, (82, 52)), (medium, (41, 26)), (small, (10, 7))):
            validate_tga(path, expected)
        runtime = REPO / f"gfx/flags/{stem}.tga"
        runtime_medium = REPO / f"gfx/flags/medium/{stem}.tga"
        runtime_small = REPO / f"gfx/flags/small/{stem}.tga"
        runtime.parent.mkdir(parents=True, exist_ok=True)
        runtime_medium.parent.mkdir(parents=True, exist_ok=True)
        runtime_small.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(full, runtime)
        shutil.copy2(medium, runtime_medium)
        shutil.copy2(small, runtime_small)
        records.append({
            "kind": "flag_triplet",
            "stem": stem,
            "source": str(src.relative_to(REPO)).replace("\\", "/"),
            "source_dimensions": dimensions(src),
            "source_sha256": sha256(src),
            "processed": str(processed.relative_to(REPO)).replace("\\", "/"),
            "processed_dimensions": dimensions(processed),
            "processed_sha256": sha256(processed),
            "final": str(runtime.relative_to(REPO)).replace("\\", "/"),
            "final_dimensions": [82, 52],
            "final_sha256": sha256(runtime),
            "medium": str(runtime_medium.relative_to(REPO)).replace("\\", "/"),
            "medium_sha256": sha256(runtime_medium),
            "small": str(runtime_small.relative_to(REPO)).replace("\\", "/"),
            "small_sha256": sha256(runtime_small),
            "provenance": "OpenAI image_gen original; deterministic local crop/export",
            "license": "Original generated fictional asset; no third-party source or character reference",
        })

    for stem in EMBLEMS:
        src = require(SOURCE / f"league_emblems/{stem}_source.png")
        processed = PROCESSED / f"league_emblems/{stem}.png"
        package = DDS / f"league_emblems/{stem}.dds"
        runtime = REPO / f"gfx/interface/015_utopia_manifesto/league_emblems/{stem}.dds"
        process_emblem(src, processed, (64, 64))
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (64, 64))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("league_emblem", stem, src, processed, runtime))

    for stem in PORTRAITS:
        src = require(SOURCE / f"portraits/{stem}_source.png")
        processed = PROCESSED / f"portraits/{stem}.png"
        package = DDS / f"portraits/{stem}.dds"
        runtime = REPO / f"gfx/leaders/015_utopia_manifesto/{stem}.dds"
        process_portrait(src, processed)
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (156, 210))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("portrait", stem, src, processed, runtime))

    for stem in FORMATIONS:
        src = require(SOURCE / f"formation/{stem}_source.png")
        processed = PROCESSED / f"formation/{stem}.png"
        package = DDS / f"formation/{stem}.dds"
        runtime = REPO / f"gfx/interface/015_utopia_manifesto/formation/{stem}.dds"
        process_emblem(src, processed, (96, 96))
        convert_dds(processed, package, runtime)
        validate_dds(runtime, (96, 96))
        decode_dds(runtime, DECODED / f"{stem}.png")
        records.append(record("formation_seal", stem, src, processed, runtime))

    (BASE / "asset_records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")

    make_contact_sheet([(s, PROCESSED / f"reports/{s}.png") for s in REPORTS], CONTACT / "event_015_report_finals.png", 4, (230, 190))
    make_contact_sheet([(s, PROCESSED / f"news/{s}.png") for s in NEWS], CONTACT / "event_015_news_finals.png", 1, (420, 170))
    make_contact_sheet([(s, PROCESSED / f"super_events/{s}.png") for s in SUPERS], CONTACT / "event_015_super_event_finals.png", 3, (330, 250))
    make_contact_sheet([(s, PROCESSED / f"flags/{s}.png") for s in FLAGS], CONTACT / "event_015_route_flag_finals.png", 2, (260, 170))
    make_contact_sheet([(s, PROCESSED / f"league_emblems/{s}.png") for s in EMBLEMS], CONTACT / "event_015_league_emblem_finals.png", 5, (120, 120))
    make_contact_sheet([(s, PROCESSED / f"portraits/{s}.png") for s in PORTRAITS], CONTACT / "event_015_institutional_portrait_finals.png", 4, (180, 230))
    make_contact_sheet([(s, PROCESSED / f"formation/{s}.png") for s in FORMATIONS], CONTACT / "event_015_formation_seal_finals.png", 5, (130, 130))
    ledger_names = ["utopia_ledger_background_panel", "utopia_ledger_header_plate", "utopia_ledger_warning_panel", *LEDGER_STATES.keys()]
    make_contact_sheet([(s, PROCESSED / f"ledger/{s}.png") for s in ledger_names], CONTACT / "event_015_ledger_finals.png", 3, (260, 150))

    # No two finals within a primary visual family may be byte-identical.
    for family in (REPORTS, NEWS, SUPERS, FLAGS, EMBLEMS, PORTRAITS, FORMATIONS):
        hashes = []
        for stem in family:
            match = next(row for row in records if row["stem"] == stem)
            hashes.append(match["final_sha256"])
        if len(hashes) != len(set(hashes)):
            raise ValueError(f"duplicate final detected in family: {family}")

    print(f"built {len(records)} final records")


if __name__ == "__main__":
    main()
