"""Build the Event 014 flag package and runtime TGA exports.

Generated source masters remain untouched. Each runtime master is center-cropped to
the HOI4 82:52 aspect, resized, and quantized without dithering to at most four
fully opaque colors. Medium and small flags are derived from that flattened master.
TGA files are written directly so the bottom-left origin and 32-bit uncompressed
layout are explicit rather than delegated to an encoder default.
"""

from __future__ import annotations

import hashlib
import json
import math
import struct
from collections import Counter, deque
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = PACKAGE / "source_png"
PROCESSED_DIR = PACKAGE / "processed_png"
PROMPTS_DIR = PACKAGE / "prompts"
SHEETS_DIR = PACKAGE / "contact_sheets"
SPECS_PATH = PROMPTS_DIR / "prompt_specs.json"

NORMAL_DIR = ROOT / "gfx" / "flags"
MEDIUM_DIR = NORMAL_DIR / "medium"
SMALL_DIR = NORMAL_DIR / "small"

SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
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
    method: Image.Quantize = Image.Quantize.MEDIANCUT,
) -> tuple[Image.Image, list[tuple[int, int, int]]]:
    cropped = center_crop_to_ratio(source.convert("RGB"), SIZES["normal"])
    resized = cropped.resize(SIZES["normal"], Image.Resampling.LANCZOS)
    quantized = resized.quantize(
        colors=4,
        method=method,
        dither=Image.Dither.NONE,
    )
    flattened = quantized.convert("RGB")
    counts = flattened.getcolors(maxcolors=82 * 52)
    if not counts:
        raise RuntimeError("Could not enumerate flattened palette")
    palette = [color for _, color in sorted(counts, reverse=True)]
    if not 2 <= len(palette) <= 4:
        raise RuntimeError(f"Expected 2-4 colors, got {len(palette)}")
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


def remove_small_color_islands(
    image: Image.Image,
    color: tuple[int, int, int],
    maximum_size: int,
) -> Image.Image:
    """Replace isolated quantization islands with their dominant neighbor color."""
    output = image.copy().convert("RGB")
    pixels = output.load()
    seen: set[tuple[int, int]] = set()
    neighbors = (
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1),
    )
    components: list[list[tuple[int, int]]] = []
    for y in range(output.height):
        for x in range(output.width):
            if (x, y) in seen or pixels[x, y] != color:
                continue
            queue = deque([(x, y)])
            seen.add((x, y))
            component: list[tuple[int, int]] = []
            while queue:
                current_x, current_y = queue.popleft()
                component.append((current_x, current_y))
                for delta_x, delta_y in neighbors:
                    adjacent = (current_x + delta_x, current_y + delta_y)
                    if (
                        0 <= adjacent[0] < output.width
                        and 0 <= adjacent[1] < output.height
                        and adjacent not in seen
                        and pixels[adjacent[0], adjacent[1]] == color
                    ):
                        seen.add(adjacent)
                        queue.append(adjacent)
            if len(component) <= maximum_size:
                components.append(component)

    for component in components:
        component_set = set(component)
        adjacent_colors: Counter[tuple[int, int, int]] = Counter()
        for x, y in component:
            for delta_x, delta_y in neighbors:
                adjacent = (x + delta_x, y + delta_y)
                if (
                    0 <= adjacent[0] < output.width
                    and 0 <= adjacent[1] < output.height
                    and adjacent not in component_set
                    and pixels[adjacent[0], adjacent[1]] != color
                ):
                    adjacent_colors[pixels[adjacent[0], adjacent[1]]] += 1
        if adjacent_colors:
            replacement = sorted(
                adjacent_colors.items(),
                key=lambda item: (-item[1], item[0]),
            )[0][0]
            for x, y in component:
                pixels[x, y] = replacement
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
    title = "EVENT 014 — IMAGEGEN SOURCE MASTERS" if source else "EVENT 014 — FINAL RUNTIME FLAGS (2–4 FLAT COLORS)"
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
        "EVENT 014 — IMAGEGEN SOURCE VS FINAL FOUR-COLOR RUNTIME MASTER",
        title_font,
        "#f1ead8",
    )
    art_size = (164, 104)
    for index, spec in enumerate(specs):
        stem = spec["stem"]
        col = index % columns
        row = index // columns
        x = col * tile_width
        y = top_margin + row * tile_height
        draw_centered(draw, (x + tile_width // 2, y + 1), f"{stem}.tga", label_font, "#f1ead8")
        left_x = x + 40
        right_x = x + 226
        labels_y = y + 22
        draw_centered(draw, (left_x + art_size[0] // 2, labels_y), "SOURCE", meta_font, "#aeb4be")
        draw_centered(draw, (right_x + art_size[0] // 2, labels_y), "FINAL 2–4 COLOR", meta_font, "#aeb4be")
        art_y = y + 39
        with Image.open(SOURCE_DIR / f"{stem}.png") as image:
            source_art = crop_preview(image, art_size)
        final_art = processed[stem].resize(art_size, Image.Resampling.NEAREST)
        sheet.paste(source_art, (left_x, art_y))
        sheet.paste(final_art, (right_x, art_y))
    return sheet


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_manifest(
    specs: list[dict[str, str]],
    source_dimensions: dict[str, tuple[int, int]],
    palette_sizes: dict[str, int],
    hashes: dict[str, str],
) -> None:
    lines = [
        "# Event 014 Cannibalism Flag Refresh Manifest",
        "",
        "Canonical provenance and runtime handoff for all 65 live Event 014 flag designs. Each flag was generated independently with the built-in image generator. Source masters are retained verbatim; runtime masters are centered to the HOI4 82:52 aspect and flattened without dithering to two through four opaque colors.",
        "",
        "- Event: `014_cannibalism`",
        "- Asset type: `flag`",
        "- Source mode: `imagegen`",
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
        lines.extend(
            [
                f"## {stem}",
                "",
                "- Event: `014_cannibalism`",
                "- Type: `flag`",
                f"- Intended use: {spec['family_role']}",
                "- Source mode: `imagegen`",
                f"- Prompt file: `{relative(prompt_path)}`",
                f"- Source path: `{relative(source_path)}`",
                f"- Processed path: `{relative(processed_path)}`",
                f"- Final normal TGA: `{relative(normal_path)}`",
                f"- Final medium TGA: `{relative(medium_path)}`",
                f"- Final small TGA: `{relative(small_path)}`",
                f"- Dimensions: source `{source_width}x{source_height}`; processed/normal `82x52`; medium `41x26`; small `10x7`",
                f"- Final palette: `{palette_sizes[stem]}` opaque flat colors",
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
    source_dimensions: dict[str, tuple[int, int]] = {}
    palette_sizes: dict[str, int] = {}
    hashes: dict[str, str] = {}

    for stem in stems:
        source_path = SOURCE_DIR / f"{stem}.png"
        with Image.open(source_path) as source:
            source_dimensions[stem] = source.size
            method = (
                Image.Quantize.MAXCOVERAGE
                if stem == "CBL_CENTRAL_COMMAND_communism"
                else Image.Quantize.MEDIANCUT
            )
            master, palette = flatten_master(source, method=method)
        if stem == "CBL_CENTRAL_COMMAND_communism":
            master = remove_small_color_islands(master, palette[0], maximum_size=4)
        elif stem == "CBG_democratic":
            master = remove_small_color_islands(master, palette[2], maximum_size=4)
        processed[stem] = master
        palette_sizes[stem] = len(palette)
        processed_path = PROCESSED_DIR / f"{stem}.png"
        master.save(processed_path, format="PNG", optimize=True)
        hashes[stem] = hashlib.sha256(processed_path.read_bytes()).hexdigest()

        medium = resize_to_palette(master, SIZES["medium"], palette)
        small = resize_to_palette(master, SIZES["small"], palette)
        write_bottom_origin_tga(master, NORMAL_DIR / f"{stem}.tga")
        write_bottom_origin_tga(medium, MEDIUM_DIR / f"{stem}.tga")
        write_bottom_origin_tga(small, SMALL_DIR / f"{stem}.tga")

    source_sheet = build_single_contact_sheet(specs, True, processed, palette_sizes)
    final_sheet = build_single_contact_sheet(specs, False, processed, palette_sizes)
    comparison_sheet = build_comparison_sheet(specs, processed)
    source_sheet.save(SHEETS_DIR / "source_masters_contact_sheet.png", optimize=True)
    final_sheet.save(SHEETS_DIR / "final_runtime_flags_contact_sheet.png", optimize=True)
    comparison_sheet.save(SHEETS_DIR / "source_vs_final_contact_sheet.png", optimize=True)
    build_manifest(specs, source_dimensions, palette_sizes, hashes)

    print(json.dumps({
        "sources": len(stems),
        "processed": len(processed),
        "runtime_tga": len(stems) * 3,
        "palette_min": min(palette_sizes.values()),
        "palette_max": max(palette_sizes.values()),
        "contact_sheets": 3,
    }))


if __name__ == "__main__":
    main()
