"""Write the mechanical runtime registration for an exported unit model.

From an export_report.json (written by export_package.py) this generates:
  gfx/entities/<stem>.gfx                          pdxmesh with one animation id per exported role and
                                                   one meshsettings block per exported stream
  gfx/models/units/<folder>/animation_<stem>.asset one animation registration per role

The entity .asset (states, events, sounds, particles) is authored by hand from the phase review,
because which sound or particle fits a phase is a design decision.

--retire <file> (repeatable) removes the unit's previous registration from a shared file when a
rebuilt unit moves to its own files: the pdxmesh block named <stem>_mesh, any entity block whose
pdxmesh is <stem>_mesh, and animation lines whose file lives in <folder>/. Other units are untouched.

Usage:
  python .tools/3d_pipeline/review/wire_unit.py --report <job>/export/<v>/export_report.json \
      --stem chaosx_demonic_zombies --folder chaosx_demonic_zombies --title "demonic zombie"
"""
import argparse
import json
from pathlib import Path

MOD = Path(__file__).resolve().parents[3]
ROLE_ORDER = ["idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"]


def _blocks(text, key):
    """Yield (start, end) spans of top-level-or-nested `key = { ... }` blocks, brace matched."""
    import re
    for m in re.finditer(r"(?m)^[ \t]*" + key + r"\s*=\s*\{", text):
        depth, i = 0, m.end() - 1
        while i < len(text):
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
            if depth == 0:
                break
        end = text.find(chr(10), i)
        yield m.start(), (len(text) if end < 0 else end + 1)


def retire(path, stem, folder):
    raw = path.read_bytes()
    bom = raw.startswith(bytes((0xEF, 0xBB, 0xBF)))
    text = raw.decode("utf-8-sig")
    mesh = f'"{stem}_mesh"'
    # A pdxmesh block is matched by its own name line (the first lines), an entity block by its pdxmesh reference.
    spans = [(a, b) for a, b in _blocks(text, "pdxmesh") if f"name = {mesh}" in text[a:a + 200]]
    spans += [(a, b) for a, b in _blocks(text, "entity") if f"pdxmesh = {mesh}" in text[a:b]]
    lines = [ln for ln in text.splitlines(keepends=True)
             if ln.lstrip().startswith("animation = {") and f'file = "{folder}/' in ln]
    for a, b in sorted(spans, reverse=True):
        text = text[:a] + text[b:]
    for ln in lines:
        text = text.replace(ln, "", 1)
    with open(path, "w", encoding="utf-8-sig" if bom else "utf-8", newline=chr(10)) as fh:
        fh.write(text)
    return len(spans) + len(lines)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--report", required=True)
    p.add_argument("--stem", required=True)
    p.add_argument("--folder", required=True, help="folder under gfx/models/units")
    p.add_argument("--title", required=True, help="unit description for the file header comments")
    p.add_argument("--gfx", help="override gfx output path (mod-relative)")
    p.add_argument("--retire", action="append", default=[], help="shared .gfx/.asset file to remove this unit's old registration from")
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
    for shared in a.retire:
        print("retired", retire(MOD / shared, a.stem, a.folder), "blocks/lines from", shared)
    print("wrote", gfx.relative_to(MOD), "and", f"gfx/models/units/{a.folder}/animation_{a.stem}.asset", "roles", roles, "streams", len(streams))


if __name__ == "__main__":
    main()
