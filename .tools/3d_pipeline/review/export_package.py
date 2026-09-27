"""Export a reviewed unit checkpoint and prove every exported byte by reimport.

Runs through the locked adapter: export_mesh, export_animation per role, and
reimport_export per role. Writes <job>/<out>/export_report.json with file hashes, stream
counts, per-role frame ranges, and the reimport ground-contact range for each sampled frame.
Optionally installs the proven files into a runtime folder with matching names.

Usage:
  python .tools/3d_pipeline/review/export_package.py --job zombies \
      --blend blender/working/soldier_v3b/blender/checkpoints/21b_export_batches.blend \
      --stem chaosx_zombies --out export/v3 \
      --role idle=chaosx_zombies_idle --role move=chaosx_zombies_move ... \
      [--install gfx/models/units/chaosx_zombies --textures <dir with <stem>_*.dds>]

The .mesh and .anim files are named <stem>.mesh and <stem>_<role>.anim; --install copies them
(and the three DDS maps) into the mod-relative runtime folder and records hash parity.
"""
import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import provider_intake as pi  # noqa: E402

MOD = pi.MOD


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--job", required=True)
    p.add_argument("--blend", required=True, help="job-relative export checkpoint (created by --partition-from when given)")
    p.add_argument("--partition-from", help="job-relative grounded checkpoint to partition into --blend first")
    p.add_argument("--armature", default="Armature.001")
    p.add_argument("--mesh-name", action="append", help="mesh object(s) to partition, default char1.001")
    p.add_argument("--stem", required=True)
    p.add_argument("--out", required=True, help="job-relative export folder")
    p.add_argument("--role", action="append", required=True, help="role=action_name")
    p.add_argument("--install", help="mod-relative runtime folder")
    p.add_argument("--textures", help="job-relative (or absolute) folder containing <stem>_diffuse/_specular/_normal.dds")
    a = p.parse_args()

    job = pi.job_root(a.job)
    if a.partition_from:
        part = pi.adapter("partition_skeletal_mesh_export_batches", {
            "job_id": a.job, "blend_rel": a.partition_from, "expected_source_sha256": digest(job / a.partition_from),
            "checkpoint_rel": a.blend, "target_armature_name": a.armature, "target_mesh_names": a.mesh_name or ["char1.001"]})
        print("partition", part.get("status"), flush=True)
    report = {"blend": a.blend, "blend_sha256": digest(job / a.blend), "roles": {}}
    mesh_rel = f"{a.out}/{a.stem}.mesh"
    mesh = pi.adapter("export_mesh", {"job_id": a.job, "blend_rel": a.blend, "output_rel": mesh_rel})
    report["mesh"] = {"rel": mesh_rel, "sha256": digest(job / mesh_rel), "streams": mesh.get("mesh_streams"),
                      "geometry": mesh.get("geometry")}
    print("mesh", report["mesh"]["sha256"][:12], len(mesh.get("mesh_streams") or []), "streams", flush=True)
    for spec in a.role:
        role, action = spec.split("=", 1)
        anim_rel = f"{a.out}/{a.stem}_{role}.anim"
        exp = pi.adapter("export_animation", {"job_id": a.job, "blend_rel": a.blend, "action_name": action, "output_rel": anim_rel})
        proof = pi.adapter("reimport_export", {"job_id": a.job, "mesh_rel": mesh_rel, "anim_rel": anim_rel,
                                               "proof_name": f"{Path(a.out).name}_{role}"})
        contact = [b["ground_contact_z"] for b in proof.get("animation_bounds", [])]
        entry = {"action": action, "anim_rel": anim_rel, "sha256": digest(job / anim_rel), "bytes": exp.get("anim_bytes"),
                 "frames": [exp.get("frame_start"), exp.get("frame_end")], "fps": exp.get("fps"),
                 "reimport_contact_min_max": [min(contact), max(contact)] if contact else None,
                 "proof_blend": proof.get("proof_blend"), "previews": proof.get("previews", [])[:3]}
        # An .anim of a few KB means no channel animated: usually an unbound action slot. Small rigs
        # (a vehicle with a handful of bones) legitimately stay near this size; check their reimport.
        if (exp.get("anim_bytes") or 0) < 10000:
            entry["warning"] = "suspiciously small .anim; check the action slot binds to the armature"
        report["roles"][role] = entry
        print(role, entry["frames"], entry["bytes"], "contact", entry["reimport_contact_min_max"], entry.get("warning", ""), flush=True)
    if a.install:
        dest = MOD / a.install
        dest.mkdir(parents=True, exist_ok=True)
        installed = {}
        files = [job / mesh_rel] + [job / r["anim_rel"] for r in report["roles"].values()]
        if a.textures:
            tex = Path(a.textures) if Path(a.textures).is_absolute() else job / a.textures
            files += [tex / f"{a.stem}_{m}.dds" for m in ("diffuse", "specular", "normal")]
        for src in files:
            shutil.copy2(src, dest / src.name)
            installed[src.name] = {"source": digest(src), "runtime": digest(dest / src.name)}
            assert installed[src.name]["source"] == installed[src.name]["runtime"]
        report["installed"] = {"folder": a.install, "files": installed}
        print("installed", len(installed), "files to", a.install)
    (job / a.out / "export_report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    print("REPORT", job / a.out / "export_report.json")


if __name__ == "__main__":
    main()
