"""Reproduce the South America portrait source crops and native review sheets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
TARGET_WIDTH = 156
TARGET_HEIGHT = 210
TARGET_RATIO = TARGET_WIDTH / TARGET_HEIGHT


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def crop_box(width: int, height: int, slot: str) -> tuple[int, int, int, int]:
    if width / height > TARGET_RATIO:
        crop_width = round(height * TARGET_RATIO)
        left = (width - crop_width) // 2
        return left, 0, left + crop_width, height

    crop_height = round(width / TARGET_RATIO)
    top = 0 if slot == "CBE" else (height - crop_height) // 2
    return 0, top, width, top + crop_height


def main() -> None:
    (ROOT / "sourcecrop").mkdir(parents=True, exist_ok=True)
    (ROOT / "processed_png").mkdir(parents=True, exist_ok=True)
    (ROOT / "review").mkdir(parents=True, exist_ok=True)
    records = []
    previews = []

    for slot in SLOTS:
        stem = f"leader_{slot}_warlord_south_america"
        source = ROOT / "source_png" / f"{stem}_source.png"
        crop_path = ROOT / "sourcecrop" / f"{stem}_source_crop.png"
        processed_path = ROOT / "processed_png" / f"{stem}_156x210.png"

        with Image.open(source) as source_image:
            source_image.load()
            width, height = source_image.size
            mode = source_image.mode
            alpha_range = None
            if "A" in source_image.getbands():
                alpha_range = source_image.getchannel("A").getextrema()
                if alpha_range != (255, 255):
                    raise ValueError(f"{slot}: opaque portrait source has non-opaque alpha {alpha_range}")
            box = crop_box(width, height, slot)
            cropped = source_image.convert("RGB").crop(box)
            cropped.save(crop_path, format="PNG", optimize=False)
            preview = cropped.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
            preview.save(processed_path, format="PNG", optimize=False)
            previews.append(preview.copy())

        records.append(
            {
                "slot": slot,
                "source": source.relative_to(ROOT).as_posix(),
                "source_dimensions": [width, height],
                "source_sha256": sha256(source),
                "source_mode": mode,
                "transparent_background_requested": False,
                "source_alpha_range": list(alpha_range) if alpha_range else None,
                "crop_box_ltrb": list(box),
                "crop_dimensions": [box[2] - box[0], box[3] - box[1]],
                "crop": crop_path.relative_to(ROOT).as_posix(),
                "crop_sha256": sha256(crop_path),
                "processed_preview": processed_path.relative_to(ROOT).as_posix(),
                "processed_dimensions": [TARGET_WIDTH, TARGET_HEIGHT],
                "resize": "Pillow LANCZOS from the retained lossless RGB crop",
                "processed_sha256": sha256(processed_path),
                "crop_policy": "top-anchored for CBE to preserve the full bald scalp; maximum centered aspect crop for all other slots",
            }
        )

    native_sheet = Image.new("RGB", (TARGET_WIDTH * 4, TARGET_HEIGHT * 2), (24, 24, 24))
    nearest_sheet = Image.new("RGB", (TARGET_WIDTH * 4 * 4, TARGET_HEIGHT * 2 * 4), (24, 24, 24))
    for index, preview in enumerate(previews):
        x = (index % 4) * TARGET_WIDTH
        y = (index // 4) * TARGET_HEIGHT
        native_sheet.paste(preview, (x, y))
        enlarged = preview.resize((TARGET_WIDTH * 4, TARGET_HEIGHT * 4), Image.Resampling.NEAREST)
        nearest_sheet.paste(enlarged, (x * 4, y * 4))

    native_path = ROOT / "review" / "south_america_native_4x2_contact_sheet.png"
    nearest_path = ROOT / "review" / "south_america_nearest4_4x2_contact_sheet.png"
    native_sheet.save(native_path, format="PNG", optimize=False)
    nearest_sheet.save(nearest_path, format="PNG", optimize=False)
    (ROOT / "review" / "contact_sheet_order.txt").write_text(
        "Rows are ordered left-to-right, then top-to-bottom.\n"
        + "\n".join(f"{index + 1}. {slot}: processed_png/leader_{slot}_warlord_south_america_156x210.png" for index, slot in enumerate(SLOTS))
        + "\n",
        encoding="utf-8",
    )

    inventory = {
        "route": "one built-in native ImageGen call per portrait; deterministic crop/resize only after source review",
        "target_canvas": [TARGET_WIDTH, TARGET_HEIGHT],
        "background_mode": "consumer_opaque",
        "sources": records,
        "contact_sheets": [
            {
                "path": native_path.relative_to(ROOT).as_posix(),
                "dimensions": list(native_sheet.size),
                "sha256": sha256(native_path),
                "scale": "native 156x210 tiles",
            },
            {
                "path": nearest_path.relative_to(ROOT).as_posix(),
                "dimensions": list(nearest_sheet.size),
                "sha256": sha256(nearest_path),
                "scale": "4x nearest-neighbour per 156x210 tile",
            },
        ],
    }
    (ROOT / "metadata" / "crop_and_preview_inventory.json").write_text(
        json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
