"""Fit opaque super-event ImageGen candidates to the installed 457x328 canvas."""

from pathlib import Path
import hashlib
import json
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/"source_generated"
OUT=ROOT/"processed"
OUT.mkdir(parents=True,exist_ok=True)

specs=[
    ("super_event_azl_candidate_v1_source.png","super_event_azl_candidate_v1.png","GFX_super_event_azl"),
    ("super_event_the_final_silence_terminal_candidate_v1_source.png","super_event_the_final_silence_terminal_candidate_v1.png","GFX_super_event_final_silence_terminal"),
]
records=[]
for src_name,out_name,sprite in specs:
    src=SOURCE/src_name; image=Image.open(src).convert("RGB")
    ratio=(457/328)/(image.width/image.height)
    # The accepted full-canvas consumer is opaque. The source ratio differs by
    # less than 0.1 percent, so ImageOps.fit removes only the minimal edge strip.
    processed=ImageOps.fit(image,(457,328),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))
    dst=OUT/out_name; processed.save(dst,format="PNG",optimize=False)
    records.append({
        "sprite":sprite,
        "source_mode":"native ImageGen edit, consumer_opaque",
        "source_path":str(src.relative_to(ROOT)),
        "source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
        "source_dimensions":image.size,
        "processed_path":str(dst.relative_to(ROOT)),
        "processed_sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),
        "processed_dimensions":processed.size,
        "resampling":"Lanczos",
        "fit_crop_ratio_delta":ratio,
        "alpha":"not applicable; opaque RGB source and processed preview",
        "external_text_check":"manual visual review; no readable text observed",
    })
report=OUT/"super_event_candidate_processing_v1.json"
report.write_text(json.dumps(records,indent=2)+"\n",encoding="utf-8")
for row in records: print(row["sprite"],row["processed_path"],row["source_dimensions"],row["processed_dimensions"],row["source_sha256"],row["processed_sha256"])
