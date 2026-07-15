#!/usr/bin/env python3
"""Build the bounded Event 006 Sardinia, Sicily, and Trieste flag package.

The three source rasters were created independently with official ImageGen.
This tool never traces a cited reference, imports a reference mask, redraws an
emblem, or invents an ideology variant.  It only maps the retained ImageGen
pixels to the documented flat palette without dithering, builds the vanilla
HOI4 size ladder, writes bottom-origin uncompressed 32-bit TGAs, validates the
payloads, assembles review sheets, and records hashes and machine-readable QA.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


PACKAGE_ROOT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
RESEARCH_ROOT = (
    ROOT
    / "docs"
    / "assets"
    / "006_independence_wave"
    / "mediterranean_danube_flag_sources_2026_07_15"
)
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
REFERENCE_ROOT = PACKAGE_ROOT / "reference_inputs"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
NOTES_ROOT = PACKAGE_ROOT / "notes"
FLAGS_ROOT = ROOT / "gfx" / "flags"
CANONICAL_FLAGS_ROOT = (
    ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "flags"
)


FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}


FLAGS = {
    "ARX": {
        "label": "Sardinia - fictional 1936 civic synthesis",
        "raw": "ARX_sardinia_four_moors_imagegen_raw.png",
        "master": "ARX_sardinia_four_moors_imagegen_flat_master.png",
        "palette": ((247, 245, 236), (200, 16, 46), (17, 17, 17)),
        "small_priority": (((17, 17, 17), 0.08), ((200, 16, 46), 0.25)),
        "cross_cleanup": {
            "cross_color": (200, 16, 46),
            "fallback_colors": ((247, 245, 236), (17, 17, 17)),
            "full_span_threshold": 0.80,
        },
        "resized_mapper": "sardinia_red_or_monochrome",
        "reference": RESEARCH_ROOT
        / "source_images"
        / "sardinia_traditional_four_moors_reference.png",
        "additional_references": (
            RESEARCH_ROOT
            / "source_images"
            / "sardinia_gelre_armorial_folio_62r.png",
        ),
        "technical_reference": CANONICAL_FLAGS_ROOT / "ARM_UK.png",
    },
    "ASX": {
        "label": "Sicily - 1848 S.015 route reconstruction",
        "raw": "ASX_sicily_1848_s015_imagegen_raw.png",
        "master": "ASX_sicily_1848_s015_imagegen_flat_master.png",
        "palette": ((0, 146, 70), (245, 241, 230), (206, 43, 55), (216, 163, 40)),
        "small_priority": (((216, 163, 40), 0.08),),
        "reference": REFERENCE_ROOT / "sicily_1848_national_flag_reference_render.png",
        "additional_references": (
            RESEARCH_ROOT
            / "source_images"
            / "sicily_1848_national_flag_reference.svg",
        ),
        "technical_reference": CANONICAL_FLAGS_ROOT / "ARG_gen_nazism_party.png",
    },
    "ICX": {
        "label": "Trieste - 1918-1936 civic reconstruction",
        "raw": "ICX_trieste_civic_imagegen_raw.png",
        "master": "ICX_trieste_civic_imagegen_flat_master.png",
        "palette": ((215, 25, 32), (248, 246, 239)),
        "small_priority": (((248, 246, 239), 0.05),),
        "reference": REFERENCE_ROOT / "trieste_free_territory_flag_reference_render.png",
        "additional_references": (
            RESEARCH_ROOT
            / "source_images"
            / "trieste_free_territory_flag_reference.svg",
        ),
        "technical_reference": CANONICAL_FLAGS_ROOT / "ANU_fascism.png",
    },
}


IDEOLOGIES = ("communism", "democratic", "fascism", "neutrality")


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidate = Path("C:/Windows/Fonts") / filename
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def prepare_directories() -> None:
    for path in (
        SOURCE_ROOT,
        REFERENCE_ROOT,
        CONTACT_ROOT,
        NOTES_ROOT,
        FLAGS_ROOT,
        FLAGS_ROOT / "medium",
        FLAGS_ROOT / "small",
        *(PROCESSED_ROOT / size_name for size_name in FLAG_SIZES),
    ):
        path.mkdir(parents=True, exist_ok=True)


def fixed_palette_image(colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
    palette = Image.new("P", (1, 1))
    values: list[int] = []
    for color in colors:
        values.extend(color)
    while len(values) < 768:
        values.extend(colors[-1])
    palette.putpalette(values[:768])
    return palette


def quantize_to_palette(
    image: Image.Image, colors: tuple[tuple[int, int, int], ...]
) -> Image.Image:
    quantized = image.convert("RGB").quantize(
        palette=fixed_palette_image(colors),
        dither=Image.Dither.NONE,
    )
    return quantized.convert("RGBA")


def normalize_imagegen_source(
    raw_path: Path,
    master_path: Path,
    colors: tuple[tuple[int, int, int], ...],
    cross_cleanup: dict[str, object] | None = None,
) -> Image.Image:
    raw = Image.open(raw_path).convert("RGBA")
    if raw.size != (1536, 1024):
        raise ValueError(f"Unexpected ImageGen source dimensions: {raw_path} ({raw.size})")
    flat = quantize_to_palette(raw, colors)
    if cross_cleanup is not None:
        flat = clean_detected_cross(
            raw,
            flat,
            cross_cleanup["cross_color"],
            cross_cleanup["fallback_colors"],
            cross_cleanup["full_span_threshold"],
        )
    flat.save(master_path)
    return flat


def clean_detected_cross(
    raw: Image.Image,
    flat: Image.Image,
    cross_color: tuple[int, int, int],
    fallback_colors: tuple[tuple[int, int, int], ...],
    threshold: float,
) -> Image.Image:
    """Keep red only on cross spans detected in the ImageGen result itself.

    ImageGen left a few red-tinted shadow pixels beside the black head charges.
    The actual cross supplies full-width rows and full-height columns.  Detecting
    those spans from the quantized source lets us remove off-cross red speckle
    without importing a mask or assigning any manual cross coordinates.
    """
    cleaned = flat.convert("RGBA")
    pixels = cleaned.load()
    cross_rgba = (*cross_color, 255)
    cross_rows = {
        y
        for y in range(cleaned.height)
        if sum(pixels[x, y] == cross_rgba for x in range(cleaned.width))
        / cleaned.width
        >= threshold
    }
    cross_columns = {
        x
        for x in range(cleaned.width)
        if sum(pixels[x, y] == cross_rgba for y in range(cleaned.height))
        / cleaned.height
        >= threshold
    }
    if not cross_rows or not cross_columns:
        raise ValueError("ImageGen cross cleanup could not detect both full-span arms")

    raw_rgb = raw.convert("RGB")
    for y in range(cleaned.height):
        for x in range(cleaned.width):
            if y in cross_rows or x in cross_columns:
                pixels[x, y] = cross_rgba
            elif pixels[x, y] == cross_rgba:
                source_color = raw_rgb.getpixel((x, y))
                replacement = min(
                    fallback_colors,
                    key=lambda candidate: sum(
                        (source_color[channel] - candidate[channel]) ** 2
                        for channel in range(3)
                    ),
                )
                pixels[x, y] = (*replacement, 255)
    return cleaned


def downsample_palette_grid(
    image: Image.Image,
    size: tuple[int, int],
    colors: tuple[tuple[int, int, int], ...],
    priority_colors: tuple[tuple[tuple[int, int, int], float], ...],
) -> Image.Image:
    """Rasterize a tiny flag from master-pixel coverage only.

    Thin historic charges can disappear when a 1536x1024 source is averaged to
    10x7 and then snapped to its palette.  This deterministic grid sampler
    chooses each output pixel from source-cell coverage.  A documented minimum
    coverage preserves only already-existing charge pixels; all other cells use
    the dominant source color.  It draws no new shape and imports no reference
    geometry.
    """
    source = image.convert("RGB")
    output = Image.new("RGBA", size)
    target_width, target_height = size
    for target_y in range(target_height):
        top = target_y * source.height // target_height
        bottom = (target_y + 1) * source.height // target_height
        for target_x in range(target_width):
            left = target_x * source.width // target_width
            right = (target_x + 1) * source.width // target_width
            pixels = list(source.crop((left, top, right, bottom)).getdata())
            counts = {color: pixels.count(color) for color in colors}
            area = len(pixels)
            selected = None
            for color, threshold in priority_colors:
                if counts[color] / area >= threshold:
                    selected = color
                    break
            if selected is None:
                selected = max(colors, key=lambda color: counts[color])
            output.putpixel((target_x, target_y), (*selected, 255))
    return output


def map_sardinia_resized_pixels(image: Image.Image) -> Image.Image:
    """Prevent neutral head-edge blends from being misclassified as red.

    LANCZOS produces neutral grey pixels where the black heads meet the white
    field.  In a three-color nearest-palette mapping, some mid-greys are closer
    to civic red than to either endpoint.  Red is therefore reserved for
    source-resampled pixels with a clear red-channel lead; every other pixel is
    classified only as near-black or white by luminance.
    """
    white = (*FLAGS["ARX"]["palette"][0], 255)
    red = (*FLAGS["ARX"]["palette"][1], 255)
    black = (*FLAGS["ARX"]["palette"][2], 255)
    output = Image.new("RGBA", image.size)
    for coordinate, source in zip(
        ((x, y) for y in range(image.height) for x in range(image.width)),
        image.convert("RGB").getdata(),
    ):
        r, g, b = source
        if r - g >= 45 and r - b >= 35:
            color = red
        else:
            luminance = (299 * r + 587 * g + 114 * b) / 1000
            color = black if luminance < 132 else white
        output.putpixel(coordinate, color)
    return output


def map_resized_pixels(image: Image.Image, config: dict[str, object]) -> Image.Image:
    if config.get("resized_mapper") == "sardinia_red_or_monochrome":
        return map_sardinia_resized_pixels(image)
    return quantize_to_palette(image, config["palette"])


def write_bottom_origin_tga(image: Image.Image, output: Path) -> None:
    """Write an uncompressed 32-bit BGRA TGA with bottom-left origin."""
    rgba = image.convert("RGBA")
    width, height = rgba.size
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
    source = rgba.tobytes()
    stride = width * 4
    pixels = bytearray()
    for y in range(height - 1, -1, -1):
        row = source[y * stride : (y + 1) * stride]
        for index in range(0, len(row), 4):
            red, green, blue, alpha = row[index : index + 4]
            pixels.extend((blue, green, red, alpha))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(header + pixels)


def runtime_tga(tag: str, size_name: str) -> Path:
    if size_name == "normal":
        return FLAGS_ROOT / f"{tag}.tga"
    return FLAGS_ROOT / size_name / f"{tag}.tga"


def process_flags() -> dict[str, dict[str, Path]]:
    outputs: dict[str, dict[str, Path]] = {}
    for tag, config in FLAGS.items():
        raw_path = SOURCE_ROOT / str(config["raw"])
        master_path = SOURCE_ROOT / str(config["master"])
        flat = normalize_imagegen_source(
            raw_path,
            master_path,
            config["palette"],
            config.get("cross_cleanup"),
        )
        normal = map_resized_pixels(
            flat.resize(FLAG_SIZES["normal"], Image.Resampling.LANCZOS),
            config,
        )
        outputs[tag] = {
            "reference": config["reference"],
            "raw": raw_path,
            "master": master_path,
        }
        for size_name, size in FLAG_SIZES.items():
            image = normal
            if size_name == "small":
                image = downsample_palette_grid(
                    flat,
                    size,
                    config["palette"],
                    config["small_priority"],
                )
            elif size_name != "normal":
                image = map_resized_pixels(
                    normal.resize(size, Image.Resampling.LANCZOS),
                    config,
                )
            png_path = PROCESSED_ROOT / size_name / f"{tag}.png"
            image.save(png_path)
            tga_path = runtime_tga(tag, size_name)
            write_bottom_origin_tga(image, tga_path)
            outputs[tag][size_name] = png_path
            outputs[tag][f"{size_name}_tga"] = tga_path
    return outputs


def validate_flat_png(
    path: Path,
    size: tuple[int, int],
    colors: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    image = Image.open(path).convert("RGBA")
    if image.size != size:
        raise ValueError(f"Unexpected PNG dimensions: {path} ({image.size})")
    actual = set(image.getdata())
    expected = {(*color, 255) for color in colors}
    if not actual or not actual.issubset(expected):
        raise ValueError(f"Unexpected palette or alpha in {path}: {sorted(actual - expected)[:8]}")
    return {
        "dimensions": list(image.size),
        "mode": image.mode,
        "palette_rgb": [list(color[:3]) for color in sorted(actual)],
        "alpha_min": min(color[3] for color in actual),
        "alpha_max": max(color[3] for color in actual),
    }


def validate_tga(path: Path, size: tuple[int, int], png_path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    expected_length = 18 + size[0] * size[1] * 4
    if len(raw) != expected_length:
        raise ValueError(f"Unexpected TGA length: {path} ({len(raw)} != {expected_length})")
    values = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    image_type = values[2]
    width, height = values[8], values[9]
    depth, descriptor = values[10], values[11]
    if image_type != 2 or (width, height) != size or depth != 32:
        raise ValueError(f"Unexpected TGA header: {path}")
    if descriptor & 0x20:
        raise ValueError(f"Top-origin TGA is not permitted: {path}")
    if descriptor & 0x0F != 8:
        raise ValueError(f"TGA alpha descriptor is not eight-bit: {path}")
    decoded = Image.open(path).convert("RGBA")
    expected = Image.open(png_path).convert("RGBA")
    if decoded.size != expected.size or decoded.tobytes() != expected.tobytes():
        raise ValueError(f"TGA decode differs from processed PNG: {path}")
    return {
        "dimensions": [width, height],
        "image_type": image_type,
        "pixel_depth": depth,
        "alpha_bits": descriptor & 0x0F,
        "origin": "bottom-left",
        "bytes": len(raw),
        "decode_matches_processed_png": True,
    }


def validate_no_ideology_variants() -> None:
    for tag in FLAGS:
        for ideology in IDEOLOGIES:
            filename = f"{tag}_{ideology}.tga"
            for directory in (FLAGS_ROOT, FLAGS_ROOT / "medium", FLAGS_ROOT / "small"):
                path = directory / filename
                if path.exists():
                    raise ValueError(f"Unapproved ideology variant exists: {path}")


def validate_outputs(outputs: dict[str, dict[str, Path]]) -> dict[str, object]:
    report: dict[str, object] = {
        "pipeline": "official ImageGen raw -> no-dither nearest fixed-palette master -> LANCZOS normal/medium plus documented master-cell coverage sampling at 10x7 -> fixed-palette -> bottom-origin 32-bit BGRA TGA",
        "small_size_rule": {
            "purpose": "preserve only source-master charge pixels that otherwise vanish at 10x7",
            "method": "source-cell coverage threshold for documented priority colors; dominant source color otherwise",
            "thresholds": {
                tag: [
                    {"rgb": list(color), "minimum_cell_coverage": threshold}
                    for color, threshold in config["small_priority"]
                ]
                for tag, config in FLAGS.items()
            },
        },
        "master_cleanup": {
            "ARX": "detect full-span red rows and columns in the quantized ImageGen source, promote those spans to the red cross, and remap only off-cross red speckle to the closest white/black raw-pixel color",
            "ASX": "fixed-palette mapping only",
            "ICX": "fixed-palette mapping only",
        },
        "resized_palette_mapping": {
            "ARX": "reserve red for resampled pixels with a clear red-channel lead; classify neutral black/white edge blends by luminance so head antialiasing cannot become red speckle",
            "ASX": "nearest documented fixed palette without dithering",
            "ICX": "nearest documented fixed palette without dithering",
        },
        "ideology_variants": "none; no route-to-filename mapping is approved",
        "flags": {},
    }
    validate_no_ideology_variants()
    flag_report: dict[str, object] = {}
    for tag, config in FLAGS.items():
        record: dict[str, object] = {
            "raw": {
                "path": outputs[tag]["raw"].relative_to(ROOT).as_posix(),
                "dimensions": list(Image.open(outputs[tag]["raw"]).size),
                "mode": Image.open(outputs[tag]["raw"]).mode,
            },
            "flat_master": validate_flat_png(
                outputs[tag]["master"], (1536, 1024), config["palette"]
            ),
            "sizes": {},
        }
        record["flat_master"]["path"] = outputs[tag]["master"].relative_to(ROOT).as_posix()
        sizes: dict[str, object] = {}
        for size_name, size in FLAG_SIZES.items():
            png_path = outputs[tag][size_name]
            tga_path = outputs[tag][f"{size_name}_tga"]
            sizes[size_name] = {
                "processed_png": validate_flat_png(png_path, size, config["palette"]),
                "tga": validate_tga(tga_path, size, png_path),
            }
            sizes[size_name]["processed_png"]["path"] = png_path.relative_to(ROOT).as_posix()
            sizes[size_name]["tga"]["path"] = tga_path.relative_to(ROOT).as_posix()
        record["sizes"] = sizes
        flag_report[tag] = record
    report["flags"] = flag_report
    output = NOTES_ROOT / "validation.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def draw_contain(
    canvas: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
    *,
    nearest: bool = False,
) -> None:
    left, top, right, bottom = box
    fitted = ImageOps.contain(
        image.convert("RGBA"),
        (right - left, bottom - top),
        Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS,
    )
    x = left + (right - left - fitted.width) // 2
    y = top + (bottom - top - fitted.height) // 2
    canvas.alpha_composite(fitted, (x, y))


def centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    *,
    size: int,
    bold: bool = False,
    fill: str = "#f1f4f8",
) -> None:
    text_font = font(size, bold=bold)
    bounds = draw.textbbox((0, 0), text, font=text_font)
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    left, top, right, bottom = box
    draw.text(
        (left + (right - left - width) // 2, top + (bottom - top - height) // 2),
        text,
        font=text_font,
        fill=fill,
    )


def build_raw_master_sheet(outputs: dict[str, dict[str, Path]]) -> Path:
    card_w, card_h = 520, 410
    header_h = 92
    sheet = Image.new("RGBA", (card_w * len(FLAGS), header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (26, 17),
        "Event 006 - Mediterranean ImageGen provenance",
        font=font(29, bold=True),
        fill="#f4f0e8",
    )
    draw.text(
        (27, 54),
        "Licensed research aid | retained official ImageGen raw | deterministic no-dither flat master",
        font=font(16),
        fill="#b8c1cc",
    )
    for index, (tag, config) in enumerate(FLAGS.items()):
        left = index * card_w
        top = header_h
        draw.rounded_rectangle(
            (left + 10, top + 10, left + card_w - 10, top + card_h - 10),
            radius=10,
            fill="#252c35",
            outline="#5b6878",
            width=2,
        )
        centered_text(
            draw,
            f"{tag} - {config['label'].split(' - ', 1)[1]}",
            (left + 20, top + 20, left + card_w - 20, top + 55),
            size=17,
            bold=True,
        )
        columns = (
            ("research aid", Image.open(outputs[tag]["reference"]).convert("RGBA")),
            ("ImageGen raw", Image.open(outputs[tag]["raw"]).convert("RGBA")),
            ("flat master", Image.open(outputs[tag]["master"]).convert("RGBA")),
        )
        for column, (label, image) in enumerate(columns):
            x = left + 18 + column * 166
            draw_contain(sheet, image, (x, top + 70, x + 154, top + 292))
            centered_text(
                draw,
                label,
                (x, top + 300, x + 154, top + 326),
                size=14,
                bold=True,
                fill="#d5dbe3",
            )
        centered_text(
            draw,
            "Reference controls historical constraints; only ImageGen pixels enter the master.",
            (left + 18, top + 340, left + card_w - 18, top + 386),
            size=13,
            fill="#aeb9c6",
        )
    output = CONTACT_ROOT / "006_mediterranean_danube_imagegen_raw_vs_flat_contact_sheet.png"
    sheet.convert("RGB").save(output)
    return output


def build_final_ladder_sheet(outputs: dict[str, dict[str, Path]]) -> Path:
    card_w, card_h = 450, 430
    header_h = 92
    sheet = Image.new("RGBA", (card_w * len(FLAGS), header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (26, 17),
        "Event 006 - final HOI4 flag ladders",
        font=font(29, bold=True),
        fill="#f4f0e8",
    )
    draw.text(
        (27, 54),
        "Actual bottom-origin uncompressed 32-bit runtime TGAs reopened after conversion",
        font=font(16),
        fill="#b8c1cc",
    )
    for index, (tag, config) in enumerate(FLAGS.items()):
        left = index * card_w
        top = header_h
        draw.rounded_rectangle(
            (left + 10, top + 10, left + card_w - 10, top + card_h - 10),
            radius=10,
            fill="#252c35",
            outline="#5b6878",
            width=2,
        )
        centered_text(
            draw,
            tag,
            (left + 20, top + 18, left + card_w - 20, top + 52),
            size=20,
            bold=True,
        )
        normal = Image.open(outputs[tag]["normal_tga"]).convert("RGBA")
        medium = Image.open(outputs[tag]["medium_tga"]).convert("RGBA")
        small = Image.open(outputs[tag]["small_tga"]).convert("RGBA")
        draw_contain(
            sheet,
            normal.resize((328, 208), Image.Resampling.NEAREST),
            (left + 60, top + 64, left + 390, top + 274),
            nearest=True,
        )
        draw_contain(
            sheet,
            medium.resize((205, 130), Image.Resampling.NEAREST),
            (left + 28, top + 286, left + 235, top + 386),
            nearest=True,
        )
        draw_contain(
            sheet,
            small.resize((120, 84), Image.Resampling.NEAREST),
            (left + 290, top + 286, left + 412, top + 386),
            nearest=True,
        )
        centered_text(draw, "82x52", (left + 170, top + 264, left + 280, top + 291), size=13, fill="#aeb9c6")
        centered_text(draw, "41x26", (left + 70, top + 385, left + 180, top + 412), size=13, fill="#aeb9c6")
        centered_text(draw, "10x7", (left + 295, top + 385, left + 405, top + 412), size=13, fill="#aeb9c6")
    output = CONTACT_ROOT / "006_mediterranean_danube_final_tga_ladders_contact_sheet.png"
    sheet.convert("RGB").save(output)
    return output


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_hash_ledger(outputs: dict[str, dict[str, Path]], contact_paths: tuple[Path, ...]) -> None:
    paths: set[Path] = set(contact_paths)
    paths.add(NOTES_ROOT / "validation.json")
    paths.update(SOURCE_ROOT.glob("*.png"))
    for config in FLAGS.values():
        paths.add(config["reference"])
        paths.add(config["technical_reference"])
        paths.update(config["additional_references"])
    for output in outputs.values():
        paths.update(output.values())
    rows = [
        f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}"
        for path in sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix().lower())
    ]
    (PACKAGE_ROOT / "hashes.sha256").write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> int:
    prepare_directories()
    outputs = process_flags()
    validate_outputs(outputs)
    raw_sheet = build_raw_master_sheet(outputs)
    final_sheet = build_final_ladder_sheet(outputs)
    write_hash_ledger(outputs, (raw_sheet, final_sheet))
    print("Built 3 official-ImageGen-derived flag masters and 9 runtime TGAs.")
    print(f"Package: {PACKAGE_ROOT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
