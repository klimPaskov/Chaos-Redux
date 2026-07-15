#!/usr/bin/env python3
"""Build and validate the generated LCX flat flag package.

The image-generation output supplies the researched three-river geometry. This
script performs deterministic technical finishing only: aspect crop, exact
two-colour flattening, HOI4 resizing, uncompressed 32-bit bottom-left TGA
encoding, contact sheets, hashes, and machine-readable validation.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_png" / "LCX_low_countries_river_fork_imagegen_raw.png"
PROCESSED = ROOT / "processed_png"
FINAL_TGA = ROOT / "final_tga"
CONTACTS = ROOT / "contact_sheets"
METADATA = ROOT / "metadata"

NAVY = (22, 58, 95)
WHITE = (255, 255, 255)
PALETTE = (NAVY, WHITE)
TARGET_RATIO = 82 / 52
MASTER_SIZE = (820, 520)
SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}


def ensure_dirs() -> None:
    for path in (PROCESSED, FINAL_TGA, CONTACTS, METADATA):
        path.mkdir(parents=True, exist_ok=True)


def center_crop_ratio(image: Image.Image) -> Image.Image:
    width, height = image.size
    current_ratio = width / height
    if current_ratio > TARGET_RATIO:
        crop_width = round(height * TARGET_RATIO)
        left = (width - crop_width) // 2
        box = (left, 0, left + crop_width, height)
    else:
        crop_height = round(width / TARGET_RATIO)
        top = (height - crop_height) // 2
        box = (0, top, width, top + crop_height)
    return image.crop(box)


def colour_distance(pixel: tuple[int, int, int], colour: tuple[int, int, int]) -> int:
    return sum((component - target) ** 2 for component, target in zip(pixel, colour))


def flatten(image: Image.Image) -> Image.Image:
    rgb = image.convert("RGB")
    pixels = [
        WHITE if colour_distance(pixel, WHITE) < colour_distance(pixel, NAVY) else NAVY
        for pixel in rgb.getdata()
    ]
    output = Image.new("RGB", rgb.size)
    output.putdata(pixels)
    return output


def resize_flat(master: Image.Image, size: tuple[int, int]) -> Image.Image:
    return flatten(master.resize(size, Image.Resampling.LANCZOS))


def write_tga_bottom_left(path: Path, image: Image.Image) -> None:
    rgb = image.convert("RGB")
    width, height = rgb.size
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        width,
        height,
        32,
        8,
    )
    payload = bytearray()
    pixels = rgb.load()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            red, green, blue = pixels[x, y]
            payload.extend((blue, green, red, 255))
    path.write_bytes(header + payload)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def tga_metadata(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    header = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    width, height, depth, descriptor = header[8], header[9], header[10], header[11]
    return {
        "width": width,
        "height": height,
        "image_type": header[2],
        "pixel_depth": depth,
        "descriptor": descriptor,
        "origin": "bottom-left" if descriptor & 0x20 == 0 else "top-left",
        "alpha_bits": descriptor & 0x0F,
        "byte_length": len(raw),
    }


def palette_values(image: Image.Image) -> list[str]:
    colours = sorted(set(image.convert("RGB").getdata()))
    return ["#%02X%02X%02X" % colour for colour in colours]


def branch_proof(image: Image.Image) -> dict[str, object]:
    rgb = image.convert("RGB")
    sample_width = max(1, round(rgb.width * 0.3))
    third = rgb.height / 3
    bands = {"upper": 0, "middle": 0, "lower": 0}
    for y in range(rgb.height):
        label = "upper" if y < third else "middle" if y < 2 * third else "lower"
        for x in range(sample_width):
            if rgb.getpixel((x, y)) == WHITE:
                bands[label] += 1
    return {
        "left_sample_width": sample_width,
        "white_pixels_by_vertical_third": bands,
        "three_branches_visible": all(value > 0 for value in bands.values()),
    }


def make_contact_sheet(raw: Image.Image, master: Image.Image, outputs: dict[str, Image.Image]) -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (1000, 720), (230, 230, 230))
    draw = ImageDraw.Draw(sheet)
    raw_preview = center_crop_ratio(raw).resize((492, 312), Image.Resampling.LANCZOS)
    master_preview = master.resize((492, 312), Image.Resampling.NEAREST)
    sheet.paste(raw_preview, (4, 24))
    sheet.paste(master_preview, (504, 24))
    draw.text((4, 6), "Official imagegen source crop", fill=(0, 0, 0), font=font)
    draw.text((504, 6), "Exact #163A5F / #FFFFFF flat master", fill=(0, 0, 0), font=font)

    x = 4
    for name in ("normal", "medium", "small"):
        image = outputs[name]
        scale = min(14, 420 // image.width, 280 // image.height)
        preview = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
        draw.text((x, 360), f"{name}: {image.width}x{image.height}", fill=(0, 0, 0), font=font)
        sheet.paste(preview, (x, 382))
        x += preview.width + 30
    sheet.save(CONTACTS / "LCX_flag_source_flat_and_size_ladder.png")


def main() -> None:
    ensure_dirs()
    raw = Image.open(SOURCE).convert("RGB")
    crop = center_crop_ratio(raw)
    master = flatten(crop.resize(MASTER_SIZE, Image.Resampling.LANCZOS))
    master_path = PROCESSED / "LCX_low_countries_river_fork_flat_master.png"
    master.save(master_path)

    outputs: dict[str, Image.Image] = {}
    records: dict[str, object] = {}
    for name, size in SIZES.items():
        output = resize_flat(master, size)
        outputs[name] = output
        png_path = PROCESSED / f"LCX_{name}_{size[0]}x{size[1]}.png"
        tga_path = FINAL_TGA / f"LCX_{name}_{size[0]}x{size[1]}.tga"
        output.save(png_path)
        write_tga_bottom_left(tga_path, output)
        records[name] = {
            "png": str(png_path.relative_to(ROOT)).replace("\\", "/"),
            "tga": str(tga_path.relative_to(ROOT)).replace("\\", "/"),
            "dimensions": list(size),
            "palette": palette_values(output),
            "branch_proof": branch_proof(output),
            "png_sha256": sha256(png_path),
            "tga_sha256": sha256(tga_path),
            "tga_header": tga_metadata(tga_path),
        }

    make_contact_sheet(raw, master, outputs)
    validation = {
        "identity": "LCX",
        "asset_classification": "alternate-history generated flag",
        "source_dimensions": list(raw.size),
        "crop_dimensions": list(crop.size),
        "master_dimensions": list(master.size),
        "required_palette": ["#163A5F", "#FFFFFF"],
        "master_palette": palette_values(master),
        "all_sizes_exact_palette": all(record["palette"] == ["#163A5F", "#FFFFFF"] for record in records.values()),
        "all_sizes_three_branches_visible": all(record["branch_proof"]["three_branches_visible"] for record in records.values()),
        "outputs": records,
        "source_sha256": sha256(SOURCE),
        "master_sha256": sha256(master_path),
        "contact_sheet": "contact_sheets/LCX_flag_source_flat_and_size_ladder.png",
    }
    (METADATA / "LCX_flag_validation.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
    )
    checksums = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in sorted(
            [SOURCE, master_path, *PROCESSED.glob("LCX_*x*.png"), *FINAL_TGA.glob("LCX_*.tga"), CONTACTS / "LCX_flag_source_flat_and_size_ladder.png"]
        )
    ]
    (METADATA / "checksums.sha256").write_text("\n".join(checksums) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
