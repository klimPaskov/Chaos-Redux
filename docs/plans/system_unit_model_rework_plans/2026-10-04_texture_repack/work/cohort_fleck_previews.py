"""Before/candidate diagnosis renders for the feast-cohort fleck inpaint (read-only evidence driver).

Uses the same views, lighting and PDX material approximation as render_previews.py. Before = byte-exact backup
of the shipped diffuse; candidate = work/staged/cannibal_feast_cohort_diffuse.dds. Normal and specular are the
unchanged runtime maps in both rows. Also renders the fleck mask as an overlay and close-ups.
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
MOD = PKG.parents[3]
sys.path.insert(0, str(HERE))
from render_previews import OUT, VIEWS, png, sheet  # noqa: E402

COH = MOD / "gfx/models/units/014_cannibalism/cannibal_feast_cohort"
REN = HERE / "renders_cohort"
CLOSE = {"torso": {"dir": [0, -1, 0.1], "center": [0, 0, 3.6], "extent": 2.6},
         "waist": {"dir": [0.3, -1, 0.1], "center": [0, 0, 2.6], "extent": 1.8},
         "head": {"dir": [0.2, -1, 0.15], "center": [-0.1, -0.6, 5.6], "extent": 1.4},
         "spear_point": {"dir": [0, -1, 0.1], "center": [-1.1, 0, 0.9], "extent": 1.8}}


def main():
    REN.mkdir(exist_ok=True)
    before = png(PKG / "originals" / "cannibal_feast_cohort_diffuse.dds", "cohort_before")
    cand = png(HERE / "staged" / "cannibal_feast_cohort_diffuse.dds", "cohort_candidate")
    spec = png(COH / "cannibal_feast_cohort_specular.dds", "current")
    nrm = png(COH / "cannibal_feast_cohort_normal.dds", "current")
    mask = str(HERE / "staged" / "cannibal_feast_cohort_fleck_mask.png")
    mesh = str(COH / "cannibal_feast_cohort.mesh")
    jobs = []
    for tag, dif in (("before", before), ("candidate", cand)):
        jobs.append({"mesh": mesh, "diffuse": dif, "specular": spec, "normal": nrm, "decode": "GA", "out_prefix": str(REN / f"cohort__{tag}")})
        jobs.append({"mesh": mesh, "diffuse": dif, "out_prefix": str(REN / f"cohort__{tag}_diffuse_only")})
    jobs.append({"mesh": mesh, "diffuse": before, "mask": mask, "out_prefix": str(REN / "cohort__fleck_mask")})
    req = {"res": [600, 840], "views": {**VIEWS, **CLOSE}, "hdri": "sunrise.exr", "jobs": jobs}
    rp = HERE / "cohort_fleck_preview_request.json"
    rp.write_text(json.dumps(req, indent=1), encoding="utf-8")
    subprocess.run([sys.executable, str(MOD / ".tools/3d_pipeline/review/review_cli.py"), "blender",
                    "--script", str(HERE / "pdx_material_preview.py"), "--config", str(rp)], check=True)
    R = lambda n: str(REN / n)  # noqa: E731
    print(sheet(OUT / "cannibal_feast_cohort_fleck_inpaint_before_candidate.png",
                [("cannibal_feast_cohort BEFORE (shipped diffuse, runtime normal/specular)", R("cohort__before")),
                 ("cannibal_feast_cohort CANDIDATE, staged not installed (fleck-inpainted diffuse)", R("cohort__candidate")),
                 ("BEFORE diffuse only (matte, no normal/specular)", R("cohort__before_diffuse_only")),
                 ("CANDIDATE diffuse only (matte, no normal/specular)", R("cohort__candidate_diffuse_only")),
                 ("fleck mask on the shipped diffuse (magenta = inpainted texels)", R("cohort__fleck_mask"))]))
    import render_previews
    render_previews.VIEWS = CLOSE
    print(sheet(OUT / "cannibal_feast_cohort_fleck_inpaint_closeups.png",
                [("close-ups BEFORE", R("cohort__before")), ("close-ups CANDIDATE (staged)", R("cohort__candidate")),
                 ("close-ups fleck mask", R("cohort__fleck_mask"))], cw=400, ch=400))


if __name__ == "__main__":
    main()
