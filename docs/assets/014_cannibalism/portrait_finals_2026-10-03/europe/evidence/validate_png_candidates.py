"""Record source and native-size QA facts for the selected Europe candidates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REPO = next(parent for parent in ROOT.parents if (parent / "interface/014_cannibalism.gfx").is_file())
SOURCES = ROOT / "source_png"
PROCESSED = ROOT / "processed_png"
REVIEW = ROOT / "review"
EVIDENCE = ROOT / "evidence"

ITEMS = [
    ("CBA", "leader_CBA_warlord_europe_v02", "leader_CBA_warlord_europe_candidate_v02.png", "leader_CBA_warlord_europe_v02_156x210.png"),
    ("CBB", "leader_CBB_warlord_europe", "leader_CBB_warlord_europe_source.png", "leader_CBB_warlord_europe_156x210.png"),
    ("CBC", "leader_CBC_warlord", "leader_CBC_warlord_source.png", "leader_CBC_warlord_156x210.png"),
    ("CBD", "leader_CBD_warlord_europe", "leader_CBD_warlord_europe_source.png", "leader_CBD_warlord_europe_156x210.png"),
    ("CBE", "leader_CBE_warlord", "leader_CBE_warlord_source.png", "leader_CBE_warlord_156x210.png"),
    ("CBF", "leader_CBF_warlord", "leader_CBF_warlord_source.png", "leader_CBF_warlord_156x210.png"),
    ("CBG", "leader_CBG_warlord_europe", "leader_CBG_warlord_europe_source.png", "leader_CBG_warlord_europe_156x210.png"),
    ("CBH", "leader_CBH_warlord", "leader_CBH_warlord_source.png", "leader_CBH_warlord_156x210.png"),
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes())


def main() -> None:
    records = []
    source_pixels = set()
    processed_pixels = set()
    for slot, stem, source_name, processed_name in ITEMS:
        source_path = SOURCES / source_name
        processed_path = PROCESSED / processed_name
        with Image.open(source_path) as source_image:
            source = source_image.copy()
        with Image.open(processed_path) as processed_image:
            processed = processed_image.copy()
        source_pixel_hash = sha256(source.convert("RGB").tobytes())
        processed_pixel_hash = sha256(processed.convert("RGB").tobytes())
        source_pixels.add(source_pixel_hash)
        processed_pixels.add(processed_pixel_hash)
        if source.mode != "RGB":
            raise ValueError(f"{slot} source mode is {source.mode}, expected opaque RGB")
        if processed.mode != "RGB" or processed.size != (156, 210):
            raise ValueError(f"{slot} processed output is {processed.mode} {processed.size}, expected RGB 156x210")
        crop_record = json.loads((EVIDENCE / f"{slot}_crop.json").read_text(encoding="utf-8"))
        if crop_record["source_sha256"] != file_sha(source_path):
            raise ValueError(f"{slot} crop record does not match the selected source bytes")
        if crop_record["processed_sha256"] != file_sha(processed_path):
            raise ValueError(f"{slot} crop record does not match the selected processed PNG bytes")
        records.append({
            "slot": slot,
            "candidate_id": "CBA-v02" if slot == "CBA" else f"{slot}-v01",
            "runtime_basename": stem.removesuffix("_v02"),
            "source_path": str(source_path.relative_to(ROOT)).replace("\\", "/"),
            "source_dimensions": list(source.size),
            "source_mode": source.mode,
            "source_sha256": file_sha(source_path),
            "source_decoded_rgb_sha256": source_pixel_hash,
            "processed_path": str(processed_path.relative_to(ROOT)).replace("\\", "/"),
            "processed_dimensions": list(processed.size),
            "processed_mode": processed.mode,
            "processed_sha256": file_sha(processed_path),
            "processed_decoded_rgb_sha256": processed_pixel_hash,
            "crop_evidence_path": f"evidence/{slot}_crop.json",
            "crop_box": crop_record["crop_box_left_top_right_bottom"],
        })
    if len(source_pixels) != 8 or len(processed_pixels) != 8:
        raise ValueError("Selected portraits must have eight distinct decoded source and processed pixel buffers")
    sheets = []
    for name, expected in [
        ("europe_native_4x2_contact_sheet_v03.png", (624, 420)),
        ("europe_nearest4_4x2_contact_sheet_v03.png", (2496, 1680)),
    ]:
        path = REVIEW / name
        with Image.open(path) as image:
            dimensions = image.size
        if dimensions != expected:
            raise ValueError(f"Unexpected contact sheet dimensions for {name}: {dimensions}")
        sheets.append({"path": str(path.relative_to(ROOT)).replace("\\", "/"), "dimensions": list(dimensions), "sha256": file_sha(path)})
    result = {
        "audit": "selected source and native-size portrait QA",
        "date": "2026-10-03",
        "source_mode": "fictional_high_chaos; built-in native ImageGen",
        "selected_count": len(records),
        "all_sources_opaque_rgb": True,
        "all_processed_pngs_rgb_156x210": True,
        "unique_decoded_source_pixel_buffers": len(source_pixels),
        "unique_decoded_processed_pixel_buffers": len(processed_pixels),
        "visual_review": "Producer inspected each full-resolution source and each selected 156x210 PNG; parent source/framing approval recorded in manifest.md.",
        "records": records,
        "contact_sheets": sheets,
    }
    (EVIDENCE / "png_review_audit.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"selected": len(records), "source_pixel_buffers": len(source_pixels), "processed_pixel_buffers": len(processed_pixels), "contact_sheets": sheets}, indent=2))


if __name__ == "__main__":
    main()
