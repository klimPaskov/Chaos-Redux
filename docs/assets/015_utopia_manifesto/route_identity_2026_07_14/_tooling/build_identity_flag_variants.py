#!/usr/bin/env python3
"""Finish and validate the corrected Event 015 cosmetic flag package.

Every independent composition consumed here is an OpenAI ImageGen source PNG.
This script performs deterministic aspect fitting, restrained colour finishing,
detail-preserving resize, bottom-left-origin TGA export, decoded review output,
contact-sheet assembly, checksum recording, and optional targeted merging into
``asset_records.json``. It never draws, traces, flattens, quantizes, or replaces
ImageGen-authored heraldry and never creates palette-swap compositions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import struct
import subprocess
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps, ImageStat


REPO = Path(__file__).resolve().parents[5]
BASE = REPO / "docs/assets/015_utopia_manifesto/route_identity_2026_07_14"
SOURCE = BASE / "source_png/flags"
PROCESSED = BASE / "processed_png/flags"
FINAL = BASE / "final_tga/flags"
DECODED = BASE / "decoded_png/flags"
CONTACT = BASE / "contact_sheets"
RUNTIME = REPO / "gfx/flags"
FILE_EXE = Path(r"C:/Program Files/Git/usr/bin/file.exe")

SIZES = {
    "main": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

# One built-in ImageGen call produced every composition in this mapping.
COMPOSITIONS = {
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic": {
        "handle": "exec-a00b7dd5-e6df-43f7-a5ec-961eac40b43e",
        "note": "Households, lamp, ledger, bridge, wheat, and olive form an open democratic civic wreath.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism": {
        "handle": "exec-4830bcae-7f57-427d-81d3-3a977aeb5adf",
        "note": "Three households, shared provisions, ledger, bridge, keys, and garden vines bind a collective covenant.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality": {
        "handle": "exec-4c0b4e46-07d2-456b-8f17-89bdfe14fa93",
        "note": "A household shelter surrounds a lamp, sprout, common table, charter knot, and bridge.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism": {
        "handle": "exec-75a8d15a-ca56-4fea-b2a7-ca646cec33b8",
        "note": "A tall storehouse and two households are held by ledger clasps, chain, keys, grain, and a command lamp.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_democratic": {
        "handle": "exec-a02699ba-d65a-4800-9b65-b79d7b56d511",
        "note": "Six vocational chambers, an empty table, open doorway, and civic branches form a deliberative seal.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_communism": {
        "handle": "exec-5e7e4a0e-330e-4300-86e7-c07ac28008e8",
        "note": "Six callings radiate around a shared ledger table inside a broken cooperative tool-wheel.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality": {
        "handle": "exec-9b9a068d-d3d0-4caa-93a5-488c880c168c",
        "note": "Six registry cabinets surround an empty council table, balance, seal, cord, and paired keys.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_fascism": {
        "handle": "exec-ac754d06-492a-4672-aa64-f7f71078797b",
        "note": "A fortified vocational register locks six callings behind a chained council table and command beacon.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic": {
        "handle": "exec-9311272b-6ed7-41a5-b45d-3f1496d9a8ab",
        "note": "A compass spans three bridged garden neighborhoods, a balance, ledger, open gate, and network nodes.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism": {
        "handle": "exec-cc3f3dc5-776a-4d90-9bd2-a4dcdcaf4ec4",
        "note": "A compass binds five settlement nodes to rail, water, a common plan table, gear, and bridge.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality": {
        "handle": "exec-7263b637-a24e-4569-ade3-a441f8372f3e",
        "note": "Standards instruments encircle a reservoir settlement plan, survey chain, ledger, weights, and bridge.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism": {
        "handle": "exec-c1d34458-0883-4df8-86ba-562dc7ebfc56",
        "note": "A compass and plumb bob lock a city, dam, granary, rail plan, sealed ledger, keys, chains, and weights.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic": {
        "handle": "exec-43161b07-9f43-4ee4-bb93-4cf87e226a6c",
        "note": "Lighthouse, granary, civic hall, broken seawalls, open gates, bridge, harbor, and branches mark an open island.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_communism": {
        "handle": "exec-38dff557-bd42-4911-9fc5-6255f59d9fe3",
        "note": "A beacon, granary, cistern, cooperative store, provision ledger, chain, and segmented seawall form one island reserve.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality": {
        "handle": "exec-94ddbc41-34a5-4345-a34e-c5215ada68df",
        "note": "A settled island lies behind balanced seawalls and a controlled causeway above a sealed ledger and harbor keys.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism": {
        "handle": "exec-bd341026-0f7d-4d7d-9933-f55af966e035",
        "note": "A fortress island, reserve store, beacon, cistern, locks, chained gate, keys, and emergency causeway form a closed reserve.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH": {
        "handle": "exec-13569204-8901-4da9-9f98-e30baf9ce967",
        "note": "An open ledger, bridge, lamp, water pump, store, garden, road, compass, service nodes, keys, and charter cord define the route.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_democratic": {
        "handle": "exec-828d91f8-92de-4bc2-86fc-8a75be943fd8",
        "note": "Five borough gates surround an empty ledger table, public lamp, bridge, garden, water outlet, rail wheel, and open gate.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_communism": {
        "handle": "exec-5d2e9889-30d2-4406-a8bb-af2f258f0b34",
        "note": "Workshop, provision store, field, and rail-water transport share one ledger table above a bridge and grain braid.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_neutrality": {
        "handle": "exec-43f01089-3ec4-4c5e-9c4a-e6a9b9fc101b",
        "note": "A lamp, bridge, standards ledger, pump, garden, crate, rail, compass, balance, conduits, keys, and charter seal form a municipal escutcheon.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_fascism": {
        "handle": "exec-ad67e6bd-46d0-4379-85d7-4e41840429df",
        "note": "A fortified store, command lamp, sealed ledger, controlled bridge, locked service conduits, keys, and chains impose assignment.",
    },
}

# These are the only intentional aliases. They do not consume extra generation
# calls; their source and final files are exact byte copies of the canonical art.
ALIASES = {
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH": "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic",
    "UTOPIA_MANIFESTO_COUNCIL_UNION": "UTOPIA_MANIFESTO_COUNCIL_UNION_communism",
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA": "UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality",
    "UTOPIA_MANIFESTO_CLOSED_ISLAND": "UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism",
}

ROUTE_STEMS = {
    "voluntary_commonwealth": "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH",
    "council_union": "UTOPIA_MANIFESTO_COUNCIL_UNION",
    "planned_utopia": "UTOPIA_MANIFESTO_PLANNED_UTOPIA",
    "closed_island": "UTOPIA_MANIFESTO_CLOSED_ISLAND",
    "practical_commonwealth": "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH",
}
IDEOLOGIES = ("democratic", "communism", "neutrality", "fascism")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO)).replace("\\", "/")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def font(size: int) -> ImageFont.ImageFont:
    for candidate in (Path(r"C:/Windows/Fonts/arial.ttf"), Path(r"C:/Windows/Fonts/segoeui.ttf")):
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def ensure_directories() -> None:
    for root in (PROCESSED, FINAL, DECODED, RUNTIME):
        root.mkdir(parents=True, exist_ok=True)
        (root / "medium").mkdir(parents=True, exist_ok=True)
        (root / "small").mkdir(parents=True, exist_ok=True)
    CONTACT.mkdir(parents=True, exist_ok=True)


def path_for(root: Path, stem: str, size_name: str, suffix: str) -> Path:
    return root / f"{stem}{suffix}" if size_name == "main" else root / size_name / f"{stem}{suffix}"


def finish_to_size(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Preserve generated geometry while preparing a readable HOI4 flag size."""
    fitted = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGB")
    fitted = ImageEnhance.Contrast(fitted).enhance(1.045)
    fitted = ImageEnhance.Color(fitted).enhance(1.025)
    if min(size) > 20:
        fitted = fitted.filter(ImageFilter.UnsharpMask(radius=0.55, percent=62, threshold=3))
    else:
        fitted = fitted.filter(ImageFilter.UnsharpMask(radius=0.30, percent=42, threshold=3))
    return fitted.convert("RGBA")


def process_source(source: Path) -> dict[str, Image.Image]:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
    return {
        size_name: finish_to_size(image, size)
        for size_name, size in SIZES.items()
    }


def source_preservation_rms(source: Path, processed: Image.Image) -> float:
    with Image.open(source) as opened:
        reference = ImageOps.fit(
            ImageOps.exif_transpose(opened).convert("RGB"),
            processed.size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
    difference = ImageChops.difference(reference, processed.convert("RGB"))
    return round(sum(ImageStat.Stat(difference).rms) / 3.0, 4)


def write_tga_bottom_left(image: Image.Image, path: Path) -> None:
    image = image.convert("RGBA")
    width, height = image.size
    header = struct.pack("<BBBHHBHHHHBB", 0, 0, 2, 0, 0, 0, 0, 0, width, height, 32, 8)
    rgba = image.tobytes()
    row_bytes = width * 4
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        handle.write(header)
        for y in range(height - 1, -1, -1):
            row = rgba[y * row_bytes : (y + 1) * row_bytes]
            bgra = bytearray(row_bytes)
            for index in range(0, row_bytes, 4):
                red, green, blue, alpha = row[index : index + 4]
                bgra[index : index + 4] = bytes((blue, green, red, alpha))
            handle.write(bgra)


def validate_tga(path: Path, expected: tuple[int, int]) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 18:
        raise ValueError(f"short TGA: {path}")
    header = struct.unpack("<BBBHHBHHHHBB", data[:18])
    id_length, color_map_type, image_type, color_map_first, color_map_length, color_map_depth, x_origin, y_origin, width, height, depth, descriptor = header
    expected_length = 18 + width * height * 4
    contract = (
        id_length == 0
        and color_map_type == 0
        and image_type == 2
        and color_map_first == 0
        and color_map_length == 0
        and color_map_depth == 0
        and x_origin == 0
        and y_origin == 0
        and (width, height) == expected
        and depth == 32
        and descriptor == 8
        and len(data) == expected_length
    )
    if not contract:
        raise ValueError(f"invalid bottom-left 32-bit TGA contract: {path}")
    alpha = [min(data[21::4]), max(data[21::4])]
    if alpha != [255, 255]:
        raise ValueError(f"flag alpha is not fully opaque: {path}: {alpha}")
    with Image.open(path) as decoded:
        decoded.load()
        if decoded.size != expected:
            raise ValueError(f"decoded size mismatch: {path}")
    return {
        "dimensions": list(expected),
        "bit_depth": depth,
        "descriptor": descriptor,
        "top_origin": bool(descriptor & 0x20),
        "alpha_range": alpha,
        "byte_length": len(data),
        "sha256": sha256(path),
    }


def file_description(path: Path) -> str:
    if not FILE_EXE.is_file():
        raise FileNotFoundError(FILE_EXE)
    result = subprocess.run([str(FILE_EXE), "-b", str(path)], check=True, capture_output=True, text=True)
    description = result.stdout.strip()
    if "Targa image data" not in description or " - top" in description:
        raise ValueError(f"unexpected file(1) output for {path}: {description}")
    return description


def copy_alias_sources() -> None:
    for alias, canonical in ALIASES.items():
        shutil.copyfile(SOURCE / f"{canonical}_source.png", SOURCE / f"{alias}_source.png")


def export_composition(stem: str, details: dict[str, str]) -> list[dict[str, object]]:
    source = SOURCE / f"{stem}_source.png"
    if not source.is_file():
        raise FileNotFoundError(source)
    with Image.open(source) as opened:
        source_dimensions = [opened.width, opened.height]
    images = process_source(source)
    records = []
    for size_name, expected in SIZES.items():
        processed = path_for(PROCESSED, stem, size_name, ".png")
        package_final = path_for(FINAL, stem, size_name, ".tga")
        runtime_final = path_for(RUNTIME, stem, size_name, ".tga")
        decoded = path_for(DECODED, stem, size_name, ".png")
        processed.parent.mkdir(parents=True, exist_ok=True)
        images[size_name].save(processed)
        write_tga_bottom_left(images[size_name], package_final)
        shutil.copyfile(package_final, runtime_final)
        validation = validate_tga(runtime_final, expected)
        with Image.open(runtime_final) as opened:
            decoded_image = opened.convert("RGBA")
        if ImageChops.difference(decoded_image, images[size_name]).getbbox() is not None:
            raise ValueError(f"decoded pixels differ from processed PNG: {runtime_final}")
        decoded.parent.mkdir(parents=True, exist_ok=True)
        decoded_image.save(decoded)
        records.append(
            {
                "kind": f"flag_{size_name}",
                "identifier": stem,
                "source": rel(source),
                "source_dimensions": source_dimensions,
                "source_sha256": sha256(source),
                "imagegen_handle": details["handle"],
                "processed": rel(processed),
                "processed_dimensions": list(expected),
                "processed_sha256": sha256(processed),
                "package_final": rel(package_final),
                "runtime_final": rel(runtime_final),
                "runtime_sha256": sha256(runtime_final),
                "validation": validation,
                "provenance": "OpenAI built-in ImageGen source; deterministic aspect fit, restrained colour finishing, detail-preserving resize, and bottom-left TGA export",
                "license": "Original generated fictional asset; no third-party source or character reference",
                "notes": details["note"],
            }
        )
    return records


def export_alias(alias: str, canonical: str, records_by_key: dict[tuple[str, str], dict[str, object]]) -> list[dict[str, object]]:
    source = SOURCE / f"{alias}_source.png"
    records = []
    for size_name, expected in SIZES.items():
        canonical_processed = path_for(PROCESSED, canonical, size_name, ".png")
        canonical_final = path_for(FINAL, canonical, size_name, ".tga")
        canonical_decoded = path_for(DECODED, canonical, size_name, ".png")
        processed = path_for(PROCESSED, alias, size_name, ".png")
        package_final = path_for(FINAL, alias, size_name, ".tga")
        runtime_final = path_for(RUNTIME, alias, size_name, ".tga")
        decoded = path_for(DECODED, alias, size_name, ".png")
        for original, target in (
            (canonical_processed, processed),
            (canonical_final, package_final),
            (canonical_final, runtime_final),
            (canonical_decoded, decoded),
        ):
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, target)
        validation = validate_tga(runtime_final, expected)
        canonical_record = records_by_key[(canonical, size_name)]
        record = dict(canonical_record)
        record.update(
            {
                "identifier": alias,
                "source": rel(source),
                "source_sha256": sha256(source),
                "processed": rel(processed),
                "processed_sha256": sha256(processed),
                "package_final": rel(package_final),
                "runtime_final": rel(runtime_final),
                "runtime_sha256": sha256(runtime_final),
                "validation": validation,
                "alias_of": canonical,
                "provenance": f"Intentional documented alias of {canonical}; source and final files are exact byte copies",
                "notes": f"Intentional unsuffixed alias of {canonical}.",
            }
        )
        records.append(record)
    return records


def expected_stems() -> list[str]:
    stems = []
    for base in ROUTE_STEMS.values():
        stems.append(base)
        stems.extend(f"{base}_{ideology}" for ideology in IDEOLOGIES)
    return stems


def validate_package(records: list[dict[str, object]]) -> dict[str, object]:
    stems = expected_stems()
    if set(stems) != set(COMPOSITIONS) | set(ALIASES):
        raise ValueError("composition and alias declarations do not cover the 25 wired stems")
    files = []
    by_key = {(str(row["identifier"]), str(row["kind"]).removeprefix("flag_")): row for row in records}
    for stem in stems:
        for size_name, expected in SIZES.items():
            row = by_key[(stem, size_name)]
            runtime = REPO / str(row["runtime_final"])
            processed = REPO / str(row["processed"])
            result = validate_tga(runtime, expected)
            with Image.open(processed) as opened:
                unique_colors = len(opened.convert("RGBA").getcolors(maxcolors=expected[0] * expected[1]) or [])
            preservation_rms = source_preservation_rms(REPO / str(row["source"]), Image.open(processed).convert("RGBA"))
            if preservation_rms > 18.0:
                raise ValueError(f"flag finishing diverged too far from the ImageGen master: {processed}: {preservation_rms}")
            files.append(
                {
                    "identifier": stem,
                    "size": size_name,
                    "path": rel(runtime),
                    "dimensions": list(expected),
                    "alpha_range": result["alpha_range"],
                    "unique_rgba_colors": unique_colors,
                    "source_preservation_rms": preservation_rms,
                    "sha256": result["sha256"],
                    "file_description": file_description(runtime),
                }
            )
    main_hashes = {str(row["identifier"]): str(row["processed_sha256"]) for row in records if row["kind"] == "flag_main"}
    independent = [main_hashes[stem] for stem in COMPOSITIONS]
    if len(set(independent)) != 21:
        raise ValueError("the 21 independent compositions do not have unique processed hashes")
    for alias, canonical in ALIASES.items():
        for size_name in SIZES:
            if by_key[(alias, size_name)]["runtime_sha256"] != by_key[(canonical, size_name)]["runtime_sha256"]:
                raise ValueError(f"alias mismatch: {alias} != {canonical} ({size_name})")
    route_distinctness = {}
    for route, base in ROUTE_STEMS.items():
        ideology_hashes = [main_hashes[f"{base}_{ideology}"] for ideology in IDEOLOGIES]
        if len(set(ideology_hashes)) != 4:
            raise ValueError(f"ideology variants are not unique for {route}")
        route_distinctness[route] = "4 of 4 ideology variants have unique processed hashes"
    validation = {
        "status": "passed",
        "source_mode": "OpenAI built-in ImageGen",
        "independent_imagegen_compositions": len(COMPOSITIONS),
        "documented_aliases": ALIASES,
        "wired_stems": len(stems),
        "runtime_tga_files": len(files),
        "imagegen_detail_preservation": "no quantization, tracing, primitive redraw, motif substitution, or palette ceiling; only aspect fit, restrained colour finishing, sharpening, and resize",
        "route_ideology_distinctness": route_distinctness,
        "checks": [
            "exact 25-stem coverage at 82x52, 41x26, and 10x7",
            "21 unique independent main-flag hashes",
            "four documented aliases are byte-identical at every size",
            "uncompressed bottom-left-origin 32-bit TGA contract",
            "decoded pixel equality with processed PNG",
            "fully opaque alpha",
            "source-to-output colour RMS remains inside the restrained finishing threshold",
            "ImageGen-authored heraldic geometry and tonal detail are retained without quantization or redraw",
            "file(1) reports no top-origin marker",
        ],
        "files": files,
    }
    validation_text = json.dumps(validation, indent=2) + "\n"
    (BASE / "flag_identity_validation_2026_07_15.json").write_text(validation_text, encoding="utf-8")
    (BASE / "ideology_flag_variant_validation.json").write_text(validation_text, encoding="utf-8")
    return validation


def fit_preview(path: Path, size: tuple[int, int]) -> Image.Image:
    with Image.open(path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def make_source_contact_sheet() -> None:
    stems = list(COMPOSITIONS)
    columns = 3
    cell_width, cell_height = 460, 330
    rows = (len(stems) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (30, 32, 34))
    draw = ImageDraw.Draw(sheet)
    label_font = font(14)
    for index, stem in enumerate(stems):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        sheet.paste(fit_preview(SOURCE / f"{stem}_source.png", (420, 266)), (x + 20, y + 16))
        draw.text((x + 20, y + 292), stem.replace("UTOPIA_MANIFESTO_", ""), font=label_font, fill=(235, 235, 232))
    output = CONTACT / "flags_corrected_imagegen_source_contact_sheet.png"
    sheet.save(output)
    shutil.copyfile(output, CONTACT / "ideology_flag_variants_source_contact_sheet.png")


def make_decoded_contact_sheet(stems: list[str]) -> None:
    columns = 5
    cell_width, cell_height = 300, 190
    rows = (len(stems) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (44, 46, 48))
    draw = ImageDraw.Draw(sheet)
    label_font = font(11)
    for index, stem in enumerate(stems):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        with Image.open(DECODED / f"{stem}.png") as opened:
            flag = opened.convert("RGB").resize((246, 156), Image.Resampling.NEAREST)
        sheet.paste(flag, (x + 27, y + 8))
        draw.text((x + 6, y + 169), stem.replace("UTOPIA_MANIFESTO_", ""), font=label_font, fill=(235, 235, 232))
    output = CONTACT / "flags_corrected_decoded_contact_sheet.png"
    sheet.save(output)
    shutil.copyfile(output, CONTACT / "flags_decoded_contact_sheet.png")
    shutil.copyfile(output, CONTACT / "ideology_flag_variants_decoded_contact_sheet.png")


def make_size_ladder(stems: list[str]) -> None:
    width, row_height = 760, 150
    sheet = Image.new("RGB", (width, row_height * len(stems)), (44, 46, 48))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    size_font = font(12)
    for index, stem in enumerate(stems):
        y = index * row_height
        draw.text((12, y + 8), stem.replace("UTOPIA_MANIFESTO_", ""), font=label_font, fill=(240, 240, 236))
        placements = {
            "main": (20, 36, 2),
            "medium": (280, 36, 4),
            "small": (535, 48, 10),
        }
        for size_name, (x, image_y, scale) in placements.items():
            source = path_for(DECODED, stem, size_name, ".png")
            with Image.open(source) as opened:
                flag = opened.convert("RGB")
            shown = flag.resize((flag.width * scale, flag.height * scale), Image.Resampling.NEAREST)
            sheet.paste(shown, (x, y + image_y))
            draw.text((x, y + 132), f"{size_name}: {flag.width}x{flag.height}", font=size_font, fill=(190, 196, 198))
        draw.line((0, y + row_height - 1, width, y + row_height - 1), fill=(72, 75, 78), width=1)
    output = CONTACT / "flag_size_ladder_decoded_contact_sheet.png"
    sheet.save(output)
    shutil.copyfile(output, CONTACT / "ideology_flag_variants_size_ladder_decoded_contact_sheet.png")


def make_source_size_comparison(stems: list[str]) -> None:
    columns = 2
    cell_width, cell_height = 680, 210
    rows = (len(stems) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (38, 40, 42))
    draw = ImageDraw.Draw(sheet)
    label_font = font(11)
    size_font = font(10)
    for index, stem in enumerate(stems):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        source = fit_preview(SOURCE / f"{stem}_source.png", (205, 130))
        sheet.paste(source, (x + 10, y + 28))
        draw.text((x + 10, y + 8), stem.replace("UTOPIA_MANIFESTO_", ""), font=label_font, fill=(240, 240, 236))
        draw.text((x + 10, y + 164), "ImageGen source", font=size_font, fill=(188, 194, 196))
        placements = {
            "main": (230, 40, 2),
            "medium": (410, 52, 3),
            "small": (550, 58, 10),
        }
        for size_name, (image_x, image_y, scale) in placements.items():
            with Image.open(path_for(DECODED, stem, size_name, ".png")) as opened:
                flag = opened.convert("RGB")
            shown = flag.resize((flag.width * scale, flag.height * scale), Image.Resampling.NEAREST)
            sheet.paste(shown, (x + image_x, y + image_y))
            draw.text((x + image_x, y + 164), f"{size_name} {flag.width}x{flag.height}", font=size_font, fill=(188, 194, 196))
        draw.line((x, y + cell_height - 1, x + cell_width, y + cell_height - 1), fill=(72, 75, 78), width=1)
    sheet.save(CONTACT / "flag_imagegen_source_normal_medium_small_comparison.png")


def make_small_readability_sheet(stems: list[str]) -> None:
    columns = 5
    cell_width, cell_height = 260, 175
    rows = (len(stems) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (44, 46, 48))
    draw = ImageDraw.Draw(sheet)
    label_font = font(11)
    for index, stem in enumerate(stems):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        with Image.open(DECODED / "small" / f"{stem}.png") as opened:
            flag = opened.convert("RGB").resize((200, 140), Image.Resampling.NEAREST)
        sheet.paste(flag, (x + 30, y + 8))
        draw.text((x + 6, y + 153), stem.replace("UTOPIA_MANIFESTO_", ""), font=label_font, fill=(235, 235, 232))
    sheet.save(CONTACT / "flags_corrected_small_10x7_readability_contact_sheet.png")


def write_records(records: list[dict[str, object]]) -> None:
    (BASE / "flag_identity_asset_records.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    lines = [f"{row['runtime_sha256']}  {row['runtime_final']}" for row in records]
    ledger = "\n".join(lines) + "\n"
    (BASE / "flag_identity_checksums.sha256").write_text(ledger, encoding="utf-8")
    (BASE / "ideology_flag_variant_checksums.sha256").write_text(ledger, encoding="utf-8")


def merge_shared_records(records: list[dict[str, object]]) -> None:
    path = BASE / "asset_records.json"
    existing = json.loads(path.read_text(encoding="utf-8"))
    identifiers = set(expected_stems())
    remaining = [row for row in existing if row.get("identifier") not in identifiers]
    first_non_flag = next(
        (index for index, row in enumerate(remaining) if not str(row.get("kind", "")).startswith("flag_")),
        len(remaining),
    )
    merged = remaining[:first_non_flag] + records + remaining[first_non_flag:]
    path.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--merge-shared-records", action="store_true", help="Replace only the 25 Event 015 flag identifiers in asset_records.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_directories()
    copy_alias_sources()
    records = []
    for stem, details in COMPOSITIONS.items():
        records.extend(export_composition(stem, details))
    records_by_key = {(str(row["identifier"]), str(row["kind"]).removeprefix("flag_")): row for row in records}
    for alias, canonical in ALIASES.items():
        records.extend(export_alias(alias, canonical, records_by_key))
    validation = validate_package(records)
    write_records(records)
    stems = expected_stems()
    make_source_contact_sheet()
    make_decoded_contact_sheet(stems)
    make_small_readability_sheet(stems)
    make_size_ladder(stems)
    make_source_size_comparison(stems)
    if args.merge_shared_records:
        merge_shared_records(records)
    print(
        f"Built {len(COMPOSITIONS)} ImageGen compositions plus {len(ALIASES)} aliases; "
        f"validated {validation['runtime_tga_files']} runtime TGAs."
    )


if __name__ == "__main__":
    main()
