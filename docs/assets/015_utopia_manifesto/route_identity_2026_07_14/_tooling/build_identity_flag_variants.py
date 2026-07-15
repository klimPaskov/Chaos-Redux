#!/usr/bin/env python3
"""Finish and validate the corrected Event 015 cosmetic flag package.

Every independent composition consumed here is an OpenAI ImageGen source PNG.
This script performs deterministic solid-fill normalization, crop/resize,
bottom-left-origin TGA export, decoded review output, contact-sheet assembly,
checksum recording, and optional targeted merging into ``asset_records.json``.
It never draws substitute motifs or creates palette-swap compositions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import struct
import subprocess
from collections import Counter
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


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
        "handle": "exec-d221430b-6b27-4ee3-86d9-ce9b79ef8471",
        "note": "Five equal households gather around a shared sprouting table.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism": {
        "handle": "exec-637487dd-a5a2-4ffd-98e3-e5095026979a",
        "note": "Household roofs, grain, and a broad common table form one shared foundation.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality": {
        "handle": "exec-e2e2e1b7-94f4-42a7-8dec-2dc2b8d4a7dc",
        "note": "Households shelter a central sprout within a balanced diamond.",
    },
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism": {
        "handle": "exec-4bfd5bd2-6634-4f2b-b06a-27a81723c8d7",
        "note": "A dominant household and two lesser roofs stand inside rigid command braces.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_democratic": {
        "handle": "exec-166408fb-5532-49a1-98a9-7931534ce029",
        "note": "Tools and wheat open around a round deliberative table.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_communism": {
        "handle": "exec-a213e972-6856-429d-9b8d-a47a37d6ac06",
        "note": "Four equal callings face inward around a common round table.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality": {
        "handle": "exec-18384790-b692-41fc-82f8-2c3caba11393",
        "note": "Six registered callings occupy two measured rows around a central mark.",
    },
    "UTOPIA_MANIFESTO_COUNCIL_UNION_fascism": {
        "handle": "exec-d90ef2e5-098f-44c9-8ed8-893d4052cb73",
        "note": "Regimented tools rise behind a sharp command chevron.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic": {
        "handle": "exec-eabafa44-47d8-45c9-98de-7a8a0fbedde2",
        "note": "A drafting divider spans three equal open civic frames.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism": {
        "handle": "exec-6bb7fe09-3064-4e3a-9a82-9a8c1d1770a2",
        "note": "A drafting divider measures five equal work nodes on a common planning table.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality": {
        "handle": "exec-456c432e-2b37-4ae7-a380-52d7733a500c",
        "note": "A single drafting divider is registered to one square and two measured guide lines.",
    },
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism": {
        "handle": "exec-51695f4d-df59-4963-9802-28b774cc60d3",
        "note": "A drafting divider is locked into a strict vertical measurement monument.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic": {
        "handle": "exec-a2424d89-6954-42f7-bb42-7ff1e047be13",
        "note": "An island remains open through separated gateways and a civic bridge.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_communism": {
        "handle": "exec-9ebdee8a-a027-4499-aa3e-8b737e0c145e",
        "note": "An island rests inside equal boundary segments joined to one foundation.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality": {
        "handle": "exec-91acc487-c80c-4436-a40c-330d7c2a1609",
        "note": "An island sits between balanced half-rings and a controlled causeway.",
    },
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism": {
        "handle": "exec-d3bea27e-81b9-4edb-990d-4f1e8cd5a674",
        "note": "An island is enclosed by a hard ring and four inward locking teeth.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH": {
        "handle": "exec-912fb135-9772-4900-acce-20bc32f1fc66",
        "note": "A handshake and sprout sit beneath two broad civic arches.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_democratic": {
        "handle": "exec-74a82e3c-4309-4148-b459-1c2dbf753ecb",
        "note": "Three open arches share a civic lamp above a turquoise bridge.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_communism": {
        "handle": "exec-acee6c41-999a-403f-bd38-07c60ea9691e",
        "note": "Four delegates share one table, doorway, and civic lamp.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_neutrality": {
        "handle": "exec-5bc343f9-6007-4b76-9943-1de4da3c7802",
        "note": "Crossed civic bands carry a central service light over a practical bridge.",
    },
    "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_fascism": {
        "handle": "exec-4e4f5847-f124-4dcb-9ab2-798e90a69bbd",
        "note": "A broken enclosure channels one streetlight and path through ordered blocks.",
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


def flatten_to_size(image: Image.Image, size: tuple[int, int], colors: int) -> Image.Image:
    fitted = ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGB")
    quantized = fitted.quantize(
        colors=colors,
        method=Image.Quantize.MAXCOVERAGE,
        dither=Image.Dither.NONE,
    ).convert("RGB")
    # Collapse low-level generated background shading to the modal border fill.
    border = []
    width, height = quantized.size
    for x in range(width):
        border.extend((quantized.getpixel((x, 0)), quantized.getpixel((x, height - 1))))
    for y in range(height):
        border.extend((quantized.getpixel((0, y)), quantized.getpixel((width - 1, y))))
    background = Counter(border).most_common(1)[0][0]
    pixels = list(quantized.getdata())
    collapsed = []
    for pixel in pixels:
        distance = sum((int(pixel[index]) - int(background[index])) ** 2 for index in range(3)) ** 0.5
        collapsed.append(background if distance < 48 else pixel)
    quantized.putdata(collapsed)
    return quantized.convert("RGBA")


def process_source(source: Path) -> dict[str, Image.Image]:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
    return {
        "main": flatten_to_size(image, SIZES["main"], 6),
        "medium": flatten_to_size(image, SIZES["medium"], 6),
        "small": flatten_to_size(image, SIZES["small"], 5),
    }


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
                "provenance": "OpenAI built-in ImageGen source; deterministic flat-fill normalization, crop/resize, and bottom-left TGA export",
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
                palette = opened.convert("RGBA").getcolors(maxcolors=256)
            if palette is None:
                raise ValueError(f"processed flag exceeds the flat-palette review ceiling: {processed}")
            unique_colors = len(palette)
            ceiling = 5 if size_name == "small" else 6
            if unique_colors > ceiling:
                raise ValueError(f"processed flag has {unique_colors} colors; expected at most {ceiling}: {processed}")
            files.append(
                {
                    "identifier": stem,
                    "size": size_name,
                    "path": rel(runtime),
                    "dimensions": list(expected),
                    "alpha_range": result["alpha_range"],
                    "unique_solid_colors": unique_colors,
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
        "solid_fill_normalization": "maximum six colors, no dithering; low-level border shading collapsed",
        "route_ideology_distinctness": route_distinctness,
        "checks": [
            "exact 25-stem coverage at 82x52, 41x26, and 10x7",
            "21 unique independent main-flag hashes",
            "four documented aliases are byte-identical at every size",
            "uncompressed bottom-left-origin 32-bit TGA contract",
            "decoded pixel equality with processed PNG",
            "fully opaque alpha",
            "maximum six solid colors without dithering (five at 10x7)",
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
    if args.merge_shared_records:
        merge_shared_records(records)
    print(
        f"Built {len(COMPOSITIONS)} ImageGen compositions plus {len(ALIASES)} aliases; "
        f"validated {validation['runtime_tga_files']} runtime TGAs."
    )


if __name__ == "__main__":
    main()
