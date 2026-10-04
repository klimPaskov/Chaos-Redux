"""Staged candidate: in-island inpaint of bright cream/gold flecks in the feast-cohort diffuse.

STATUS: candidate only, staged under work/staged/, NOT installed. The shipped cohort diffuse/normal/specular
were processed on 2026-08-22 from the superseded recovery model's UV layout, while the shipped mesh is the
2026-08-24 recovery_v6 model (see handoff), so this inpaint can only mitigate the bright speckle; it cannot
restore correct materials. Rerun with --install only after the parent accepts that interim.

Method (always from the byte-exact backup in ../originals/):
1. Mesh UV islands from the shipped .mesh (uv_islands.py); gutter texels = -1.
2. Luminance L; island-local background level = Gaussian normalized convolution (sigma 6) of L over same-island
   texels, recomputed once with the first-pass bright texels excluded, so nothing leaks across a seam.
3. Fleck texel: inside an island, L >= 0.30, L >= 1.45 * background and L >= background + 0.10, warm
   (R >= B) and cream/gold saturation 0.08..0.70; then a 1-texel dilation clipped to the same island.
4. Per island: OpenCV Telea inpaint (radius 5) on the island's bounding box with every non-island texel also
   marked unknown, so fills draw only from the same island's non-fleck texels. Islands with fewer than 25%
   non-fleck texels are left unchanged (no in-island source) and reported.
5. Gutter texels within 2 texels of an island are re-padded from their nearest island texel (standard
   padding), so bilinear sampling at island edges does not pick up removed flecks.
6. PNG -> repository DDS converter (same uncompressed B8G8R8A8 1024 single-level layout); texel-exact round
   trip and header identity with the current file are asserted.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
MOD = PKG.parents[3]
sys.path.insert(0, str(HERE))
from repack_textures import CONVERTER, SIZE, read_bgra_dds, sha  # noqa: E402
from uv_islands import load  # noqa: E402

STEM = "cannibal_feast_cohort"
RUNTIME = MOD / "gfx/models/units/014_cannibalism/cannibal_feast_cohort/cannibal_feast_cohort_diffuse.dds"
ORIGINAL = PKG / "originals" / "cannibal_feast_cohort_diffuse.dds"
P = {"sigma": 6.0, "l_min": 0.30, "ratio": 1.45, "delta": 0.10, "sat": (0.08, 0.70), "min_source_share": 0.25,
     "telea_radius": 5, "gutter_repad": 2}


def island_background(L, lab, exclude):
    valid = (lab >= 0) & ~exclude
    out = np.zeros_like(L)
    for isl in np.unique(lab[lab >= 0]):
        m = lab == isl
        rows, cols = np.nonzero(m)
        r0, r1 = max(rows.min() - 20, 0), min(rows.max() + 21, SIZE)
        c0, c1 = max(cols.min() - 20, 0), min(cols.max() + 21, SIZE)
        w = (m & valid)[r0:r1, c0:c1].astype(np.float64)
        num = ndimage.gaussian_filter(L[r0:r1, c0:c1] * w, P["sigma"])
        den = ndimage.gaussian_filter(w, P["sigma"])
        bg = np.where(den > 1e-6, num / np.maximum(den, 1e-6), L[r0:r1, c0:c1])
        sub = m[r0:r1, c0:c1]
        out[r0:r1, c0:c1][sub] = bg[sub]
    return out


def detect(rgb, lab):
    f = rgb.astype(np.float64) / 255.0
    L = f @ [0.299, 0.587, 0.114]
    mx, mn = f.max(-1), f.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    warm = (f[..., 0] >= f[..., 2]) & (sat >= P["sat"][0]) & (sat <= P["sat"][1])
    inside = lab >= 0
    first = np.zeros_like(inside)
    for _ in range(2):
        bg = island_background(L, lab, first)
        fl = inside & warm & (L >= P["l_min"]) & (L >= P["ratio"] * bg) & (L >= bg + P["delta"])
        first = fl
    grown = ndimage.binary_dilation(fl, iterations=1)
    # keep the dilation inside the same island as the seed fleck
    same = ndimage.grey_dilation(np.where(fl, lab, -1), size=3) == lab
    return fl | (grown & same & inside)


def inpaint(rgb, lab, fleck):
    out = rgb.copy()
    skipped = []
    for isl in np.unique(lab[fleck]):
        m = lab == isl
        f = fleck & m
        if (m & ~f).sum() < P["min_source_share"] * m.sum():
            skipped.append(int(isl))
            continue
        rows, cols = np.nonzero(m)
        r0, r1 = max(rows.min() - 6, 0), min(rows.max() + 7, SIZE)
        c0, c1 = max(cols.min() - 6, 0), min(cols.max() + 7, SIZE)
        crop = np.ascontiguousarray(rgb[r0:r1, c0:c1, :3][..., ::-1])
        unknown = (f | ~m)[r0:r1, c0:c1].astype(np.uint8) * 255
        filled = cv2.inpaint(crop, unknown, P["telea_radius"], cv2.INPAINT_TELEA)[..., ::-1]
        sub = f[r0:r1, c0:c1]
        out[r0:r1, c0:c1, :3][sub] = filled[sub]
    return out, skipped


def repad_gutter(rgb, lab):
    inside = lab >= 0
    dist, (ri, ci) = ndimage.distance_transform_edt(~inside, return_indices=True)
    ring = (~inside) & (dist <= P["gutter_repad"])
    out = rgb.copy()
    out[ring, :3] = rgb[ri[ring], ci[ring], :3]
    return out, int(ring.sum())


def main(install):
    _, _, _, lab = load(STEM)
    src, header = read_bgra_dds(ORIGINAL)
    fleck = detect(src[..., :3], lab)
    fixed, skipped = inpaint(src, lab, fleck)
    fixed, repadded = repad_gutter(fixed, lab)
    stage = HERE / "staged"
    stage.mkdir(exist_ok=True)
    Image.fromarray((fleck * 255).astype(np.uint8)).save(stage / "cannibal_feast_cohort_fleck_mask.png")
    png = stage / "cannibal_feast_cohort_diffuse_candidate.png"
    Image.fromarray(fixed, "RGBA").save(png)
    dds = stage / "cannibal_feast_cohort_diffuse.dds"
    subprocess.run([sys.executable, str(CONVERTER), "--input", str(png), "--output", str(dds),
                    "--width", str(SIZE), "--height", str(SIZE)], check=True, capture_output=True)
    back, new_header = read_bgra_dds(dds)
    assert np.array_equal(back, fixed), "DDS round trip differs from PNG"
    assert new_header == header, "DDS header differs from the current cohort diffuse"
    assert np.array_equal(back[..., 3], src[..., 3]), "alpha changed"
    rec = {"status": "staged_candidate_not_installed", "params": P, "original_sha256": sha(ORIGINAL),
           "candidate_dds_sha256": sha(dds), "candidate_bytes": dds.stat().st_size,
           "fleck_texels": int(fleck.sum()), "fleck_share_of_island_texels": float(fleck.sum() / (lab >= 0).sum()),
           "islands_touched": int(len(np.unique(lab[fleck]))), "islands_skipped_no_source": skipped,
           "gutter_texels_repadded": repadded, "roundtrip_exact": True, "header_identical": True}
    if install:
        shutil.copyfile(dds, RUNTIME)
        rec["status"] = "installed"
        rec["installed_sha256"] = sha(RUNTIME)
    (HERE / "cohort_fleck_record.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    print(json.dumps(rec, indent=1))


if __name__ == "__main__":
    main(install="--install" in sys.argv)
