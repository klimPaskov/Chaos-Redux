"""Prepare brighter 76x42 native-alpha large-emblem v3 candidates."""

from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "source_generated"
OUT = ROOT / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def process(source_name: str, output_name: str, sprite: str):
    source = GEN / source_name
    image = Image.open(source).convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.point(lambda value: 255 if value >= 8 else 0).getbbox()
    if bbox is None:
        raise ValueError(f"empty alpha subject: {source}")
    padding = 16
    bbox = (max(0,bbox[0]-padding),max(0,bbox[1]-padding),min(image.width,bbox[2]+padding),min(image.height,bbox[3]+padding))
    subject = image.crop(bbox)
    scale = min(36/subject.height,72/subject.width)
    size = (max(1,round(subject.width*scale)),max(1,round(subject.height*scale)))
    art=subject.resize(size,Image.Resampling.LANCZOS)
    canvas=Image.new("RGBA",(76,42),(0,0,0,0))
    offset=((76-size[0])//2,(42-size[1])//2)
    canvas.alpha_composite(art,offset)
    output=OUT/output_name
    canvas.save(output)
    out_alpha=canvas.getchannel("A")
    return {
        "sprite":sprite,
        "source_path":str(source.relative_to(ROOT)),
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "source_size":image.size,
        "threshold_bbox_plus_16px_padding":bbox,
        "processed_path":str(output.relative_to(ROOT)),
        "processed_sha256":hashlib.sha256(output.read_bytes()).hexdigest(),
        "canvas_size":canvas.size,
        "subject_size":size,
        "subject_offset":offset,
        "visible_bbox":out_alpha.getbbox(),
        "alpha_extrema":out_alpha.getextrema(),
        "corner_alpha":[out_alpha.getpixel(p) for p in ((0,0),(75,0),(0,41),(75,41))],
        "resampling":"Lanczos",
    }

items=[
    process("custom_template_046_large_candidate_v3_source.png","custom_template_046_large_candidate_v3.png","GFX_div_templ_46_large"),
    process("custom_template_047_large_candidate_v3_source.png","custom_template_047_large_candidate_v3.png","GFX_div_templ_47_large"),
]
report=OUT/"division_template_candidate_bounds_v3.json"
report.write_text(json.dumps(items,indent=2)+"\n",encoding="utf-8")
for item in items: print(item["sprite"],item["processed_path"],"bbox",item["visible_bbox"],"size",item["subject_size"],"corners",item["corner_alpha"])
