#!/usr/bin/env python3
"""Build the generated Event 006 northern/western Europe art package.

The source rasters in ``source_png/generated_nwe`` were created independently
with ImageGen. Historical flag generation used cited flat design references and
the canonical vanilla HOI4 flag ladder. This script only performs deterministic
palette normalisation, a recorded minimal scanline cleanup on ImageGen pixels,
resizing, legacy portrait finishing, format conversion, validation, hash
inventory generation, and contact-sheet assembly. Portraits approved through
the dedicated HOI4 portrait processor are preserved byte-for-byte at the PNG
stage and only reconverted or decoded here. The script never imports masks,
traces reference art, redraws flag geometry, or invents small-size variants.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
import subprocess
import sys
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_ROOT = ASSET_ROOT / "source_png" / "generated_nwe"
PROCESSED_ROOT = ASSET_ROOT / "processed_png" / "generated_nwe"
DECODED_ROOT = ASSET_ROOT / "dds_decoded_png" / "generated_nwe"
CONTACT_ROOT = ASSET_ROOT / "contact_sheets"
FLAGS_ROOT = ROOT / "gfx" / "flags"
PORTRAITS_ROOT = ROOT / "gfx" / "leaders" / "006_independence_wave"
DDS_CONVERTER = ROOT / ".tools" / "convert_to_dds.py"
HASH_LEDGER = ASSET_ROOT / "generated_nwe_hashes.sha256"
VANILLA_FLAG_REFERENCE_ROOT = (
    ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "vanilla_reference"
    / "flags"
)


def vanilla_flag_ladder(stem: str) -> tuple[Path, Path, Path]:
    return tuple(
        VANILLA_FLAG_REFERENCE_ROOT / size_name / f"{stem}.png"
        for size_name in ("normal", "medium", "small")
    )


FLAGS = {
    "ACX": {
        "label": "St Piran's Cross",
        "raw_source": "ACX_st_pirans_cross_imagegen_raw.png",
        "flat_master": "ACX_st_pirans_cross_imagegen_flat_master.png",
        "design_reference": ASSET_ROOT / "source_png" / "country_symbols" / "acx_st_pirans_cross_source.png",
        "vanilla_ladder": vanilla_flag_ladder("arm"),
        "palette": ((0, 0, 0), (255, 255, 255)),
        "majority_scanline_cleanup": ((255, 255, 255), 0.65),
    },
    "AFX": {
        "label": "1913 Walloon coq hardi",
        "raw_source": "AFX_walloon_coq_hardi_1913_imagegen_raw.png",
        "flat_master": "AFX_walloon_coq_hardi_1913_imagegen_flat_master.png",
        "design_reference": ASSET_ROOT / "source_png" / "country_symbols" / "afx_walloon_rooster_source.png",
        "vanilla_ladder": vanilla_flag_ladder("isr"),
        "palette": ((255, 209, 0), (228, 0, 43)),
    },
    "AGX": {
        "label": "Friesland provincial flag",
        "raw_source": "AGX_friesland_provincial_imagegen_raw.png",
        "flat_master": "AGX_friesland_provincial_imagegen_flat_master.png",
        "design_reference": ASSET_ROOT / "source_png" / "country_symbols" / "agx_west_frisian_flag_source.png",
        "vanilla_ladder": vanilla_flag_ladder("ice"),
        "palette": ((36, 73, 148), (255, 255, 255), (231, 35, 38)),
    },
    "AJX": {
        "label": "Saar Territory, 1920-1935",
        "raw_source": "AJX_saar_territory_1920_1935_imagegen_raw.png",
        "flat_master": "AJX_saar_territory_1920_1935_imagegen_flat_master.png",
        "design_reference": ASSET_ROOT / "source_png" / "country_symbols" / "ajx_saar_territory_1920_1935_source.png",
        "vanilla_ladder": vanilla_flag_ladder("arm"),
        "palette": ((0, 32, 159), (255, 255, 255), (0, 0, 0)),
    },
}

OBSOLETE_CIVIC_FLAG_SOURCES = tuple(
    SOURCE_ROOT / "flags" / f"{tag}_civic_baseline_generated_source.png"
    for tag in ("ACX", "AEX", "AFX", "AGX", "AJX")
)

RETIRED_AEX_FLAG_PATHS = (
    PROCESSED_ROOT / "flags" / "normal" / "AEX.png",
    PROCESSED_ROOT / "flags" / "medium" / "AEX.png",
    PROCESSED_ROOT / "flags" / "small" / "AEX.png",
    FLAGS_ROOT / "AEX.tga",
    FLAGS_ROOT / "medium" / "AEX.tga",
    FLAGS_ROOT / "small" / "AEX.tga",
)

FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

PORTRAITS = {
    "institutional": {
        "ACX": {
            "stem": "portrait_ACX_cornish_port_and_mines_committee",
            "label": "Cornish Port and Mines Security Committee",
        },
        "AEX": {
            "stem": "portrait_AEX_flemish_civil_industrial_board",
            "label": "Flemish Civil-Industrial Security Board",
        },
        "AFX": {
            "stem": "portrait_AFX_walloon_provisional_assembly",
            "label": "Walloon Provisional Assembly",
        },
        "AGX": {
            "stem": "portrait_AGX_friesland_coastal_council",
            "label": "Friesland Coastal Council",
        },
        "AJX": {
            "stem": "portrait_AJX_saar_municipal_neutral_commission",
            "label": "Saar Municipal Neutral Commission",
        },
    },
    "command": {
        "ACX": {
            "stem": "portrait_ACX_cornish_coastal_commander",
            "label": "Thomas Trevorrow — coastal commander",
        },
        "AEX": {
            "stem": "portrait_AEX_flemish_industrial_security_commander",
            "label": "Hendrik Vermeulen — industrial-security commander",
        },
        "AFX": {
            "stem": "portrait_AFX_walloon_reserve_commander",
            "label": "Marcel Delcourt — reserve commander",
        },
        "AGX": {
            "stem": "portrait_AGX_friesland_coastal_commander",
            "label": "Sjoerd Hoekstra — coastal commander",
        },
        "AJX": {
            "stem": "portrait_AJX_saar_industrial_security_commissioner",
            "label": "Karl Becker — industrial-security commissioner",
        },
    },
}

# These masters were separately finished, compared with canonical vanilla
# portraits, and approved through .tools/process_hoi4_portrait.py. Rebuilding
# this broader package must never replace those reviewed PNGs with the older
# generic finish_portrait path.
EXTERNALLY_APPROVED_PORTRAIT_STEMS = {
    "portrait_AFX_walloon_provisional_assembly",
    "portrait_AFX_walloon_reserve_commander",
    "portrait_AGX_friesland_coastal_council",
    "portrait_AGX_friesland_coastal_commander",
}


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidates = (
        Path("C:/Windows/Fonts") / filename,
        Path(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ),
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def prepare_directories() -> None:
    directories = [
        PROCESSED_ROOT / "flags" / size_name for size_name in FLAG_SIZES
    ]
    directories.extend(
        [
            SOURCE_ROOT / "flags",
            PROCESSED_ROOT / "institutional_portraits",
            PROCESSED_ROOT / "command_portraits",
            PROCESSED_ROOT / "command_portraits_small",
            DECODED_ROOT / "institutional_portraits",
            DECODED_ROOT / "command_portraits",
            DECODED_ROOT / "command_portraits_small",
            CONTACT_ROOT,
            FLAGS_ROOT / "medium",
            FLAGS_ROOT / "small",
            PORTRAITS_ROOT,
        ]
    )
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def retire_obsolete_flag_artifacts() -> None:
    """Remove only the superseded civic masters and retired AEX runtime family."""
    for path in (*OBSOLETE_CIVIC_FLAG_SOURCES, *RETIRED_AEX_FLAG_PATHS):
        path.unlink(missing_ok=True)


def fixed_palette_image(colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
    palette = Image.new("P", (1, 1))
    values: list[int] = []
    for color in colors:
        values.extend(color)
    while len(values) < 768:
        values.extend(colors[-1])
    palette.putpalette(values[:768])
    return palette


def quantize_to_palette(image: Image.Image, colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
    palette = fixed_palette_image(colors)
    quantized = image.convert("RGB").quantize(palette=palette, dither=Image.Dither.NONE)
    return quantized.convert("RGBA")


def clean_majority_scanlines(
    image: Image.Image,
    target: tuple[int, int, int],
    threshold: float,
) -> Image.Image:
    """Promote almost-solid scanlines left by ImageGen edge noise.

    The rule uses only the quantized ImageGen pixels. It neither imports a mask
    nor traces/reconstructs geometry from the cited design reference.
    """
    cleaned = image.convert("RGBA")
    pixels = cleaned.load()
    target_rgba = (*target, 255)
    for y in range(cleaned.height):
        matches = sum(pixels[x, y][:3] == target for x in range(cleaned.width))
        if threshold < matches / cleaned.width < 1.0:
            for x in range(cleaned.width):
                pixels[x, y] = target_rgba
    for x in range(cleaned.width):
        matches = sum(pixels[x, y][:3] == target for y in range(cleaned.height))
        if threshold < matches / cleaned.height < 1.0:
            for y in range(cleaned.height):
                pixels[x, y] = target_rgba
    return cleaned


def normalize_imagegen_flag_source(
    raw_source: Path,
    flat_master: Path,
    colors: tuple[tuple[int, int, int], ...],
    majority_scanline_cleanup: tuple[tuple[int, int, int], float] | None = None,
) -> Image.Image:
    """Flatten one ImageGen raster without redrawing or replacing its geometry."""
    image = Image.open(raw_source).convert("RGBA")
    if image.width * 2 != image.height * 3:
        raise ValueError(f"ImageGen flag source is not exactly 3:2: {raw_source} ({image.size})")
    flat = quantize_to_palette(image, colors)
    if majority_scanline_cleanup is not None:
        flat = clean_majority_scanlines(flat, *majority_scanline_cleanup)
    flat.save(flat_master)
    return flat


def write_bottom_origin_tga(image: Image.Image, output: Path) -> None:
    """Write uncompressed 32-bit BGRA TGA with a bottom-left origin."""
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


def process_flags() -> dict[str, dict[str, Path]]:
    outputs: dict[str, dict[str, Path]] = {}
    for tag, config in FLAGS.items():
        raw_source = SOURCE_ROOT / "flags" / str(config["raw_source"])
        flat_master = SOURCE_ROOT / "flags" / str(config["flat_master"])
        source = normalize_imagegen_flag_source(
            raw_source,
            flat_master,
            config["palette"],
            config.get("majority_scanline_cleanup"),
        )
        normal = source.resize(FLAG_SIZES["normal"], Image.Resampling.LANCZOS)
        normal = quantize_to_palette(normal, config["palette"])
        outputs[tag] = {
            "raw": raw_source,
            "flat_master": flat_master,
            "design_reference": config["design_reference"],
        }
        for size_name, size in FLAG_SIZES.items():
            if size_name == "normal":
                image = normal
            else:
                image = normal.resize(size, Image.Resampling.LANCZOS)
                image = quantize_to_palette(image, config["palette"])
            png_output = PROCESSED_ROOT / "flags" / size_name / f"{tag}.png"
            image.save(png_output)
            if size_name == "normal":
                tga_output = FLAGS_ROOT / f"{tag}.tga"
            else:
                tga_output = FLAGS_ROOT / size_name / f"{tag}.tga"
            write_bottom_origin_tga(image, tga_output)
            outputs[tag][size_name] = png_output
    return outputs


def finish_portrait(source: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = ImageOps.fit(
        source.convert("RGB"),
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.46),
    )
    image = ImageOps.autocontrast(image, cutoff=0.35)
    image = ImageEnhance.Color(image).enhance(0.92)
    image = ImageEnhance.Contrast(image).enhance(1.035)
    image = image.filter(ImageFilter.UnsharpMask(radius=0.72, percent=92, threshold=2))
    return image.convert("RGBA")


def convert_dds(png_path: Path, dds_path: Path, size: tuple[int, int]) -> None:
    command = [
        sys.executable,
        str(DDS_CONVERTER),
        "--input",
        str(png_path),
        "--output",
        str(dds_path),
        "--width",
        str(size[0]),
        "--height",
        str(size[1]),
    ]
    result = subprocess.run(command, check=False, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(
            f"DDS conversion failed for {png_path}:\n{result.stdout}\n{result.stderr}"
        )


def decode_bgra_dds(path: Path) -> Image.Image:
    raw = path.read_bytes()
    validate_dds(path)
    height, width = struct.unpack_from("<II", raw, 12)
    data = raw[128:]
    rgba = bytearray(len(data))
    for index in range(0, len(data), 4):
        blue, green, red, alpha = data[index : index + 4]
        rgba[index : index + 4] = bytes((red, green, blue, alpha))
    return Image.frombytes("RGBA", (width, height), bytes(rgba))


def process_portraits() -> dict[str, dict[str, dict[str, Path]]]:
    outputs: dict[str, dict[str, dict[str, Path]]] = {"institutional": {}, "command": {}}
    for category, records in PORTRAITS.items():
        source_directory = SOURCE_ROOT / f"{category}_portraits"
        processed_directory = PROCESSED_ROOT / f"{category}_portraits"
        decoded_directory = DECODED_ROOT / f"{category}_portraits"
        for tag, record in records.items():
            stem = str(record["stem"])
            png_output = processed_directory / f"{stem}.png"
            if stem in EXTERNALLY_APPROVED_PORTRAIT_STEMS:
                if not png_output.exists():
                    raise FileNotFoundError(
                        f"Missing externally approved portrait PNG: {png_output}"
                    )
                large = Image.open(png_output).convert("RGBA")
                if large.size != (156, 210):
                    raise ValueError(
                        f"Unexpected approved portrait dimensions: {png_output} ({large.size})"
                    )
            else:
                source = Image.open(source_directory / f"{stem}_source.png")
                large = finish_portrait(source, (156, 210))
                large.save(png_output)
            dds_output = PORTRAITS_ROOT / f"{stem}.dds"
            convert_dds(png_output, dds_output, (156, 210))
            decoded_output = decoded_directory / f"{stem}.png"
            decoded = decode_bgra_dds(dds_output)
            if stem in EXTERNALLY_APPROVED_PORTRAIT_STEMS and decoded_output.exists():
                retained_decode = Image.open(decoded_output).convert("RGBA")
                if retained_decode.size != decoded.size or retained_decode.tobytes() != decoded.tobytes():
                    raise ValueError(
                        f"Approved decoded portrait no longer matches runtime DDS: {decoded_output}"
                    )
            else:
                decoded.save(decoded_output)
            outputs[category][tag] = {
                "source": source_directory / f"{stem}_source.png",
                "processed": png_output,
                "dds": dds_output,
                "decoded": decoded_output,
            }

            if category == "command":
                small_png = PROCESSED_ROOT / "command_portraits_small" / f"{stem}_small.png"
                if stem in EXTERNALLY_APPROVED_PORTRAIT_STEMS:
                    if not small_png.exists():
                        raise FileNotFoundError(
                            f"Missing externally approved army-thumbnail PNG: {small_png}"
                        )
                    small = Image.open(small_png).convert("RGBA")
                    if small.size != (50, 67):
                        raise ValueError(
                            f"Unexpected approved army-thumbnail dimensions: {small_png} ({small.size})"
                        )
                else:
                    small = finish_portrait(large, (50, 67))
                    small.save(small_png)
                small_dds = PORTRAITS_ROOT / f"{stem}_small.dds"
                convert_dds(small_png, small_dds, (50, 67))
                small_decoded = DECODED_ROOT / "command_portraits_small" / f"{stem}_small.png"
                decoded_small = decode_bgra_dds(small_dds)
                if stem in EXTERNALLY_APPROVED_PORTRAIT_STEMS and small_decoded.exists():
                    retained_small_decode = Image.open(small_decoded).convert("RGBA")
                    if (
                        retained_small_decode.size != decoded_small.size
                        or retained_small_decode.tobytes() != decoded_small.tobytes()
                    ):
                        raise ValueError(
                            "Approved decoded army thumbnail no longer matches "
                            f"runtime DDS: {small_decoded}"
                        )
                else:
                    decoded_small.save(small_decoded)
                outputs[category][tag].update(
                    {
                        "small_processed": small_png,
                        "small_dds": small_dds,
                        "small_decoded": small_decoded,
                    }
                )
    return outputs


def validate_tga(path: Path, size: tuple[int, int]) -> None:
    raw = path.read_bytes()
    if len(raw) != 18 + size[0] * size[1] * 4:
        raise ValueError(f"Unexpected TGA length: {path}")
    values = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    image_type, width, height, depth, descriptor = values[2], values[8], values[9], values[10], values[11]
    if image_type != 2 or (width, height) != size or depth != 32:
        raise ValueError(f"Unexpected TGA header: {path}")
    if descriptor & 0x20:
        raise ValueError(f"Top-origin TGA is not permitted: {path}")
    if descriptor & 0x0F != 8:
        raise ValueError(f"TGA alpha descriptor is not 8-bit: {path}")


def validate_flat_flag_png(
    path: Path,
    size: tuple[int, int],
    colors: tuple[tuple[int, int, int], ...],
) -> None:
    image = Image.open(path).convert("RGBA")
    if image.size != size:
        raise ValueError(f"Unexpected flat flag size: {path} ({image.size})")
    pixels = set(image.getdata())
    expected = {(*color, 255) for color in colors}
    if not pixels or not pixels.issubset(expected):
        unexpected = sorted(pixels - expected)[:8]
        raise ValueError(f"Unexpected colors or alpha in flat flag: {path}: {unexpected}")


def validate_dds(path: Path) -> None:
    raw = path.read_bytes()
    if len(raw) < 128 or raw[:4] != b"DDS ":
        raise ValueError(f"Invalid DDS magic/header: {path}")
    header_size = struct.unpack_from("<I", raw, 4)[0]
    height = struct.unpack_from("<I", raw, 12)[0]
    width = struct.unpack_from("<I", raw, 16)[0]
    pitch = struct.unpack_from("<I", raw, 20)[0]
    pf_size = struct.unpack_from("<I", raw, 76)[0]
    pf_flags = struct.unpack_from("<I", raw, 80)[0]
    rgb_bits = struct.unpack_from("<I", raw, 88)[0]
    masks = struct.unpack_from("<IIII", raw, 92)
    caps = struct.unpack_from("<I", raw, 108)[0]
    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    if header_size != 124 or pf_size != 32 or pf_flags != 0x41 or rgb_bits != 32:
        raise ValueError(f"DDS is not uncompressed 32-bit BGRA: {path}")
    if masks != expected_masks or caps != 0x1000 or pitch != width * 4:
        raise ValueError(f"Unexpected DDS masks/caps/pitch: {path}")
    if len(raw) != 128 + width * height * 4:
        raise ValueError(f"Unexpected DDS payload length: {path}")


def draw_contain(
    canvas: Image.Image,
    image: Image.Image,
    box: tuple[int, int, int, int],
    *,
    nearest: bool = False,
) -> None:
    left, top, right, bottom = box
    target = image.copy().convert("RGBA")
    resampling = Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS
    target.thumbnail((right - left, bottom - top), resampling)
    x = left + ((right - left) - target.width) // 2
    y = top + ((bottom - top) - target.height) // 2
    canvas.alpha_composite(target, (x, y))


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    *,
    size: int,
    bold: bool = False,
    fill: str = "#f4f0e8",
    wrap_width: int = 34,
) -> None:
    left, top, right, _ = box
    text_font = font(size, bold=bold)
    y = top
    for line in wrap(text, width=wrap_width):
        bounds = draw.textbbox((0, 0), line, font=text_font)
        width = bounds[2] - bounds[0]
        draw.text((left + ((right - left) - width) // 2, y), line, font=text_font, fill=fill)
        y += size + 4


def build_flag_contact_sheet() -> Path:
    card_w, card_h = 390, 390
    header_h = 88
    sheet = Image.new("RGBA", (card_w * len(FLAGS), header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 18), "Event 006 — live historical country flags", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Actual bottom-origin uncompressed 32-bit TGA triplets; no small-size redesign", font=font(16), fill="#b8c1cc")
    for index, (tag, config) in enumerate(FLAGS.items()):
        left = index * card_w
        top = header_h
        draw.rounded_rectangle((left + 10, top + 10, left + card_w - 10, top + card_h - 10), radius=10, fill="#252c35", outline="#5b6878", width=2)
        normal = Image.open(FLAGS_ROOT / f"{tag}.tga").convert("RGBA")
        medium = Image.open(FLAGS_ROOT / "medium" / f"{tag}.tga").convert("RGBA")
        small = Image.open(FLAGS_ROOT / "small" / f"{tag}.tga").convert("RGBA")
        draw_centered_lines(draw, f"{tag} — {config['label']}", (left + 18, top + 22, left + card_w - 18, top + 62), size=17, bold=True, wrap_width=31)
        draw_contain(sheet, normal.resize((296, 188), Image.Resampling.NEAREST), (left + 46, top + 64, left + 344, top + 254), nearest=True)
        draw_contain(sheet, medium.resize((164, 104), Image.Resampling.NEAREST), (left + 35, top + 264, left + 205, top + 346), nearest=True)
        draw_contain(sheet, small.resize((100, 70), Image.Resampling.NEAREST), (left + 238, top + 264, left + 345, top + 346), nearest=True)
        draw.text((left + 151, top + 246), "82×52", font=font(13), fill="#aeb9c6")
        draw.text((left + 41, top + 350), "41×26", font=font(13), fill="#aeb9c6")
        draw.text((left + 269, top + 350), "10×7", font=font(13), fill="#aeb9c6")
    output = CONTACT_ROOT / "006_nwe_generated_flags_contact_sheet.png"
    sheet.convert("RGB").save(output, quality=95)
    return output


def build_flag_raw_flat_comparison_sheet(
    flag_outputs: dict[str, dict[str, Path]],
) -> Path:
    card_w, card_h = 470, 340
    header_h = 92
    sheet = Image.new("RGBA", (card_w * len(FLAGS), header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (28, 18),
        "Event 006 — ImageGen provenance and flat normalization",
        font=font(29, bold=True),
        fill="#f4f0e8",
    )
    draw.text(
        (29, 53),
        "Cited design reference | official ImageGen raw | deterministic flat master; geometry is never redrawn",
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
        draw_centered_lines(
            draw,
            f"{tag} — {config['label']}",
            (left + 20, top + 22, left + card_w - 20, top + 55),
            size=17,
            bold=True,
            wrap_width=38,
        )
        images = (
            ("cited design", Image.open(flag_outputs[tag]["design_reference"]).convert("RGBA")),
            ("ImageGen raw", Image.open(flag_outputs[tag]["raw"]).convert("RGBA")),
            ("flat master", Image.open(flag_outputs[tag]["flat_master"]).convert("RGBA")),
        )
        for column, (label, image) in enumerate(images):
            box_left = left + 22 + column * 148
            draw_contain(sheet, image, (box_left, top + 72, box_left + 134, top + 246))
            label_font = font(13, bold=True)
            label_bounds = draw.textbbox((0, 0), label, font=label_font)
            label_width = label_bounds[2] - label_bounds[0]
            draw.text(
                (box_left + (134 - label_width) // 2, top + 255),
                label,
                font=label_font,
                fill="#d5dbe3",
            )
        draw_centered_lines(
            draw,
            "Flat master uses nearest-palette cleanup; ACX also promotes one noisy cross-edge scanline. No masks or tracing.",
            (left + 24, top + 282, left + card_w - 24, top + card_h - 18),
            size=13,
            fill="#aeb9c6",
            wrap_width=58,
        )
    output = CONTACT_ROOT / "006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png"
    sheet.convert("RGB").save(output, quality=95)
    return output


def build_portrait_contact_sheet(
    category: str,
    portrait_outputs: dict[str, dict[str, dict[str, Path]]],
) -> Path:
    card_w, card_h = 320, 390
    header_h = 88
    sheet = Image.new("RGBA", (card_w * 5, header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    title = "institutional councils" if category == "institutional" else "regional officers"
    draw.text((28, 18), f"Event 006 — generated {title}", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Independent fictional ImageGen sources; final 156×210 portrait crop shown", font=font(16), fill="#b8c1cc")
    for index, (tag, record) in enumerate(PORTRAITS[category].items()):
        left = index * card_w
        top = header_h
        draw.rounded_rectangle((left + 10, top + 10, left + card_w - 10, top + card_h - 10), radius=10, fill="#252c35", outline="#5b6878", width=2)
        final_image = Image.open(portrait_outputs[category][tag]["processed"]).convert("RGBA")
        draw_contain(sheet, final_image.resize((218, 294), Image.Resampling.LANCZOS), (left + 50, top + 28, left + 270, top + 324))
        draw_centered_lines(draw, f"{tag} — {record['label']}", (left + 22, top + 328, left + card_w - 22, top + card_h - 18), size=16, bold=True, wrap_width=31)
    output = CONTACT_ROOT / f"006_nwe_generated_{category}_portraits_contact_sheet.png"
    sheet.convert("RGB").save(output, quality=95)
    return output


def build_decoded_contact_sheet(
    portrait_outputs: dict[str, dict[str, dict[str, Path]]]
) -> tuple[Path, Path]:
    card_w, card_h = 300, 360
    header_h = 88
    sheet = Image.new("RGBA", (card_w * 5, header_h + card_h * 2), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 18), "Event 006 — final generated portrait DDS decode", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Actual runtime files decoded after conversion: 156×210 uncompressed BGRA", font=font(16), fill="#b8c1cc")
    for row, category in enumerate(("institutional", "command")):
        for column, (tag, record) in enumerate(PORTRAITS[category].items()):
            left = column * card_w
            top = header_h + row * card_h
            draw.rounded_rectangle((left + 10, top + 10, left + card_w - 10, top + card_h - 10), radius=10, fill="#252c35", outline="#5b6878", width=2)
            image = Image.open(portrait_outputs[category][tag]["decoded"]).convert("RGBA")
            draw_contain(sheet, image.resize((202, 272), Image.Resampling.NEAREST), (left + 48, top + 24, left + 252, top + 298), nearest=True)
            draw_centered_lines(draw, f"{tag} — {record['label']}", (left + 20, top + 302, left + card_w - 20, top + card_h - 14), size=15, bold=True, wrap_width=31)
    large_output = CONTACT_ROOT / "006_nwe_generated_final_dds_decoded_contact_sheet.png"
    sheet.convert("RGB").save(large_output, quality=95)

    small_sheet = Image.new("RGBA", (240 * 5, 230), "#161b22")
    small_draw = ImageDraw.Draw(small_sheet)
    small_draw.text((24, 14), "Event 006 — final officer thumbnail DDS decode", font=font(25, bold=True), fill="#f4f0e8")
    small_draw.text((25, 45), "Actual 50×67 army portrait files, enlarged with nearest-neighbour sampling", font=font(15), fill="#b8c1cc")
    for column, (tag, record) in enumerate(PORTRAITS["command"].items()):
        left = column * 240
        image = Image.open(portrait_outputs["command"][tag]["small_decoded"]).convert("RGBA")
        draw_contain(small_sheet, image.resize((150, 201), Image.Resampling.NEAREST), (left + 45, 68, left + 195, 202), nearest=True)
        draw_centered_lines(small_draw, f"{tag} — {record['label'].split(' — ')[0]}", (left + 10, 202, left + 230, 226), size=15, bold=True, wrap_width=25)
    small_output = CONTACT_ROOT / "006_nwe_generated_officer_small_dds_decoded_contact_sheet.png"
    small_sheet.convert("RGB").save(small_output, quality=95)
    return large_output, small_output


def runtime_flag_paths() -> list[Path]:
    paths: list[Path] = []
    for tag in FLAGS:
        paths.extend((FLAGS_ROOT / f"{tag}.tga", FLAGS_ROOT / "medium" / f"{tag}.tga", FLAGS_ROOT / "small" / f"{tag}.tga"))
    return paths


def runtime_portrait_paths() -> list[Path]:
    paths: list[Path] = []
    for category, records in PORTRAITS.items():
        for record in records.values():
            stem = str(record["stem"])
            paths.append(PORTRAITS_ROOT / f"{stem}.dds")
            if category == "command":
                paths.append(PORTRAITS_ROOT / f"{stem}_small.dds")
    return paths


def validate_flag_outputs() -> None:
    for tag, config in FLAGS.items():
        flat_master = SOURCE_ROOT / "flags" / str(config["flat_master"])
        validate_flat_flag_png(flat_master, (1536, 1024), config["palette"])
        for size_name, size in FLAG_SIZES.items():
            validate_flat_flag_png(
                PROCESSED_ROOT / "flags" / size_name / f"{tag}.png",
                size,
                config["palette"],
            )
        validate_tga(FLAGS_ROOT / f"{tag}.tga", FLAG_SIZES["normal"])
        validate_tga(FLAGS_ROOT / "medium" / f"{tag}.tga", FLAG_SIZES["medium"])
        validate_tga(FLAGS_ROOT / "small" / f"{tag}.tga", FLAG_SIZES["small"])

    for path in RETIRED_AEX_FLAG_PATHS:
        if path.exists():
            raise ValueError(f"Retired standalone AEX flag artifact still exists: {path}")


def validate_portrait_outputs() -> None:
    for path in runtime_portrait_paths():
        validate_dds(path)


def write_hash_ledger() -> None:
    paths: list[Path] = []
    for directory in (SOURCE_ROOT, PROCESSED_ROOT, DECODED_ROOT):
        paths.extend(path for path in directory.rglob("*") if path.is_file())
    for config in FLAGS.values():
        paths.append(config["design_reference"])
        paths.extend(config["vanilla_ladder"])
    paths.extend(CONTACT_ROOT.glob("006_nwe_generated_*.png"))
    paths.extend(runtime_flag_paths())
    paths.extend(runtime_portrait_paths())
    rows = []
    for path in sorted(set(paths), key=lambda item: item.relative_to(ROOT).as_posix().lower()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    HASH_LEDGER.write_text("\n".join(rows) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scope",
        choices=("all", "flags", "portraits"),
        default="all",
        help="Build all assets or restrict the run to one non-overlapping package surface.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prepare_directories()
    retire_obsolete_flag_artifacts()

    if args.scope in ("all", "flags"):
        flag_outputs = process_flags()
        validate_flag_outputs()
        build_flag_contact_sheet()
        build_flag_raw_flat_comparison_sheet(flag_outputs)

    if args.scope in ("all", "portraits"):
        portrait_outputs = process_portraits()
        validate_portrait_outputs()
        build_portrait_contact_sheet("institutional", portrait_outputs)
        build_portrait_contact_sheet("command", portrait_outputs)
        build_decoded_contact_sheet(portrait_outputs)

    write_hash_ledger()
    if args.scope == "flags":
        print("Built 4 live historical flag triplets; retired standalone AEX flag artifacts.")
    elif args.scope == "portraits":
        print("Built 10 large portraits and 5 officer thumbnails; retired standalone AEX flag artifacts.")
    else:
        print("Built 4 live historical flag triplets, 10 large portraits, and 5 officer thumbnails; retired standalone AEX flag artifacts.")
    print(f"Hash ledger: {HASH_LEDGER.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
