"""Validate Event 016 qualifying-defeat aftermath icon package."""
from __future__ import annotations

import csv
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "docs/assets/016_brilliant_scientist/aftermath_decision_icons"
RECORDS = BASE / "package_records"
MANIFEST = RECORDS / "aftermath_decision_category_manifest.json"
REPORT = BASE / "validation/aftermath_validation_report.json"
DETAILS = BASE / "validation/aftermath_validation_details.tsv"

DECISION_SIZE = (32, 32)
CATEGORY_SIZE = (50, 40)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def rel_path(value: str) -> Path:
    return ROOT / Path(value)


def check_dds(path: Path, size: tuple[int, int]) -> bytes:
    data = path.read_bytes()
    if data[:4] != b"DDS ":
        raise AssertionError(f"{path}: missing DDS magic")
    if len(data) != 128 + size[0] * size[1] * 4:
        raise AssertionError(f"{path}: unexpected RGBA DDS length {len(data)}")
    header_size, flags, height, width, pitch = struct.unpack_from("<IIIII", data, 4)
    if (header_size, width, height, pitch) != (124, size[0], size[1], size[0] * 4):
        raise AssertionError(f"{path}: header dimensions/pitch mismatch")
    pf = struct.unpack_from("<IIIIIIII", data, 76)
    if pf != (32, 65, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000):
        raise AssertionError(f"{path}: expected uncompressed BGRA DDS pixel format, got {pf}")
    caps = struct.unpack_from("<I", data, 108)[0]
    if not caps & 0x1000:
        raise AssertionError(f"{path}: DDS_TEXTURE cap absent")
    return data


def check_png(path: Path, size: tuple[int, int], require_full_alpha: bool = True) -> Image.Image:
    image = Image.open(path).convert("RGBA")
    if image.size != size:
        raise AssertionError(f"{path}: expected {size}, got {image.size}")
    extrema = image.getchannel("A").getextrema()
    if extrema[0] != 0 or (require_full_alpha and extrema[1] != 255):
        raise AssertionError(f"{path}: alpha extrema must be (0, 255), got {extrema}")
    corners = [(0, 0), (size[0] - 1, 0), (0, size[1] - 1), (size[0] - 1, size[1] - 1)]
    if require_full_alpha and any(image.getpixel(point)[3] != 0 for point in corners):
        raise AssertionError(f"{path}: all four corners must be transparent")
    return image


def read_ledger(path: Path, id_column: str, sprite_column: str) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows or id_column not in rows[0] or sprite_column not in rows[0]:
        raise AssertionError(f"{path}: malformed ledger")
    return rows


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assets = manifest["assets"]
    decisions = [asset for asset in assets if asset["type"] == "decision"]
    categories = [asset for asset in assets if asset["type"] == "decision_category"]
    if len(decisions) != 22 or len(categories) != 4:
        raise AssertionError(f"manifest counts are {len(decisions)} decisions and {len(categories)} categories")
    if manifest.get("decision_count") != 22 or manifest.get("category_count") != 4:
        raise AssertionError("manifest declared counts are not 22/4")

    decision_ledger = read_ledger(RECORDS / "aftermath_assignment_ledger.tsv", "decision_id_or_role", "sprite_identifier")
    category_ledger = read_ledger(RECORDS / "aftermath_category_assignment_ledger.tsv", "category_role", "sprite_identifier")
    if len(decision_ledger) != 22 or len(category_ledger) != 4:
        raise AssertionError("assignment ledgers do not contain exactly 22/4 rows")
    if len({row["decision_id_or_role"] for row in decision_ledger}) != 22:
        raise AssertionError("decision ledger IDs are not unique")
    if len({row["category_role"] for row in category_ledger}) != 4:
        raise AssertionError("category ledger roles are not unique")
    if {row["sprite_identifier"] for row in decision_ledger} != {asset["sprite"] for asset in decisions}:
        raise AssertionError("decision ledger and manifest sprite identifiers differ")
    if {row["sprite_identifier"] for row in category_ledger} != {asset["sprite"] for asset in categories}:
        raise AssertionError("category ledger and manifest sprite identifiers differ")

    seen_source_hashes: set[str] = set()
    details: list[list[str]] = []
    for asset in assets:
        size = tuple(int(value) for value in asset["size"].split("x"))
        expected_size = DECISION_SIZE if asset["type"] == "decision" else CATEGORY_SIZE
        if size != expected_size:
            raise AssertionError(f"{asset['name']}: manifest size mismatch")
        source = rel_path(asset["source"])
        alpha = rel_path(asset["alpha"])
        processed = rel_path(asset["processed"])
        runtime = rel_path(asset["runtime"])
        decoded = rel_path(asset["decoded"])
        for path in (source, alpha, processed, runtime, decoded):
            if not path.is_file():
                raise AssertionError(f"{asset['name']}: missing {path}")
        source_hash = sha(source)
        if source_hash != asset["source_sha256"]:
            raise AssertionError(f"{asset['name']}: source hash mismatch")
        if source_hash in seen_source_hashes:
            raise AssertionError(f"{asset['name']}: duplicate source hash")
        seen_source_hashes.add(source_hash)
        processed_hash = sha(processed)
        runtime_hash = sha(runtime)
        if processed_hash != asset["processed_sha256"] or runtime_hash != asset["runtime_sha256"]:
            raise AssertionError(f"{asset['name']}: processed/runtime hash mismatch")
        processed_image = check_png(processed, expected_size)
        check_png(alpha, Image.open(alpha).size, require_full_alpha=False)
        check_dds(runtime, expected_size)
        decoded_image = check_png(decoded, expected_size)
        if ImageChops.difference(processed_image, decoded_image).getbbox() is not None:
            raise AssertionError(f"{asset['name']}: decoded DDS differs from processed PNG")
        details.append([asset["type"], asset["name"], asset["sprite"], asset["size"], source_hash, processed_hash, runtime_hash, "ok"])

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    report = {"assets": len(assets), "decisions": len(decisions), "categories": len(categories), "assignment_rows": len(decision_ledger), "category_assignment_rows": len(category_ledger), "status": "ok"}
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    with DETAILS.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["type", "name", "sprite", "size", "source_sha256", "processed_sha256", "runtime_sha256", "status"])
        writer.writerows(details)
    print(json.dumps(report))


if __name__ == "__main__":
    main()
