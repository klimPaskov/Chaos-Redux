"""Does a texture atlas belong to a mesh's UV layout? (2026-10-04 texture repack evidence)

Baked atlases pad their gutter by copying the colour of the nearest island texel outward (Voronoi-style fills
or radial smears). If a texture was baked for the mesh's UV layout, a gutter texel 2-6 texels outside an
island therefore matches the colour of its nearest island texel almost exactly. If the texture belongs to a
different layout, that prediction is no better than an arbitrary nearby texel.

Reported per transform (all eight flips/rotations of the texture): the share of near-gutter texels whose
colour is within 6/255 (max channel) of their nearest island texel. The matching orientation of a matching
atlas scores far above the others; a texture baked for a different UV layout scores low for every transform.

Usage (from work/): python analysis/uv_layout_agreement.py <stem>=<dds> [...]
"""
import os
import sys

import numpy as np
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from repack_textures import read_bgra_dds  # noqa: E402
from uv_islands import load  # noqa: E402

TRANSFORMS = {
    "identity": lambda a: a,
    "flip_v": lambda a: a[::-1],
    "flip_u": lambda a: a[:, ::-1],
    "rot180": lambda a: a[::-1, ::-1],
    "transpose": lambda a: np.swapaxes(a, 0, 1),
    "rot90": lambda a: np.rot90(a, 1),
    "rot270": lambda a: np.rot90(a, 3),
    "anti_transpose": lambda a: np.swapaxes(np.rot90(a, 2), 0, 1),
}


def padding_match(island, rgb):
    # Shrink islands by one texel so rasterization edge texels never count as gutter or source.
    core = ndimage.binary_erosion(island, iterations=1)
    dist, (ri, ci) = ndimage.distance_transform_edt(~core, return_indices=True)
    ring = (~ndimage.binary_dilation(island, iterations=1)) & (dist >= 2) & (dist <= 6)
    pred = rgb[ri[ring], ci[ring]].astype(np.int32)
    err = np.abs(rgb[ring].astype(np.int32) - pred).max(axis=1)
    return float((err <= 6).mean())


def score(stem, dds):
    island = load(stem)[3] >= 0
    rgb = read_bgra_dds(dds)[0][..., :3]
    return {name: padding_match(island, f(rgb)) for name, f in TRANSFORMS.items()}


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        stem, dds = arg.split("=", 1)
        s = score(stem, dds)
        best = max(s, key=s.get)
        print(f"{stem:32s} " + " ".join(f"{k}={v:.3f}" for k, v in s.items()) + f"  -> best {best}")
