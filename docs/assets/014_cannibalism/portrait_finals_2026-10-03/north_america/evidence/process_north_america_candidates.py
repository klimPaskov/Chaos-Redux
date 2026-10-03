"""Process Event 014 North America native masters into deterministic review crops.
Run from the mod root with: python -B <this file>.
This performs only aspect-ratio crop, RGB Lanczos resize, metadata, and review contact sheets; it does not generate or alter portrait design.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[6]
PACKAGE = ROOT / "docs/assets/014_cannibalism/portrait_finals_2026-10-03/north_america"
SLOTS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
TARGET_RATIO = 26 / 35
GENERATION_PATHS = {
    "CBA": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-9b402aef-8f7b-4fe5-8bb5-7679c9ae353e.png",
    "CBB": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-d4ceceea-92b7-4c25-b8bb-b085619d4126.png",
    "CBC": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-2724bcfa-d537-4972-b51d-1774ff4c28cb.png",
    "CBD": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-85823be4-d025-4619-8ea0-e55493da369b.png",
    "CBE": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-014d4696-dc3a-4430-9a52-bdef6ebd70ff.png",
    "CBF": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-01616614-f8e6-44ef-abee-6a44889b3b54.png",
    "CBG": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-fc8370e3-85e6-40d8-93d4-e32f4eb5a377.png",
    "CBH": r"C:\Users\klimp\.codex\generated_images\01a101ff-fb86-79e0-b06b-ab4247da87bc\exec-5226bd1f-9d72-4bbb-a8e6-b83ced560fec.png",
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def main() -> None:
    processed: dict[str, Image.Image] = {}
    call_log = {
        "production_date": "2026-10-03",
        "execution": "one built-in native image_gen call per distinct asset; no CLI/API generation; opaque output requested; no input images attached",
        "source_mode": "fictional_high_chaos",
        "classification": "CBA-CBH are invented Event 014 warlord slot identities, not grounded real people or real polities",
        "calls": [],
    }
    inventory = []
    for slot in SLOTS:
        stem = f"leader_{slot}_warlord_north_america"
        prompt_rel = Path("prompts") / f"{slot}_prompt_v01.txt"
        source_rel = Path("source_png") / f"{stem}_source.png"
        crop_rel = Path("sourcecrop") / f"{stem}_source_crop.png"
        preview_rel = Path("processed_png") / f"{stem}_156x210.png"
        prompt_path = PACKAGE / prompt_rel
        source_path = PACKAGE / source_rel
        native_path = Path(GENERATION_PATHS[slot])
        prompt_bytes = prompt_path.read_bytes()
        source_bytes = source_path.read_bytes()
        native_bytes = native_path.read_bytes()
        if source_bytes != native_bytes:
            raise RuntimeError(f"{slot}: archived source is not byte-identical to the native tool output")
        with Image.open(source_path) as opened:
            native_mode = opened.mode
            if native_mode != "RGB":
                raise RuntimeError(f"{slot}: native output is not an opaque RGB image")
            source = opened.copy()
        width, height = source.size
        if source.mode != "RGB" or width < 800 or height < 1000:
            raise RuntimeError(f"{slot}: unexpected native source mode or dimensions")
        source_ratio = width / height
        if source_ratio > TARGET_RATIO:
            crop_width = min(width, round(height * TARGET_RATIO))
            left = (width - crop_width) // 2
            bounds = (left, 0, left + crop_width, height)
        else:
            crop_height = min(height, round(width / TARGET_RATIO))
            top = (height - crop_height) // 2
            bounds = (0, top, width, top + crop_height)
        crop = source.crop(bounds)
        crop_path = PACKAGE / crop_rel
        crop.save(crop_path, format="PNG", optimize=False)
        crop_reopened = Image.open(crop_path).convert("RGB")
        if ImageChops.difference(crop, crop_reopened).getbbox() is not None:
            raise RuntimeError(f"{slot}: crop PNG decoded pixels do not match the exact source crop")
        preview = crop.resize((156, 210), Image.Resampling.LANCZOS)
        preview_path = PACKAGE / preview_rel
        preview.save(preview_path, format="PNG", optimize=False)
        processed[slot] = preview.copy()
        crop_bytes = crop_path.read_bytes()
        preview_bytes = preview_path.read_bytes()
        crop_json = {
            "slot": slot,
            "source_mode": "fictional_high_chaos",
            "source_archive": source_rel.as_posix(),
            "native_tool_output": str(native_path),
            "native_copy_byte_equality": True,
            "source_size": [width, height],
            "source_mode_pixels": "RGB opaque",
            "source_sha256": sha256(source_bytes),
            "source_crop": crop_rel.as_posix(),
            "crop_bounds_xyxy": list(bounds),
            "crop_size": list(crop.size),
            "target_aspect_ratio": "26:35",
            "crop_decoded_pixel_equality": True,
            "crop_pixel_sha256": sha256(crop.tobytes()),
            "crop_png_bytes": len(crop_bytes),
            "crop_png_sha256": sha256(crop_bytes),
            "processed_preview": preview_rel.as_posix(),
            "processed_size": [156, 210],
            "processed_mode": preview.mode,
            "processed_alpha": "none; source and output are fully opaque",
            "resize": "Pillow Lanczos resampling after the explicit centered aspect crop; no repaint, color filter, background removal, compositing, or content addition",
            "processed_png_bytes": len(preview_bytes),
            "processed_png_sha256": sha256(preview_bytes),
            "prompt_file": prompt_rel.as_posix(),
            "prompt_bytes": len(prompt_bytes),
            "prompt_sha256": sha256(prompt_bytes),
            "provenance": "Generated from text with built-in native ImageGen; no Internet source or third-party raster was used. No separate rights/license claim is made.",
        }
        write_json(PACKAGE / "metadata" / f"{slot}_metadata.json", crop_json)
        prompt_text = prompt_bytes.decode("utf-8")
        call_log["calls"].append({
            "slot": slot,
            "revision": "v01",
            "status": "generated",
            "route": "built-in native image_gen",
            "call_count_for_asset": 1,
            "input_images": [],
            "transparent_background": False,
            "prompt_path": prompt_rel.as_posix(),
            "prompt": prompt_text,
            "prompt_sha256": sha256(prompt_bytes),
            "tool_reported_output_path": str(native_path),
            "archived_source_path": source_rel.as_posix(),
            "tool_output_and_archive_byte_equal": True,
            "native_size": [width, height],
            "native_mode": "RGB",
            "native_sha256": sha256(native_bytes),
            "tool_request_id": "not exposed in tool result",
            "tool_response": "Built-in native ImageGen returned one opaque RGB PNG and an output path; the original was copied byte-for-byte into the tranche archive.",
            "retry": False,
            "status_after_generation": "source candidate; parent source/framing review pending; no runtime promotion",
        })
        inventory.append({
            "slot": slot,
            "prompt": prompt_rel.as_posix(),
            "native_source": source_rel.as_posix(),
            "source_crop": crop_rel.as_posix(),
            "processed_preview": preview_rel.as_posix(),
            "metadata": f"metadata/{slot}_metadata.json",
            "native_dimensions": [width, height],
            "native_sha256": sha256(source_bytes),
            "crop_sha256": sha256(crop_bytes),
            "processed_dimensions": [156, 210],
            "processed_sha256": sha256(preview_bytes),
        })
    call_log["count"] = len(call_log["calls"])
    if len({item["native_sha256"] for item in inventory}) != len(SLOTS):
        raise RuntimeError("Native source byte hashes are not unique")
    if len({item["processed_sha256"] for item in inventory}) != len(SLOTS):
        raise RuntimeError("Processed preview byte hashes are not unique")
    write_json(PACKAGE / "evidence" / "imagegen_call_log.json", call_log)
    write_json(PACKAGE / "evidence" / "output_inventory.json", {
        "status": "eight original North America source and 156x210 review candidates; parent review pending; no DDS/runtime installation",
        "items": inventory,
    })
    order = [f"{slot}: leader_{slot}_warlord_north_america_156x210.png" for slot in SLOTS]
    (PACKAGE / "review" / "contact_sheet_order.txt").write_text("\n".join(order) + "\n", encoding="utf-8")
    cell_w, cell_h = 156, 210
    native_sheet = Image.new("RGB", (cell_w * 4, cell_h * 2), (28, 28, 28))
    nearest_sheet = Image.new("RGB", (cell_w * 4 * 4, cell_h * 2 * 4), (28, 28, 28))
    for index, slot in enumerate(SLOTS):
        x = (index % 4) * cell_w
        y = (index // 4) * cell_h
        native_sheet.paste(processed[slot], (x, y))
        upscaled = processed[slot].resize((cell_w * 4, cell_h * 4), Image.Resampling.NEAREST)
        nearest_sheet.paste(upscaled, (x * 4, y * 4))
    native_sheet.save(PACKAGE / "review/north_america_native_4x2_contact_sheet.png", format="PNG", optimize=False)
    nearest_sheet.save(PACKAGE / "review/north_america_nearest4_4x2_contact_sheet.png", format="PNG", optimize=False)
    print(json.dumps({
        "processed_count": len(inventory),
        "native_contact": [native_sheet.width, native_sheet.height],
        "nearest4_contact": [nearest_sheet.width, nearest_sheet.height],
        "outputs": inventory,
    }, indent=2))

if __name__ == "__main__":
    main()
