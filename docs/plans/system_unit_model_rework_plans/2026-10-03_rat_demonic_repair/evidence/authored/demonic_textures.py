"""Rebuild the demonic zombie PDX maps from the immutable Meshy PBR download (2026-10-03 repair).

Why: the shipped diffuse came from the shared humanoid profile grade (gamma 0.72), which lifted an
already pale, low-contrast provider atlas to a mottled light grey (mean RGB ~118/108/112), and the
Meshy texture had lost the dark wing membranes of the approved reference. Combined with a glossiness
channel of ~0.49 (vanilla GER infantry ~0.17), the shader's Fresnel cubemap term washed the thin body
and the wing membranes toward white at map distance.

Inputs (never modified): provider/downloads/demonic_body_01_textures/{base_color,roughness,metallic,normal}.png,
plus maps baked from the rest mesh onto its own UV atlas: tex/ao_2048.png (Cycles AO, 0.6 units) and
tex/regions_2048.png (R = wing-bone weight, G = head/neck weight, B = hands/feet weight).

Every number below is a deliberate material decision recorded with its reason:
- Region colour targets are sampled from the approved Meshy reference refs/original/meshy_input.png;
  skin and head sit about 8 % below the sampled reference to offset the brighter in-game mesh lighting
  (skin chest 113/98/101, face 129/111/113, wing membrane 64/51/52 and 54/45/46, wing bone 39/29/29).
- Variation around each target keeps the provider's own detail, scaled per region (head stronger so
  the eye sockets, teeth, and grin read at map scale).
- AO multiplies the result so ribs, sockets, armpits, and membrane folds carry contrast.
- Specular green (strength) per region; alpha = 255 - roughness (inversion kept), scaled into the
  installed vanilla infantry glossiness range (GER_infantry_alt_0_specular alpha median 40, p95 76).
- Normal: PDX RRxG layout exactly as vanilla GER_infantry_alt_0_normal: R = G = tangent X, B = 0
  (no emissive), A = tangent Y. The provider normal is OpenGL-convention, which is the convention
  io_pdx_mesh and the shader's UnpackRRxGNormal (y = -(A*2-1) on DirectX UVs) expect.
Packed RGBA data maps are resized channel by channel (no colour conversion, no premultiplication).

Usage: python demonic_textures.py   (writes tex/png/*.png, tex/dds/*.dds, tex/textures_manifest.json)
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent
NS = HERE.parent                                   # blender/working/r2
JOB = NS.parents[2]                                # demonic_zombies job root
MOD = JOB.parents[4]
SRC = JOB / "provider" / "downloads" / "demonic_body_01_textures"
TEX = NS / "tex"
CONVERTER = MOD / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
STEM = "chaosx_demonic_zombies"
SIZE = 1024

# Region colour targets (sRGB 0-255) from the approved reference, and detail scale per region.
SKIN_TARGET = np.array([104.0, 89.0, 93.0]); SKIN_DETAIL = 1.15
HEAD_TARGET = np.array([116.0, 99.0, 103.0]); HEAD_DETAIL = 1.45
WING_TARGET = np.array([60.0, 48.0, 49.0]); WING_DETAIL = 0.95
CLAW_TARGET = np.array([96.0, 84.0, 86.0]); CLAW_DETAIL = 1.25
AO_FLOOR = 0.35          # fully occluded texels keep 35 % of their value
UNSHARP = dict(radius=5, percent=70, threshold=2)
# Specular strength (green) per region and the glossiness scale into the vanilla range.
SPEC_SKIN, SPEC_HEAD, SPEC_WING, SPEC_CLAW, SPEC_CLOTH = 34, 40, 46, 70, 14
CLOTH_LUMA = 52.0        # provider texels darker than this are the loincloth and sash
GLOSS_SCALE = 0.40


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()


def load(name, mode):
    return np.asarray(Image.open(SRC / name).convert(mode)).astype(np.float64)


def region_mean(img, w):
    s = w.sum()
    return (img * w[..., None]).sum((0, 1)) / max(s, 1e-6)


def main():
    base = load("base_color.png", "RGB")
    rough = load("roughness.png", "L")
    metal = load("metallic.png", "L")
    nrm = load("normal.png", "RGB")
    ao = np.asarray(Image.open(TEX / "ao_2048.png").convert("L")).astype(np.float64) / 255.0
    reg = np.asarray(Image.open(TEX / "regions_2048.png").convert("RGB")).astype(np.float64) / 255.0
    wing, head, claw = reg[..., 0], reg[..., 1], reg[..., 2]
    luma = base @ np.array([0.299, 0.587, 0.114])
    cloth = np.clip((CLOTH_LUMA + 12 - luma) / 24.0, 0, 1) * (1 - wing)
    skin = np.clip(1 - wing - head - claw - cloth, 0, 1)

    out = np.zeros_like(base)
    weights = {"skin": skin, "head": head, "wing": wing, "claw": claw}
    targets = {"skin": (SKIN_TARGET, SKIN_DETAIL), "head": (HEAD_TARGET, HEAD_DETAIL),
               "wing": (WING_TARGET, WING_DETAIL), "claw": (CLAW_TARGET, CLAW_DETAIL)}
    total = np.zeros(base.shape[:2])
    stats = {}
    for name, w in weights.items():
        m = region_mean(base, w)
        tgt, k = targets[name]
        graded = tgt + (base - m) * k
        out += graded * w[..., None]
        total += w
        stats[name] = {"provider_mean": m.round(1).tolist(), "target": tgt.tolist(), "detail": k, "coverage": round(float(w.mean()), 4)}
    out += base * cloth[..., None]          # cloth keeps its provider colour
    total += cloth
    out = out / np.maximum(total, 1e-6)[..., None]
    out *= (AO_FLOOR + (1 - AO_FLOOR) * ao)[..., None]
    out = np.clip(out, 0, 255).astype(np.uint8)
    img = Image.fromarray(out, "RGB").filter(ImageFilter.UnsharpMask(**UNSHARP))
    diffuse = img.resize((SIZE, SIZE), Image.Resampling.LANCZOS).convert("RGBA")

    spec_g = (SPEC_SKIN * skin + SPEC_HEAD * head + SPEC_WING * wing + SPEC_CLAW * claw + SPEC_CLOTH * cloth) / np.maximum(total, 1e-6)
    gloss = (255.0 - rough) * GLOSS_SCALE

    def chan(a):
        return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "L").resize((SIZE, SIZE), Image.Resampling.LANCZOS)

    zero = Image.new("L", (SIZE, SIZE), 0)
    specular = Image.merge("RGBA", (zero, chan(spec_g), chan(metal), chan(gloss)))
    nx, ny = chan(nrm[..., 0]), chan(nrm[..., 1])
    normal = Image.merge("RGBA", (nx, nx, zero, ny))

    (TEX / "png").mkdir(parents=True, exist_ok=True)
    (TEX / "dds").mkdir(parents=True, exist_ok=True)
    record = {"sources": {n: digest(SRC / n) for n in ("base_color.png", "roughness.png", "metallic.png", "normal.png")},
              "baked": {n: digest(TEX / n) for n in ("ao_2048.png", "regions_2048.png")},
              "regions": stats, "params": {"AO_FLOOR": AO_FLOOR, "UNSHARP": UNSHARP, "GLOSS_SCALE": GLOSS_SCALE, "CLOTH_LUMA": CLOTH_LUMA,
                                           "spec_green": [SPEC_SKIN, SPEC_HEAD, SPEC_WING, SPEC_CLAW, SPEC_CLOTH]},
              "outputs": {}}
    for role, im in (("diffuse", diffuse), ("specular", specular), ("normal", normal)):
        png = TEX / "png" / f"{STEM}_{role}.png"
        im.save(png)
        dds = TEX / "dds" / f"{STEM}_{role}.dds"
        subprocess.run([sys.executable, str(CONVERTER), "--input", str(png), "--output", str(dds), "--width", str(SIZE), "--height", str(SIZE)],
                       check=True, capture_output=True)
        a = np.asarray(Image.open(dds).convert("RGBA")).astype(np.float64).reshape(-1, 4)
        record["outputs"][role] = {"png": png.name, "dds": dds.name, "sha256": digest(dds), "bytes": dds.stat().st_size,
                                   "dds_mean_rgba": a.mean(0).round(1).tolist(), "dds_p5_p95": [np.percentile(a, 5, axis=0).round(0).tolist(), np.percentile(a, 95, axis=0).round(0).tolist()]}
    # Inversion check: decoded glossiness must fall as provider roughness rises.
    g = np.asarray(Image.open(TEX / "dds" / f"{STEM}_specular.dds").convert("RGBA"))[..., 3].astype(np.float64).ravel()
    r = np.asarray(Image.fromarray(rough.astype(np.uint8)).resize((SIZE, SIZE), Image.Resampling.LANCZOS)).astype(np.float64).ravel()
    record["gloss_vs_roughness_correlation"] = round(float(np.corrcoef(g, r)[0, 1]), 4)
    (TEX / "textures_manifest.json").write_text(json.dumps(record, indent=1), encoding="utf-8")
    print(json.dumps({k: v for k, v in record.items() if k in ("outputs", "regions", "gloss_vs_roughness_correlation")}, indent=1))


if __name__ == "__main__":
    main()
