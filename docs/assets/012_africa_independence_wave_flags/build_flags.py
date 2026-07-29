"""Build and validate the Event 12 Africa revival base-flag ladders.

The source masters are either the public-domain Asante flag image or original
fictional 1936 revival designs generated for this package. The build flattens
minor antialiasing and generation gradients into explicit per-flag palettes,
then writes the exact HOI4 base-flag ladder as uncompressed, bottom-origin,
32-bit TGA files.
"""

from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
MOD_ROOT = PACKAGE_ROOT.parents[2]
SOURCE_ROOT = PACKAGE_ROOT / "source_png"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
NOTES_ROOT = PACKAGE_ROOT / "notes"

FLAG_SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

FLAGS = {
    "DOX": {
        "name": "Asante",
        "source": "DOX_flag_of_ashanti_1024.png",
        "classification": "public-domain historical-source design",
        "palette": [
            (255, 255, 0),
            (0, 153, 0),
            (0, 0, 0),
            (255, 255, 255),
        ],
    },
    "DSX": {
        "name": "Oyo revival",
        "source": "DSX_oyo_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (3, 19, 84),
            (235, 208, 136),
            (139, 40, 35),
        ],
    },
    "DUX": {
        "name": "Kanem-Bornu revival",
        "source": "DUX_kanem_bornu_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (2, 31, 84),
            (236, 199, 131),
            (41, 58, 58),
            (217, 175, 116),
        ],
    },
    "DYX": {
        "name": "Luba revival",
        "source": "DYX_luba_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (4, 74, 83),
            (183, 101, 40),
            (206, 150, 99),
            (28, 34, 33),
        ],
    },
    "DZX": {
        "name": "Lunda revival",
        "source": "DZX_lunda_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (1, 28, 119),
            (196, 103, 31),
            (222, 193, 163),
        ],
    },
    "EMX": {
        "name": "Kilwa revival",
        "source": "EMX_kilwa_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (2, 77, 88),
            (121, 0, 16),
            (253, 252, 251),
            (221, 218, 197),
            (205, 101, 45),
        ],
    },
    "EQX": {
        "name": "Zulu revival",
        "source": "EQX_zulu_revival_imagegen.png",
        "classification": "original fictional 1936 revival design",
        "palette": [
            (10, 62, 32),
            (187, 108, 31),
            (243, 232, 206),
            (26, 26, 26),
            (214, 145, 32),
        ],
    },
}

SMALL_PIXEL_PATTERNS = {
    "DUX": [
        "0001100000",
        "0011000000",
        "0110203000",
        "0100320000",
        "0112301000",
        "0011110000",
        "0000000000",
    ],
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fixed_palette_image(colors: list[tuple[int, int, int]]) -> Image.Image:
    palette = Image.new("P", (1, 1))
    flat = [channel for color in colors for channel in color]
    flat.extend([0] * (768 - len(flat)))
    palette.putpalette(flat)
    return palette


def flatten_to_palette(
    image: Image.Image,
    size: tuple[int, int],
    colors: list[tuple[int, int, int]],
    resample: Image.Resampling,
) -> Image.Image:
    resized = image.convert("RGB").resize(size, resample)
    indexed = resized.quantize(
        palette=fixed_palette_image(colors),
        dither=Image.Dither.NONE,
    )
    return indexed.convert("RGBA")


def render_small_pixel_pattern(
    rows: list[str],
    colors: list[tuple[int, int, int]],
) -> Image.Image:
    if len(rows) != FLAG_SIZES["small"][1]:
        raise ValueError("Small pixel pattern has the wrong row count")
    image = Image.new("RGBA", FLAG_SIZES["small"], (*colors[0], 255))
    pixels = image.load()
    for y, row in enumerate(rows):
        if len(row) != FLAG_SIZES["small"][0]:
            raise ValueError("Small pixel pattern has the wrong column count")
        for x, palette_index in enumerate(row):
            index = int(palette_index)
            pixels[x, y] = (*colors[index], 255)
    return image


def write_bottom_origin_tga(image: Image.Image, path: Path) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    pixels = rgba.load()
    payload = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            red, green, blue, alpha = pixels[x, y]
            payload.extend((blue, green, red, alpha))

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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header + payload)


def inspect_tga(path: Path, expected_size: tuple[int, int]) -> dict[str, object]:
    data = path.read_bytes()
    (
        id_length,
        color_map_type,
        image_type,
        _color_map_first,
        _color_map_length,
        _color_map_depth,
        _x_origin,
        _y_origin,
        width,
        height,
        pixel_depth,
        descriptor,
    ) = struct.unpack("<BBBHHBHHHHBB", data[:18])
    decoded = Image.open(path).convert("RGBA")
    expected_bytes = 18 + width * height * 4
    checks = {
        "id_length_zero": id_length == 0,
        "no_color_map": color_map_type == 0,
        "uncompressed_true_color": image_type == 2,
        "exact_dimensions": (width, height) == expected_size,
        "32_bit": pixel_depth == 32,
        "bottom_origin": descriptor & 0x20 == 0,
        "eight_alpha_bits": descriptor & 0x0F == 8,
        "opaque_alpha": decoded.getchannel("A").getextrema() == (255, 255),
        "exact_file_size": len(data) == expected_bytes,
    }
    return {
        "path": path.relative_to(MOD_ROOT).as_posix(),
        "width": width,
        "height": height,
        "pixel_depth": pixel_depth,
        "descriptor": descriptor,
        "byte_length": len(data),
        "sha256": sha256(path),
        "checks": checks,
        "valid": all(checks.values()),
    }


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def create_contact_sheet(rows: dict[str, dict[str, Image.Image]]) -> Path:
    label_width = 330
    cell_width = 250
    cell_height = 180
    header_height = 90
    margin = 24
    column_names = ["source", "flat master", "normal TGA", "medium TGA", "small TGA"]
    width = margin * 2 + label_width + cell_width * len(column_names)
    height = header_height + margin + cell_height * len(rows) + margin
    sheet = Image.new("RGB", (width, height), (33, 36, 42))
    draw = ImageDraw.Draw(sheet)
    title_font = load_font(28)
    label_font = load_font(24)
    small_font = load_font(18)
    draw.text(
        (margin, 18),
        "Event 12 Africa revival flags — source, flattened master, and decoded HOI4 ladder",
        fill=(245, 245, 245),
        font=title_font,
    )
    for index, column_name in enumerate(column_names):
        x = margin + label_width + index * cell_width
        draw.text((x + 12, 58), column_name, fill=(212, 215, 221), font=small_font)

    for row_index, (tag, images) in enumerate(rows.items()):
        top = header_height + row_index * cell_height
        draw.rectangle(
            (margin, top, width - margin, top + cell_height - 8),
            fill=(45, 49, 57) if row_index % 2 == 0 else (39, 43, 50),
        )
        draw.text(
            (margin + 12, top + 54),
            f"{tag}  {FLAGS[tag]['name']}",
            fill=(250, 250, 250),
            font=label_font,
        )
        for column_index, key in enumerate(["source", "master", "normal", "medium", "small"]):
            image = images[key].convert("RGBA")
            max_width = cell_width - 28
            max_height = cell_height - 44
            scale = min(max_width / image.width, max_height / image.height)
            display_size = (
                max(1, round(image.width * scale)),
                max(1, round(image.height * scale)),
            )
            display = image.resize(display_size, Image.Resampling.NEAREST)
            x = margin + label_width + column_index * cell_width
            paste_x = x + (cell_width - display.width) // 2
            paste_y = top + (cell_height - display.height) // 2
            checker = Image.new("RGBA", display.size, (235, 235, 235, 255))
            checker.alpha_composite(display)
            sheet.paste(checker.convert("RGB"), (paste_x, paste_y))

    CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
    output = CONTACT_ROOT / "africa_revival_flag_ladders_contact_sheet.png"
    sheet.save(output, optimize=True)
    return output


def main() -> None:
    PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
    CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
    NOTES_ROOT.mkdir(parents=True, exist_ok=True)

    validation: dict[str, object] = {
        "package": "012_africa_independence_wave_flags",
        "scope": "base flags only; no ideology variants",
        "format_contract": {
            "normal": "82x52",
            "medium": "41x26",
            "small": "10x7",
            "tga": "uncompressed true-color, 32-bit BGRA, bottom-left origin, opaque alpha",
        },
        "flags": {},
    }
    contact_rows: dict[str, dict[str, Image.Image]] = {}
    hash_paths: list[Path] = []

    for tag, spec in FLAGS.items():
        source_path = SOURCE_ROOT / str(spec["source"])
        source = Image.open(source_path).convert("RGBA")
        colors = list(spec["palette"])
        master = flatten_to_palette(
            source,
            (820, 520),
            colors,
            Image.Resampling.LANCZOS,
        )
        master_path = PROCESSED_ROOT / f"{tag}_flat_master_820x520.png"
        master.save(master_path, optimize=True)
        hash_paths.extend([source_path, master_path])

        flag_validation: dict[str, object] = {
            "name": spec["name"],
            "classification": spec["classification"],
            "source": source_path.relative_to(MOD_ROOT).as_posix(),
            "source_sha256": sha256(source_path),
            "master": master_path.relative_to(MOD_ROOT).as_posix(),
            "master_sha256": sha256(master_path),
            "palette_rgb": colors,
            "ladder": {},
        }
        contact_images = {
            "source": source,
            "master": master,
        }

        for size_name, dimensions in FLAG_SIZES.items():
            resample = (
                Image.Resampling.NEAREST
                if size_name == "small"
                else Image.Resampling.LANCZOS
            )
            ladder_image = flatten_to_palette(master, dimensions, colors, resample)
            if size_name == "small" and tag in SMALL_PIXEL_PATTERNS:
                ladder_image = render_small_pixel_pattern(
                    SMALL_PIXEL_PATTERNS[tag],
                    colors,
                )
            png_path = PROCESSED_ROOT / size_name / f"{tag}.png"
            png_path.parent.mkdir(parents=True, exist_ok=True)
            ladder_image.save(png_path, optimize=True)

            if size_name == "normal":
                tga_path = MOD_ROOT / "gfx" / "flags" / f"{tag}.tga"
            else:
                tga_path = MOD_ROOT / "gfx" / "flags" / size_name / f"{tag}.tga"
            write_bottom_origin_tga(ladder_image, tga_path)

            decoded = Image.open(tga_path).convert("RGBA")
            if decoded.tobytes() != ladder_image.tobytes():
                raise RuntimeError(f"{tga_path}: Pillow TGA round-trip differs")
            tga_result = inspect_tga(tga_path, dimensions)
            if not tga_result["valid"]:
                raise RuntimeError(f"{tga_path}: TGA contract validation failed")

            flag_validation["ladder"][size_name] = {
                "processed_png": png_path.relative_to(MOD_ROOT).as_posix(),
                "processed_png_sha256": sha256(png_path),
                "runtime_tga": tga_result,
            }
            contact_images[size_name] = decoded
            hash_paths.extend([png_path, tga_path])

        validation["flags"][tag] = flag_validation
        contact_rows[tag] = contact_images

    contact_path = create_contact_sheet(contact_rows)
    hash_paths.append(contact_path)
    validation["contact_sheet"] = contact_path.relative_to(MOD_ROOT).as_posix()
    validation["contact_sheet_sha256"] = sha256(contact_path)
    validation["all_valid"] = all(
        ladder["runtime_tga"]["valid"]
        for flag in validation["flags"].values()
        for ladder in flag["ladder"].values()
    )

    validation_path = NOTES_ROOT / "validation.json"
    validation_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    hashes_path = NOTES_ROOT / "hashes.sha256"
    lines = [
        f"{sha256(path)}  {path.relative_to(MOD_ROOT).as_posix()}"
        for path in sorted(set(hash_paths))
    ]
    hashes_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Built {len(FLAGS) * len(FLAG_SIZES)} runtime TGA files.")
    print(f"Validation: {validation['all_valid']}")
    print(f"Contact sheet: {contact_path.relative_to(MOD_ROOT)}")


if __name__ == "__main__":
    main()
