"""Build UV-space metal masks from geometric weapon selections (2026-10-04 texture repack evidence).

Input: work/uvdump/<stem>.npz written by pdx_material_preview.py (rest-pose world triangle positions and
UVs of the runtime .mesh, Blender Z-up, v up). A triangle is metal when its centroid falls inside one of the
model's selection boxes below. Selected UV triangles are rasterized into a 1024x1024 mask (row = (1 - v) * H),
dilated by one texel so bilinear sampling at island edges stays inside the metal value.

The rules were chosen from rest-pose renders of the shipped diffuse and confirmed by diffuse samples at the
selected triangles (recorded in the handoff):
- island reavers: the harpoon's iron tip above z 6.62 (rgb about 63,48,35, saturation 0.44) and its barb hook,
  i.e. triangles between z 5.70 and 6.45 lying more than 0.12 from the fitted shaft axis (rgb about 68,50,35,
  saturation 0.48). The wooden shaft (rgb about 95,61,39, saturation 0.58-0.60, radius about 0.085) and its
  lashing stay non-metal.
- march predation column: the cleaver-style machete blade, which lies flat forward (-Y) of the right hand.
  The hand, the handle butt behind it, skin, bone, rope, wood, leather and cloth stay non-metal.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

HERE = Path(__file__).resolve().parent
SIZE = 1024

# Rule kinds on triangle centroids (rest pose, Blender Z-up):
#   ("box", xmin, xmax, ymin, ymax, zmin, zmax)
#   ("off_axis", axis_box, zmin, zmax, rmin): distance from a straight axis fitted (x, y as linear functions of z)
#       to the centroids inside axis_box exceeds rmin, within [zmin, zmax] and inside axis_box's x/y extent.
SELECTIONS = {
    "cannibal_island_reavers": {
        "harpoon_tip": [("box", 1.40, 2.00, -1.20, 1.20, 6.62, 7.40)],
        "harpoon_barb": [("off_axis", (1.30, 2.00, -1.20, 1.20, 5.00, 5.70), 5.70, 6.45, 0.12)],
    },
    "cannibal_march_predation_column": {
        "machete_blade": [("box", -4.00, -2.50, -2.10, 0.10, 5.30, 6.40)],
    },
}


def in_box(c, x0, x1, y0, y1, z0, z1):
    return (c[:, 0] >= x0) & (c[:, 0] <= x1) & (c[:, 1] >= y0) & (c[:, 1] <= y1) & (c[:, 2] >= z0) & (c[:, 2] <= z1)


def apply_rule(c, rule):
    if rule[0] == "box":
        return in_box(c, *rule[1:])
    _, axis_box, z0, z1, rmin = rule
    ref = in_box(c, *axis_box)
    fx = np.polyfit(c[ref, 2], c[ref, 0], 1)
    fy = np.polyfit(c[ref, 2], c[ref, 1], 1)
    r = np.hypot(c[:, 0] - np.polyval(fx, c[:, 2]), c[:, 1] - np.polyval(fy, c[:, 2]))
    x0, x1, y0, y1 = axis_box[:4]
    return in_box(c, x0, x1, y0, y1, z0, z1) & (r > rmin)


def build(stem, out_dir):
    d = np.load(HERE / "uvdump" / f"{stem}.npz")
    pos, uv = d["pos"], d["uv"]
    c = pos.mean(1)
    sel = np.zeros(len(c), dtype=bool)
    parts = {}
    for part, rules in SELECTIONS[stem].items():
        m = np.zeros(len(c), dtype=bool)
        for rule in rules:
            m |= apply_rule(c, rule)
        parts[part] = int(m.sum())
        sel |= m
    img = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(img)
    for tri in uv[sel]:
        draw.polygon([(u * SIZE, (1.0 - v) * SIZE) for u, v in tri], fill=255)
    mask = ndimage.binary_dilation(np.asarray(img) > 127, iterations=1)
    Image.fromarray((mask * 255).astype(np.uint8)).save(out_dir / f"{stem}_metal_mask.png")
    return {"stem": stem, "triangles": int(sel.sum()), "parts": parts, "texel_coverage": float(mask.mean()),
            "boxes": SELECTIONS[stem]}


if __name__ == "__main__":
    out = HERE / "masks"
    out.mkdir(exist_ok=True)
    rep = [build(s, out) for s in (sys.argv[1:] or SELECTIONS)]
    (out / "metal_masks.json").write_text(json.dumps(rep, indent=1), encoding="utf-8")
    print(json.dumps(rep, indent=1))
