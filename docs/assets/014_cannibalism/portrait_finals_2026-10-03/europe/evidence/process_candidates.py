"""Reproducibly crop and resize the native ImageGen portrait candidates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_png"
PROCESSED = ROOT / "processed_png"
EVIDENCE = ROOT / "evidence"
REVIEW = ROOT / "review"
TARGET = (156, 210)
RESAMPLING = Image.Resampling.LANCZOS

PORTRAITS = [
    ("CBA", "leader_CBA_warlord_europe_v02", "leader_CBA_warlord_europe_candidate_v02.png"),
    ("CBB", "leader_CBB_warlord_europe", "leader_CBB_warlord_europe_source.png"),
    ("CBC", "leader_CBC_warlord", "leader_CBC_warlord_source.png"),
    ("CBD", "leader_CBD_warlord_europe", "leader_CBD_warlord_europe_source.png"),
    ("CBE", "leader_CBE_warlord", "leader_CBE_warlord_source.png"),
    ("CBF", "leader_CBF_warlord", "leader_CBF_warlord_source.png"),
    ("CBG", "leader_CBG_warlord_europe", "leader_CBG_warlord_europe_source.png"),
    ("CBH", "leader_CBH_warlord", "leader_CBH_warlord_source.png"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def centered_crop_box(width: int, height: int) -> tuple[int, int, int, int]:
    target_ratio = TARGET[0] / TARGET[1]
    if width / height < target_ratio:
        crop_height = round(width / target_ratio)
        top = (height - crop_height) // 2
        return (0, top, width, top + crop_height)
    crop_width = round(height * target_ratio)
    left = (width - crop_width) // 2
    return (left, 0, left + crop_width, height)


def make_sheets() -> None:
    native_cell = TARGET
    native_sheet = Image.new("RGB", (native_cell[0] * 4, native_cell[1] * 2), (52, 52, 52))
    draw = ImageDraw.Draw(native_sheet)
    for index, (slot, stem, source_name) in enumerate(PORTRAITS):
        x = (index % 4) * native_cell[0]
        y = (index // 4) * native_cell[1]
        processed = PROCESSED / f"{stem}_156x210.png"
        if processed.exists():
            with Image.open(processed) as image:
                native_sheet.paste(image.convert("RGB"), (x, y))
        else:
            draw.multiline_text((x + 12, y + 82), f"{slot}\nBLOCKED", fill=(235, 225, 205), font=ImageFont.load_default(), spacing=5)

    native_path = REVIEW / "europe_native_4x2_contact_sheet_v03.png"
    native_sheet.save(native_path, format="PNG", optimize=False)
    enlarged = native_sheet.resize((native_sheet.width * 4, native_sheet.height * 4), Image.Resampling.NEAREST)
    enlarged.save(REVIEW / "europe_nearest4_4x2_contact_sheet_v03.png", format="PNG", optimize=False)
    (REVIEW / "contact_sheet_order_v03.txt").write_text(
        "Grid order, left to right then top to bottom: CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH.\n"
        "CBA is a blocked review cell and has no portrait pixels. All other cells are exact 156x210 processed PNGs.\n",
        encoding="utf-8",
    )


def main() -> None:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    for slot, stem, source_name in PORTRAITS:
        if source_name is None:
            continue
        source_path = SOURCE / source_name
        processed_path = PROCESSED / f"{stem}_156x210.png"
        if processed_path.exists():
            print(f"Preserved existing candidate PNG: {processed_path}")
            continue
        with Image.open(source_path) as opened:
            source = opened.convert("RGB")
        width, height = source.size
        box = centered_crop_box(width, height)
        crop = source.crop(box)
        crop_path = PROCESSED / f"{stem}_source_crop.png"
        crop.save(crop_path, format="PNG", optimize=False)
        resized = crop.resize(TARGET, RESAMPLING)
        resized.save(processed_path, format="PNG", optimize=False)
        record = {
            "slot": slot,
            "candidate_id": "CBA-v02" if slot == "CBA" else f"{slot}-v01",
            "source_mode": "fictional_high_chaos; built-in native ImageGen",
            "source_path": str(source_path.relative_to(ROOT)).replace("\\", "/"),
            "source_sha256": sha256(source_path),
            "source_dimensions": [width, height],
            "source_mode": "RGB",
            "background": "opaque full-canvas; no alpha generation or transparency removal",
            "crop_box_left_top_right_bottom": list(box),
            "crop_dimensions": list(crop.size),
            "crop_path": str(crop_path.relative_to(ROOT)).replace("\\", "/"),
            "crop_sha256": sha256(crop_path),
            "target_dimensions": list(TARGET),
            "resampling": "Pillow Image.Resampling.LANCZOS",
            "processed_path": str(processed_path.relative_to(ROOT)).replace("\\", "/"),
            "processed_sha256": sha256(processed_path),
            "processed_mode": "RGB",
            "candidate_only": True,
        }
        (EVIDENCE / f"{slot}_crop.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    make_sheets()


if __name__ == "__main__":
    main()
