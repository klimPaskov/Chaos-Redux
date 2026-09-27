"""Ingest Meshy provider actions onto a prepared rig through the locked adapter.

For every role in a manifest, this tool hashes the downloaded FBX, asks the adapter
(`inspect_animation_source`) for the source armature and the longest action, writes a
verified provenance receipt, then chains `import_animation_action` from the prepared
checkpoint, one new sibling checkpoint per role. It never edits motion; it only records
and forwards provider results that were downloaded by the agent.

Manifest (JSON):
{
  "job_id": "zombies",
  "namespace": "blender/working/soldier_v3b",           # job-relative
  "base_blend": "blender/checkpoints/05_pre_export.blend",  # namespace-relative
  "target_armature": "Armature.001",
  "action_prefix": "chaosx_zombies",
  "roles": {
    "idle":   {"fbx": "anims/idle.fbx",   "task": "<meshy animate task id>", "kind": "meshy_animate", "preset": 336},
    "attack": {"fbx": "anims/attack.fbx", "task": "<meshy animate task id>", "kind": "meshy_animate",
               "motion_task": "<text-to-motion task id>", "prompt": "..."}
  }
}
fbx paths are namespace-relative. Roles are imported in manifest order.

Usage: python .tools/3d_pipeline/review/provider_intake.py <manifest.json>
The final checkpoint path and every per-role result are written to <namespace>/intake_report.json.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIPE = HERE.parent
sys.path.insert(0, str(PIPE / "lib"))
from mcp_stdio import call_stdio  # noqa: E402

MOD = PIPE.parent.parent
ADAPTER = ["cmd.exe", "/d", "/c", "call", str(PIPE / "wrappers" / "run_blender_hoi4_adapter.cmd")]
CONFIG = json.loads((PIPE / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))


def job_root(job_id):
    override = CONFIG.get("job_overrides", {}).get(job_id)
    return Path(override) if override else Path(CONFIG["job_root"]) / job_id


def adapter(tool, args):
    r = call_stdio(ADAPTER, tool="chaosx_blender_hoi4_" + tool, arguments=args, cwd=MOD, timeout_seconds=3600)
    sc = r.get("structuredContent") or r.get("result", {}).get("structuredContent")
    if sc is None:
        content = r.get("content") or r.get("result", {}).get("content") or []
        text = "".join(c.get("text", "") for c in content)
        try:
            sc = json.loads(text)
        except json.JSONDecodeError:
            # The adapter reports only "evidence: <file>"; the worker's final line there is the real error.
            detail = ""
            if "evidence: " in text:
                ev = Path(text.split("evidence: ")[-1].strip())
                if ev.exists():
                    lines = [l for l in ev.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
                    detail = " | " + (lines[-1] if lines else "")
            raise RuntimeError(f"{tool} failed: {text[:600]}{detail[:1500]}")
    if isinstance(sc, dict) and "result" in sc:
        sc = sc["result"]
    if r.get("isError") or (isinstance(sc, dict) and sc.get("error")):
        raise RuntimeError(f"{tool} failed: {json.dumps(sc)[:2000]}")
    return sc


MESHY = ["cmd.exe", "/d", "/c", "call", str(PIPE / "wrappers" / "run_meshy_mcp.cmd")]


def meshy(tool, args):
    r = call_stdio(MESHY, tool=tool, arguments=args, cwd=MOD, timeout_seconds=900)
    content = r.get("content") or r.get("result", {}).get("content") or []
    text = "".join(c.get("text", "") for c in content)
    if r.get("isError") or r.get("result", {}).get("isError") or text.startswith("Error"):
        raise RuntimeError(f"{tool}: {text[:800]}")
    return json.loads(text) if text.strip().startswith("{") else text


def download_missing(manifest, job, ns):
    """Download the rig GLB (manifest["rig_task"] -> manifest["rig_glb"]) and every role FBX that is
    not on disk yet, through the locked Meshy MCP route. Waits for unfinished animation tasks."""
    todo = []
    if manifest.get("rig_task") and manifest.get("rig_glb") and not (job / ns / manifest["rig_glb"]).exists():
        todo.append((manifest["rig_task"], "rigging", "glb", manifest["rig_glb"]))
    for spec in manifest["roles"].values():
        if not (job / ns / spec["fbx"]).exists():
            todo.append((spec["task"], "animation", "fbx", spec["fbx"]))
    for task, ttype, fmt, rel in todo:
        status = meshy("meshy_get_task_status", {"task_id": task, "task_type": ttype, "timeout_seconds": 300, "response_format": "json"})
        if isinstance(status, dict) and status.get("status") != "SUCCEEDED":
            raise RuntimeError(f"{task} not finished: {status.get('status')}")
        dest = job / ns / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        got = meshy("meshy_download_model", {"task_id": task, "task_type": ttype, "format": fmt, "save_to": str(dest).replace("\\", "/")})
        print("downloaded", rel, (got.get("sha256") or "")[:12] if isinstance(got, dict) else "", flush=True)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def main():
    manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    job = job_root(manifest["job_id"])
    ns = manifest["namespace"].rstrip("/")
    ns_dir = job / ns
    ns_dir.mkdir(parents=True, exist_ok=True)
    download_missing(manifest, job, ns)
    if "--download-only" in sys.argv:
        return
    prep = manifest.get("prepare")
    if prep and not (ns_dir / manifest["base_blend"]).exists():
        # Calibrate against the installed vanilla mesh named by the asset profile (copied read-only
        # into the namespace, because adapter reference paths are namespace-relative).
        profiles = json.loads((PIPE / "config" / "asset_profiles.json").read_text(encoding="utf-8"))["profiles"]
        ref = dict(profiles[prep.get("profile", "humanoid_unit")]["vanilla_reference"])
        vanilla = Path(json.loads((PIPE / "config" / "dependencies.lock.json").read_text(encoding="utf-8"))
                       .get("vanilla_game_root", "C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")) / ref["mesh"]
        (ns_dir / "reference").mkdir(exist_ok=True)
        import shutil
        shutil.copy2(vanilla, ns_dir / "reference" / vanilla.name)
        ref["mesh_rel"] = f"reference/{vanilla.name}"
        ref["exclude_name_patterns"] = ref.get("exclude_name_patterns", []) + ["pcube"]
        result = adapter("prepare_candidate", {
            "job_id": manifest["job_id"], "output_namespace_rel": ns, "source_rel": f"{ns}/{manifest['rig_glb']}",
            "asset_kind": prep.get("asset_kind", "humanoid"), "target_height_m": ref["mesh_height"],
            "runtime_stem": manifest["action_prefix"], "runtime_entity_scale": ref["entity_scale"],
            "preserve_geometry_topology": True,
            # Meshy rig downloads include a stray "Icosphere" helper object that inflates the footprint.
            "excluded_provider_objects": prep.get("exclude", ["Icosphere"]),
            "vanilla_reference": ref,
        })
        print("prepared", result.get("geometry", {}).get("triangles"), "tris, dims", result.get("geometry", {}).get("dimensions"), flush=True)
    (ns_dir / "provenance").mkdir(exist_ok=True)
    report = {"roles": {}, "chain": []}
    blend = f"{ns}/{manifest['base_blend']}"
    for index, (role, spec) in enumerate(manifest["roles"].items(), start=10):
        fbx_rel = f"{ns}/{spec['fbx']}"
        digest = sha(job / fbx_rel)
        info = adapter("inspect_animation_source", {"job_id": manifest["job_id"], "source_rel": fbx_rel, "source_sha256": digest})
        action = max(info["actions"], key=lambda a: a["frame_range"][1] - a["frame_range"][0])
        armature = info["armatures"][0]["name"] if info.get("armatures") else ""
        kind = spec.get("kind", "meshy_animate")
        provenance = {
            "verification_status": "verified",
            "source_kind": kind,
            "source_reference_id": spec["task"],
            "source_action_name": action["name"],
            "source_sha256": digest,
            "source_rel": fbx_rel,
            "source_fps": info.get("fps"),
            "source_frame_range": action["frame_range"],
            "source_armature": armature,
            "preset_action_id": spec.get("preset"),
            "motion_task_id": spec.get("motion_task"),
            "motion_prompt": spec.get("prompt"),
        }
        prov_rel = f"{ns}/provenance/{role}.json"
        (job / prov_rel).write_text(json.dumps(provenance, indent=1), encoding="utf-8")
        checkpoint = f"{ns}/blender/checkpoints/{index}_{role}_imported.blend"
        target = f"{manifest['action_prefix']}_{role}"
        request = {
            "job_id": manifest["job_id"], "blend_rel": blend, "source_rel": fbx_rel, "provenance_rel": prov_rel,
            # The source armature is renamed on import when its name collides with the target rig
            # (Armature -> Armature.002), so it is only passed when the manifest pins it explicitly.
            "checkpoint_rel": checkpoint, "source_action_name": action["name"], "source_armature_name": spec.get("source_armature", ""),
            "target_armature_name": manifest["target_armature"], "target_action_name": target, "source_kind": kind,
            "source_reference_id": spec["task"], "source_sha256": digest,
        }
        try:
            result = adapter("import_animation_action", request)
        except RuntimeError as exc:
            # FBX action names carry the importing armature's object name as their first token, so a
            # collision inside the target scene exposes e.g. "Armature.002|...|baselayer" instead of the
            # disposable-scene "Armature|...|baselayer". Accept the renamed id only when exactly one
            # exposed action keeps the identical remainder; the file hash is unchanged.
            log = str(exc)
            evidence = log.split("evidence: ")[-1].strip() if "evidence: " in log else ""
            text = Path(evidence).read_text(encoding="utf-8", errors="replace") if evidence and Path(evidence).exists() else log
            marker = '"available_source_actions": '
            if marker not in text.replace('\\"', '"'):
                raise
            body = text.replace('\\"', '"')
            available = json.loads(body[body.index(marker) + len(marker):].split("]", 1)[0] + "]")
            tail = action["name"].split("|", 1)[1]
            matches = [a for a in available if a.split("|", 1)[1] == tail]
            if len(matches) != 1:
                raise
            provenance["source_action_name"] = matches[0]
            provenance["source_action_name_in_disposable_scene"] = action["name"]
            (job / prov_rel).write_text(json.dumps(provenance, indent=1), encoding="utf-8")
            request["source_action_name"] = matches[0]
            result = adapter("import_animation_action", request)
        report["roles"][role] = {"action": target, "source_action": action["name"], "frames": action["frame_range"],
                                 "checkpoint": checkpoint, "result_keys": sorted(result.keys()) if isinstance(result, dict) else None}
        report["chain"].append(checkpoint)
        blend = checkpoint
        print(f"{role}: {action['name']} {action['frame_range']} -> {target} @ {checkpoint}", flush=True)
    report["final_checkpoint"] = blend
    (ns_dir / "intake_report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    print("FINAL", blend)


if __name__ == "__main__":
    main()
