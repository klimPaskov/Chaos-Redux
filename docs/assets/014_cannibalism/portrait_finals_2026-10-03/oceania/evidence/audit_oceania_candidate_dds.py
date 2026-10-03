from __future__ import annotations

import hashlib
import json
import shutil
import struct
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


BASE = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE / "processed_png"
DDS_DIR = BASE / "candidate_dds"
REVIEW_DIR = BASE / "review"
EVIDENCE_DIR = BASE / "evidence"
TAGS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
TARGET = (156, 210)
HEADER_BYTES = 128


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def decode_bgra_payload(payload: bytes, size: tuple[int, int]) -> bytes:
    rgba = bytearray(len(payload))
    for offset in range(0, len(payload), 4):
        blue, green, red, alpha = payload[offset : offset + 4]
        rgba[offset : offset + 4] = bytes((red, green, blue, alpha))
    image = Image.frombytes("RGBA", size, bytes(rgba))
    return image.tobytes()


def main() -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    decoded_images: list[Image.Image] = []
    for tag in TAGS:
        png_path = PROCESSED_DIR / f"leader_{tag}_warlord_oceania_156x210.png"
        dds_path = DDS_DIR / f"leader_{tag}_warlord_oceania.dds"
        if not png_path.is_file() or not dds_path.is_file():
            raise FileNotFoundError(f"{tag}: processed PNG or candidate DDS is missing")

        with Image.open(png_path) as opened_png:
            png = opened_png.convert("RGBA")
            if png.size != TARGET:
                raise ValueError(f"{tag}: PNG dimensions are {png.size}, expected {TARGET}")
            png_rgba = png.tobytes()
            png_alpha = png.getchannel("A").getextrema()
            if png_alpha != (255, 255):
                raise ValueError(f"{tag}: PNG is not fully opaque: alpha={png_alpha}")

        data = dds_path.read_bytes()
        if data[:4] != b"DDS ":
            raise ValueError(f"{tag}: missing DDS magic")
        if len(data) < HEADER_BYTES:
            raise ValueError(f"{tag}: truncated DDS header")
        height = read_u32(data, 12)
        width = read_u32(data, 16)
        pitch = read_u32(data, 20)
        mipmap_count = read_u32(data, 28)
        pf_size = read_u32(data, 76)
        pf_flags = read_u32(data, 80)
        fourcc = data[84:88]
        bit_count = read_u32(data, 88)
        masks = [read_u32(data, offset) for offset in (92, 96, 100, 104)]
        caps = read_u32(data, 108)
        expected_size = HEADER_BYTES + width * height * 4
        header = {
            "magic": data[:4].decode("ascii"),
            "file_bytes": len(data),
            "header_bytes": HEADER_BYTES,
            "dds_header_size": read_u32(data, 4),
            "flags": read_u32(data, 8),
            "width": width,
            "height": height,
            "pitch": pitch,
            "mipmap_count_field": mipmap_count,
            "pixel_format_size": pf_size,
            "pixel_format_flags": pf_flags,
            "fourcc": fourcc.hex(),
            "rgb_bit_count": bit_count,
            "red_mask": masks[0],
            "green_mask": masks[1],
            "blue_mask": masks[2],
            "alpha_mask": masks[3],
            "caps": caps,
            "expected_file_bytes": expected_size,
        }
        if (
            width != TARGET[0]
            or height != TARGET[1]
            or len(data) != expected_size
            or read_u32(data, 4) != 124
            or pitch != width * 4
            or mipmap_count != 0
            or pf_size != 32
            or pf_flags != 65
            or fourcc != b"\x00\x00\x00\x00"
            or bit_count != 32
            or masks != [0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000]
            or caps != 0x1000
        ):
            raise ValueError(f"{tag}: invalid legacy uncompressed BGRA32 one-level DDS header: {header}")

        decoded_rgba = decode_bgra_payload(data[HEADER_BYTES:], TARGET)
        decoded_alpha = decoded_rgba[3::4]
        alpha_min = min(decoded_alpha)
        alpha_max = max(decoded_alpha)
        if (alpha_min, alpha_max) != (255, 255):
            raise ValueError(f"{tag}: decoded DDS is not opaque: alpha={(alpha_min, alpha_max)}")
        exact_match = decoded_rgba == png_rgba
        if not exact_match:
            raise ValueError(f"{tag}: decoded DDS pixels differ from the processed PNG")

        decoded_image = Image.frombytes("RGBA", TARGET, decoded_rgba).convert("RGB")
        decoded_images.append(decoded_image)
        rows.append(
            {
                "slot": tag,
                "png_path": png_path.relative_to(BASE).as_posix(),
                "png_bytes": png_path.stat().st_size,
                "png_sha256": sha256(png_path.read_bytes()),
                "png_rgba_sha256": sha256(png_rgba),
                "candidate_dds_path": dds_path.relative_to(BASE).as_posix(),
                "candidate_dds_bytes": len(data),
                "candidate_dds_sha256": sha256(data),
                "format": "legacy uncompressed BGRA32 / B8G8R8A8_UNORM",
                "header": header,
                "decoded_dimensions": [width, height],
                "decoded_mode": "RGBA",
                "decoded_alpha_min_max": [alpha_min, alpha_max],
                "decoded_rgba_sha256": sha256(decoded_rgba),
                "decoded_rgba_exactly_matches_processed_png": exact_match,
                "runtime_state": "isolated candidate only; runtime promotion awaits parent final DDS review",
            }
        )

    native_sheet = Image.new("RGB", (TARGET[0] * 4, TARGET[1] * 2), (0, 0, 0))
    for index, image in enumerate(decoded_images):
        native_sheet.paste(image, ((index % 4) * TARGET[0], (index // 4) * TARGET[1]))
    decoded_sheet_path = REVIEW_DIR / "oceania_dds_decoded_native_4x2_contact_sheet.png"
    native_sheet.save(decoded_sheet_path, format="PNG", optimize=False)

    with Image.open(REVIEW_DIR / "oceania_native_4x2_contact_sheet.png") as expected_sheet:
        expected_sheet = expected_sheet.convert("RGB")
        contact_matches = expected_sheet.size == native_sheet.size and expected_sheet.tobytes() == native_sheet.tobytes()
    if not contact_matches:
        raise ValueError("Decoded DDS native contact sheet differs from the processed-PNG native contact sheet")

    source_hashes = [str(row["png_rgba_sha256"]) for row in rows]
    decoded_hashes = [str(row["decoded_rgba_sha256"]) for row in rows]
    if len(set(source_hashes)) != len(rows) or len(set(decoded_hashes)) != len(rows):
        raise ValueError("Processed PNG or decoded DDS pixel buffers are not unique")

    texconv_found = shutil.which("texconv") or shutil.which("texconv.exe")
    docker_image = __import__("os").environ.get("TEXCONV_DOCKER_IMAGE")
    backend = "texconv" if texconv_found else "TEXCONV_DOCKER_IMAGE" if docker_image else "built-in FFmpeg BGRA fallback"
    result = {
        "date": "2026-10-03",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "conversion_tool": ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py",
        "conversion_backend": backend,
        "target_dimensions": list(TARGET),
        "candidate_dds_folder": "candidate_dds",
        "candidate_count": len(rows),
        "all_dds_headers_valid": True,
        "all_decoded_dimensions_156x210": True,
        "all_decoded_pixels_exactly_match_png": True,
        "all_decoded_rgba_opaque": True,
        "unique_decoded_rgba_hash_count": len(set(decoded_hashes)),
        "all_eight_decoded_pixel_buffers_unique": len(set(decoded_hashes)) == len(rows),
        "decoded_native_contact_sheet": {
            "path": decoded_sheet_path.relative_to(BASE).as_posix(),
            "dimensions": list(native_sheet.size),
            "bytes": decoded_sheet_path.stat().st_size,
            "sha256": sha256(decoded_sheet_path.read_bytes()),
            "pixel_equal_to_processed_png_native_sheet": contact_matches,
        },
        "runtime_copy": "not performed; parent final DDS review is pending",
        "failures": [],
        "assets": rows,
    }
    (EVIDENCE_DIR / "dds_roundtrip_audit.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "backend": backend,
                "candidate_count": len(rows),
                "headers_valid": True,
                "exact_png_roundtrip": True,
                "opaque_alpha": True,
                "unique_decoded_rgba_count": len(set(decoded_hashes)),
                "decoded_native_sheet_matches_png_sheet": contact_matches,
                "decoded_sheet_dimensions": list(native_sheet.size),
            }
        )
    )


if __name__ == "__main__":
    main()
