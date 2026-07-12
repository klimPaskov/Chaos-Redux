#!/usr/bin/env python3
"""Build and verify the Event 014 Europe/Asia/Africa warlord portrait tranche.

This helper is intentionally limited to the 24 CBA-CBH portraits owned by this
tranche. It does not discover or modify Middle East, Americas, or Oceania files.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
REPO = PACKAGE.parents[3]
SOURCE_DIR = PACKAGE / "source_png"
PROCESSED_DIR = PACKAGE / "processed_png"
CONTACT_DIR = PACKAGE / "contact_sheets"
NOTES_DIR = PACKAGE / "notes"
RUNTIME_DIR = REPO / "gfx" / "leaders" / "014_cannibalism"

WIDTH = 156
HEIGHT = 210
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
REGIONS = {
    "europe": "",
    "asia": "_asia",
    "africa": "_africa",
}


def stem(slot: str, suffix: str) -> str:
    return f"leader_{slot}_warlord{suffix}"


def source_path(slot: str, suffix: str) -> Path:
    return SOURCE_DIR / f"{stem(slot, suffix)}_source.png"


def processed_path(slot: str, suffix: str) -> Path:
    return PROCESSED_DIR / f"{stem(slot, suffix)}.png"


def runtime_path(slot: str, suffix: str) -> Path:
    return RUNTIME_DIR / f"{stem(slot, suffix)}.dds"


def font(size: int) -> ImageFont.ImageFont:
    for name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def cover_crop_box(width: int, height: int) -> tuple[int, int, int, int]:
    target_ratio = WIDTH / HEIGHT
    source_ratio = width / height
    if source_ratio > target_ratio:
        crop_width = round(height * target_ratio)
        left = (width - crop_width) // 2
        return left, 0, left + crop_width, height
    crop_height = round(width / target_ratio)
    top = (height - crop_height) // 2
    return 0, top, width, top + crop_height


def labeled_contact(
    images: list[tuple[str, Image.Image]],
    columns: int,
    cell_width: int,
    cell_height: int,
    output: Path,
) -> None:
    label_height = 32
    margin = 12
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new(
        "RGBA",
        (margin + columns * (cell_width + margin), margin + rows * (cell_height + label_height + margin)),
        (20, 22, 25, 255),
    )
    draw = ImageDraw.Draw(sheet)
    label_font = font(18)
    for index, (label, image) in enumerate(images):
        row, column = divmod(index, columns)
        x = margin + column * (cell_width + margin)
        y = margin + row * (cell_height + label_height + margin)
        thumb = ImageOps.contain(image.convert("RGBA"), (cell_width, cell_height), Image.Resampling.LANCZOS)
        px = x + (cell_width - thumb.width) // 2
        py = y + (cell_height - thumb.height) // 2
        sheet.alpha_composite(thumb, (px, py))
        draw.rectangle((x, y, x + cell_width - 1, y + cell_height - 1), outline=(100, 105, 112, 255), width=1)
        draw.text((x, y + cell_height + 5), label, fill=(235, 236, 238, 255), font=label_font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(output, quality=95)


def build() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    crop_rows: list[dict[str, object]] = []
    combined_sources: list[tuple[str, Image.Image]] = []
    combined_processed: list[tuple[str, Image.Image]] = []

    for region, suffix in REGIONS.items():
        source_images: list[tuple[str, Image.Image]] = []
        processed_images: list[tuple[str, Image.Image]] = []
        for slot in SLOTS:
            source = source_path(slot, suffix)
            if not source.is_file():
                raise FileNotFoundError(source)
            with Image.open(source) as opened:
                original = opened.convert("RGBA")
            crop_box = cover_crop_box(*original.size)
            cropped = original.crop(crop_box)
            processed = cropped.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
            output = processed_path(slot, suffix)
            processed.save(output)

            label = f"{region.title()} {slot}"
            source_images.append((label, original))
            processed_images.append((label, processed))
            combined_sources.append((label, original))
            combined_processed.append((label, processed))
            crop_rows.append(
                {
                    "region": region,
                    "slot": slot,
                    "source": source.relative_to(REPO).as_posix(),
                    "original_width": original.width,
                    "original_height": original.height,
                    "crop_left": crop_box[0],
                    "crop_top": crop_box[1],
                    "crop_right": crop_box[2],
                    "crop_bottom": crop_box[3],
                    "processed": output.relative_to(REPO).as_posix(),
                    "processed_width": WIDTH,
                    "processed_height": HEIGHT,
                    "mode": processed.mode,
                }
            )

        labeled_contact(
            source_images,
            columns=4,
            cell_width=234,
            cell_height=315,
            output=CONTACT_DIR / f"warlord_{region}_source_contact.png",
        )
        labeled_contact(
            processed_images,
            columns=4,
            cell_width=234,
            cell_height=315,
            output=CONTACT_DIR / f"warlord_{region}_processed_contact.png",
        )

    labeled_contact(
        combined_sources,
        columns=8,
        cell_width=156,
        cell_height=210,
        output=CONTACT_DIR / "warlord_europe_asia_africa_source_contact.png",
    )
    labeled_contact(
        combined_processed,
        columns=8,
        cell_width=156,
        cell_height=210,
        output=CONTACT_DIR / "warlord_europe_asia_africa_processed_contact.png",
    )
    labeled_contact(
        combined_processed,
        columns=8,
        cell_width=156,
        cell_height=210,
        output=CONTACT_DIR / "warlord_europe_asia_africa_actual_size_contact.png",
    )

    crop_ledger = NOTES_DIR / "europe_asia_africa_crop_ledger.csv"
    with crop_ledger.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(crop_rows[0]))
        writer.writeheader()
        writer.writerows(crop_rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def dhash(image: Image.Image) -> int:
    gray = image.convert("L").resize((9, 8), Image.Resampling.LANCZOS)
    pixels = list(gray.getdata())
    value = 0
    for y in range(8):
        for x in range(8):
            value = (value << 1) | int(pixels[y * 9 + x] > pixels[y * 9 + x + 1])
    return value


def read_dds_header(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()[:128]
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError(f"Invalid DDS magic/header: {path}")
    values = {
        "magic": "DDS ",
        "header_size": struct.unpack_from("<I", data, 4)[0],
        "flags": struct.unpack_from("<I", data, 8)[0],
        "height": struct.unpack_from("<I", data, 12)[0],
        "width": struct.unpack_from("<I", data, 16)[0],
        "pitch": struct.unpack_from("<I", data, 20)[0],
        "mipmap_count": struct.unpack_from("<I", data, 28)[0],
        "pixel_format_size": struct.unpack_from("<I", data, 76)[0],
        "pixel_format_flags": struct.unpack_from("<I", data, 80)[0],
        "fourcc": data[84:88].decode("ascii", errors="replace"),
        "rgb_bit_count": struct.unpack_from("<I", data, 88)[0],
        "red_mask": f"{struct.unpack_from('<I', data, 92)[0]:08X}",
        "green_mask": f"{struct.unpack_from('<I', data, 96)[0]:08X}",
        "blue_mask": f"{struct.unpack_from('<I', data, 100)[0]:08X}",
        "alpha_mask": f"{struct.unpack_from('<I', data, 104)[0]:08X}",
        "caps": struct.unpack_from("<I", data, 108)[0],
        "file_size": path.stat().st_size,
    }
    return values


def verify() -> None:
    CONTACT_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, object]] = []
    decoded_images: list[tuple[str, Image.Image]] = []
    hashes: dict[str, list[str]] = {"source": [], "processed": [], "dds": []}
    d_hashes: dict[str, int] = {}

    for region, suffix in REGIONS.items():
        region_decoded: list[tuple[str, Image.Image]] = []
        for slot in SLOTS:
            source = source_path(slot, suffix)
            processed = processed_path(slot, suffix)
            dds = runtime_path(slot, suffix)
            for path in (source, processed, dds):
                if not path.is_file():
                    raise FileNotFoundError(path)
            with Image.open(processed) as opened:
                processed_image = opened.convert("RGBA")
            with Image.open(dds) as opened:
                decoded = opened.convert("RGBA")
            difference = ImageChops.difference(processed_image, decoded)
            pixel_identical = difference.getbbox() is None
            header = read_dds_header(dds)
            key = f"{region}_{slot}"
            label = f"{region.title()} {slot}"
            region_decoded.append((label, decoded))
            decoded_images.append((label, decoded))
            d_hashes[key] = dhash(decoded)
            item_hashes = {
                "source": sha256(source),
                "processed": sha256(processed),
                "dds": sha256(dds),
            }
            for kind, value in item_hashes.items():
                hashes[kind].append(value)
            entries.append(
                {
                    "key": key,
                    "source": source.relative_to(REPO).as_posix(),
                    "processed": processed.relative_to(REPO).as_posix(),
                    "dds": dds.relative_to(REPO).as_posix(),
                    "processed_mode": processed_image.mode,
                    "processed_size": list(processed_image.size),
                    "decoded_mode": decoded.mode,
                    "decoded_size": list(decoded.size),
                    "pixel_identical": pixel_identical,
                    "sha256": item_hashes,
                    "dhash64": f"{d_hashes[key]:016x}",
                    "dds_header": header,
                }
            )
        labeled_contact(
            region_decoded,
            columns=4,
            cell_width=234,
            cell_height=315,
            output=CONTACT_DIR / f"warlord_{region}_dds_decoded_contact.png",
        )

    labeled_contact(
        decoded_images,
        columns=8,
        cell_width=156,
        cell_height=210,
        output=CONTACT_DIR / "warlord_europe_asia_africa_dds_decoded_contact.png",
    )

    distances: list[dict[str, object]] = []
    for left, right in itertools.combinations(sorted(d_hashes), 2):
        distances.append(
            {
                "left": left,
                "right": right,
                "distance": bin(d_hashes[left] ^ d_hashes[right]).count("1"),
            }
        )
    distances.sort(key=lambda row: (row["distance"], row["left"], row["right"]))

    report = {
        "entry_count": len(entries),
        "all_processed_rgba_156x210": all(
            entry["processed_mode"] == "RGBA" and entry["processed_size"] == [WIDTH, HEIGHT]
            for entry in entries
        ),
        "all_dds_decoded_156x210": all(entry["decoded_size"] == [WIDTH, HEIGHT] for entry in entries),
        "all_dds_pixel_identical": all(entry["pixel_identical"] for entry in entries),
        "unique_hash_counts": {kind: len(set(values)) for kind, values in hashes.items()},
        "dhash_min_distance": distances[0]["distance"],
        "dhash_max_distance": distances[-1]["distance"],
        "closest_dhash_pairs": distances[:10],
        "entries": entries,
    }
    (NOTES_DIR / "europe_asia_africa_validation.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )

    hash_lines: list[str] = []
    for entry in entries:
        for kind in ("source", "processed", "dds"):
            hash_lines.append(f"{entry['sha256'][kind]}  {entry[kind]}")
    (PACKAGE / "europe_asia_africa_hashes.sha256").write_text(
        "\n".join(hash_lines) + "\n",
        encoding="utf-8",
    )

    failures: list[str] = []
    if report["entry_count"] != 24:
        failures.append(f"expected 24 entries, got {report['entry_count']}")
    if not report["all_processed_rgba_156x210"]:
        failures.append("processed PNG mode/size mismatch")
    if not report["all_dds_decoded_156x210"]:
        failures.append("DDS decoded size mismatch")
    if not report["all_dds_pixel_identical"]:
        failures.append("processed/DDS pixel mismatch")
    for kind, count in report["unique_hash_counts"].items():
        if count != 24:
            failures.append(f"{kind} unique hash count is {count}, expected 24")
    if failures:
        raise RuntimeError("; ".join(failures))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("build", "verify"))
    args = parser.parse_args()
    if args.command == "build":
        build()
    else:
        verify()


if __name__ == "__main__":
    main()
