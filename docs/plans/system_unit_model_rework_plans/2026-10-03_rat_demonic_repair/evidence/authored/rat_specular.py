"""Rebuild the rat's PDX specular map from the immutable Meshy remesh download (2026-10-03 repair).

Why: the shipped black_plague_rat_spec.dds stored the provider roughness directly in alpha (correlation
+0.9999 with roughness.png, mean 149), so the shader read rough fur as glossy and its Fresnel cubemap term
made the black coat shine. Glossiness must be the inversion of roughness. Here alpha = (255 - roughness) x
0.40, which keeps the inversion and lands in the installed vanilla infantry range
(GER_infantry_alt_0_specular alpha mean 44, p95 76); green stays the profile specular level 32 used by the
shipped map (vanilla mean 31.5); blue is the provider metallic; red 0. The diffuse and normal maps are not
touched. Channels are resampled independently (no colour conversion or premultiplication).

Usage: python rat_specular.py   (writes tex/black_plague_rat_spec.png/.dds and tex/specular_manifest.json)
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
NS = HERE.parent
JOB = NS.parents[2]
MOD = JOB.parents[4]
SRC = JOB / "provider" / "downloads" / "humanoid_remesh_01_model_textures"
OUT = NS / "tex"
CONVERTER = MOD / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
SIZE = 1024
SPEC_GREEN = 32
GLOSS_SCALE = 0.40


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()


def chan(name):
    return Image.open(SRC / name).convert("L").resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rough = np.asarray(chan("roughness.png")).astype(np.float64)
    gloss = Image.fromarray(np.clip((255.0 - rough) * GLOSS_SCALE, 0, 255).astype(np.uint8), "L")
    spec = Image.merge("RGBA", (Image.new("L", (SIZE, SIZE), 0), Image.new("L", (SIZE, SIZE), SPEC_GREEN), chan("metallic.png"), gloss))
    png = OUT / "black_plague_rat_spec.png"
    spec.save(png)
    dds = OUT / "black_plague_rat_spec.dds"
    subprocess.run([sys.executable, str(CONVERTER), "--input", str(png), "--output", str(dds), "--width", str(SIZE), "--height", str(SIZE)],
                   check=True, capture_output=True)
    a = np.asarray(Image.open(dds).convert("RGBA")).astype(np.float64)
    rec = {"sources": {n: digest(SRC / n) for n in ("roughness.png", "metallic.png")},
           "params": {"SPEC_GREEN": SPEC_GREEN, "GLOSS_SCALE": GLOSS_SCALE},
           "dds": dds.name, "sha256": digest(dds), "bytes": dds.stat().st_size,
           "dds_mean_rgba": a.reshape(-1, 4).mean(0).round(1).tolist(),
           "gloss_p5_p95": np.percentile(a[..., 3], [5, 95]).round(0).tolist(),
           "gloss_vs_roughness_correlation": round(float(np.corrcoef(a[..., 3].ravel(), rough.ravel())[0, 1]), 4)}
    (OUT / "specular_manifest.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    print(json.dumps(rec, indent=1))


if __name__ == "__main__":
    main()
