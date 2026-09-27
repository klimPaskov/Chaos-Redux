"""Derive a recoloured texture set for a unit variant that shares another unit's mesh.

A variant (an elite company, a veteran cadre) reuses the base unit's .mesh and animations and
differs only by its diffuse map. This tool colourises the low-saturation materials of a base
colour atlas (cloth, leather, webbing, metal) toward an authored tint, leaves saturated skin
tones and the held-item atlas cells untouched, and copies the other PBR maps unchanged, so
``pdx_textures.py --textures <out> --stem <variant stem>`` converts the result like any atlas.

Spec (JSON):
{
  "source": "<dir with base_color/metallic/roughness/normal.png>",
  "out": "<variant dir to write>",
  "tint": [r, g, b],            # 0-255 target hue for recoloured materials
  "strength": 0.7,              # 0-1 blend toward the colourised result
  "value_scale": 0.85,          # multiplies brightness of recoloured pixels (night dye < 1)
  "saturation_keep": [0.18, 0.35],   # pixels above the upper saturation stay; ramp between
  "skin_hue": [5, 50],          # hue degrees protected when saturation is above the lower bound
  "keep_top": 0.25              # fraction of the image height kept (lab_items puts item cells there)
}
Writes <out>/variant_manifest.json with source and output hashes and the spec.

Usage: python .tools/3d_pipeline/review/texture_variant.py <spec.json>
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

import numpy as np
from PIL import Image

MAPS = ("metallic.png", "roughness.png", "normal.png")


def _sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()


def _smooth(x, a, b):
    t = np.clip((x - a) / max(b - a, 1e-6), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def recolour(rgb, spec):
    f = rgb.astype(np.float32) / 255.0
    mx, mn = f.max(axis=2), f.min(axis=2)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0.0)
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    d = np.maximum(mx - mn, 1e-6)
    hue = np.where(mx == r, (g - b) / d % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60.0
    s0, s1 = spec.get("saturation_keep", [0.18, 0.35])
    weight = 1.0 - _smooth(sat, s0, s1)
    h0, h1 = spec.get("skin_hue", [5, 50])
    skin = (hue >= h0) & (hue <= h1) & (sat > s0)
    weight = np.where(skin, 0.0, weight) * spec.get("strength", 0.7)
    keep = int(round(f.shape[0] * spec.get("keep_top", 0.0)))
    weight[:keep, :] = 0.0
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    tint = np.array(spec["tint"], dtype=np.float32) / 255.0
    tint_lum = max(float(0.2126 * tint[0] + 0.7152 * tint[1] + 0.0722 * tint[2]), 1e-3)
    dyed = np.clip(lum[..., None] * (tint / tint_lum) * spec.get("value_scale", 1.0), 0.0, 1.0)
    out = f * (1 - weight[..., None]) + dyed * weight[..., None]
    return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)


def main(spec_path):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    src, out = Path(spec["source"]), Path(spec["out"])
    out.mkdir(parents=True, exist_ok=True)
    img = Image.open(src / "base_color.png")
    alpha = img.getchannel("A") if img.mode == "RGBA" else None
    rgb = np.asarray(img.convert("RGB"))
    result = Image.fromarray(recolour(rgb, spec), "RGB")
    if alpha is not None:
        result.putalpha(alpha)
    result.save(out / "base_color.png")
    for name in MAPS:
        if (src / name).exists():
            shutil.copy2(src / name, out / name)
    manifest = {"spec": spec, "source_base_color_sha256": _sha(src / "base_color.png"),
                "base_color_sha256": _sha(out / "base_color.png"),
                "copied": {n: _sha(out / n) for n in MAPS if (out / n).exists()}}
    (out / "variant_manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print("VARIANT", out, manifest["base_color_sha256"][:12])


if __name__ == "__main__":
    main(sys.argv[1])
