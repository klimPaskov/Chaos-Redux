import hashlib
import json
import math
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/asia"
TARGET = (156, 210)
ASPECT = 26 / 35
SLOTS = {
    "CBA": "leader_CBA_warlord_asia",
    "CBB": "leader_CBB_warlord_asia",
    "CBC": "leader_CBC_warlord_asia",
    "CBD": "leader_CBD_warlord_asia",
    "CBE": "leader_CBE_warlord_asia",
    "CBF": "leader_CBF_warlord_asia",
    "CBG": "leader_CBG_warlord_asia",
    "CBH": "leader_CBH_warlord_asia",
}
PARENT_REVIEW_PATH = BASE / "evidence" / "parent_source_framing_review.json"
DDS_AUDIT_PATH = BASE / "evidence" / "dds_roundtrip_audit.json"
INSTALL_RECEIPT_PATH = BASE / "evidence" / "runtime_install_receipt.json"
PARENT_REVIEW = json.loads(PARENT_REVIEW_PATH.read_text(encoding="utf-8")) if PARENT_REVIEW_PATH.exists() else None
DDS_AUDIT = json.loads(DDS_AUDIT_PATH.read_text(encoding="utf-8")) if DDS_AUDIT_PATH.exists() else None
DDS_BY_SLOT = {item["slot"]: item for item in DDS_AUDIT["assets"]} if DDS_AUDIT else {}
INSTALL_RECEIPT = json.loads(INSTALL_RECEIPT_PATH.read_text(encoding="utf-8")) if INSTALL_RECEIPT_PATH.exists() else None
INSTALLED_BY_SLOT = {item["slot"]: item for item in INSTALL_RECEIPT["installed_targets"]} if INSTALL_RECEIPT else {}


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pixel_sha(image):
    return hashlib.sha256(image.tobytes()).hexdigest()


records = []
native_tiles = []
nearest_tiles = []
for slot, basename in SLOTS.items():
    source_path = BASE / "source_png" / f"{basename}_source.png"
    source = Image.open(source_path)
    source.load()
    source_size = source.size
    source_mode = source.mode
    width, height = source_size

    if width / height < ASPECT:
        crop_width = width
        crop_height = min(height, round(width / ASPECT))
        left = 0
        top = 0
    else:
        crop_height = height
        crop_width = min(width, round(height * ASPECT))
        left = (width - crop_width) // 2
        top = 0
    right = left + crop_width
    bottom = top + crop_height
    crop = source.crop((left, top, right, bottom))

    crop_path = BASE / "sourcecrop" / f"{basename}_source_crop.png"
    crop.save(crop_path, format="PNG", optimize=False)
    processed = crop.resize(TARGET, Image.Resampling.LANCZOS)
    processed_path = BASE / "processed_png" / f"{basename}_156x210.png"
    processed.save(processed_path, format="PNG", optimize=False)

    alpha_range = None
    if "A" in source.getbands():
        alpha_range = list(source.getchannel("A").getextrema())
        if alpha_range != [255, 255]:
            raise ValueError(f"{slot}: expected opaque full-canvas source, alpha range={alpha_range}")

    crop_record = {
        "date": "2026-10-03",
        "slot": slot,
        "candidate_id": f"{slot}-asia-native-v01",
        "source_mode": "fictional_high_chaos",
        "source_path": source_path.relative_to(ROOT).as_posix(),
        "source_dimensions": list(source_size),
        "source_mode_pixels": source_mode,
        "source_bytes": source_path.stat().st_size,
        "source_sha256": file_sha(source_path),
        "source_pixel_sha256": pixel_sha(source),
        "background": "consumer_opaque",
        "alpha_range": alpha_range,
        "target_crop_aspect": "26:35 (156:210)",
        "crop_coordinates_ltrb_source_pixels": [left, top, right, bottom],
        "crop_dimensions": [crop_width, crop_height],
        "crop_method": "direct pixel-preserving crop; top anchored to preserve complete bald scalp and keep lower prop/action in frame",
        "crop_path": crop_path.relative_to(ROOT).as_posix(),
        "crop_sha256": file_sha(crop_path),
        "crop_pixel_sha256": pixel_sha(crop),
        "crop_pixels_equal_source_region": crop.tobytes() == source.crop((left, top, right, bottom)).tobytes(),
        "processed_path": processed_path.relative_to(ROOT).as_posix(),
        "processed_dimensions": list(processed.size),
        "processed_mode": processed.mode,
        "resize_filter": "Pillow LANCZOS, crop-to-canvas conversion only",
        "processed_sha256": file_sha(processed_path),
        "processed_pixel_sha256": pixel_sha(processed),
        "processed_alpha_range": list(processed.getchannel("A").getextrema()) if "A" in processed.getbands() else None,
        "runtime_basename": f"{basename}.dds",
        "runtime_path": f"gfx/leaders/014_cannibalism/{basename}.dds",
        "sprite": f"GFX_portrait_{slot}_warlord_asia",
        "dds_state": (
            "parent-approved candidate DDS installed at existing runtime path"
            if slot in INSTALLED_BY_SLOT
            else "candidate DDS converted; exact parent DDS review pending; runtime copy not performed"
            if slot in DDS_BY_SLOT
            else "not converted; see parent review gate"
        ),
        "review_state": (
            "parent source/framing and exact DDS review approved; installed"
            if slot in INSTALLED_BY_SLOT
            else "parent source/framing approved; exact parent DDS review pending"
            if PARENT_REVIEW
            else "producer review complete; parent source/framing review pending"
        ),
    }
    if slot in DDS_BY_SLOT:
        crop_record["candidate_dds"] = DDS_BY_SLOT[slot]["candidate_dds"]
    if slot in INSTALLED_BY_SLOT:
        installed = INSTALLED_BY_SLOT[slot]
        crop_record["runtime_install_status"] = "installed and SHA-256 verified"
        crop_record["installed_runtime_sha256"] = installed["installed"]["sha256"]
        crop_record["runtime_backup_path"] = installed["backup"]["path"]
        crop_record["runtime_backup_sha256"] = installed["backup"]["sha256"]
    (BASE / "evidence" / f"{slot}_crop.json").write_text(
        json.dumps(crop_record, indent=2) + "\n", encoding="utf-8"
    )
    records.append(crop_record)
    native_tiles.append(processed.convert("RGB"))
    nearest_tiles.append(processed.convert("RGB").resize((156 * 4, 210 * 4), Image.Resampling.NEAREST))

def contact_sheet(tiles, tile_size, filename):
    cols, rows, gutter = 4, 2, 0
    sheet = Image.new("RGB", (cols * tile_size[0] + (cols - 1) * gutter, rows * tile_size[1] + (rows - 1) * gutter), (26, 29, 30))
    for i, tile in enumerate(tiles):
        x = (i % cols) * (tile_size[0] + gutter)
        y = (i // cols) * (tile_size[1] + gutter)
        sheet.paste(tile, (x, y))
    path = BASE / "review" / filename
    sheet.save(path, format="PNG", optimize=False)
    return {"path": path.relative_to(ROOT).as_posix(), "dimensions": list(sheet.size), "bytes": path.stat().st_size, "sha256": file_sha(path)}

order = [f"{slot} — {SLOTS[slot]}" for slot in SLOTS]
(BASE / "review" / "contact_sheet_order.txt").write_text("\n".join(order) + "\n", encoding="utf-8")
inventory = {
    "date": "2026-10-03",
    "scope": "Eight original Asia fictional portraits; source/framing, exact DDS approval, and runtime installation are separately evidenced stages.",
    "candidate_count": len(records),
    "source_pngs": records,
    "contact_sheets": [
        contact_sheet(native_tiles, (156, 210), "asian_native_4x2_contact_sheet.png"),
        contact_sheet(nearest_tiles, (156 * 4, 210 * 4), "asian_nearest4_4x2_contact_sheet.png"),
    ],
    "parent_source_framing_review": PARENT_REVIEW,
    "candidate_dds_status": (
        "parent DDS review approved; eight exact candidate files installed at existing runtime paths"
        if INSTALL_RECEIPT
        else "converted and audited; exact parent DDS review pending; no runtime copy"
        if DDS_AUDIT
        else "not converted; see source/framing review gate"
    ),
    "candidate_dds_audit": "evidence/dds_roundtrip_audit.json" if DDS_AUDIT else None,
    "candidate_dds_outputs": [item["candidate_dds"] for item in DDS_AUDIT["assets"]] if DDS_AUDIT else [],
    "decoded_dds_contact_sheets": [
        DDS_AUDIT["decoded_native_contact_sheet"],
        DDS_AUDIT["decoded_nearest4_contact_sheet"],
    ] if DDS_AUDIT else [],
    "runtime_install_receipt": "evidence/runtime_install_receipt.json" if INSTALL_RECEIPT else None,
    "runtime_replacement": (
        "8 Asia DDS installed and verified; Europe 8 remain as recorded in the current preinstall baseline; 40 other region-slot portraits remain queued."
        if INSTALL_RECEIPT
        else "not performed"
    ),
}
(BASE / "evidence" / "output_inventory.json").write_text(
    json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
)
print(f"processed={len(records)} native={inventory['contact_sheets'][0]['dimensions']} nearest4={inventory['contact_sheets'][1]['dimensions']}")
for item in records:
    print(f"{item['slot']}|source={item['source_dimensions']}|crop={item['crop_coordinates_ltrb_source_pixels']}|processed={item['processed_dimensions']}|source_sha256={item['source_sha256']}|processed_sha256={item['processed_sha256']}")
