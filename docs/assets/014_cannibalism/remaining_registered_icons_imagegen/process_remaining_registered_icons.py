from __future__ import annotations

import argparse
import csv
import hashlib
import math
import os
import re
import shutil
import struct
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


PACKAGE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
SOURCE = PACKAGE / "source_png"
ALPHA = PACKAGE / "alpha_png"
PROCESSED = PACKAGE / "processed_png"
DDS_PACKAGE = PACKAGE / "dds"
CONTACT = PACKAGE / "contact_sheets"
VALIDATION = PACKAGE / "validation" / "remaining_registered_icons_validation.tsv"
VALIDATION_SUMMARY = PACKAGE / "validation" / "validation_summary.md"
CONVERTER = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
CHROMA_HELPER = Path(
    "C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py"
)
APPROVED_TEXCONV = Path(
    "C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe"
)
APPROVED_TEXCONV_SHA256 = (
    "dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06"
)
GFX_FILE = ROOT / "interface" / "014_cannibalism.gfx"
LIVE_DECISIONS = ROOT / "gfx" / "interface" / "decisions" / "014_cannibalism"
LIVE_IDEAS = ROOT / "gfx" / "interface" / "ideas" / "014_cannibalism"


CATEGORY_PANELS = [
    "cannibalism_international_response_category_panel",
    "cannibalism_reconstruction_category_panel",
    "cannibalism_unified_command_category_panel",
    "cannibalism_unified_global_campaign_category_panel",
    "cannibalism_unified_larder_category_panel",
    "cannibalism_unified_war_machine_category_panel",
    "cannibalism_unified_world_end_category_panel",
    "cannibalism_wendigo_command_category_panel",
    "cannibalism_wendigo_counterwar_category_panel",
]
CATEGORY_ICONS = [
    "decision_category_cannibalism_international_response",
    "decision_category_cannibalism_reconstruction",
    "decision_category_cannibalism_unified_command",
    "decision_category_cannibalism_unified_global_campaign",
    "decision_category_cannibalism_unified_larder",
    "decision_category_cannibalism_unified_war_machine",
    "decision_category_cannibalism_unified_world_end",
    "decision_category_cannibalism_wendigo_command",
    "decision_category_cannibalism_wendigo_counterwar",
]
DECISIONS = [
    "decision_cannibalism_accelerate_transformation_countdown",
    "decision_cannibalism_assault_transformation_anchor",
    "decision_cannibalism_blockade_island_host",
    "decision_cannibalism_break_wendigo_recruitment_site",
    "decision_cannibalism_complete_memorial_site",
    "decision_cannibalism_consume_transformation_anchor_population",
    "decision_cannibalism_designate_transformation_anchor",
    "decision_cannibalism_disrupt_transformation_logistics",
    "decision_cannibalism_end_terror_exploitation",
    "decision_cannibalism_feed_selected_prisoners",
    "decision_cannibalism_fortify_transformation_anchor",
    "decision_cannibalism_freeze_supply_corridor",
    "decision_cannibalism_identify_and_bury_victims",
    "decision_cannibalism_identify_transformation_anchor",
    "decision_cannibalism_interdict_convergence_host",
    "decision_cannibalism_joint_suppression_operation",
    "decision_cannibalism_land_against_island_host",
    "decision_cannibalism_maintain_inspection_compact",
    "decision_cannibalism_ratify_inspection_compact",
    "decision_cannibalism_rebuild_feeding_state_institutions",
    "decision_cannibalism_rescue_island_survivors",
    "decision_cannibalism_stabilize_transformation_countdown",
    "decision_cannibalism_train_additional_wendigo_packs",
]
IDEAS = [
    "idea_cannibalism_authority_without_rivals",
    "idea_cannibalism_battlefield_continental_larder",
    "idea_cannibalism_confederation_under_one_name",
    "idea_cannibalism_council_of_retained_hosts",
    "idea_cannibalism_dominion_of_chains",
    "idea_cannibalism_harvest_follows_victory",
    "idea_cannibalism_island_host_blockade",
    "idea_cannibalism_island_host_landing_pressure",
    "idea_cannibalism_larder_that_moves",
    "idea_cannibalism_managed_continental_larder",
    "idea_cannibalism_managed_continental_reserve",
    "idea_cannibalism_many_jaws",
    "idea_cannibalism_mobile_continental_larder",
    "idea_cannibalism_one_command",
    "idea_cannibalism_rapid_continental_larder",
    "idea_cannibalism_retained_lieutenants",
    "idea_cannibalism_ritual_administration",
    "idea_cannibalism_rivals_in_chains",
    "idea_cannibalism_short_horizon_continent",
    "idea_cannibalism_single_operational_will",
    "idea_cannibalism_state_of_the_last_table",
    "idea_cannibalism_unified_command_burden",
    "idea_cannibalism_warlords_broken",
    "idea_cannibalism_wendigo_broken_anchor_recovery",
    "idea_cannibalism_wendigo_frozen_supply_corridor",
    "idea_cannibalism_wendigo_frozen_supply_disruption",
    "idea_cannibalism_wendigo_transformation_anchor",
]

TRANSPARENT = CATEGORY_ICONS + DECISIONS + IDEAS
ORDERED = CATEGORY_PANELS + CATEGORY_ICONS + DECISIONS + IDEAS


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_approved_texconv() -> None:
    if not APPROVED_TEXCONV.exists():
        raise FileNotFoundError(f"Approved texconv is missing: {APPROVED_TEXCONV}")
    digest = sha256_file(APPROVED_TEXCONV)
    if digest != APPROVED_TEXCONV_SHA256:
        raise RuntimeError(
            f"Approved texconv hash mismatch: {digest}, expected {APPROVED_TEXCONV_SHA256}"
        )


def remove_chroma(name: str, refresh: bool) -> Path:
    source = SOURCE / f"{name}_source.png"
    output = ALPHA / f"{name}_alpha.png"
    if not source.exists():
        raise FileNotFoundError(source)
    if output.exists() and not refresh:
        return output
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "python",
        str(CHROMA_HELPER),
        "--input",
        str(source),
        "--out",
        str(output),
        "--auto-key",
        "border",
        "--soft-matte",
        "--transparent-threshold",
        "12",
        "--opaque-threshold",
        "220",
        "--despill",
    ]
    if refresh:
        command.append("--force")
    subprocess.run(command, check=True)
    return output


def trim_alpha(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    alpha = rgba.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()
    if bbox is None:
        raise RuntimeError("Imagegen source has no visible pixels after chroma-key removal")
    return rgba.crop(bbox)


def fit_alpha(
    source: Path,
    size: tuple[int, int],
    padding: int,
    outline_width: float,
    shadow_offset: float,
) -> Image.Image:
    scale = 4
    target_w, target_h = size
    image = trim_alpha(Image.open(source))
    maximum = (
        max(1, (target_w - padding * 2 - math.ceil(outline_width * 2)) * scale),
        max(1, (target_h - padding * 2 - math.ceil(outline_width * 2)) * scale),
    )
    ratio = min(maximum[0] / image.width, maximum[1] / image.height)
    resized = image.resize(
        (max(1, round(image.width * ratio)), max(1, round(image.height * ratio))),
        Image.Resampling.LANCZOS,
    )
    high_size = (target_w * scale, target_h * scale)
    x = (high_size[0] - resized.width) // 2
    y = (high_size[1] - resized.height) // 2
    subject_alpha = Image.new("L", high_size, 0)
    subject_alpha.paste(resized.getchannel("A"), (x, y))

    shadow_alpha = subject_alpha.filter(ImageFilter.GaussianBlur(radius=2.0 * scale))
    shadow_alpha = shadow_alpha.point(lambda value: round(value * 0.42))
    shifted_shadow = Image.new("L", high_size, 0)
    shifted_shadow.paste(
        shadow_alpha,
        (round(shadow_offset * scale), round(shadow_offset * scale)),
    )
    shadow = Image.new("RGBA", high_size, (0, 0, 0, 0))
    shadow.putalpha(shifted_shadow)

    outline_pixels = max(1, round(outline_width * scale))
    outline_alpha = subject_alpha.filter(ImageFilter.MaxFilter(outline_pixels * 2 + 1))
    outline_alpha = outline_alpha.point(lambda value: round(value * 0.9))
    outline = Image.new("RGBA", high_size, (21, 16, 13, 255))
    outline.putalpha(outline_alpha)

    subject = Image.new("RGBA", high_size, (0, 0, 0, 0))
    subject.alpha_composite(resized, (x, y))
    canvas = Image.alpha_composite(shadow, outline)
    canvas = Image.alpha_composite(canvas, subject)
    final = canvas.resize(size, Image.Resampling.LANCZOS)
    final_alpha = final.getchannel("A")
    alpha_draw = ImageDraw.Draw(final_alpha)
    alpha_draw.rectangle((0, 0, size[0] - 1, 0), fill=0)
    alpha_draw.rectangle((0, size[1] - 1, size[0] - 1, size[1] - 1), fill=0)
    alpha_draw.rectangle((0, 0, 0, size[1] - 1), fill=0)
    alpha_draw.rectangle((size[0] - 1, 0, size[0] - 1, size[1] - 1), fill=0)
    final.putalpha(final_alpha)
    return final


def cover_opaque(source: Path, size: tuple[int, int]) -> Image.Image:
    image = Image.open(source).convert("RGB")
    return ImageOps.fit(
        image,
        size,
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    ).convert("RGBA")


def expected_metadata(name: str) -> tuple[str, tuple[int, int], Path]:
    if name in CATEGORY_PANELS:
        return "decision category panel", (114, 101), LIVE_DECISIONS / f"{name}.dds"
    if name in CATEGORY_ICONS:
        return "decision category icon", (32, 32), LIVE_DECISIONS / f"{name}.dds"
    if name in DECISIONS:
        return "decision icon", (32, 32), LIVE_DECISIONS / f"{name}.dds"
    if name in IDEAS:
        return "idea/dynamic-modifier icon", (64, 64), LIVE_IDEAS / f"{name}.dds"
    raise KeyError(name)


def convert_to_dds(png: Path, package_dds: Path, live_dds: Path, size: tuple[int, int]) -> None:
    package_dds.parent.mkdir(parents=True, exist_ok=True)
    live_dds.parent.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["TEXCONV_PATH"] = str(APPROVED_TEXCONV)
    env.pop("TEXCONV_EXE", None)
    env.pop("TEXCONV_DOCKER_IMAGE", None)
    subprocess.run(
        [
            "python",
            str(CONVERTER),
            "--input",
            str(png),
            "--output",
            str(package_dds),
            "--width",
            str(size[0]),
            "--height",
            str(size[1]),
        ],
        check=True,
        env=env,
    )
    shutil.copy2(package_dds, live_dds)


def dds_header(path: Path) -> tuple[int, int, int, tuple[int, int, int, int]]:
    data = path.read_bytes()[:128]
    if len(data) != 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS magic/header: {path}")
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mip_count = struct.unpack_from("<I", data, 28)[0]
    masks = tuple(struct.unpack_from("<I", data, offset)[0] for offset in (92, 96, 100, 104))
    return width, height, mip_count, masks


def decode_bgra_dds(path: Path) -> Image.Image:
    data = path.read_bytes()
    width, height, _, _ = dds_header(path)
    expected = width * height * 4
    payload = data[128:]
    if len(payload) != expected:
        raise RuntimeError(
            f"Unexpected uncompressed DDS payload for {path}: {len(payload)}, expected {expected}"
        )
    return Image.frombytes("RGBA", (width, height), payload, "raw", "BGRA")


def checker(size: tuple[int, int], tile: int = 8) -> Image.Image:
    image = Image.new("RGBA", size, (67, 67, 67, 255))
    draw = ImageDraw.Draw(image)
    colors = ((72, 72, 72, 255), (116, 116, 116, 255))
    for y in range(0, size[1], tile):
        for x in range(0, size[0], tile):
            draw.rectangle(
                (x, y, min(x + tile - 1, size[0] - 1), min(y + tile - 1, size[1] - 1)),
                fill=colors[((x // tile) + (y // tile)) % 2],
            )
    return image


def font(size: int) -> ImageFont.ImageFont:
    for path in (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/arial.ttf")):
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def make_source_contact(
    entries: list[tuple[str, Image.Image]], output: Path, columns: int
) -> None:
    cell_w, cell_h = 270, 220
    preview_size = (174, 174)
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    for index, (name, image) in enumerate(entries):
        col, row = index % columns, index // columns
        x0, y0 = col * cell_w, row * cell_h
        draw.rectangle(
            (x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4),
            outline=(88, 92, 98),
            width=1,
        )
        preview = ImageOps.contain(
            image.convert("RGB"), preview_size, Image.Resampling.LANCZOS
        )
        plate = Image.new("RGB", preview_size, (48, 50, 54))
        plate.paste(
            preview,
            (
                (preview_size[0] - preview.width) // 2,
                (preview_size[1] - preview.height) // 2,
            ),
        )
        sheet.paste(plate, (x0 + (cell_w - preview_size[0]) // 2, y0 + 8))
        y = y0 + 187
        for line in textwrap.wrap(name, width=34)[:2]:
            bbox = draw.textbbox((0, 0), line, font=label_font)
            draw.text(
                (x0 + (cell_w - (bbox[2] - bbox[0])) // 2, y),
                line,
                font=label_font,
                fill=(235, 235, 235),
            )
            y += 15
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, optimize=True)


def make_target_contact(
    entries: list[tuple[str, Image.Image]], output: Path, columns: int
) -> None:
    cell_w, cell_h = 330, 230
    native_plate_size = (132, 150)
    large_plate_size = (164, 150)
    rows = math.ceil(len(entries) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), (28, 30, 33))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    small_font = font(11)
    for index, (name, image) in enumerate(entries):
        col, row = index % columns, index // columns
        x0, y0 = col * cell_w, row * cell_h
        draw.rectangle(
            (x0 + 3, y0 + 3, x0 + cell_w - 4, y0 + cell_h - 4),
            outline=(88, 92, 98),
            width=1,
        )
        rgba = image.convert("RGBA")
        native = checker(native_plate_size, 8)
        native.alpha_composite(
            rgba,
            (
                (native_plate_size[0] - rgba.width) // 2,
                (native_plate_size[1] - rgba.height) // 2,
            ),
        )
        sheet.paste(native.convert("RGB"), (x0 + 10, y0 + 20))

        scale = min(
            4,
            max(
                1,
                min(
                    large_plate_size[0] // rgba.width,
                    large_plate_size[1] // rgba.height,
                ),
            ),
        )
        enlarged = rgba.resize(
            (rgba.width * scale, rgba.height * scale), Image.Resampling.NEAREST
        )
        large = checker(large_plate_size, 12)
        large.alpha_composite(
            enlarged,
            (
                (large_plate_size[0] - enlarged.width) // 2,
                (large_plate_size[1] - enlarged.height) // 2,
            ),
        )
        sheet.paste(large.convert("RGB"), (x0 + 154, y0 + 20))
        draw.text(
            (x0 + 48, y0 + 7), "native", font=small_font, fill=(190, 194, 200)
        )
        draw.text(
            (x0 + 215, y0 + 7), f"{scale}x", font=small_font, fill=(190, 194, 200)
        )
        y = y0 + 177
        for line in textwrap.wrap(name, width=40)[:3]:
            bbox = draw.textbbox((0, 0), line, font=label_font)
            draw.text(
                (x0 + (cell_w - (bbox[2] - bbox[0])) // 2, y),
                line,
                font=label_font,
                fill=(235, 235, 235),
            )
            y += 15
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, optimize=True)


def visible_key_green(image: Image.Image) -> int:
    rgba = image.convert("RGBA")
    return sum(
        1
        for red, green, blue, alpha in rgba.getdata()
        if alpha > 10 and green > 190 and green > red * 1.55 and green > blue * 1.55
    )


def exact_gfx_mapping(name: str, live_dds: Path) -> tuple[str, str]:
    sprite = f"GFX_{name}"
    relative = live_dds.relative_to(ROOT).as_posix()
    text = GFX_FILE.read_text(encoding="utf-8-sig")
    pattern = re.compile(
        r'spriteType\s*=\s*\{\s*name\s*=\s*"' + re.escape(sprite)
        + r'"\s*texturefile\s*=\s*"' + re.escape(relative) + r'"\s*\}'
    )
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one GFX mapping for {sprite} -> {relative}; "
            f"found {len(matches)}"
        )
    return sprite, relative


def write_contacts(
    processed: dict[str, Image.Image], decoded: dict[str, Image.Image]
) -> None:
    families = [
        ("category_panels", CATEGORY_PANELS, 3),
        ("category_icons", CATEGORY_ICONS, 3),
        ("decision_icons", DECISIONS, 4),
        ("idea_icons", IDEAS, 4),
    ]
    for family, names, columns in families:
        make_source_contact(
            [
                (
                    name,
                    Image.open(SOURCE / f"{name}_source.png").convert("RGBA"),
                )
                for name in names
            ],
            CONTACT / f"{family}_sources_contact_sheet.png",
            columns,
        )
        make_target_contact(
            [(name, processed[name]) for name in names],
            CONTACT / f"{family}_processed_checker_contact_sheet.png",
            columns,
        )
        make_target_contact(
            [(name, decoded[name]) for name in names],
            CONTACT / f"{family}_decoded_dds_checker_contact_sheet.png",
            columns,
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh-alpha",
        action="store_true",
        help="Regenerate every chroma-key alpha intermediate.",
    )
    args = parser.parse_args()

    validate_approved_texconv()
    for directory in (
        ALPHA,
        PROCESSED,
        DDS_PACKAGE,
        CONTACT,
        LIVE_DECISIONS,
        LIVE_IDEAS,
        VALIDATION.parent,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    source_files = sorted(SOURCE.glob("*_source.png"), key=lambda path: path.name)
    expected_source_files = sorted(
        (SOURCE / f"{name}_source.png" for name in ORDERED),
        key=lambda path: path.name,
    )
    if source_files != expected_source_files:
        missing = sorted(
            str(path) for path in set(expected_source_files) - set(source_files)
        )
        extra = sorted(str(path) for path in set(source_files) - set(expected_source_files))
        raise RuntimeError(f"Source ledger mismatch. Missing={missing}; extra={extra}")

    processed: dict[str, Image.Image] = {}
    for name in CATEGORY_PANELS:
        processed[name] = cover_opaque(SOURCE / f"{name}_source.png", (114, 101))
    for name in CATEGORY_ICONS + DECISIONS:
        alpha_source = remove_chroma(name, args.refresh_alpha)
        processed[name] = fit_alpha(alpha_source, (32, 32), 2, 0.85, 0.75)
    for name in IDEAS:
        alpha_source = remove_chroma(name, args.refresh_alpha)
        processed[name] = fit_alpha(alpha_source, (64, 64), 3, 1.0, 1.0)

    for name in ORDERED:
        _, size, live_dds = expected_metadata(name)
        png = PROCESSED / f"{name}.png"
        processed[name].save(png, optimize=True)
        convert_to_dds(png, DDS_PACKAGE / f"{name}.dds", live_dds, size)

    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    normalized_hashes: dict[str, str] = {}
    source_hashes: dict[str, str] = {}
    decoded: dict[str, Image.Image] = {}
    rows: list[list[str]] = []
    for name in ORDERED:
        asset_type, expected_size, live_dds = expected_metadata(name)
        source = SOURCE / f"{name}_source.png"
        png = PROCESSED / f"{name}.png"
        package_dds = DDS_PACKAGE / f"{name}.dds"
        image = Image.open(png).convert("RGBA")
        if image.size != expected_size:
            raise RuntimeError(
                f"Wrong processed size for {name}: {image.size}, expected {expected_size}"
            )

        source_digest = sha256_file(source)
        if source_digest in source_hashes:
            raise RuntimeError(
                f"Byte-identical generated source: {name} duplicates "
                f"{source_hashes[source_digest]}"
            )
        source_hashes[source_digest] = name

        alpha = image.getchannel("A")
        alpha_min, alpha_max = alpha.getextrema()
        transparent = sum(1 for value in alpha.getdata() if value == 0)
        partial = sum(1 for value in alpha.getdata() if 0 < value < 255)
        corner_alpha = tuple(
            alpha.getpixel(point)
            for point in (
                (0, 0),
                (expected_size[0] - 1, 0),
                (0, expected_size[1] - 1),
                (expected_size[0] - 1, expected_size[1] - 1),
            )
        )
        if name not in CATEGORY_PANELS and alpha_min != 0:
            raise RuntimeError(f"Transparent icon lost transparent pixels: {name}")
        if name not in CATEGORY_PANELS and alpha_max != 255:
            raise RuntimeError(f"Transparent icon has no fully opaque pixels: {name}")
        if name not in CATEGORY_PANELS and corner_alpha != (0, 0, 0, 0):
            raise RuntimeError(
                f"Transparent icon has non-transparent corners: {name} {corner_alpha}"
            )
        if name in CATEGORY_PANELS and (alpha_min, alpha_max) != (255, 255):
            raise RuntimeError(f"Category panel should remain opaque: {name}")
        key_green = visible_key_green(image)
        if key_green:
            raise RuntimeError(
                f"Visible chroma-key green remains in {name}: {key_green} pixels"
            )
        normalized_digest = hashlib.sha256(image.tobytes()).hexdigest()
        if normalized_digest in normalized_hashes:
            raise RuntimeError(
                f"Duplicate normalized artwork: {name} duplicates "
                f"{normalized_hashes[normalized_digest]}"
            )
        normalized_hashes[normalized_digest] = name

        width, height, mip_count, masks = dds_header(live_dds)
        if (width, height) != expected_size:
            raise RuntimeError(
                f"Wrong DDS size for {name}: {(width, height)}, expected {expected_size}"
            )
        if mip_count not in (0, 1):
            raise RuntimeError(
                f"DDS should have one image level: {name} reports {mip_count}"
            )
        if masks != expected_masks:
            raise RuntimeError(f"DDS is not uncompressed BGRA8 for {name}: {masks}")

        package_hash = sha256_file(package_dds)
        runtime_hash = sha256_file(live_dds)
        if package_hash != runtime_hash:
            raise RuntimeError(f"Package/runtime DDS hash mismatch: {name}")

        decoded_image = decode_bgra_dds(live_dds)
        if decoded_image.tobytes() != image.tobytes():
            raise RuntimeError(f"Decoded DDS pixels do not match processed PNG: {name}")
        decoded[name] = decoded_image
        sprite, gfx_path = exact_gfx_mapping(name, live_dds)

        rows.append(
            [
                name,
                asset_type,
                f"{expected_size[0]}x{expected_size[1]}",
                str(alpha_min),
                str(alpha_max),
                str(transparent),
                str(partial),
                "/".join(str(value) for value in corner_alpha),
                str(key_green),
                source_digest,
                normalized_digest,
                package_hash,
                runtime_hash,
                f"{width}x{height}",
                str(mip_count),
                "0x00ff0000/0x0000ff00/0x000000ff/0xff000000",
                sprite,
                gfx_path,
                "complete",
            ]
        )

    write_contacts(processed, decoded)

    with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(
            [
                "asset",
                "asset_type",
                "processed_dimensions",
                "alpha_min",
                "alpha_max",
                "transparent_pixels",
                "partial_alpha_pixels",
                "corner_alpha_tl_tr_bl_br",
                "visible_key_green_pixels",
                "source_sha256",
                "processed_rgba_sha256",
                "package_dds_sha256",
                "runtime_dds_sha256",
                "dds_dimensions",
                "dds_mip_count",
                "dds_channel_masks",
                "registered_sprite",
                "registered_texture_path",
                "status",
            ]
        )
        writer.writerows(rows)

    VALIDATION_SUMMARY.write_text(
        "\n".join(
            [
                "# Event 014 Remaining Registered Icon Validation",
                "",
                f"- Ledger coverage: {len(rows)}/68.",
                "- Family coverage: 9 opaque category panels, 9 transparent "
                "category icons, 23 transparent decision icons, and 27 transparent "
                "idea/dynamic-modifier icons.",
                "- Every processed PNG matches the exact target dimensions and "
                "decodes pixel-identically from its runtime DDS.",
                "- Transparent icons have true alpha and zero-alpha corners; "
                "category panels are fully opaque.",
                "- No visible chroma-key green remains.",
                "- Generated source hashes and normalized processed RGBA hashes "
                "are unique across all 68 assets.",
                "- Every package DDS is byte-identical to its runtime DDS.",
                "- Every DDS is an uncompressed one-image-level 32-bit BGRA "
                "texture with the expected channel masks.",
                "- Every runtime path has exactly one matching sprite registration "
                "in interface/014_cannibalism.gfx.",
                f"- DDS backend: Microsoft DirectXTex texconv May 2026 at "
                f"{APPROVED_TEXCONV}.",
                f"- Approved backend SHA-256: "
                f"{APPROVED_TEXCONV_SHA256.upper()}.",
                "- Detailed per-asset evidence: "
                "remaining_registered_icons_validation.tsv.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"processed and validated {len(rows)} remaining registered Event 014 assets")


if __name__ == "__main__":
    main()
