#!/usr/bin/env python3
"""Strictly validate staged AOX DDS headers, alpha, dimensions and pixel roundtrips."""
from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image


WORK = Path("docs/assets/005_soviet_collapse/gfx_fix_aox")
SELECTION = json.loads((WORK / "notes/candidate_selection.json").read_text(encoding="utf-8"))
INVENTORY = json.loads((WORK / "notes/aox_source_inventory.json").read_text(encoding="utf-8"))
PNG_BY_SUFFIX = {item["focus_suffix"]: item for item in SELECTION["assets"]}
OLD_BY_SUFFIX = {item["suffix"]: item for item in INVENTORY["assets"]}
TARGET = (94, 86)
EXPECTED_LENGTH = 128 + TARGET[0] * TARGET[1] * 4
EXPECTED_FLAGS = 0x0000100F
EXPECTED_MASKS = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
REPORT = WORK / "notes/dds_roundtrip_report.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    records: list[dict] = []
    failures: list[str] = []
    for old in sorted(INVENTORY["assets"], key=lambda row: row["suffix"]):
        suffix = old["suffix"]
        selected = PNG_BY_SUFFIX[suffix]
        png_path = Path(selected["processed_png"])
        dds_path = Path(selected["staged_dds"])
        png_raw = png_path.read_bytes()
        dds_raw = dds_path.read_bytes()
        checks: dict[str, bool] = {}
        checks["magic"] = dds_raw[:4] == b"DDS "
        checks["header_size"] = struct.unpack_from("<I", dds_raw, 4)[0] == 124
        checks["header_flags"] = struct.unpack_from("<I", dds_raw, 8)[0] == EXPECTED_FLAGS
        height = struct.unpack_from("<I", dds_raw, 12)[0]
        width = struct.unpack_from("<I", dds_raw, 16)[0]
        checks["dimensions"] = (width, height) == TARGET
        checks["pitch"] = struct.unpack_from("<I", dds_raw, 20)[0] == TARGET[0] * 4
        checks["depth_zero"] = struct.unpack_from("<I", dds_raw, 24)[0] == 0
        checks["mipmap_count_zero"] = struct.unpack_from("<I", dds_raw, 28)[0] == 0
        pf_size, pf_flags, fourcc, bits, red, green, blue, alpha = struct.unpack_from(
            "<II4sIIIII", dds_raw, 76
        )
        checks["pixel_format"] = (
            pf_size == 32
            and pf_flags == 65
            and fourcc == b"\x00\x00\x00\x00"
            and bits == 32
            and (red, green, blue, alpha) == EXPECTED_MASKS
        )
        checks["texture_caps"] = struct.unpack_from("<I", dds_raw, 108)[0] == 0x1000
        checks["no_caps2"] = struct.unpack_from("<I", dds_raw, 112)[0] == 0
        checks["exact_length"] = len(dds_raw) == EXPECTED_LENGTH
        png = Image.open(png_path).convert("RGBA")
        dds_image = Image.open(dds_path)
        decoded = dds_image.convert("RGBA")
        checks["png_dimensions"] = png.size == TARGET
        checks["dds_decoder_dimensions"] = decoded.size == TARGET
        checks["pixel_roundtrip_equal"] = png.tobytes() == decoded.tobytes()
        png_alpha = png.getchannel("A")
        dds_alpha = decoded.getchannel("A")
        checks["alpha_roundtrip_equal"] = png_alpha.tobytes() == dds_alpha.tobytes()
        checks["transparent_corners"] = all(
            png_alpha.getpixel(point) == 0
            for point in ((0, 0), (TARGET[0] - 1, 0), (0, TARGET[1] - 1), (TARGET[0] - 1, TARGET[1] - 1))
        )
        checks["alpha_has_visible_subject"] = png_alpha.getextrema()[1] == 255
        checks["registered_runtime_path"] = selected["runtime_dds"] == old["runtime_dds"]
        failed = [name for name, passed in checks.items() if not passed]
        if failed:
            failures.append(f"{suffix}: {', '.join(failed)}")
        records.append(
            {
                "focus_id": old["focus_id"],
                "suffix": suffix,
                "sprite": old["sprite"],
                "shine_sprite": old["shine_sprite"],
                "processed_png": str(png_path),
                "staged_dds": str(dds_path),
                "runtime_dds": selected["runtime_dds"],
                "dds_dimensions": [width, height],
                "dds_file_size": len(dds_raw),
                "expected_file_size": EXPECTED_LENGTH,
                "dds_sha256": sha(dds_raw),
                "processed_png_sha256": sha(png_raw),
                "processed_pixel_sha256": sha(png.tobytes()),
                "decoded_dds_pixel_sha256": sha(decoded.tobytes()),
                "png_alpha_extrema": list(png_alpha.getextrema()),
                "dds_alpha_extrema": list(dds_alpha.getextrema()),
                "pixel_equality": checks["pixel_roundtrip_equal"],
                "checks": checks,
                "status": "pass" if not failed else "failed",
            }
        )
    report = {
        "converter": ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py",
        "target_dimensions": list(TARGET),
        "expected_legacy_bgra_header": {
            "magic": "DDS ",
            "header_size": 124,
            "header_flags": EXPECTED_FLAGS,
            "pixel_format_size": 32,
            "pixel_format_flags": 65,
            "fourcc": "0",
            "bits_per_pixel": 32,
            "masks": list(EXPECTED_MASKS),
            "texture_caps": 0x1000,
            "mipmaps": 0,
            "expected_total_length": EXPECTED_LENGTH,
        },
        "asset_count": len(records),
        "passed": not failures and len(records) == 47,
        "failures": failures,
        "assets": records,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"dds_roundtrips={len(records)} passed={report['passed']} report={REPORT}")
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
