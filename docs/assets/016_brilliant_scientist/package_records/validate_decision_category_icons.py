"""Technical validation for the Event 016 decision/category icon package."""
from __future__ import annotations

import csv
import hashlib
import json
import struct
from pathlib import Path

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[4]
RECORDS = ROOT / "docs/assets/016_brilliant_scientist/package_records"
VALIDATION = ROOT / "docs/assets/016_brilliant_scientist/validation/decision_category_icon_validation_detailed.tsv"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()


def header(path: Path) -> dict[str, int]:
    raw = path.read_bytes()
    if raw[:4] != b"DDS ":
        raise AssertionError(f"{path}: missing DDS magic")
    if len(raw) < 128:
        raise AssertionError(f"{path}: short header")
    size, flags, height, width, pitch = struct.unpack_from("<5I", raw, 4)
    if size != 124:
        raise AssertionError(f"{path}: header size {size}")
    pf_size, pf_flags, fourcc, rgb_bits, rmask, gmask, bmask, amask = struct.unpack_from("<8I", raw, 76)
    caps = struct.unpack_from("<I", raw, 108)[0]
    expected_masks = (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    if (pf_size, pf_flags, fourcc, rgb_bits, rmask, gmask, bmask, amask) != (32, 65, 0, 32, *expected_masks):
        raise AssertionError(f"{path}: unexpected DDS pixel format")
    if caps & 0x1000 == 0:
        raise AssertionError(f"{path}: missing DDSCAPS_TEXTURE")
    if pitch != width * 4:
        raise AssertionError(f"{path}: pitch {pitch} != {width * 4}")
    if len(raw) != 128 + width * height * 4:
        raise AssertionError(f"{path}: length {len(raw)} != {128 + width * height * 4}")
    return {"width": width, "height": height, "pitch": pitch, "length": len(raw)}


def main() -> None:
    manifest = json.loads((RECORDS / "decision_category_icon_manifest.json").read_text(encoding="utf-8"))
    assets = manifest["assets"]
    if len([a for a in assets if a["type"] == "decision"]) != 40:
        raise AssertionError("decision asset count is not 40")
    if len([a for a in assets if a["type"] == "decision_category"]) != 10:
        raise AssertionError("category asset count is not 10")
    source_hashes = [a["source_sha256"] for a in assets]
    if len(set(source_hashes)) != len(source_hashes):
        raise AssertionError("source masters are not unique")
    decision_ledger = list(csv.DictReader((RECORDS / "decision_assignment_ledger.tsv").open(encoding="utf-8"), delimiter="\t"))
    category_ledger = list(csv.DictReader((RECORDS / "decision_category_assignment_ledger.tsv").open(encoding="utf-8"), delimiter="\t"))
    if len(decision_ledger) != 134:
        raise AssertionError(f"decision ledger rows {len(decision_ledger)} != 134")
    if len({r["decision_or_mission_id"] for r in decision_ledger}) != 134:
        raise AssertionError("duplicate decision/mission assignment")
    if len(category_ledger) != 10 or len({r["category_id"] for r in category_ledger}) != 10:
        raise AssertionError("category ledger does not cover 10 unique categories")
    sprite_names = {a["sprite"] for a in assets if a["type"] == "decision"}
    if {r["sprite_identifier"] for r in decision_ledger} != sprite_names:
        raise AssertionError("orphan or unknown decision sprite in assignment ledger")
    category_sprite_names = {a["sprite"] for a in assets if a["type"] == "decision_category"}
    if {r["sprite_identifier"] for r in category_ledger} != category_sprite_names:
        raise AssertionError("orphan or unknown decision-category sprite in assignment ledger")
    rows = []
    for asset in assets:
        source = ROOT / asset["source"]
        processed = ROOT / asset["processed"]
        runtime = ROOT / asset["runtime"]
        if sha256(source) != asset["source_sha256"] or sha256(processed) != asset["processed_sha256"] or sha256(runtime) != asset["runtime_sha256"]:
            raise AssertionError(f"hash drift for {asset['name']}")
        w, h = (32, 32) if asset["type"] == "decision" else (50, 40)
        image = Image.open(processed).convert("RGBA")
        if image.size != (w, h):
            raise AssertionError(f"{asset['name']}: processed size {image.size}")
        alpha = image.getchannel("A")
        if alpha.getextrema()[0] != 0 or alpha.getextrema()[1] != 255:
            raise AssertionError(f"{asset['name']}: alpha range {alpha.getextrema()}")
        if any(alpha.getpixel(p) != 0 for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]):
            raise AssertionError(f"{asset['name']}: non-transparent corner")
        info = header(runtime)
        decoded = Image.open(runtime).convert("RGBA")
        if decoded.size != image.size or ImageChops.difference(decoded, image).getbbox() is not None:
            raise AssertionError(f"{asset['name']}: DDS decode differs from processed PNG")
        rows.append([asset["type"], asset["name"], w, h, alpha.getextrema()[0], alpha.getextrema()[1], info["length"], 128 + w * h * 4, asset["source_sha256"], asset["processed_sha256"], asset["runtime_sha256"], "ok"])
    with VALIDATION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["type", "name", "width", "height", "alpha_min", "alpha_max", "dds_length", "expected_length", "source_sha256", "processed_sha256", "runtime_sha256", "status"])
        writer.writerows(rows)
    print(json.dumps({"assets": len(rows), "decisions": 40, "categories": 10, "assignment_rows": 134, "category_assignment_rows": 10, "status": "ok"}, indent=2))


if __name__ == "__main__":
    main()
