"""Read-only Blender review worker for Chaos Redux unit models.

Run through ``review_cli.py``; it launches the locked Blender in background mode with
``--python blender_review.py -- <request.json>``. Every mode is read-only: it imports
assets into a disposable scene, renders PNG evidence, measures, and writes a JSON report.

Modes
- ``triage``: import shipped runtime ``.mesh`` + every ``.anim`` in a folder, render
  sampled frames from front and side, and measure per-action ground contact and height.
- ``legacy_ref``: import a shipped ``.mesh`` with its diffuse and render lit reference views.
- ``glb_ref``: import a provider GLB and render lit views (optionally a face close-up).
- ``actions``: open a working ``.blend`` and render the named actions of its armature from
  several views, scanning every frame for floor contact and returning phase measurements
  (hand reach peaks, foot plants, jaw opens, spine height) for sound and event timing.
"""
import json
import os
import sys

import bpy
import mathutils

REQ = json.load(open(sys.argv[sys.argv.index("--") + 1], encoding="utf-8"))
VIEWS = {"front": (0, -1, 0), "side": (1, 0, 0), "three_quarter": (0.6, -0.8, 0), "rear": (0, 1, 0), "left": (-1, 0, 0)}


def pdx():
    from bl_ext.user_default.io_pdx_mesh.pdx_blender import blender_import_export as m  # noqa: E402
    return m


def clear():
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.armatures, bpy.data.actions, bpy.data.materials,
                 bpy.data.cameras, bpy.data.lights):
        for item in list(coll):
            coll.remove(item)


def meshes():
    return [o for o in bpy.data.objects if o.type == "MESH" and not o.name.startswith("CX_")]


def bounds(objs, step=1):
    dg = bpy.context.evaluated_depsgraph_get()
    pts = []
    for o in objs:
        ev = o.evaluated_get(dg)
        mw = ev.matrix_world
        pts.extend(mw @ v.co for i, v in enumerate(ev.data.vertices) if i % step == 0)
    lo = mathutils.Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    hi = mathutils.Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return lo, hi


def setup_render(engine, res, background=(0.35, 0.35, 0.37)):
    sc = bpy.context.scene
    sc.render.engine = engine
    sc.render.resolution_x, sc.render.resolution_y = res
    if engine == "BLENDER_WORKBENCH":
        sc.display.shading.light = "STUDIO"
        sc.display.shading.color_type = "TEXTURE"
    else:
        sc.world = sc.world or bpy.data.worlds.new("CX_World")
        sc.world.use_nodes = True
        bg = sc.world.node_tree.nodes.get("Background")
        bg.inputs[0].default_value = (*background, 1)
        for name, (d, energy) in {"key": ((-0.5, -1, 0.8), 3.5), "fill": ((1, -0.6, 0.3), 1.5), "rim": ((0, 1, 0.6), 2.0)}.items():
            light = bpy.data.lights.new("CX_" + name, "SUN")
            light.energy = energy
            obj = bpy.data.objects.new("CX_" + name, light)
            sc.collection.objects.link(obj)
            obj.rotation_euler = (-mathutils.Vector(d)).to_track_quat("-Z", "Y").to_euler()
    cam = bpy.data.objects.new("CX_Camera", bpy.data.cameras.new("CX_Camera"))
    sc.collection.objects.link(cam)
    cam.data.type = "ORTHO"
    sc.camera = cam
    return cam


def shoot(cam, objs, view, path, margin=1.12, step=7):
    lo, hi = bounds(objs, step)
    c = (lo + hi) / 2
    ext = max((hi - lo).length, 1e-3)
    d = mathutils.Vector(VIEWS[view] if isinstance(view, str) else view).normalized()
    cam.location = c + d * ext * 4
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    cam.data.ortho_scale = ext * margin
    cam.data.clip_start, cam.data.clip_end = ext * 0.01, ext * 20
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)


def bind_diffuse(objs, image_path):
    if not image_path or not os.path.exists(image_path):
        return False
    img = bpy.data.images.load(image_path)
    for o in objs:
        for m in o.data.materials:
            if not m:
                continue
            nt = m.node_tree
            for n in list(nt.nodes):
                nt.nodes.remove(n)
            out = nt.nodes.new("ShaderNodeOutputMaterial")
            bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
            tex = nt.nodes.new("ShaderNodeTexImage")
            tex.image = img
            bsdf.inputs["Roughness"].default_value = 0.8
            nt.links.new(tex.outputs[0], bsdf.inputs["Base Color"])
            nt.links.new(bsdf.outputs[0], out.inputs[0])
    return True


def use_action(rig, action):
    rig.animation_data_create()
    rig.animation_data.action = action
    if action.slots:
        rig.animation_data.action_slot = action.slots[0]


def contact_scan(objs, f0, f1, stride=1):
    sc = bpy.context.scene
    out = []
    for f in range(f0, f1 + 1, stride):
        sc.frame_set(f)
        lo, hi = bounds(objs, 5)
        out.append((f, round(lo.z, 4), round(hi.z, 4)))
    return out


def import_runtime(folder, mesh_name):
    m = pdx()
    m.import_meshfile(os.path.join(folder, mesh_name), imp_mesh=True, imp_skel=True, imp_locs=True, join_materials=True, bonespace=False)
    return m


def mode_triage():
    report = {}
    out = REQ["out_dir"]
    os.makedirs(out, exist_ok=True)
    for spec in REQ["models"]:
        clear()
        folder = spec["folder"]
        m = import_runtime(folder, spec["mesh"])
        objs = meshes()
        rig = next(o for o in bpy.data.objects if o.type == "ARMATURE")
        cam = setup_render("BLENDER_WORKBENCH", REQ.get("res", [300, 400]))
        diffuse = bind_diffuse(objs, os.path.join(folder, spec.get("diffuse", "")))
        rep = {"tris": sum(sum(len(p.vertices) - 2 for p in o.data.polygons) for o in objs), "objects": len(objs),
               "bones": len(rig.data.bones), "diffuse": diffuse, "anims": {}}
        for anim in sorted(f for f in os.listdir(folder) if f.endswith(".anim")):
            role = anim[:-5]
            # The importer writes into the rig's bound action when one exists, so every .anim after the
            # first would inherit the previous action's keys and frame range. Unbind and reset first.
            if rig.animation_data:
                rig.animation_data.action = None
            for pb in rig.pose.bones:
                pb.location = (0, 0, 0)
                pb.rotation_quaternion = (1, 0, 0, 0)
                pb.scale = (1, 1, 1)
            before = set(bpy.data.actions)
            m.import_animfile(os.path.join(folder, anim), frame_start=1)
            new = list(set(bpy.data.actions) - before)
            act = new[0] if new else rig.animation_data.action
            act.name = role
            use_action(rig, act)
            f0, f1 = map(int, act.frame_range)
            scan = contact_scan(objs, f0, f1, max(1, (f1 - f0) // 24))
            frames = sorted({round(f0 + (f1 - f0) * i / (REQ.get("samples", 5) - 1)) for i in range(REQ.get("samples", 5))})
            for f in frames:
                bpy.context.scene.frame_set(f)
                for view in ("front", "side"):
                    shoot(cam, objs, view, os.path.join(out, f"{spec['name']}__{role}__{f:03d}__{view}.png"), step=9)
            rep["anims"][role] = {"frames": [f0, f1], "fps": bpy.context.scene.render.fps,
                                  "min_z_range": [min(s[1] for s in scan), max(s[1] for s in scan)],
                                  "max_z_range": [min(s[2] for s in scan), max(s[2] for s in scan)], "rendered": frames}
        report[spec["name"]] = rep
        print("TRIAGE", spec["name"], json.dumps(rep))
    json.dump(report, open(os.path.join(out, REQ.get("report", "triage_report.json")), "w"), indent=1)


def mode_legacy_ref():
    clear()
    import_runtime(REQ["folder"], REQ["mesh"])
    objs = meshes()
    bind_diffuse(objs, os.path.join(REQ["folder"], REQ.get("diffuse", "")))
    cam = setup_render("BLENDER_EEVEE", REQ.get("res", [1024, 1536]), (0.92, 0.92, 0.92))
    for view in REQ.get("views", ["front", "three_quarter", "side"]):
        shoot(cam, objs, view, f"{REQ['out']}_{view}.png", step=3)


def mode_glb_ref():
    clear()
    bpy.ops.import_scene.gltf(filepath=REQ["glb"])
    objs = meshes()
    cam = setup_render("BLENDER_EEVEE", REQ.get("res", [768, 1024]))
    for view in REQ.get("views", ["front", "three_quarter", "side", "rear"]):
        shoot(cam, objs, view, f"{REQ['out']}_{view}.png", margin=1.1, step=3)
    lo, hi = bounds(objs, 3)
    if REQ.get("face"):
        h = hi.z - lo.z
        cam.data.ortho_scale = h * 0.22
        cam.location = mathutils.Vector(((lo.x + hi.x) / 2, lo.y - h * 4, hi.z - h * 0.1))
        cam.rotation_euler = mathutils.Vector((0, 1, 0)).to_track_quat("-Z", "Y").to_euler()
        bpy.context.scene.render.filepath = f"{REQ['out']}_face.png"
        bpy.ops.render.render(write_still=True)
    tris = sum(sum(len(p.vertices) - 2 for p in o.data.polygons) for o in objs)
    json.dump({"tris": tris, "dims": list(hi - lo)}, open(f"{REQ['out']}_stats.json", "w"))
    print("GLB", tris, list(hi - lo))


def peaks(values, frames, floor):
    return [(frames[i], round(values[i], 3)) for i in range(1, len(values) - 1)
            if values[i] > values[i - 1] and values[i] >= values[i + 1] and values[i] > floor]


def mode_actions():
    bpy.ops.wm.open_mainfile(filepath=REQ["blend"])
    rig = bpy.data.objects[REQ["armature"]]
    objs = [bpy.data.objects[n] for n in REQ["meshes"]]
    out = REQ["out_dir"]
    os.makedirs(out, exist_ok=True)
    # An atlased model (held items packed by lab_items.py) keeps its provider images in the blend
    # while its UVs point into the atlas, so its review binds the atlas diffuse in this disposable scene.
    bind_diffuse(objs, REQ.get("diffuse", ""))
    cam = setup_render("BLENDER_WORKBENCH", REQ.get("res", [360, 480]))
    mw = rig.matrix_world
    names = REQ.get("bones", {})
    report = {}
    for act_name in REQ["actions"]:
        act = bpy.data.actions[act_name]
        use_action(rig, act)
        f0, f1 = map(int, act.frame_range)
        frames = list(range(f0, f1 + 1))
        scan = contact_scan(objs, f0, f1)
        measure = {k: [] for k in ("reach_l", "reach_r", "toe_l", "toe_r", "jaw", "spine_z")}
        for f in frames:
            bpy.context.scene.frame_set(f)
            pb = rig.pose.bones
            fwd = mathutils.Vector(REQ.get("forward", [0, -1, 0]))
            if names.get("hand_l") and names["hand_l"] in pb:
                measure["reach_l"].append((mw @ pb[names["hand_l"]].head).dot(fwd))
                measure["reach_r"].append((mw @ pb[names["hand_r"]].head).dot(fwd))
            if names.get("toe_l") and names["toe_l"] in pb:
                measure["toe_l"].append((mw @ pb[names["toe_l"]].head).z)
                measure["toe_r"].append((mw @ pb[names["toe_r"]].head).z)
            if names.get("jaw") and names["jaw"] in pb:
                measure["jaw"].append(pb[names["jaw"]].rotation_quaternion.angle * 57.2958)
            if names.get("spine") and names["spine"] in pb:
                measure["spine_z"].append((mw @ pb[names["spine"]].head).z)
        rep = {"frames": [f0, f1], "fps": bpy.context.scene.render.fps,
               "min_z": [min(s[1] for s in scan), max(s[1] for s in scan)],
               "below_floor_frames": [s[0] for s in scan if s[1] < -REQ.get("floor_tolerance", 0.01)],
               "floating_frames": [s[0] for s in scan if s[1] > REQ.get("float_tolerance", 0.03)]}
        if measure["reach_l"]:
            fl = REQ.get("reach_floor", 1.2)
            rep["reach_peaks_l"] = peaks(measure["reach_l"], frames, fl)
            rep["reach_peaks_r"] = peaks(measure["reach_r"], frames, fl)
        for side in ("l", "r"):
            z = measure["toe_" + side]
            if z:
                base = min(z)
                lift = REQ.get("plant_lift", 0.08)
                rep["plants_" + side] = [frames[i] for i in range(1, len(z)) if z[i - 1] - base > lift and z[i] - base <= lift]
        if measure["jaw"]:
            rep["jaw_peaks"] = peaks(measure["jaw"], frames, REQ.get("jaw_floor", 8))
        if measure["spine_z"]:
            rep["spine_z_first_last"] = [round(measure["spine_z"][0], 3), round(measure["spine_z"][-1], 3)]
            drops = [frames[i] for i in range(1, len(frames)) if measure["spine_z"][i - 1] - measure["spine_z"][i] > REQ.get("impact_drop", 0.5)]
            rep["spine_fast_drops"] = drops
        n = REQ.get("samples", 8)
        sample = REQ.get("frames", {}).get(act_name) or sorted({round(f0 + (f1 - f0) * i / (n - 1)) for i in range(n)})
        for f in sample:
            bpy.context.scene.frame_set(f)
            for view in REQ.get("views", ["front", "side", "three_quarter"]):
                shoot(cam, objs, view, os.path.join(out, f"{REQ.get('tag', 'act')}__{act_name}__{f:03d}__{view}.png"))
        report[act_name] = rep
        print("ACTION", act_name, json.dumps(rep))
    json.dump(report, open(os.path.join(out, REQ.get("report", "actions_report.json")), "w"), indent=1)


{"triage": mode_triage, "legacy_ref": mode_legacy_ref, "glb_ref": mode_glb_ref, "actions": mode_actions}[REQ["mode"]]()
