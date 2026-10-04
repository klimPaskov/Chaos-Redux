"""UV island labelling for the feast-cohort diffuse repair (2026-10-04 texture repack evidence).

Reads work/uvdump/<stem>.npz (rest-pose world triangle positions and UVs from pdx_material_preview.py).
Two triangles belong to the same UV island when they share a corner with the same UV coordinate and the same
3D position, so texture seams (same 3D edge, different UVs) always split islands.
Each triangle is rasterized into a SIZE x SIZE label image (row = (1 - v) * SIZE); texels not covered by any
triangle are gutter (-1). Returns the label image plus per-island triangle lists for 3D lookups.
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

HERE = Path(__file__).resolve().parent
SIZE = 1024


def triangle_islands(pos, uv):
    keys = np.concatenate([np.round(uv.reshape(-1, 2) / 1e-6), np.round(pos.reshape(-1, 3) / 1e-5)], axis=1).astype(np.int64)
    _, corner = np.unique(keys, axis=0, return_inverse=True)
    corner = corner.reshape(-1, 3)
    n = corner.max() + 1
    rows = np.concatenate([corner[:, 0], corner[:, 1], corner[:, 2]])
    cols = np.concatenate([corner[:, 1], corner[:, 2], corner[:, 0]])
    g = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    _, lab = connected_components(g, directed=False)
    _, tri_island = np.unique(lab[corner[:, 0]], return_inverse=True)
    return tri_island


def label_image(uv, tri_island):
    """Rasterize island ids; 32-bit 'I' mode image so ids above 255 survive."""
    img = Image.new("I", (SIZE, SIZE), -1)
    draw = ImageDraw.Draw(img)
    for t, isl in zip(uv, tri_island):
        draw.polygon([(u * SIZE, (1.0 - v) * SIZE) for u, v in t], fill=int(isl))
    return np.asarray(img, dtype=np.int32)


def load(stem):
    d = np.load(HERE / "uvdump" / f"{stem}.npz")
    pos, uv = d["pos"], d["uv"]
    tri_island = triangle_islands(pos, uv)
    return pos, uv, tri_island, label_image(uv, tri_island)


if __name__ == "__main__":
    pos, uv, ti, lab = load("cannibal_feast_cohort")
    sizes = np.bincount(lab[lab >= 0].ravel())
    print("islands", ti.max() + 1, "covered texels", (lab >= 0).mean().round(4),
          "island texel size pct", np.percentile(sizes[sizes > 0], [10, 50, 90, 99]).round(0))
