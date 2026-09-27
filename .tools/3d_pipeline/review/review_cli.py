"""Host-side CLI for read-only unit model review.

Runs the locked Blender (path from config/dependencies.lock.json) in background mode
with blender_review.py and builds contact sheets from the rendered frames.

Examples (from the mod root):
  python .tools/3d_pipeline/review/review_cli.py triage --out <dir> \
      --model infected=gfx/models/units/chaosx_infected_zombies
  python .tools/3d_pipeline/review/review_cli.py legacy-ref --folder gfx/models/units/chaosx_demonic_zombies --out <prefix>
  python .tools/3d_pipeline/review/review_cli.py glb-ref --glb <file.glb> --out <prefix> --face
  python .tools/3d_pipeline/review/review_cli.py actions --blend <job>/blender/checkpoints/x.blend --armature Armature.001 \
      --mesh char1.001 --action chaosx_zombies_attack --action chaosx_zombies_death --out <dir> --humanoid
  python .tools/3d_pipeline/review/review_cli.py compare --row <portrait> <legacy> <reference> --out <file.png>
  python .tools/3d_pipeline/review/review_cli.py blender --script lab_finalize.py --config <cfg.json>
      (runs a writing worker such as lab_finalize.py or lab_items.py headless with the locked Blender)

--model accepts name=folder[:mesh[:diffuse]]; mesh defaults to the folder's single .mesh and
diffuse to the first *diff*.dds in the folder. --humanoid supplies Meshy/Mixamo-style bone names
(LeftHand, RightHand, LeftToeBase, RightToeBase, Jaw, Spine) for phase measurements.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPE = HERE.parent
MOD = PIPE.parent.parent
WORKER = HERE / "blender_review.py"
HUMANOID_BONES = {"hand_l": "LeftHand", "hand_r": "RightHand", "toe_l": "LeftToeBase", "toe_r": "RightToeBase", "jaw": "Jaw", "spine": "Spine"}


def blender_exe():
    lock = json.loads((PIPE / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))
    return lock["routes"]["blender"]["executable"]


def run_worker(request):
    # Blender resolves a relative render filepath against the (unsaved) blend directory rather than
    # the process directory, so renders written from relative paths silently land nowhere.
    for key in ("out", "out_dir", "glb", "blend", "folder"):
        if isinstance(request.get(key), str) and request[key]:
            request[key] = os.path.abspath(request[key])
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(request, fh)
        req_path = fh.name
    cmd = [blender_exe(), "--background", "--factory-startup", "--addons", "bl_ext.user_default.io_pdx_mesh",
           "--python", str(WORKER), "--", req_path]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = [l for l in proc.stdout.splitlines() + proc.stderr.splitlines()
             if l.startswith(("TRIAGE", "GLB", "ACTION")) or "Error" in l or "Traceback" in l or l.startswith("  File")]
    print("\n".join(lines))
    os.unlink(req_path)
    if proc.returncode != 0:
        sys.exit(proc.returncode)


def resolve_model(spec):
    name, rest = spec.split("=", 1)
    parts = rest.split(":")
    folder = Path(parts[0]) if Path(parts[0]).is_absolute() else MOD / parts[0]
    mesh = parts[1] if len(parts) > 1 and parts[1] else next(p.name for p in folder.glob("*.mesh"))
    diffuse = parts[2] if len(parts) > 2 else next((p.name for p in sorted(folder.glob("*diff*.dds"))), "")
    return {"name": name, "folder": str(folder), "mesh": mesh, "diffuse": diffuse}


def contact_sheet(out_dir, prefix, dest, cell=(150, 200), views=None):
    from PIL import Image, ImageDraw
    files = glob.glob(os.path.join(out_dir, f"{prefix}__*__*__*.png"))
    rx = re.compile(re.escape(prefix) + r"__(.+)__(\d{3})__([a-z_]+)\.png$")
    table = {}
    for f in files:
        m = rx.search(os.path.basename(f))
        if m:
            table.setdefault(m.group(1), {}).setdefault(int(m.group(2)), {})[m.group(3)] = f
    if not table:
        return None
    views = views or sorted({v for r in table.values() for fr in r.values() for v in fr})
    ncol = max(len(r) for r in table.values()) * len(views)
    w, h = cell
    sheet = Image.new("RGB", (w * ncol, h * len(table)), "white")
    for i, role in enumerate(sorted(table)):
        col = 0
        for fr in sorted(table[role]):
            for v in views:
                if v in table[role][fr]:
                    im = Image.open(table[role][fr][v]).convert("RGB").resize((w, h))
                    ImageDraw.Draw(im).text((3, 3), f"{role} {fr} {v[:5]}", fill="red")
                    sheet.paste(im, (col * w, i * h))
                col += 1
    sheet.save(dest)
    return dest


def cmd_triage(a):
    models = [resolve_model(m) for m in a.model]
    run_worker({"mode": "triage", "models": models, "out_dir": a.out, "samples": a.samples, "report": "triage_report.json"})
    for m in models:
        print(contact_sheet(a.out, m["name"], os.path.join(a.out, f"sheet_{m['name']}.png"), views=["front", "side"]))


def cmd_legacy_ref(a):
    spec = resolve_model("ref=" + a.folder)
    run_worker({"mode": "legacy_ref", "folder": spec["folder"], "mesh": spec["mesh"], "diffuse": spec["diffuse"], "out": a.out,
                "views": a.view or ["front", "three_quarter", "side"]})


def cmd_glb_ref(a):
    run_worker({"mode": "glb_ref", "glb": a.glb, "out": a.out, "face": a.face})


def cmd_actions(a):
    req = {"mode": "actions", "blend": a.blend, "armature": a.armature, "meshes": a.mesh, "actions": a.action, "out_dir": a.out,
           "tag": a.tag, "samples": a.samples, "views": a.view or ["front", "side", "three_quarter"]}
    if a.humanoid:
        req["bones"] = HUMANOID_BONES
    if a.bones:
        req["bones"] = json.loads(a.bones)
    if a.frame:
        req["frames"] = {spec.split("=")[0]: [int(f) for f in spec.split("=")[1].split(",")] for spec in a.frame}
    if a.res:
        req["res"] = [int(v) for v in a.res.split("x")]
    if a.diffuse:
        req["diffuse"] = os.path.abspath(a.diffuse)
    run_worker(req)
    print(contact_sheet(a.out, a.tag, os.path.join(a.out, f"sheet_{a.tag}.png"), cell=(120, 160)))


def cmd_compare(a):
    from PIL import Image
    rows = a.row
    w, h = 320, 440
    sheet = Image.new("RGB", (w * max(len(r) for r in rows), h * len(rows)), "white")
    for i, row in enumerate(rows):
        for j, p in enumerate(row):
            sheet.paste(Image.open(p).convert("RGB").resize((w, h)), (j * w, i * h))
    sheet.save(a.out)
    print(a.out)


def cmd_blender(a):
    script = Path(a.script) if Path(a.script).is_absolute() else Path(__file__).resolve().parent / a.script
    cmd = [blender_exe(), "--background", "--factory-startup", "--addons", "bl_ext.user_default.io_pdx_mesh",
           "--python", str(script), "--", os.path.abspath(a.config)]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    keep = [l for l in (proc.stdout + proc.stderr).splitlines()
            if l.startswith(("FINAL", "ITEMS", "SURVEY", "LIMBS", "KEYS", "SKELETON", "IMPORT")) or "Error" in l or "Traceback" in l or l.startswith("  File")]
    print("\n".join(keep))
    if proc.returncode != 0 or any("Traceback" in l for l in keep):
        sys.exit(proc.returncode or 1)
    out_dir = json.load(open(a.config, encoding="utf-8")).get("review", {}).get("out_dir")
    if out_dir and os.path.isdir(out_dir):
        print(review_sheet(out_dir))


def review_sheet(out_dir, cell=(150, 200)):
    """Grid of <tag>__<frame>__<target>__<view>.png renders: one row per (tag, target), frames x views across."""
    from PIL import Image, ImageDraw
    rx = re.compile(r"^(.+)__(\d{3})__([^_].*?)__([a-z_]+)\.png$")
    rows = {}
    for f in sorted(glob.glob(os.path.join(out_dir, "*__*__*__*.png"))):
        m = rx.match(os.path.basename(f))
        if m:
            rows.setdefault((m.group(1), m.group(3)), []).append((int(m.group(2)), m.group(4), f))
    if not rows:
        return None
    w, h = cell
    ncol = max(len(v) for v in rows.values())
    sheet = Image.new("RGB", (w * ncol, h * len(rows)), "white")
    for i, key in enumerate(sorted(rows, key=lambda k: (k[0] != "rest", k))):
        for j, (fr, view, f) in enumerate(sorted(rows[key])):
            im = Image.open(f).convert("RGB").resize((w, h))
            ImageDraw.Draw(im).text((3, 3), f"{key[0][-14:]} {key[1][:9]} {fr} {view[:5]}", fill="red")
            sheet.paste(im, (j * w, i * h))
    dest = os.path.join(out_dir, "sheet_items.png")
    sheet.save(dest)
    return dest


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("triage"); t.add_argument("--model", action="append", required=True); t.add_argument("--out", required=True); t.add_argument("--samples", type=int, default=5)
    l = sub.add_parser("legacy-ref"); l.add_argument("--folder", required=True); l.add_argument("--out", required=True); l.add_argument("--view", action="append")
    g = sub.add_parser("glb-ref"); g.add_argument("--glb", required=True); g.add_argument("--out", required=True); g.add_argument("--face", action="store_true")
    c = sub.add_parser("actions"); c.add_argument("--blend", required=True); c.add_argument("--armature", required=True)
    c.add_argument("--mesh", action="append", required=True); c.add_argument("--action", action="append", required=True)
    c.add_argument("--out", required=True); c.add_argument("--tag", default="act"); c.add_argument("--samples", type=int, default=8)
    c.add_argument("--view", action="append"); c.add_argument("--humanoid", action="store_true"); c.add_argument("--bones")
    c.add_argument("--frame", action="append", help="action=f1,f2,... renders exactly these frames for that action")
    c.add_argument("--res", help="WIDTHxHEIGHT per render, default 360x480")
    c.add_argument("--diffuse", help="image to bind for review renders, e.g. the atlas base_color.png of an atlased model")
    b = sub.add_parser("blender"); b.add_argument("--script", required=True); b.add_argument("--config", required=True)
    m = sub.add_parser("compare"); m.add_argument("--row", nargs="+", action="append", required=True); m.add_argument("--out", required=True)
    a = p.parse_args()
    {"triage": cmd_triage, "legacy-ref": cmd_legacy_ref, "glb-ref": cmd_glb_ref, "actions": cmd_actions, "compare": cmd_compare, "blender": cmd_blender}[a.cmd](a)


if __name__ == "__main__":
    main()
