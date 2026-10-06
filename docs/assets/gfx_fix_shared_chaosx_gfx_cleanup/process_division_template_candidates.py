"""Prepare non-runtime 30x12 and 76x42 division-template emblem candidates."""

from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent
OLD = ROOT / "source_runtime"
GEN = ROOT / "source_generated"
OUT = ROOT / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def resize_visible(source: Path, target: Path, canvas_size: tuple[int, int], desired_visible_height: int) -> dict:
    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError(f"empty alpha: {source}")
    visible = image.crop(bbox)
    max_height = min(desired_visible_height, canvas_size[1])
    scale = max_height / visible.height
    size = (max(1, round(visible.width * scale)), max(1, round(visible.height * scale)))
    if size[0] > canvas_size[0]:
        scale = canvas_size[0] / visible.width
        size = (canvas_size[0], max(1, round(visible.height * scale)))
    resized = visible.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    offset = ((canvas_size[0] - size[0]) // 2, (canvas_size[1] - size[1]) // 2)
    canvas.alpha_composite(resized, offset)
    canvas.save(target)
    alpha_after = canvas.getchannel("A")
    return {
        "source_path": str(source.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_canvas": image.size,
        "source_visible_bbox": bbox,
        "processed_path": str(target.relative_to(ROOT)),
        "processed_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        "target_canvas": canvas_size,
        "resized_visible_size": size,
        "offset": offset,
        "processed_visible_bbox": alpha_after.getbbox(),
        "alpha_extrema": alpha_after.getextrema(),
        "corner_alpha": [alpha_after.getpixel(p) for p in ((0, 0), (canvas_size[0]-1, 0), (0, canvas_size[1]-1), (canvas_size[0]-1, canvas_size[1]-1))],
        "resampling": "Lanczos",
    }

records = []
for number in (46, 47):
    source = OLD / f"custom_template_{number:03d}_large.png"
    target = OUT / f"custom_template_{number:03d}_large_candidate.png"
    record = resize_visible(source, target, (76, 42), 36)
    record.update({"sprite": f"GFX_div_templ_{number}_large", "source_mode": "inherited template emblem; deterministic alpha-bbox scale and recenter"})
    records.append(record)

source = GEN / "custom_template_047_small_candidate_v1_source.png"
target = OUT / "custom_template_047_small_candidate_v1.png"
record = resize_visible(source, target, (30, 12), 12)
record.update({"sprite": "GFX_div_templ_47_small", "source_mode": "native ImageGen alpha; inherited emblem supplied for symbol identity and installed vanilla small for style"})
records.append(record)

(OUT / "division_template_candidate_bounds_v1.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
for r in records:
    print(r["sprite"], r["processed_path"], "bbox", r["processed_visible_bbox"], "canvas", r["target_canvas"], "corners", r["corner_alpha"])
