#!/usr/bin/env python3
"""Mechanically process the Event 006 chunk-3 flag source masters.

The source PNGs are retained ImageGen outputs.  This script only performs
cover-cropping, colour-management, resizing, and bottom-origin uncompressed
32-bit BGRA TGA export.  It never draws or traces a replacement emblem.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PACKAGE_ROOT = Path(__file__).resolve().parent
# chunk3 lives at <repo>/docs/assets/006_independence_wave/<package>; the
# repository root is the fourth parent of the package directory.
REPO_ROOT = PACKAGE_ROOT.parents[3]
SOURCE_DIR = PACKAGE_ROOT / "source_png"
PROCESSED_DIR = PACKAGE_ROOT / "processed_png"
FINAL_TGA_DIR = PACKAGE_ROOT / "final_tga"
CONTACT_DIR = PACKAGE_ROOT / "contact_sheets"
METADATA_DIR = PACKAGE_ROOT / "metadata"
PROMPT_DIR = PACKAGE_ROOT / "prompts"

SIZES = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}
TARGET_RATIO = 82 / 52

REVIEW_TAGS = {
    "GMX",
    "GZX",
    "HAX",
    "HDX",
    "HEX",
    "IBX",
    "GIX",
    "GRX",
    "HFX",
    "HGX",
    "HKX",
    "HPX",
    "HSX",
    "HUX",
}

REVIEW_NOTES = {
    "GMX": "Kokbayraq identity is grounded, but East Turkestan scope and modern reference overlap need review.",
    "GZX": "The Great Seal-style roundel is a simplified generated emblem and needs small-size review.",
    "HAX": "Fictional Cascadia route synthesis; not an asserted historical flag.",
    "HDX": "Generated Cherokee civic synthesis; institutional and community review required.",
    "HEX": "Generated Haudenosaunee synthesis; universal historical claim and community approval remain open.",
    "IBX": "Generated Kachin civic synthesis; no defensible single 1936 historical flag source was found.",
    "GIX": "Generated Wa civic synthesis; no defensible single 1936 historical flag source was found.",
    "GRX": "Generated negotiated iwi-led synthesis; not a copy of the modern Tino Rangatiratanga flag.",
    "HFX": "Generated Lakota treaty-state synthesis; community review required.",
    "HGX": "Generated pre-1968 Diné synthesis; modern Navajo flag intentionally excluded.",
    "HKX": "Generated negotiated Zapotec-Mixtec textile synthesis; community review required.",
    "HPX": "Generated Aymara Altiplano synthesis; Wiphala intentionally excluded and review required.",
    "HSX": "Generated Muisca restoration synthesis; archaeological motifs are not an attested 1936 flag.",
    "HUX": "Generated Patagonian civic synthesis; explicitly not Welsh, Araucanian, or Argentine flag art.",
}


SPECS = (
    ("GMX", "East Turkestan", "GMX_east_turkestan_imagegen_raw.png", "https://en.wikipedia.org/wiki/Flag_of_East_Turkestan", "1933–1934 East Turkestan Republic Kokbayraq reference: deep blue field, one white hoist-opening crescent, one white five-point star"),
    ("GTX", "Tonga", "GTX_tonga_imagegen_raw.png", "https://en.wikipedia.org/wiki/Flag_of_Tonga", "attested 1875 Tongan flag: red field, white hoist canton, centered red Greek cross"),
    ("GYX", "Acadia", "GYX_acadia_imagegen_raw.png", "https://en.wikipedia.org/wiki/Flag_of_Acadia", "attested 1884 Acadian flag: French tricolour bands with one gold star in the blue hoist band"),
    ("GZX", "Newfoundland", "GZX_newfoundland_imagegen_raw.png", "https://en.wikipedia.org/wiki/Dominion_of_Newfoundland", "1904–1949 Dominion of Newfoundland red ensign: Union Jack canton and compact Great Seal-style roundel"),
    ("HAX", "Cascadia", "HAX_cascadia_imagegen_raw.png", "https://en.wikipedia.org/wiki/Cascadia_(independence_movement)", "fictional alternate-history civic synthesis from Pacific Northwest forest and river motifs; not a historical flag claim"),
    ("HCX", "Texas", "HCX_texas_imagegen_raw.png", "https://en.wikipedia.org/wiki/Flag_of_Texas", "attested Texas Lone Star flag: blue hoist panel, white upper fly, red lower fly, one white star"),
    ("HDX", "Cherokee Nation", "HDX_cherokee_imagegen_raw.png", "https://www.cherokee.org/about-the-nation/frequently-asked-questions/culture/?page=2&pageSize=7&term=", "generated compact civic synthesis using the exact Cherokee seven-point star and seven-oak-leaf institutional cues; not a copy of the modern official flag"),
    ("HEX", "Haudenosaunee Confederacy", "HEX_haudenosaunee_imagegen_raw.png", "https://en.wikipedia.org/wiki/Flag_of_the_Iroquois_Confederacy", "generated negotiated-confederacy civic synthesis from the Haudenosaunee wampum-belt and Eastern white pine motif; not an asserted universal historical flag"),
    ("IBX", "Kachin State", "IBX_kachin_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Kachin_Independence_Army", "generated alternate-history civic synthesis from Kachin highland, river, jade, and sun motifs; no attested historical flag claim"),
    ("GIX", "Wa State", "GIX_wa_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Wa_State", "generated alternate-history civic synthesis from Wa mountain-valley, tea, rubber, and sun motifs; no exact modern Wa flag copy"),
    ("GRX", "Iwi-led Maori Federation", "GRX_maori_federation_imagegen_raw.png", "https://en.wikipedia.org/wiki/Tino_Rangatiratanga", "generated negotiated iwi-led civic synthesis using restrained koru and wave geometry; not a copy of the modern Tino Rangatiratanga flag"),
    ("HFX", "Lakota State", "HFX_lakota_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Lakota_people", "generated alternate-history civic synthesis from Lakota treaty-territory, Black Hills, directional sun, and restrained feather cues"),
    ("HGX", "Dine State", "HGX_dine_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Navajo_Nation", "generated pre-1968 alternate-history Diné civic synthesis from four-direction mountain geometry; explicitly not the 1968 Navajo Nation flag"),
    ("HKX", "Zapotec-Mixtec Federation", "HKX_zapotec_mixtec_imagegen_raw.png", "https://en.wikipedia.org/wiki/Mixtec", "generated negotiated Oaxaca civic synthesis combining distinct Zapotec and Mixtec textile geometry; no generic Aztec or Mexican motif"),
    ("HPX", "Aymara State", "HPX_aymara_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Aymara_people", "generated alternate-history Altiplano civic synthesis from restrained chakana-inspired geometry; explicitly not a Wiphala copy"),
    ("HSX", "Muisca Restoration", "HSX_muisca_restoration_imagegen_raw.png", "https://en.wikipedia.org/wiki/Muisca", "generated alternate-history civic synthesis from Muisca raft, sun, river, and mountain archaeology cues"),
    ("HUX", "Patagonian State", "HUX_patagonian_state_imagegen_raw.png", "https://en.wikipedia.org/wiki/Patagonia", "generated non-Welsh, non-Araucania civic synthesis from southern wind, steppe, coastal wave, star, and sun motifs"),
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
    # Mechanical colour management removes generation gradients while
    # retaining the source emblem geometry and colour fields.
    return image.convert("RGB").quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")


def write_tga_bottom_left(path: Path, image: Image.Image) -> None:
    rgba = image.convert("RGBA")
    width, height = rgba.size
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
    pixels = rgba.transpose(Image.Transpose.FLIP_TOP_BOTTOM).getdata()
    payload = bytes(channel for pixel in pixels for channel in (pixel[2], pixel[1], pixel[0], pixel[3]))
    path.write_bytes(header + payload)


def read_tga_header(path: Path) -> dict[str, int | str]:
    raw = path.read_bytes()
    header = struct.unpack("<BBBHHBHHHHBB", raw[:18])
    return {
        "image_type": header[2],
        "width": header[8],
        "height": header[9],
        "pixel_depth": header[10],
        "descriptor": header[11],
        "origin": "top-left" if header[11] & 0x20 else "bottom-left",
        "byte_length": len(raw),
        "expected_byte_length": 18 + header[8] * header[9] * 4,
    }


def make_contact_sheets(source_images: dict[str, Image.Image], finals: dict[str, dict[str, Image.Image]]) -> None:
    font = ImageFont.load_default()
    cols = 2
    rows = (len(SPECS) + cols - 1) // cols
    source_sheet = Image.new("RGB", (1600, 205 * rows + 42), (235, 235, 235))
    draw = ImageDraw.Draw(source_sheet)
    draw.text((16, 12), "Event 006 chunk 3 ImageGen source masters", fill=(0, 0, 0), font=font)
    for index, (tag, identity, *_rest) in enumerate(SPECS):
        row, col = divmod(index, cols)
        x, y = 16 + col * 790, 42 + row * 205
        preview = source_images[tag].copy()
        preview.thumbnail((740, 160), Image.Resampling.LANCZOS)
        draw.text((x, y), f"{tag} – {identity} – {source_images[tag].size[0]}x{source_images[tag].size[1]}", fill=(0, 0, 0), font=font)
        source_sheet.paste(preview, (x, y + 18))
    source_sheet.save(CONTACT_DIR / "source_masters_contact_sheet.png")

    # The small flag is enlarged 32x (224 px high), so leave enough vertical
    # clearance between rows for an honest ladder review instead of letting
    # neighbouring assets overlap.
    row_height = 250
    ladder = Image.new("RGB", (1300, 65 + row_height * len(SPECS)), (235, 235, 235))
    draw = ImageDraw.Draw(ladder)
    draw.text((16, 12), "Event 006 chunk 3 final flag ladders (normal / medium / small)", fill=(0, 0, 0), font=font)
    scales = {"normal": 4, "medium": 8, "small": 32}
    x_positions = {"normal": 160, "medium": 570, "small": 950}
    for name in SIZES:
        draw.text((x_positions[name], 35), f"{name} {SIZES[name][0]}x{SIZES[name][1]}", fill=(0, 0, 0), font=font)
    for row, (tag, identity, *_rest) in enumerate(SPECS):
        y = 65 + row * row_height
        draw.text((16, y + 8), tag, fill=(0, 0, 0), font=font)
        for name in SIZES:
            image = finals[tag][name]
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

    for tag, identity, source_name, reference, geometry in SPECS:
        source_path = SOURCE_DIR / source_name
        source = Image.open(source_path).convert("RGB")
        source_images[tag] = source
        (PROMPT_DIR / f"{tag}_flag_imagegen_prompt.txt").write_text(
            f"Clean flat flag source for {identity}. Preserve the cited design reference {reference}. {geometry}. Horizontal 3:2 rectangular flag, no fabric, pole, perspective, shadow, gradient, painterly texture, text, or scene.\n",
            encoding="utf-8",
        )
        master = flatten(cover_crop(source).resize((820, 520), Image.Resampling.LANCZOS))
        master_path = PROCESSED_DIR / f"{tag}_flat_master_820x520.png"
        master.save(master_path)
        tag_outputs: dict[str, Image.Image] = {}
        size_records: dict[str, object] = {}
        for role, size in SIZES.items():
            resample = Image.Resampling.NEAREST if role == "small" else Image.Resampling.LANCZOS
            candidate = master.resize(size, resample)
            png_path = PROCESSED_DIR / role / f"{tag}.png"
            tga_path = FINAL_TGA_DIR / f"{tag}_{role}_{size[0]}x{size[1]}.tga"
            png_path.parent.mkdir(parents=True, exist_ok=True)
            candidate.save(png_path)
            write_tga_bottom_left(tga_path, candidate)
            runtime_path = REPO_ROOT / "gfx" / "flags" / (f"{tag}.tga" if role == "normal" else f"{role}/{tag}.tga")
            runtime_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(tga_path, runtime_path)
            decoded = Image.open(tga_path).convert("RGB")
            if decoded.size != size or list(decoded.getdata()) != list(candidate.getdata()):
                raise ValueError(f"{tag} {role} TGA does not decode to the processed PNG")
            header = read_tga_header(tga_path)
            if not (header["image_type"] == 2 and header["pixel_depth"] == 32 and header["origin"] == "bottom-left" and header["byte_length"] == header["expected_byte_length"]):
                raise ValueError(f"{tag} {role} TGA header invalid: {header}")
            tag_outputs[role] = decoded
            size_records[role] = {
                "dimensions": list(size),
                "processed_png": png_path.relative_to(PACKAGE_ROOT).as_posix(),
                "package_tga": tga_path.relative_to(PACKAGE_ROOT).as_posix(),
                "runtime_tga": runtime_path.relative_to(REPO_ROOT).as_posix(),
                "processed_png_sha256": sha256(png_path),
                "package_tga_sha256": sha256(tga_path),
                "runtime_tga_sha256": sha256(runtime_path),
                "tga_header": header,
            }
        final_images[tag] = tag_outputs
        records[tag] = {
            "identity": identity,
            "source_mode": "imagegen",
            "source_png": source_path.relative_to(PACKAGE_ROOT).as_posix(),
            "source_dimensions": list(source.size),
            "source_sha256": sha256(source_path),
            "design_reference": reference,
            "geometry_note": geometry,
            "processed_master": master_path.relative_to(PACKAGE_ROOT).as_posix(),
            "processed_master_sha256": sha256(master_path),
            "sizes": size_records,
            "status": "needs_user_review" if tag in REVIEW_TAGS else "handed_off",
            "uncertainty": REVIEW_NOTES.get(tag, "No material uncertainty beyond the generated clean redraw."),
        }

    make_contact_sheets(source_images, final_images)
    validation = {
        "package": "006_independence_wave/event006_missing_flags_2026_08_02_chunk3",
        "asset_type": "historical and historically grounded flat flags",
        "target_sizes": {key: list(value) for key, value in SIZES.items()},
        "flags": records,
        "contact_sheets": [
            "contact_sheets/source_masters_contact_sheet.png",
            "contact_sheets/final_size_ladder_enlarged_contact_sheet.png",
        ],
    }
    (METADATA_DIR / "flag_validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    lines = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if path.is_file() and path.name != "hashes.sha256" and "__pycache__" not in path.parts:
            lines.append(f"{sha256(path)}  {path.relative_to(PACKAGE_ROOT).as_posix()}")
    for tag, *_ in SPECS:
        for role in SIZES:
            runtime = REPO_ROOT / "gfx" / "flags" / (f"{tag}.tga" if role == "normal" else f"{role}/{tag}.tga")
            lines.append(f"{sha256(runtime)}  repo:{runtime.relative_to(REPO_ROOT).as_posix()}")
    (METADATA_DIR / "hashes.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    process()
