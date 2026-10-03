"""Audit North America Event 014 candidate DDS files and build DDS-decoded contacts.
Run from the mod root with: python -B <this file>.
This verifies the bundled converter output against each approved 156x210 PNG and never writes runtime files.
"""
from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[6]
PACKAGE = ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/north_america"
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
EXPECTED_WIDTH = 156
EXPECTED_HEIGHT = 210
EXPECTED_SIZE = 128 + EXPECTED_WIDTH * EXPECTED_HEIGHT * 4
CONVERTER = ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"
BACKEND = "bundled converter FFmpeg BGRA fallback; texconv and texconv.exe were absent at conversion preflight"
FFMPEG_PATH = r"C:\Users\klimp\AppData\Local\Microsoft\WinGet\Packages\yt-dlp.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-N-123778-g3b55818764-win64-gpl\bin\ffmpeg.exe"

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]

def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def main() -> None:
    entries = []
    decoded: dict[str, Image.Image] = {}
    for slot in SLOTS:
        stem = f"leader_{slot}_warlord_north_america"
        png_rel = Path("processed_png") / f"{stem}_156x210.png"
        dds_rel = Path("candidate_dds") / f"{stem}.dds"
        png_path = PACKAGE / png_rel
        dds_path = PACKAGE / dds_rel
        png_bytes = png_path.read_bytes()
        dds_bytes = dds_path.read_bytes()
        if len(dds_bytes) != EXPECTED_SIZE:
            raise RuntimeError(f"{slot}: DDS length {len(dds_bytes)} != {EXPECTED_SIZE}")
        if dds_bytes[:4] != b"DDS " or u32(dds_bytes, 4) != 124:
            raise RuntimeError(f"{slot}: invalid legacy DDS magic/header size")
        header = {
            "flags": u32(dds_bytes, 8),
            "height": u32(dds_bytes, 12),
            "width": u32(dds_bytes, 16),
            "pitch": u32(dds_bytes, 20),
            "depth": u32(dds_bytes, 24),
            "mip_count": u32(dds_bytes, 28),
            "pixel_format_size": u32(dds_bytes, 76),
            "pixel_format_flags": u32(dds_bytes, 80),
            "fourcc": u32(dds_bytes, 84),
            "bit_count": u32(dds_bytes, 88),
            "red_mask": u32(dds_bytes, 92),
            "green_mask": u32(dds_bytes, 96),
            "blue_mask": u32(dds_bytes, 100),
            "alpha_mask": u32(dds_bytes, 104),
            "caps": u32(dds_bytes, 108),
        }
        expected_header = {
            "flags": 0x100F,
            "height": EXPECTED_HEIGHT,
            "width": EXPECTED_WIDTH,
            "pitch": EXPECTED_WIDTH * 4,
            "depth": 0,
            "mip_count": 0,
            "pixel_format_size": 32,
            "pixel_format_flags": 65,
            "fourcc": 0,
            "bit_count": 32,
            "red_mask": 0x00FF0000,
            "green_mask": 0x0000FF00,
            "blue_mask": 0x000000FF,
            "alpha_mask": 0xFF000000,
            "caps": 0x1000,
        }
        if header != expected_header:
            raise RuntimeError(f"{slot}: unexpected DDS header: {header}")
        payload = dds_bytes[128:]
        alpha = payload[3::4]
        alpha_min, alpha_max = min(alpha), max(alpha)
        if (alpha_min, alpha_max) != (255, 255):
            raise RuntimeError(f"{slot}: DDS is not fully opaque: alpha {alpha_min}-{alpha_max}")
        with Image.open(png_path) as source:
            if source.size != (EXPECTED_WIDTH, EXPECTED_HEIGHT) or source.mode != "RGB":
                raise RuntimeError(f"{slot}: processed PNG is not opaque RGB 156x210")
            expected_rgba = source.convert("RGBA")
        with Image.open(dds_path) as opened:
            if opened.size != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
                raise RuntimeError(f"{slot}: DDS decoder reports wrong dimensions {opened.size}")
            decoded_image = opened.convert("RGBA")
        expected_pixels = expected_rgba.tobytes()
        actual_pixels = decoded_image.tobytes()
        if actual_pixels != expected_pixels:
            raise RuntimeError(f"{slot}: decoded DDS RGBA pixels differ from the processed PNG")
        decoded[slot] = decoded_image.copy()
        entries.append({
            "slot": slot,
            "processed_png": png_rel.as_posix(),
            "processed_png_sha256": digest(png_bytes),
            "candidate_dds": dds_rel.as_posix(),
            "dimensions": [EXPECTED_WIDTH, EXPECTED_HEIGHT],
            "dds_bytes": len(dds_bytes),
            "dds_sha256": digest(dds_bytes),
            "dds_header": header,
            "alpha_byte_min": alpha_min,
            "alpha_byte_max": alpha_max,
            "opaque": True,
            "decoded_rgba_pixel_sha256": digest(actual_pixels),
            "processed_png_to_decoded_dds_rgba_pixel_equal": True,
            "candidate_state": "technically validated; parent final DDS review pending; not installed",
        })
    if len({e["dds_sha256"] for e in entries}) != len(SLOTS):
        raise RuntimeError("Candidate DDS file hashes are not unique")
    if len({e["decoded_rgba_pixel_sha256"] for e in entries}) != len(SLOTS):
        raise RuntimeError("Decoded DDS RGBA pixel hashes are not unique")
    native = Image.new("RGB", (EXPECTED_WIDTH * 4, EXPECTED_HEIGHT * 2), (28, 28, 28))
    nearest4 = Image.new("RGB", (EXPECTED_WIDTH * 16, EXPECTED_HEIGHT * 8), (28, 28, 28))
    for index, slot in enumerate(SLOTS):
        image = decoded[slot].convert("RGB")
        x = (index % 4) * EXPECTED_WIDTH
        y = (index // 4) * EXPECTED_HEIGHT
        native.paste(image, (x, y))
        nearest4.paste(image.resize((EXPECTED_WIDTH * 4, EXPECTED_HEIGHT * 4), Image.Resampling.NEAREST), (x * 4, y * 4))
    native_rel = "review/north_america_dds_decoded_native_4x2_contact_sheet.png"
    nearest_rel = "review/north_america_dds_decoded_nearest4_4x2_contact_sheet.png"
    native.save(PACKAGE / native_rel, format="PNG", optimize=False)
    nearest4.save(PACKAGE / nearest_rel, format="PNG", optimize=False)
    audit = {
        "status": "PASS: eight unique opaque BGRA32, one-level DDS candidates; every decoded RGBA pixel exactly matches its processed PNG",
        "review_gate": "parent final DDS review pending; no runtime writes",
        "conversion_date": "2026-10-03",
        "converter": CONVERTER,
        "backend": BACKEND,
        "ffmpeg_path": FFMPEG_PATH,
        "header_contract": {
            "magic": "DDS ",
            "header_size": 124,
            "file_header_bytes": 128,
            "pixel_format_offset": 76,
            "pixel_format_flags": 65,
            "bit_count": 32,
            "fourcc": 0,
            "mip_levels": 1,
            "mip_count_field": 0,
            "BGRA_masks": ["0x00FF0000", "0x0000FF00", "0x000000FF", "0xFF000000"],
            "texture_caps": "0x1000",
            "expected_dimensions": [EXPECTED_WIDTH, EXPECTED_HEIGHT],
            "expected_bytes_per_file": EXPECTED_SIZE,
        },
        "contact_sheets": [
            {"path": native_rel, "dimensions": [native.width, native.height], "decoded_from_dds": True},
            {"path": nearest_rel, "dimensions": [nearest4.width, nearest4.height], "decoded_from_dds": True, "scaling": "4x nearest-neighbour"},
        ],
        "entries": entries,
    }
    audit_path = PACKAGE / "evidence/dds_roundtrip_audit.json"
    write_json(audit_path, audit)
    inventory_path = PACKAGE / "evidence/output_inventory.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    by_slot = {e["slot"]: e for e in entries}
    for item in inventory["items"]:
        item["candidate_dds"] = by_slot[item["slot"]]["candidate_dds"]
        item["candidate_dds_bytes"] = by_slot[item["slot"]]["dds_bytes"]
        item["candidate_dds_sha256"] = by_slot[item["slot"]]["dds_sha256"]
        item["decoded_rgba_pixel_sha256"] = by_slot[item["slot"]]["decoded_rgba_pixel_sha256"]
        item["dds_roundtrip_exact"] = True
    inventory["status"] = "eight source masters and 156x210 previews parent-approved; eight isolated candidate DDS files passed BGRA32/header/opacity/unique-RGBA/pixel-roundtrip review; parent final DDS review pending; no runtime installation"
    write_json(inventory_path, inventory)
    call_log_path = PACKAGE / "evidence/imagegen_call_log.json"
    call_log = json.loads(call_log_path.read_text(encoding="utf-8"))
    for call in call_log["calls"]:
        call["status_after_generation"] = "source/framing parent-approved; candidate DDS technically reviewed; parent final DDS review pending; no runtime copy"
    write_json(call_log_path, call_log)
    print(json.dumps({
        "audit": str(audit_path),
        "status": audit["status"],
        "entries": entries,
        "contact_sheets": audit["contact_sheets"],
    }, indent=2))

if __name__ == "__main__":
    main()
