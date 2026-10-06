"""Resize the native-alpha connected-node icon source to its 32x32 slot."""

from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_generated" / "decision_mengele_hidden_clone_network_candidate_v1_source.png"
OUTPUT = ROOT / "processed" / "decision_mengele_hidden_clone_network_candidate_v1.png"

image = Image.open(SOURCE).convert("RGBA")
alpha = image.getchannel("A")
bbox = alpha.point(lambda value: 255 if value >= 8 else 0).getbbox()
if bbox is None:
    raise ValueError("ImageGen source has no visible subject")
padding = 16
bbox = (max(0,bbox[0]-padding),max(0,bbox[1]-padding),min(image.width,bbox[2]+padding),min(image.height,bbox[3]+padding))
subject = image.crop(bbox)
scale = min(26/subject.width,25/subject.height)
size = (max(1,round(subject.width*scale)),max(1,round(subject.height*scale)))
resized = subject.resize(size,Image.Resampling.LANCZOS)
canvas = Image.new("RGBA",(32,32),(0,0,0,0))
offset = ((32-size[0])//2,(32-size[1])//2)
canvas.alpha_composite(resized,offset)
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
canvas.save(OUTPUT)
out_alpha=canvas.getchannel("A")
record={
    "sprite":"GFX_decision_mengele_hidden_clone_network",
    "source_path":str(SOURCE.relative_to(ROOT)),
    "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "source_size":image.size,
    "threshold_8_bbox_plus_16px_padding":bbox,
    "processed_path":str(OUTPUT.relative_to(ROOT)),
    "processed_sha256":hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
    "target_canvas":canvas.size,
    "resized_subject_size":size,
    "offset":offset,
    "visible_bbox":out_alpha.getbbox(),
    "alpha_extrema":out_alpha.getextrema(),
    "corner_alpha":[out_alpha.getpixel(p) for p in ((0,0),(31,0),(0,31),(31,31))],
    "resampling":"Lanczos",
}
report=ROOT/"processed"/"decision_mengele_hidden_clone_network_candidate_bounds_v1.json"
report.write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(record)
