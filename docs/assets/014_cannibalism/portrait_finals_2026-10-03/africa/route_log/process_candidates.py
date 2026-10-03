"""Deterministic Event 014 Africa portrait crop, resize, and review-sheet builder."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source_png"
CROP_DIR = ROOT / "crops"
PROCESSED_DIR = ROOT / "processed_png"
REVIEW_DIR = ROOT / "review"
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
TARGET_SIZE = (156, 210)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def pixel_sha256(image: Image.Image) -> str:
    return hashlib.sha256(image.tobytes()).hexdigest().upper()


def write_new(path: Path, image: Image.Image) -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite candidate evidence: {path}")
    image.save(path, format="PNG", optimize=False)


def main() -> None:
    for folder in (CROP_DIR, PROCESSED_DIR, REVIEW_DIR):
        folder.mkdir(parents=True, exist_ok=True)

    entries = []
    processed_images = []
    for slot in SLOTS:
        basename = f"leader_{slot}_warlord_africa"
        source_path = SOURCE_DIR / f"{basename}_native.png"
        crop_path = CROP_DIR / f"{basename}_source_crop.png"
        processed_path = PROCESSED_DIR / f"{basename}_156x210.png"

        with Image.open(source_path) as opened:
            opened.load()
            if opened.mode != "RGB":
                raise ValueError(f"Expected opaque RGB native source, got {opened.mode}: {source_path}")
            source = opened.copy()

        width, height = source.size
        source_box = (0, 0, width, height)
        crop = source.crop(source_box)
        write_new(crop_path, crop)
        processed = crop.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        write_new(processed_path, processed)
        processed_images.append((slot, processed.copy()))

        entries.append(
            {
                "slot": slot,
                "source_png": source_path.relative_to(ROOT).as_posix(),
                "source_dimensions": [width, height],
                "source_mode": "RGB",
                "source_sha256": sha256(source_path),
                "source_pixel_sha256": pixel_sha256(source),
                "source_crop_png": crop_path.relative_to(ROOT).as_posix(),
                "crop_box_ltrb": list(source_box),
                "crop_dimensions": list(crop.size),
                "crop_mode": crop.mode,
                "crop_sha256": sha256(crop_path),
                "crop_pixel_sha256": pixel_sha256(crop),
                "crop_is_pixel_exact_full_source": crop.tobytes() == source.tobytes(),
                "processed_png": processed_path.relative_to(ROOT).as_posix(),
                "processed_dimensions": list(processed.size),
                "processed_mode": processed.mode,
                "resampling": "Pillow LANCZOS only",
                "processed_sha256": sha256(processed_path),
                "processed_pixel_sha256": pixel_sha256(processed),
                "background": "opaque, unchanged",
            }
        )

    native_sheet_path = REVIEW_DIR / "africa_native_4x2_contact_sheet.png"
    nearest_sheet_path = REVIEW_DIR / "africa_nearest4_4x2_contact_sheet.png"
    if native_sheet_path.exists() or nearest_sheet_path.exists():
        raise FileExistsError("Refusing to overwrite an existing Africa contact sheet")

    native_sheet = Image.new("RGB", (TARGET_SIZE[0] * 4, TARGET_SIZE[1] * 2))
    nearest_sheet = Image.new("RGB", (TARGET_SIZE[0] * 4 * 4, TARGET_SIZE[1] * 2 * 4))
    order_lines = ["Event 014 Africa portrait candidates; row-major slot order; each portrait is 156x210 RGB."]
    for index, (slot, image) in enumerate(processed_images):
        column, row = index % 4, index // 4
        native_sheet.paste(image, (column * TARGET_SIZE[0], row * TARGET_SIZE[1]))
        enlarged = image.resize((TARGET_SIZE[0] * 4, TARGET_SIZE[1] * 4), Image.Resampling.NEAREST)
        nearest_sheet.paste(enlarged, (column * TARGET_SIZE[0] * 4, row * TARGET_SIZE[1] * 4))
        order_lines.append(
            f"row {row + 1}, column {column + 1}: {slot} -> processed_png/leader_{slot}_warlord_africa_156x210.png"
        )

    native_sheet.save(native_sheet_path, format="PNG", optimize=False)
    nearest_sheet.save(nearest_sheet_path, format="PNG", optimize=False)
    order_path = REVIEW_DIR / "contact_sheet_order.txt"
    if order_path.exists():
        raise FileExistsError(f"Refusing to overwrite review order: {order_path}")
    order_path.write_text("\n".join(order_lines) + "\n", encoding="utf-8")

    audit = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "CBA-CBH Africa fictional native ImageGen candidate assets only",
        "tool": "Pillow deterministic full-source crop and LANCZOS resize; no color, paint, filter, or alpha edits",
        "target_dimensions": list(TARGET_SIZE),
        "native_contact_sheet": {
            "path": native_sheet_path.relative_to(ROOT).as_posix(),
            "dimensions": list(native_sheet.size),
            "sha256": sha256(native_sheet_path),
        },
        "nearest4_contact_sheet": {
            "path": nearest_sheet_path.relative_to(ROOT).as_posix(),
            "dimensions": list(nearest_sheet.size),
            "sha256": sha256(nearest_sheet_path),
        },
        "slots": entries,
        "distinct_processed_pixel_hashes": len({entry["processed_pixel_sha256"] for entry in entries}),
    }
    audit_path = ROOT / "route_log" / "processing_audit.json"
    if audit_path.exists():
        raise FileExistsError(f"Refusing to overwrite processing audit: {audit_path}")
    audit_path.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"audit": audit_path.as_posix(), "slots": len(entries), "unique_pixels": audit["distinct_processed_pixel_hashes"]}))


if __name__ == "__main__":
    main()
