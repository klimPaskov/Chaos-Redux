#!/usr/bin/env python3
"""Mechanical finishing, review sheets, and validation for the AFX visual package."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


FOCUS_SIZE = (94, 86)
REPORT_SIZE = (210, 176)

FOCUS_STEMS = (
    "goal_independence_wave_afx_sambre_meuse_authority",
    "goal_independence_wave_afx_mines_rails_furnaces",
    "goal_independence_wave_afx_basin_government",
    "goal_independence_wave_afx_industrial_reserve",
    "goal_independence_wave_afx_industrial_succession",
    "goal_independence_wave_afx_meuse_network_office",
    "goal_independence_wave_afx_meuse_conference",
    "goal_independence_wave_afx_low_countries_delegation",
)

REPORT_STEMS = (
    "report_event_006_afx_industrial_authority",
    "report_event_006_afx_basin_government",
    "report_event_006_afx_meuse_ambition",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def sanitize_transparent_rgb(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, alpha = pixels[x, y]
            if alpha == 0:
                pixels[x, y] = (0, 0, 0, 0)
    return image


def scaled_alpha(alpha: Image.Image, factor: float) -> Image.Image:
    return alpha.point(lambda value: max(0, min(255, round(value * factor))))


def process_focus_icon(source: Path, output: Path) -> None:
    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 5 else 0).getbbox()
    if bbox is None:
        raise ValueError(f"No visible subject in {source}")
    image = image.crop(bbox)

    # Leave room for a one-pixel outline and soft one-pixel shadow.
    max_width = FOCUS_SIZE[0] - 8
    max_height = FOCUS_SIZE[1] - 8
    scale = min(max_width / image.width, max_height / image.height)
    resized_size = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    image = image.convert("RGBa").resize(resized_size, Image.Resampling.LANCZOS).convert("RGBA")
    image = sanitize_transparent_rgb(image)

    subject_alpha = image.getchannel("A")
    outline_alpha = ImageChops.subtract(subject_alpha.filter(ImageFilter.MaxFilter(3)), subject_alpha)
    shadow_alpha = scaled_alpha(subject_alpha.filter(ImageFilter.GaussianBlur(0.75)), 0.55)

    canvas = Image.new("RGBA", FOCUS_SIZE, (0, 0, 0, 0))
    left = (FOCUS_SIZE[0] - image.width) // 2
    top = (FOCUS_SIZE[1] - image.height) // 2 - 1

    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow.putalpha(shadow_alpha)
    canvas.alpha_composite(shadow, (left + 1, top + 2))

    outline = Image.new("RGBA", image.size, (10, 9, 8, 0))
    outline.putalpha(scaled_alpha(outline_alpha, 0.9))
    canvas.alpha_composite(outline, (left, top))
    canvas.alpha_composite(image, (left, top))
    canvas = sanitize_transparent_rgb(canvas)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def process_focus_folder(input_dir: Path, output_dir: Path) -> None:
    actual = {path.stem for path in input_dir.glob("*.png")}
    expected = set(FOCUS_STEMS)
    if actual != expected:
        raise ValueError(f"Focus alpha-master set mismatch; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")
    for stem in FOCUS_STEMS:
        process_focus_icon(input_dir / f"{stem}.png", output_dir / f"{stem}.png")


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    result = Image.new("RGB", size, (78, 78, 78))
    draw = ImageDraw.Draw(result)
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            if (x // tile + y // tile) % 2:
                draw.rectangle((x, y, x + tile - 1, y + tile - 1), fill=(126, 126, 126))
    return result


def wrap_label(label: str, limit: int = 35) -> list[str]:
    words = label.split("_")
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current}_{word}"
        if len(candidate) <= limit:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:3]


def build_contact_sheet(
    paths: Iterable[Path],
    output: Path,
    title: str,
    columns: int,
    scale: int,
) -> None:
    paths = list(paths)
    if not paths:
        raise ValueError(f"No images supplied for {output}")
    images = [Image.open(path).convert("RGBA") for path in paths]
    preview_width = max(image.width for image in images) * scale
    preview_height = max(image.height for image in images) * scale
    cell_width = max(330, preview_width + 28)
    cell_height = preview_height + 100
    rows = (len(paths) + columns - 1) // columns
    margin = 24
    header = 52
    sheet = Image.new(
        "RGB",
        (margin * 2 + cell_width * columns, margin * 2 + header + cell_height * rows),
        (25, 27, 29),
    )
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, margin), title, font=load_font(25), fill=(242, 242, 242))
    for index, (path, image) in enumerate(zip(paths, images)):
        row, column = divmod(index, columns)
        left = margin + column * cell_width
        top = margin + header + row * cell_height
        preview = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
        background = checker((preview_width, preview_height), max(4, scale * 2))
        paste_x = (preview_width - preview.width) // 2
        paste_y = (preview_height - preview.height) // 2
        background.paste(preview, (paste_x, paste_y), preview)
        sheet.paste(background, (left + (cell_width - preview_width) // 2, top))
        label_y = top + preview_height + 8
        for line in wrap_label(path.stem):
            draw.text((left + 6, label_y), line, font=load_font(16), fill=(232, 232, 232))
            label_y += 18
        draw.text(
            (left + 6, top + preview_height + 70),
            f"{image.width}x{image.height} RGBA",
            font=load_font(15),
            fill=(160, 194, 220),
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, format="PNG", optimize=True)


def image_record(path: Path) -> dict[str, object]:
    with Image.open(path) as source:
        image = source.convert("RGBA")
    alpha = image.getchannel("A")
    alpha_min, alpha_max = alpha.getextrema()
    histogram = alpha.histogram()
    pixel_count = image.width * image.height
    return {
        "path": path.as_posix(),
        "sha256": sha256(path),
        "dimensions": [image.width, image.height],
        "mode": image.mode,
        "alpha_min": alpha_min,
        "alpha_max": alpha_max,
        "alpha_nonzero_fraction": round(sum(histogram[1:]) / pixel_count, 6),
        "corner_alpha": [
            alpha.getpixel((0, 0)),
            alpha.getpixel((image.width - 1, 0)),
            alpha.getpixel((0, image.height - 1)),
            alpha.getpixel((image.width - 1, image.height - 1)),
        ],
    }


def dds_record(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 128:
        raise ValueError(f"DDS shorter than legacy header: {path}")
    header_size = struct.unpack_from("<I", data, 4)[0]
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mipmap_count = struct.unpack_from("<I", data, 28)[0]
    pixel_format = struct.unpack_from("<8I", data, 76)
    caps = struct.unpack_from("<I", data, 108)[0]
    pixel_data = data[128:]
    alpha_values = pixel_data[3::4]
    expected_length = 128 + width * height * 4
    checks = {
        "magic": data[:4] == b"DDS ",
        "header_size_124": header_size == 124,
        "pixel_format_size_32": pixel_format[0] == 32,
        "pixel_format_flags_65": pixel_format[1] == 65,
        "fourcc_zero": pixel_format[2] == 0,
        "bit_count_32": pixel_format[3] == 32,
        "bgra_masks": list(pixel_format[4:]) == [0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000],
        "dds_caps_texture": bool(caps & 0x1000),
        "no_mipmaps": mipmap_count in (0, 1),
        "exact_length": len(data) == expected_length,
    }
    return {
        "path": path.as_posix(),
        "sha256": sha256(path),
        "dimensions": [width, height],
        "file_length": len(data),
        "expected_length": expected_length,
        "alpha_min": min(alpha_values) if alpha_values else None,
        "alpha_max": max(alpha_values) if alpha_values else None,
        "checks": checks,
        "valid": all(checks.values()),
    }


def average_hash(path: Path) -> int:
    image = Image.open(path).convert("RGBA")
    background = Image.new("RGBA", image.size, (18, 18, 18, 255))
    background.alpha_composite(image)
    grey = background.convert("L").resize((16, 16), Image.Resampling.LANCZOS)
    values = list(grey.getdata())
    mean = sum(values) / len(values)
    result = 0
    for value in values:
        result = (result << 1) | int(value >= mean)
    return result


def uniqueness_record(paths: Iterable[Path]) -> dict[str, object]:
    paths = list(paths)
    pairs: list[dict[str, object]] = []
    hashes = {path: average_hash(path) for path in paths}
    for index, left in enumerate(paths):
        for right in paths[index + 1 :]:
            distance = bin(hashes[left] ^ hashes[right]).count("1")
            pairs.append({"left": left.as_posix(), "right": right.as_posix(), "hamming_distance": distance})
    minimum = min((pair["hamming_distance"] for pair in pairs), default=None)
    return {
        "algorithm": "16x16 luminance average hash composited over dark grey",
        "sha256_all_unique": len({sha256(path) for path in paths}) == len(paths),
        "minimum_pairwise_hamming_distance": minimum,
        "perceptual_hashes_all_distinct": all(pair["hamming_distance"] > 0 for pair in pairs),
        "pairs": pairs,
    }


def validate(package_root: Path, mod_root: Path, output: Path, inventory: Path) -> None:
    source_focus = [package_root / "source_png/focus" / f"{stem}.png" for stem in FOCUS_STEMS]
    source_report = [package_root / "source_png/report" / f"{stem}.png" for stem in REPORT_STEMS]
    processed_focus = [package_root / "processed_png/focus" / f"{stem}.png" for stem in FOCUS_STEMS]
    processed_report = [package_root / "processed_png/report" / f"{stem}.png" for stem in REPORT_STEMS]
    final_focus = [mod_root / "gfx/interface/goals/006_independence_wave/afx" / f"{stem}.dds" for stem in FOCUS_STEMS]
    final_report = [mod_root / "gfx/event_pictures/006_independence_wave/afx" / f"{stem}.dds" for stem in REPORT_STEMS]

    all_expected = source_focus + source_report + processed_focus + processed_report + final_focus + final_report
    missing = [path.as_posix() for path in all_expected if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing expected assets: {missing}")

    roundtrip: list[dict[str, object]] = []
    for png_path, dds_path in zip(processed_focus + processed_report, final_focus + final_report):
        png = Image.open(png_path).convert("RGBA")
        dds = Image.open(dds_path).convert("RGBA")
        exact = png.size == dds.size and ImageChops.difference(png, dds).getbbox() is None
        roundtrip.append(
            {
                "stem": png_path.stem,
                "processed_png": png_path.as_posix(),
                "final_dds": dds_path.as_posix(),
                "dimensions_match": png.size == dds.size,
                "rgba_exact_match": exact,
            }
        )

    focus_records = [image_record(path) for path in processed_focus]
    report_records = [image_record(path) for path in processed_report]
    dds_records = [dds_record(path) for path in final_focus + final_report]
    focus_alpha_valid = all(
        record["alpha_min"] == 0
        and record["alpha_max"] == 255
        and record["corner_alpha"] == [0, 0, 0, 0]
        and 0.08 < record["alpha_nonzero_fraction"] < 0.93
        for record in focus_records
    )
    dimensions_valid = all(record["dimensions"] == list(FOCUS_SIZE) for record in focus_records)
    dimensions_valid = dimensions_valid and all(record["dimensions"] == list(REPORT_SIZE) for record in report_records)
    dimensions_valid = dimensions_valid and all(
        record["dimensions"] == list(FOCUS_SIZE if index < len(final_focus) else REPORT_SIZE)
        for index, record in enumerate(dds_records)
    )

    report = {
        "package": "IW-006 Wallonia (AFX) Level-2 unique visual package",
        "expected_counts": {"source_png": 11, "processed_png": 11, "runtime_dds": 11},
        "actual_counts": {
            "source_png": len(source_focus + source_report),
            "processed_png": len(processed_focus + processed_report),
            "runtime_dds": len(final_focus + final_report),
        },
        "source_png": [image_record(path) for path in source_focus + source_report],
        "processed_focus_png": focus_records,
        "processed_report_png": report_records,
        "runtime_dds": dds_records,
        "focus_alpha_valid": focus_alpha_valid,
        "dimensions_valid": dimensions_valid,
        "source_uniqueness": uniqueness_record(source_focus + source_report),
        "focus_runtime_uniqueness": uniqueness_record(processed_focus),
        "report_runtime_uniqueness": uniqueness_record(processed_report),
        "decoded_equivalence": {
            "all_exact": all(record["rgba_exact_match"] for record in roundtrip),
            "pairs": roundtrip,
        },
    }
    report["counts_match"] = report["actual_counts"] == report["expected_counts"]
    report["all_dds_valid"] = all(record["valid"] for record in dds_records)
    report["all_checks_pass"] = all(
        (
            report["counts_match"],
            report["all_dds_valid"],
            report["focus_alpha_valid"],
            report["dimensions_valid"],
            report["decoded_equivalence"]["all_exact"],
            report["source_uniqueness"]["sha256_all_unique"],
            report["focus_runtime_uniqueness"]["sha256_all_unique"],
            report["focus_runtime_uniqueness"]["perceptual_hashes_all_distinct"],
            report["report_runtime_uniqueness"]["sha256_all_unique"],
            report["report_runtime_uniqueness"]["perceptual_hashes_all_distinct"],
        )
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    package_files = [
        path
        for path in package_root.rglob("*")
        if path.is_file() and path.resolve() != inventory.resolve()
    ]
    inventory_paths = sorted(set(package_files + final_focus + final_report), key=lambda path: path.as_posix())
    inventory.write_text(
        "".join(f"{sha256(path)}  {path.as_posix()}\n" for path in inventory_paths),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    icons = subparsers.add_parser("focus-icons")
    icons.add_argument("--input-dir", required=True, type=Path)
    icons.add_argument("--output-dir", required=True, type=Path)

    contacts = subparsers.add_parser("contact")
    contacts.add_argument("--input-dir", required=True, type=Path)
    contacts.add_argument("--output", required=True, type=Path)
    contacts.add_argument("--title", required=True)
    contacts.add_argument("--columns", type=int, default=4)
    contacts.add_argument("--scale", type=int, default=3)

    validation = subparsers.add_parser("validate")
    validation.add_argument("--package-root", required=True, type=Path)
    validation.add_argument("--mod-root", required=True, type=Path)
    validation.add_argument("--output", required=True, type=Path)
    validation.add_argument("--inventory", required=True, type=Path)

    args = parser.parse_args()
    if args.command == "focus-icons":
        process_focus_folder(args.input_dir, args.output_dir)
    elif args.command == "contact":
        build_contact_sheet(
            sorted(args.input_dir.glob("*.png")),
            args.output,
            args.title,
            args.columns,
            args.scale,
        )
    else:
        validate(args.package_root, args.mod_root, args.output, args.inventory)


if __name__ == "__main__":
    main()
