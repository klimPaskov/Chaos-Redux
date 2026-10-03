from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


BASE = Path(__file__).resolve().parents[1]
SOURCE_DIR = BASE / "source_png"
CROP_DIR = BASE / "sourcecrop"
PROCESSED_DIR = BASE / "processed_png"
REVIEW_DIR = BASE / "review"
EVIDENCE_DIR = BASE / "evidence"
TAGS = ("CBA", "CBB", "CBC", "CBD", "CBE", "CBF", "CBG", "CBH")
TARGET = (156, 210)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def raw_pixel_hash(image: Image.Image) -> str:
    return sha256_bytes(image.convert("RGBA").tobytes())


def ensure_opaque(image: Image.Image, slot: str) -> Image.Image:
    if image.mode in ("RGBA", "LA") or "transparency" in image.info:
        rgba = image.convert("RGBA")
        alpha = rgba.getchannel("A")
        if alpha.getextrema() != (255, 255):
            raise ValueError(f"{slot}: source is not fully opaque")
        return rgba.convert("RGB")
    return image.convert("RGB")


def main() -> None:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    crops: list[Image.Image] = []
    inventory: list[dict[str, object]] = []
    for slot in TAGS:
        source_path = SOURCE_DIR / f"leader_{slot}_warlord_oceania_source.png"
        prompt_path = BASE / "prompts" / f"{slot}.txt"
        if not source_path.is_file() or not prompt_path.is_file():
            raise FileNotFoundError(f"{slot}: missing source or prompt")

        with Image.open(source_path) as opened:
            source = ensure_opaque(opened, slot)
        width, height = source.size
        crop_height = round(width * TARGET[1] / TARGET[0])
        if crop_height > height:
            crop_width = round(height * TARGET[0] / TARGET[1])
            left = (width - crop_width) // 2
            box = (left, 0, left + crop_width, height)
        else:
            box = (0, 0, width, crop_height)
        crop = source.crop(box)
        crop_path = CROP_DIR / f"leader_{slot}_warlord_oceania_source_crop.png"
        processed_path = PROCESSED_DIR / f"leader_{slot}_warlord_oceania_156x210.png"
        crop.save(crop_path, format="PNG", optimize=False)
        processed = crop.resize(TARGET, Image.Resampling.LANCZOS)
        processed.save(processed_path, format="PNG", optimize=False)

        with Image.open(crop_path) as saved_crop:
            saved_crop = saved_crop.convert("RGB")
            exact_crop = saved_crop.tobytes() == source.crop(box).tobytes()
        if not exact_crop:
            raise ValueError(f"{slot}: saved source crop differs from direct pixel crop")
        with Image.open(processed_path) as saved_processed:
            saved_processed = saved_processed.convert("RGB")
            if saved_processed.size != TARGET:
                raise ValueError(f"{slot}: processed image has wrong dimensions")
            if saved_processed.getextrema() is None:
                raise ValueError(f"{slot}: processed image could not be decoded")

        prompt_bytes = prompt_path.read_bytes()
        metadata = {
            "slot": slot,
            "source_mode": "fictional_high_chaos",
            "route": "built-in native image_gen",
            "consumer": f"GFX_portrait_{slot}_warlord_oceania",
            "runtime_path": f"gfx/leaders/014_cannibalism/leader_{slot}_warlord_oceania.dds",
            "background_mode": "consumer_opaque",
            "source_path": source_path.relative_to(BASE).as_posix(),
            "source_dimensions": [width, height],
            "source_mode_pixels": "RGB",
            "source_sha256": sha256_file(source_path),
            "source_rgba_pixel_sha256": raw_pixel_hash(source),
            "crop_path": crop_path.relative_to(BASE).as_posix(),
            "crop_box_ltrb": list(box),
            "crop_dimensions": list(crop.size),
            "crop_sha256": sha256_file(crop_path),
            "crop_rgba_pixel_sha256": raw_pixel_hash(crop),
            "direct_pixel_crop_equal": exact_crop,
            "processed_path": processed_path.relative_to(BASE).as_posix(),
            "processed_dimensions": list(TARGET),
            "processed_sha256": sha256_file(processed_path),
            "processed_rgba_pixel_sha256": raw_pixel_hash(processed),
            "prompt_path": prompt_path.relative_to(BASE).as_posix(),
            "prompt_sha256": sha256_bytes(prompt_bytes),
            "resize": "Pillow LANCZOS from direct crop",
            "source_review_state": "parent_source_framing_approved",
            "parent_review_date": "2026-10-03",
            "parent_review_basis": "Parent acceptance within the existing 56-portrait scope; original source art and framing approved for all eight Oceania slots, with candidate DDS final review still pending.",
            "rights_provenance": "native ImageGen output from an authorized fictional brief; no third-party source or separate license claim",
            "reviewer": "portrait-production subagent",
            "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
        }
        metadata_path = CROP_DIR / f"leader_{slot}_warlord_oceania_crop.json"
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        inventory.append(metadata)
        crops.append(saved_processed.copy())

    native = Image.new("RGB", (TARGET[0] * 4, TARGET[1] * 2), (0, 0, 0))
    nearest4 = Image.new("RGB", (TARGET[0] * 16, TARGET[1] * 8), (0, 0, 0))
    for index, image in enumerate(crops):
        x = (index % 4) * TARGET[0]
        y = (index // 4) * TARGET[1]
        native.paste(image, (x, y))
        enlarged = image.resize((TARGET[0] * 4, TARGET[1] * 4), Image.Resampling.NEAREST)
        nearest4.paste(enlarged, (x * 4, y * 4))
    native_path = REVIEW_DIR / "oceania_native_4x2_contact_sheet.png"
    nearest_path = REVIEW_DIR / "oceania_nearest4_4x2_contact_sheet.png"
    native.save(native_path, format="PNG", optimize=False)
    nearest4.save(nearest_path, format="PNG", optimize=False)
    (REVIEW_DIR / "contact_sheet_order.txt").write_text(
        "Grid order, left to right then top to bottom: CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH.\n",
        encoding="utf-8",
    )

    output = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "event": "014_cannibalism",
        "region": "oceania",
        "target_dimensions": list(TARGET),
        "portrait_ratio": "26:35",
        "crop_policy": "full source width, top anchored to preserve complete bald scalp; direct lossless crop before LANCZOS resize",
        "contact_sheets": [
            {
                "path": native_path.relative_to(BASE).as_posix(),
                "dimensions": list(native.size),
                "sha256": sha256_file(native_path),
            },
            {
                "path": nearest_path.relative_to(BASE).as_posix(),
                "dimensions": list(nearest4.size),
                "sha256": sha256_file(nearest_path),
            },
        ],
        "assets": inventory,
        "dds_conversion": "not performed; parent source/framing review is required first",
    }
    (EVIDENCE_DIR / "output_inventory.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "assets": len(inventory),
        "all_direct_crops_equal": all(item["direct_pixel_crop_equal"] for item in inventory),
        "source_hashes_unique": len({item["source_sha256"] for item in inventory}) == len(inventory),
        "processed_hashes_unique": len({item["processed_sha256"] for item in inventory}) == len(inventory),
        "native_contact_sheet": [native.width, native.height],
        "nearest4_contact_sheet": [nearest4.width, nearest4.height],
    }))


if __name__ == "__main__":
    main()
