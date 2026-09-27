"""Write the mechanical runtime registration for an exported unit model.

From an export_report.json (written by export_package.py) this generates:
  gfx/entities/<stem>.gfx                          pdxmesh with one animation id per exported role and
                                                   one meshsettings block per exported stream
  gfx/models/units/<folder>/animation_<stem>.asset one animation registration per role

The entity .asset (states, events, sounds, particles) is authored by hand from the phase review,
because which sound or particle fits a phase is a design decision.

Usage:
  python .tools/3d_pipeline/review/wire_unit.py --report <job>/export/<v>/export_report.json \
      --stem chaosx_demonic_zombies --folder chaosx_demonic_zombies --title "demonic zombie"
"""
import argparse
import json
from pathlib import Path

MOD = Path(__file__).resolve().parents[3]
ROLE_ORDER = ["idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--report", required=True)
    p.add_argument("--stem", required=True)
    p.add_argument("--folder", required=True, help="folder under gfx/models/units")
    p.add_argument("--title", required=True, help="unit description for the file header comments")
    p.add_argument("--gfx", help="override gfx output path (mod-relative)")
    a = p.parse_args()
    rep = json.loads(Path(a.report).read_text(encoding="utf-8"))
    roles = [r for r in ROLE_ORDER if r in rep["roles"]] + [r for r in rep["roles"] if r not in ROLE_ORDER]
    streams = sorted(rep["mesh"]["streams"], key=lambda s: s["mesh_index"])
    tris = sum(s["triangles"] for s in streams)

    lines = [f"# Chaos Redux {a.title} mesh registration.",
             f"# The {tris:,}-triangle body exports as {len(streams)} skinned stream(s) that share one PDX material.", "",
             "objectTypes = {", "\tpdxmesh = {", f'\t\tname = "{a.stem}_mesh"',
             f'\t\tfile = "gfx/models/units/{a.folder}/{a.stem}.mesh"', ""]
    lines += [f'\t\tanimation = {{ id = "{r}" type = "{a.stem}_{r}_animation" }}' for r in roles]
    for s in streams:
        lines += ["", "\t\tmeshsettings = {", f'\t\t\tname = "{s["object_name"]}"', f"\t\t\tindex = {s['mesh_index']}",
                  f'\t\t\ttexture_diffuse = "{a.stem}_diffuse.dds"', f'\t\t\ttexture_specular = "{a.stem}_specular.dds"',
                  f'\t\t\ttexture_normal = "{a.stem}_normal.dds"', '\t\t\tshader = "PdxMeshAdvanced"', "\t\t}"]
    lines += ["\t}", "}", ""]
    gfx = MOD / (a.gfx or f"gfx/entities/{a.stem}.gfx")
    with open(gfx, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))

    anim = [f"# Chaos Redux {a.title} skeletal action registrations.",
            "# Each animation id maps to a reimport-proven export in this folder.", ""]
    anim += [f'animation = {{ name = "{a.stem}_{r}_animation" file = "{a.stem}_{r}.anim" }}' for r in roles]
    with open(MOD / "gfx" / "models" / "units" / a.folder / f"animation_{a.stem}.asset", "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(anim) + "\n")
    print("wrote", gfx.relative_to(MOD), "and", f"gfx/models/units/{a.folder}/animation_{a.stem}.asset", "roles", roles, "streams", len(streams))


if __name__ == "__main__":
    main()
