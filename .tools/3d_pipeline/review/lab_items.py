"""Attach separately generated held items (weapons, staffs, shields) to a rigged unit.

Every held item is its own Meshy geometry task (the body is always generated empty-handed).
This worker places each item rigidly on the bone that carries it, packs the body and item
textures into one atlas so the unit keeps a single PDX material, joins the items into the body
mesh with a 1.0 weight on the carrying bone, and writes a new checkpoint plus review evidence.
It never creates or edits motion: grip transforms are explicit numbers the agent chose after
looking at the hand close-ups, and the contact report says where a pose needs live correction.

Run headless (no Lab socket needed):
    blender --background --factory-startup --python lab_items.py -- <config.json>
or inside a Lab session: ``import lab_items; lab_items.run(r"<config.json>")``.

Config (JSON, absolute paths):
{
  "blend": "<grounded checkpoint from lab_finalize>",
  "out":   "<checkpoint to write>",           # omit (or "review_only": true) to only render/measure
  "armature": "Armature.001", "body": "char1.001",
  "body_textures": "<dir with base_color/metallic/roughness/normal.png of the body>",
  "atlas": {"dir": "<output dir for the atlas PNGs>", "size": 2048, "cell": 0.25},
  "items": [{
     "name": "stone_axe", "glb": "<item.glb>", "textures": "<item textures dir>",
     "bone": "RightHand",
     "length": 0.55,             # longest item dimension as a fraction of the rig's rest height
     "head": "-X",               # item-local direction from the grip to the head (axe head, spear tip)
     "side": "+Y",               # optional item-local facing (blade edge, hammer face); default: head mass offset
     "head_to": "Z", "side_to": "-X",   # bone-local axes those directions are laid along
     "roll": 0,                  # optional degrees about the head axis
     "grip_along": 0.85,         # grip position from butt (0) to head (1); centred on the real shaft section
     "offset": [0, 0.03, 0]      # grip position in the bone frame, in fractions of rig height
  }],
  "contacts": [{"item": "halberd", "bone": "LeftHand", "offset": [0, 0.03, 0]}],   # off-hand checks
  "floor_items": {"actions": ["chaosx_x_death"], "clearance": 0.01},   # optional measured floor fix
  # items_report.json records each item's head_bone_local: pass it to the adapter's
  # author_locator (parent_bone = the item's bone) for a muzzle or nozzle particle node.
  "review": {"out_dir": "<dir>", "actions": ["chaosx_x_attack"], "samples": 6, "res": [420, 560],
             "closeup": 0.35}   # optional hand close-ups, width as a fraction of the framed extent
}

Atlas: the body keeps UV v in [0, 1 - cell] (full width); item k gets the square cell
u in [k*cell, (k+1)*cell], v in [1 - cell, 1]. The atlas PNGs keep the provider file names, so
``pdx_textures.py --textures <atlas dir>`` converts them unchanged. Item materials and images are
removed after the join, so the partition step's image-identity proof still sees only the body set.

Contacts: for every sampled frame of every action, the distance from each off-hand grip point to
the item's long axis segment, and the lowest item point against the floor, go into
``items_report.json``. Large off-hand gaps mean the provider action was not authored for this
item and needs a live pose correction before export.
"""
import json
import math
import os
import sys

import bpy
import mathutils
from mathutils import Euler, Matrix, Vector

CHANNELS = ("base_color", "metallic", "roughness", "normal")


def _cfg():
    return json.load(open(sys.argv[sys.argv.index("--") + 1], encoding="utf-8"))


def _import_item(spec):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=spec["glb"])
    new = [o for o in bpy.data.objects if o not in before]
    parts = [o for o in new if o.type == "MESH"]
    for o in new:
        if o.type != "MESH":
            bpy.data.objects.remove(o)
    bpy.ops.object.select_all(action="DESELECT")
    for o in parts:
        o.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    if len(parts) > 1:
        bpy.ops.object.join()
    item = bpy.context.view_layer.objects.active
    item.parent = None
    item.data.transform(item.matrix_world)
    item.matrix_world = Matrix.Identity(4)
    item.name = "CXITEM_" + spec["name"]
    return item


def _rest_height(body):
    mw = body.matrix_world
    zs = [(mw @ v.co).z for v in body.data.vertices]
    return max(zs) - min(zs)


def _axis(token):
    """'+X', '-z', 'Y' -> unit Vector."""
    token = token.strip().upper()
    sign = -1.0 if token.startswith("-") else 1.0
    v = Vector((0.0, 0.0, 0.0))
    v["XYZ".index(token[-1])] = sign
    return v


def bone_frame(rig, bone_name, pose=False):
    """World matrix of a bone without scale. Meshy rigs carry a 0.05 object scale and their bone
    lengths are meaningless (tails sit far from the next joint), so frames are rotation + head only."""
    m = rig.matrix_world @ (rig.pose.bones[bone_name].matrix if pose else rig.data.bones[bone_name].matrix_local)
    return Matrix.LocRotScale(m.translation, m.to_quaternion(), None)


def _place(item, rig, spec, height):
    """Put the item's grip on the carrying bone. Orientation is semantic: the item-local direction
    from the grip to the head ("head", e.g. "-X") is laid along the bone-local axis "head_to", and the
    item-local facing direction ("side": blade edge, hammer face, shield front) along "side_to";
    "roll" turns about the head axis afterwards. "grip_along" is the grip position from the butt (0)
    to the head (1); its cross-section centroid is measured from the real vertices so the bone sits
    on the shaft, not at the bounding-box centre. Sizes and offsets are fractions of rig height."""
    co = [v.co.copy() for v in item.data.vertices]
    lo = Vector((min(c.x for c in co), min(c.y for c in co), min(c.z for c in co)))
    hi = Vector((max(c.x for c in co), max(c.y for c in co), max(c.z for c in co)))
    size = hi - lo
    scale = spec["length"] * height / max(size)
    head = _axis(spec["head"])
    k = [i for i in range(3) if head[i]][0]
    butt_t = 0.0 if head[k] > 0 else 1.0
    along = lo[k] + size[k] * (butt_t + (1 - 2 * butt_t) * spec.get("grip_along", 0.5))
    if spec.get("grip"):
        grip = Vector([lo[i] + size[i] * spec["grip"][i] for i in range(3)])
    else:
        band = [c for c in co if abs(c[k] - along) < size[k] * 0.02] or co
        grip = sum(band, Vector()) / len(band)
        grip[k] = along
    side = _axis(spec["side"]) if spec.get("side") else None
    if side is None:
        # Facing defaults to where the head's mass sits off the shaft line (the blade side).
        tip = [c for c in co if (c[k] - along) * head[k] > size[k] * 0.6]
        off = (sum(tip, Vector()) / len(tip) - grip) if tip else Vector((1, 0, 0))
        off -= head * off.dot(head)
        side = off.normalized() if off.length > 1e-6 else Vector([1 if i != k else 0 for i in range(3)]).normalized()
    side = (side - head * side.dot(head)).normalized()
    src = Matrix((head, side, head.cross(side))).transposed()
    dh, ds = _axis(spec["head_to"]), _axis(spec["side_to"])
    ds = (ds - dh * ds.dot(dh)).normalized()
    dst = Matrix((dh, ds, dh.cross(ds))).transposed()
    rot = (dst @ src.transposed()).to_4x4()
    if spec.get("roll"):
        rot = Matrix.Rotation(math.radians(spec["roll"]), 4, dh) @ rot
    offset = Vector(spec.get("offset", [0, 0.03, 0])) * height
    local = Matrix.Translation(offset) @ rot @ Matrix.Scale(scale, 4) @ Matrix.Translation(-grip)
    item.data.transform(bone_frame(rig, spec["bone"]) @ local)
    # Shaft endpoints (butt, head) in bone space, for the off-hand and floor measurements.
    ends = []
    for t in (butt_t, 1 - butt_t):
        p = grip.copy()
        p[k] = lo[k] + size[k] * t
        ends.append(local @ p)
    # A vertex sample in bone space: blades, hammer heads and shield rims reach past the shaft line,
    # so floor checks use the real surface, not the shaft ends.
    step = max(1, len(co) // 400)
    points = [local @ c for c in co[::step]]
    # The head end in the bone's own local space and armature units: the input the adapter's
    # author_locator operation takes for a muzzle or nozzle locator on this item.
    bone = rig.data.bones[spec["bone"]]
    bone_local = (rig.matrix_world @ bone.matrix_local).inverted() @ (bone_frame(rig, spec["bone"]) @ ends[1])
    return {"bone": spec["bone"], "axis_ends_bone_space": ends, "points_bone_space": points, "scale": scale,
            "head_bone_local": list(bone_local)}


def _atlas_uvs(obj, rect):
    u0, v0, u1, v1 = rect
    uv = obj.data.uv_layers.active.data
    for loop in uv:
        u, v = loop.uv
        u, v = min(max(u, 0.0), 1.0), min(max(v, 0.0), 1.0)
        loop.uv = (u0 + (u1 - u0) * u, v0 + (v1 - v0) * v)


def _pixels(path, w, h):
    """Load a PNG through Blender (no PIL in its Python), resample to w x h, return rows bottom-up."""
    import numpy as np
    img = bpy.data.images.load(path)
    img.colorspace_settings.name = "Non-Color"   # copy raw values; never colour-convert maps
    img.scale(w, h)
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    bpy.data.images.remove(img)
    return px.reshape(h, w, 4)


def _write_atlas(cfg, item_specs):
    import numpy as np
    at = cfg["atlas"]
    size, cell = at.get("size", 2048), at.get("cell", 0.25)
    os.makedirs(at["dir"], exist_ok=True)
    body_h = round(size * (1 - cell))
    c = round(size * cell)
    for ch in CHANNELS:
        sheet = np.zeros((size, size, 4), dtype=np.float32)
        sheet[..., 3] = 1.0
        if ch == "normal":
            sheet[..., :3] = (0.5, 0.5, 1.0)
        # Blender pixel rows run bottom-up like UV v: the body fills rows [0, body_h), items the top cell row.
        sheet[:body_h, :, :] = _pixels(os.path.join(cfg["body_textures"], ch + ".png"), size, body_h)
        for k, spec in enumerate(item_specs):
            sheet[size - c:, k * c:(k + 1) * c, :] = _pixels(os.path.join(spec["textures"], ch + ".png"), c, c)
        out = bpy.data.images.new("CXATLAS_" + ch, size, size, alpha=False, float_buffer=False)
        out.colorspace_settings.name = "Non-Color"
        out.pixels.foreach_set(sheet.ravel())
        out.filepath_raw = os.path.join(at["dir"], ch + ".png")
        out.file_format = "PNG"
        out.save()
        bpy.data.images.remove(out)
    return {"size": size, "cell": cell, "dir": at["dir"]}


def _join(body, items, bones):
    for item, bone in zip(items, bones):
        vg = item.vertex_groups.new(name=bone)
        vg.add(list(range(len(item.data.vertices))), 1.0, "REPLACE")
        item.data.materials.clear()
        if not item.data.uv_layers:
            item.data.uv_layers.new()
        item.data.uv_layers.active.name = body.data.uv_layers.active.name
    bpy.ops.object.select_all(action="DESELECT")
    for o in items:
        o.select_set(True)
    body.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.join()
    for p in body.data.polygons:
        p.material_index = 0
    # The join can leave empty slots behind; the partition step requires every slot to be the PDX material.
    keep = next(m for m in body.data.materials if m)
    body.data.materials.clear()
    body.data.materials.append(keep)


def _purge_unused():
    for m in list(bpy.data.materials):
        if m.users == 0:
            bpy.data.materials.remove(m)
    used = set()
    for m in bpy.data.materials:
        if m.use_nodes:
            used.update(n.image for n in m.node_tree.nodes if n.type == "TEX_IMAGE" and n.image)
    for img in list(bpy.data.images):
        if img not in used:
            bpy.data.images.remove(img)


def _floor_items(cfg, rig, placed, height):
    """Measured floor correction for held items, the item analogue of lab_actions.ground_action.
    For each action named in cfg["floor_items"]["actions"], every frame where any sampled item vertex
    sinks below the floor re-keys only the carrying bone, turning it about its own head in the
    vertical plane through its lowest point until that point rests at the clearance height. Frames above the
    floor are untouched, so the provider motion stays as authored. Returns per-action fixed frames."""
    from lab_actions import bind_action
    opts = cfg.get("floor_items") or {}
    clearance = opts.get("clearance", 0.01) * height
    fixed = {}
    for name in opts.get("actions", []):
        act = bpy.data.actions[name]
        bind_action(rig, act)
        f0, f1 = map(int, act.frame_range)
        done = []
        for f in range(f0, f1 + 1):
            bpy.context.scene.frame_set(f)
            for iname, pl in placed.items():
                pb = rig.pose.bones[pl["bone"]]
                turns = 0
                for _ in range(4):   # the lowest point can change as the item turns; converge
                    m = bone_frame(rig, pl["bone"], pose=True)
                    low = min((m @ q for q in pl["points_bone_space"]), key=lambda q: q.z)
                    if low.z >= clearance - 1e-4:
                        break
                    turns += 1
                    pivot = m.translation
                    d = low - pivot
                    r = d.length
                    horiz = Vector((d.x, d.y, 0.0))
                    if r < 1e-6 or horiz.length < 1e-6:
                        horiz = m.to_3x3() @ Vector((1, 0, 0))
                        horiz.z = 0
                    target_sin = max(-1.0, min(1.0, (clearance - pivot.z) / r))
                    new_dir = horiz.normalized() * math.sqrt(1 - target_sin ** 2) + Vector((0, 0, target_sin))
                    rot = d.normalized().rotation_difference(new_dir).to_matrix().to_4x4()
                    world = rig.matrix_world @ pb.matrix
                    turned = Matrix.Translation(pivot) @ rot @ Matrix.Translation(-pivot) @ world
                    pb.matrix = rig.matrix_world.inverted() @ turned
                    bpy.context.view_layer.update()
                    pb.keyframe_insert("rotation_quaternion" if pb.rotation_mode == "QUATERNION" else
                                       ("rotation_axis_angle" if pb.rotation_mode == "AXIS_ANGLE" else "rotation_euler"), frame=f)
                if turns and f not in done:
                    done.append(f)
        fixed[name] = done
    return fixed


def _segment_distance(p, a, b):
    ab = b - a
    t = max(0.0, min(1.0, (p - a).dot(ab) / max(ab.length_squared, 1e-9)))
    return (a + ab * t - p).length


def _measure(cfg, rig, body, placed, height):
    from lab_actions import bind_action
    rev = cfg.get("review", {})
    report = {}
    for name in rev.get("actions", []):
        act = bpy.data.actions[name]
        bind_action(rig, act)
        f0, f1 = map(int, act.frame_range)
        n = rev.get("samples", 6)
        frames = sorted({round(f0 + (f1 - f0) * i / (n - 1)) for i in range(n)})
        rows = []
        for f in range(f0, f1 + 1):
            bpy.context.scene.frame_set(f)
            row = {"frame": f}
            for c in cfg.get("contacts", []):
                pl = placed[c["item"]]
                m = bone_frame(rig, pl["bone"], pose=True)
                a, b = (m @ e for e in pl["axis_ends_bone_space"])
                p = bone_frame(rig, c["bone"], pose=True) @ (Vector(c.get("offset", [0, 0.03, 0])) * height)
                row[c["item"] + "_" + c["bone"]] = round(_segment_distance(p, a, b), 4)
            for iname, pl in placed.items():
                m = bone_frame(rig, pl["bone"], pose=True)
                row[iname + "_low_z"] = round(min((m @ q).z for q in pl["points_bone_space"]), 4)
            rows.append(row)
        keys = [k for k in rows[0] if k != "frame"]
        report[name] = {"frames": [f0, f1], "sampled": frames,
                        "summary": {k: [min(r[k] for r in rows), max(r[k] for r in rows)] for k in keys},
                        "per_frame": rows}
    return report


def _render(cfg, rig, body, height):
    rev = cfg.get("review")
    if not rev or not rev.get("out_dir"):
        return
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from lab_actions import bind_action
    out = rev["out_dir"]
    os.makedirs(out, exist_ok=True)
    diffuse = os.path.join(cfg["atlas"]["dir"], "base_color.png") if cfg.get("atlas") else ""
    img = bpy.data.images.load(diffuse) if diffuse and os.path.exists(diffuse) else None
    preview = bpy.data.materials.new("CXPREVIEW")
    preview.use_nodes = True
    if img:
        tex = preview.node_tree.nodes.new("ShaderNodeTexImage")
        tex.image = img
        bsdf = preview.node_tree.nodes["Principled BSDF"]
        preview.node_tree.links.new(tex.outputs[0], bsdf.inputs["Base Color"])
    saved = [s.material for s in body.material_slots]
    for s in body.material_slots:
        s.material = preview
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_WORKBENCH"
    sc.display.shading.light = "STUDIO"
    sc.display.shading.color_type = "TEXTURE"
    sc.render.resolution_x, sc.render.resolution_y = rev.get("res", [420, 560])
    cam = bpy.data.objects.new("CXCAM", bpy.data.cameras.new("CXCAM"))
    sc.collection.objects.link(cam)
    cam.data.type = "ORTHO"
    sc.camera = cam
    views = {"front": (0, -1, 0), "side": (1, 0, 0), "three_quarter": (0.6, -0.8, 0.15)}
    shots = [("rest", None, None)]
    names = rev.get("actions", [])
    # File names use the role only (the shared "<prefix>_" is dropped): long job paths plus full
    # action names exceed the Windows 260-character path limit and the render save fails.
    common = os.path.commonprefix(names) if len(names) > 1 else ""
    common = common[:common.rfind("_") + 1]
    for name in names:
        act = bpy.data.actions[name]
        f0, f1 = map(int, act.frame_range)
        n = rev.get("samples", 6)
        shots += [(name[len(common):], act, round(f0 + (f1 - f0) * i / (n - 1))) for i in range(n)]
    for tag, act, frame in shots:
        if act:
            bind_action(rig, act)
            sc.frame_set(frame)
        else:
            rig.data.pose_position = "REST"
        dg = bpy.context.evaluated_depsgraph_get()
        ev = body.evaluated_get(dg)
        pts = [ev.matrix_world @ v.co for i, v in enumerate(ev.data.vertices) if i % 5 == 0]
        lo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
        hi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
        ext = (hi - lo).length
        targets = [("full", (lo + hi) / 2, ext * 1.05)]
        if rev.get("closeup"):
            # Close-up on each item's grip point, "closeup" x rig height across.
            for spec in cfg["items"]:
                grip = Vector(spec.get("offset", [0, 0.03, 0])) * height
                centre = bone_frame(rig, spec["bone"], pose=act is not None) @ grip
                targets.append((spec["name"], centre, rev["closeup"] * height))
        for tname, centre, width in targets:
            for vname, d in views.items():
                d = Vector(d).normalized()
                cam.location = centre + d * ext * 4
                cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
                cam.data.ortho_scale = width
                cam.data.clip_start, cam.data.clip_end = ext * 0.01, ext * 20
                sc.render.filepath = os.path.join(out, f"{tag}__{frame or 0:03d}__{tname}__{vname}.png")
                bpy.ops.render.render(write_still=True)
        rig.data.pose_position = "POSE"
    for s, m in zip(body.material_slots, saved):
        s.material = m
    bpy.data.materials.remove(preview)
    bpy.data.objects.remove(cam)
    if img:
        bpy.data.images.remove(img)


def run(config_path=None):
    cfg = json.load(open(config_path, encoding="utf-8")) if config_path else _cfg()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    bpy.ops.wm.open_mainfile(filepath=cfg["blend"])
    rig = bpy.data.objects[cfg.get("armature", "Armature.001")]
    body = bpy.data.objects[cfg.get("body", "char1.001")]
    rig.data.pose_position = "REST"
    height = _rest_height(body)
    specs = cfg["items"]
    items, placed = [], {}
    for spec in specs:
        item = _import_item(spec)
        placed[spec["name"]] = _place(item, rig, spec, height)
        items.append(item)
    rig.data.pose_position = "POSE"
    cell = cfg["atlas"].get("cell", 0.25)
    _atlas_uvs(body, (0.0, 0.0, 1.0, 1.0 - cell))
    for k, item in enumerate(items):
        _atlas_uvs(item, (k * cell, 1.0 - cell, (k + 1) * cell, 1.0))
    atlas = _write_atlas(cfg, specs)
    _join(body, items, [s["bone"] for s in specs])
    _purge_unused()
    report = {"rest_height": height, "atlas": atlas,
              "items": {k: {"bone": v["bone"], "scale": v["scale"],
                            "axis_ends_bone_space": [list(e) for e in v["axis_ends_bone_space"]],
                            "head_bone_local": v["head_bone_local"]} for k, v in placed.items()},
              "floor_fixed_frames": _floor_items(cfg, rig, placed, height),
              "contacts": _measure(cfg, rig, body, placed, height), "triangles": sum(len(p.vertices) - 2 for p in body.data.polygons)}
    _render(cfg, rig, body, height)
    _purge_unused()
    if cfg.get("out") and not cfg.get("review_only"):
        bpy.ops.wm.save_as_mainfile(filepath=cfg["out"])
    dest = os.path.join(cfg.get("review", {}).get("out_dir") or os.path.dirname(cfg.get("out") or cfg["blend"]), "items_report.json")
    json.dump(report, open(dest, "w", encoding="utf-8"), indent=1)
    print("ITEMS", json.dumps({k: v["summary"] for k, v in report["contacts"].items()}))
    return report


if __name__ == "__main__" and "--" in sys.argv:
    run()
