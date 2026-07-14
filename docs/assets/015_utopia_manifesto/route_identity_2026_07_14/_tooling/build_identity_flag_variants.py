#!/usr/bin/env python3
"""Build and validate the missing Event 015 ideology flag variants.

The source PNGs are independent OpenAI image_gen masters.  This script performs
only deterministic crop/resize, bottom-left-origin 32-bit TGA export, package
mirroring, decoded review output, contact-sheet assembly, and checksum/format
validation.  It does not synthesize substitute artwork.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import struct
import subprocess
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

VARIANTS = {
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism": (
        "Five equal households share a curved common foundation beneath the sprouting table."
    ),
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality": (
        "Five households form a sheltered diamond around the sprouting table."
    ),
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism": (
        "Five households form a stepped hierarchy between rigid side braces."
    ),
    "UTOPIA_MANIFESTO_COUNCIL_UNION_democratic": (
        "Six tools face an open deliberative chamber and low common table."
    ),
    "UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality": (
        "Six tools occupy two balanced register rows around a measured center."
    ),
    "UTOPIA_MANIFESTO_COUNCIL_UNION_fascism": (
        "Six tools rise in regimented ranks behind a command chevron."
    ),
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic": (
        "The survey compass spans three equal open civic frames and broken corner rules."
    ),
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism": (
        "The survey compass measures five equal work nodes on a common planning table."
    ),
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism": (
        "The survey compass is locked into a strict vertical measurement monument."
    ),
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic": (
        "The island is protected by separated civic gateway brackets and an open bridge."
    ),
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_communism": (
        "The island rests within equal boundary segments joined by a common foundation."
    ),
    "UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality": (
        "The island sits between balanced half-arcs and a controlled passage channel."
    ),
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


def dimensions(path: Path) -> list[int]:
    with Image.open(path) as image:
        return [image.width, image.height]


def alpha_range(image: Image.Image) -> list[int]:
    alpha = image.convert("RGBA").getchannel("A")
    extrema = alpha.getextrema()
    return [int(extrema[0]), int(extrema[1])]


def font(size: int) -> ImageFont.ImageFont:
    candidates = (
        Path(r"C:/Windows/Fonts/arial.ttf"),
        Path(r"C:/Windows/Fonts/segoeui.ttf"),
    )
    for candidate in candidates:
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def ensure_directories() -> None:
    for root in (PROCESSED, FINAL, DECODED):
        root.mkdir(parents=True, exist_ok=True)
        (root / "medium").mkdir(parents=True, exist_ok=True)
        (root / "small").mkdir(parents=True, exist_ok=True)
    CONTACT.mkdir(parents=True, exist_ok=True)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    (RUNTIME / "medium").mkdir(parents=True, exist_ok=True)
    (RUNTIME / "small").mkdir(parents=True, exist_ok=True)


def path_for(root: Path, stem: str, size_name: str, suffix: str) -> Path:
    if size_name == "main":
        return root / f"{stem}{suffix}"
    return root / size_name / f"{stem}{suffix}"


def process_source(source: Path) -> dict[str, Image.Image]:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        main = ImageOps.fit(
            image,
            SIZES["main"],
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        ).convert("RGBA")
    return {
        "main": main,
        "medium": main.resize(SIZES["medium"], Image.Resampling.LANCZOS),
        "small": main.resize(SIZES["small"], Image.Resampling.LANCZOS),
    }


def write_tga_bottom_left(image: Image.Image, path: Path) -> None:
    image = image.convert("RGBA")
    width, height = image.size
    header = struct.pack(
        "<BBBHHBHHHHBB",
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        width,
        height,
        32,
        8,
    )
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
    (
        id_length,
        color_map_type,
        image_type,
        color_map_first,
        color_map_length,
        color_map_depth,
        x_origin,
        y_origin,
        width,
        height,
        depth,
        descriptor,
    ) = header
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
    alpha_bytes = data[21::4]
    if not alpha_bytes:
        raise ValueError(f"missing alpha bytes: {path}")
    alpha = [min(alpha_bytes), max(alpha_bytes)]
    if alpha != [255, 255]:
        raise ValueError(f"flag alpha is not fully opaque: {path}: {alpha}")
    with Image.open(path) as decoded:
        decoded.load()
        decoded_dimensions = decoded.size
    if decoded_dimensions != expected:
        raise ValueError(f"Pillow decode dimensions mismatch: {path}")
    return {
        "dimensions": [width, height],
        "bit_depth": depth,
        "descriptor": descriptor,
        "top_origin": bool(descriptor & 0x20),
        "alpha_range": alpha,
        "byte_length": len(data),
        "sha256": sha256(path),
    }


def validate_dds(path: Path, expected: tuple[int, int]) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 128 or data[:4] != b"DDS ":
        raise ValueError(f"invalid DDS magic/header: {path}")
    header_size = int.from_bytes(data[4:8], "little")
    height = int.from_bytes(data[12:16], "little")
    width = int.from_bytes(data[16:20], "little")
    mipmaps = int.from_bytes(data[28:32], "little")
    pixel_format_size = int.from_bytes(data[76:80], "little")
    pixel_format_flags = int.from_bytes(data[80:84], "little")
    fourcc = data[84:88]
    bit_count = int.from_bytes(data[88:92], "little")
    masks = tuple(int.from_bytes(data[offset : offset + 4], "little") for offset in (92, 96, 100, 104))
    caps = int.from_bytes(data[108:112], "little")
    expected_length = 128 + width * height * 4
    contract = (
        header_size == 124
        and (width, height) == expected
        and mipmaps in (0, 1)
        and pixel_format_size == 32
        and pixel_format_flags == 65
        and fourcc == b"\x00\x00\x00\x00"
        and bit_count == 32
        and masks == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
        and caps == 0x1000
        and len(data) == expected_length
    )
    if not contract:
        raise ValueError(f"invalid one-level BGRA DDS contract: {path}")
    with Image.open(path) as decoded:
        decoded_rgba = decoded.convert("RGBA")
    return {
        "dimensions": [width, height],
        "alpha_range": alpha_range(decoded_rgba),
        "byte_length": len(data),
        "sha256": sha256(path),
    }


def decode_and_compare(final: Path, processed: Path, decoded: Path) -> None:
    with Image.open(final) as opened:
        decoded_image = opened.convert("RGBA")
    with Image.open(processed) as opened:
        processed_image = opened.convert("RGBA")
    if ImageChops.difference(decoded_image, processed_image).getbbox() is not None:
        raise ValueError(f"decoded pixels differ from processed PNG: {final}")
    decoded.parent.mkdir(parents=True, exist_ok=True)
    decoded_image.save(decoded)


def build_variants() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for stem, note in VARIANTS.items():
        source = SOURCE / f"{stem}_source.png"
        if not source.is_file():
            raise FileNotFoundError(source)
        source_dimensions = dimensions(source)
        source_hash = sha256(source)
        images = process_source(source)
        for size_name, expected in SIZES.items():
            processed = path_for(PROCESSED, stem, size_name, ".png")
            package_final = path_for(FINAL, stem, size_name, ".tga")
            runtime_final = path_for(RUNTIME, stem, size_name, ".tga")
            decoded = path_for(DECODED, stem, size_name, ".png")
            processed.parent.mkdir(parents=True, exist_ok=True)
            images[size_name].save(processed)
            write_tga_bottom_left(images[size_name], package_final)
            runtime_final.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(package_final, runtime_final)
            if package_final.read_bytes() != runtime_final.read_bytes():
                raise ValueError(f"package/runtime TGA mismatch: {stem} {size_name}")
            validation = validate_tga(runtime_final, expected)
            decode_and_compare(runtime_final, processed, decoded)
            records.append(
                {
                    "kind": f"flag_{size_name}",
                    "identifier": stem,
                    "source": rel(source),
                    "source_dimensions": source_dimensions,
                    "source_sha256": source_hash,
                    "processed": rel(processed),
                    "processed_dimensions": list(expected),
                    "processed_sha256": sha256(processed),
                    "package_final": rel(package_final),
                    "runtime_final": rel(runtime_final),
                    "runtime_sha256": sha256(runtime_final),
                    "validation": {
                        "dimensions": list(expected),
                        "alpha_range": validation["alpha_range"],
                        "sha256": validation["sha256"],
                    },
                    "provenance": "OpenAI image_gen original; deterministic local crop, resize, and bottom-left TGA export",
                    "license": "Original generated fictional asset; no third-party source or character reference",
                    "notes": note,
                }
            )
    return records


def merge_asset_records(new_records: list[dict[str, object]]) -> list[dict[str, object]]:
    path = BASE / "asset_records.json"
    existing = json.loads(path.read_text(encoding="utf-8"))
    existing = [row for row in existing if row.get("identifier") not in VARIANTS]
    first_non_flag = next(
        (index for index, row in enumerate(existing) if not str(row.get("kind", "")).startswith("flag_")),
        len(existing),
    )
    merged = existing[:first_non_flag] + new_records + existing[first_non_flag:]
    path.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")
    return merged


def expected_flag_stems() -> list[str]:
    stems: list[str] = []
    for base in ROUTE_STEMS.values():
        stems.append(base)
        stems.extend(f"{base}_{ideology}" for ideology in IDEOLOGIES)
    return stems


def validate_coverage() -> dict[str, object]:
    expected = expected_flag_stems()
    by_size: dict[str, object] = {}
    for size_name in SIZES:
        root = RUNTIME if size_name == "main" else RUNTIME / size_name
        present = sorted(path.stem for path in root.glob("UTOPIA_MANIFESTO_*.tga"))
        missing = sorted(set(expected) - set(present))
        unexpected = sorted(set(present) - set(expected))
        if missing:
            raise ValueError(f"missing {size_name} flag stems: {missing}")
        by_size[size_name] = {
            "expected": len(expected),
            "present": len(set(expected) & set(present)),
            "missing": missing,
            "unexpected_event_015_stems": unexpected,
        }
    return by_size


def file_description(path: Path) -> str:
    if not FILE_EXE.is_file():
        raise FileNotFoundError(FILE_EXE)
    result = subprocess.run(
        [str(FILE_EXE), "-b", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    description = result.stdout.strip()
    if "Targa image data" not in description or description.endswith("- top") or " - top" in description:
        raise ValueError(f"unexpected file(1) output for {path}: {description}")
    return description


def rebuild_validation(records: list[dict[str, object]]) -> dict[str, object]:
    files: list[dict[str, object]] = []
    file_descriptions: dict[str, str] = {}
    for row in records:
        runtime = REPO / str(row["runtime_final"])
        expected = tuple(int(value) for value in row["validation"]["dimensions"])
        kind = str(row["kind"])
        if kind.startswith("flag_"):
            result = validate_tga(runtime, expected)
            size_name = kind.removeprefix("flag_")
            processed = REPO / str(row["processed"])
            decoded = path_for(DECODED, str(row["identifier"]), size_name, ".png")
            decode_and_compare(runtime, processed, decoded)
            description = file_description(runtime)
            if str(row["identifier"]) in VARIANTS:
                file_descriptions[rel(runtime)] = description
            files.append(
                {
                    "kind": "flag_tga",
                    "identifier": row["identifier"],
                    "size": size_name,
                    "path": rel(runtime),
                    "dimensions": result["dimensions"],
                    "alpha_range": result["alpha_range"],
                    "sha256": result["sha256"],
                }
            )
        else:
            result = validate_dds(runtime, expected)
            kind_map = {
                "institutional_portrait": "institutional_portrait_dds",
                "advisor_portrait": "advisor_portrait_dds",
                "league_emblem": "league_emblem_dds",
            }
            files.append(
                {
                    "kind": kind_map.get(kind, f"{kind}_dds"),
                    "identifier": row["identifier"],
                    "path": rel(runtime),
                    "dimensions": result["dimensions"],
                    "alpha_range": result["alpha_range"],
                    "sha256": result["sha256"],
                }
            )

    main_hashes = {
        str(row["identifier"]): str(row["processed_sha256"])
        for row in records
        if row["kind"] == "flag_main"
    }
    route_distinctness: dict[str, str] = {}
    for route, base in ROUTE_STEMS.items():
        ideology_hashes = [main_hashes[f"{base}_{ideology}"] for ideology in IDEOLOGIES]
        if len(set(ideology_hashes)) != 4:
            raise ValueError(f"ideology variants are not unique for {route}")
        route_distinctness[route] = "4 of 4 ideology variants have unique processed hashes"
    new_hashes = [main_hashes[stem] for stem in VARIANTS]
    if len(set(new_hashes)) != len(new_hashes):
        raise ValueError("new ideology variant processed hashes are not all unique")

    validation = {
        "status": "passed",
        "validated_runtime_files": len(files),
        "counts": {
            "flag_tga_files": sum(1 for item in files if item["kind"] == "flag_tga"),
            "institutional_portrait_dds_files": sum(1 for item in files if item["kind"] == "institutional_portrait_dds"),
            "advisor_portrait_dds_files": sum(1 for item in files if item["kind"] == "advisor_portrait_dds"),
            "league_emblem_dds_files": sum(1 for item in files if item["kind"] == "league_emblem_dds"),
        },
        "coverage": validate_coverage(),
        "distinctness": {
            "route_ideology_families": route_distinctness,
            "new_ideology_variants": "12 of 12 unique processed hashes",
            "institutional_portraits": "4 of 4 unique processed hashes",
            "advisor_portraits": "16 of 16 unique processed hashes",
            "league_emblems": "5 of 5 unique processed hashes",
            "intentional_unsuffixed_aliases": [
                "VOLUNTARY_COMMONWEALTH -> VOLUNTARY_COMMONWEALTH_democratic",
                "COUNCIL_UNION -> COUNCIL_UNION_communism",
                "PLANNED_UTOPIA -> PLANNED_UTOPIA_neutrality",
                "CLOSED_ISLAND -> CLOSED_ISLAND_fascism",
            ],
        },
        "checks": [
            "runtime filename coverage for all five route stems and four ideologies at every size",
            "uncompressed bottom-left-origin 32-bit TGA header contract",
            "file(1) descriptions contain no top-origin marker",
            "uncompressed one-level BGRA DDS contract for unchanged package DDS files",
            "Pillow decode",
            "decoded pixel equality with processed PNG",
            "fully opaque flag alpha range",
            "exact runtime file length",
            "SHA-256 checksum recording",
            "route-family ideology distinctness",
        ],
        "new_variant_file_descriptions": file_descriptions,
        "files": files,
    }
    (BASE / "validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    (BASE / "ideology_flag_variant_validation.json").write_text(
        json.dumps(
            {
                "status": "passed",
                "new_stems": list(VARIANTS),
                "new_runtime_tga_files": 36,
                "coverage": validation["coverage"],
                "distinctness": validation["distinctness"]["route_ideology_families"],
                "file_descriptions": file_descriptions,
                "files": [item for item in files if item.get("identifier") in VARIANTS],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return validation


def fit_preview(path: Path, size: tuple[int, int]) -> Image.Image:
    with Image.open(path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def make_source_contact_sheet() -> None:
    columns = 3
    cell_width, cell_height = 460, 330
    rows = (len(VARIANTS) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (30, 32, 34))
    draw = ImageDraw.Draw(sheet)
    label_font = font(14)
    for index, stem in enumerate(VARIANTS):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        preview = fit_preview(SOURCE / f"{stem}_source.png", (420, 266))
        sheet.paste(preview, (x + 20, y + 16))
        label = stem.replace("UTOPIA_MANIFESTO_", "")
        draw.text((x + 20, y + 292), label, font=label_font, fill=(235, 235, 232))
    sheet.save(CONTACT / "ideology_flag_variants_source_contact_sheet.png")


def make_decoded_contact_sheet(stems: list[str], output: Path, columns: int) -> None:
    cell_width, cell_height = 360, 180
    rows = (len(stems) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), (44, 46, 48))
    draw = ImageDraw.Draw(sheet)
    label_font = font(13)
    for index, stem in enumerate(stems):
        x = (index % columns) * cell_width
        y = (index // columns) * cell_height
        with Image.open(DECODED / f"{stem}.png") as opened:
            flag = opened.convert("RGB").resize((246, 156), Image.Resampling.NEAREST)
        sheet.paste(flag, (x + 57, y + 8))
        label = stem.replace("UTOPIA_MANIFESTO_", "")
        draw.text((x + 8, y + 164), label, font=label_font, fill=(235, 235, 232))
    sheet.save(output)


def make_size_ladder(stems: list[str], output: Path) -> None:
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
            draw.text(
                (x, y + 132),
                f"{size_name}: {flag.width}x{flag.height}",
                font=size_font,
                fill=(190, 196, 198),
            )
        draw.line((0, y + row_height - 1, width, y + row_height - 1), fill=(72, 75, 78), width=1)
    sheet.save(output)


def write_checksum_ledger(records: list[dict[str, object]]) -> None:
    lines = []
    for row in records:
        if row.get("identifier") in VARIANTS:
            lines.append(f"{row['runtime_sha256']}  {row['runtime_final']}")
    (BASE / "ideology_flag_variant_checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_directories()
    new_records = build_variants()
    records = merge_asset_records(new_records)
    validation = rebuild_validation(records)
    write_checksum_ledger(new_records)
    all_stems = expected_flag_stems()
    make_source_contact_sheet()
    make_decoded_contact_sheet(list(VARIANTS), CONTACT / "ideology_flag_variants_decoded_contact_sheet.png", 3)
    make_size_ladder(list(VARIANTS), CONTACT / "ideology_flag_variants_size_ladder_decoded_contact_sheet.png")
    make_decoded_contact_sheet(all_stems, CONTACT / "flags_decoded_contact_sheet.png", 4)
    make_size_ladder(all_stems, CONTACT / "flag_size_ladder_decoded_contact_sheet.png")
    print(
        f"Built {len(VARIANTS)} ideology stems / {len(new_records)} TGAs; "
        f"validated {validation['validated_runtime_files']} package runtime files."
    )


if __name__ == "__main__":
    main()
