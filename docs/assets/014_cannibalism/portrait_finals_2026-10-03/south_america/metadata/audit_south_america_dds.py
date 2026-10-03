"""Audit Event 014 South America candidate DDS headers and pixel round trips."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
WIDTH = 156
HEIGHT = 210
EXPECTED_BYTES = 128 + WIDTH * HEIGHT * 4
EXPECTED_FLAGS = 0x1 | 0x2 | 0x4 | 0x8 | 0x1000


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def audit_slot(slot: str) -> tuple[dict, Image.Image]:
    stem = f"leader_{slot}_warlord_south_america"
    dds_path = ROOT / "candidate_dds" / f"{stem}.dds"
    png_name = f"{stem}_156x210_v02.png" if slot == "CBD" else f"{stem}_156x210.png"
    png_path = ROOT / "processed_png" / png_name
    data = dds_path.read_bytes()
    if len(data) != EXPECTED_BYTES:
        raise ValueError(f"{slot}: DDS length {len(data)} != {EXPECTED_BYTES}")
    if data[:4] != b"DDS ":
        raise ValueError(f"{slot}: missing DDS magic")

    words = struct.unpack("<31I", data[4:128])
    schema = {
        "header_size": words[0],
        "header_flags": words[1],
        "height": words[2],
        "width": words[3],
        "pitch": words[4],
        "depth": words[5],
        "mipmap_count": words[6],
        "reserved_words": list(words[7:18]),
        "pixel_format_size": words[18],
        "pixel_format_flags": words[19],
        "fourcc": words[20],
        "rgb_bit_count": words[21],
        "red_mask": words[22],
        "green_mask": words[23],
        "blue_mask": words[24],
        "alpha_mask": words[25],
        "caps": words[26],
        "caps2": words[27],
        "caps3": words[28],
        "caps4": words[29],
        "reserved2": words[30],
    }
    expected = {
        "header_size": 124,
        "height": HEIGHT,
        "width": WIDTH,
        "pitch": WIDTH * 4,
        "depth": 0,
        "mipmap_count": 0,
        "pixel_format_size": 32,
        "pixel_format_flags": 65,
        "fourcc": 0,
        "rgb_bit_count": 32,
        "red_mask": 0x00FF0000,
        "green_mask": 0x0000FF00,
        "blue_mask": 0x000000FF,
        "alpha_mask": 0xFF000000,
        "caps": 0x1000,
        "caps2": 0,
        "caps3": 0,
        "caps4": 0,
        "reserved2": 0,
    }
    for key, value in expected.items():
        if schema[key] != value:
            raise ValueError(f"{slot}: DDS {key}={schema[key]!r}, expected {value!r}")
    if schema["header_flags"] != EXPECTED_FLAGS:
        raise ValueError(f"{slot}: unexpected DDS header flags {schema['header_flags']:#x}")
    if any(schema["reserved_words"]):
        raise ValueError(f"{slot}: nonzero reserved header dword")

    bgra = data[128:]
    decoded = Image.frombytes("RGBA", (WIDTH, HEIGHT), bgra, "raw", "BGRA")
    with Image.open(png_path) as source:
        source.load()
        source_rgba = source.convert("RGBA")
    if decoded.tobytes() != source_rgba.tobytes():
        raise ValueError(f"{slot}: decoded DDS RGBA pixels differ from selected PNG")
    alpha_min, alpha_max = decoded.getchannel("A").getextrema()
    if (alpha_min, alpha_max) != (255, 255):
        raise ValueError(f"{slot}: unexpected alpha range {(alpha_min, alpha_max)}")

    return (
        {
            "slot": slot,
            "selected_png": png_path.relative_to(ROOT).as_posix(),
            "selected_png_sha256": sha256(png_path.read_bytes()),
            "selected_png_dimensions": [WIDTH, HEIGHT],
            "dds": dds_path.relative_to(ROOT).as_posix(),
            "dds_file_bytes": len(data),
            "dds_sha256": sha256(data),
            "schema": schema,
            "decoded_rgba_sha256": sha256(decoded.tobytes()),
            "decoded_rgba_matches_selected_png_exactly": True,
            "alpha_min": alpha_min,
            "alpha_max": alpha_max,
        },
        decoded,
    )


def main() -> None:
    rows = []
    decoded_images = []
    for slot in SLOTS:
        row, image = audit_slot(slot)
        rows.append(row)
        decoded_images.append(image)

    if len({row["dds_sha256"] for row in rows}) != len(SLOTS):
        raise ValueError("DDS files are not byte-unique")
    if len({row["decoded_rgba_sha256"] for row in rows}) != len(SLOTS):
        raise ValueError("Decoded DDS pixel buffers are not unique")

    native = Image.new("RGB", (WIDTH * 4, HEIGHT * 2), (24, 24, 24))
    nearest = Image.new("RGB", (WIDTH * 16, HEIGHT * 8), (24, 24, 24))
    for index, image in enumerate(decoded_images):
        x = (index % 4) * WIDTH
        y = (index // 4) * HEIGHT
        native.paste(image.convert("RGB"), (x, y))
        nearest.paste(image.convert("RGB").resize((WIDTH * 4, HEIGHT * 4), Image.Resampling.NEAREST), (x * 4, y * 4))

    native_path = ROOT / "review" / "south_america_dds_decoded_native_4x2_contact_sheet.png"
    nearest_path = ROOT / "review" / "south_america_dds_decoded_nearest4_4x2_contact_sheet.png"
    native.save(native_path, format="PNG", optimize=False)
    nearest.save(nearest_path, format="PNG", optimize=False)

    selected_native_path = ROOT / "review" / "south_america_native_4x2_contact_sheet_v02.png"
    selected_nearest_path = ROOT / "review" / "south_america_nearest4_4x2_contact_sheet_v02.png"
    with Image.open(selected_native_path) as selected_native, Image.open(selected_nearest_path) as selected_nearest:
        if native.tobytes() != selected_native.convert("RGB").tobytes():
            raise ValueError("Decoded DDS native contact sheet differs from selected-PNG native sheet")
        if nearest.tobytes() != selected_nearest.convert("RGB").tobytes():
            raise ValueError("Decoded DDS nearest-neighbour contact differs from selected-PNG contact")

    report = {
        "target_canvas": [WIDTH, HEIGHT],
        "format": "legacy uncompressed 32-bit BGRA, opaque alpha, one base image level, no mipmaps",
        "backend": "Bundled converter FFmpeg BGRA fallback; texconv absent and ffmpeg available on PATH.",
        "dds_schema_and_pixel_checks": rows,
        "unique_dds_file_hashes": len({row["dds_sha256"] for row in rows}),
        "unique_decoded_rgba_hashes": len({row["decoded_rgba_sha256"] for row in rows}),
        "decoded_contact_sheets": [
            {"path": native_path.relative_to(ROOT).as_posix(), "dimensions": list(native.size), "sha256": sha256(native_path.read_bytes()), "matches_selected_png_contact_exactly": True},
            {"path": nearest_path.relative_to(ROOT).as_posix(), "dimensions": list(nearest.size), "sha256": sha256(nearest_path.read_bytes()), "matches_selected_png_contact_exactly": True},
        ],
        "runtime_installation": "separate promotion step; see metadata/runtime_install_receipt_2026-10-03.json",
    }
    (ROOT / "metadata" / "dds_roundtrip_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
