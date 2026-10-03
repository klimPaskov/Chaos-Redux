"""Verify Event 014 Africa DDS headers and exact processed-PNG round trips."""

from __future__ import annotations

import hashlib
import json
import struct
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
SIZE = (156, 210)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> None:
    entries = []
    decoded_images = []
    for slot in SLOTS:
        stem = f"leader_{slot}_warlord_africa"
        png_path = ROOT / "processed_png" / f"{stem}_156x210.png"
        dds_path = ROOT / "candidate_dds" / f"{stem}.dds"
        dds_data = dds_path.read_bytes()
        if dds_data[:4] != b"DDS ":
            raise ValueError(f"Invalid DDS magic: {dds_path}")
        header = struct.unpack_from("<31I", dds_data, 4)
        dds_header_size, flags, height, width, pitch = header[:5]
        mip_count = header[6]
        pf_size, pf_flags, fourcc, bit_count, red, green, blue, alpha = struct.unpack_from("<8I", dds_data, 76)
        caps = struct.unpack_from("<I", dds_data, 108)[0]
        if (width, height) != SIZE:
            raise ValueError(f"DDS dimensions are {(width, height)}, expected {SIZE}: {dds_path}")
        if dds_header_size != 124 or pf_size != 32:
            raise ValueError(f"Unexpected legacy DDS header size: {dds_path}")
        if (pf_flags, fourcc, bit_count, red, green, blue, alpha) != (
            0x41,
            0,
            32,
            0x00FF0000,
            0x0000FF00,
            0x000000FF,
            0xFF000000,
        ):
            raise ValueError(f"DDS is not uncompressed BGRA32: {dds_path}")
        if pitch != width * 4 or len(dds_data) != 128 + width * height * 4:
            raise ValueError(f"Unexpected DDS pitch or byte length: {dds_path}")
        if caps != 0x1000 or (flags & 0x20000):
            raise ValueError(f"Unexpected texture caps or mip-chain flag: {dds_path}")

        with Image.open(png_path) as source:
            source_rgba = source.convert("RGBA")
        with Image.open(dds_path) as decoded:
            decoded.load()
            decoded_rgba = decoded.convert("RGBA")
        exact = source_rgba.tobytes() == decoded_rgba.tobytes()
        if not exact:
            raise ValueError(f"DDS decoded pixels differ from processed PNG: {slot}")
        decoded_images.append((slot, decoded_rgba.copy()))
        entries.append(
            {
                "slot": slot,
                "processed_png": png_path.relative_to(ROOT).as_posix(),
                "processed_png_sha256": sha256(png_path.read_bytes()),
                "candidate_dds": dds_path.relative_to(ROOT).as_posix(),
                "candidate_dds_dimensions": [width, height],
                "candidate_dds_bytes": len(dds_data),
                "candidate_dds_sha256": sha256(dds_data),
                "dds_header": {
                    "legacy_header_bytes": 128,
                    "pixel_format": "BGRA32 / B8G8R8A8_UNORM masks",
                    "rgb_bit_count": bit_count,
                    "pitch_bytes": pitch,
                    "mip_count_field": mip_count,
                    "mip_chain": False,
                    "texture_caps": caps,
                },
                "decoded_mode": decoded_rgba.mode,
                "decoded_pixel_sha256": sha256(decoded_rgba.tobytes()),
                "exact_processed_png_roundtrip": exact,
                "alpha_is_opaque": decoded_rgba.getchannel("A").getextrema() == (255, 255),
            }
        )

    review_dir = ROOT / "review"
    native_path = review_dir / "africa_dds_decoded_native_4x2_contact_sheet.png"
    nearest_path = review_dir / "africa_dds_decoded_nearest4_4x2_contact_sheet.png"
    if native_path.exists() or nearest_path.exists():
        raise FileExistsError("Refusing to overwrite DDS round-trip contact sheets")
    native = Image.new("RGB", (SIZE[0] * 4, SIZE[1] * 2))
    nearest = Image.new("RGB", (SIZE[0] * 16, SIZE[1] * 8))
    for index, (_, image) in enumerate(decoded_images):
        column, row = index % 4, index // 4
        native.paste(image.convert("RGB"), (column * SIZE[0], row * SIZE[1]))
        enlarged = image.resize((SIZE[0] * 4, SIZE[1] * 4), Image.Resampling.NEAREST).convert("RGB")
        nearest.paste(enlarged, (column * SIZE[0] * 4, row * SIZE[1] * 4))
    native.save(native_path, format="PNG", optimize=False)
    nearest.save(nearest_path, format="PNG", optimize=False)

    audit = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "conversion_command": "python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <156x210.png> --output <candidate_dds.dds> --width 156 --height 210",
        "converter_backend": "FFmpeg BGRA fallback inside the required converter; texconv was not available on PATH",
        "all_dds_are_bgra32_single_level": True,
        "all_dds_roundtrip_exact": all(entry["exact_processed_png_roundtrip"] for entry in entries),
        "distinct_decoded_pixel_hashes": len({entry["decoded_pixel_sha256"] for entry in entries}),
        "decoded_native_contact_sheet": native_path.relative_to(ROOT).as_posix(),
        "decoded_nearest4_contact_sheet": nearest_path.relative_to(ROOT).as_posix(),
        "entries": entries,
    }
    audit_path = ROOT / "route_log" / "dds_roundtrip_audit.json"
    if audit_path.exists():
        raise FileExistsError(f"Refusing to overwrite DDS round-trip audit: {audit_path}")
    audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "audit": audit_path.as_posix(),
                "outputs": len(entries),
                "all_bgra32_single_level": audit["all_dds_are_bgra32_single_level"],
                "all_roundtrip_exact": audit["all_dds_roundtrip_exact"],
                "unique_pixels": audit["distinct_decoded_pixel_hashes"],
            }
        )
    )


if __name__ == "__main__":
    main()
