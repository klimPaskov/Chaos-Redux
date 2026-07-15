#!/usr/bin/env python3
"""Rebuild the aggregate Event 015 route-identity validation ledger."""

from __future__ import annotations

import hashlib
import json
import struct
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


REPO = Path(__file__).resolve().parents[5]
BASE = REPO / "docs/assets/015_utopia_manifesto/route_identity_2026_07_14"
FILE_EXE = Path(r"C:/Program Files/Git/usr/bin/file.exe")

ROUTES = {
    "voluntary_commonwealth": "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH",
    "council_union": "UTOPIA_MANIFESTO_COUNCIL_UNION",
    "planned_utopia": "UTOPIA_MANIFESTO_PLANNED_UTOPIA",
    "closed_island": "UTOPIA_MANIFESTO_CLOSED_ISLAND",
    "practical_commonwealth": "UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH",
}
IDEOLOGIES = ("democratic", "communism", "neutrality", "fascism")
ALIASES = {
    "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH": "UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic",
    "UTOPIA_MANIFESTO_COUNCIL_UNION": "UTOPIA_MANIFESTO_COUNCIL_UNION_communism",
    "UTOPIA_MANIFESTO_PLANNED_UTOPIA": "UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality",
    "UTOPIA_MANIFESTO_CLOSED_ISLAND": "UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism",
}


def rel(path: Path) -> str:
    return str(path.relative_to(REPO)).replace("\\", "/")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_tga(path: Path, expected: tuple[int, int]) -> dict[str, object]:
    data = path.read_bytes()
    if len(data) < 18:
        raise ValueError(f"short TGA: {path}")
    header = struct.unpack("<BBBHHBHHHHBB", data[:18])
    id_length, color_map_type, image_type, color_map_first, color_map_length, color_map_depth, x_origin, y_origin, width, height, depth, descriptor = header
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
        and len(data) == 18 + width * height * 4
    )
    if not contract:
        raise ValueError(f"invalid bottom-left 32-bit TGA contract: {path}")
    alpha = [min(data[21::4]), max(data[21::4])]
    description = subprocess.run(
        [str(FILE_EXE), "-b", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if "Targa image data" not in description or " - top" in description:
        raise ValueError(f"unexpected file(1) description: {path}: {description}")
    with Image.open(path) as opened:
        decoded = opened.convert("RGBA")
    return {
        "dimensions": [width, height],
        "alpha_range": alpha,
        "bit_depth": depth,
        "descriptor": descriptor,
        "top_origin": False,
        "byte_length": len(data),
        "file_description": description,
        "decoded": decoded,
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
        and len(data) == 128 + width * height * 4
    )
    if not contract:
        raise ValueError(f"invalid one-level BGRA DDS contract: {path}")
    with Image.open(path) as opened:
        decoded = opened.convert("RGBA")
    extrema = decoded.getchannel("A").getextrema()
    return {
        "dimensions": [width, height],
        "alpha_range": [int(extrema[0]), int(extrema[1])],
        "byte_length": len(data),
        "decoded": decoded,
    }


def expected_flag_stems() -> list[str]:
    stems = []
    for base in ROUTES.values():
        stems.append(base)
        stems.extend(f"{base}_{ideology}" for ideology in IDEOLOGIES)
    return stems


def validate_records(records: list[dict[str, object]]) -> dict[str, object]:
    files = []
    for record in records:
        source = REPO / str(record["source"])
        processed = REPO / str(record["processed"])
        package = REPO / str(record["package_final"])
        runtime = REPO / str(record["runtime_final"])
        for path in (source, processed, package, runtime):
            if not path.is_file():
                raise FileNotFoundError(path)
        if sha256(source) != record["source_sha256"]:
            raise ValueError(f"source checksum drift: {source}")
        if sha256(processed) != record["processed_sha256"]:
            raise ValueError(f"processed checksum drift: {processed}")
        if package.read_bytes() != runtime.read_bytes():
            raise ValueError(f"package/runtime byte mismatch: {runtime}")
        runtime_hash = sha256(runtime)
        if runtime_hash != record["runtime_sha256"]:
            raise ValueError(f"runtime checksum drift: {runtime}")
        expected = tuple(int(value) for value in record["processed_dimensions"])
        kind = str(record["kind"])
        result = validate_tga(runtime, expected) if kind.startswith("flag_") else validate_dds(runtime, expected)
        with Image.open(processed) as opened:
            processed_rgba = opened.convert("RGBA")
        if ImageChops.difference(processed_rgba, result["decoded"]).getbbox() is not None:
            raise ValueError(f"decoded runtime differs from processed PNG: {runtime}")
        files.append(
            {
                "kind": "flag_tga" if kind.startswith("flag_") else f"{kind}_dds",
                "identifier": record["identifier"],
                "size": kind.removeprefix("flag_") if kind.startswith("flag_") else None,
                "path": rel(runtime),
                "dimensions": result["dimensions"],
                "alpha_range": result["alpha_range"],
                "sha256": runtime_hash,
            }
        )
    return {"files": files}


def validate_identity(records: list[dict[str, object]]) -> dict[str, object]:
    flag_main = {str(row["identifier"]): row for row in records if row["kind"] == "flag_main"}
    expected = expected_flag_stems()
    if set(flag_main) != set(expected):
        raise ValueError("main flag records do not cover exactly the 25 wired stems")
    independent = [stem for stem in expected if stem not in ALIASES]
    if len(independent) != 21 or len({flag_main[stem]["processed_sha256"] for stem in independent}) != 21:
        raise ValueError("the 21 independent flag compositions are not all distinct")
    if any(not flag_main[stem].get("imagegen_handle") for stem in independent):
        raise ValueError("an independent flag composition lacks built-in ImageGen source evidence")
    for alias, canonical in ALIASES.items():
        for kind in ("flag_main", "flag_medium", "flag_small"):
            by_identifier = {str(row["identifier"]): row for row in records if row["kind"] == kind}
            if by_identifier[alias]["runtime_sha256"] != by_identifier[canonical]["runtime_sha256"]:
                raise ValueError(f"documented flag alias differs: {alias} / {canonical} / {kind}")
    route_distinctness = {}
    for route, base in ROUTES.items():
        hashes = {flag_main[f"{base}_{ideology}"]["processed_sha256"] for ideology in IDEOLOGIES}
        if len(hashes) != 4:
            raise ValueError(f"ideology compositions are not distinct for {route}")
        route_distinctness[route] = "4 of 4 ideology variants have unique processed hashes"
    institutions = [row for row in records if row["kind"] == "institutional_portrait"]
    if len(institutions) != 4 or len({row["processed_sha256"] for row in institutions}) != 4:
        raise ValueError("institutional portrait distinctness failed")
    for row in institutions:
        if row.get("source_kind") != "collective" or not row.get("imagegen_handle"):
            raise ValueError(f"institutional source evidence is incomplete: {row['identifier']}")
        metadata = json.loads((REPO / str(row["metadata"])).read_text(encoding="utf-8"))
        if metadata.get("status") != "approved_after_visual_comparison":
            raise ValueError(f"institutional visual approval is missing: {row['identifier']}")
    advisors = [row for row in records if row["kind"] == "advisor_portrait"]
    emblems = [row for row in records if row["kind"] == "league_emblem"]
    if len(advisors) != 16 or len({row["processed_sha256"] for row in advisors}) != 16:
        raise ValueError("advisor distinctness failed")
    if len(emblems) != 5 or len({row["processed_sha256"] for row in emblems}) != 5:
        raise ValueError("league emblem distinctness failed")
    return {
        "route_ideology_families": route_distinctness,
        "flag_imagegen_compositions": "21 of 21 independently generated sources have unique processed hashes and recorded built-in handles",
        "intentional_unsuffixed_aliases": [f"{alias} -> {canonical}" for alias, canonical in ALIASES.items()],
        "institutional_portraits": "4 of 4 distinct, source-kind collective, built-in ImageGen handles recorded, vanilla comparison approval recorded",
        "advisor_portraits": "16 of 16 unique 65x67 dossier-card processed hashes",
        "league_emblems": "5 of 5 unique processed hashes",
    }


def main() -> None:
    records = json.loads((BASE / "asset_records.json").read_text(encoding="utf-8"))
    validated = validate_records(records)
    distinctness = validate_identity(records)
    files = validated["files"]
    validation = {
        "status": "passed",
        "validated_runtime_files": len(files),
        "counts": {
            "flag_tga_files": sum(1 for item in files if item["kind"] == "flag_tga"),
            "institutional_portrait_dds_files": sum(1 for item in files if item["kind"] == "institutional_portrait_dds"),
            "advisor_portrait_dds_files": sum(1 for item in files if item["kind"] == "advisor_portrait_dds"),
            "league_emblem_dds_files": sum(1 for item in files if item["kind"] == "league_emblem_dds"),
        },
        "coverage": {
            "wired_flag_stems": 25,
            "flag_sizes": ["82x52", "41x26", "10x7"],
            "independent_flag_imagegen_compositions": 21,
            "documented_flag_aliases": 4,
            "institutional_portraits": 4,
            "advisors": 16,
            "league_emblems": 5,
        },
        "distinctness": distinctness,
        "focused_validation": {
            "flags": "docs/assets/015_utopia_manifesto/route_identity_2026_07_14/flag_identity_validation_2026_07_15.json",
            "institutional_portraits": "docs/assets/015_utopia_manifesto/route_identity_2026_07_14/institutional_portrait_validation_2026_07_15.json",
            "advisors": "docs/assets/015_utopia_manifesto/route_identity_2026_07_14/advisor_validation_2026_07_15.json",
            "imagegen_source_evidence": "docs/assets/015_utopia_manifesto/route_identity_2026_07_14/imagegen_source_evidence_2026_07_15.json",
        },
        "checks": [
            "source, processed, package, and runtime checksums match the asset records",
            "package/runtime files are byte-identical",
            "runtime decodes are pixel-identical to processed PNGs",
            "all flags are uncompressed bottom-left-origin 32-bit TGA without a top-origin marker",
            "all portraits and emblems are one-level uncompressed BGRA DDS",
            "21 independent flag compositions carry built-in ImageGen evidence; only four documented aliases repeat art",
            "institutional portraits carry collective-source metadata and approved vanilla comparison sheets",
        ],
        "files": files,
    }
    (BASE / "validation.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    (BASE / "checksums.sha256").write_text(
        "\n".join(f"{item['sha256']}  {item['path']}" for item in files) + "\n",
        encoding="utf-8",
    )
    print(
        f"Validated {len(files)} runtime files: {validation['counts']['flag_tga_files']} flags, "
        f"{validation['counts']['institutional_portrait_dds_files']} institutions, "
        f"{validation['counts']['advisor_portrait_dds_files']} advisors, "
        f"{validation['counts']['league_emblem_dds_files']} emblems."
    )


if __name__ == "__main__":
    main()
