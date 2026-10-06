"""Prepare parent-requested light-neutral/bright-green native-alpha v2 candidates."""

from pathlib import Path
import hashlib
import json
from PIL import Image
from typing import Optional

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "source_generated"
OUT = ROOT / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def alpha_crop(image: Image.Image, threshold: int = 8, padding: int = 16):
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value >= threshold else 0).getbbox()
    if bbox is None:
        raise ValueError("source has no visible alpha body")
    bbox = (
        max(0, bbox[0] - padding),
        max(0, bbox[1] - padding),
        min(image.width, bbox[2] + padding),
        min(image.height, bbox[3] + padding),
    )
    return image.crop(bbox), bbox

def fit(source: Path, output: Path, canvas: tuple[int, int], height: int, *, max_width: Optional[int] = None):
    image = Image.open(source).convert("RGBA")
    visible, crop_box = alpha_crop(image)
    limit_width = min(canvas[0], max_width or canvas[0])
    scale = min(height / visible.height, limit_width / visible.width)
    size = (max(1, round(visible.width * scale)), max(1, round(visible.height * scale)))
    art = visible.resize(size, Image.Resampling.LANCZOS)
    result = Image.new("RGBA", canvas, (0, 0, 0, 0))
    offset = ((canvas[0] - size[0]) // 2, (canvas[1] - size[1]) // 2)
    result.alpha_composite(art, offset)
    result.save(output)
    alpha = result.getchannel("A")
    return {
        "sprite_source": str(source.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_size": image.size,
        "subject_fit_bbox_threshold_8_plus_16px": crop_box,
        "processed_path": str(output.relative_to(ROOT)),
        "processed_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "target_canvas": canvas,
        "resized_subject_size": size,
        "offset": offset,
        "processed_visible_bbox": alpha.getbbox(),
        "alpha_extrema": alpha.getextrema(),
        "corner_alpha": [alpha.getpixel(p) for p in ((0, 0), (canvas[0]-1, 0), (0, canvas[1]-1), (canvas[0]-1, canvas[1]-1))],
        "resampling": "Lanczos",
    }

specs = [
    ("custom_template_047_small_candidate_v2_source.png", "custom_template_047_small_candidate_v2.png", (30, 12), 12, 20, "GFX_div_templ_47_small"),
    ("custom_template_046_large_candidate_v2_source.png", "custom_template_046_large_candidate_v2.png", (76, 42), 36, 72, "GFX_div_templ_46_large"),
    ("custom_template_047_large_candidate_v2_source.png", "custom_template_047_large_candidate_v2.png", (76, 42), 36, 72, "GFX_div_templ_47_large"),
]
items=[]
for source_name, output_name, canvas, height, max_width, sprite in specs:
    item=fit(GEN/source_name, OUT/output_name, canvas, height, max_width=max_width)
    item.update({"sprite":sprite,"source_mode":"native ImageGen focused edit with transparent background"})
    items.append(item)
(OUT/"division_template_candidate_bounds_v2.json").write_text(json.dumps(items,indent=2)+"\n",encoding="utf-8")
for item in items: print(item["sprite"],item["processed_path"],"bbox",item["processed_visible_bbox"],"size",item["resized_subject_size"],"corners",item["corner_alpha"])
