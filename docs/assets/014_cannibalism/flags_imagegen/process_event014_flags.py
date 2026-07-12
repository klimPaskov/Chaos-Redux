"""Process the frozen Event 014 flag source sheets into HOI4 flag assets.

The source artwork is image-generated. This helper only crops the five selected
panels from each sheet, resizes them, writes bottom-left-origin uncompressed
32-bit TGAs, creates review contact sheets, and records mechanical validation.
"""

from __future__ import annotations

import csv
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parents[3]

FAMILIES = (
    "CBA",
    "CBB",
    "CBC",
    "CBD",
    "CBE",
    "CBF",
    "CBG",
    "CBH",
    "CBL",
    "CBL_CENTRAL_COMMAND",
    "CBL_HOST_CONFEDERATION",
    "CBL_RITUAL_STATE",
    "ZZZ_CANNIBALISM_HANNIBAL",
)

VARIANTS = (
    ("", "base"),
    ("_communism", "communism"),
    ("_democratic", "democratic"),
    ("_fascism", "fascism"),
    ("_neutrality", "neutrality"),
)

SIZES = {
    "82x52": (82, 52),
    "41x26": (41, 26),
    "10x7": (10, 7),
}

LIVE_DIRS = {
    "82x52": REPO_ROOT / "gfx" / "flags",
    "41x26": REPO_ROOT / "gfx" / "flags" / "medium",
    "10x7": REPO_ROOT / "gfx" / "flags" / "small",
}

SOURCE_SHEETS = PACKAGE_ROOT / "source_sheets"
SOURCE_CROPS = PACKAGE_ROOT / "source_crops"
PROCESSED_ROOT = PACKAGE_ROOT / "processed_png"
CONTACT_ROOT = PACKAGE_ROOT / "contact_sheets"
VALIDATION_ROOT = PACKAGE_ROOT / "validation"


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def crop_box(family: str, panel_index: int) -> tuple[int, int, int, int]:
    """Return the selected cell interior in the 1536x1024 source sheet."""

    col = panel_index % 3
    row = panel_index // 3
    if family == "CBA":
        lefts = (30, 532, 1028)
        rights = (508, 1004, 1510)
        tops = (80, 521)
        bottoms = (479, 935)
    else:
        lefts = (24, 528, 1032)
        rights = (500, 1004, 1508)
        tops = (24, 528)
        bottoms = (500, 1000)
    return lefts[col], tops[row], rights[col], bottoms[row]


def write_tga_bottom_left(image: Image.Image, path: Path) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,  # id length
        0,  # no color map
        2,  # uncompressed true-color image
        0,
        0,
        0,
        0,  # x origin
        0,  # y origin
        width,
        height,
        32,
        8,  # 8 alpha bits, bottom-left origin (bit 5 clear)
    )
    bottom_up = rgba.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        handle.write(header)
        handle.write(bottom_up.tobytes("raw", "BGRA"))


def expected_name(family: str, suffix: str) -> str:
    return f"{family}{suffix}"


def process_assets() -> dict[str, dict[str, Path]]:
    SOURCE_CROPS.mkdir(parents=True, exist_ok=True)
    for size_key in SIZES:
        (PROCESSED_ROOT / size_key).mkdir(parents=True, exist_ok=True)
        LIVE_DIRS[size_key].mkdir(parents=True, exist_ok=True)

    outputs: dict[str, dict[str, Path]] = {}
    for family in FAMILIES:
        sheet_path = SOURCE_SHEETS / f"{family}_source_sheet.png"
        with Image.open(sheet_path) as opened:
            sheet = opened.convert("RGBA")
        if sheet.size != (1536, 1024):
            raise ValueError(f"Unexpected source-sheet size for {family}: {sheet.size}")

        for panel_index, (suffix, _variant_label) in enumerate(VARIANTS):
            name = expected_name(family, suffix)
            crop = sheet.crop(crop_box(family, panel_index)).convert("RGBA")
            crop.putalpha(255)
            crop_path = SOURCE_CROPS / f"{name}_source_crop.png"
            crop.save(crop_path, format="PNG", optimize=True)

            standard = crop.resize(SIZES["82x52"], Image.Resampling.LANCZOS)
            standard.putalpha(255)
            medium = standard.resize(SIZES["41x26"], Image.Resampling.LANCZOS)
            medium.putalpha(255)
            small = standard.resize(SIZES["10x7"], Image.Resampling.LANCZOS)
            small.putalpha(255)
            rendered = {
                "82x52": standard,
                "41x26": medium,
                "10x7": small,
            }

            outputs[name] = {}
            for size_key, image in rendered.items():
                png_path = PROCESSED_ROOT / size_key / f"{name}.png"
                tga_path = LIVE_DIRS[size_key] / f"{name}.tga"
                image.save(png_path, format="PNG", optimize=True)
                write_tga_bottom_left(image, tga_path)
                outputs[name][f"png_{size_key}"] = png_path
                outputs[name][f"tga_{size_key}"] = tga_path

    return outputs


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = (
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/calibri.ttf"),
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


def label_for(family: str, label: str) -> str:
    return f"{family} / {label}"


def make_size_contact_sheet(size_key: str, outputs: dict[str, dict[str, Path]]) -> Path:
    cell_w, cell_h = 270, 190
    canvas = Image.new("RGB", (cell_w * 5, cell_h * 13), (24, 25, 27))
    draw = ImageDraw.Draw(canvas)
    title_font = font(15)
    source_size = SIZES[size_key]
    scale = min(246 // source_size[0], 150 // source_size[1])
    scale = max(scale, 1)
    preview_size = (source_size[0] * scale, source_size[1] * scale)

    for row, family in enumerate(FAMILIES):
        for col, (suffix, variant_label) in enumerate(VARIANTS):
            name = expected_name(family, suffix)
            # Decode the live TGA so the contact sheet proves visual orientation.
            with Image.open(outputs[name][f"tga_{size_key}"]) as opened:
                preview = opened.convert("RGB").resize(preview_size, Image.Resampling.NEAREST)
            x0, y0 = col * cell_w, row * cell_h
            px = x0 + (cell_w - preview.width) // 2
            py = y0 + 28 + (150 - preview.height) // 2
            canvas.paste(preview, (px, py))
            draw.rectangle((x0, y0, x0 + cell_w - 1, y0 + cell_h - 1), outline=(70, 73, 77))
            draw.text((x0 + 8, y0 + 6), label_for(family, variant_label), fill=(232, 232, 226), font=title_font)

    output = CONTACT_ROOT / f"event014_flags_{size_key}_contact_sheet.png"
    CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)
    return output


def make_three_size_contact_sheet(outputs: dict[str, dict[str, Path]]) -> Path:
    cell_w, cell_h = 300, 205
    canvas = Image.new("RGB", (cell_w * 5, cell_h * 13), (22, 23, 25))
    draw = ImageDraw.Draw(canvas)
    title_font = font(15)
    size_font = font(12)

    for row, family in enumerate(FAMILIES):
        for col, (suffix, variant_label) in enumerate(VARIANTS):
            name = expected_name(family, suffix)
            x0, y0 = col * cell_w, row * cell_h
            draw.rectangle((x0, y0, x0 + cell_w - 1, y0 + cell_h - 1), outline=(70, 73, 77))
            draw.text((x0 + 8, y0 + 6), label_for(family, variant_label), fill=(236, 234, 226), font=title_font)

            # All three previews are decoded from the live TGAs.
            with Image.open(outputs[name]["tga_82x52"]) as opened:
                normal = opened.convert("RGB").resize((164, 104), Image.Resampling.NEAREST)
            with Image.open(outputs[name]["tga_41x26"]) as opened:
                medium = opened.convert("RGB").resize((82, 52), Image.Resampling.NEAREST)
            with Image.open(outputs[name]["tga_10x7"]) as opened:
                small = opened.convert("RGB").resize((60, 42), Image.Resampling.NEAREST)

            canvas.paste(normal, (x0 + 8, y0 + 34))
            canvas.paste(medium, (x0 + 180, y0 + 34))
            canvas.paste(small, (x0 + 191, y0 + 96))
            draw.text((x0 + 8, y0 + 143), "82x52", fill=(190, 193, 196), font=size_font)
            draw.text((x0 + 180, y0 + 88), "41x26", fill=(190, 193, 196), font=size_font)
            draw.text((x0 + 191, y0 + 143), "10x7", fill=(190, 193, 196), font=size_font)

    output = CONTACT_ROOT / "event014_flags_three_size_contact_sheet.png"
    CONTACT_ROOT.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)
    return output


def parse_tga(path: Path) -> dict[str, int | str]:
    data = path.read_bytes()
    if len(data) < 18:
        raise ValueError(f"Short TGA: {path}")
    width = int.from_bytes(data[12:14], "little")
    height = int.from_bytes(data[14:16], "little")
    expected_length = 18 + width * height * 4
    return {
        "id_length": data[0],
        "color_map_type": data[1],
        "image_type": data[2],
        "width": width,
        "height": height,
        "bpp": data[16],
        "descriptor": data[17],
        "origin": "top" if data[17] & 0x20 else "bottom",
        "alpha_bits": data[17] & 0x0F,
        "file_length": len(data),
        "expected_length": expected_length,
    }


def validate_outputs(outputs: dict[str, dict[str, Path]]) -> None:
    VALIDATION_ROOT.mkdir(parents=True, exist_ok=True)
    tga_rows: list[dict[str, object]] = []
    normalized_by_size: dict[str, dict[str, list[str]]] = {key: {} for key in SIZES}
    source_digest_to_names: dict[str, list[str]] = {}

    for family in FAMILIES:
        for suffix, _variant_label in VARIANTS:
            name = expected_name(family, suffix)
            crop_path = SOURCE_CROPS / f"{name}_source_crop.png"
            with Image.open(crop_path) as opened:
                crop = opened.convert("RGBA")
                crop_digest = sha256_bytes(struct.pack("<II", *crop.size) + crop.tobytes())
            source_digest_to_names.setdefault(crop_digest, []).append(name)

            for size_key, expected_dimensions in SIZES.items():
                png_path = outputs[name][f"png_{size_key}"]
                tga_path = outputs[name][f"tga_{size_key}"]
                header = parse_tga(tga_path)
                with Image.open(png_path) as opened:
                    png = opened.convert("RGBA")
                with Image.open(tga_path) as opened:
                    tga = opened.convert("RGBA")

                alpha = tga.getchannel("A")
                alpha_min, alpha_max = alpha.getextrema()
                rgba_digest = sha256_bytes(struct.pack("<II", *tga.size) + tga.tobytes())
                normalized_by_size[size_key].setdefault(rgba_digest, []).append(name)

                checks = {
                    "dimensions": tga.size == expected_dimensions,
                    "uncompressed_true_color": header["image_type"] == 2,
                    "32_bit": header["bpp"] == 32,
                    "bottom_left": header["origin"] == "bottom",
                    "alpha_header": header["alpha_bits"] == 8,
                    "alpha_opaque": (alpha_min, alpha_max) == (255, 255),
                    "exact_length": header["file_length"] == header["expected_length"],
                    "matches_processed_png": tga.tobytes() == png.tobytes(),
                }
                status = "PASS" if all(checks.values()) else "FAIL"
                tga_rows.append(
                    {
                        "path": rel(tga_path),
                        "width": header["width"],
                        "height": header["height"],
                        "image_type": header["image_type"],
                        "bpp": header["bpp"],
                        "descriptor_hex": f"0x{header['descriptor']:02X}",
                        "origin": header["origin"],
                        "alpha_bits": header["alpha_bits"],
                        "alpha_min": alpha_min,
                        "alpha_max": alpha_max,
                        "normalized_rgba_sha256": rgba_digest,
                        "matches_processed_png": checks["matches_processed_png"],
                        "status": status,
                    }
                )
                if status != "PASS":
                    failed = [key for key, value in checks.items() if not value]
                    raise ValueError(f"Validation failed for {tga_path}: {failed}")

    validation_path = VALIDATION_ROOT / "tga_validation.tsv"
    with validation_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(tga_rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(tga_rows)

    uniqueness_rows: list[dict[str, object]] = []
    for size_key, digests in normalized_by_size.items():
        duplicates = {digest: names for digest, names in digests.items() if len(names) > 1}
        uniqueness_rows.append(
            {
                "scope": f"normalized_rgba_{size_key}",
                "asset_count": 65,
                "unique_count": len(digests),
                "duplicate_groups": json.dumps(duplicates, sort_keys=True),
                "status": "PASS" if len(digests) == 65 else "FAIL",
            }
        )
        if len(digests) != 65:
            raise ValueError(f"Normalized RGBA duplicates at {size_key}: {duplicates}")

    source_duplicates = {
        digest: names for digest, names in source_digest_to_names.items() if len(names) > 1
    }
    uniqueness_rows.append(
        {
            "scope": "source_crops_rgba",
            "asset_count": 65,
            "unique_count": len(source_digest_to_names),
            "duplicate_groups": json.dumps(source_duplicates, sort_keys=True),
            "status": "PASS" if len(source_digest_to_names) == 65 else "FAIL",
        }
    )
    if len(source_digest_to_names) != 65:
        raise ValueError(f"Duplicate source crops: {source_duplicates}")

    uniqueness_path = VALIDATION_ROOT / "rgba_uniqueness.tsv"
    with uniqueness_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(uniqueness_rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(uniqueness_rows)

    summary = {
        "families": len(FAMILIES),
        "compositions_per_family": len(VARIANTS),
        "source_sheets": len(list(SOURCE_SHEETS.glob("*_source_sheet.png"))),
        "source_crops": len(list(SOURCE_CROPS.glob("*_source_crop.png"))),
        "processed_pngs": sum(len(list((PROCESSED_ROOT / key).glob("*.png"))) for key in SIZES),
        "live_tgas": len(tga_rows),
        "tga_passes": sum(row["status"] == "PASS" for row in tga_rows),
        "contact_sheets": len(list(CONTACT_ROOT.glob("*.png"))),
        "all_normalized_rgba_unique_each_size": all(
            len(digests) == 65 for digests in normalized_by_size.values()
        ),
        "all_source_crops_unique": len(source_digest_to_names) == 65,
    }
    (VALIDATION_ROOT / "processing_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def write_asset_manifest(outputs: dict[str, dict[str, Path]]) -> None:
    manifest_path = PACKAGE_ROOT / "asset_manifest.tsv"
    fieldnames = (
        "family",
        "variant",
        "asset_stem",
        "source_mode",
        "source_sheet",
        "source_crop",
        "processed_82x52",
        "processed_41x26",
        "processed_10x7",
        "live_tga_82x52",
        "live_tga_41x26",
        "live_tga_10x7",
        "format_contract",
        "prompt_ledger",
        "status",
    )
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for family in FAMILIES:
            for suffix, variant_label in VARIANTS:
                name = expected_name(family, suffix)
                writer.writerow(
                    {
                        "family": family,
                        "variant": variant_label,
                        "asset_stem": name,
                        "source_mode": "built-in image_gen fictional source-sheet crop",
                        "source_sheet": rel(SOURCE_SHEETS / f"{family}_source_sheet.png"),
                        "source_crop": rel(SOURCE_CROPS / f"{name}_source_crop.png"),
                        "processed_82x52": rel(outputs[name]["png_82x52"]),
                        "processed_41x26": rel(outputs[name]["png_41x26"]),
                        "processed_10x7": rel(outputs[name]["png_10x7"]),
                        "live_tga_82x52": rel(outputs[name]["tga_82x52"]),
                        "live_tga_41x26": rel(outputs[name]["tga_41x26"]),
                        "live_tga_10x7": rel(outputs[name]["tga_10x7"]),
                        "format_contract": "uncompressed 32-bit RGBA TGA; bottom-left origin; opaque alpha",
                        "prompt_ledger": rel(PACKAGE_ROOT / "prompts" / "imagegen_prompt_ledger.md"),
                        "status": "complete",
                    }
                )


def write_hash_inventory(outputs: dict[str, dict[str, Path]]) -> None:
    rows: list[tuple[str, Path]] = []
    rows.extend(("source_sheet", path) for path in sorted(SOURCE_SHEETS.glob("*.png")))
    rows.extend(("source_crop", path) for path in sorted(SOURCE_CROPS.glob("*.png")))
    for size_key in SIZES:
        rows.extend((f"processed_png_{size_key}", path) for path in sorted((PROCESSED_ROOT / size_key).glob("*.png")))
    rows.extend(("contact_sheet", path) for path in sorted(CONTACT_ROOT.glob("*.png")))
    rows.extend(("prompt_record", path) for path in sorted((PACKAGE_ROOT / "prompts").glob("*")) if path.is_file())
    rows.append(("asset_manifest", PACKAGE_ROOT / "asset_manifest.tsv"))
    for name in sorted(outputs):
        for size_key in SIZES:
            rows.append((f"live_tga_{size_key}", outputs[name][f"tga_{size_key}"]))

    inventory = VALIDATION_ROOT / "sha256sums.tsv"
    with inventory.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(("category", "path", "bytes", "sha256"))
        for category, path in rows:
            writer.writerow((category, rel(path), path.stat().st_size, sha256_file(path)))


def main() -> None:
    outputs = process_assets()
    for size_key in SIZES:
        make_size_contact_sheet(size_key, outputs)
    make_three_size_contact_sheet(outputs)
    write_asset_manifest(outputs)
    validate_outputs(outputs)
    write_hash_inventory(outputs)
    summary = json.loads((VALIDATION_ROOT / "processing_summary.json").read_text(encoding="utf-8"))
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
