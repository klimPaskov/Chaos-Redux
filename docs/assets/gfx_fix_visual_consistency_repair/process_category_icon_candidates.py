"""Create transparent, centered 52x40 review candidates without repainting art.

Generated network/borders candidates use their native-alpha content bounds.
Eight inherited painted category icons are smoothly reduced as whole canvases
to add a visible edge margin while preserving their exact source composition.
No runtime assets are written by this script.
"""

from pathlib import Path
from PIL import Image
import json

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "source_generated"
OLD = ROOT / "source_runtime"
OUT = ROOT / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def fit_center(image: Image.Image, *, use_alpha_bbox: bool) -> tuple[Image.Image, dict]:
    image = image.convert("RGBA")
    source_size = image.size
    if use_alpha_bbox:
        alpha = image.getchannel("A")
        # The native ImageGen source has a large, very faint transparent-area
        # halo. Use its visible subject edge while retaining a small native
        # antialias margin, rather than shrinking the halo into the final icon.
        bbox = alpha.point(lambda value: 255 if value >= 8 else 0).getbbox()
        if bbox is None:
            raise ValueError("source has no visible pixels")
        pad = 16
        bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(image.width, bbox[2] + pad), min(image.height, bbox[3] + pad))
        image = image.crop(bbox)
    else:
        bbox = (0, 0, image.width, image.height)
    source_content_size = image.size
    scale = min(46 / image.width, 34 / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    art = image.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (52, 40), (0, 0, 0, 0))
    xy = ((52 - size[0]) // 2, (40 - size[1]) // 2)
    canvas.alpha_composite(art, xy)
    alpha_bbox = canvas.getchannel("A").getbbox()
    metadata = {
        "source_size": source_size,
        "source_fit_bbox_including_16px_edge": bbox,
        "fit_source_size": source_content_size,
        "resized_content_size": size,
        "content_offset": xy,
        "processed_visible_bbox": alpha_bbox,
        "corners_alpha": [canvas.getpixel((x, y))[3] for x, y in ((0, 0), (51, 0), (0, 39), (51, 39))],
        "resampling": "Lanczos",
    }
    return canvas, metadata

items = []
for stem in ("network", "borders"):
    name = f"decision_category_independence_wave_{stem}"
    source = SRC / f"{name}_candidate_v3_source.png"
    output = OUT / f"{name}_candidate_v3_tightbbox.png"
    candidate, meta = fit_center(Image.open(source), use_alpha_bbox=True)
    candidate.save(output)
    items.append({"sprite": f"GFX_{name}", "source": str(source.relative_to(ROOT)), "output": str(output.relative_to(ROOT)), "source_mode": "native ImageGen alpha; reference used for style only", **meta})

for stem in (
    "cannibalism_unified_command",
    "random_faction_bloc_pressure",
    "utopia_island",
    "utopia_district",
    "cannibalism_international_response",
    "cannibalism_unified_larder",
    "cannibalism_wendigo_command",
    "resources_found_cave",
):
    name = f"decision_category_{stem}"
    source = OLD / f"{name}_before.png"
    output = OUT / f"{name}_contained_candidate.png"
    candidate, meta = fit_center(Image.open(source), use_alpha_bbox=False)
    candidate.save(output)
    items.append({"sprite": f"GFX_{name}", "source": str(source.relative_to(ROOT)), "output": str(output.relative_to(ROOT)), "source_mode": "inherited runtime pixels; deterministic smooth contain and recenter", **meta})

(OUT / "category_icon_candidate_bounds_tightbbox.json").write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")
for item in items:
    print(item["sprite"], "->", item["output"], "bbox", item["processed_visible_bbox"], "corners", item["corners_alpha"])
