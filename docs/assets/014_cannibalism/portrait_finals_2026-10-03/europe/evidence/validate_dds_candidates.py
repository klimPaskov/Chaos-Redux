"""Validate converter-produced candidate DDS files and their pixel round trips."""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REPO = next(parent for parent in ROOT.parents if (parent / "interface/014_cannibalism.gfx").is_file())
PROCESSED = ROOT / "processed_png"
DDS_DIR = ROOT / "candidate_dds"
REVIEW = ROOT / "review"
EVIDENCE = ROOT / "evidence"
ITEMS = [
    ("CBA", "leader_CBA_warlord_europe_v02_156x210.png", "leader_CBA_warlord_europe.dds", "gfx/leaders/014_cannibalism/leader_CBA_warlord_europe.dds", "BAAC09CBECE6A013BC0058536A89799A021736BFB4D5882CA4FF0093CFBDE305"),
    ("CBB", "leader_CBB_warlord_europe_156x210.png", "leader_CBB_warlord_europe.dds", "gfx/leaders/014_cannibalism/leader_CBB_warlord_europe.dds", "7F4DB437DCC4308DB91E24AA0CAB533EFE16899E24CEDD8E6A80EF6330C25BAC"),
    ("CBC", "leader_CBC_warlord_156x210.png", "leader_CBC_warlord.dds", "gfx/leaders/014_cannibalism/leader_CBC_warlord.dds", "48E341F4CEF25E001443D1F1F03A5B61EA4B22E2A99CF580EEF7DFE4B6B86DD1"),
    ("CBD", "leader_CBD_warlord_europe_156x210.png", "leader_CBD_warlord_europe.dds", "gfx/leaders/014_cannibalism/leader_CBD_warlord_europe.dds", "C8CD84ACF35B1CA3D4ED33C45175BF84750866F145379C4EF9F560775769DBA9"),
    ("CBE", "leader_CBE_warlord_156x210.png", "leader_CBE_warlord.dds", "gfx/leaders/014_cannibalism/leader_CBE_warlord.dds", "AD551FC190B873D93FBE9FE17907D285D6C3DAC5722CDEA7EAD96370ED190C10"),
    ("CBF", "leader_CBF_warlord_156x210.png", "leader_CBF_warlord.dds", "gfx/leaders/014_cannibalism/leader_CBF_warlord.dds", "0E2FABEF510FE103453E69DDB4F1B8E5FD66F7871D7FF60D6D63EEC6E4923970"),
    ("CBG", "leader_CBG_warlord_europe_156x210.png", "leader_CBG_warlord_europe.dds", "gfx/leaders/014_cannibalism/leader_CBG_warlord_europe.dds", "40E93A509AADE8C90BC7676E7D34EED2928165FDF562A14170C3E40164E3E7FE"),
    ("CBH", "leader_CBH_warlord_156x210.png", "leader_CBH_warlord.dds", "gfx/leaders/014_cannibalism/leader_CBH_warlord.dds", "2E7401457A4C9E3DF428A85C392137F623BD6AD56864783ADF0104CF58E71896"),
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes())


def main() -> None:
    records = []
    decoded_images = []
    decoded_pixel_hashes = set()
    for slot, png_name, dds_name, runtime_rel, runtime_hash_before in ITEMS:
        png_path = PROCESSED / png_name
        dds_path = DDS_DIR / dds_name
        png_bytes = png_path.read_bytes()
        dds_bytes = dds_path.read_bytes()
        if dds_bytes[:4] != b"DDS " or struct.unpack_from("<I", dds_bytes, 4)[0] != 124:
            raise ValueError(f"{slot}: invalid DDS magic/header size")
        height, width = struct.unpack_from("<II", dds_bytes, 12)
        pitch = struct.unpack_from("<I", dds_bytes, 20)[0]
        mip_count = struct.unpack_from("<I", dds_bytes, 28)[0]
        pf_size, pf_flags, fourcc, bitcount, rmask, gmask, bmask, amask = struct.unpack_from("<8I", dds_bytes, 76)
        caps = struct.unpack_from("<I", dds_bytes, 108)[0]
        expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
        if (width, height) != (156, 210) or pitch != 156 * 4:
            raise ValueError(f"{slot}: unexpected DDS dimensions/pitch {(width, height, pitch)}")
        if (pf_size, pf_flags, fourcc, bitcount, rmask, gmask, bmask, amask) != (32, 65, 0, 32, *expected_masks):
            raise ValueError(f"{slot}: unexpected BGRA32 pixel format")
        if caps != 0x1000 or mip_count not in (0, 1) or len(dds_bytes) != 128 + 156 * 210 * 4:
            raise ValueError(f"{slot}: invalid texture caps, mip count, or file length")
        payload = dds_bytes[128:]
        alpha = payload[3::4]
        alpha_min, alpha_max = min(alpha), max(alpha)
        if (alpha_min, alpha_max) != (255, 255):
            raise ValueError(f"{slot}: opaque portrait DDS has alpha range {(alpha_min, alpha_max)}")
        decoded = Image.frombytes("RGBA", (width, height), payload, "raw", "BGRA")
        with Image.open(png_path) as opened:
            png_rgba = opened.convert("RGBA")
        if decoded.tobytes() != png_rgba.tobytes():
            raise ValueError(f"{slot}: decoded DDS pixels differ from processed PNG pixels")
        decoded_pixel_hash = sha256(decoded.tobytes())
        decoded_pixel_hashes.add(decoded_pixel_hash)
        decoded_images.append((slot, decoded.convert("RGB")))
        runtime_path = REPO / runtime_rel
        runtime_hash_after = file_sha(runtime_path)
        if runtime_hash_after != runtime_hash_before:
            raise ValueError(f"{slot}: existing runtime DDS changed during candidate production")
        records.append({
            "slot": slot,
            "processed_png_path": str(png_path.relative_to(ROOT)).replace("\\", "/"),
            "processed_png_sha256": file_sha(png_path),
            "candidate_dds_path": str(dds_path.relative_to(ROOT)).replace("\\", "/"),
            "candidate_dds_dimensions": [width, height],
            "candidate_dds_bytes": len(dds_bytes),
            "candidate_dds_sha256": file_sha(dds_path),
            "header": {"magic": "DDS ", "header_size": 124, "pixel_format_size": pf_size, "pixel_flags": pf_flags, "fourcc": fourcc, "bits_per_pixel": bitcount, "channel_masks_rgba": [rmask, gmask, bmask, amask], "pitch": pitch, "mip_count_field": mip_count, "caps": caps},
            "alpha_min_max": [alpha_min, alpha_max],
            "decoded_pixel_sha256": decoded_pixel_hash,
            "round_trip_exact_match_to_png": True,
            "existing_runtime_dds_path": runtime_rel,
            "existing_runtime_sha256_before": runtime_hash_before,
            "existing_runtime_sha256_after": runtime_hash_after,
            "runtime_untouched": True,
        })
    if len(decoded_pixel_hashes) != 8:
        raise ValueError("Candidate DDS decoded pixel buffers are not all unique")

    native = Image.new("RGB", (156 * 4, 210 * 2), (52, 52, 52))
    for index, (_, image) in enumerate(decoded_images):
        native.paste(image, ((index % 4) * 156, (index // 4) * 210))
    native_path = REVIEW / "europe_dds_decoded_native_4x2_contact_sheet.png"
    native.save(native_path, format="PNG", optimize=False)
    enlarged = native.resize((native.width * 4, native.height * 4), Image.Resampling.NEAREST)
    enlarged_path = REVIEW / "europe_dds_decoded_nearest4_4x2_contact_sheet.png"
    enlarged.save(enlarged_path, format="PNG", optimize=False)
    result = {
        "audit": "candidate DDS header, opacity, exact PNG round-trip, decoded-pixel uniqueness, and runtime preservation",
        "date": "2026-10-03",
        "converter": ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py",
        "backend": "the bundled converter's FFmpeg BGRA32 fallback; no texconv executable was found on PATH",
        "format": "legacy uncompressed BGRA32, opaque alpha 255, one image level, no mip chain",
        "candidate_count": len(records),
        "all_headers_valid": True,
        "all_png_round_trips_exact": True,
        "unique_decoded_dds_pixel_buffers": len(decoded_pixel_hashes),
        "all_runtime_files_unchanged": True,
        "records": records,
        "decoded_contact_sheets": [
            {"path": str(native_path.relative_to(ROOT)).replace("\\", "/"), "dimensions": list(native.size), "sha256": file_sha(native_path)},
            {"path": str(enlarged_path.relative_to(ROOT)).replace("\\", "/"), "dimensions": list(enlarged.size), "sha256": file_sha(enlarged_path)},
        ],
    }
    (EVIDENCE / "dds_roundtrip_audit.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidates": len(records), "unique_decoded_pixel_buffers": len(decoded_pixel_hashes), "runtime_unchanged": True}, indent=2))


if __name__ == "__main__":
    main()
