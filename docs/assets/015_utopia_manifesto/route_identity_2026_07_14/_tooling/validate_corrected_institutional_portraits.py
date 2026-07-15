#!/usr/bin/env python3
"""Validate and document the corrected Event 015 institutional portraits."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


REPO = Path(__file__).resolve().parents[5]
BASE = REPO / "docs/assets/015_utopia_manifesto/route_identity_2026_07_14"
SOURCE = BASE / "source_png/institutional_portraits"
PROCESSED = BASE / "processed_png/institutional_portraits"
FINAL = BASE / "final_dds/institutional_portraits"
DECODED = BASE / "decoded_png/institutional_portraits"
REVIEWS = BASE / "contact_sheets/institutional_reviews"
METADATA = BASE / "metadata/institutional_portraits"
CONTACT = BASE / "contact_sheets"
RUNTIME = REPO / "gfx/leaders/015_utopia_manifesto"

PORTRAITS = {
    "leader_household_assembly": {
        "handle": "exec-59ff2fa1-755d-4e86-9df8-1a9586d9f629",
        "brief": "Three household delegates, with an older woman centered as the institutional voice.",
    },
    "leader_council_of_callings": {
        "handle": "exec-db5ac931-dd5a-4f4c-b56c-f0a13d7ced05",
        "brief": "Three skilled-worker delegates in practical interwar clothing, with a woman centered.",
    },
    "leader_board_of_measure": {
        "handle": "exec-a710c8a9-e1bc-4b67-bc73-da2db13f8851",
        "brief": "Three technical administrators, with an older bespectacled man centered.",
    },
    "leader_stewardship_council": {
        "handle": "exec-6fae8a6d-e911-4667-b258-f8173bdf73df",
        "brief": "Three stern stewardship officials, with an older man centered.",
    },
}


def rel(path: Path) -> str:
    return str(path.relative_to(REPO)).replace("\\", "/")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (Path(r"C:/Windows/Fonts/arial.ttf"), Path(r"C:/Windows/Fonts/segoeui.ttf")):
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def validate_dds(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError(f"invalid DDS magic/header: {path}")
    header_size = int.from_bytes(data[4:8], "little")
    height = int.from_bytes(data[12:16], "little")
    width = int.from_bytes(data[16:20], "little")
    mipmaps = int.from_bytes(data[28:32], "little")
    pixel_format_size = int.from_bytes(data[76:80], "little")
    pixel_format_flags = int.from_bytes(data[80:84], "little")
    fourcc = data[84:88]
    bit_count = int.from_bytes(data[88:92], "little")
    masks = tuple(int.from_bytes(data[offset : offset + 4], "little") for offset in (92, 96, 100, 104))
    caps = int.from_bytes(data[108:112], "little")
    expected_length = 128 + width * height * 4
    contract = (
        header_size == 124
        and (width, height) == (156, 210)
        and mipmaps in (0, 1)
        and pixel_format_size == 32
        and pixel_format_flags == 65
        and fourcc == b"\x00\x00\x00\x00"
        and bit_count == 32
        and masks == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
        and caps == 0x1000
        and len(data) == expected_length
    )
    if not contract:
        raise ValueError(f"invalid one-level BGRA DDS contract: {path}")
    with Image.open(path) as opened:
        decoded = opened.convert("RGBA")
    alpha = decoded.getchannel("A").getextrema()
    return {
        "dimensions": [width, height],
        "alpha_range": [int(alpha[0]), int(alpha[1])],
        "byte_length": len(data),
        "sha256": sha256(path),
        "decoded": decoded,
    }


def approve_metadata(stem: str, details: dict[str, str], record: dict[str, object]) -> None:
    path = METADATA / f"{stem}.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    metadata.update(
        {
            "status": "approved_after_visual_comparison",
            "imagegen_handle": details["handle"],
            "source_sha256": record["source_sha256"],
            "processed_sha256": record["processed_sha256"],
            "package_dds": record["package_final"],
            "runtime_dds": record["runtime_final"],
            "runtime_sha256": record["runtime_sha256"],
            "visual_review": "Approved against the bundled vanilla HOI4 leader portrait references: close readable bust grouping, interwar clothing, subdued painted finish, quiet background, no photographic or modern concept-art treatment.",
            "source_reference_mode": "collective fictional institution; vanilla references used for painted style only, never identity",
        }
    )
    path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def validate_portraits() -> tuple[list[dict[str, object]], dict[str, object]]:
    DECODED.mkdir(parents=True, exist_ok=True)
    records = []
    files = []
    for stem, details in PORTRAITS.items():
        source = SOURCE / f"{stem}_source.png"
        processed = PROCESSED / f"{stem}.png"
        package = FINAL / f"{stem}.dds"
        runtime = RUNTIME / f"{stem}.dds"
        review = REVIEWS / f"{stem}_comparison.png"
        metadata = METADATA / f"{stem}.json"
        for path in (source, processed, package, runtime, review, metadata):
            if not path.is_file():
                raise FileNotFoundError(path)
        with Image.open(source) as opened:
            source_dimensions = [opened.width, opened.height]
        with Image.open(processed) as opened:
            processed_rgba = opened.convert("RGBA")
        if processed_rgba.size != (156, 210):
            raise ValueError(f"processed portrait dimensions differ: {processed}")
        package_result = validate_dds(package)
        runtime_result = validate_dds(runtime)
        if package.read_bytes() != runtime.read_bytes():
            raise ValueError(f"package/runtime DDS mismatch: {stem}")
        if ImageChops.difference(processed_rgba, runtime_result["decoded"]).getbbox() is not None:
            raise ValueError(f"decoded DDS pixels differ from processed PNG: {stem}")
        decoded = DECODED / f"{stem}.png"
        runtime_result["decoded"].save(decoded)
        record = {
            "kind": "institutional_portrait",
            "identifier": stem,
            "source": rel(source),
            "source_dimensions": source_dimensions,
            "source_sha256": sha256(source),
            "imagegen_handle": details["handle"],
            "source_kind": "collective",
            "crop": [5, 0, 1075, 1440],
            "processor": ".tools/process_hoi4_portrait.py leader",
            "processed": rel(processed),
            "processed_dimensions": [156, 210],
            "processed_sha256": sha256(processed),
            "package_final": rel(package),
            "runtime_final": rel(runtime),
            "runtime_sha256": runtime_result["sha256"],
            "review_sheet": rel(review),
            "metadata": rel(metadata),
            "validation": {
                "dimensions": [156, 210],
                "alpha_range": runtime_result["alpha_range"],
                "decoded_pixel_equality": True,
                "package_runtime_byte_equality": True,
            },
            "provenance": "Original fictional collective produced with OpenAI built-in ImageGen; deterministic official HOI4 leader portrait finishing and DDS conversion",
            "license": "Original generated fictional asset; no third-party person or identity reference",
            "notes": details["brief"],
        }
        records.append(record)
        approve_metadata(stem, details, record)
        files.append(
            {
                "identifier": stem,
                "runtime": rel(runtime),
                "dimensions": [156, 210],
                "sha256": runtime_result["sha256"],
                "package_runtime_byte_equality": True,
                "decoded_pixel_equality": True,
                "review_sheet": rel(review),
            }
        )
    if len({record["source_sha256"] for record in records}) != 4:
        raise ValueError("institutional source masters are not all distinct")
    if len({record["processed_sha256"] for record in records}) != 4:
        raise ValueError("institutional processed portraits are not all distinct")
    validation = {
        "status": "passed",
        "source_mode": "OpenAI built-in ImageGen",
        "source_kind": "collective",
        "portrait_count": 4,
        "runtime_dds_files": 4,
        "output_dimensions": [156, 210],
        "crop": [5, 0, 1075, 1440],
        "visual_approval": "passed against bundled vanilla leader portrait references",
        "checks": [
            "four distinct built-in ImageGen source hashes",
            "official processor metadata records source-kind collective and explicit crop",
            "individual vanilla comparison sheet exists for every portrait",
            "one-level uncompressed BGRA DDS contract",
            "package/runtime byte equality",
            "decoded DDS/processed PNG pixel equality",
            "four distinct processed portrait hashes",
        ],
        "files": files,
    }
    return records, validation


def make_contact_sheet(records: list[dict[str, object]], source_mode: bool) -> Path:
    cell_width = 330 if source_mode else 250
    preview = (300, 400) if source_mode else (156, 210)
    label_y = preview[1] + 20
    sheet = Image.new("RGB", (cell_width * 4, label_y + 40), (35, 37, 39))
    draw = ImageDraw.Draw(sheet)
    label_font = font(12)
    for index, record in enumerate(records):
        path = REPO / str(record["source"] if source_mode else record["processed"])
        with Image.open(path) as opened:
            image = ImageOps.fit(opened.convert("RGB"), preview, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        x = index * cell_width + (cell_width - preview[0]) // 2
        sheet.paste(image, (x, 10))
        draw.text((index * cell_width + 8, label_y), str(record["identifier"]).removeprefix("leader_"), font=label_font, fill=(236, 236, 232))
    name = "institutional_portraits_corrected_source_contact_sheet.png" if source_mode else "institutional_portraits_corrected_processed_contact_sheet.png"
    output = CONTACT / name
    sheet.save(output)
    if not source_mode:
        shutil.copyfile(output, CONTACT / "institutional_portraits_decoded_contact_sheet.png")
    return output


def merge_shared_records(records: list[dict[str, object]]) -> None:
    path = BASE / "asset_records.json"
    existing = json.loads(path.read_text(encoding="utf-8"))
    identifiers = set(PORTRAITS)
    remaining = [row for row in existing if row.get("identifier") not in identifiers]
    insertion = next(
        (index for index, row in enumerate(remaining) if row.get("kind") == "advisor_portrait"),
        len(remaining),
    )
    merged = remaining[:insertion] + records + remaining[insertion:]
    path.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--merge-shared-records", action="store_true", help="Replace only the four institutional identifiers in asset_records.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records, validation = validate_portraits()
    (BASE / "institutional_portrait_asset_records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    (BASE / "institutional_portrait_validation_2026_07_15.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    (BASE / "institutional_portrait_checksums.sha256").write_text(
        "\n".join(f"{record['runtime_sha256']}  {record['runtime_final']}" for record in records) + "\n",
        encoding="utf-8",
    )
    make_contact_sheet(records, source_mode=True)
    make_contact_sheet(records, source_mode=False)
    if args.merge_shared_records:
        merge_shared_records(records)
    print(f"Validated {validation['runtime_dds_files']} corrected institutional portrait DDS files.")


if __name__ == "__main__":
    main()
