"""Before/after PDX material previews for the 2026-10-04 texture repack (read-only evidence driver).

Decodes DDS maps to lossless PNGs (before = byte-exact backups in ../originals/, after = installed runtime
files, unchanged maps = runtime files), writes a request for pdx_material_preview.py, runs it through
`.tools/3d_pipeline/review/review_cli.py blender` (locked Blender + locked io_pdx_mesh, headless), and
assembles labelled comparison sheets in ../previews/.
The cohort row also renders one diagnostic-only variant (not shipped) to test the speckle diagnosis.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
MOD = PKG.parents[3]
sys.path.insert(0, str(HERE))
from repack_textures import read_bgra_dds  # noqa: E402

U = MOD / "gfx" / "models" / "units"
CAN = U / "014_cannibalism"
DEC = HERE / "decoded"
REN = HERE / "renders"
OUT = PKG / "previews"
VIEWS = {"front": [0, -1, 0.15], "three_quarter": [0.65, -0.75, 0.3], "game_high": [0.45, -0.6, 1.0], "rear": [-0.3, 1, 0.25]}


def png(dds, tag):
    dest = DEC / tag / (Path(dds).stem + ".png")
    dest.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(read_bgra_dds(dds)[0], "RGBA").save(dest)
    return str(dest)


def set_for(folder, stem, tag, overrides=None):
    maps = {k: png((overrides or {}).get(k, folder / f"{stem}_{k}.dds"), tag) for k in ("diffuse", "specular", "normal")}
    return maps


def diagnostic_cohort():
    """Cohort with vanilla-band gloss (A scaled so its mean matches ENG infantry, about 87): diagnostic only."""
    rgba, _ = read_bgra_dds(CAN / "cannibal_feast_cohort" / "cannibal_feast_cohort_specular.dds")
    d = rgba.copy()
    d[..., 3] = np.clip(np.rint(d[..., 3].astype(np.float64) * (87.0 / d[..., 3].mean())), 0, 255).astype(np.uint8)
    dest = DEC / "diagnostic" / "cannibal_feast_cohort_specular_vanilla_gloss.png"
    dest.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(d, "RGBA").save(dest)
    return str(dest)


def jobs():
    out = []
    for stem in ("cannibal_island_reavers", "cannibal_march_predation_column"):
        folder = CAN / stem
        before = set_for(folder, stem, "before", {"specular": PKG / "originals" / f"{stem}_specular.dds",
                                                  "normal": PKG / "originals" / f"{stem}_normal.dds"})
        after = set_for(folder, stem, "after")
        mesh = str(folder / f"{stem}.mesh")
        # Before: decode exactly as the engine does (x = G, y = A) on the original RGB normal bytes.
        out.append({"mesh": mesh, **before, "decode": "GA", "out_prefix": str(REN / f"{stem}__before")})
        out.append({"mesh": mesh, **after, "decode": "GA", "out_prefix": str(REN / f"{stem}__after")})
    cohort = CAN / "cannibal_feast_cohort"
    cur = set_for(cohort, "cannibal_feast_cohort", "current")
    out.append({"mesh": str(cohort / "cannibal_feast_cohort.mesh"), **cur, "decode": "GA",
                "out_prefix": str(REN / "cannibal_feast_cohort__current")})
    out.append({"mesh": str(cohort / "cannibal_feast_cohort.mesh"), **cur, "specular": diagnostic_cohort(), "decode": "GA",
                "out_prefix": str(REN / "cannibal_feast_cohort__diagnostic_vanilla_gloss")})
    guard = CAN / "cannibal_feast_guard"
    out.append({"mesh": str(guard / "cannibal_feast_guard.mesh"), **set_for(guard, "cannibal_feast_guard", "current"),
                "decode": "GA", "out_prefix": str(REN / "cannibal_feast_guard__reference")})
    alien = U / "alien_infantry"
    body = {k: png(alien / f"alien_infantry_body_{k}.dds", "current") for k in ("diffuse", "specular", "normal")}
    pistol = {k: png(alien / f"alien_infantry_pistol_{k}_square.dds", "current") for k in ("diffuse", "specular", "normal")}
    out.append({"mesh": str(alien / "alien_infantry.mesh"), **body, "per_object": {"AlienRayPistol": pistol}, "decode": "GA",
                "out_prefix": str(REN / "alien_infantry__runtime_binding")})
    return out


def sheet(dest, rows, cw=330, ch=460):
    lab = 24
    sh = Image.new("RGB", (cw * len(VIEWS), (ch + lab) * len(rows)), (22, 22, 22))
    d = ImageDraw.Draw(sh)
    for r, (label, prefix) in enumerate(rows):
        y = r * (ch + lab)
        d.text((6, y + 6), label, fill=(255, 230, 120))
        for c, v in enumerate(VIEWS):
            im = Image.open(f"{prefix}__{v}.png").convert("RGB")
            im.thumbnail((cw, ch))
            sh.paste(im, (c * cw + (cw - im.width) // 2, y + lab + (ch - im.height) // 2))
    sh.save(dest)
    return str(dest)


def main():
    REN.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    req = {"res": [600, 840], "views": VIEWS, "hdri": "sunrise.exr", "report": str(REN / "render_report.json"), "jobs": jobs()}
    req_path = HERE / "preview_request.json"
    req_path.write_text(json.dumps(req, indent=1), encoding="utf-8")
    subprocess.run([sys.executable, str(MOD / ".tools/3d_pipeline/review/review_cli.py"), "blender",
                    "--script", str(HERE / "pdx_material_preview.py"), "--config", str(req_path)], check=True)
    R = lambda n: str(REN / n)  # noqa: E731
    made = [
        sheet(OUT / "cannibal_island_reavers_before_after.png",
              [("cannibal_island_reavers BEFORE (original RGB normal + grey specular, engine decoding)", R("cannibal_island_reavers__before")),
               ("cannibal_island_reavers AFTER (repacked normal + rebuilt specular, installed bytes)", R("cannibal_island_reavers__after"))]),
        sheet(OUT / "cannibal_march_predation_column_before_after.png",
              [("cannibal_march_predation_column BEFORE (original, engine decoding)", R("cannibal_march_predation_column__before")),
               ("cannibal_march_predation_column AFTER (installed bytes)", R("cannibal_march_predation_column__after"))]),
        sheet(OUT / "cannibal_feast_cohort_diagnosis.png",
              [("cannibal_feast_cohort CURRENT (unchanged runtime maps)", R("cannibal_feast_cohort__current")),
               ("cannibal_feast_guard REFERENCE (working family model, runtime maps)", R("cannibal_feast_guard__reference")),
               ("cannibal_feast_cohort DIAGNOSTIC ONLY, not shipped: gloss scaled to vanilla infantry mean", R("cannibal_feast_cohort__diagnostic_vanilla_gloss"))]),
        sheet(OUT / "alien_infantry_runtime_binding.png",
              [("alien_infantry runtime binding (body_* + pistol_* maps; alien_infantry_normal.dds is not bound)", R("alien_infantry__runtime_binding"))]),
    ]
    print("\n".join(made))


if __name__ == "__main__":
    main()
