#!/usr/bin/env python3
"""Process the KCX, NUX, and RLX ImageGen flag masters.

The three source PNGs are genuine official ImageGen outputs. This processor
does not draw or replace their designs. It performs only the permitted
technical finishing pass: researched-aspect cropping, solid-colour cleanup
that retains the generated silhouettes, resizing, bottom-left 32-bit TGA
encoding, runtime installation, contact sheets, hashes, and validation.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = PACKAGE_ROOT / "source_png"
PROCESSED_DIR = PACKAGE_ROOT / "processed_png"
FINAL_TGA_DIR = PACKAGE_ROOT / "final_tga"
CONTACT_DIR = PACKAGE_ROOT / "contact_sheets"
METADATA_DIR = PACKAGE_ROOT / "metadata"

MASTER_SIZE = (820, 520)
SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}


@dataclass(frozen=True)
class FlagSpec:
    tag: str
    identity: str
    source_name: str
    crop_box: tuple[int, int, int, int]
    expected_source_size: tuple[int, int]
    palette: tuple[tuple[int, int, int], ...]


SPECS = (
    FlagSpec(
        tag="KCX",
        identity="Celtic Congress",
        source_name="KCX_celtic_congress_heather_imagegen_raw.png",
        # The generated center panel spans x=456..1120. Cropping the equal
        # excess from the two outer fields preserves the generated heather
        # while bringing the three generated panels to the accepted 1:2:1.
        crop_box=(123, 77, 1453, 920),
        expected_source_size=(1577, 997),
        palette=((34, 84, 61), (241, 232, 207), (112, 69, 108)),
    ),
    FlagSpec(
        tag="NUX",
        identity="North Atlantic Union",
        source_name="NUX_north_atlantic_union_saltire_cross_imagegen_raw.png",
        # The crop preserves the generated saltire and cross while centering
        # the generated red arms at one third width and one half height.
        crop_box=(96, 32, 1513, 931),
        expected_source_size=(1576, 998),
        palette=((16, 46, 74), (255, 255, 255), (183, 47, 59)),
    ),
    FlagSpec(
        tag="RLX",
        identity="Rhenish League",
        source_name="RLX_rhenish_league_river_tricolor_imagegen_raw.png",
        crop_box=(0, 0, 1576, 998),
        expected_source_size=(1576, 998),
        palette=((22, 131, 74), (242, 240, 230), (197, 45, 52), (36, 91, 134)),
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def hex_colour(colour: tuple[int, int, int]) -> str:
    return "#%02X%02X%02X" % colour


def palette_values(image: Image.Image) -> list[str]:
    return sorted(hex_colour(colour) for colour in set(image.convert("RGB").getdata()))


def nearest_palette(
    pixels: np.ndarray,
    palette: tuple[tuple[int, int, int], ...],
) -> np.ndarray:
    values = pixels.astype(np.int32)
    colours = np.asarray(palette, dtype=np.int32)
    distances = ((values[:, :, None, :] - colours[None, None, :, :]) ** 2).sum(axis=3)
    return distances.argmin(axis=2)


def clean_kcx(pixels: np.ndarray, palette: tuple[tuple[int, int, int], ...]) -> np.ndarray:
    values = pixels.astype(np.int32)
    red, green, blue = values[:, :, 0], values[:, :, 1], values[:, :, 2]
    purple = (red > green + 15) & (blue > green + 12) & (red < 205)
    field_palette = palette[:2]
    field_labels = nearest_palette(pixels, field_palette)
    output = np.asarray(field_palette, dtype=np.uint8)[field_labels]
    output[purple] = palette[2]
    return output


def clean_nux(pixels: np.ndarray, palette: tuple[tuple[int, int, int], ...]) -> np.ndarray:
    values = pixels.astype(np.int32)
    red, green, blue = values[:, :, 0], values[:, :, 1], values[:, :, 2]
    red_device = (red > 115) & (red > green + 42) & (red > blue + 32)
    field_palette = palette[:2]
    field_labels = nearest_palette(pixels, field_palette)
    output = np.asarray(field_palette, dtype=np.uint8)[field_labels]
    output[red_device] = palette[2]
    return output


def clean_rlx(pixels: np.ndarray, palette: tuple[tuple[int, int, int], ...]) -> np.ndarray:
    values = pixels.astype(np.int32)
    red, green, blue = values[:, :, 0], values[:, :, 1], values[:, :, 2]
    blue_river = (blue > red + 30) & (blue > green + 5) & (blue > 75)
    green_field = (green > red + 30) & (green > blue + 20)
    red_field = (red > green + 45) & (red > blue + 40)
    output = np.empty_like(pixels, dtype=np.uint8)
    output[:, :] = palette[1]
    output[green_field] = palette[0]
    output[red_field] = palette[2]
    output[blue_river] = palette[3]
    return output


def clean_image(spec: FlagSpec, image: Image.Image) -> Image.Image:
    pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
    if spec.tag == "KCX":
        cleaned = clean_kcx(pixels, spec.palette)
    elif spec.tag == "NUX":
        cleaned = clean_nux(pixels, spec.palette)
    elif spec.tag == "RLX":
        cleaned = clean_rlx(pixels, spec.palette)
    else:
        raise ValueError(f"Unsupported tag: {spec.tag}")
    return Image.fromarray(cleaned, mode="RGB")


def write_tga_bottom_left(path: Path, image: Image.Image) -> None:
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    height, width = rgba.shape[:2]
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
    bgra_bottom_up = rgba[::-1, :, [2, 1, 0, 3]].tobytes()
    path.write_bytes(header + bgra_bottom_up)


def read_tga_metadata(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    if len(raw) < 18:
        raise ValueError(f"Truncated TGA: {path}")
    header = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    width, height = header[8], header[9]
    descriptor = header[11]
    return {
        "image_type": header[2],
        "width": width,
        "height": height,
        "pixel_depth": header[10],
        "alpha_bits": descriptor & 0x0F,
        "origin": "top-left" if descriptor & 0x20 else "bottom-left",
        "descriptor": descriptor,
        "byte_length": len(raw),
        "expected_uncompressed_byte_length": 18 + width * height * 4,
    }


def connected_components(mask: np.ndarray) -> list[int]:
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    sizes: list[int] = []
    for y in range(height):
        for x in range(width):
            if not mask[y, x] or seen[y, x]:
                continue
            stack = [(x, y)]
            seen[y, x] = True
            size = 0
            while stack:
                current_x, current_y = stack.pop()
                size += 1
                # Four-neighbour connectivity matches how distinct tiny
                # pixel-art heads read: diagonal contact does not merge two
                # blossoms into one silhouette at native flag scale.
                for offset_x, offset_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_x, next_y = current_x + offset_x, current_y + offset_y
                    if not (0 <= next_x < width and 0 <= next_y < height):
                        continue
                    if mask[next_y, next_x] and not seen[next_y, next_x]:
                        seen[next_y, next_x] = True
                        stack.append((next_x, next_y))
            sizes.append(size)
    return sorted(sizes, reverse=True)


def colour_mask(image: Image.Image, colour: tuple[int, int, int]) -> np.ndarray:
    pixels = np.asarray(image.convert("RGB"), dtype=np.uint8)
    return np.all(pixels == np.asarray(colour, dtype=np.uint8), axis=2)


def semantic_validation(spec: FlagSpec, image: Image.Image) -> dict[str, object]:
    width, height = image.size
    if spec.tag == "KCX":
        purple = colour_mask(image, spec.palette[2])
        green = colour_mask(image, spec.palette[0])
        components = connected_components(purple)
        central_green = int(green[:, width // 4 : (width * 3) // 4].sum())
        return {
            "purple_pixels": int(purple.sum()),
            "purple_component_sizes": components,
            "three_generated_blossoms_separate": len([size for size in components if size > 0]) >= 3,
            "central_stem_green_pixels": central_green,
            "heather_device_visible": int(purple.sum()) > 0 and central_green > 0,
        }
    if spec.tag == "NUX":
        red = colour_mask(image, spec.palette[2])
        white = colour_mask(image, spec.palette[1])
        quadrant_counts = {
            "upper_left": int(white[: height // 2, : width // 2].sum()),
            "upper_right": int(white[: height // 2, width // 2 :].sum()),
            "lower_left": int(white[height // 2 :, : width // 2].sum()),
            "lower_right": int(white[height // 2 :, width // 2 :].sum()),
        }
        return {
            "red_pixels": int(red.sum()),
            "red_vertical_arm_crosses_every_row": bool(np.all(red.any(axis=1))),
            "red_horizontal_arm_crosses_every_column": bool(np.all(red.any(axis=0))),
            "white_pixels_by_quadrant": quadrant_counts,
            "saltire_visible_in_every_quadrant": all(value > 0 for value in quadrant_counts.values()),
        }
    if spec.tag == "RLX":
        blue = colour_mask(image, spec.palette[3])
        top_row = np.asarray(image.convert("RGB"), dtype=np.uint8)[0]
        return {
            "blue_pixels": int(blue.sum()),
            "blue_river_crosses_every_row": bool(np.all(blue.any(axis=1))),
            "top_left_is_green": bool(np.array_equal(top_row[0], spec.palette[0])),
            "top_center_contains_blue": bool(np.any(np.all(top_row == spec.palette[3], axis=1))),
            "top_right_is_red": bool(np.array_equal(top_row[-1], spec.palette[2])),
        }
    raise ValueError(spec.tag)


def fit_preview(image: Image.Image, max_size: tuple[int, int], resample: int) -> Image.Image:
    copy = image.copy()
    copy.thumbnail(max_size, resample)
    return copy


def create_source_contact_sheet(sources: dict[str, Image.Image]) -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (1600, 390), (235, 235, 235))
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 10), "Official ImageGen source masters - retained before technical cleanup", fill=(0, 0, 0), font=font)
    for index, spec in enumerate(SPECS):
        image = sources[spec.tag]
        preview = fit_preview(image, (500, 317), Image.Resampling.LANCZOS)
        x = 16 + index * 528
        y = 52
        sheet.paste(preview, (x, y))
        draw.text((x, 34), f"{spec.tag} - {spec.identity} - source {image.width}x{image.height}", fill=(0, 0, 0), font=font)
    sheet.save(CONTACT_DIR / "source_masters_contact_sheet.png")


def create_native_contact_sheet(outputs: dict[str, dict[str, Image.Image]]) -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (560, 350), (238, 238, 238))
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 10), "Final flags at exact native sizes (1:1 pixels)", fill=(0, 0, 0), font=font)
    positions = {"normal": 160, "medium": 310, "small": 445}
    for column, name in enumerate(("normal", "medium", "small")):
        draw.text((positions[name], 34), f"{name} {SIZES[name][0]}x{SIZES[name][1]}", fill=(0, 0, 0), font=font)
    for row, spec in enumerate(SPECS):
        y = 78 + row * 88
        draw.text((16, y + 18), spec.tag, fill=(0, 0, 0), font=font)
        for name in ("normal", "medium", "small"):
            image = outputs[spec.tag][name]
            x = positions[name]
            sheet.paste(image, (x, y))
            draw.rectangle((x - 1, y - 1, x + image.width, y + image.height), outline=(80, 80, 80))
    sheet.save(CONTACT_DIR / "final_size_ladder_native_contact_sheet.png")


def create_enlarged_contact_sheet(outputs: dict[str, dict[str, Image.Image]]) -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (1310, 970), (232, 232, 232))
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 10), "Nearest-neighbour enlargement of every final native flag", fill=(0, 0, 0), font=font)
    scales = {"normal": 5, "medium": 10, "small": 40}
    x_positions = {"normal": 16, "medium": 450, "small": 884}
    for name in ("normal", "medium", "small"):
        draw.text((x_positions[name], 34), f"{name} {SIZES[name][0]}x{SIZES[name][1]} at {scales[name]}x", fill=(0, 0, 0), font=font)
    for row, spec in enumerate(SPECS):
        y = 68 + row * 285
        for name in ("normal", "medium", "small"):
            image = outputs[spec.tag][name]
            scale = scales[name]
            enlarged = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
            x = x_positions[name]
            draw.text((x, y), f"{spec.tag} - {spec.identity}", fill=(0, 0, 0), font=font)
            sheet.paste(enlarged, (x, y + 18))
            draw.rectangle((x - 1, y + 17, x + enlarged.width, y + 18 + enlarged.height), outline=(70, 70, 70))
    sheet.save(CONTACT_DIR / "final_size_ladder_enlarged_nearest_contact_sheet.png")


def create_source_vs_final_sheet(
    sources: dict[str, Image.Image],
    masters: dict[str, Image.Image],
    outputs: dict[str, dict[str, Image.Image]],
) -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (1900, 870), (235, 235, 235))
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 10), "ImageGen source crop, cleaned generated master, and final size ladder", fill=(0, 0, 0), font=font)
    for row, spec in enumerate(SPECS):
        y = 48 + row * 270
        source_crop = sources[spec.tag].crop(spec.crop_box).resize((410, 260), Image.Resampling.LANCZOS)
        master_preview = masters[spec.tag].resize((410, 260), Image.Resampling.NEAREST)
        draw.text((16, y), f"{spec.tag} source crop", fill=(0, 0, 0), font=font)
        sheet.paste(source_crop, (16, y + 18))
        draw.text((446, y), f"{spec.tag} solid-colour cleanup of generated geometry", fill=(0, 0, 0), font=font)
        sheet.paste(master_preview, (446, y + 18))
        x = 886
        for name, scale in (("normal", 4), ("medium", 8), ("small", 28)):
            image = outputs[spec.tag][name]
            enlarged = image.resize((image.width * scale, image.height * scale), Image.Resampling.NEAREST)
            draw.text((x, y), f"{name} {image.width}x{image.height}", fill=(0, 0, 0), font=font)
            sheet.paste(enlarged, (x, y + 18))
            x += max(enlarged.width, 120) + 12
    sheet.save(CONTACT_DIR / "source_vs_final_contact_sheet.png")


def write_checksums() -> None:
    checksum_path = METADATA_DIR / "checksums.sha256"
    package_files = [
        path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path != checksum_path
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    ]
    runtime_files = []
    for spec in SPECS:
        runtime_files.extend(
            (
                REPO_ROOT / "gfx" / "flags" / f"{spec.tag}.tga",
                REPO_ROOT / "gfx" / "flags" / "medium" / f"{spec.tag}.tga",
                REPO_ROOT / "gfx" / "flags" / "small" / f"{spec.tag}.tga",
            )
        )
    lines = [
        f"{sha256(path)}  {path.relative_to(PACKAGE_ROOT).as_posix()}"
        for path in sorted(package_files)
    ]
    lines.extend(
        f"{sha256(path)}  repo:{path.relative_to(REPO_ROOT).as_posix()}"
        for path in sorted(runtime_files)
    )
    checksum_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def process() -> None:
    for directory in (PROCESSED_DIR, FINAL_TGA_DIR, CONTACT_DIR, METADATA_DIR):
        directory.mkdir(parents=True, exist_ok=True)

    sources: dict[str, Image.Image] = {}
    masters: dict[str, Image.Image] = {}
    outputs: dict[str, dict[str, Image.Image]] = {}
    validation: dict[str, object] = {
        "asset_classification": "three alternate-history generated base flags",
        "processing_rule": "technical cleanup preserves ImageGen-authored geometry; no local source drawing",
        "master_size": list(MASTER_SIZE),
        "flags": {},
    }

    for spec in SPECS:
        source_path = SOURCE_DIR / spec.source_name
        source = Image.open(source_path).convert("RGB")
        if source.size != spec.expected_source_size:
            raise ValueError(f"{spec.tag} source size {source.size} != {spec.expected_source_size}")
        sources[spec.tag] = source

        crop = source.crop(spec.crop_box)
        resized = crop.resize(MASTER_SIZE, Image.Resampling.LANCZOS)
        master = clean_image(spec, resized)
        master_path = PROCESSED_DIR / f"{spec.tag}_flat_master_820x520.png"
        master.save(master_path)
        masters[spec.tag] = master

        tag_outputs: dict[str, Image.Image] = {}
        size_records: dict[str, object] = {}
        for role, size in SIZES.items():
            # The KCX 10x7 export needs point sampling to retain the generated
            # three-blossom cluster and perfectly straight 1:2:1 panel edges.
            # The other ladders retain LANCZOS because their diagonal or wavy
            # generated devices need coverage-aware reduction.
            resample = (
                Image.Resampling.NEAREST
                if spec.tag == "KCX" and role == "small"
                else Image.Resampling.LANCZOS
            )
            candidate = clean_image(spec, master.resize(size, resample))
            png_path = PROCESSED_DIR / f"{spec.tag}_{role}_{size[0]}x{size[1]}.png"
            package_tga = FINAL_TGA_DIR / f"{spec.tag}_{role}_{size[0]}x{size[1]}.tga"
            candidate.save(png_path)
            write_tga_bottom_left(package_tga, candidate)
            tag_outputs[role] = candidate

            if role == "normal":
                runtime_path = REPO_ROOT / "gfx" / "flags" / f"{spec.tag}.tga"
            else:
                runtime_path = REPO_ROOT / "gfx" / "flags" / role / f"{spec.tag}.tga"
            runtime_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(package_tga, runtime_path)

            decoded_package = Image.open(package_tga).convert("RGB")
            decoded_runtime = Image.open(runtime_path).convert("RGB")
            decoded_package_matches_png = np.array_equal(
                np.asarray(decoded_package), np.asarray(candidate)
            )
            decoded_runtime_matches_png = np.array_equal(
                np.asarray(decoded_runtime), np.asarray(candidate)
            )
            if not decoded_package_matches_png or not decoded_runtime_matches_png:
                raise ValueError(f"{spec.tag} {role} TGA decode differs from the processed PNG")
            # Contact sheets review the decoded runtime TGA, not a PNG proxy.
            tag_outputs[role] = decoded_runtime

            tga_metadata = read_tga_metadata(package_tga)
            expected_palette = sorted(hex_colour(colour) for colour in spec.palette)
            actual_palette = palette_values(candidate)
            size_records[role] = {
                "dimensions": list(candidate.size),
                "resampling": "nearest" if resample == Image.Resampling.NEAREST else "lanczos",
                "png": png_path.relative_to(PACKAGE_ROOT).as_posix(),
                "package_tga": package_tga.relative_to(PACKAGE_ROOT).as_posix(),
                "runtime_tga": runtime_path.relative_to(REPO_ROOT).as_posix(),
                "palette": actual_palette,
                "expected_palette": expected_palette,
                "exact_palette": actual_palette == expected_palette,
                "semantic_readability": semantic_validation(spec, candidate),
                "png_sha256": sha256(png_path),
                "package_tga_sha256": sha256(package_tga),
                "runtime_tga_sha256": sha256(runtime_path),
                "runtime_matches_package": sha256(package_tga) == sha256(runtime_path),
                "decoded_package_tga_matches_png": decoded_package_matches_png,
                "decoded_runtime_tga_matches_png": decoded_runtime_matches_png,
                "tga_header": tga_metadata,
                "tga_bottom_left_32bit_uncompressed": (
                    tga_metadata["image_type"] == 2
                    and tga_metadata["pixel_depth"] == 32
                    and tga_metadata["origin"] == "bottom-left"
                    and tga_metadata["byte_length"] == tga_metadata["expected_uncompressed_byte_length"]
                ),
            }

        outputs[spec.tag] = tag_outputs
        validation["flags"][spec.tag] = {
            "identity": spec.identity,
            "source": source_path.relative_to(PACKAGE_ROOT).as_posix(),
            "source_dimensions": list(source.size),
            "source_sha256": sha256(source_path),
            "crop_box": list(spec.crop_box),
            "crop_dimensions": [spec.crop_box[2] - spec.crop_box[0], spec.crop_box[3] - spec.crop_box[1]],
            "master": master_path.relative_to(PACKAGE_ROOT).as_posix(),
            "master_palette": palette_values(master),
            "master_semantic_readability": semantic_validation(spec, master),
            "sizes": size_records,
        }

    create_source_contact_sheet(sources)
    create_native_contact_sheet(outputs)
    create_enlarged_contact_sheet(outputs)
    create_source_vs_final_sheet(sources, masters, outputs)

    validation["contact_sheets"] = [
        "contact_sheets/source_masters_contact_sheet.png",
        "contact_sheets/final_size_ladder_native_contact_sheet.png",
        "contact_sheets/final_size_ladder_enlarged_nearest_contact_sheet.png",
        "contact_sheets/source_vs_final_contact_sheet.png",
    ]
    (METADATA_DIR / "flag_validation.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
    )
    write_checksums()


if __name__ == "__main__":
    process()
