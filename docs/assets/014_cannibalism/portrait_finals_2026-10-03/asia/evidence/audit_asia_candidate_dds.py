import hashlib
import json
import os
import shutil
import struct
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/asia"
TARGET = (156, 210)
INSTALL_RECEIPT_PATH = BASE / "evidence" / "runtime_install_receipt.json"
INSTALL_RECEIPT = json.loads(INSTALL_RECEIPT_PATH.read_text(encoding="utf-8")) if INSTALL_RECEIPT_PATH.exists() else None
INSTALLED_BY_SLOT = {item["slot"]: item for item in INSTALL_RECEIPT["installed_targets"]} if INSTALL_RECEIPT else {}
SLOTS = {
    "CBA": "leader_CBA_warlord_asia",
    "CBB": "leader_CBB_warlord_asia",
    "CBC": "leader_CBC_warlord_asia",
    "CBD": "leader_CBD_warlord_asia",
    "CBE": "leader_CBE_warlord_asia",
    "CBF": "leader_CBF_warlord_asia",
    "CBG": "leader_CBG_warlord_asia",
    "CBH": "leader_CBH_warlord_asia",
}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def file_record(path):
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "sha256": sha256(data),
    }


def u32(data, offset):
    return struct.unpack_from("<I", data, offset)[0]


dds_dir = BASE / "candidate_dds"
review_dir = BASE / "review"
review_dir.mkdir(parents=True, exist_ok=True)
records = []
decoded_images = []
failures = []

for slot, basename in SLOTS.items():
    png_path = BASE / "processed_png" / f"{basename}_156x210.png"
    dds_path = dds_dir / f"{basename}.dds"
    dds = dds_path.read_bytes()
    png = Image.open(png_path).convert("RGBA")
    png.load()

    header_ok = len(dds) >= 128 and dds[:4] == b"DDS "
    header_size = u32(dds, 4) if header_ok else None
    flags = u32(dds, 8) if header_ok else None
    height = u32(dds, 12) if header_ok else None
    width = u32(dds, 16) if header_ok else None
    pitch = u32(dds, 20) if header_ok else None
    depth = u32(dds, 24) if header_ok else None
    mipmap_count = u32(dds, 28) if header_ok else None
    pf_size = u32(dds, 76) if header_ok else None
    pf_flags = u32(dds, 80) if header_ok else None
    fourcc = u32(dds, 84) if header_ok else None
    bit_count = u32(dds, 88) if header_ok else None
    red_mask = u32(dds, 92) if header_ok else None
    green_mask = u32(dds, 96) if header_ok else None
    blue_mask = u32(dds, 100) if header_ok else None
    alpha_mask = u32(dds, 104) if header_ok else None
    caps = u32(dds, 108) if header_ok else None
    expected_bytes = 128 + TARGET[0] * TARGET[1] * 4
    payload = dds[128:] if header_ok else b""
    payload_size_ok = len(dds) == expected_bytes and len(payload) == TARGET[0] * TARGET[1] * 4

    decoded = None
    if header_ok and width == TARGET[0] and height == TARGET[1] and payload_size_ok:
        decoded = Image.frombytes("RGBA", (width, height), payload, "raw", "BGRA")
    else:
        failures.append(f"{slot}: DDS header or payload dimensions/length invalid")

    alpha_range = list(decoded.getchannel("A").getextrema()) if decoded else None
    pixel_equal = bool(decoded and decoded.tobytes() == png.tobytes())
    pixel_hash = sha256(decoded.tobytes()) if decoded else None
    unique_header_ok = (
        header_ok
        and header_size == 124
        and (flags & 0x100F) == 0x100F
        and pitch == TARGET[0] * 4
        and depth == 0
        and mipmap_count in (0, 1)
        and pf_size == 32
        and pf_flags == 65
        and fourcc == 0
        and bit_count == 32
        and red_mask == 0x00FF0000
        and green_mask == 0x0000FF00
        and blue_mask == 0x000000FF
        and alpha_mask == 0xFF000000
        and caps is not None
        and (caps & 0x1000) == 0x1000
    )
    if not unique_header_ok:
        failures.append(f"{slot}: legacy single-level BGRA32 header fields invalid")
    if not decoded or decoded.size != TARGET:
        failures.append(f"{slot}: decoded DDS is not 156x210")
    if alpha_range != [255, 255]:
        failures.append(f"{slot}: decoded alpha is not fully opaque: {alpha_range}")
    if not pixel_equal:
        failures.append(f"{slot}: decoded DDS RGBA pixels differ from processed PNG")

    record = {
        "slot": slot,
        "png": file_record(png_path),
        "candidate_dds": file_record(dds_path),
        "format": "legacy uncompressed BGRA32 / B8G8R8A8_UNORM (unsigned 8.8.8.8)",
        "header": {
            "magic": dds[:4].decode("ascii", errors="replace") if header_ok else None,
            "dds_file_bytes": len(dds),
            "dds_header_and_pixel_start_bytes": 128,
            "dds_header_size": header_size,
            "flags": flags,
            "width": width,
            "height": height,
            "pitch": pitch,
            "depth": depth,
            "mipmap_count_field": mipmap_count,
            "pixel_format_size": pf_size,
            "pixel_format_flags": pf_flags,
            "fourcc": fourcc,
            "rgb_bit_count": bit_count,
            "red_mask": red_mask,
            "green_mask": green_mask,
            "blue_mask": blue_mask,
            "alpha_mask": alpha_mask,
            "caps": caps,
            "single_level_payload_bytes": len(payload),
            "expected_total_bytes": expected_bytes,
            "actual_total_bytes": len(dds),
            "header_valid": bool(unique_header_ok),
        },
        "decoded_dimensions": list(decoded.size) if decoded else None,
        "decoded_mode": decoded.mode if decoded else None,
        "decoded_alpha_min_max": alpha_range,
        "decoded_rgba_sha256": pixel_hash,
        "decoded_rgba_exactly_matches_processed_png": pixel_equal,
        "runtime_install_state": (
            "parent-approved and installed; runtime SHA-256 matches candidate"
            if slot in INSTALLED_BY_SLOT
            else "not copied; exact parent DDS review pending"
        ),
        "runtime_path": INSTALLED_BY_SLOT[slot]["runtime_path"] if slot in INSTALLED_BY_SLOT else None,
        "runtime_installed_sha256": INSTALLED_BY_SLOT[slot]["installed"]["sha256"] if slot in INSTALLED_BY_SLOT else None,
    }
    records.append(record)
    if decoded:
        decoded_images.append((slot, decoded))

unique_hashes = {r["decoded_rgba_sha256"] for r in records if r["decoded_rgba_sha256"]}
all_unique = len(unique_hashes) == len(SLOTS)
if not all_unique:
    failures.append("Decoded RGBA pixel buffers are not unique across all eight candidates")


def make_sheet(images, scale, filename):
    cols, rows = 4, 2
    w, h = TARGET[0] * scale, TARGET[1] * scale
    sheet = Image.new("RGB", (cols * w, rows * h), (26, 29, 30))
    for index, (_, rgba) in enumerate(images):
        tile = rgba.convert("RGB")
        if scale != 1:
            tile = tile.resize((w, h), Image.Resampling.NEAREST)
        sheet.paste(tile, ((index % cols) * w, (index // cols) * h))
    path = review_dir / filename
    sheet.save(path, format="PNG", optimize=False)
    return sheet, file_record(path)


native_sheet, native_sheet_record = make_sheet(
    decoded_images, 1, "asian_dds_decoded_native_4x2_contact_sheet.png"
)
nearest_sheet, nearest_sheet_record = make_sheet(
    decoded_images, 4, "asian_dds_decoded_nearest4_4x2_contact_sheet.png"
)
png_native_sheet = Image.open(review_dir / "asian_native_4x2_contact_sheet.png").convert("RGB")
png_nearest_sheet = Image.open(review_dir / "asian_nearest4_4x2_contact_sheet.png").convert("RGB")
sheet_native_equal = native_sheet.tobytes() == png_native_sheet.tobytes()
sheet_nearest_equal = nearest_sheet.tobytes() == png_nearest_sheet.tobytes()
if not sheet_native_equal:
    failures.append("DDS-decoded native contact sheet differs from the processed-PNG sheet")
if not sheet_nearest_equal:
    failures.append("DDS-decoded 4x nearest contact sheet differs from the processed-PNG sheet")

texconv_env = any(os.environ.get(name) for name in ("TEXCONV_PATH", "TEXCONV_EXE", "TEXCONV_DOCKER_IMAGE"))
texconv_path = shutil.which("texconv") or shutil.which("texconv.exe")
ffmpeg_path = shutil.which("ffmpeg")
if texconv_env or texconv_path:
    backend = "DirectXTex texconv selected by the required converter"
else:
    backend = "required converter built-in FFmpeg BGRA fallback"
    if not ffmpeg_path:
        failures.append("Converter backend could not be resolved to texconv or FFmpeg")

audit = {
    "date": "2026-10-03",
    "conversion_tool": ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py",
    "conversion_backend": backend,
    "texconv_found": bool(texconv_env or texconv_path),
    "ffmpeg_path": ffmpeg_path,
    "target_dimensions": list(TARGET),
    "candidate_dds_folder": "docs/assets/014_cannibalism/portrait_finals_2026-10-03/asia/candidate_dds",
    "candidate_count": len(records),
    "all_dds_headers_valid": all(r["header"]["header_valid"] for r in records),
    "all_decoded_dimensions_156x210": all(r["decoded_dimensions"] == list(TARGET) for r in records),
    "all_decoded_pixels_exactly_match_png": all(r["decoded_rgba_exactly_matches_processed_png"] for r in records),
    "all_decoded_rgba_opaque": all(r["decoded_alpha_min_max"] == [255, 255] for r in records),
    "unique_decoded_rgba_hash_count": len(unique_hashes),
    "all_eight_decoded_pixel_buffers_unique": all_unique,
    "decoded_native_contact_sheet": native_sheet_record,
    "decoded_nearest4_contact_sheet": nearest_sheet_record,
    "decoded_sheets_match_processed_png_sheets": {
        "native": sheet_native_equal,
        "nearest4": sheet_nearest_equal,
    },
    "runtime_copy": (
        "parent-approved and installed at the eight existing Asia runtime paths; see evidence/runtime_install_receipt.json"
        if INSTALL_RECEIPT
        else "not performed; exact parent DDS review pending"
    ),
    "runtime_install_receipt": "evidence/runtime_install_receipt.json" if INSTALL_RECEIPT else None,
    "failures": failures,
    "assets": records,
}
out = BASE / "evidence" / "dds_roundtrip_audit.json"
out.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
print(f"dds={len(records)} headers={sum(r['header']['header_valid'] for r in records)}/8 exact_png_rgba={sum(r['decoded_rgba_exactly_matches_processed_png'] for r in records)}/8 opaque={sum(r['decoded_alpha_min_max']==[255,255] for r in records)}/8 unique={len(unique_hashes)}/8")
print(f"native_sheet={native_sheet_record['path']} {native_sheet.size} matches_png={sheet_native_equal}")
print(f"nearest4_sheet={nearest_sheet_record['path']} {nearest_sheet.size} matches_png={sheet_nearest_equal}")
print(f"backend={backend}")
if failures:
    for failure in failures:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
