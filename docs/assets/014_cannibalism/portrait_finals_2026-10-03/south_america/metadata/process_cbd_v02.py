"""Process the parent-requested CBD utensil edit and refresh review sheets."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
SIZE = (156, 210)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    stem = "leader_CBD_warlord_south_america"
    source = ROOT / "source_png" / f"{stem}_source_v02.png"
    crop_path = ROOT / "sourcecrop" / f"{stem}_source_crop_v02.png"
    preview_path = ROOT / "processed_png" / f"{stem}_156x210_v02.png"

    with Image.open(source) as image:
        image.load()
        if image.size != (1081, 1455):
            raise ValueError(f"CBD v02 canvas changed unexpectedly: {image.size}")
        if image.mode not in ("RGB",):
            raise ValueError(f"CBD v02 source mode is not RGB: {image.mode}")
        crop = image.copy()
        crop.save(crop_path, format="PNG", optimize=False)
        preview = crop.resize(SIZE, Image.Resampling.LANCZOS)
        preview.save(preview_path, format="PNG", optimize=False)

    base_inventory_path = ROOT / "metadata" / "crop_and_preview_inventory.json"
    inventory = json.loads(base_inventory_path.read_text(encoding="utf-8-sig"))
    rows = copy.deepcopy(inventory["sources"])
    cbd = next(row for row in rows if row["slot"] == "CBD")
    old_cbd = copy.deepcopy(cbd)
    cbd.update(
        {
            "candidate_id": "south_america_CBD_v02",
            "parent_candidate_id": "south_america_CBD_v01",
            "new_generation_reason": "Parent review rejected only v01's visibly intact field spoon and requested one narrow native edit showing the utensil mid-break.",
            "source": source.relative_to(ROOT).as_posix(),
            "source_dimensions": [1081, 1455],
            "source_sha256": sha256(source),
            "source_mode": "RGB",
            "transparent_background_requested": False,
            "source_alpha_range": None,
            "crop_box_ltrb": [0, 0, 1081, 1455],
            "crop_dimensions": [1081, 1455],
            "crop": crop_path.relative_to(ROOT).as_posix(),
            "crop_sha256": sha256(crop_path),
            "processed_preview": preview_path.relative_to(ROOT).as_posix(),
            "processed_dimensions": list(SIZE),
            "resize": "Pillow LANCZOS from the retained lossless RGB crop",
            "processed_sha256": sha256(preview_path),
            "crop_policy": "full source retained; no crop required for the 26:35 consumer ratio",
            "supersedes_candidate": old_cbd,
        }
    )

    previews = []
    for slot in SLOTS:
        if slot == "CBD":
            path = preview_path
        else:
            path = ROOT / "processed_png" / f"leader_{slot}_warlord_south_america_156x210.png"
        with Image.open(path) as image:
            image.load()
            if image.size != SIZE:
                raise ValueError(f"{slot} selected preview has wrong dimensions: {image.size}")
            previews.append(image.convert("RGB"))

    native = Image.new("RGB", (SIZE[0] * 4, SIZE[1] * 2), (24, 24, 24))
    nearest = Image.new("RGB", (SIZE[0] * 16, SIZE[1] * 8), (24, 24, 24))
    for index, preview in enumerate(previews):
        x = (index % 4) * SIZE[0]
        y = (index // 4) * SIZE[1]
        native.paste(preview, (x, y))
        nearest.paste(preview.resize((SIZE[0] * 4, SIZE[1] * 4), Image.Resampling.NEAREST), (x * 4, y * 4))

    native_path = ROOT / "review" / "south_america_native_4x2_contact_sheet_v02.png"
    nearest_path = ROOT / "review" / "south_america_nearest4_4x2_contact_sheet_v02.png"
    native.save(native_path, format="PNG", optimize=False)
    nearest.save(nearest_path, format="PNG", optimize=False)
    (ROOT / "review" / "contact_sheet_order_v02.txt").write_text(
        "Version 02 selected-source order is left-to-right, then top-to-bottom. CBD uses source v02; all other slots reuse the parent-approved v01 source preview.\n"
        + "\n".join(f"{index + 1}. {slot}" for index, slot in enumerate(SLOTS))
        + "\n",
        encoding="utf-8",
    )

    selected = {
        "route": "seven parent-approved v01 sources plus the parent-requested CBD v02 native edit",
        "target_canvas": list(SIZE),
        "background_mode": "consumer_opaque",
        "source_rows": rows,
        "contact_sheets": [
            {"path": native_path.relative_to(ROOT).as_posix(), "dimensions": list(native.size), "sha256": sha256(native_path), "scale": "native 156x210 tiles"},
            {"path": nearest_path.relative_to(ROOT).as_posix(), "dimensions": list(nearest.size), "sha256": sha256(nearest_path), "scale": "4x nearest-neighbour per tile"},
        ],
    }
    (ROOT / "metadata" / "crop_and_preview_inventory_v02.json").write_text(
        json.dumps(selected, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
