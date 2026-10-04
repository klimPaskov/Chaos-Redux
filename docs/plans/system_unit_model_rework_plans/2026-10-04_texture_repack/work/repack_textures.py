"""Deterministic PDX repack of mis-packed unit normal/specular DDS maps (2026-10-04 texture repack).

Always rebuilds from the immutable byte-exact backups in ../originals/ (never from a runtime or previously
processed texture), writes processed PNGs to work/png/, converts them with the repository converter
(.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py: uncompressed B8G8R8A8, 1024x1024, single
level, the same layout as the working cannibal_bone_guard / cannibal_feast_guard maps), verifies the DDS by
decoding it back and comparing every texel with the PNG, and only then installs it to the runtime path.

Engine contract (gfx/FX/pdxmesh.shader, PdxMeshAdvanced -> PDX_IMPROVED_BLINN_PHONG):
  normal:   x = G, y = -A (UnpackRRxGNormal), B = EMISSIVE strength, R unused
  specular: G = specular strength (F0 = G^2 * 0.4), B = metalness (remapped 1-(1-B)^2), A = glossiness, R unused

Normal repack: R = 0, G = source R (tangent X), B = 0 (no emission), A = source G (tangent Y). No Y flip:
installed vanilla normals store Y green-up in A (curl test -0.34 to -0.55 on ENG/GER/FRA/FIN/JAP/ITA/SOV/USA
infantry), the Meshy-derived sources share the glTF green-up convention, and the family's working
Meshy-derived maps (feast_guard, siege_eaters, feast_cohort) were packed the same way by pdx_textures.py.

Specular rebuild from the grey (R = G = B) raw roughness map:
  gloss_raw = 255 - grey                                  (profile: A = inverted roughness)
  A = linear map of gloss_raw's p1..p99 onto bone_guard's A p1..p99 band [91, 178], clipped to 0..255
  G = 32                                                  (asset_profiles.json humanoid_unit specular_packing)
  R = 0
  B = 0 outside the geometric metal mask; inside it, gloss_raw's in-mask p5..p95 mapped onto [64, 123]
      (the 75th-percentile metal band of cannibal_bone_guard and cannibal_feast_guard), so rough/rusty
      texels stay less metallic than polished ones.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
MOD = PKG.parents[3]
CONVERTER = MOD / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
SIZE = 1024
GLOSS_BAND = (91.0, 178.0)
METAL_BAND = (64.0, 123.0)
SPEC_GREEN = 32

JOBS = [
    {"file": "cannibal_island_reavers_normal.dds", "kind": "normal",
     "runtime": "gfx/models/units/014_cannibalism/cannibal_island_reavers/cannibal_island_reavers_normal.dds"},
    {"file": "cannibal_island_reavers_specular.dds", "kind": "specular", "mask": "cannibal_island_reavers",
     "runtime": "gfx/models/units/014_cannibalism/cannibal_island_reavers/cannibal_island_reavers_specular.dds"},
    {"file": "cannibal_march_predation_column_normal.dds", "kind": "normal",
     "runtime": "gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_normal.dds"},
    {"file": "cannibal_march_predation_column_specular.dds", "kind": "specular", "mask": "cannibal_march_predation_column",
     "runtime": "gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_specular.dds"},
    {"file": "alien_infantry_normal.dds", "kind": "normal",
     "runtime": "gfx/models/units/alien_infantry/alien_infantry_normal.dds"},
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def read_bgra_dds(path):
    """Decode an uncompressed 32-bit A8R8G8B8 DDS (the only layout these files use) to RGBA uint8."""
    raw = Path(path).read_bytes()
    assert raw[:4] == b"DDS ", path
    h, w = np.frombuffer(raw[12:20], dtype="<u4")
    fourcc = raw[84:88]
    bits, rm, gm, bm, am = np.frombuffer(raw[88:108], dtype="<u4")
    assert fourcc == b"\0\0\0\0" and bits == 32 and (rm, gm, bm, am) == (0xFF0000, 0xFF00, 0xFF, 0xFF000000), path
    bgra = np.frombuffer(raw[128:128 + int(w) * int(h) * 4], dtype=np.uint8).reshape(int(h), int(w), 4)
    return bgra[..., [2, 1, 0, 3]].copy(), raw[:128]


def remap(x, src_lo, src_hi, dst_lo, dst_hi):
    t = np.clip((x - src_lo) / max(src_hi - src_lo, 1e-6), 0.0, 1.0)
    return dst_lo + t * (dst_hi - dst_lo)


def build_normal(src):
    out = np.zeros_like(src)
    out[..., 1] = src[..., 0]
    out[..., 3] = src[..., 1]
    return out, {"layout": "R=0, G=src.R (X), B=0, A=src.G (Y)", "y_flip": False}


def build_specular(src, mask_stem):
    r, g, b = (src[..., i].astype(np.int32) for i in range(3))
    assert np.array_equal(r, g) and np.array_equal(g, b), "specular source is not grey"
    gloss_raw = 255.0 - r.astype(np.float64)
    lo, hi = np.percentile(gloss_raw, [1, 99])
    a = np.clip(np.rint(remap(gloss_raw, lo, hi, *GLOSS_BAND)), 0, 255)
    mask = np.asarray(Image.open(HERE / "masks" / f"{mask_stem}_metal_mask.png").convert("L")) > 127
    assert mask.shape == (SIZE, SIZE)
    mlo, mhi = np.percentile(gloss_raw[mask], [5, 95])
    metal = np.zeros(gloss_raw.shape)
    metal[mask] = np.rint(remap(gloss_raw[mask], mlo, mhi, *METAL_BAND))
    out = np.zeros(src.shape, dtype=np.uint8)
    out[..., 1] = SPEC_GREEN
    out[..., 2] = metal.astype(np.uint8)
    out[..., 3] = a.astype(np.uint8)
    rec = {"layout": "R=0, G=32, B=metal(mask), A=gloss", "gloss_raw_p1_p99": [float(lo), float(hi)],
           "gloss_band": GLOSS_BAND, "metal_raw_p5_p95": [float(mlo), float(mhi)], "metal_band": METAL_BAND,
           "metal_texel_share": float(mask.mean())}
    return out, rec


def stats(arr):
    a = arr.astype(np.float64)
    return {"mean": [round(float(a[..., i].mean()), 2) for i in range(4)],
            "p1": [int(np.percentile(a[..., i], 1)) for i in range(4)],
            "p99": [int(np.percentile(a[..., i], 99)) for i in range(4)]}


def main(install):
    png_dir = HERE / "png"
    dds_dir = HERE / "dds"
    png_dir.mkdir(exist_ok=True)
    dds_dir.mkdir(exist_ok=True)
    ref_header = read_bgra_dds(MOD / "gfx/models/units/014_cannibalism/cannibal_bone_guard/cannibal_bone_guard_normal.dds")[1]
    records = []
    for job in JOBS:
        src_path = PKG / "originals" / job["file"]
        src, _ = read_bgra_dds(src_path)
        assert src.shape == (SIZE, SIZE, 4)
        if job["kind"] == "normal":
            out, rec = build_normal(src)
        else:
            out, rec = build_specular(src, job["mask"])
        png = png_dir / job["file"].replace(".dds", ".png")
        Image.fromarray(out, "RGBA").save(png)
        dds = dds_dir / job["file"]
        subprocess.run([sys.executable, str(CONVERTER), "--input", str(png), "--output", str(dds),
                        "--width", str(SIZE), "--height", str(SIZE)], check=True, capture_output=True)
        back, header = read_bgra_dds(dds)
        exact = bool(np.array_equal(back, out))
        assert exact, f"DDS round trip differs from PNG for {job['file']}"
        assert header == ref_header, f"DDS header differs from cannibal_bone_guard for {job['file']}"
        rec.update({"file": job["file"], "kind": job["kind"], "runtime": job["runtime"],
                    "original_sha256": sha(src_path), "png_sha256": sha(png), "dds_sha256": sha(dds),
                    "dds_bytes": dds.stat().st_size, "roundtrip_exact": exact, "header_matches_bone_guard": True,
                    "before": stats(src), "after": stats(back)})
        if install:
            dest = MOD / job["runtime"]
            shutil.copyfile(dds, dest)
            rec["installed_sha256"] = sha(dest)
            assert rec["installed_sha256"] == rec["dds_sha256"]
        records.append(rec)
        print(job["file"], "OK", rec["dds_sha256"][:16], "installed" if install else "staged")
    (HERE / "repack_record.json").write_text(json.dumps(records, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(install="--install" in sys.argv)
