#!/usr/bin/env python3
"""Build Event 015 Ledger Value and Calling icons from the frozen ImageGen atlas.

This processor is intentionally mechanical. It slices the accepted 5x2 source
atlas, delegates magenta-key removal to the installed ImageGen skill helper,
alpha-fits the preserved artwork to its documented native GUI canvas, writes
legacy one-level BGRA DDS files, decodes them for pixel verification, and emits
machine-readable provenance and validation records.

It does not draw, trace, simplify, recolour, or reconstruct visible icon art.
Primitive drawing is limited to checkerboards and labels in review-only contact
sheets.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
import re
import struct
import subprocess
import sys
from typing import Any, Iterable

from PIL import Image, ImageDraw, __version__ as PILLOW_VERSION


PROCESSING_DATE = "2026-07-16"
ATLAS_RELATIVE = Path(
    "docs/assets/015_utopia_manifesto/source_png/identity_gui/"
    "utopia_ledger_value_calling_icons_imagegen_atlas.png"
)
EXPECTED_ATLAS_SHA256 = (
    "7a1704f1c6d720ff72b9cdc3715101361bb8b836033607d0ff244dbb31c7d440"
)
EXPECTED_ATLAS_SIZE = (1774, 887)
GRID_COLUMNS = 5
GRID_ROWS = 2

PACKAGE_RELATIVE = Path(
    "docs/assets/015_utopia_manifesto/value_calling_icon_repair_2026_07_16"
)
RUNTIME_RELATIVE = Path("gfx/interface/015_utopia_manifesto/ledger")

DDSD_CAPS = 0x1
DDSD_HEIGHT = 0x2
DDSD_WIDTH = 0x4
DDSD_PITCH = 0x8
DDSD_PIXELFORMAT = 0x1000
DDPF_ALPHAPIXELS = 0x1
DDPF_RGB = 0x40
DDSCAPS_TEXTURE = 0x1000


@dataclass(frozen=True)
class Asset:
    asset_id: str
    display_name: str
    asset_type: str
    row: int
    column: int
    target_size: int
    sprite_name: str
    intended_use: str


ASSETS = (
    Asset(
        "utopia_ledger_value_need",
        "Need",
        "value_icon",
        0,
        0,
        32,
        "GFX_utopia_ledger_value_need",
        "Compact Commonwealth Ledger Need value emblem",
    ),
    Asset(
        "utopia_ledger_value_plenty",
        "Plenty",
        "value_icon",
        0,
        1,
        32,
        "GFX_utopia_ledger_value_plenty",
        "Compact Commonwealth Ledger Plenty value emblem",
    ),
    Asset(
        "utopia_ledger_value_concord",
        "Concord",
        "value_icon",
        0,
        2,
        32,
        "GFX_utopia_ledger_value_concord",
        "Compact Commonwealth Ledger Concord value emblem",
    ),
    Asset(
        "utopia_ledger_value_balance",
        "Choice / Assignment",
        "value_icon",
        0,
        3,
        32,
        "GFX_utopia_ledger_value_balance",
        "Morally neutral compact Choice-versus-Assignment value emblem",
    ),
    Asset(
        "utopia_ledger_calling_provisioning",
        "Provisioning / Agriculture",
        "calling_icon",
        0,
        4,
        48,
        "GFX_utopia_ledger_calling_provisioning",
        "Calling selector for Provisioning and Agriculture",
    ),
    Asset(
        "utopia_ledger_calling_workshops",
        "Workshops / Arsenal",
        "calling_icon",
        1,
        0,
        48,
        "GFX_utopia_ledger_calling_workshops",
        "Calling selector for Workshops and Arsenal",
    ),
    Asset(
        "utopia_ledger_calling_civic_works",
        "Civic Works / Transport",
        "calling_icon",
        1,
        1,
        48,
        "GFX_utopia_ledger_calling_civic_works",
        "Calling selector for Civic Works and Transport",
    ),
    Asset(
        "utopia_ledger_calling_learning_and_care",
        "Learning / Care",
        "calling_icon",
        1,
        2,
        48,
        "GFX_utopia_ledger_calling_learning_and_care",
        "Calling selector for Learning and Care",
    ),
    Asset(
        "utopia_ledger_calling_maritime_and_settlement",
        "Maritime / Settlement",
        "calling_icon",
        1,
        3,
        48,
        "GFX_utopia_ledger_calling_maritime_and_settlement",
        "Calling selector for Maritime and Settlement",
    ),
    Asset(
        "utopia_ledger_calling_defense_and_watches",
        "Defense / Watches",
        "calling_icon",
        1,
        4,
        48,
        "GFX_utopia_ledger_calling_defense_and_watches",
        "Calling selector for Defense and Watches",
    ),
)


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    default_workspace = script_path.parents[5]
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    default_helper = (
        codex_home
        / "skills"
        / ".system"
        / "imagegen"
        / "scripts"
        / "remove_chroma_key.py"
    )

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace",
        type=Path,
        default=default_workspace,
        help="Chaos Redux repository root.",
    )
    parser.add_argument(
        "--chroma-helper",
        type=Path,
        default=default_helper,
        help="Installed imagegen remove_chroma_key.py helper.",
    )
    return parser.parse_args()


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def save_png(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, format="PNG", compress_level=9, optimize=False)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def repository_path(path: Path, workspace: Path) -> str:
    return path.resolve().relative_to(workspace.resolve()).as_posix()


def proportional_bounds(extent: int, count: int) -> list[int]:
    """Return half-up proportional grid boundaries using integer arithmetic."""

    return [(index * extent + count // 2) // count for index in range(count + 1)]


def source_box(asset: Asset, atlas_size: tuple[int, int]) -> tuple[int, int, int, int]:
    x_bounds = proportional_bounds(atlas_size[0], GRID_COLUMNS)
    y_bounds = proportional_bounds(atlas_size[1], GRID_ROWS)
    return (
        x_bounds[asset.column],
        y_bounds[asset.row],
        x_bounds[asset.column + 1],
        y_bounds[asset.row + 1],
    )


def run_chroma_helper(helper: Path, source: Path, output: Path) -> str:
    if not helper.is_file():
        raise FileNotFoundError(f"ImageGen chroma helper is missing: {helper}")
    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(helper),
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
        "--force",
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            "ImageGen chroma helper failed for "
            f"{source}:\n{result.stdout}\n{result.stderr}"
        )
    match = re.search(r"Key color: (#?[0-9a-fA-F]{6})", result.stdout)
    if match is None:
        raise RuntimeError(
            f"ImageGen chroma helper did not report a key color for {source}."
        )
    key = match.group(1).lower()
    return key if key.startswith("#") else f"#{key}"


def alpha_fit(keyed: Image.Image, target_size: int) -> tuple[Image.Image, tuple[int, int, int, int]]:
    rgba = keyed.convert("RGBA")
    binary_alpha = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0)
    bounds = binary_alpha.getbbox()
    if bounds is None:
        raise RuntimeError("Chroma removal produced no visible icon pixels.")

    subject = rgba.crop(bounds)
    available = target_size - 2
    scale = min(available / subject.width, available / subject.height)
    resized_size = (
        max(1, int(round(subject.width * scale))),
        max(1, int(round(subject.height * scale))),
    )

    # Resize premultiplied RGBA to avoid a matte fringe at the tiny GUI sizes.
    resized = (
        subject.convert("RGBa")
        .resize(resized_size, Image.Resampling.LANCZOS)
        .convert("RGBA")
    )
    canvas = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
    position = (
        (target_size - resized.width) // 2,
        (target_size - resized.height) // 2,
    )
    canvas.alpha_composite(resized, position)
    return canvas, tuple(int(value) for value in bounds)


def alpha_statistics(image: Image.Image) -> dict[str, Any]:
    rgba = image.convert("RGBA")
    alpha = list(rgba.getchannel("A").getdata())
    corners = [
        rgba.getpixel((0, 0))[3],
        rgba.getpixel((rgba.width - 1, 0))[3],
        rgba.getpixel((0, rgba.height - 1))[3],
        rgba.getpixel((rgba.width - 1, rgba.height - 1))[3],
    ]
    residual_chroma = 0
    for red, green, blue, opacity in rgba.getdata():
        if (
            opacity >= 32
            and red >= 170
            and blue >= 170
            and green <= 90
            and min(red, blue) - green >= 80
        ):
            residual_chroma += 1

    visible_mask = rgba.getchannel("A").point(lambda value: 255 if value > 8 else 0)
    visible_bounds = visible_mask.getbbox()
    return {
        "minimum": min(alpha),
        "maximum": max(alpha),
        "transparent_pixels": sum(value == 0 for value in alpha),
        "partially_transparent_pixels": sum(0 < value < 255 for value in alpha),
        "opaque_pixels": sum(value == 255 for value in alpha),
        "corner_alpha": corners,
        "visible_bounds": list(visible_bounds) if visible_bounds else None,
        "residual_magenta_key_pixels_at_alpha_32_or_more": residual_chroma,
    }


def write_bgra_dds(path: Path, image: Image.Image) -> None:
    """Mirror the event-assets skill's convert_to_dds.py legacy one-level BGRA layout."""

    rgba = image.convert("RGBA")
    width, height = rgba.size
    bgra_data = rgba.tobytes("raw", "BGRA")
    expected_size = width * height * 4
    if len(bgra_data) != expected_size:
        raise RuntimeError(
            f"Unexpected BGRA payload for {path}: {len(bgra_data)} != {expected_size}"
        )

    header = struct.pack(
        "<4s31I",
        b"DDS ",
        124,
        DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT | DDSD_PITCH,
        height,
        width,
        width * 4,
        0,
        0,
        *([0] * 11),
        32,
        DDPF_RGB | DDPF_ALPHAPIXELS,
        0,
        32,
        0x00FF0000,
        0x0000FF00,
        0x000000FF,
        0xFF000000,
        DDSCAPS_TEXTURE,
        0,
        0,
        0,
        0,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(header + bgra_data)


def validate_and_decode_dds(
    path: Path,
    expected_image: Image.Image,
) -> tuple[Image.Image, dict[str, Any]]:
    data = path.read_bytes()
    if len(data) < 128:
        raise RuntimeError(f"DDS is shorter than the legacy header: {path}")
    if data[:4] != b"DDS ":
        raise RuntimeError(f"DDS magic is invalid: {path}")

    fields = struct.unpack("<31I", data[4:128])
    (
        header_size,
        flags,
        height,
        width,
        pitch,
        depth,
        mipmap_count,
        *remaining,
    ) = fields
    reserved = remaining[:11]
    (
        pixel_format_size,
        pixel_format_flags,
        four_cc,
        bit_count,
        red_mask,
        green_mask,
        blue_mask,
        alpha_mask,
        caps,
        caps2,
        caps3,
        caps4,
        reserved2,
    ) = remaining[11:]

    expected_flags = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT | DDSD_PITCH
    expected_length = 128 + width * height * 4
    checks = {
        "magic": data[:4] == b"DDS ",
        "header_size_124": header_size == 124,
        "flags_0x100f": flags == expected_flags,
        "pitch_width_times_four": pitch == width * 4,
        "depth_zero": depth == 0,
        "mipmap_count_zero": mipmap_count == 0,
        "eleven_reserved_dwords_zero": all(value == 0 for value in reserved),
        "pixel_format_offset_76": struct.unpack_from("<I", data, 76)[0] == 32,
        "pixel_format_size_32": pixel_format_size == 32,
        "pixel_format_flags_65": pixel_format_flags == (DDPF_RGB | DDPF_ALPHAPIXELS),
        "four_cc_zero": four_cc == 0,
        "bit_count_32": bit_count == 32,
        "red_mask_bgra": red_mask == 0x00FF0000,
        "green_mask_bgra": green_mask == 0x0000FF00,
        "blue_mask_bgra": blue_mask == 0x000000FF,
        "alpha_mask_bgra": alpha_mask == 0xFF000000,
        "dds_caps_texture_at_108": (
            caps == DDSCAPS_TEXTURE
            and struct.unpack_from("<I", data, 108)[0] == DDSCAPS_TEXTURE
        ),
        "remaining_caps_zero": caps2 == caps3 == caps4 == reserved2 == 0,
        "exact_file_length": len(data) == expected_length,
        "declared_dimensions": (width, height) == expected_image.size,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise RuntimeError(f"Malformed DDS {path}; failed: {', '.join(failed)}")

    payload = data[128:]
    decoded = Image.frombytes("RGBA", (width, height), payload, "raw", "BGRA")
    expected_rgba = expected_image.convert("RGBA")
    decoded_pixel_match = decoded.tobytes() == expected_rgba.tobytes()
    if not decoded_pixel_match:
        raise RuntimeError(f"DDS payload differs from the processed PNG pixels: {path}")

    with Image.open(path) as pillow_dds:
        pillow_decoded = pillow_dds.convert("RGBA")
    pillow_pixel_match = pillow_decoded.tobytes() == expected_rgba.tobytes()
    if not pillow_pixel_match:
        raise RuntimeError(f"Pillow DDS decode differs from the processed PNG: {path}")

    alpha_bytes = payload[3::4]
    return decoded, {
        "declared_width": width,
        "declared_height": height,
        "pitch": pitch,
        "file_length": len(data),
        "expected_file_length": expected_length,
        "pixel_format_offset": 76,
        "caps_offset": 108,
        "alpha_minimum": min(alpha_bytes),
        "alpha_maximum": max(alpha_bytes),
        "processed_pixel_match": decoded_pixel_match,
        "pillow_decode_pixel_match": pillow_pixel_match,
        "header_checks": checks,
    }


def perceptual_dhash(image: Image.Image) -> str:
    rgba = image.convert("RGBA")
    backing = Image.new("RGBA", rgba.size, (127, 127, 127, 255))
    backing.alpha_composite(rgba)
    grayscale = backing.convert("L").resize((17, 16), Image.Resampling.LANCZOS)
    pixels = list(grayscale.getdata())
    bits = []
    for row in range(16):
        start = row * 17
        bits.extend(
            pixels[start + column] > pixels[start + column + 1]
            for column in range(16)
        )
    value = 0
    for bit in bits:
        value = (value << 1) | int(bit)
    return f"{value:064x}"


def hamming_distance(left: str, right: str) -> int:
    # Python 3.9 compatibility: int.bit_count() arrived in Python 3.10.
    return bin(int(left, 16) ^ int(right, 16)).count("1")


def checkerboard(size: tuple[int, int], cell: int = 12) -> Image.Image:
    # Review-only background; never written to an asset source or runtime file.
    image = Image.new("RGBA", size, (148, 148, 148, 255))
    draw = ImageDraw.Draw(image)
    for top in range(0, size[1], cell):
        for left in range(0, size[0], cell):
            colour = (198, 198, 198, 255) if (left // cell + top // cell) % 2 else (132, 132, 132, 255)
            draw.rectangle(
                (left, top, min(left + cell - 1, size[0] - 1), min(top + cell - 1, size[1] - 1)),
                fill=colour,
            )
    return image


def create_source_contact_sheet(
    package_root: Path,
    source_paths: dict[str, Path],
) -> Path:
    tile_width, tile_height = 250, 250
    sheet = Image.new(
        "RGB",
        (tile_width * GRID_COLUMNS, tile_height * GRID_ROWS),
        (24, 26, 28),
    )
    draw = ImageDraw.Draw(sheet)
    for asset in ASSETS:
        left = asset.column * tile_width
        top = asset.row * tile_height
        with Image.open(source_paths[asset.asset_id]) as raw:
            preview = raw.convert("RGB")
        preview.thumbnail((224, 202), Image.Resampling.LANCZOS)
        x = left + (tile_width - preview.width) // 2
        y = top + 8 + (202 - preview.height) // 2
        sheet.paste(preview, (x, y))
        draw.text((left + 10, top + 215), asset.display_name, fill=(240, 240, 240))
        draw.text(
            (left + 10, top + 231),
            f"cell r{asset.row} c{asset.column}",
            fill=(175, 184, 190),
        )
    output = package_root / "contact_sheets" / "source_cells_contact_sheet.png"
    save_png(sheet, output)
    return output


def create_alpha_contact_sheet(
    package_root: Path,
    image_paths: dict[str, Path],
    filename: str,
    evidence_label: str,
) -> Path:
    tile_width, tile_height = 250, 250
    sheet = Image.new(
        "RGBA",
        (tile_width * GRID_COLUMNS, tile_height * GRID_ROWS),
        (24, 26, 28, 255),
    )
    draw = ImageDraw.Draw(sheet)
    for asset in ASSETS:
        left = asset.column * tile_width
        top = asset.row * tile_height
        background = checkerboard((192, 192), cell=12)
        with Image.open(image_paths[asset.asset_id]) as source:
            icon = source.convert("RGBA")
        factor = 192 // asset.target_size
        enlarged = icon.resize(
            (asset.target_size * factor, asset.target_size * factor),
            Image.Resampling.NEAREST,
        )
        background.alpha_composite(
            enlarged,
            ((192 - enlarged.width) // 2, (192 - enlarged.height) // 2),
        )
        sheet.alpha_composite(background, (left + 29, top + 8))
        draw.text((left + 10, top + 207), asset.display_name, fill=(240, 240, 240, 255))
        draw.text(
            (left + 10, top + 223),
            f"{asset.target_size}x{asset.target_size} {evidence_label}",
            fill=(175, 184, 190, 255),
        )
    output = package_root / "contact_sheets" / filename
    save_png(sheet, output)
    return output


def write_checksums(
    workspace: Path,
    package_root: Path,
    atlas_path: Path,
    runtime_paths: Iterable[Path],
) -> Path:
    checksum_path = package_root / "checksums.sha256"
    owned_files = [atlas_path, Path(__file__).resolve()]
    owned_files.extend(
        path
        for path in package_root.rglob("*")
        if path.is_file()
        and path != checksum_path
        and "__pycache__" not in path.parts
    )
    owned_files.extend(runtime_paths)
    unique = {path.resolve(): path.resolve() for path in owned_files}
    ordered = sorted(unique.values(), key=lambda path: repository_path(path, workspace))
    lines = [
        f"{file_sha256(path)}  {repository_path(path, workspace)}"
        for path in ordered
    ]
    with checksum_path.open("w", encoding="ascii", newline="\n") as output:
        output.write("\n".join(lines) + "\n")
    return checksum_path


def main() -> None:
    args = parse_args()
    workspace = args.workspace.resolve()
    helper = args.chroma_helper.resolve()
    atlas_path = workspace / ATLAS_RELATIVE
    package_root = workspace / PACKAGE_RELATIVE
    runtime_root = workspace / RUNTIME_RELATIVE

    if not atlas_path.is_file():
        raise FileNotFoundError(f"Frozen ImageGen atlas is missing: {atlas_path}")
    atlas_hash = file_sha256(atlas_path)
    if atlas_hash != EXPECTED_ATLAS_SHA256:
        raise RuntimeError(
            "Frozen ImageGen atlas hash mismatch; refusing to process different art. "
            f"Expected {EXPECTED_ATLAS_SHA256}, got {atlas_hash}."
        )
    with Image.open(atlas_path) as source_atlas:
        atlas = source_atlas.convert("RGB")
    if atlas.size != EXPECTED_ATLAS_SIZE:
        raise RuntimeError(
            f"Frozen atlas dimensions changed: expected {EXPECTED_ATLAS_SIZE}, got {atlas.size}."
        )

    directories = {
        "source": package_root / "source_cells",
        "keyed": package_root / "keyed_cells",
        "processed": package_root / "processed_png",
        "dds": package_root / "dds",
        "decoded": package_root / "decoded_png",
        "contact": package_root / "contact_sheets",
    }
    for directory in (*directories.values(), runtime_root):
        directory.mkdir(parents=True, exist_ok=True)

    helper_hash = file_sha256(helper)
    source_paths: dict[str, Path] = {}
    processed_paths: dict[str, Path] = {}
    decoded_paths: dict[str, Path] = {}
    runtime_paths: list[Path] = []
    source_entries: list[dict[str, Any]] = []
    validation_entries: list[dict[str, Any]] = []

    for order, asset in enumerate(ASSETS, start=1):
        box = source_box(asset, atlas.size)
        source_cell = atlas.crop(box)
        source_path = directories["source"] / f"{asset.asset_id}_source_cell.png"
        keyed_path = directories["keyed"] / f"{asset.asset_id}_keyed.png"
        processed_path = directories["processed"] / f"{asset.asset_id}.png"
        package_dds = directories["dds"] / f"{asset.asset_id}.dds"
        runtime_dds = runtime_root / f"{asset.asset_id}.dds"
        decoded_path = directories["decoded"] / f"{asset.asset_id}_decoded.png"

        save_png(source_cell, source_path)
        key_colour = run_chroma_helper(helper, source_path, keyed_path)
        with Image.open(keyed_path) as keyed_source:
            processed, keyed_subject_box = alpha_fit(keyed_source, asset.target_size)
        save_png(processed, processed_path)

        stats = alpha_statistics(processed)
        if stats["minimum"] != 0 or stats["maximum"] != 255:
            raise RuntimeError(f"Alpha range is incomplete for {asset.asset_id}: {stats}")
        if any(stats["corner_alpha"]):
            raise RuntimeError(f"Processed corners are not transparent: {asset.asset_id}")
        if stats["transparent_pixels"] == 0 or stats["opaque_pixels"] == 0:
            raise RuntimeError(f"Processed alpha lacks transparent/opaque coverage: {asset.asset_id}")
        if stats["residual_magenta_key_pixels_at_alpha_32_or_more"] != 0:
            raise RuntimeError(f"Residual magenta key pixels remain: {asset.asset_id}")

        write_bgra_dds(package_dds, processed)
        runtime_dds.write_bytes(package_dds.read_bytes())
        decoded, dds_validation = validate_and_decode_dds(package_dds, processed)
        runtime_decoded, runtime_validation = validate_and_decode_dds(runtime_dds, processed)
        if decoded.tobytes() != runtime_decoded.tobytes():
            raise RuntimeError(f"Package/runtime DDS decodes differ: {asset.asset_id}")
        save_png(decoded, decoded_path)

        package_hash = file_sha256(package_dds)
        runtime_hash = file_sha256(runtime_dds)
        if package_hash != runtime_hash:
            raise RuntimeError(f"Package/runtime DDS bytes differ: {asset.asset_id}")

        source_paths[asset.asset_id] = source_path
        processed_paths[asset.asset_id] = processed_path
        decoded_paths[asset.asset_id] = decoded_path
        runtime_paths.append(runtime_dds)

        source_entries.append(
            {
                "order": order,
                "asset_id": asset.asset_id,
                "display_name": asset.display_name,
                "asset_type": asset.asset_type,
                "atlas_cell": {"row": asset.row, "column": asset.column},
                "atlas_crop_box_left_top_right_bottom": list(box),
                "raw_source_cell_size": list(source_cell.size),
                "raw_source_cell_path": repository_path(source_path, workspace),
                "raw_source_cell_sha256": file_sha256(source_path),
                "keyed_source_path": repository_path(keyed_path, workspace),
                "keyed_source_sha256": file_sha256(keyed_path),
                "sampled_chroma_key": key_colour,
                "keyed_subject_bounds": list(keyed_subject_box),
            }
        )
        validation_entries.append(
            {
                "asset_id": asset.asset_id,
                "display_name": asset.display_name,
                "asset_type": asset.asset_type,
                "target_size": [asset.target_size, asset.target_size],
                "sprite_name": asset.sprite_name,
                "intended_use": asset.intended_use,
                "processed_png": repository_path(processed_path, workspace),
                "processed_png_sha256": file_sha256(processed_path),
                "processed_alpha": stats,
                "package_dds": repository_path(package_dds, workspace),
                "package_dds_sha256": package_hash,
                "runtime_dds": repository_path(runtime_dds, workspace),
                "runtime_dds_sha256": runtime_hash,
                "package_runtime_byte_identical": package_hash == runtime_hash,
                "dds_header_and_pixel_validation": dds_validation,
                "runtime_header_and_pixel_validation": runtime_validation,
                "decoded_png": repository_path(decoded_path, workspace),
                "decoded_png_sha256": file_sha256(decoded_path),
                "perceptual_dhash_256": perceptual_dhash(processed),
            }
        )

    source_hashes = [entry["raw_source_cell_sha256"] for entry in source_entries]
    processed_hashes = [entry["processed_png_sha256"] for entry in validation_entries]
    dds_hashes = [entry["runtime_dds_sha256"] for entry in validation_entries]
    perceptual_hashes = [entry["perceptual_dhash_256"] for entry in validation_entries]
    if len(set(source_hashes)) != len(ASSETS):
        raise RuntimeError("Raw ImageGen source-cell records are not all distinct.")
    if len(set(processed_hashes)) != len(ASSETS):
        raise RuntimeError("Processed icons are not all byte-distinct.")
    if len(set(dds_hashes)) != len(ASSETS):
        raise RuntimeError("Runtime DDS files are not all byte-distinct.")
    if len(set(perceptual_hashes)) != len(ASSETS):
        raise RuntimeError("Processed icons are not all perceptually distinct by dHash.")

    pairwise_distances = [
        hamming_distance(left, right)
        for left, right in combinations(perceptual_hashes, 2)
    ]
    source_contact = create_source_contact_sheet(package_root, source_paths)
    processed_contact = create_alpha_contact_sheet(
        package_root,
        processed_paths,
        "processed_alpha_contact_sheet.png",
        "processed PNG",
    )
    decoded_contact = create_alpha_contact_sheet(
        package_root,
        decoded_paths,
        "dds_decoded_contact_sheet.png",
        "DDS decoded",
    )

    source_record = {
        "schema": "chaos_redux_event_asset_source_records_v1",
        "processing_date": PROCESSING_DATE,
        "source_mode": "built-in ImageGen atlas (frozen generated source)",
        "source_atlas": {
            "path": repository_path(atlas_path, workspace),
            "sha256": atlas_hash,
            "dimensions": list(atlas.size),
            "mode": "RGB",
            "grid": {"columns": GRID_COLUMNS, "rows": GRID_ROWS},
        },
        "provenance_verification": {
            "imagegen_source_evidence_retained": True,
            "atlas_hash_pinned_by_processor": True,
            "accepted_design_sources": [
                "docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_8_assets_localisation_and_acceptance.md",
                "docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md",
                "docs/assets/015_utopia_manifesto/requirement_to_runtime_coverage_2026_07_16.md",
                "docs/assets/015_utopia_manifesto/icon_animation_handoff.md",
                "docs/assets/015_utopia_manifesto/gfx_handoff.md",
            ],
            "exact_original_generation_prompt_present_in_repository": False,
            "prompt_record_note": (
                "The repository preserves and explicitly identifies the atlas as ImageGen "
                "provenance, but no verbatim original generation prompt was found. This "
                "record does not invent or relabel a reconstructed prompt as exact."
            ),
            "cell_semantics_verified_against_visual_motifs_and_accepted_spec": True,
            "visible_art_reconstructed_or_redrawn": False,
        },
        "transparency_processor": {
            "path": "$CODEX_HOME/skills/.system/imagegen/scripts/remove_chroma_key.py",
            "sha256": helper_hash,
            "arguments": [
                "--auto-key border",
                "--soft-matte",
                "--transparent-threshold 12",
                "--opaque-threshold 220",
                "--despill",
            ],
        },
        "assets": source_entries,
    }
    write_json(package_root / "source_records.json", source_record)

    validation_record = {
        "schema": "chaos_redux_event_asset_validation_v1",
        "processing_date": PROCESSING_DATE,
        "python": sys.version.split()[0],
        "pillow": PILLOW_VERSION,
        "all_checks_passed": True,
        "canvas_authority": {
            "value_icons": [32, 32],
            "calling_icons": [48, 48],
            "source": "current Event 015 GFX handoff and requirement-to-runtime crosswalk",
        },
        "distinctness": {
            "asset_count": len(ASSETS),
            "unique_raw_source_cell_sha256_count": len(set(source_hashes)),
            "unique_processed_png_sha256_count": len(set(processed_hashes)),
            "unique_runtime_dds_sha256_count": len(set(dds_hashes)),
            "unique_perceptual_dhash_count": len(set(perceptual_hashes)),
            "minimum_pairwise_perceptual_hamming_distance": min(pairwise_distances),
            "maximum_pairwise_perceptual_hamming_distance": max(pairwise_distances),
        },
        "contact_sheets": [
            {
                "path": repository_path(source_contact, workspace),
                "sha256": file_sha256(source_contact),
                "purpose": "raw atlas cell evidence",
            },
            {
                "path": repository_path(processed_contact, workspace),
                "sha256": file_sha256(processed_contact),
                "purpose": "native processed alpha review over checkerboard",
            },
            {
                "path": repository_path(decoded_contact, workspace),
                "sha256": file_sha256(decoded_contact),
                "purpose": "decoded runtime DDS alpha review over checkerboard",
            },
        ],
        "assets": validation_entries,
    }
    write_json(package_root / "validation.json", validation_record)

    checksum_path = write_checksums(
        workspace,
        package_root,
        atlas_path,
        runtime_paths,
    )
    print(f"Processed {len(ASSETS)} distinct Event 015 Ledger icons.")
    print(f"Source records: {package_root / 'source_records.json'}")
    print(f"Validation: {package_root / 'validation.json'}")
    print(f"Checksums: {checksum_path}")
    print(f"Runtime folder: {runtime_root}")


if __name__ == "__main__":
    main()
