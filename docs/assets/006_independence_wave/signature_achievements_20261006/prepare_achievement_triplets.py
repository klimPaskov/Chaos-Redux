#!/usr/bin/env python3
"""Create the three 64x64 source-state triplets from accepted ImageGen masters.

The generated masters remain immutable. The working pass removes only isolated
alpha=1 residue, crops to the alpha>=2 subject bounds with an 8px source guard,
fits that silhouette within a 45px maximum footprint, and centers it on a
transparent 64x64 canvas. Resizing uses premultiplied RGBA to preserve genuine
transparency without introducing dark RGB fringes. Grey and not-eligible
states are deterministic derivatives of the same color subject and the exact
unchanged supplied overlay.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[4]
ARCHIVE = ROOT / "docs/assets/006_independence_wave/signature_achievements_20261006"
TRIPLET_DIR = ARCHIVE / "source_triplets"
TEMPLATE_DIR = ROOT / ".agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template"
OVERLAY_PATH = TEMPLATE_DIR / "overlay.png"
MAX_SUBJECT_PIXELS = 45
SOURCE_PADDING_PIXELS = 8
IDS = (
    "chaosx_006_oyo_compact",
    "chaosx_006_aceh_free_ports",
    "chaosx_006_mon_federal_charter",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def image_alpha_bbox(alpha: Image.Image, threshold: int) -> tuple[int, int, int, int]:
    mask = alpha.point(lambda value: 255 if value >= threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("Accepted master contains no usable subject alpha.")
    return bbox


def prepare_subject(master: Path) -> tuple[Image.Image, dict[str, object]]:
    image = Image.open(master).convert("RGBA")
    if image.size != (1254, 1254):
        raise ValueError(f"Unexpected master canvas {image.size}: {master}")

    rgba = image.load()
    removed_alpha_one = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, alpha = rgba[x, y]
            if alpha == 1:
                rgba[x, y] = (0, 0, 0, 0)
                removed_alpha_one += 1

    alpha = image.getchannel("A")
    bbox = image_alpha_bbox(alpha, 2)
    left, top, right, bottom = bbox
    bounds_w, bounds_h = right - left, bottom - top
    pad = SOURCE_PADDING_PIXELS
    crop_box = (
        max(0, left - pad),
        max(0, top - pad),
        min(image.width, right + pad),
        min(image.height, bottom + pad),
    )
    cropped = image.crop(crop_box)

    scale = MAX_SUBJECT_PIXELS / max(bounds_w, bounds_h)
    scaled_size = (
        max(1, round(cropped.width * scale)),
        max(1, round(cropped.height * scale)),
    )
    # PIL mode RGBa stores premultiplied color; convert back after resampling.
    resized = cropped.convert("RGBa").resize(scaled_size, Image.Resampling.LANCZOS).convert("RGBA")
    canvas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    paste_xy = ((64 - resized.width) // 2, (64 - resized.height) // 2)
    canvas.alpha_composite(resized, paste_xy)

    final_bbox = image_alpha_bbox(canvas.getchannel("A"), 2)
    return canvas, {
        "master": str(master.relative_to(ROOT)).replace("\\", "/"),
        "master_sha256": sha256(master),
        "master_dimensions": list(image.size),
        "removed_alpha_one_pixels": removed_alpha_one,
        "subject_bbox_alpha_ge_2": list(bbox),
        "subject_bbox_alpha_ge_2_dimensions": [bounds_w, bounds_h],
        "crop_box_with_8px_guard": list(crop_box),
        "target_max_subject_pixels": MAX_SUBJECT_PIXELS,
        "scaled_padded_canvas_size": list(scaled_size),
        "centered_paste_xy": list(paste_xy),
        "processed_subject_bbox_alpha_ge_2": list(final_bbox),
        "processed_subject_dimensions_alpha_ge_2": [final_bbox[2] - final_bbox[0], final_bbox[3] - final_bbox[1]],
        "processing": "alpha=1 residue cleared; alpha>=2 support crop; symmetric 8px source guard; premultiplied RGBA Lanczos; centered on transparent 64x64",
    }


def main() -> None:
    with (ARCHIVE / "brief.json").open("r", encoding="utf-8") as stream:
        brief = json.load(stream)
    expected = {row["achievement_id"]: row["source_sha256"] for row in brief["rows"]}
    overlay = Image.open(OVERLAY_PATH).convert("RGBA")
    if overlay.size != (64, 64):
        raise ValueError(f"Overlay must stay at 64x64; got {overlay.size}")

    TRIPLET_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for achievement_id in IDS:
        row = next((item for item in brief["rows"] if item["achievement_id"] == achievement_id), None)
        if row is None:
            raise ValueError(f"Missing brief entry: {achievement_id}")
        master = ROOT / row["source_master"]
        if sha256(master) != expected[achievement_id]:
            raise ValueError(f"Accepted master hash changed: {master}")
        color, record = prepare_subject(master)
        if color.size != (64, 64):
            raise ValueError(f"Processed subject is not 64x64: {achievement_id}")
        grey_rgb = ImageOps.grayscale(color.convert("RGB")).convert("RGB")
        grey = Image.merge("RGBA", (*grey_rgb.split(), color.getchannel("A")))
        not_eligible = Image.alpha_composite(grey, overlay)

        for suffix, state in (("", color), ("_grey", grey), ("_not_eligible", not_eligible)):
            state.save(TRIPLET_DIR / f"{achievement_id}{suffix}.png", format="PNG")

        record.update({
            "achievement_id": achievement_id,
            "source_states": {
                "completed": str((TRIPLET_DIR / f"{achievement_id}.png").relative_to(ROOT)).replace("\\", "/"),
                "grey": str((TRIPLET_DIR / f"{achievement_id}_grey.png").relative_to(ROOT)).replace("\\", "/"),
                "not_eligible": str((TRIPLET_DIR / f"{achievement_id}_not_eligible.png").relative_to(ROOT)).replace("\\", "/"),
            },
            "state_dimensions": [64, 64],
            "grey_derivation": "Pillow ImageOps.grayscale from processed color subject RGB; original subject alpha restored unchanged",
            "not_eligible_derivation": "Pillow alpha_composite(grey_source, unchanged 64x64 template/overlay.png)",
        })
        rows.append(record)

    manifest = {
        "task": "Event 006 signature achievements: deterministic 64x64 source triplets",
        "date": "2026-10-06",
        "source_mode": "native ImageGen transparent subject masters supplied and accepted by parent",
        "rejected_drafts": "retained as provenance only; never used for final output",
        "prompt_records": "initial_request_rejected.json and native_subject_edit_request.json retained beside each master",
        "overlay": {
            "path": str(OVERLAY_PATH.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(OVERLAY_PATH),
            "dimensions": list(overlay.size),
        },
        "triplet_processing": rows,
    }
    (ARCHIVE / "triplet_processing.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
