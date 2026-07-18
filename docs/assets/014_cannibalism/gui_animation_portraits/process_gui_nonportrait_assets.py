#!/usr/bin/env python3
"""Finalize Event 014 static GUI art and non-portrait frame animations.

The generated sources are already frozen in this package. This processor only
performs the allowed mechanical work: exact crop/resize, chroma-key removal,
OpenRaster guide-master assembly, frame-sheet assembly, preview/contact-sheet
creation, uncompressed BGRA DDS writing, hashing, and inventory generation.
It deliberately leaves the two leader portrait packages to their dedicated
portrait production tranche.
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import shutil
import struct
import sys
import zipfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = Path(__file__).resolve().parent
STATIC_SOURCE = PACKAGE / "static" / "source_png"
STATIC_PROCESSED = PACKAGE / "static" / "processed_png"
STATIC_ORA = PACKAGE / "static" / "editable_ora"
ANIMATIONS = PACKAGE / "animations"
VALIDATION = PACKAGE / "validation"
RUNTIME_STATIC = ROOT / "gfx" / "interface" / "014_cannibalism"
RUNTIME_ANIMATED = ROOT / "gfx" / "interface" / "animated" / "014_cannibalism"


STATIC_SIZES: dict[str, tuple[int, int]] = {
    "early_category_background": (470, 304),
    "network_window_background": (860, 620),
    "warlord_command_background": (470, 340),
    "revealed_command_background": (470, 380),
    "wendigo_command_background": (470, 400),
    "field_hunger_meter": (278, 48),
    "command_integrity_meter": (278, 48),
    "cult_cohesion_meter": (278, 48),
    "primary_state_card": (278, 72),
    "network_country_card": (374, 64),
    "network_state_card": (374, 64),
    "network_target_frame": (374, 64),
    "larder_meter": (278, 48),
    "frenzy_meter": (278, 48),
    "network_alignment_meter": (278, 48),
    "controlled_state_card": (278, 72),
    "global_larder_meter": (278, 48),
    "global_network_meter": (278, 48),
    "warlord_loyalty_card": (278, 72),
    "continental_target_card": (278, 72),
    "revealed_portrait_frame": (166, 220),
    "transformed_portrait_frame": (166, 220),
    "anchor_card": (278, 72),
    "countdown_frame": (278, 48),
    "wendigo_unit_capacity": (278, 48),
    "winter_hunger_meter": (278, 48),
}


ANIMATION_SPECS: dict[str, tuple[int, int, int, int]] = {
    # stem: width, height, frames, fps
    "cannibalism_early_warning_seal": (64, 64, 8, 8),
    "cannibalism_cult_cohesion_emblem": (64, 64, 8, 8),
    "cannibalism_network_threads": (824, 120, 12, 8),
    "cannibalism_island_alert": (64, 64, 8, 8),
    "cannibalism_selected_target_overlay": (374, 64, 6, 6),
    "cannibalism_critical_larder_glow": (64, 64, 8, 8),
    "cannibalism_frenzy_border": (142, 54, 8, 8),
    "cannibalism_warlord_route_emblem": (94, 86, 8, 8),
    "cannibalism_unification_seal": (94, 86, 12, 8),
    "cannibalism_ordinary_terminal_frame": (438, 40, 12, 8),
    "cannibalism_wendigo_anchor_pulse": (64, 64, 12, 8),
    "cannibalism_wendigo_terminal_frame": (438, 40, 12, 8),
}


METER_GUIDE = [(14, 10, 244, 28)]
CARD_GUIDE = [(14, 10, 244, 52)]
STATIC_GUIDES: dict[str, list[tuple[int, int, int, int]]] = {
    "early_category_background": [
        (24, 14, 330, 32), (20, 54, 278, 48), (20, 104, 278, 48),
        (20, 154, 278, 48), (20, 204, 278, 72), (308, 216, 145, 42),
        (14, 266, 106, 29), (335, 266, 106, 29),
    ],
    "network_window_background": [
        (22, 16, 430, 32), (22, 46, 520, 44), (18, 88, 662, 34),
        (682, 88, 161, 34), (18, 130, 824, 120), (25, 264, 374, 26),
        (438, 264, 374, 26), (18, 290, 394, 222), (431, 290, 394, 222),
        (243, 530, 374, 64),
    ],
    "warlord_command_background": [
        (24, 14, 320, 32), (20, 54, 278, 48), (20, 104, 278, 48),
        (20, 154, 278, 48), (20, 204, 278, 72), (306, 252, 142, 44),
        (14, 302, 106, 29),
    ],
    "revealed_command_background": [
        (24, 14, 410, 32), (15, 49, 166, 220), (184, 58, 278, 48),
        (184, 108, 278, 48), (184, 158, 278, 72), (184, 232, 278, 72),
        (16, 304, 438, 40), (14, 342, 106, 29),
    ],
    "wendigo_command_background": [
        (24, 14, 410, 32), (15, 49, 166, 220), (184, 58, 278, 72),
        (184, 132, 278, 48), (184, 182, 278, 48), (184, 232, 278, 48),
        (16, 320, 438, 40), (14, 362, 106, 29),
    ],
    "field_hunger_meter": METER_GUIDE,
    "command_integrity_meter": METER_GUIDE,
    "cult_cohesion_meter": METER_GUIDE,
    "primary_state_card": CARD_GUIDE,
    "network_country_card": [(58, 8, 304, 50)],
    "network_state_card": [(14, 8, 346, 50)],
    "network_target_frame": [(12, 13, 39, 26), (59, 10, 300, 45)],
    "larder_meter": METER_GUIDE,
    "frenzy_meter": METER_GUIDE,
    "network_alignment_meter": METER_GUIDE,
    "controlled_state_card": CARD_GUIDE,
    "global_larder_meter": METER_GUIDE,
    "global_network_meter": METER_GUIDE,
    "warlord_loyalty_card": CARD_GUIDE,
    "continental_target_card": CARD_GUIDE,
    "revealed_portrait_frame": [],
    "transformed_portrait_frame": [],
    "anchor_card": CARD_GUIDE,
    "countdown_frame": METER_GUIDE,
    "wendigo_unit_capacity": METER_GUIDE,
    "winter_hunger_meter": METER_GUIDE,
}


def load_dds_writer():
    path = ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
    spec = importlib.util.spec_from_file_location("chaos_dds", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load DDS writer: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.write_bgra_dds


WRITE_BGRA_DDS = load_dds_writer()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_dds(image: Image.Image, path: Path) -> None:
    image = image.convert("RGBA")
    path.parent.mkdir(parents=True, exist_ok=True)
    WRITE_BGRA_DDS(path, image.width, image.height, image.tobytes("raw", "BGRA"))


def dds_header(path: Path) -> tuple[int, int, int, int, int, int]:
    data = path.read_bytes()[:128]
    if len(data) != 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS header: {path}")
    values = struct.unpack("<31I", data[4:128])
    height, width = values[2], values[3]
    rgb_bits, r_mask, g_mask, b_mask, a_mask = values[21:26]
    return width, height, rgb_bits, r_mask, g_mask, b_mask, a_mask


def validate_dds(path: Path, width: int, height: int) -> None:
    values = dds_header(path)
    expected = (width, height, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    if values != expected:
        raise RuntimeError(f"DDS format mismatch for {path}: {values!r}")
    expected_size = 128 + width * height * 4
    if path.stat().st_size != expected_size:
        raise RuntimeError(f"DDS payload-size mismatch for {path}")


def remove_green(image: Image.Image) -> Image.Image:
    """Remove the generated flat green field with antialias and spill cleanup."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    rgb = rgba[:, :, :3].astype(np.float32)
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    dominance = green - np.maximum(red, blue)
    distance = np.sqrt(red * red + (green - 255) * (green - 255) + blue * blue)
    likely_key = (green > 65) & (dominance > 18)
    alpha_dominance = np.clip((100 - dominance) * (255.0 / 82.0), 0, 255)
    alpha_distance = np.clip((distance - 12) * (255.0 / 120.0), 0, 255)
    key_alpha = np.where(likely_key, np.minimum(alpha_dominance, alpha_distance), 255)
    rgba[:, :, 3] = np.minimum(rgba[:, :, 3], key_alpha.astype(np.uint8))
    affected = rgba[:, :, 3] < 250
    clean_green = np.minimum(green, np.maximum(red, blue) + 12)
    rgba[:, :, 1] = np.where(affected, clean_green, green).astype(np.uint8)
    rgba[rgba[:, :, 3] == 0, :3] = 0
    return Image.fromarray(rgba, "RGBA")


def fit_static(source: Image.Image, size: tuple[int, int], keyed: bool) -> Image.Image:
    target = ImageOps.fit(source.convert("RGBA"), size, Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    return remove_green(target) if keyed else target


def draw_guides(size: tuple[int, int], boxes: list[tuple[int, int, int, int]]) -> Image.Image:
    guide = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(guide, "RGBA")
    for x, y, width, height in boxes:
        draw.rectangle((x, y, x + width - 1, y + height - 1), fill=(255, 204, 0, 36), outline=(255, 64, 32, 230), width=2)
    return guide


def png_bytes(image: Image.Image) -> bytes:
    output = io.BytesIO()
    image.save(output, format="PNG", optimize=True)
    return output.getvalue()


def write_ora(artwork: Image.Image, guide: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    composite = Image.alpha_composite(artwork.convert("RGBA"), guide.convert("RGBA"))
    thumbnail = composite.copy()
    thumbnail.thumbnail((256, 256), Image.Resampling.LANCZOS)
    stack_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<image version="0.0.3" w="{artwork.width}" h="{artwork.height}" name="{path.stem}">\n'
        '  <stack name="root">\n'
        '    <layer name="Text-safe guides" src="data/text_safe_guide.png" visibility="visible"/>\n'
        '    <layer name="Generated artwork" src="data/artwork.png" visibility="visible"/>\n'
        '  </stack>\n'
        '</image>\n'
    ).encode("utf-8")
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("mimetype", b"image/openraster", compress_type=zipfile.ZIP_STORED)
        archive.writestr("stack.xml", stack_xml, compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("data/artwork.png", png_bytes(artwork), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("data/text_safe_guide.png", png_bytes(guide), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("mergedimage.png", png_bytes(composite), compress_type=zipfile.ZIP_DEFLATED)
        archive.writestr("Thumbnails/thumbnail.png", png_bytes(thumbnail), compress_type=zipfile.ZIP_DEFLATED)


def checker(size: tuple[int, int], cell: int = 12) -> Image.Image:
    image = Image.new("RGBA", size, (42, 42, 42, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(70, 70, 70, 255))
    return image


def labeled_native_contact(entries: list[tuple[str, Image.Image, Image.Image]], path: Path) -> None:
    cell_width, cell_height, columns = 900, 680, 2
    rows = (len(entries) + columns - 1) // columns
    contact = Image.new("RGB", (cell_width * columns, cell_height * rows), (16, 16, 16))
    draw = ImageDraw.Draw(contact)
    for index, (name, artwork, guide) in enumerate(entries):
        x0 = (index % columns) * cell_width
        y0 = (index // columns) * cell_height
        composite = Image.alpha_composite(artwork, guide)
        backdrop = checker(composite.size)
        backdrop.alpha_composite(composite)
        x = x0 + (cell_width - backdrop.width) // 2
        y = y0 + 34 + (620 - backdrop.height) // 2
        contact.paste(backdrop.convert("RGB"), (x, y))
        draw.text((x0 + 12, y0 + 8), f"{name} — native {artwork.width}x{artwork.height}", fill=(245, 245, 245))
    path.parent.mkdir(parents=True, exist_ok=True)
    contact.save(path, optimize=True)


def animation_contact(name: str, frames: list[Image.Image], path: Path) -> None:
    max_preview_w = 420 if frames[0].width > 300 else 220
    max_preview_h = 150 if frames[0].height < 100 else 220
    columns = 2 if frames[0].width > 300 else 4
    tile_w, tile_h = max_preview_w + 20, max_preview_h + 44
    rows = (len(frames) + columns - 1) // columns
    contact = Image.new("RGB", (tile_w * columns, tile_h * rows), (15, 15, 15))
    draw = ImageDraw.Draw(contact)
    for index, frame in enumerate(frames):
        preview = frame.copy()
        preview.thumbnail((max_preview_w, max_preview_h), Image.Resampling.LANCZOS)
        tile = checker((max_preview_w, max_preview_h))
        tile.alpha_composite(preview, ((max_preview_w - preview.width) // 2, (max_preview_h - preview.height) // 2))
        x = (index % columns) * tile_w + 10
        y = (index // columns) * tile_h + 10
        contact.paste(tile.convert("RGB"), (x, y))
        draw.text((x, y + max_preview_h + 7), f"frame {index:03d}", fill=(240, 240, 240))
    path.parent.mkdir(parents=True, exist_ok=True)
    contact.save(path, optimize=True)


def process_static() -> list[list[str]]:
    STATIC_PROCESSED.mkdir(parents=True, exist_ok=True)
    STATIC_ORA.mkdir(parents=True, exist_ok=True)
    RUNTIME_STATIC.mkdir(parents=True, exist_ok=True)
    rows: list[list[str]] = []
    contact_entries: list[tuple[str, Image.Image, Image.Image]] = []
    for stem, size in STATIC_SIZES.items():
        source_path = STATIC_SOURCE / f"{stem}_source.png"
        if not source_path.exists():
            raise RuntimeError(f"Missing static GUI source: {source_path}")
        keyed = stem in {"revealed_portrait_frame", "transformed_portrait_frame"}
        artwork = fit_static(Image.open(source_path), size, keyed)
        guide = draw_guides(size, STATIC_GUIDES[stem])
        processed_path = STATIC_PROCESSED / f"{stem}.png"
        ora_path = STATIC_ORA / f"{stem}.ora"
        runtime_png = RUNTIME_STATIC / f"{stem}.png"
        runtime_dds = RUNTIME_STATIC / f"{stem}.dds"
        artwork.save(processed_path, optimize=True)
        shutil.copyfile(processed_path, runtime_png)
        write_dds(artwork, runtime_dds)
        validate_dds(runtime_dds, *size)
        write_ora(artwork, guide, ora_path)
        if Image.open(processed_path).size != size or Image.open(runtime_png).size != size:
            raise RuntimeError(f"PNG size mismatch for {stem}")
        if sha256(processed_path) != sha256(runtime_png):
            raise RuntimeError(f"Runtime PNG differs from processed master for {stem}")
        if keyed and artwork.getchannel("A").getextrema()[0] != 0:
            raise RuntimeError(f"Expected transparency was not produced for {stem}")
        rows.append([
            stem, f"{size[0]}x{size[1]}", source_path.as_posix(), sha256(source_path),
            processed_path.as_posix(), sha256(processed_path), ora_path.as_posix(), sha256(ora_path),
            runtime_png.relative_to(ROOT).as_posix(), sha256(runtime_png),
            runtime_dds.relative_to(ROOT).as_posix(), sha256(runtime_dds), str(runtime_dds.stat().st_size),
        ])
        contact_entries.append((stem, artwork, guide))
    labeled_native_contact(contact_entries, VALIDATION / "static_gui_text_safe_native_contact.png")
    return rows


def process_animations() -> tuple[list[list[str]], list[list[str]]]:
    RUNTIME_ANIMATED.mkdir(parents=True, exist_ok=True)
    inventory_rows: list[list[str]] = []
    handoff_rows: list[list[str]] = []
    for stem, (width, height, frame_count, fps) in ANIMATION_SPECS.items():
        package = ANIMATIONS / stem
        source_paths = sorted((package / "source_frames").glob("*.png"))
        if len(source_paths) != frame_count:
            raise RuntimeError(f"{stem}: expected {frame_count} source frames, found {len(source_paths)}")
        processed_dir = package / "processed_frames"
        sheets_dir = package / "sheets"
        previews_dir = package / "previews"
        notes_dir = package / "notes"
        for directory in (processed_dir, sheets_dir, previews_dir, notes_dir):
            directory.mkdir(parents=True, exist_ok=True)
        frames: list[Image.Image] = []
        frame_rows: list[list[str]] = []
        for index, source_path in enumerate(source_paths):
            source = Image.open(source_path).convert("RGBA")
            resized = source.resize((width, height), Image.Resampling.LANCZOS)
            frame = remove_green(resized)
            if frame.getchannel("A").getextrema()[0] != 0:
                raise RuntimeError(f"{stem} frame {index}: chroma key left no transparent pixels")
            processed_path = processed_dir / f"{stem}_{index:03d}.png"
            frame.save(processed_path, optimize=True)
            frames.append(frame)
            frame_rows.append([
                f"{index:03d}", source_path.as_posix(), sha256(source_path),
                processed_path.as_posix(), sha256(processed_path),
            ])
        source_hashes = {row[2] for row in frame_rows}
        processed_hashes = {row[4] for row in frame_rows}
        if len(source_hashes) != frame_count or len(processed_hashes) != frame_count:
            raise RuntimeError(f"{stem}: duplicate source or processed frames detected")
        sheet = Image.new("RGBA", (width * frame_count, height), (0, 0, 0, 0))
        for index, frame in enumerate(frames):
            sheet.alpha_composite(frame, (index * width, 0))
        sheet_png = sheets_dir / f"{stem}_sheet.png"
        sheet_dds = sheets_dir / f"{stem}_sheet.dds"
        static_png = sheets_dir / f"{stem}_static.png"
        static_dds = sheets_dir / f"{stem}_static.dds"
        sheet.save(sheet_png, optimize=True)
        frames[0].save(static_png, optimize=True)
        write_dds(sheet, sheet_dds)
        write_dds(frames[0], static_dds)
        validate_dds(sheet_dds, width * frame_count, height)
        validate_dds(static_dds, width, height)
        runtime_sheet_png = RUNTIME_ANIMATED / f"{stem}_sheet.png"
        runtime_sheet_dds = RUNTIME_ANIMATED / f"{stem}_sheet.dds"
        runtime_static_png = RUNTIME_ANIMATED / f"{stem}_static.png"
        runtime_static_dds = RUNTIME_ANIMATED / f"{stem}_static.dds"
        for source, destination in (
            (sheet_png, runtime_sheet_png), (sheet_dds, runtime_sheet_dds),
            (static_png, runtime_static_png), (static_dds, runtime_static_dds),
        ):
            shutil.copyfile(source, destination)
        validate_dds(runtime_sheet_dds, width * frame_count, height)
        validate_dds(runtime_static_dds, width, height)
        preview_gif = previews_dir / f"{stem}_preview.gif"
        gif_frames = [frame.convert("RGBA") for frame in frames]
        gif_frames[0].save(
            preview_gif, save_all=True, append_images=gif_frames[1:], duration=round(1000 / fps),
            loop=0, disposal=2, optimize=False,
        )
        contact_path = previews_dir / f"{stem}_contact.png"
        animation_contact(stem, frames, contact_path)
        frame_inventory = notes_dir / "frame_inventory.tsv"
        with frame_inventory.open("w", encoding="utf-8", newline="") as handle:
            handle.write("frame\tsource\tsource_sha256\tprocessed\tprocessed_sha256\n")
            for row in frame_rows:
                handle.write("\t".join(row) + "\n")
        manifest_path = notes_dir / "manifest.md"
        manifest_text = (
            f"# {stem} Final Animation Manifest\n\n"
            f"- Source frames: {frame_count} independent generated or accepted semantic frames.\n"
            f"- Frame size: {width}x{height}.\n"
            f"- Horizontal sheet: {width * frame_count}x{height}.\n"
            f"- Runtime FPS: {fps}; looping and play-on-show.\n"
            f"- Static fallback: source frame 000 after exact processing.\n"
            f"- Transparency: chroma-key field removed with antialiased spill cleanup.\n"
            f"- DDS: one-image-level, uncompressed 32-bit BGRA.\n"
            f"- Frame hashes: `{frame_inventory.relative_to(PACKAGE).as_posix()}`.\n"
            f"- Contact sheet: `{contact_path.relative_to(PACKAGE).as_posix()}`.\n"
            f"- Preview GIF: `{preview_gif.relative_to(PACKAGE).as_posix()}`.\n"
            f"- Runtime static: `{runtime_static_dds.relative_to(ROOT).as_posix()}`.\n"
            f"- Runtime sheet: `{runtime_sheet_dds.relative_to(ROOT).as_posix()}`.\n"
        )
        manifest_path.write_text(manifest_text, encoding="utf-8")
        for kind, local_png, local_dds, runtime_png, runtime_dds, final_width, final_height in (
            ("static", static_png, static_dds, runtime_static_png, runtime_static_dds, width, height),
            ("sheet", sheet_png, sheet_dds, runtime_sheet_png, runtime_sheet_dds, width * frame_count, height),
        ):
            if sha256(local_png) != sha256(runtime_png) or sha256(local_dds) != sha256(runtime_dds):
                raise RuntimeError(f"{stem}: runtime {kind} differs from package final")
            inventory_rows.append([
                stem, kind, f"{final_width}x{final_height}", str(frame_count), str(fps),
                local_png.as_posix(), sha256(local_png), local_dds.as_posix(), sha256(local_dds),
                runtime_png.relative_to(ROOT).as_posix(), sha256(runtime_png),
                runtime_dds.relative_to(ROOT).as_posix(), sha256(runtime_dds), str(runtime_dds.stat().st_size),
                preview_gif.as_posix(), sha256(preview_gif), contact_path.as_posix(), sha256(contact_path),
            ])
        handoff_rows.append([
            stem,
            f"GFX_{stem}_static",
            f"GFX_{stem}_animated",
            runtime_static_dds.relative_to(ROOT).as_posix(),
            runtime_sheet_dds.relative_to(ROOT).as_posix(),
            f"{width}x{height}", str(frame_count), str(fps), "yes", "yes",
        ])
    return inventory_rows, handoff_rows


def write_tsv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write("\t".join(header) + "\n")
        for row in rows:
            handle.write("\t".join(row) + "\n")


def write_consolidated_runtime_inventory() -> None:
    rows: list[list[str]] = []
    for stem, size in STATIC_SIZES.items():
        for extension in ("png", "dds"):
            path = RUNTIME_STATIC / f"{stem}.{extension}"
            if not path.exists():
                raise RuntimeError(f"Missing consolidated static runtime: {path}")
            rows.append([
                "static_gui", stem, extension, path.relative_to(ROOT).as_posix(),
                f"{size[0]}x{size[1]}", sha256(path), str(path.stat().st_size), "complete",
            ])
    for stem, (width, height, frame_count, _fps) in ANIMATION_SPECS.items():
        for kind, final_width in (("static", width), ("sheet", width * frame_count)):
            for extension in ("png", "dds"):
                path = RUNTIME_ANIMATED / f"{stem}_{kind}.{extension}"
                if not path.exists():
                    raise RuntimeError(f"Missing consolidated animation runtime: {path}")
                rows.append([
                    "nonportrait_animation", stem, f"{kind}_{extension}", path.relative_to(ROOT).as_posix(),
                    f"{final_width}x{height}", sha256(path), str(path.stat().st_size), "complete",
                ])
    write_tsv(
        VALIDATION / "final_inventory.tsv",
        ["family", "stem", "kind", "runtime_path", "dimensions", "sha256", "bytes", "status"],
        rows,
    )


def write_consolidated_gfx_handoff(handoff_rows: list[list[str]]) -> None:
    rows: list[list[str]] = []
    for stem, size in STATIC_SIZES.items():
        rows.append([
            "static_gui", stem, f"GFX_cannibalism_{stem}", "",
            f"gfx/interface/014_cannibalism/{stem}.dds", "", f"{size[0]}x{size[1]}",
            "1", "", "no", "no", "surface-gated by scripted GUI",
        ])
    gates = {
        "cannibalism_early_warning_seal": "early containment",
        "cannibalism_cult_cohesion_emblem": "Evolution I / Cult Cohesion",
        "cannibalism_network_threads": "Evolution II network",
        "cannibalism_island_alert": "Evolution II island node",
        "cannibalism_selected_target_overlay": "Evolution II network selection",
        "cannibalism_critical_larder_glow": "warlord command",
        "cannibalism_frenzy_border": "warlord command",
        "cannibalism_warlord_route_emblem": "warlord command",
        "cannibalism_unification_seal": "public reveal complete",
        "cannibalism_ordinary_terminal_frame": "ordinary terminal preparation",
        "cannibalism_wendigo_anchor_pulse": "Wendigo route active",
        "cannibalism_wendigo_terminal_frame": "Wendigo terminal preparation",
    }
    for row in handoff_rows:
        stem, static_sprite, animated_sprite, static_runtime, sheet_runtime, frame_size, frames, fps, looping, play_on_show = row
        rows.append([
            "nonportrait_animation", stem, static_sprite, animated_sprite, static_runtime, sheet_runtime,
            frame_size, frames, fps, looping, play_on_show, gates[stem],
        ])
    write_tsv(
        VALIDATION / "gfx_handoff.tsv",
        [
            "family", "stem", "static_sprite", "animated_sprite", "static_runtime", "sheet_runtime",
            "frame_size", "frames", "fps", "looping", "play_on_show", "gate",
        ],
        rows,
    )


def main() -> int:
    static_rows = process_static()
    animation_rows, handoff_rows = process_animations()
    write_tsv(
        VALIDATION / "static_gui_inventory.tsv",
        [
            "stem", "size", "source", "source_sha256", "processed", "processed_sha256",
            "ora", "ora_sha256", "runtime_png", "runtime_png_sha256", "runtime_dds",
            "runtime_dds_sha256", "runtime_dds_bytes",
        ],
        static_rows,
    )
    write_tsv(
        VALIDATION / "nonportrait_animation_inventory.tsv",
        [
            "stem", "kind", "size", "frames", "fps", "package_png", "package_png_sha256",
            "package_dds", "package_dds_sha256", "runtime_png", "runtime_png_sha256",
            "runtime_dds", "runtime_dds_sha256", "runtime_dds_bytes", "preview_gif",
            "preview_gif_sha256", "contact_sheet", "contact_sheet_sha256",
        ],
        animation_rows,
    )
    write_tsv(
        VALIDATION / "gfx_handoff_nonportrait.tsv",
        [
            "stem", "static_sprite", "animated_sprite", "static_runtime", "sheet_runtime",
            "frame_size", "frames", "fps", "looping", "play_on_show",
        ],
        handoff_rows,
    )
    write_consolidated_runtime_inventory()
    write_consolidated_gfx_handoff(handoff_rows)
    print(f"Processed {len(static_rows)} static GUI assets and {len(ANIMATION_SPECS)} animations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
