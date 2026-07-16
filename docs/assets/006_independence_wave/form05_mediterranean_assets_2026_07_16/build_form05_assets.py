#!/usr/bin/env python3
"""Build and validate the bounded Event 006 FORM-05 visual package.

The retained flag and UI sources were created with official ImageGen.  This
tool performs only deterministic post-processing: fixed-palette flag cleanup,
size-ladder rasterization, transparent UI resizing, official DDS conversion,
contact-sheet assembly, exact runtime validation, and hash-ledger generation.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


PACKAGE_ROOT = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
NOTES_ROOT = PACKAGE_ROOT / "notes"
FLAGS_ROOT = ROOT / "gfx" / "flags"
DDS_CONVERTER = (
    ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "tools"
    / "convert_to_dds.py"
)
INTERFACE_FILE = ROOT / "interface" / "006_independence_wave_form05.gfx"
HANDOFF_FILE = (
    ROOT
    / "docs"
    / "plans"
    / "006_independence_wave_plans"
    / "subagent_handoffs"
    / "006_mediterranean_form05_visual_assets_2026_07_16.md"
)

FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}
FLAG_SUFFIXES = ("", "_democratic", "_communism", "_fascism", "_neutrality")

FLAGS = {
    "ARX": {
        "label": "Sardinia — attested all-left Four Moors arrangement",
        "raw": SOURCE_ROOT / "flags" / "ARX_sardinia_four_moors_all_left_imagegen_raw.png",
        "master": SOURCE_ROOT / "flags" / "ARX_sardinia_four_moors_all_left_flat_master.png",
        "palette": ((247, 245, 236), (200, 16, 46), (17, 17, 17)),
        "priority": (((17, 17, 17), 0.08), ((200, 16, 46), 0.20)),
        "cleanup": "cross",
    },
    "ASX": {
        "label": "Sicily — 1848 S.015 flat-field normalization",
        "raw": SOURCE_ROOT / "flags" / "ASX_sicily_1848_s015_imagegen_raw.png",
        "master": SOURCE_ROOT / "flags" / "ASX_sicily_1848_s015_imagegen_flat_master.png",
        "palette": ((0, 146, 70), (245, 241, 230), (206, 43, 55), (216, 163, 40)),
        "priority": (((216, 163, 40), 0.30),),
        "cleanup": "retained_master",
    },
    "MIX": {
        "label": "Mediterranean Island League — fictional civic league flag",
        "raw": SOURCE_ROOT / "flags" / "MIX_mediterranean_island_league_imagegen_raw.png",
        "master": SOURCE_ROOT / "flags" / "MIX_mediterranean_island_league_flat_master.png",
        "palette": ((12, 35, 64), (20, 119, 116), (222, 169, 47), (245, 243, 232)),
        "priority": (((245, 243, 232), 0.05), ((222, 169, 47), 0.05)),
        "cleanup": "fixed_palette",
    },
}

DECISIONS = (
    "charter",
    "delegation",
    "shipping",
    "defense",
    "customs",
    "capital",
    "proclamation",
)
IDEAS = ("provisional_charter", "ratified_union", "charter_breakdown")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    candidate = Path("C:/Windows/Fonts") / name
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def fixed_palette_image(colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
    palette = Image.new("P", (1, 1))
    values: list[int] = []
    for color in colors:
        values.extend(color)
    while len(values) < 768:
        values.extend(colors[-1])
    palette.putpalette(values[:768])
    return palette


def quantize(image: Image.Image, colors: tuple[tuple[int, int, int], ...]) -> Image.Image:
    return image.convert("RGB").quantize(
        palette=fixed_palette_image(colors),
        dither=Image.Dither.NONE,
    ).convert("RGBA")


def clean_cross(
    raw: Image.Image,
    flat: Image.Image,
    red: tuple[int, int, int],
    fallbacks: tuple[tuple[int, int, int], ...],
) -> Image.Image:
    """Retain red only on full-span cross arms detected from ImageGen pixels."""
    output = flat.copy().convert("RGBA")
    pixels = output.load()
    red_rgba = (*red, 255)
    rows = {
        y
        for y in range(output.height)
        if sum(pixels[x, y] == red_rgba for x in range(output.width)) / output.width >= 0.75
    }
    columns = {
        x
        for x in range(output.width)
        if sum(pixels[x, y] == red_rgba for y in range(output.height)) / output.height >= 0.75
    }
    if not rows or not columns:
        raise ValueError("ARX cross cleanup could not detect both full-span arms")
    source = raw.convert("RGB")
    for y in range(output.height):
        for x in range(output.width):
            if y in rows or x in columns:
                pixels[x, y] = red_rgba
            elif pixels[x, y] == red_rgba:
                original = source.getpixel((x, y))
                replacement = min(
                    fallbacks,
                    key=lambda color: sum((original[channel] - color[channel]) ** 2 for channel in range(3)),
                )
                pixels[x, y] = (*replacement, 255)
    return output


def normalize_flag_masters() -> None:
    for tag, config in FLAGS.items():
        raw = Image.open(config["raw"]).convert("RGBA")
        if raw.size != (1536, 1024):
            raise ValueError(f"Unexpected official ImageGen flag source size: {config['raw']} {raw.size}")
        if config["cleanup"] == "retained_master":
            master = Image.open(config["master"]).convert("RGBA")
        else:
            master = quantize(raw, config["palette"])
            if config["cleanup"] == "cross":
                master = clean_cross(
                    raw,
                    master,
                    config["palette"][1],
                    (config["palette"][0], config["palette"][2]),
                )
            master.save(config["master"])
        validate_palette(master, config["palette"], (1536, 1024), config["master"])


def resized_palette(image: Image.Image, size: tuple[int, int], config: dict[str, object]) -> Image.Image:
    resized = image.resize(size, Image.Resampling.LANCZOS)
    if config is FLAGS["ARX"]:
        white = (*config["palette"][0], 255)
        red = (*config["palette"][1], 255)
        black = (*config["palette"][2], 255)
        output = Image.new("RGBA", size)
        for index, source in enumerate(resized.convert("RGB").getdata()):
            r, g, b = source
            if r - g >= 45 and r - b >= 35:
                color = red
            else:
                luminance = (299 * r + 587 * g + 114 * b) / 1000
                color = black if luminance < 132 else white
            output.putpixel((index % size[0], index // size[0]), color)
        return output
    return quantize(resized, config["palette"])


def sample_small(image: Image.Image, size: tuple[int, int], config: dict[str, object]) -> Image.Image:
    source = image.convert("RGB")
    colors = config["palette"]
    output = Image.new("RGBA", size)
    for target_y in range(size[1]):
        top = target_y * source.height // size[1]
        bottom = (target_y + 1) * source.height // size[1]
        for target_x in range(size[0]):
            left = target_x * source.width // size[0]
            right = (target_x + 1) * source.width // size[0]
            cell = list(source.crop((left, top, right, bottom)).getdata())
            counts = {color: cell.count(color) for color in colors}
            selected = None
            for color, threshold in config["priority"]:
                if counts[color] / len(cell) >= threshold:
                    selected = color
                    break
            if selected is None:
                selected = max(colors, key=lambda color: counts[color])
            output.putpixel((target_x, target_y), (*selected, 255))
    return output


def write_bottom_origin_tga(image: Image.Image, output: Path) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
    source = rgba.tobytes()
    stride = width * 4
    payload = bytearray()
    for y in range(height - 1, -1, -1):
        row = source[y * stride : (y + 1) * stride]
        for index in range(0, len(row), 4):
            r, g, b, a = row[index : index + 4]
            payload.extend((b, g, r, a))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(header + payload)


def runtime_flag(tag: str, suffix: str, size_name: str) -> Path:
    directory = FLAGS_ROOT if size_name == "normal" else FLAGS_ROOT / size_name
    return directory / f"{tag}{suffix}.tga"


def build_flags() -> None:
    normalize_flag_masters()
    for tag, config in FLAGS.items():
        master = Image.open(config["master"]).convert("RGBA")
        normal = resized_palette(master, FLAG_SIZES["normal"], config)
        for size_name, size in FLAG_SIZES.items():
            if size_name == "normal":
                image = normal
            elif size_name == "medium":
                image = resized_palette(normal, size, config)
            else:
                image = sample_small(master, size, config)
            validate_palette(image, config["palette"], size, Path(f"{tag}/{size_name}"))
            processed = PROCESSED_ROOT / "flags" / size_name / f"{tag}.png"
            processed.parent.mkdir(parents=True, exist_ok=True)
            image.save(processed)
            base_runtime = runtime_flag(tag, "", size_name)
            write_bottom_origin_tga(image, base_runtime)
            for suffix in FLAG_SUFFIXES[1:]:
                shutil.copyfile(base_runtime, runtime_flag(tag, suffix, size_name))


def validate_palette(
    image: Image.Image,
    palette: tuple[tuple[int, int, int], ...],
    size: tuple[int, int],
    path: Path,
) -> dict[str, object]:
    rgba = image.convert("RGBA")
    if rgba.size != size:
        raise ValueError(f"Unexpected dimensions for {path}: {rgba.size}")
    actual = set(rgba.getdata())
    expected = {(*color, 255) for color in palette}
    if not actual or not actual.issubset(expected):
        raise ValueError(f"Non-flat pixels in {path}: {sorted(actual - expected)[:8]}")
    return {
        "dimensions": list(size),
        "palette_rgb": [list(pixel[:3]) for pixel in sorted(actual)],
        "opaque": True,
    }


def process_alpha(source: Path, output: Path, size: tuple[int, int], content: tuple[int, int]) -> None:
    image = Image.open(source).convert("RGBA")
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError(f"No visible pixels in alpha master: {source}")
    cropped = image.crop(bbox)
    fitted = ImageOps.contain(cropped, content, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    canvas.alpha_composite(fitted, ((size[0] - fitted.width) // 2, (size[1] - fitted.height) // 2))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def convert_dds(source: Path, output: Path, size: tuple[int, int]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            sys.executable,
            "-B",
            str(DDS_CONVERTER),
            "--input",
            str(source),
            "--output",
            str(output),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        cwd=ROOT,
        check=True,
    )


def build_ui() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for name in DECISIONS:
        source = SOURCE_ROOT / "decisions" / f"decision_independence_wave_form05_{name}_alpha_master.png"
        processed = PROCESSED_ROOT / "decisions" / f"decision_independence_wave_form05_{name}.png"
        runtime = ROOT / "gfx" / "interface" / "decisions" / "006_independence_wave" / "mediterranean" / f"decision_independence_wave_form05_{name}.dds"
        process_alpha(source, processed, (32, 32), (28, 28))
        convert_dds(processed, runtime, (32, 32))
        records.append({"kind": "decision", "name": name, "sprite": f"GFX_decision_independence_wave_form05_{name}", "source": source, "processed": processed, "runtime": runtime, "size": (32, 32)})
    for name in IDEAS:
        source = SOURCE_ROOT / "ideas" / f"idea_independence_wave_form05_{name}_alpha_master.png"
        processed = PROCESSED_ROOT / "ideas" / f"idea_independence_wave_form05_{name}.png"
        runtime = ROOT / "gfx" / "interface" / "ideas" / "006_independence_wave" / "mediterranean" / f"idea_independence_wave_form05_{name}.dds"
        process_alpha(source, processed, (64, 64), (58, 58))
        convert_dds(processed, runtime, (64, 64))
        records.append({"kind": "idea", "name": name, "sprite": f"GFX_idea_independence_wave_form05_{name}", "source": source, "processed": processed, "runtime": runtime, "size": (64, 64)})
    emblem_source = SOURCE_ROOT / "emblems" / "independence_wave_formable_form_05_alpha_master.png"
    emblem_processed = PROCESSED_ROOT / "emblems" / "independence_wave_formable_form_05.png"
    emblem_runtime = ROOT / "gfx" / "interface" / "006_independence_wave" / "emblems" / "independence_wave_formable_form_05.dds"
    process_alpha(emblem_source, emblem_processed, (128, 128), (116, 116))
    convert_dds(emblem_processed, emblem_runtime, (128, 128))
    records.append({"kind": "emblem", "name": "form_05", "sprite": "GFX_independence_wave_formable_form_05", "source": emblem_source, "processed": emblem_processed, "runtime": emblem_runtime, "size": (128, 128)})
    report_processed = PROCESSED_ROOT / "report" / "report_event_independence_wave_form05_charter_congress.png"
    report_runtime = ROOT / "gfx" / "event_pictures" / "006_independence_wave" / "mediterranean" / "report_event_independence_wave_form05_charter_congress.dds"
    convert_dds(report_processed, report_runtime, (210, 176))
    records.append({"kind": "report", "name": "charter_congress", "sprite": "GFX_report_event_independence_wave_form05_charter_congress", "source": SOURCE_ROOT / "report" / "report_event_independence_wave_form05_charter_congress_imagegen_raw.png", "processed": report_processed, "runtime": report_runtime, "size": (210, 176)})
    return records


def validate_tga(path: Path, size: tuple[int, int], processed: Path) -> dict[str, object]:
    raw = path.read_bytes()
    expected_length = 18 + size[0] * size[1] * 4
    values = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    if len(raw) != expected_length:
        raise ValueError(f"Unexpected TGA payload length: {path}")
    if values[0:3] != (0, 0, 2):
        raise ValueError(f"TGA is not uncompressed true-color: {path}")
    if (values[8], values[9]) != size or values[10] != 32:
        raise ValueError(f"Unexpected TGA dimensions/depth: {path}")
    if values[11] & 0x20 or values[11] & 0x0F != 8:
        raise ValueError(f"TGA is not bottom-left origin with 8-bit alpha: {path}")
    decoded = Image.open(path).convert("RGBA")
    expected = Image.open(processed).convert("RGBA")
    if decoded.tobytes() != expected.tobytes():
        raise ValueError(f"TGA decode differs from processed PNG: {path}")
    return {"dimensions": list(size), "image_type": 2, "pixel_depth": 32, "origin": "bottom-left", "alpha_bits": 8, "bytes": len(raw), "sha256": sha256(path), "decode_matches_processed_png": True}


def validate_dds(path: Path, size: tuple[int, int], processed: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if len(raw) != 128 + size[0] * size[1] * 4 or raw[:4] != b"DDS ":
        raise ValueError(f"Unexpected DDS framing: {path}")
    header_size = struct.unpack_from("<I", raw, 4)[0]
    height, width = struct.unpack_from("<II", raw, 12)
    pf_size, pf_flags, fourcc, bits, r_mask, g_mask, b_mask, a_mask = struct.unpack_from("<IIIIIIII", raw, 76)
    caps = struct.unpack_from("<I", raw, 108)[0]
    if header_size != 124 or (width, height) != size:
        raise ValueError(f"Unexpected DDS header/size: {path}")
    if (pf_size, pf_flags, fourcc, bits) != (32, 65, 0, 32):
        raise ValueError(f"DDS is not legacy uncompressed BGRA: {path}")
    if (r_mask, g_mask, b_mask, a_mask) != (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000) or caps != 0x1000:
        raise ValueError(f"Unexpected DDS masks/caps: {path}")
    decoded = Image.open(path).convert("RGBA")
    expected = Image.open(processed).convert("RGBA")
    if decoded.tobytes() != expected.tobytes():
        raise ValueError(f"DDS decode differs from processed PNG: {path}")
    alpha = expected.getchannel("A")
    chroma_like = 0
    for r, g, b, a in expected.getdata():
        if a > 16 and ((r > 230 and b > 230 and g < 70) or (g > 230 and r < 70 and b < 70)):
            chroma_like += 1
    return {"dimensions": list(size), "format": "legacy uncompressed BGRA8888", "bytes": len(raw), "sha256": sha256(path), "alpha_min": alpha.getextrema()[0], "alpha_max": alpha.getextrema()[1], "chroma_like_visible_pixels": chroma_like, "decode_matches_processed_png": True}


def checker(size: tuple[int, int], cell: int = 8) -> Image.Image:
    image = Image.new("RGBA", size)
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            shade = 218 if (x // cell + y // cell) % 2 == 0 else 174
            draw.rectangle((x, y, min(x + cell - 1, size[0] - 1), min(y + cell - 1, size[1] - 1)), fill=(shade, shade, shade, 255))
    return image


def place_contain(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], *, nearest: bool = False) -> None:
    left, top, right, bottom = box
    fitted = ImageOps.contain(source.convert("RGBA"), (right - left, bottom - top), Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS)
    canvas.alpha_composite(fitted, (left + (right - left - fitted.width) // 2, top + (bottom - top - fitted.height) // 2))


def contact_sheets(records: list[dict[str, object]]) -> None:
    CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
    title_font = font(24, bold=True)
    label_font = font(17, bold=True)
    small_font = font(14)

    flags = Image.new("RGBA", (1500, 990), (235, 231, 220, 255))
    draw = ImageDraw.Draw(flags)
    draw.text((30, 18), "Event 006 FORM-05 flag sources, flat masters, and exact runtime ladders", fill=(20, 25, 31, 255), font=title_font)
    for row, (tag, config) in enumerate(FLAGS.items()):
        top = 72 + row * 300
        draw.text((30, top), f"{tag} — {config['label']}", fill=(20, 25, 31, 255), font=label_font)
        columns = [
            ("official ImageGen source", Image.open(config["raw"]), False),
            ("fixed-palette master", Image.open(config["master"]), False),
            ("82x52", Image.open(PROCESSED_ROOT / "flags" / "normal" / f"{tag}.png"), True),
            ("41x26", Image.open(PROCESSED_ROOT / "flags" / "medium" / f"{tag}.png"), True),
            ("10x7", Image.open(PROCESSED_ROOT / "flags" / "small" / f"{tag}.png"), True),
        ]
        x_positions = (30, 330, 650, 930, 1190)
        widths = (270, 270, 240, 220, 180)
        for (label, image, nearest), left, width in zip(columns, x_positions, widths):
            draw.rectangle((left, top + 36, left + width, top + 235), fill=(250, 248, 241, 255), outline=(70, 75, 82, 255), width=2)
            place_contain(flags, image, (left + 8, top + 44, left + width - 8, top + 227), nearest=nearest)
            draw.text((left, top + 244), label, fill=(35, 40, 48, 255), font=small_font)
        draw.text((30, top + 269), "All five ideology filenames use this identical civic design intentionally; no ideological overlay is present.", fill=(50, 56, 65, 255), font=small_font)
    flags.convert("RGB").save(CONTACT_ROOT / "006_form05_flag_sources_and_ladders.png")

    ui = Image.new("RGBA", (1320, 650), (229, 226, 218, 255))
    draw = ImageDraw.Draw(ui)
    draw.text((28, 18), "Event 006 FORM-05 final UI assets at target-pixel scale", fill=(20, 25, 31, 255), font=title_font)
    ui_records = [record for record in records if record["kind"] != "report"]
    for index, record in enumerate(ui_records):
        column = index % 6
        row = index // 6
        left = 28 + column * 210
        top = 70 + row * 260
        panel = checker((172, 172), 12)
        image = Image.open(record["processed"]).convert("RGBA")
        scale = min(5 if record["kind"] == "decision" else 2, 5)
        enlarged = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
        panel.alpha_composite(enlarged, ((172 - enlarged.width) // 2, (172 - enlarged.height) // 2))
        ui.alpha_composite(panel, (left, top))
        draw.rectangle((left, top, left + 171, top + 171), outline=(55, 61, 69, 255), width=2)
        draw.text((left, top + 180), str(record["kind"]), fill=(45, 51, 59, 255), font=small_font)
        draw.text((left, top + 199), str(record["name"]), fill=(20, 25, 31, 255), font=small_font)
        draw.text((left, top + 220), f"{record['size'][0]}x{record['size'][1]}", fill=(70, 76, 84, 255), font=small_font)
    ui.convert("RGB").save(CONTACT_ROOT / "006_form05_ui_icons_contact_sheet.png")

    report = Image.new("RGBA", (1040, 550), (232, 228, 218, 255))
    draw = ImageDraw.Draw(report)
    draw.text((28, 18), "Event 006 FORM-05 charter congress report art", fill=(20, 25, 31, 255), font=title_font)
    raw = Image.open(SOURCE_ROOT / "report" / "report_event_independence_wave_form05_charter_congress_imagegen_raw.png")
    final = Image.open(PROCESSED_ROOT / "report" / "report_event_independence_wave_form05_charter_congress.png")
    draw.rectangle((28, 70, 620, 470), fill=(247, 244, 237, 255), outline=(60, 65, 72, 255), width=2)
    place_contain(report, raw, (38, 80, 610, 460))
    panel = checker((350, 350), 16)
    enlarged = final.resize((420, 352), Image.Resampling.NEAREST)
    panel.alpha_composite(enlarged, ((350 - enlarged.width) // 2, (350 - enlarged.height) // 2))
    report.alpha_composite(panel, (660, 70))
    draw.rectangle((660, 70, 1009, 419), outline=(60, 65, 72, 255), width=2)
    draw.text((28, 480), "Official ImageGen fictional 1938 press-photograph source", fill=(35, 40, 48, 255), font=small_font)
    draw.text((660, 430), "Final 210x176 tilted transparent report card (2x nearest preview)", fill=(35, 40, 48, 255), font=small_font)
    report.convert("RGB").save(CONTACT_ROOT / "006_form05_report_event_contact_sheet.png")


def validation(records: list[dict[str, object]]) -> dict[str, object]:
    report: dict[str, object] = {
        "pipeline": "official ImageGen source -> deterministic chroma removal/fixed-palette flattening -> target PNG -> official legacy DDS converter or custom bottom-origin uncompressed TGA writer",
        "flags": {},
        "ui": [],
        "expected_runtime_counts": {"flags": 45, "dds": 12},
        "protected_asset_boundary": "No advisor-icon or portrait path is produced by this package.",
    }
    flag_records: dict[str, object] = {}
    tga_count = 0
    for tag, config in FLAGS.items():
        sizes: dict[str, object] = {}
        for size_name, size in FLAG_SIZES.items():
            processed = PROCESSED_ROOT / "flags" / size_name / f"{tag}.png"
            palette_check = validate_palette(Image.open(processed), config["palette"], size, processed)
            variants: dict[str, object] = {}
            base_hash = None
            for suffix in FLAG_SUFFIXES:
                path = runtime_flag(tag, suffix, size_name)
                result = validate_tga(path, size, processed)
                if base_hash is None:
                    base_hash = result["sha256"]
                elif result["sha256"] != base_hash:
                    raise ValueError(f"Intentional shared civic flag family is not byte-identical: {path}")
                variants[path.name] = result
                tga_count += 1
            sizes[size_name] = {"processed_png": {"path": rel(processed), **palette_check}, "runtime_variants": variants, "intentional_shared_design": True}
        flag_records[tag] = {
            "source": rel(config["raw"]),
            "flat_master": rel(config["master"]),
            "master_palette": validate_palette(Image.open(config["master"]), config["palette"], (1536, 1024), config["master"]),
            "sizes": sizes,
        }
    if tga_count != 45:
        raise ValueError(f"Expected exactly 45 validated FORM-05 TGA files, got {tga_count}")
    report["flags"] = flag_records

    ui_results: list[dict[str, object]] = []
    for record in records:
        result = validate_dds(record["runtime"], record["size"], record["processed"])
        if record["kind"] != "report" and result["alpha_min"] != 0:
            raise ValueError(f"Transparent UI asset has no transparent pixels: {record['runtime']}")
        if result["chroma_like_visible_pixels"] > 2:
            raise ValueError(f"Visible chroma-key contamination remains in {record['runtime']}: {result['chroma_like_visible_pixels']}")
        ui_results.append({
            "kind": record["kind"],
            "sprite": record["sprite"],
            "source": rel(record["source"]),
            "processed_png": rel(record["processed"]),
            "runtime_dds": rel(record["runtime"]),
            **result,
        })
    if len(ui_results) != 12:
        raise ValueError(f"Expected exactly 12 validated FORM-05 DDS assets, got {len(ui_results)}")
    report["ui"] = ui_results

    produced_paths = [Path(item["runtime_dds"]) for item in ui_results]
    produced_paths += [Path(size["processed_png"]["path"]) for flag in flag_records.values() for size in flag["sizes"].values()]
    if any("advisor" in str(path).lower() or "portrait" in str(path).lower() for path in produced_paths):
        raise ValueError("Protected advisor/portrait boundary was violated")
    NOTES_ROOT.mkdir(parents=True, exist_ok=True)
    (NOTES_ROOT / "validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def write_hashes(records: list[dict[str, object]]) -> None:
    paths: set[Path] = set()
    for path in PACKAGE_ROOT.rglob("*"):
        if path.is_file() and path.name not in {"hashes.sha256", "validation.json"}:
            paths.add(path)
    for tag in FLAGS:
        for size_name in FLAG_SIZES:
            for suffix in FLAG_SUFFIXES:
                paths.add(runtime_flag(tag, suffix, size_name))
    for record in records:
        paths.add(record["runtime"])
    paths.add(INTERFACE_FILE)
    paths.add(HANDOFF_FILE)
    lines = [f"{sha256(path)}  {rel(path)}" for path in sorted(paths, key=lambda item: rel(item))]
    (PACKAGE_ROOT / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    build_flags()
    records = build_ui()
    contact_sheets(records)
    validation(records)
    write_hashes(records)
    print("Built 45 fixed-palette TGA flags and 12 legacy BGRA DDS assets.")


if __name__ == "__main__":
    main()
