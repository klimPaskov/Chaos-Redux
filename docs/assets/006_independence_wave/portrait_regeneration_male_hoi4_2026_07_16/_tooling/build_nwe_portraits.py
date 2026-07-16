#!/usr/bin/env python3
"""Build the ACX/AEX/AFX/AGX/AJX male Event 006 portrait tranche.

The source masters are independent built-in ImageGen outputs. This helper only
performs the repository-approved deterministic portrait finish, canonical
commander-small dossier composition, DDS conversion/decoding, contact-sheet
assembly, and immutable historical-portrait hash guards.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[5]
PACKAGE = Path(__file__).resolve().parents[1]
RAW = PACKAGE / "raw_outputs"
PROCESSED = PACKAGE / "processed_png"
DECODED = PACKAGE / "dds_decoded_png"
SMALL_PROCESSED = PACKAGE / "small_processed_png"
SMALL_DECODED = PACKAGE / "small_dds_decoded_png"
REVIEWS = PACKAGE / "review_sheets"
CONTACTS = PACKAGE / "contact_sheets"
METADATA = PACKAGE / "metadata"
RUNTIME = ROOT / "gfx" / "leaders" / "006_independence_wave"
TOOLS = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools"
SKILL_ASSETS = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "assets"
PROCESSOR = TOOLS / "advisor_icon_processing.py"
CONVERTER = TOOLS / "convert_to_dds.py"
LEADER_REFS = SKILL_ASSETS / "vanilla_reference" / "portraits" / "leaders"
COMMANDER_REFS = SKILL_ASSETS / "vanilla_reference" / "portraits" / "commanders"
ADVISOR_REFS = SKILL_ASSETS / "vanilla_reference" / "portraits" / "advisors"
OVERLAY_ROOT = SKILL_ASSETS / "advisor_dossier_overlays"
OVERLAY_MANIFEST = OVERLAY_ROOT / "advisor_dossier_overlay_manifest.json"
FRAME_SOURCE = OVERLAY_ROOT / "v3" / "advisor_frame_shadowless_imagegen_source.png"
FRAME_OVERLAY = OVERLAY_ROOT / "v3" / "advisor_frame_shadowless_overlay.png"
PAPER_SOURCE = OVERLAY_ROOT / "v3" / "advisor_paper_shadowless_imagegen_source.png"
PAPER_OVERLAY = OVERLAY_ROOT / "v3" / "advisor_paper_shadowless_overlay.png"


PORTRAITS = (
    "portrait_ACX_cornish_coastal_commander",
    "portrait_ACX_cornish_port_and_mines_committee",
    "portrait_AEX_flemish_civil_industrial_board",
    "portrait_AEX_flemish_industrial_security_commander",
    "portrait_AFX_walloon_provisional_assembly",
    "portrait_AFX_walloon_reserve_commander",
    "portrait_AGX_friesland_coastal_commander",
    "portrait_AGX_friesland_coastal_council",
    "portrait_AJX_saar_industrial_security_commissioner",
    "portrait_AJX_saar_municipal_neutral_commission",
)

COMMANDERS = {
    "portrait_ACX_cornish_coastal_commander",
    "portrait_AEX_flemish_industrial_security_commander",
    "portrait_AFX_walloon_reserve_commander",
    "portrait_AGX_friesland_coastal_commander",
    "portrait_AJX_saar_industrial_security_commissioner",
}

ALL_PORTRAITS = PORTRAITS + (
    "portrait_BAY_independence_wave_mountain_commandant",
    "portrait_BAY_independence_wave_state_council",
    "portrait_BRI_independence_wave_civic_commission",
    "portrait_BRI_independence_wave_coastal_commandant",
    "portrait_RHI_independence_wave_provisional_directorate",
    "portrait_RHI_independence_wave_river_commandant",
    "portrait_SCO_independence_wave_civic_convention",
    "portrait_SCO_independence_wave_territorial_commandant",
    "portrait_WLS_independence_wave_mountain_commandant",
    "portrait_WLS_independence_wave_national_council",
)

ALL_COMMANDERS = tuple(sorted(COMMANDERS | {
    "portrait_BAY_independence_wave_mountain_commandant",
    "portrait_BRI_independence_wave_coastal_commandant",
    "portrait_RHI_independence_wave_river_commandant",
    "portrait_SCO_independence_wave_territorial_commandant",
    "portrait_WLS_independence_wave_mountain_commandant",
}))

# Crop and visible-face boxes are in each ImageGen master's native pixels.
SMALL_GEOMETRY = {
    "portrait_ACX_cornish_coastal_commander": ((100, 0, 980, 1400), (360, 310, 750, 800)),
    "portrait_AEX_flemish_industrial_security_commander": ((100, 0, 980, 1400), (350, 300, 760, 800)),
    "portrait_AFX_walloon_reserve_commander": ((100, 0, 980, 1400), (350, 270, 750, 770)),
    "portrait_AGX_friesland_coastal_commander": ((100, 0, 980, 1400), (320, 330, 760, 820)),
    "portrait_AJX_saar_industrial_security_commissioner": ((100, 0, 980, 1400), (330, 290, 760, 800)),
}

APPROVED_HASHES = {
    "portrait_BAY_rupprecht_of_bavaria.dds": "7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b",
    "portrait_RHI_josef_friedrich_matthes.dds": "aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_approved_unchanged() -> None:
    for filename, expected in APPROVED_HASHES.items():
        path = RUNTIME / filename
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"protected portrait changed: {path}\nexpected {expected}\nactual   {actual}")


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def ensure_dirs() -> None:
    for directory in (PROCESSED, DECODED, SMALL_PROCESSED, SMALL_DECODED, REVIEWS, CONTACTS, METADATA):
        directory.mkdir(parents=True, exist_ok=True)


def process_large() -> None:
    assert_approved_unchanged()
    ensure_dirs()
    for stem in PORTRAITS:
        source = RAW / f"{stem}.png"
        with Image.open(source) as image:
            width, height = image.size
        output = PROCESSED / f"{stem}.png"
        review = REVIEWS / f"{stem}_review.png"
        metadata = METADATA / f"{stem}.json"
        # The retained processor's leader-mode comparison layout is pinned to
        # Stauning/de Valera filenames. Commander-family comparison is added by
        # this package's dedicated commander contact sheet after processing.
        reference_dir = LEADER_REFS
        run([
            sys.executable,
            str(PROCESSOR),
            "leader",
            str(source),
            str(output),
            "--crop", "0", "0", str(width), str(height),
            "--source-kind", "fictional",
            "--review-sheet", str(review),
            "--metadata", str(metadata),
            "--reference-dir", str(reference_dir),
        ])
    make_large_contact(PROCESSED, CONTACTS / "nwe_processed_156x210_contact_sheet.png", "Processed 156x210 candidates")
    make_canonical_comparisons()
    assert_approved_unchanged()


def convert(source: Path, output: Path, width: int, height: int) -> None:
    run([
        sys.executable,
        str(CONVERTER),
        "--input", str(source),
        "--output", str(output),
        "--width", str(width),
        "--height", str(height),
    ])


def decode_dds(path: Path, expected: tuple[int, int]) -> Image.Image:
    raw = path.read_bytes()
    if raw[:4] != b"DDS " or len(raw) < 128:
        raise ValueError(f"invalid DDS: {path}")
    height = struct.unpack_from("<I", raw, 12)[0]
    width = struct.unpack_from("<I", raw, 16)[0]
    header_size = struct.unpack_from("<I", raw, 4)[0]
    pitch = struct.unpack_from("<I", raw, 20)[0]
    pixel_format_size = struct.unpack_from("<I", raw, 76)[0]
    flags = struct.unpack_from("<I", raw, 80)[0]
    bits = struct.unpack_from("<I", raw, 88)[0]
    masks = struct.unpack_from("<IIII", raw, 92)
    caps = struct.unpack_from("<I", raw, 108)[0]
    if (width, height) != expected:
        raise ValueError(f"wrong DDS size: {path}: {(width, height)}")
    if (header_size, pixel_format_size, flags, bits) != (124, 32, 0x41, 32):
        raise ValueError(f"wrong DDS format fields: {path}")
    if masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
        raise ValueError(f"wrong DDS masks: {path}")
    if pitch != width * 4 or caps != 0x1000 or len(raw) != 128 + width * height * 4:
        raise ValueError(f"wrong DDS pitch, caps, or length: {path}")
    rgba = bytearray(width * height * 4)
    for offset in range(0, len(rgba), 4):
        blue, green, red, alpha = raw[128 + offset : 132 + offset]
        rgba[offset : offset + 4] = bytes((red, green, blue, alpha))
    return Image.frombytes("RGBA", (width, height), bytes(rgba))


def verify_round_trip(source: Path, decoded: Image.Image, runtime: Path) -> None:
    with Image.open(source) as image:
        expected = image.convert("RGBA")
    if ImageChops.difference(expected, decoded).getbbox() is not None:
        raise ValueError(f"DDS round-trip differs from PNG: {runtime}")


def install_large() -> None:
    assert_approved_unchanged()
    ensure_dirs()
    for stem in PORTRAITS:
        source = PROCESSED / f"{stem}.png"
        runtime = RUNTIME / f"{stem}.dds"
        convert(source, runtime, 156, 210)
        decoded = decode_dds(runtime, (156, 210))
        verify_round_trip(source, decoded, runtime)
        decoded.save(DECODED / f"{stem}.png")
    make_large_contact(DECODED, CONTACTS / "nwe_runtime_dds_156x210_contact_sheet.png", "Runtime DDS decodes at 156x210")
    assert_approved_unchanged()


def process_small() -> None:
    assert_approved_unchanged()
    ensure_dirs()
    for stem in sorted(COMMANDERS):
        source = RAW / f"{stem}.png"
        crop, face_box = SMALL_GEOMETRY[stem]
        output = SMALL_PROCESSED / f"{stem}_small.png"
        review = REVIEWS / f"{stem}_small_review.png"
        metadata = METADATA / f"{stem}_small.json"
        run([
            sys.executable,
            str(PROCESSOR),
            "advisor",
            str(source),
            str(output),
            "--crop", *(str(value) for value in crop),
            "--face-box", *(str(value) for value in face_box),
            "--source-kind", "fictional",
            "--review-sheet", str(review),
            "--metadata", str(metadata),
            "--reference-dir", str(ADVISOR_REFS),
            "--advisor-overlay-manifest", str(OVERLAY_MANIFEST),
            "--advisor-frame-source", str(FRAME_SOURCE),
            "--advisor-frame-overlay", str(FRAME_OVERLAY),
            "--advisor-paper-source", str(PAPER_SOURCE),
            "--advisor-paper-overlay", str(PAPER_OVERLAY),
        ])
        runtime = RUNTIME / f"{stem}_small.dds"
        convert(output, runtime, 65, 67)
        decoded = decode_dds(runtime, (65, 67))
        verify_round_trip(output, decoded, runtime)
        decoded.save(SMALL_DECODED / f"{stem}_small.png")
    make_small_contact(SMALL_DECODED, CONTACTS / "nwe_runtime_commander_small_65x67_contact_sheet.png")
    assert_approved_unchanged()


def label_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    path = Path("C:/Windows/Fonts") / ("arialbd.ttf" if bold else "arial.ttf")
    return ImageFont.truetype(str(path), size=size) if path.is_file() else ImageFont.load_default()


def short_label(stem: str) -> str:
    return stem.replace("portrait_", "").replace("_independence_wave_", "\n").replace("_", " ")


def make_large_contact(source_dir: Path, output: Path, title: str) -> None:
    columns = 5
    scale = 2
    display = (156 * scale, 210 * scale)
    cell = (display[0] + 24, display[1] + 62)
    rows = (len(PORTRAITS) + columns - 1) // columns
    sheet = Image.new("RGB", (cell[0] * columns, 70 + cell[1] * rows), "#171b20")
    draw = ImageDraw.Draw(sheet)
    draw.text((18, 12), title, fill="#f1eee7", font=label_font(26, True))
    draw.text((18, 44), "ACX / AEX / AFX / AGX / AJX male portrait tranche", fill="#aeb8c5", font=label_font(14))
    for index, stem in enumerate(PORTRAITS):
        x = (index % columns) * cell[0]
        y = 70 + (index // columns) * cell[1]
        draw.rectangle((x + 5, y + 5, x + cell[0] - 6, y + cell[1] - 6), fill="#252c35", outline="#5b6878", width=2)
        with Image.open(source_dir / f"{stem}.png") as image:
            preview = image.convert("RGB").resize(display, Image.Resampling.NEAREST)
        sheet.paste(preview, (x + 12, y + 12))
        draw.multiline_text((x + 10, y + display[1] + 18), short_label(stem), fill="#f0eee8", font=label_font(12, True), spacing=2)
    sheet.save(output)


def make_small_contact(source_dir: Path, output: Path) -> None:
    references = (
        ("Vanilla Paulus", ADVISOR_REFS / "army_small_ger_friedrich_paulus.png"),
        ("Vanilla von Kluge", ADVISOR_REFS / "army_small_ger_gunther_von_kluge.png"),
        ("Vanilla Rommel", ADVISOR_REFS / "army_small_ger_erwin_rommel.png"),
    )
    records = [(short_label(stem), source_dir / f"{stem}_small.png") for stem in sorted(COMMANDERS)] + list(references)
    columns = 4
    scale = 4
    display = (65 * scale, 67 * scale)
    cell = (display[0] + 24, display[1] + 54)
    rows = (len(records) + columns - 1) // columns
    sheet = Image.new("RGB", (cell[0] * columns, 70 + cell[1] * rows), "#171b20")
    draw = ImageDraw.Draw(sheet)
    draw.text((18, 12), "Runtime commander-small dossier decodes", fill="#f1eee7", font=label_font(26, True))
    draw.text((18, 44), "65x67 sources enlarged 4x nearest-neighbour; canonical vanilla comparisons included", fill="#aeb8c5", font=label_font(14))
    for index, (label, path) in enumerate(records):
        x = (index % columns) * cell[0]
        y = 70 + (index // columns) * cell[1]
        draw.rectangle((x + 5, y + 5, x + cell[0] - 6, y + cell[1] - 6), fill="#252c35", outline="#5b6878", width=2)
        with Image.open(path) as image:
            preview = image.convert("RGBA").resize(display, Image.Resampling.NEAREST)
        checker = Image.new("RGB", display, "#8e8e8e")
        checker_draw = ImageDraw.Draw(checker)
        step = 24
        for yy in range(0, display[1], step):
            for xx in range(0, display[0], step):
                if (xx // step + yy // step) % 2:
                    checker_draw.rectangle((xx, yy, xx + step - 1, yy + step - 1), fill="#b6b6b6")
        checker.paste(preview, mask=preview.getchannel("A"))
        sheet.paste(checker, (x + 12, y + 12))
        draw.multiline_text((x + 10, y + display[1] + 18), label, fill="#f0eee8", font=label_font(12, True), spacing=2)
    sheet.save(output)


def make_all_small_contact(source_dir: Path, output: Path) -> None:
    references = (
        ("Vanilla Paulus", ADVISOR_REFS / "army_small_ger_friedrich_paulus.png"),
        ("Vanilla von Kluge", ADVISOR_REFS / "army_small_ger_gunther_von_kluge.png"),
        ("Vanilla Rommel", ADVISOR_REFS / "army_small_ger_erwin_rommel.png"),
    )
    records = [(short_label(stem), source_dir / f"{stem}_small.png") for stem in ALL_COMMANDERS] + list(references)
    columns = 5
    scale = 4
    display = (65 * scale, 67 * scale)
    cell = (display[0] + 24, display[1] + 54)
    rows = (len(records) + columns - 1) // columns
    sheet = Image.new("RGB", (cell[0] * columns, 70 + cell[1] * rows), "#171b20")
    draw = ImageDraw.Draw(sheet)
    draw.text((18, 12), "All Event 006 commander-small runtime decodes", fill="#f1eee7", font=label_font(26, True))
    draw.text((18, 44), "Ten 65x67 dossiers enlarged 4x; canonical vanilla comparisons included", fill="#aeb8c5", font=label_font(14))
    for index, (label, path) in enumerate(records):
        x = (index % columns) * cell[0]
        y = 70 + (index // columns) * cell[1]
        draw.rectangle((x + 5, y + 5, x + cell[0] - 6, y + cell[1] - 6), fill="#252c35", outline="#5b6878", width=2)
        with Image.open(path) as image:
            preview = image.convert("RGBA").resize(display, Image.Resampling.NEAREST)
        checker = Image.new("RGB", display, "#8e8e8e")
        checker_draw = ImageDraw.Draw(checker)
        step = 24
        for yy in range(0, display[1], step):
            for xx in range(0, display[0], step):
                if (xx // step + yy // step) % 2:
                    checker_draw.rectangle((xx, yy, xx + step - 1, yy + step - 1), fill="#b6b6b6")
        checker.paste(preview, mask=preview.getchannel("A"))
        sheet.paste(checker, (x + 12, y + 12))
        draw.multiline_text((x + 10, y + display[1] + 18), label, fill="#f0eee8", font=label_font(12, True), spacing=2)
    sheet.save(output)


def make_comparison_contact(
    records: list[tuple[str, Path]],
    output: Path,
    title: str,
    columns: int,
) -> None:
    scale = 2
    display = (156 * scale, 210 * scale)
    cell = (display[0] + 24, display[1] + 62)
    rows = (len(records) + columns - 1) // columns
    sheet = Image.new("RGB", (cell[0] * columns, 70 + cell[1] * rows), "#171b20")
    draw = ImageDraw.Draw(sheet)
    draw.text((18, 12), title, fill="#f1eee7", font=label_font(26, True))
    draw.text((18, 44), "Target-size art enlarged 2x nearest-neighbour for style and framing review", fill="#aeb8c5", font=label_font(14))
    for index, (label, path) in enumerate(records):
        x = (index % columns) * cell[0]
        y = 70 + (index // columns) * cell[1]
        draw.rectangle((x + 5, y + 5, x + cell[0] - 6, y + cell[1] - 6), fill="#252c35", outline="#5b6878", width=2)
        with Image.open(path) as image:
            preview = image.convert("RGB").resize(display, Image.Resampling.NEAREST)
        sheet.paste(preview, (x + 12, y + 12))
        draw.multiline_text((x + 10, y + display[1] + 18), label, fill="#f0eee8", font=label_font(12, True), spacing=2)
    sheet.save(output)


def make_canonical_comparisons() -> None:
    approved_root = ROOT / "docs" / "assets" / "006_independence_wave" / "processed_png" / "portraits"
    institutional = [
        (short_label(stem), PROCESSED / f"{stem}.png")
        for stem in PORTRAITS
        if stem not in COMMANDERS
    ]
    leader_refs = [
        ("Vanilla Stauning", LEADER_REFS / "den_thorvald_stauning.png"),
        ("Vanilla de Valera", LEADER_REFS / "ire_eamon_de_valera.png"),
        ("Approved Matthes", approved_root / "portrait_rhi_josef_friedrich_matthes.png"),
        ("Approved Rupprecht", approved_root / "portrait_bay_rupprecht_of_bavaria.png"),
    ]
    make_comparison_contact(
        institutional + leader_refs,
        CONTACTS / "nwe_institutional_canonical_comparison.png",
        "Institutional portraits against canonical quality targets",
        5,
    )


def make_merged_evidence() -> None:
    """Decode and compare the complete 20-large/10-small runtime package.

    This stage is deliberately processor-free. It only verifies already
    installed DDS files against the retained processed PNGs and creates merged
    visual evidence.
    """

    assert_approved_unchanged()
    ensure_dirs()
    for stem in ALL_PORTRAITS:
        source = PROCESSED / f"{stem}.png"
        runtime = RUNTIME / f"{stem}.dds"
        decoded = decode_dds(runtime, (156, 210))
        verify_round_trip(source, decoded, runtime)
        decoded.save(DECODED / f"{stem}.png")
    for stem in ALL_COMMANDERS:
        source = SMALL_PROCESSED / f"{stem}_small.png"
        runtime = RUNTIME / f"{stem}_small.dds"
        decoded = decode_dds(runtime, (65, 67))
        verify_round_trip(source, decoded, runtime)
        decoded.save(SMALL_DECODED / f"{stem}_small.png")

    all_runtime = [(short_label(stem), DECODED / f"{stem}.png") for stem in ALL_PORTRAITS]
    make_comparison_contact(
        all_runtime,
        CONTACTS / "all_runtime_large_156x210_contact_sheet.png",
        "All Event 006 regenerated runtime portrait decodes",
        5,
    )
    approved_root = ROOT / "docs" / "assets" / "006_independence_wave" / "processed_png" / "portraits"
    canonical = [
        ("Vanilla Stauning", LEADER_REFS / "den_thorvald_stauning.png"),
        ("Vanilla de Valera", LEADER_REFS / "ire_eamon_de_valera.png"),
        ("Approved Matthes", approved_root / "portrait_rhi_josef_friedrich_matthes.png"),
        ("Approved Rupprecht", approved_root / "portrait_bay_rupprecht_of_bavaria.png"),
    ]
    make_comparison_contact(
        all_runtime + canonical,
        CONTACTS / "all_runtime_large_canonical_comparison.png",
        "Complete regenerated set with canonical quality targets",
        6,
    )
    make_all_small_contact(
        SMALL_DECODED,
        CONTACTS / "all_runtime_commander_small_65x67_contact_sheet.png",
    )
    assert_approved_unchanged()
    commanders = [(short_label(stem), PROCESSED / f"{stem}.png") for stem in sorted(COMMANDERS)]
    commander_refs = [
        ("Vanilla land commander 1", COMMANDER_REFS / "generic_africa_land_1.png"),
        ("Vanilla land commander 2", COMMANDER_REFS / "generic_africa_land_2.png"),
        ("Vanilla land commander 3", COMMANDER_REFS / "generic_africa_land_3.png"),
        ("Vanilla Mannerheim", LEADER_REFS / "fin_carl_mannerheim.png"),
        ("Approved Rupprecht", approved_root / "portrait_bay_rupprecht_of_bavaria.png"),
    ]
    make_comparison_contact(
        commanders + commander_refs,
        CONTACTS / "nwe_commander_canonical_comparison.png",
        "Commander portraits against canonical quality targets",
        5,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=("process-large", "install-large", "process-small", "comparisons", "merge-evidence", "all"))
    args = parser.parse_args()
    if args.stage in ("process-large", "all"):
        process_large()
    if args.stage in ("install-large", "all"):
        install_large()
    if args.stage in ("process-small", "all"):
        process_small()
    if args.stage == "comparisons":
        ensure_dirs()
        make_canonical_comparisons()
    if args.stage == "merge-evidence":
        make_merged_evidence()


if __name__ == "__main__":
    main()
