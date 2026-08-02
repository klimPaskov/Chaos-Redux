#!/usr/bin/env python3
"""Build the Event 006 COX--CYX researched flag tranche.

The retained ImageGen source masters are the design source.  This script only
performs mechanical cover-cropping, palette flattening, resizing, contact-sheet
assembly, and bottom-origin 32-bit BGRA TGA export.  It never draws or edits a
replacement emblem.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
# package root -> event folder -> assets -> docs -> mod root
REPO_ROOT = PACKAGE_ROOT.parents[3]
SOURCE_DIR = PACKAGE_ROOT / "source_png"
REFERENCE_DIR = PACKAGE_ROOT / "references"
PROCESSED_DIR = PACKAGE_ROOT / "processed_png"
FINAL_TGA_DIR = PACKAGE_ROOT / "final_tga"
CONTACT_DIR = PACKAGE_ROOT / "contact_sheets"
METADATA_DIR = PACKAGE_ROOT / "metadata"
PROMPT_DIR = PACKAGE_ROOT / "prompts"

SIZES = {"normal": (82, 52), "medium": (41, 26), "small": (10, 7)}
TARGET_RATIO = 82 / 52

SPECS = (
    ("COX", "Lazistan", "COX_lazistan_imagegen_raw.png", "COX_lazistan.png", "https://en.wikipedia.org/wiki/Lazistan; https://commons.wikimedia.org/wiki/File:Fictitious_flag_of_Lazistan_Sanjak.svg", "generated Laz coastal civic synthesis: deep Black Sea green, oxblood border, white mountain-and-wave emblem, red sun disk; replaces the reference's generic crescent-star with a civic maritime symbol"),
    ("CPX", "Pontus", "CPX_pontus_imagegen_raw.png", "CPX_pontus.png", "https://en.wikipedia.org/wiki/Republic_of_Pontus; https://commons.wikimedia.org/wiki/File:Flag_of_Pontus.svg", "Pontic heraldic reconstruction: gold field, centered black double-headed eagle and thin circular keyline; no text"),
    ("CQX", "Cilicia", "CQX_cilicia_imagegen_raw.png", "CQX_cilicia.png", "https://en.wikipedia.org/wiki/Armenian_Kingdom_of_Cilicia; https://commons.wikimedia.org/wiki/File:Flag_of_the_Rubenid_Dynasty.svg", "generated civic synthesis using the Rubenid red crowned lion on gold with Mediterranean blue and red lower stripe; not claimed as an attested 1936 standard"),
    ("CUX", "Hejaz", "CUX_hejaz_imagegen_raw.png", "CUX_hejaz.png", "https://en.wikipedia.org/wiki/Flag_of_the_Arab_Revolt; https://commons.wikimedia.org/wiki/File:Flag_of_Hejaz_(1917).svg", "historical Hejaz reconstruction: red hoist triangle with black, green, and white horizontal fields; no script"),
    ("CVX", "Najd", "CVX_najd_imagegen_raw.png", "CVX_najd.png", "https://en.wikipedia.org/wiki/Third_Saudi_state; https://commons.wikimedia.org/wiki/File:Flag_of_Saudi_Arabia.svg", "generated Najdi civic adaptation: deep green field, white sword and eight-point desert rosette; Arabic script intentionally omitted"),
    ("CWX", "Jabal Shammar", "CWX_jabal_shammar_imagegen_raw.png", "CWX_jabal_shammar.png", "https://en.wikipedia.org/wiki/Emirate_of_Jabal_Shammar; https://commons.wikimedia.org/wiki/File:Flag_of_the_Emirate_of_Ha%27il.svg", "historical Rashidi/Ha'il reconstruction: red field with golden crescent and eight-point star"),
    ("CXX", "Hadhramaut", "CXX_hadhramaut_imagegen_raw.png", "CXX_hadhramaut.png", "https://en.wikipedia.org/wiki/Hadhramaut; https://en.wikipedia.org/wiki/File:Kathiri_flag.svg", "generated Hadhramaut civic synthesis from Kathiri regional colours: gold-green-gold bands, red hoist triangle, three white stars"),
    ("CYX", "Mahra", "CYX_mahra_imagegen_raw.png", "CYX_mahra.png", "https://en.wikipedia.org/wiki/Mahra_Sultanate; https://commons.wikimedia.org/wiki/File:Flag_of_the_Mahra_Sultanate.svg", "historical Mahra reconstruction: green-white-red bands with a centered black crescent and star"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def cover_crop(image: Image.Image) -> Image.Image:
    width, height = image.size
    ratio = width / height
    if ratio > TARGET_RATIO:
        crop_width = int(round(height * TARGET_RATIO))
        left = max(0, (width - crop_width) // 2)
        return image.crop((left, 0, left + crop_width, height))
    crop_height = int(round(width / TARGET_RATIO))
    top = max(0, (height - crop_height) // 2)
    return image.crop((0, top, width, top + crop_height))


def flatten(image: Image.Image) -> Image.Image:
    return image.convert("RGB").quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")


def write_tga_bottom_left(path: Path, image: Image.Image) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
    pixels = rgba.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    payload = bytes(channel for pixel in pixels.getdata() for channel in (pixel[2], pixel[1], pixel[0], pixel[3]))
    path.write_bytes(header + payload)


def tga_header(path: Path) -> dict[str, int | str]:
    raw = path.read_bytes()
    header = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    return {"image_type": header[2], "width": header[8], "height": header[9], "pixel_depth": header[10], "descriptor": header[11], "origin": "top-left" if header[11] & 0x20 else "bottom-left", "byte_length": len(raw), "expected_byte_length": 18 + header[8] * header[9] * 4}


def contact_sheets(source_images: dict[str, Image.Image], final_images: dict[str, dict[str, Image.Image]]) -> None:
    font = ImageFont.load_default()
    source_sheet = Image.new("RGB", (1600, 900), (235, 235, 235))
    draw = ImageDraw.Draw(source_sheet)
    draw.text((16, 12), "Event 006 COX-CYX ImageGen flag source masters", fill=(0, 0, 0), font=font)
    for index, (tag, identity, *_rest) in enumerate(SPECS):
        row, col = divmod(index, 2)
        x, y = 16 + col * 790, 42 + row * 205
        preview = source_images[tag].copy()
        preview.thumbnail((740, 160), Image.Resampling.LANCZOS)
        draw.text((x, y), f"{tag} - {identity} - {source_images[tag].size[0]}x{source_images[tag].size[1]}", fill=(0, 0, 0), font=font)
        source_sheet.paste(preview, (x, y + 18))
    source_sheet.save(CONTACT_DIR / "source_masters_contact_sheet.png")

    ladder = Image.new("RGB", (1300, 1160), (235, 235, 235))
    draw = ImageDraw.Draw(ladder)
    draw.text((16, 12), "Event 006 COX-CYX final flag ladders (nearest-neighbour review)", fill=(0, 0, 0), font=font)
    scales = {"normal": 2, "medium": 3, "small": 12}
    x_positions = {"normal": 160, "medium": 420, "small": 620}
    for name in SIZES:
        draw.text((x_positions[name], 35), f"{name} {SIZES[name][0]}x{SIZES[name][1]}", fill=(0, 0, 0), font=font)
    for row, (tag, _identity, *_rest) in enumerate(SPECS):
        y = 65 + row * 135
        draw.text((16, y + 8), tag, fill=(0, 0, 0), font=font)
        for name in SIZES:
            image = final_images[tag][name]
            enlarged = image.resize((image.width * scales[name], image.height * scales[name]), Image.Resampling.NEAREST)
            ladder.paste(enlarged, (x_positions[name], y))
            draw.rectangle((x_positions[name] - 1, y - 1, x_positions[name] + enlarged.width, y + enlarged.height), outline=(80, 80, 80))
    ladder.save(CONTACT_DIR / "final_size_ladder_enlarged_contact_sheet.png")


def process() -> None:
    for directory in (PROCESSED_DIR, FINAL_TGA_DIR, CONTACT_DIR, METADATA_DIR, PROMPT_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    source_images: dict[str, Image.Image] = {}
    final_images: dict[str, dict[str, Image.Image]] = {}
    records: dict[str, object] = {}
    for tag, identity, source_name, reference_name, design_reference, geometry in SPECS:
        source_path = SOURCE_DIR / source_name
        source = Image.open(source_path).convert("RGB")
        source_images[tag] = source
        (PROMPT_DIR / f"{tag}_flag_imagegen_prompt.txt").write_text(f"ImageGen flat flag source for {identity}: {geometry}. Preserve cited design reference {design_reference}. Horizontal 16:10 rectangular flag, no fabric, pole, perspective, shadow, gradient, painterly texture, text, or scene.\n", encoding="utf-8")
        master = flatten(cover_crop(source).resize((820, 520), Image.Resampling.LANCZOS))
        master_path = PROCESSED_DIR / f"{tag}_flat_master_820x520.png"
        master.save(master_path)
        tag_outputs: dict[str, Image.Image] = {}
        size_records: dict[str, object] = {}
        for role, size in SIZES.items():
            candidate = master.resize(size, Image.Resampling.NEAREST if role == "small" else Image.Resampling.LANCZOS)
            png_path = PROCESSED_DIR / role / f"{tag}.png"
            tga_path = FINAL_TGA_DIR / f"{tag}_{role}_{size[0]}x{size[1]}.tga"
            candidate.save(png_path)
            write_tga_bottom_left(tga_path, candidate)
            runtime_path = REPO_ROOT / "gfx" / "flags" / (f"{tag}.tga" if role == "normal" else f"{role}/{tag}.tga")
            runtime_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(tga_path, runtime_path)
            decoded = Image.open(tga_path).convert("RGB")
            if decoded.size != size or list(decoded.getdata()) != list(candidate.getdata()):
                raise ValueError(f"{tag} {role} TGA does not decode to processed PNG")
            header = tga_header(tga_path)
            if not (header["image_type"] == 2 and header["pixel_depth"] == 32 and header["origin"] == "bottom-left" and header["byte_length"] == header["expected_byte_length"]):
                raise ValueError(f"{tag} {role} TGA header invalid: {header}")
            tag_outputs[role] = decoded
            size_records[role] = {"dimensions": list(size), "processed_png": png_path.relative_to(PACKAGE_ROOT).as_posix(), "package_tga": tga_path.relative_to(PACKAGE_ROOT).as_posix(), "runtime_tga": runtime_path.relative_to(REPO_ROOT).as_posix(), "processed_png_sha256": sha256(png_path), "package_tga_sha256": sha256(tga_path), "runtime_tga_sha256": sha256(runtime_path), "tga_header": header}
        final_images[tag] = tag_outputs
        ref_path = REFERENCE_DIR / reference_name
        records[tag] = {"package_id": {"COX": "IW-067", "CPX": "IW-068", "CQX": "IW-069", "CUX": "IW-073", "CVX": "IW-074", "CWX": "IW-075", "CXX": "IW-076", "CYX": "IW-077"}[tag], "identity": identity, "source_mode": "imagegen", "source_png": source_path.relative_to(PACKAGE_ROOT).as_posix(), "source_dimensions": list(source.size), "source_sha256": sha256(source_path), "reference_file": ref_path.relative_to(PACKAGE_ROOT).as_posix(), "reference_sha256": sha256(ref_path), "design_reference": design_reference, "geometry_note": geometry, "processed_master": master_path.relative_to(PACKAGE_ROOT).as_posix(), "processed_master_sha256": sha256(master_path), "sizes": size_records, "status": "handed_off"}
    contact_sheets(source_images, final_images)
    validation = {"package": "006_independence_wave/event006_missing_flags_2026_08_02_chunk_cox_ebx", "asset_type": "historical and historically grounded flat flags", "target_sizes": {key: list(value) for key, value in SIZES.items()}, "flags": records, "contact_sheets": ["contact_sheets/source_masters_contact_sheet.png", "contact_sheets/final_size_ladder_enlarged_contact_sheet.png"]}
    (METADATA_DIR / "flag_validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    lines = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if path.is_file() and path.name != "hashes.sha256" and "__pycache__" not in path.parts:
            lines.append(f"{sha256(path)}  {path.relative_to(PACKAGE_ROOT).as_posix()}")
    for tag, *_rest in SPECS:
        for role in SIZES:
            runtime = REPO_ROOT / "gfx" / "flags" / (f"{tag}.tga" if role == "normal" else f"{role}/{tag}.tga")
            lines.append(f"{sha256(runtime)}  repo:{runtime.relative_to(REPO_ROOT).as_posix()}")
    (METADATA_DIR / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    process()
