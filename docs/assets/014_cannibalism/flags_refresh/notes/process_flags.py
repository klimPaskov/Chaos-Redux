"""Build the Event 014 flag package and runtime TGA exports.

Generated source masters remain untouched. Each runtime master is center-cropped to
the HOI4 82:52 aspect, resized, and adaptively flattened without dithering to three
through five fully opaque colors. This is colour management, not drawing: no
generated emblem is traced, replaced, edge-simplified, or rebuilt from primitives.
Medium and small flags are derived from the retained generated design. TGA files
are written directly so the bottom-left origin and 32-bit uncompressed layout are
explicit rather than delegated to an encoder default.
"""

from __future__ import annotations

import hashlib
import json
import math
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = PACKAGE / "source_png"
PROCESSED_DIR = PACKAGE / "processed_png"
PROMPTS_DIR = PACKAGE / "prompts"
SHEETS_DIR = PACKAGE / "contact_sheets"
SPECS_PATH = PROMPTS_DIR / "prompt_specs.json"
EVIDENCE_PATH = PACKAGE / "generation_evidence.json"
VALIDATION_PATH = PACKAGE / "validation.json"

NORMAL_DIR = ROOT / "gfx" / "flags"
MEDIUM_DIR = NORMAL_DIR / "medium"
SMALL_DIR = NORMAL_DIR / "small"

SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

# Maximum coverage best preserves the small, high-contrast generated heraldry in
# most masters. These visually reviewed exceptions use the Pillow method that
# retains their source palette and device silhouette more faithfully at 82x52.
QUANTIZE_OVERRIDES = {
    "CBA_democratic": Image.Quantize.FASTOCTREE,
    "CBA_neutrality": Image.Quantize.FASTOCTREE,
    "CBC_democratic": Image.Quantize.FASTOCTREE,
    "CBE": Image.Quantize.MEDIANCUT,
    "CBF_communism": Image.Quantize.FASTOCTREE,
    "CBF_democratic": Image.Quantize.FASTOCTREE,
    "CBG": Image.Quantize.MEDIANCUT,
    "CBG_neutrality": Image.Quantize.MEDIANCUT,
    "CBH": Image.Quantize.MEDIANCUT,
}

QUANTIZE_NAMES = {
    Image.Quantize.MEDIANCUT: "median-cut",
    Image.Quantize.MAXCOVERAGE: "maximum-coverage",
    Image.Quantize.FASTOCTREE: "fast-octree",
}


def center_crop_to_ratio(image: Image.Image, target: tuple[int, int]) -> Image.Image:
    target_ratio = target[0] / target[1]
    source_ratio = image.width / image.height
    if source_ratio > target_ratio:
        width = round(image.height * target_ratio)
        left = (image.width - width) // 2
        box = (left, 0, left + width, image.height)
    else:
        height = round(image.width / target_ratio)
        top = (image.height - height) // 2
        box = (0, top, image.width, top + height)
    return image.crop(box)


def flatten_master(
    source: Image.Image,
    method: Image.Quantize = Image.Quantize.MAXCOVERAGE,
) -> tuple[Image.Image, list[tuple[int, int, int]]]:
    cropped = center_crop_to_ratio(source.convert("RGB"), SIZES["normal"])
    resized = cropped.resize(SIZES["normal"], Image.Resampling.LANCZOS)
    quantized = resized.quantize(
        colors=5,
        method=method,
        dither=Image.Dither.NONE,
    )
    flattened = quantized.convert("RGB")
    counts = flattened.getcolors(maxcolors=82 * 52)
    if not counts:
        raise RuntimeError("Could not enumerate flattened palette")
    palette = [color for _, color in sorted(counts, reverse=True)]
    if not 3 <= len(palette) <= 5:
        raise RuntimeError(f"Expected 3-5 colors, got {len(palette)}")
    return flattened, palette


def resize_to_palette(
    image: Image.Image,
    target: tuple[int, int],
    palette: list[tuple[int, int, int]],
) -> Image.Image:
    resized = image.resize(target, Image.Resampling.LANCZOS).convert("RGB")
    mapped: list[tuple[int, int, int]] = []
    for pixel in resized.getdata():
        mapped.append(
            min(
                palette,
                key=lambda color: (
                    (pixel[0] - color[0]) ** 2
                    + (pixel[1] - color[1]) ** 2
                    + (pixel[2] - color[2]) ** 2
                ),
            )
        )
    output = Image.new("RGB", target)
    output.putdata(mapped)
    return output


def write_bottom_origin_tga(image: Image.Image, path: Path) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,  # image id length
        0,  # no color map
        2,  # uncompressed true-color image
        0,
        0,
        0,
        0,  # x origin
        0,  # y origin
        width,
        height,
        32,  # BGRA, eight bits per channel
        8,  # eight alpha bits; top-origin bit deliberately unset
    )
    bottom_first = rgba.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header + bottom_first.tobytes("raw", "BGRA"))


def font(size: int) -> ImageFont.ImageFont:
    candidates = (
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
    )
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def crop_preview(source: Image.Image, size: tuple[int, int]) -> Image.Image:
    return center_crop_to_ratio(source.convert("RGB"), size).resize(
        size, Image.Resampling.LANCZOS
    )


def draw_centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, used_font: ImageFont.ImageFont, fill: str) -> None:
    box = draw.textbbox((0, 0), text, font=used_font)
    width = box[2] - box[0]
    draw.text((xy[0] - width // 2, xy[1]), text, font=used_font, fill=fill)


def build_single_contact_sheet(
    specs: list[dict[str, str]],
    source: bool,
    processed: dict[str, Image.Image],
    colors: dict[str, int],
) -> Image.Image:
    columns = 5
    rows = math.ceil(len(specs) / columns)
    tile_width, tile_height = 250, 176
    top_margin = 54
    sheet = Image.new("RGB", (columns * tile_width, top_margin + rows * tile_height), "#17191d")
    draw = ImageDraw.Draw(sheet)
    title_font = font(24)
    label_font = font(11)
    meta_font = font(10)
    title = "EVENT 014 - IMAGEGEN SOURCE MASTERS" if source else "EVENT 014 - FINAL RUNTIME FLAGS (3-5 FLAT COLORS)"
    draw_centered(draw, (sheet.width // 2, 13), title, title_font, "#f1ead8")
    art_size = (205, 130)
    for index, spec in enumerate(specs):
        stem = spec["stem"]
        col = index % columns
        row = index // columns
        x = col * tile_width
        y = top_margin + row * tile_height
        draw_centered(draw, (x + tile_width // 2, y + 3), f"{stem}.tga", label_font, "#f1ead8")
        if source:
            with Image.open(SOURCE_DIR / f"{stem}.png") as image:
                artwork = crop_preview(image, art_size)
        else:
            artwork = processed[stem].resize(art_size, Image.Resampling.NEAREST)
        art_x = x + (tile_width - art_size[0]) // 2
        art_y = y + 23
        sheet.paste(artwork, (art_x, art_y))
        if not source:
            draw_centered(
                draw,
                (x + tile_width // 2, y + 158),
                f"{colors[stem]} colors",
                meta_font,
                "#aeb4be",
            )
    return sheet


def build_comparison_sheet(
    specs: list[dict[str, str]],
    processed: dict[str, Image.Image],
    medium: dict[str, Image.Image],
    small: dict[str, Image.Image],
) -> Image.Image:
    columns = 4
    rows = math.ceil(len(specs) / columns)
    tile_width, tile_height = 430, 158
    top_margin = 58
    sheet = Image.new("RGB", (columns * tile_width, top_margin + rows * tile_height), "#17191d")
    draw = ImageDraw.Draw(sheet)
    title_font = font(24)
    label_font = font(11)
    meta_font = font(9)
    draw_centered(
        draw,
        (sheet.width // 2, 13),
        "EVENT 014 - SOURCE / NORMAL / MEDIUM / SMALL",
        title_font,
        "#f1ead8",
    )
    source_size = (128, 81)
    normal_size = (128, 81)
    medium_size = (80, 51)
    small_size = (50, 35)
    for index, spec in enumerate(specs):
        stem = spec["stem"]
        col = index % columns
        row = index // columns
        x = col * tile_width
        y = top_margin + row * tile_height
        draw_centered(draw, (x + tile_width // 2, y + 1), f"{stem}.tga", label_font, "#f1ead8")
        source_x = x + 8
        normal_x = x + 143
        medium_x = x + 278
        small_x = x + 370
        labels_y = y + 22
        draw_centered(draw, (source_x + source_size[0] // 2, labels_y), "SOURCE", meta_font, "#aeb4be")
        draw_centered(draw, (normal_x + normal_size[0] // 2, labels_y), "NORMAL", meta_font, "#aeb4be")
        draw_centered(draw, (medium_x + medium_size[0] // 2, labels_y), "MEDIUM", meta_font, "#aeb4be")
        draw_centered(draw, (small_x + small_size[0] // 2, labels_y), "SMALL", meta_font, "#aeb4be")
        art_y = y + 39
        with Image.open(SOURCE_DIR / f"{stem}.png") as image:
            source_art = crop_preview(image, source_size)
        normal_art = processed[stem].resize(normal_size, Image.Resampling.NEAREST)
        medium_art = medium[stem].resize(medium_size, Image.Resampling.NEAREST)
        small_art = small[stem].resize(small_size, Image.Resampling.NEAREST)
        sheet.paste(source_art, (source_x, art_y))
        sheet.paste(normal_art, (normal_x, art_y))
        sheet.paste(medium_art, (medium_x, art_y + 15))
        sheet.paste(small_art, (small_x, art_y + 23))
    return sheet


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_and_validate_evidence(
    specs: list[dict[str, str]],
) -> dict[str, dict[str, object]]:
    evidence = json.loads(EVIDENCE_PATH.read_text(encoding="utf-8-sig"))
    assets = evidence.get("assets", [])
    stems = [spec["stem"] for spec in specs]
    records = {asset["stem"]: asset for asset in assets}
    if evidence.get("call_count") != 65 or evidence.get("design_count") != 65:
        raise RuntimeError("generation_evidence.json must record 65 built-in calls")
    if len(assets) != 65 or set(records) != set(stems):
        raise RuntimeError("generation_evidence.json does not match the 65 prompt specs")
    for stem in stems:
        record = records[stem]
        if record.get("mode") != "built-in-imagegen":
            raise RuntimeError(f"{stem} is missing built-in imagegen evidence")
        built_in_output = Path(str(record["built_in_output"]))
        prompt_path = ROOT / str(record["prompt_file"])
        source_path = ROOT / str(record["source_path"])
        if not built_in_output.is_file():
            raise RuntimeError(f"Missing built-in output for {stem}: {built_in_output}")
        if not prompt_path.is_file() or not source_path.is_file():
            raise RuntimeError(f"Missing prompt or source copy for {stem}")
        built_hash = sha256(built_in_output)
        source_hash = sha256(source_path)
        if built_hash != source_hash:
            raise RuntimeError(f"Source copy does not match built-in output for {stem}")
        record["prompt_sha256"] = sha256(prompt_path)
        record["built_in_output_sha256"] = built_hash
        record["source_sha256"] = source_hash
        record["copy_matches_built_in"] = True
    EVIDENCE_PATH.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    return records


def build_manifest(
    specs: list[dict[str, str]],
    source_dimensions: dict[str, tuple[int, int]],
    palette_sizes: dict[str, int],
    quantize_methods: dict[str, str],
    hashes: dict[str, str],
    evidence: dict[str, dict[str, object]],
) -> None:
    lines = [
        "# Event 014 Cannibalism Flag Refresh Manifest",
        "",
        "Canonical provenance and runtime handoff for all 65 live Event 014 flag designs. Each flag was generated independently with the built-in image generator. Source masters are retained verbatim; runtime masters are centered to the HOI4 82:52 aspect and flattened without dithering to three through five opaque colors while preserving the generated emblem geometry.",
        "",
        "- Event: `014_cannibalism`",
        "- Asset type: `flag`",
        "- Source mode: `imagegen`",
        "- Built-in call evidence: `docs/assets/014_cannibalism/flags_refresh/generation_evidence.json`",
        "- Source count: `65`",
        "- Runtime output count: `195`",
        "- Runtime formats: uncompressed 32-bit bottom-origin TGA",
        "- Runtime sizes: normal `82x52`, medium `41x26`, small `10x7`",
        "- Excluded asset: `ZZZ_weaponized_wendigo` (intentionally untouched)",
        "",
    ]
    for spec in specs:
        stem = spec["stem"]
        prompt_path = PROMPTS_DIR / f"{stem}.txt"
        source_path = SOURCE_DIR / f"{stem}.png"
        processed_path = PROCESSED_DIR / f"{stem}.png"
        normal_path = NORMAL_DIR / f"{stem}.tga"
        medium_path = MEDIUM_DIR / f"{stem}.tga"
        small_path = SMALL_DIR / f"{stem}.tga"
        prompt = prompt_path.read_text(encoding="utf-8-sig").rstrip()
        source_width, source_height = source_dimensions[stem]
        record = evidence[stem]
        lines.extend(
            [
                f"## {stem}",
                "",
                "- Event: `014_cannibalism`",
                "- Type: `flag`",
                f"- Intended use: {spec['family_role']}",
                "- Source mode: `imagegen`",
                f"- Built-in output: `{record['built_in_output']}`",
                f"- Prompt SHA-256: `{record['prompt_sha256']}`",
                f"- Source SHA-256: `{record['source_sha256']}`",
                "- Built-in/source copy match: `true`",
                f"- Prompt file: `{relative(prompt_path)}`",
                f"- Source path: `{relative(source_path)}`",
                f"- Processed path: `{relative(processed_path)}`",
                f"- Final normal TGA: `{relative(normal_path)}`",
                f"- Final medium TGA: `{relative(medium_path)}`",
                f"- Final small TGA: `{relative(small_path)}`",
                f"- Dimensions: source `{source_width}x{source_height}`; processed/normal `82x52`; medium `41x26`; small `10x7`",
                f"- Final palette: `{palette_sizes[stem]}` opaque flat colors",
                f"- Flattening method: `{quantize_methods[stem]}` (visually selected from three non-dithered five-color candidates)",
                f"- Processed SHA-256: `{hashes[stem]}`",
                "- Status: `complete`",
                "- Exact prompt:",
                "",
                "```text",
                prompt,
                "```",
                "",
            ]
        )
    (PACKAGE / "manifest.md").write_text("\n".join(lines), encoding="utf-8")


def read_tga_header(path: Path) -> dict[str, int | bool]:
    data = path.read_bytes()
    if len(data) < 18:
        raise RuntimeError(f"Truncated TGA: {path}")
    width, height = struct.unpack_from("<HH", data, 12)
    image_type = data[2]
    depth = data[16]
    descriptor = data[17]
    expected_length = 18 + width * height * 4
    return {
        "width": width,
        "height": height,
        "image_type": image_type,
        "depth": depth,
        "descriptor": descriptor,
        "bottom_origin": not bool(descriptor & 0x20),
        "alpha_bits": descriptor & 0x0F,
        "exact_length": len(data) == expected_length,
    }


def edge_transitions(image: Image.Image) -> int:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    total = 0
    for y in range(rgb.height):
        for x in range(rgb.width):
            if x and pixels[x, y] != pixels[x - 1, y]:
                total += 1
            if y and pixels[x, y] != pixels[x, y - 1]:
                total += 1
    return total


def build_validation(
    specs: list[dict[str, str]],
    processed: dict[str, Image.Image],
    medium: dict[str, Image.Image],
    small: dict[str, Image.Image],
    palette_sizes: dict[str, int],
    quantize_methods: dict[str, str],
    evidence: dict[str, dict[str, object]],
) -> None:
    entries: list[dict[str, object]] = []
    processed_hashes: set[str] = set()
    source_hashes: set[str] = set()
    runtime_hashes: dict[str, set[str]] = {
        "normal": set(),
        "medium": set(),
        "small": set(),
    }
    for spec in specs:
        stem = spec["stem"]
        source_hashes.add(str(evidence[stem]["source_sha256"]))
        processed_path = PROCESSED_DIR / f"{stem}.png"
        processed_hash = sha256(processed_path)
        processed_hashes.add(processed_hash)
        outputs = {
            "normal": (NORMAL_DIR / f"{stem}.tga", processed[stem], SIZES["normal"]),
            "medium": (MEDIUM_DIR / f"{stem}.tga", medium[stem], SIZES["medium"]),
            "small": (SMALL_DIR / f"{stem}.tga", small[stem], SIZES["small"]),
        }
        tga_results: dict[str, object] = {}
        for size_name, (path, expected_image, expected_size) in outputs.items():
            header = read_tga_header(path)
            with Image.open(path) as decoded:
                decoded_rgba = decoded.convert("RGBA")
                decoded_rgb = decoded_rgba.convert("RGB")
            alpha = decoded_rgba.getchannel("A")
            alpha_min, alpha_max = alpha.getextrema()
            runtime_hash = sha256(path)
            runtime_hashes[size_name].add(runtime_hash)
            pixels_match = decoded_rgb.tobytes() == expected_image.convert("RGB").tobytes()
            valid = (
                (header["width"], header["height"]) == expected_size
                and header["image_type"] == 2
                and header["depth"] == 32
                and header["bottom_origin"]
                and header["alpha_bits"] == 8
                and header["exact_length"]
                and alpha_min == 255
                and alpha_max == 255
                and pixels_match
            )
            if not valid:
                raise RuntimeError(f"Invalid {size_name} TGA for {stem}: {header}")
            tga_results[size_name] = {
                **header,
                "sha256": runtime_hash,
                "alpha_min": alpha_min,
                "alpha_max": alpha_max,
                "decoded_pixels_match": pixels_match,
            }
        small_counts = small[stem].getcolors(maxcolors=70) or []
        dominant_small_fraction = max(count for count, _ in small_counts) / 70
        transitions = edge_transitions(processed[stem])
        if len(small_counts) < 2 or dominant_small_fraction >= 0.90:
            raise RuntimeError(f"Small flag lost useful contrast for {stem}")
        if transitions < 40:
            raise RuntimeError(f"Processed flag is too geometrically sparse for {stem}")
        entries.append(
            {
                "stem": stem,
                "source_sha256": evidence[stem]["source_sha256"],
                "processed_sha256": processed_hash,
                "palette_colors": palette_sizes[stem],
                "flattening_method": quantize_methods[stem],
                "normal_edge_transitions": transitions,
                "small_unique_colors": len(small_counts),
                "small_dominant_color_fraction": round(dominant_small_fraction, 4),
                "tga": tga_results,
            }
        )
    if len(source_hashes) != 65:
        raise RuntimeError("Built-in source masters are not all byte-distinct")
    if len(processed_hashes) != 65:
        raise RuntimeError("Processed flag masters are not all byte-distinct")
    for size_name, hashes in runtime_hashes.items():
        if len(hashes) != 65:
            raise RuntimeError(f"Runtime {size_name} TGAs are not all byte-distinct")
    validation = {
        "status": "passed",
        "revision": "built-in-imagegen-regeneration-2026-07-15",
        "design_count": 65,
        "built_in_call_count": 65,
        "source_count": 65,
        "processed_count": 65,
        "runtime_tga_count": 195,
        "all_sources_match_built_in_outputs": True,
        "all_sources_byte_distinct": True,
        "all_processed_masters_byte_distinct": True,
        "all_runtime_tiers_byte_distinct": True,
        "runtime_unique_hashes": {
            size_name: len(hashes) for size_name, hashes in runtime_hashes.items()
        },
        "palette_range": [min(palette_sizes.values()), max(palette_sizes.values())],
        "tga_format": "uncompressed 32-bit BGRA, bottom-left origin, 8 alpha bits",
        "visual_review_sheet": "docs/assets/014_cannibalism/flags_refresh/contact_sheets/source_vs_final_contact_sheet.png",
        "entries": entries,
    }
    VALIDATION_PATH.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    specs = json.loads(SPECS_PATH.read_text(encoding="utf-8-sig"))
    stems = [spec["stem"] for spec in specs]
    if len(stems) != 65 or len(set(stems)) != 65:
        raise RuntimeError("prompt_specs.json must contain exactly 65 unique stems")
    source_stems = {path.stem for path in SOURCE_DIR.glob("*.png")}
    if source_stems != set(stems):
        missing = sorted(set(stems) - source_stems)
        extra = sorted(source_stems - set(stems))
        raise RuntimeError(f"Source mismatch; missing={missing}, extra={extra}")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    SHEETS_DIR.mkdir(parents=True, exist_ok=True)
    processed: dict[str, Image.Image] = {}
    medium_images: dict[str, Image.Image] = {}
    small_images: dict[str, Image.Image] = {}
    source_dimensions: dict[str, tuple[int, int]] = {}
    palette_sizes: dict[str, int] = {}
    quantize_methods: dict[str, str] = {}
    hashes: dict[str, str] = {}
    evidence = load_and_validate_evidence(specs)

    for stem in stems:
        source_path = SOURCE_DIR / f"{stem}.png"
        method = QUANTIZE_OVERRIDES.get(stem, Image.Quantize.MAXCOVERAGE)
        with Image.open(source_path) as source:
            source_dimensions[stem] = source.size
            master, palette = flatten_master(source, method)
        processed[stem] = master
        palette_sizes[stem] = len(palette)
        quantize_methods[stem] = QUANTIZE_NAMES[method]
        processed_path = PROCESSED_DIR / f"{stem}.png"
        master.save(processed_path, format="PNG", optimize=True)
        hashes[stem] = hashlib.sha256(processed_path.read_bytes()).hexdigest()

        medium = resize_to_palette(master, SIZES["medium"], palette)
        small = resize_to_palette(master, SIZES["small"], palette)
        medium_images[stem] = medium
        small_images[stem] = small
        write_bottom_origin_tga(master, NORMAL_DIR / f"{stem}.tga")
        write_bottom_origin_tga(medium, MEDIUM_DIR / f"{stem}.tga")
        write_bottom_origin_tga(small, SMALL_DIR / f"{stem}.tga")

    source_sheet = build_single_contact_sheet(specs, True, processed, palette_sizes)
    final_sheet = build_single_contact_sheet(specs, False, processed, palette_sizes)
    comparison_sheet = build_comparison_sheet(specs, processed, medium_images, small_images)
    source_sheet.save(SHEETS_DIR / "source_masters_contact_sheet.png", optimize=True)
    final_sheet.save(SHEETS_DIR / "final_runtime_flags_contact_sheet.png", optimize=True)
    comparison_sheet.save(SHEETS_DIR / "source_vs_final_contact_sheet.png", optimize=True)
    build_manifest(
        specs,
        source_dimensions,
        palette_sizes,
        quantize_methods,
        hashes,
        evidence,
    )
    build_validation(
        specs,
        processed,
        medium_images,
        small_images,
        palette_sizes,
        quantize_methods,
        evidence,
    )

    print(json.dumps({
        "sources": len(stems),
        "processed": len(processed),
        "runtime_tga": len(stems) * 3,
        "palette_min": min(palette_sizes.values()),
        "palette_max": max(palette_sizes.values()),
        "contact_sheets": 3,
        "validation": "passed",
    }))


if __name__ == "__main__":
    main()
