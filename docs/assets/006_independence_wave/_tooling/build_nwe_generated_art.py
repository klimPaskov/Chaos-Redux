#!/usr/bin/env python3
"""Build the Event 006 northern/western Europe flag package.

The source rasters in ``source_png/generated_nwe/flags`` were created in four
independent official ImageGen calls. Each historical design used its cited
flat reference as the design constraint and a canonical vanilla HOI4 flag
ladder as the presentation reference. This tool performs only deterministic
palette normalization, one recorded ACX scanline cleanup, resizing, bottom-
origin TGA export, flag validation, flag contact-sheet assembly, and an
explicit flag-only SHA-256 inventory. It never scans or processes any non-flag
asset tree.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[4]
ASSET_ROOT = ROOT / "docs" / "assets" / "006_independence_wave"
SOURCE_FLAGS_ROOT = ASSET_ROOT / "source_png" / "generated_nwe" / "flags"
PROCESSED_FLAGS_ROOT = ASSET_ROOT / "processed_png" / "generated_nwe" / "flags"
CONTACT_ROOT = ASSET_ROOT / "contact_sheets"
FLAGS_ROOT = ROOT / "gfx" / "flags"
HASH_LEDGER = ASSET_ROOT / "generated_nwe_hashes.sha256"
FLAG_CONTACT_SHEET = CONTACT_ROOT / "006_nwe_generated_flags_contact_sheet.png"
FLAG_PROVENANCE_CONTACT_SHEET = (
    CONTACT_ROOT / "006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png"
)
VANILLA_FLAG_REFERENCE_ROOT = (
    ROOT
    / ".agents"
    / "skills"
    / "chaos-redux-event-assets"
    / "assets"
    / "vanilla_reference"
    / "flags"
)

EXPECTED_TAGS = ("ACX", "AFX", "AGX", "AJX")
FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}


def vanilla_flag_ladder(stem: str) -> tuple[Path, Path, Path]:
    return tuple(
        VANILLA_FLAG_REFERENCE_ROOT / size_name / f"{stem}.png"
        for size_name in FLAG_SIZES
    )


FLAGS = {
    "ACX": {
        "label": "St Piran's Cross",
        "raw_source": "ACX_st_pirans_cross_imagegen_raw.png",
        "flat_master": "ACX_st_pirans_cross_imagegen_flat_master.png",
        "design_reference": (
            ASSET_ROOT
            / "source_png"
            / "country_symbols"
            / "acx_st_pirans_cross_source.png"
        ),
        "vanilla_ladder": vanilla_flag_ladder("arm"),
        "palette": ((0, 0, 0), (255, 255, 255)),
        "majority_scanline_cleanup": ((255, 255, 255), 0.65),
    },
    "AFX": {
        "label": "1913 Walloon coq hardi",
        "raw_source": "AFX_walloon_coq_hardi_1913_imagegen_raw.png",
        "flat_master": "AFX_walloon_coq_hardi_1913_imagegen_flat_master.png",
        "design_reference": (
            ASSET_ROOT
            / "source_png"
            / "country_symbols"
            / "afx_walloon_rooster_source.png"
        ),
        "vanilla_ladder": vanilla_flag_ladder("isr"),
        "palette": ((255, 209, 0), (228, 0, 43)),
    },
    "AGX": {
        "label": "Friesland provincial flag",
        "raw_source": "AGX_friesland_provincial_imagegen_raw.png",
        "flat_master": "AGX_friesland_provincial_imagegen_flat_master.png",
        "design_reference": (
            ASSET_ROOT
            / "source_png"
            / "country_symbols"
            / "agx_west_frisian_flag_source.png"
        ),
        "vanilla_ladder": vanilla_flag_ladder("ice"),
        "palette": ((36, 73, 148), (255, 255, 255), (231, 35, 38)),
    },
    "AJX": {
        "label": "Saar Territory, 1920-1935",
        "raw_source": "AJX_saar_territory_1920_1935_imagegen_raw.png",
        "flat_master": "AJX_saar_territory_1920_1935_imagegen_flat_master.png",
        "design_reference": (
            ASSET_ROOT
            / "source_png"
            / "country_symbols"
            / "ajx_saar_territory_1920_1935_source.png"
        ),
        "vanilla_ladder": vanilla_flag_ladder("arm"),
        "palette": ((0, 32, 159), (255, 255, 255), (0, 0, 0)),
    },
}


def source_path(config: dict[str, object], key: str) -> Path:
    return SOURCE_FLAGS_ROOT / str(config[key])


def runtime_flag_path(tag: str, size_name: str) -> Path:
    if size_name == "normal":
        return FLAGS_ROOT / f"{tag}.tga"
    return FLAGS_ROOT / size_name / f"{tag}.tga"


def processed_flag_path(tag: str, size_name: str) -> Path:
    return PROCESSED_FLAGS_ROOT / size_name / f"{tag}.png"


def font(
    size: int,
    *,
    bold: bool = False,
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
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
        SOURCE_FLAGS_ROOT,
        CONTACT_ROOT,
        FLAGS_ROOT / "medium",
        FLAGS_ROOT / "small",
    ]
    directories.extend(
        PROCESSED_FLAGS_ROOT / size_name for size_name in FLAG_SIZES
    )
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def fixed_palette_image(
    colors: tuple[tuple[int, int, int], ...],
) -> Image.Image:
    palette = Image.new("P", (1, 1))
    values: list[int] = []
    for color in colors:
        values.extend(color)
    while len(values) < 768:
        values.extend(colors[-1])
    palette.putpalette(values[:768])
    return palette


def quantize_to_palette(
    image: Image.Image,
    colors: tuple[tuple[int, int, int], ...],
) -> Image.Image:
    palette = fixed_palette_image(colors)
    quantized = image.convert("RGB").quantize(
        palette=palette,
        dither=Image.Dither.NONE,
    )
    return quantized.convert("RGBA")


def clean_majority_scanlines(
    image: Image.Image,
    target: tuple[int, int, int],
    threshold: float,
) -> Image.Image:
    """Promote almost-solid scanlines left by ImageGen edge noise.

    The rule uses only quantized ImageGen pixels. It neither imports a mask nor
    traces or reconstructs geometry from the cited design reference.
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
    """Flatten one retained ImageGen raster without replacing its geometry."""
    image = Image.open(raw_source).convert("RGBA")
    if image.size != (1536, 1024):
        raise ValueError(
            f"ImageGen flag source must be 1536x1024: {raw_source} ({image.size})"
        )
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
    if tuple(FLAGS) != EXPECTED_TAGS:
        raise ValueError(
            f"Flag configuration must be exactly {EXPECTED_TAGS}, got {tuple(FLAGS)}"
        )

    outputs: dict[str, dict[str, Path]] = {}
    for tag, config in FLAGS.items():
        raw_source = source_path(config, "raw_source")
        flat_master = source_path(config, "flat_master")
        source = normalize_imagegen_flag_source(
            raw_source,
            flat_master,
            config["palette"],
            config.get("majority_scanline_cleanup"),
        )
        normal = quantize_to_palette(
            source.resize(FLAG_SIZES["normal"], Image.Resampling.LANCZOS),
            config["palette"],
        )
        outputs[tag] = {
            "raw": raw_source,
            "flat_master": flat_master,
            "design_reference": config["design_reference"],
        }
        for size_name, size in FLAG_SIZES.items():
            image = normal
            if size_name != "normal":
                image = quantize_to_palette(
                    normal.resize(size, Image.Resampling.LANCZOS),
                    config["palette"],
                )
            png_output = processed_flag_path(tag, size_name)
            tga_output = runtime_flag_path(tag, size_name)
            image.save(png_output)
            write_bottom_origin_tga(image, tga_output)
            outputs[tag][size_name] = png_output
    return outputs


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


def decode_bottom_origin_tga(path: Path, size: tuple[int, int]) -> Image.Image:
    raw = path.read_bytes()
    if len(raw) != 18 + size[0] * size[1] * 4:
        raise ValueError(f"Unexpected TGA length: {path}")
    values = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    image_type = values[2]
    width, height = values[8], values[9]
    depth, descriptor = values[10], values[11]
    if image_type != 2 or (width, height) != size or depth != 32:
        raise ValueError(f"Unexpected TGA header: {path}")
    if descriptor & 0x20:
        raise ValueError(f"Top-origin TGA is not permitted: {path}")
    if descriptor & 0x0F != 8:
        raise ValueError(f"TGA alpha descriptor is not 8-bit: {path}")

    rgba = bytearray(width * height * 4)
    source_offset = 18
    for target_y in range(height - 1, -1, -1):
        for x in range(width):
            blue, green, red, alpha = raw[source_offset : source_offset + 4]
            source_offset += 4
            target_offset = (target_y * width + x) * 4
            rgba[target_offset : target_offset + 4] = bytes(
                (red, green, blue, alpha)
            )
    return Image.frombytes("RGBA", size, bytes(rgba))


def validate_source_scope() -> None:
    required_raw_names = {
        str(config["raw_source"]) for config in FLAGS.values()
    }
    permitted_source_names = {
        str(config[key])
        for config in FLAGS.values()
        for key in ("raw_source", "flat_master")
    }
    actual_source_names = {
        path.name for path in SOURCE_FLAGS_ROOT.iterdir() if path.is_file()
    }
    missing_raw_names = required_raw_names - actual_source_names
    unexpected_source_names = actual_source_names - permitted_source_names
    if missing_raw_names or unexpected_source_names:
        raise ValueError(
            "Generated flag source directory must contain the four retained "
            "raw inputs and no unrelated files; "
            f"missing_raw={sorted(missing_raw_names)}, "
            f"unexpected={sorted(unexpected_source_names)}"
        )

    for config in FLAGS.values():
        raw_source = source_path(config, "raw_source")
        with Image.open(raw_source) as image:
            if image.size != (1536, 1024):
                raise ValueError(
                    f"Unexpected retained ImageGen source dimensions: {raw_source} ({image.size})"
                )

        design_reference = config["design_reference"]
        with Image.open(design_reference) as image:
            if image.width < 1 or image.height < 1:
                raise ValueError(f"Empty cited design reference: {design_reference}")

        vanilla_ladder = config["vanilla_ladder"]
        if len(vanilla_ladder) != len(FLAG_SIZES):
            raise ValueError(
                f"Canonical flag ladder must contain three files: {vanilla_ladder}"
            )
        for size_name, reference in zip(FLAG_SIZES, vanilla_ladder):
            with Image.open(reference) as image:
                if image.size != FLAG_SIZES[size_name]:
                    raise ValueError(
                        f"Unexpected canonical ladder dimensions: {reference} ({image.size})"
                    )


def validate_no_aex_standalone_flag() -> None:
    forbidden = list(SOURCE_FLAGS_ROOT.glob("AEX*"))
    forbidden.extend(
        processed_flag_path("AEX", size_name) for size_name in FLAG_SIZES
    )
    forbidden.extend(runtime_flag_path("AEX", size_name) for size_name in FLAG_SIZES)
    existing = [path for path in forbidden if path.exists()]
    if existing:
        rendered = ", ".join(path.relative_to(ROOT).as_posix() for path in existing)
        raise ValueError(
            "AEX has no standalone flag authority; remove the stale artifact "
            f"through a separately reviewed cleanup: {rendered}"
        )


def validate_flag_outputs() -> None:
    expected_source_names = {
        str(config[key])
        for config in FLAGS.values()
        for key in ("raw_source", "flat_master")
    }
    actual_source_names = {
        path.name for path in SOURCE_FLAGS_ROOT.iterdir() if path.is_file()
    }
    if actual_source_names != expected_source_names:
        raise ValueError(
            "Built flag source directory is not the exact four raw/flat pairs: "
            f"missing={sorted(expected_source_names - actual_source_names)}, "
            f"unexpected={sorted(actual_source_names - expected_source_names)}"
        )

    expected_output_names = {f"{tag}.png" for tag in EXPECTED_TAGS}
    for size_name in FLAG_SIZES:
        actual_output_names = {
            path.name
            for path in (PROCESSED_FLAGS_ROOT / size_name).iterdir()
            if path.is_file()
        }
        if actual_output_names != expected_output_names:
            raise ValueError(
                f"Processed {size_name} flag directory is not the exact four-tag set: "
                f"missing={sorted(expected_output_names - actual_output_names)}, "
                f"unexpected={sorted(actual_output_names - expected_output_names)}"
            )

    for tag, config in FLAGS.items():
        flat_master = source_path(config, "flat_master")
        validate_flat_flag_png(flat_master, (1536, 1024), config["palette"])
        for size_name, size in FLAG_SIZES.items():
            png_path = processed_flag_path(tag, size_name)
            tga_path = runtime_flag_path(tag, size_name)
            validate_flat_flag_png(png_path, size, config["palette"])
            processed = Image.open(png_path).convert("RGBA")
            decoded = decode_bottom_origin_tga(tga_path, size)
            if processed.tobytes() != decoded.tobytes():
                raise ValueError(
                    f"Runtime TGA pixels or orientation differ from processed PNG: {tga_path}"
                )

    validate_no_aex_standalone_flag()


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
        draw.text(
            (left + ((right - left) - width) // 2, y),
            line,
            font=text_font,
            fill=fill,
        )
        y += size + 4


def build_flag_contact_sheet() -> Path:
    card_w, card_h = 390, 390
    header_h = 88
    sheet = Image.new("RGBA", (card_w * len(FLAGS), header_h + card_h), "#161b22")
    draw = ImageDraw.Draw(sheet)
    draw.text(
        (28, 18),
        "Event 006 — live historical country flags",
        font=font(29, bold=True),
        fill="#f4f0e8",
    )
    draw.text(
        (29, 53),
        "Actual bottom-origin uncompressed 32-bit TGA triplets; no small-size redesign",
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
        normal = decode_bottom_origin_tga(
            runtime_flag_path(tag, "normal"), FLAG_SIZES["normal"]
        )
        medium = decode_bottom_origin_tga(
            runtime_flag_path(tag, "medium"), FLAG_SIZES["medium"]
        )
        small = decode_bottom_origin_tga(
            runtime_flag_path(tag, "small"), FLAG_SIZES["small"]
        )
        draw_centered_lines(
            draw,
            f"{tag} — {config['label']}",
            (left + 18, top + 22, left + card_w - 18, top + 62),
            size=17,
            bold=True,
            wrap_width=31,
        )
        draw_contain(
            sheet,
            normal.resize((296, 188), Image.Resampling.NEAREST),
            (left + 46, top + 64, left + 344, top + 254),
            nearest=True,
        )
        draw_contain(
            sheet,
            medium.resize((164, 104), Image.Resampling.NEAREST),
            (left + 35, top + 264, left + 205, top + 346),
            nearest=True,
        )
        draw_contain(
            sheet,
            small.resize((100, 70), Image.Resampling.NEAREST),
            (left + 238, top + 264, left + 345, top + 346),
            nearest=True,
        )
        draw.text((left + 151, top + 246), "82×52", font=font(13), fill="#aeb9c6")
        draw.text((left + 41, top + 350), "41×26", font=font(13), fill="#aeb9c6")
        draw.text((left + 269, top + 350), "10×7", font=font(13), fill="#aeb9c6")
    sheet.convert("RGB").save(FLAG_CONTACT_SHEET, quality=95)
    return FLAG_CONTACT_SHEET


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
            (
                "cited design",
                Image.open(flag_outputs[tag]["design_reference"]).convert("RGBA"),
            ),
            ("ImageGen raw", Image.open(flag_outputs[tag]["raw"]).convert("RGBA")),
            (
                "flat master",
                Image.open(flag_outputs[tag]["flat_master"]).convert("RGBA"),
            ),
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
    sheet.convert("RGB").save(FLAG_PROVENANCE_CONTACT_SHEET, quality=95)
    return FLAG_PROVENANCE_CONTACT_SHEET


def flag_inventory_paths(contact_sheets: tuple[Path, Path]) -> list[Path]:
    paths: list[Path] = []
    for tag, config in FLAGS.items():
        paths.extend(
            (
                source_path(config, "raw_source"),
                source_path(config, "flat_master"),
                config["design_reference"],
            )
        )
        paths.extend(config["vanilla_ladder"])
        for size_name in FLAG_SIZES:
            paths.extend(
                (
                    processed_flag_path(tag, size_name),
                    runtime_flag_path(tag, size_name),
                )
            )
    paths.extend(contact_sheets)
    return sorted(
        set(paths),
        key=lambda item: item.relative_to(ROOT).as_posix().lower(),
    )


def write_hash_ledger(contact_sheets: tuple[Path, Path]) -> None:
    rows = []
    for path in flag_inventory_paths(contact_sheets):
        if not path.is_file():
            raise FileNotFoundError(f"Missing flag inventory input: {path}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rows.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    HASH_LEDGER.write_text("\n".join(rows) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scope",
        choices=("flags",),
        default="flags",
        help="Optional compatibility selector; this tool owns only the flag package.",
    )
    return parser.parse_args()


def main() -> int:
    parse_args()
    prepare_directories()
    validate_no_aex_standalone_flag()
    validate_source_scope()
    flag_outputs = process_flags()
    validate_flag_outputs()
    contact_sheets = (
        build_flag_contact_sheet(),
        build_flag_raw_flat_comparison_sheet(flag_outputs),
    )
    write_hash_ledger(contact_sheets)
    print("Built and validated 4 historical ImageGen flag triplets: ACX, AFX, AGX, AJX.")
    print("AEX remains outside the standalone flag scope.")
    print(f"Hash ledger: {HASH_LEDGER.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
