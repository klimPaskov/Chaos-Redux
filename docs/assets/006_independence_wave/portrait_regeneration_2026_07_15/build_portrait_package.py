#!/usr/bin/env python3
"""Build and validate the Event 006 fictional leader portrait package.

The 18 source masters are independently generated ImageGen portraits. This
script performs only deterministic HOI4 finishing, commander-thumbnail
derivation, DDS conversion, runtime decoding, contact-sheet assembly, and
hash-ledger generation. It never writes the two user-approved historical
portraits and refuses to run if either approved DDS has changed.
"""

from __future__ import annotations

import hashlib
import json
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE_ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
SMALL_ROOT = PACKAGE_ROOT / "processed_small_png"
DECODED_ROOT = PACKAGE_ROOT / "dds_decoded_png"
SMALL_DECODED_ROOT = PACKAGE_ROOT / "dds_decoded_small_png"
REVIEW_ROOT = PACKAGE_ROOT / "review_sheets"
METADATA_ROOT = PACKAGE_ROOT / "metadata"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
RUNTIME_ROOT = ROOT / "gfx" / "leaders" / "006_independence_wave"
PORTRAIT_PROCESSOR = ROOT / ".tools" / "process_hoi4_portrait.py"
DDS_CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
HASH_LEDGER = PACKAGE_ROOT / "portrait_package_hashes.sha256"


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
    "portrait_BAY_independence_wave_mountain_commandant",
    "portrait_BAY_independence_wave_state_council",
    "portrait_RHI_independence_wave_provisional_directorate",
    "portrait_RHI_independence_wave_river_commandant",
    "portrait_SCO_independence_wave_civic_convention",
    "portrait_SCO_independence_wave_territorial_commandant",
    "portrait_WLS_independence_wave_mountain_commandant",
    "portrait_WLS_independence_wave_national_council",
)


COMMANDERS = {
    "portrait_ACX_cornish_coastal_commander",
    "portrait_AEX_flemish_industrial_security_commander",
    "portrait_AFX_walloon_reserve_commander",
    "portrait_AGX_friesland_coastal_commander",
    "portrait_AJX_saar_industrial_security_commissioner",
    "portrait_BAY_independence_wave_mountain_commandant",
    "portrait_RHI_independence_wave_river_commandant",
    "portrait_SCO_independence_wave_territorial_commandant",
    "portrait_WLS_independence_wave_mountain_commandant",
}


APPROVED_HISTORICAL_HASHES = {
    "portrait_BAY_rupprecht_of_bavaria.dds": "7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b",
    "portrait_RHI_josef_friedrich_matthes.dds": "aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidate = Path("C:/Windows/Fonts") / filename
    if candidate.is_file():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def ensure_directories() -> None:
    for directory in (
        PROCESSED_ROOT,
        SMALL_ROOT,
        DECODED_ROOT,
        SMALL_DECODED_ROOT,
        REVIEW_ROOT,
        METADATA_ROOT,
        CONTACT_ROOT,
        RUNTIME_ROOT,
    ):
        directory.mkdir(parents=True, exist_ok=True)


def assert_approved_portraits_unchanged() -> None:
    for filename, expected in APPROVED_HISTORICAL_HASHES.items():
        path = RUNTIME_ROOT / filename
        if not path.is_file():
            raise FileNotFoundError(f"Missing approved historical portrait: {path}")
        actual = sha256(path)
        if actual != expected:
            raise ValueError(
                f"Approved historical portrait changed: {path}\n"
                f"expected {expected}\nactual   {actual}"
            )


def run_portrait_processor(stem: str) -> Path:
    source = SOURCE_ROOT / f"{stem}_source.png"
    if not source.is_file():
        raise FileNotFoundError(source)
    with Image.open(source) as image:
        width, height = image.size
    processed = PROCESSED_ROOT / f"{stem}.png"
    review = REVIEW_ROOT / f"{stem}_review.png"
    metadata = METADATA_ROOT / f"{stem}.json"
    command = [
        sys.executable,
        str(PORTRAIT_PROCESSOR),
        "leader",
        str(source),
        str(processed),
        "--crop",
        "0",
        "0",
        str(width),
        str(height),
        "--source-kind",
        "fictional",
        "--review-sheet",
        str(review),
        "--metadata",
        str(metadata),
    ]
    subprocess.run(command, cwd=ROOT, check=True)
    metadata_payload = json.loads(metadata.read_text(encoding="utf-8"))
    for key in ("source", "output", "review_sheet", "reference_dir"):
        value = Path(metadata_payload[key])
        if value.is_absolute() and value.is_relative_to(ROOT):
            metadata_payload[key] = value.relative_to(ROOT).as_posix()
    metadata.write_text(json.dumps(metadata_payload, indent=2) + "\n", encoding="utf-8")
    return processed


def convert_dds(source: Path, output: Path, size: tuple[int, int]) -> None:
    command = [
        sys.executable,
        str(DDS_CONVERTER),
        "--input",
        str(source),
        "--output",
        str(output),
        "--width",
        str(size[0]),
        "--height",
        str(size[1]),
    ]
    subprocess.run(command, cwd=ROOT, check=True)


def decode_dds(path: Path, expected_size: tuple[int, int]) -> Image.Image:
    raw = path.read_bytes()
    if len(raw) < 128 or raw[:4] != b"DDS ":
        raise ValueError(f"Invalid DDS header: {path}")
    header_size = struct.unpack_from("<I", raw, 4)[0]
    height = struct.unpack_from("<I", raw, 12)[0]
    width = struct.unpack_from("<I", raw, 16)[0]
    pitch = struct.unpack_from("<I", raw, 20)[0]
    pixel_format_size = struct.unpack_from("<I", raw, 76)[0]
    pixel_format_flags = struct.unpack_from("<I", raw, 80)[0]
    rgb_bits = struct.unpack_from("<I", raw, 88)[0]
    masks = struct.unpack_from("<IIII", raw, 92)
    caps = struct.unpack_from("<I", raw, 108)[0]
    if (width, height) != expected_size:
        raise ValueError(f"Unexpected DDS dimensions in {path}: {(width, height)}")
    if (header_size, pixel_format_size, pixel_format_flags, rgb_bits) != (124, 32, 0x41, 32):
        raise ValueError(f"DDS is not legacy uncompressed 32-bit BGRA: {path}")
    if masks != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
        raise ValueError(f"Unexpected DDS channel masks: {path}")
    if pitch != width * 4 or caps != 0x1000 or len(raw) != 128 + width * height * 4:
        raise ValueError(f"Unexpected DDS pitch, caps, or payload length: {path}")
    rgba = bytearray(width * height * 4)
    for index in range(0, len(rgba), 4):
        blue, green, red, alpha = raw[128 + index : 132 + index]
        rgba[index : index + 4] = bytes((red, green, blue, alpha))
    return Image.frombytes("RGBA", (width, height), bytes(rgba))


def verify_round_trip(source: Image.Image, decoded: Image.Image, path: Path) -> None:
    difference = ImageChops.difference(source.convert("RGBA"), decoded.convert("RGBA"))
    if difference.getbbox() is not None:
        raise ValueError(f"Decoded DDS differs from processed PNG: {path}")


def build_runtime_files() -> None:
    for stem in PORTRAITS:
        processed_path = run_portrait_processor(stem)
        with Image.open(processed_path) as image:
            processed = image.convert("RGBA")
        runtime_path = RUNTIME_ROOT / f"{stem}.dds"
        convert_dds(processed_path, runtime_path, (156, 210))
        decoded = decode_dds(runtime_path, (156, 210))
        verify_round_trip(processed, decoded, runtime_path)
        decoded.save(DECODED_ROOT / f"{stem}.png")

        if stem not in COMMANDERS:
            continue
        small = ImageOps.fit(
            processed,
            (50, 67),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.40),
        )
        small_path = SMALL_ROOT / f"{stem}_small.png"
        small.save(small_path)
        small_runtime_path = RUNTIME_ROOT / f"{stem}_small.dds"
        convert_dds(small_path, small_runtime_path, (50, 67))
        small_decoded = decode_dds(small_runtime_path, (50, 67))
        verify_round_trip(small, small_decoded, small_runtime_path)
        small_decoded.save(SMALL_DECODED_ROOT / f"{stem}_small.png")


def contact_sheet(
    records: list[tuple[str, Path]],
    output: Path,
    *,
    columns: int,
    native_size: tuple[int, int],
    scale: int,
    title: str,
) -> None:
    portrait_width, portrait_height = native_size
    display_size = (portrait_width * scale, portrait_height * scale)
    cell_width = display_size[0] + 28
    cell_height = display_size[1] + 66
    rows = (len(records) + columns - 1) // columns
    header = 72
    sheet = Image.new("RGB", (cell_width * columns, header + cell_height * rows), "#181c21")
    draw = ImageDraw.Draw(sheet)
    draw.text((22, 14), title, font=font(28, bold=True), fill="#f0eee8")
    draw.text(
        (23, 47),
        "Actual runtime DDS files decoded after legacy BGRA conversion",
        font=font(15),
        fill="#aeb8c5",
    )
    for index, (label, path) in enumerate(records):
        column = index % columns
        row = index // columns
        left = column * cell_width
        top = header + row * cell_height
        draw.rectangle(
            (left + 6, top + 6, left + cell_width - 7, top + cell_height - 7),
            fill="#252c35",
            outline="#5b6878",
            width=2,
        )
        with Image.open(path) as image:
            preview = image.convert("RGB").resize(display_size, Image.Resampling.NEAREST)
        sheet.paste(preview, (left + 14, top + 14))
        text_box = (left + 10, top + display_size[1] + 22, left + cell_width - 10, top + cell_height - 10)
        draw.multiline_text(
            (text_box[0], text_box[1]),
            label.replace("portrait_", "").replace("_independence_wave_", "\n").replace("_", " "),
            font=font(13, bold=True),
            fill="#f0eee8",
            spacing=2,
            align="center",
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def build_contact_sheets() -> list[Path]:
    large_records = [(stem, DECODED_ROOT / f"{stem}.png") for stem in PORTRAITS]
    small_records = [
        (stem, SMALL_DECODED_ROOT / f"{stem}_small.png")
        for stem in PORTRAITS
        if stem in COMMANDERS
    ]
    large_output = CONTACT_ROOT / "006_independence_wave_regenerated_portraits_runtime_dds_contact_sheet.png"
    small_output = CONTACT_ROOT / "006_independence_wave_regenerated_commander_thumbnails_runtime_dds_contact_sheet.png"
    contact_sheet(
        large_records,
        large_output,
        columns=6,
        native_size=(156, 210),
        scale=2,
        title="Event 006 regenerated character portraits",
    )
    contact_sheet(
        small_records,
        small_output,
        columns=5,
        native_size=(50, 67),
        scale=4,
        title="Event 006 regenerated commander thumbnails",
    )
    return [large_output, small_output]


def write_hash_ledger(contact_sheets: list[Path]) -> None:
    paths: set[Path] = set()
    for directory in (
        SOURCE_ROOT,
        PROCESSED_ROOT,
        SMALL_ROOT,
        DECODED_ROOT,
        SMALL_DECODED_ROOT,
        REVIEW_ROOT,
        METADATA_ROOT,
    ):
        paths.update(path for path in directory.glob("*") if path.is_file())
    paths.update(contact_sheets)
    for stem in PORTRAITS:
        paths.add(RUNTIME_ROOT / f"{stem}.dds")
        if stem in COMMANDERS:
            paths.add(RUNTIME_ROOT / f"{stem}_small.dds")
    paths.update(RUNTIME_ROOT / filename for filename in APPROVED_HISTORICAL_HASHES)
    rows = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in sorted(paths, key=lambda item: item.as_posix().lower())
    ]
    HASH_LEDGER.write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_build_report(contact_sheets: list[Path]) -> None:
    report = {
        "sources": len(PORTRAITS),
        "large_runtime_portraits": len(PORTRAITS),
        "commander_thumbnails": len(COMMANDERS),
        "approved_historical_portraits_preserved": sorted(APPROVED_HISTORICAL_HASHES),
        "contact_sheets": [path.relative_to(ROOT).as_posix() for path in contact_sheets],
        "dds_contract": "legacy uncompressed 32-bit BGRA, exact PNG round-trip",
        "visual_review": "required before acceptance",
    }
    (PACKAGE_ROOT / "build_report.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    ensure_directories()
    assert_approved_portraits_unchanged()
    build_runtime_files()
    assert_approved_portraits_unchanged()
    contact_sheets = build_contact_sheets()
    write_hash_ledger(contact_sheets)
    write_build_report(contact_sheets)
    print(f"Built {len(PORTRAITS)} leader portraits and {len(COMMANDERS)} commander thumbnails.")
    print("All runtime DDS files passed exact PNG-to-DDS round-trip validation.")
    print("The two approved historical portrait hashes remained unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
