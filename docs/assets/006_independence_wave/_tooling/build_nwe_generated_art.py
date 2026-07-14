#!/usr/bin/env python3
"""Build the generated Event 006 northern/western Europe art package.

The source rasters in ``source_png/generated_nwe`` were created independently
with ImageGen.  This script only performs deterministic crops, palette
normalisation, resizing, tonal finishing, format conversion, validation, hash
inventory generation, and contact-sheet assembly.
"""

from __future__ import annotations

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


FLAGS = {
    "ACX": {
        "label": "Cornish civic baseline",
        "source": "ACX_civic_baseline_generated_source.png",
        "palette": ((7, 8, 9), (247, 246, 239)),
    },
    "AEX": {
        "label": "Flemish civic-industrial baseline",
        "source": "AEX_civic_baseline_generated_source.png",
        "palette": ((10, 10, 10), (238, 184, 0), (188, 20, 30)),
    },
    "AFX": {
        "label": "Walloon provisional baseline",
        "source": "AFX_civic_baseline_generated_source.png",
        "palette": ((151, 9, 43), (242, 188, 24)),
    },
    "AGX": {
        "label": "West Frisian civic baseline",
        "source": "AGX_civic_baseline_generated_source.png",
        "palette": ((31, 77, 144), (245, 244, 237), (194, 28, 42)),
    },
    "AJX": {
        "label": "Saar municipal baseline",
        "source": "AJX_civic_baseline_generated_source.png",
        "palette": ((21, 51, 145), (246, 245, 240), (8, 9, 10)),
    },
}

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
        source = Image.open(SOURCE_ROOT / "flags" / str(config["source"])).convert("RGB")
        normal = ImageOps.fit(
            source,
            FLAG_SIZES["normal"],
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        normal = quantize_to_palette(normal, config["palette"])
        outputs[tag] = {}
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
            source = Image.open(source_directory / f"{stem}_source.png")
            large = finish_portrait(source, (156, 210))
            png_output = processed_directory / f"{stem}.png"
            large.save(png_output)
            dds_output = PORTRAITS_ROOT / f"{stem}.dds"
            convert_dds(png_output, dds_output, (156, 210))
            decoded_output = decoded_directory / f"{stem}.png"
            decode_bgra_dds(dds_output).save(decoded_output)
            outputs[category][tag] = {
                "source": source_directory / f"{stem}_source.png",
                "processed": png_output,
                "dds": dds_output,
                "decoded": decoded_output,
            }

            if category == "command":
                small = finish_portrait(large, (50, 67))
                small_png = PROCESSED_ROOT / "command_portraits_small" / f"{stem}_small.png"
                small.save(small_png)
                small_dds = PORTRAITS_ROOT / f"{stem}_small.dds"
                convert_dds(small_png, small_dds, (50, 67))
                small_decoded = DECODED_ROOT / "command_portraits_small" / f"{stem}_small.png"
                decode_bgra_dds(small_dds).save(small_decoded)
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
    sheet = Image.new("RGBA", (card_w * 5, header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text((28, 18), "Event 006 — generated civic baseline flags", font=font(29, bold=True), fill="#f4f0e8")
    draw.text((29, 53), "Final bottom-origin 32-bit TGA triplets; designs are fictional, not historical state flags", font=font(16), fill="#b8c1cc")
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
        draw.text((left + 41, top + 350), "41×26", font=font(13), fill="#aeb9c6")
        draw.text((left + 269, top + 350), "10×7", font=font(13), fill="#aeb9c6")
    output = CONTACT_ROOT / "006_nwe_generated_flags_contact_sheet.png"
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


def validate_outputs() -> None:
    for tag in FLAGS:
        validate_tga(FLAGS_ROOT / f"{tag}.tga", FLAG_SIZES["normal"])
        validate_tga(FLAGS_ROOT / "medium" / f"{tag}.tga", FLAG_SIZES["medium"])
        validate_tga(FLAGS_ROOT / "small" / f"{tag}.tga", FLAG_SIZES["small"])
    for path in runtime_portrait_paths():
        validate_dds(path)


def write_hash_ledger() -> None:
    paths: list[Path] = []
    for directory in (SOURCE_ROOT, PROCESSED_ROOT, DECODED_ROOT):
        paths.extend(path for path in directory.rglob("*") if path.is_file())
    paths.extend(CONTACT_ROOT.glob("006_nwe_generated_*.png"))
    paths.extend(runtime_flag_paths())
    paths.extend(runtime_portrait_paths())
    rows = []
    for path in sorted(set(paths), key=lambda item: item.relative_to(ROOT).as_posix().lower()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    HASH_LEDGER.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> int:
    prepare_directories()
    process_flags()
    portrait_outputs = process_portraits()
    validate_outputs()
    build_flag_contact_sheet()
    build_portrait_contact_sheet("institutional", portrait_outputs)
    build_portrait_contact_sheet("command", portrait_outputs)
    build_decoded_contact_sheet(portrait_outputs)
    write_hash_ledger()
    print("Built 5 flag triplets, 10 large portraits, and 5 officer thumbnails.")
    print(f"Hash ledger: {HASH_LEDGER.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
