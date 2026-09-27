"""Finalize ingested provider actions for export inside the live Blender Lab session.

Call from a Lab ``execute_blender_code`` request:

    import sys; sys.path.insert(0, r"<mod>/.tools/3d_pipeline/review")
    import importlib, lab_finalize; importlib.reload(lab_finalize)
    lab_finalize.run(r"<config.json>")

Config (JSON):
{
  "blend": "<abs path of the last intake checkpoint>",
  "out": "<abs path of the grounded checkpoint to write>",
  "prefix": "chaosx_unit",                      # actions are <prefix>_<role>
  "roles": ["idle", "move", ...],
  "replace": {"<prefix>_idle": "<prefix>_idle2"},  # optional: retire a rejected action for its replacement
  "armature": "Armature.001", "meshes": ["char1.001"]
}

Steps: retire replaced actions, ground every role (lab_actions.ground_all: root keyed so the
lowest vertex sits 4 mm above the floor, slot identifiers repaired, NLA/drivers cleared, orphan
materials and unused images purged), then save to "out". Returns the per-role offset ranges.
Do not bind preview textures here: extra images break the partition step's image-identity proof.
"""
import importlib
import json

import bpy

import lab_actions as la


def run(config_path):
    importlib.reload(la)
    cfg = json.load(open(config_path, encoding="utf-8"))
    bpy.ops.wm.open_mainfile(filepath=cfg["blend"])
    rig = bpy.data.objects[cfg.get("armature", "Armature.001")]
    meshes = [bpy.data.objects[n] for n in cfg.get("meshes", ["char1.001"])]
    for old, new in cfg.get("replace", {}).items():
        bpy.data.actions[old].name = "rejected_" + old
        bpy.data.actions[new].name = old
    result = la.ground_all(rig, meshes, cfg["prefix"], cfg["roles"])
    bpy.ops.wm.save_as_mainfile(filepath=cfg["out"])
    summary = {k: (v.get("offset_range") if isinstance(v, dict) else v) for k, v in result.items()}
    print("FINAL", json.dumps(summary))
    return summary
