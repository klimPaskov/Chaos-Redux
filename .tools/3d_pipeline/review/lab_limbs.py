"""Add and animate appendages the provider's humanoid rig does not cover (wings, extra arms,
tentacles, tails, growths) on a Meshy-rigged unit.

Meshy rigs two arms and two legs. Anything else either follows the nearest arm or spine bone
(wings wrapping the head, extra arms bending with the elbows) or does not move. This worker
gives each extra appendage its own bone chain placed on measured joints, weights exactly that
appendage's vertices to the new bones with Blender heat weighting on a welded duplicate
(Meshy meshes are triangle soup, so heat weighting fails on the original), maps the weights back
by exact position, and keys the chains per action from angles the agent authors after looking
at the rendered actions. It never invents motion: every key is an explicit number in the config.

Run headless:  review_cli.py blender --script lab_limbs.py --config <cfg.json>
Modes (cfg "mode"):

survey  Open cfg["blend"] in rest pose and report, for each entry of cfg["probes"]
        ({"name", "boxes": [[[x0,y0,z0],[x1,y1,z1]], ...], "exclude": [...]}), the vertex count,
        centroid, bounds, and the highest/lowest/outermost points, in rest world units
        (+Z up, -Y forward). Use it with rest renders to settle selections and joint positions.

rig     For each limb in cfg["limbs"]:
          {"name": "ArmUpperL", "parent": "Spine02",
           "select": {"boxes": [...], "exclude": [...]},
           "joints": [[x,y,z], [x,y,z], ...],      # root -> tip, rest world units, >= 2 points
           "feather": 0.35}                         # optional seam blend distance (rest units)
        builds one bone per joint segment (<name>_1, <name>_2, ...) chained under "parent",
        heat-weights the selected vertices to those bones only, replaces their old weights, and
        saves cfg["out"]. A selection with more than 1% unweighted vertices aborts unsaved.
        Where the selection meets vertices that keep their old weights (an appendage root fused to
        a provider-rigged limb or torso), "feather" blends both sides 50/50 at the seam, fading
        out over that distance, so the appendage does not tear away when either side moves.

skeleton  Build a whole skeleton for a creature the provider cannot rig (quadrupeds, serpents):
        cfg["bones"] = [{"name", "parent" (or null), "head": [x,y,z], "tail": [x,y,z]}, ...] in rest
        world units. Any existing armature and weights on the body are replaced; the whole mesh is
        heat-weighted to the new bones through a welded duplicate (bones listed in
        cfg["non_deform"], e.g. a root, get no weights). Aborts unsaved if more than 1% of vertices
        stay unweighted.

keys    For each action in cfg["keys"] ({action: {frame: {bone: value}}}), removes earlier keys on
        the listed bones and keys them. value is [swing_deg, lift_deg] or
        {"dir": [swing_deg, lift_deg], "loc": [dx, dy, dz]}:
          dir  points the bone's segment along its rest direction turned by swing_deg about world Z
               (positive = toward +X) then lift_deg about world X (positive = tip up/forward), in
               rest-world space, carried through the current pose of cfg["carry_bone"] (default
               "Spine"; the bone the limbs hang from). A bone's segment runs from its head to
               cfg["tips"][bone] (a child bone name or a rest-world point) or, by default, to its
               only child's head, else its tail; this matters for rigs whose bones have stub tails.
          loc  offsets the bone's head from its rest position by (dx, dy, dz) rest-world units
               (body bob, crouches, collapses).
        cfg["create"] = {action: [first, last]} makes new empty actions first (bound to the rig).
        cfg["floor"] = {"actions": [...], "chains": {name: [first bone, ...]}, "clearance": 0.004}
        then runs a measured floor correction: frames where a chain's vertices sink below the floor
        re-key only the chain's first bone, turned about its head until the lowest vertex rests on
        the floor (run it after authoring, on every role; untouched frames stay as authored).
        Every number is authored by the agent; nothing is generated. Saves cfg["out"].

Common keys: "blend", "out", "armature" (default "Armature.001"), "body" (default "char1.001").
"""
import json
import math
import os
import sys

import bmesh
import bpy
import mathutils.kdtree
from mathutils import Matrix, Quaternion, Vector


def _cfg():
    return json.load(open(sys.argv[sys.argv.index("--") + 1], encoding="utf-8"))


def _in_box(p, box):
    lo, hi = box
    return all(min(lo[i], hi[i]) <= p[i] <= max(lo[i], hi[i]) for i in range(3))


def _select(points, sel):
    keep = [i for i, p in enumerate(points) if any(_in_box(p, b) for b in sel["boxes"])]
    return [i for i in keep if not any(_in_box(points[i], b) for b in sel.get("exclude", []))]


def _open(cfg):
    bpy.ops.wm.open_mainfile(filepath=cfg["blend"])
    rig = bpy.data.objects[cfg.get("armature", "Armature.001")]
    body = bpy.data.objects[cfg.get("body", "char1.001")]
    rig.data.pose_position = "REST"
    bpy.context.view_layer.update()
    return rig, body


def _weight_totals(body, idx):
    names = {g.index: g.name for g in body.vertex_groups}
    tot = {}
    for i in idx:
        for g in body.data.vertices[i].groups:
            tot[names[g.group]] = round(tot.get(names[g.group], 0.0) + g.weight, 1)
    return tot


def _components(body, idx, pts, opts):
    """Union-find over polygon edges plus coincident positions, restricted to idx. Returns the
    pieces with at least opts["min"] vertices (default 50), largest first, each with its count,
    centroid, bounds, root (nearest to opts["root"], default the body centre line at the piece's
    top), tip (farthest from that root), and a centreline sampled in opts.get("samples", 5) steps
    of distance from the root."""
    sel = set(idx)
    parent = {i: i for i in idx}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for poly in body.data.polygons:
        vs = [v for v in poly.vertices if v in sel]
        for a, b in zip(vs, vs[1:]):
            union(a, b)
    kd = mathutils.kdtree.KDTree(len(idx))
    for i in idx:
        kd.insert(pts[i], i)
    kd.balance()
    for i in idx:
        for _, j, _ in kd.find_range(pts[i], opts.get("weld", 0.002)):
            union(i, j)
    groups = {}
    for i in idx:
        groups.setdefault(find(i), []).append(i)
    out = []
    for members in sorted(groups.values(), key=len, reverse=True):
        if len(members) < opts.get("min", 50):
            continue
        ps = [pts[i] for i in members]
        c = sum(ps, Vector()) / len(ps)
        root_hint = Vector(opts["root"]) if opts.get("root") else Vector((0, c.y, max(p.z for p in ps)))
        root = min(ps, key=lambda p: (p - root_hint).length)
        tip = max(ps, key=lambda p: (p - root).length)
        span = (tip - root).length
        n = opts.get("samples", 5)
        line = []
        for k in range(n + 1):
            band = [p for p in ps if abs((p - root).length - span * k / n) < span / (2 * n)]
            if band:
                line.append([round(v, 3) for v in sum(band, Vector()) / len(band)])
        out.append({"count": len(members), "centroid": [round(v, 3) for v in c],
                    "root": [round(v, 3) for v in root], "tip": [round(v, 3) for v in tip], "centreline": line})
    return out


def survey(cfg):
    rig, body = _open(cfg)
    mw = body.matrix_world
    pts = [mw @ v.co for v in body.data.vertices]
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    report = {"body_bounds": [list(lo), list(hi)], "bones": {}, "probes": {}}
    for b in rig.data.bones:
        report["bones"][b.name] = [round(c, 3) for c in (rig.matrix_world @ b.head_local)]
    for probe in cfg.get("probes", []):
        idx = _select(pts, probe)
        sel = [pts[i] for i in idx]
        if not sel:
            report["probes"][probe["name"]] = {"count": 0}
            continue
        c = sum(sel, Vector()) / len(sel)
        report["probes"][probe["name"]] = {
            "count": len(sel), "centroid": [round(v, 3) for v in c],
            "bounds": [[round(min(p[i] for p in sel), 3) for i in range(3)], [round(max(p[i] for p in sel), 3) for i in range(3)]],
            "highest": [round(v, 3) for v in max(sel, key=lambda p: p.z)],
            "lowest": [round(v, 3) for v in min(sel, key=lambda p: p.z)],
            "outermost_x": [round(v, 3) for v in max(sel, key=lambda p: abs(p.x))],
            # Which bones this region follows now: summed weights of the top groups.
            "weights": dict(sorted(_weight_totals(body, idx).items(), key=lambda kv: -kv[1])[:5])}
        if probe.get("components"):
            # Connected pieces of the selection (position-welded, since provider meshes are
            # triangle soup). Cutting the torso core away with "exclude" leaves each appendage as
            # its own piece: its root (the end nearest cfg "components.root") and tip give joints.
            report["probes"][probe["name"]]["components"] = _components(body, idx, pts, probe["components"])
        if probe.get("hist"):
            # Vertex counts per bin along one axis: separates limbs that fan in one plane.
            axis, edges = probe["hist"]["axis"], probe["hist"]["edges"]
            report["probes"][probe["name"]]["hist"] = [
                sum(1 for p in sel if edges[k] <= p[axis] < edges[k + 1]) for k in range(len(edges) - 1)]
    print("SURVEY", json.dumps(report))
    return report


def _heat_weights(rig, body, idx, bones, pts):
    """Heat-weight the vertices idx of body to bones through a welded duplicate and return
    ({vertex: [(bone, weight)]}, unweighted count). Meshy and PDX meshes are triangle soup, which
    Blender's heat weighting rejects, so the weld happens on a throwaway copy."""
    mw = body.matrix_world
    dup = body.copy()
    dup.data = body.data.copy()
    dup.name = "CX_limb_tmp"
    bpy.context.scene.collection.objects.link(dup)
    for m in list(dup.modifiers):
        dup.modifiers.remove(m)
    dup.parent = None
    dup.matrix_world = mw.copy()
    dup.vertex_groups.clear()
    bm = bmesh.new()
    bm.from_mesh(dup.data)
    bm.verts.ensure_lookup_table()
    keep = set(idx)
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if v.index not in keep], context="VERTS")
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=0.0005)
    bm.to_mesh(dup.data)
    bm.free()
    saved = {b.name: b.use_deform for b in rig.data.bones}
    for b in rig.data.bones:
        b.use_deform = b.name in bones
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    dup.select_set(True)
    rig.select_set(True)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")
    for b in rig.data.bones:
        b.use_deform = saved.get(b.name, True)
    dnames = {g.index: g.name for g in dup.vertex_groups}
    kd = mathutils.kdtree.KDTree(len(dup.data.vertices))
    for dv in dup.data.vertices:
        kd.insert(dup.matrix_world @ dv.co, dv.index)
    kd.balance()
    weights, unweighted = {}, 0
    for i in idx:
        _, di, _ = kd.find(pts[i])
        ws = [(dnames[g.group], g.weight) for g in dup.data.vertices[di].groups if dnames[g.group] in bones and g.weight > 0.001]
        if ws:
            weights[i] = ws
        else:
            unweighted += 1
    bpy.data.objects.remove(dup, do_unlink=True)
    return weights, unweighted


def build_skeleton(cfg):
    bpy.ops.wm.open_mainfile(filepath=cfg["blend"])
    body = bpy.data.objects[cfg.get("body", "char1.001")]
    name = cfg.get("armature", "Armature.001")
    old = bpy.data.objects.get(name)
    mw = body.matrix_world.copy()
    body.parent = None
    body.matrix_world = mw
    for m in list(body.modifiers):
        if m.type == "ARMATURE":
            body.modifiers.remove(m)
    body.vertex_groups.clear()
    if old:
        bpy.data.objects.remove(old, do_unlink=True)
    rig = bpy.data.objects.new(name, bpy.data.armatures.new(name))
    bpy.context.scene.collection.objects.link(rig)
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    eb = rig.data.edit_bones
    for spec in cfg["bones"]:
        b = eb.new(spec["name"])
        b.head, b.tail = Vector(spec["head"]), Vector(spec["tail"])
    for spec in cfg["bones"]:
        if spec.get("parent"):
            eb[spec["name"]].parent = eb[spec["parent"]]
    bpy.ops.object.mode_set(mode="OBJECT")
    for n in cfg.get("non_deform", []):
        rig.data.bones[n].use_deform = False
    pts = [mw @ v.co for v in body.data.vertices]
    bones = [b.name for b in rig.data.bones if b.use_deform]
    weights, unweighted = _heat_weights(rig, body, list(range(len(pts))), bones, pts)
    if unweighted > max(1, len(pts) * 0.01):
        raise RuntimeError(f"heat weights missing on {unweighted} of {len(pts)} vertices; nothing saved")
    groups = {n: body.vertex_groups.new(name=n) for n in bones}
    for i, ws in weights.items():
        tot = sum(w for _, w in ws)
        for n, w in ws:
            groups[n].add([i], w / tot, "REPLACE")
    body.parent = rig
    mod = body.modifiers.new("Armature", "ARMATURE")
    mod.object = rig
    bpy.ops.wm.save_as_mainfile(filepath=cfg["out"])
    report = {"bones": len(rig.data.bones), "vertices": len(pts), "weighted": len(weights), "unweighted": unweighted}
    print("SKELETON", json.dumps(report))
    return report


def rig_limbs(cfg):
    rig, body = _open(cfg)
    mw = body.matrix_world
    pts = [mw @ v.co for v in body.data.vertices]
    rinv = rig.matrix_world.inverted()
    for o in bpy.context.view_layer.objects:
        o.select_set(False)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    eb = rig.data.edit_bones
    chains = {}
    for limb in cfg["limbs"]:
        joints = [Vector(j) for j in limb["joints"]]
        prev = eb[limb["parent"]]
        names = []
        for k in range(len(joints) - 1):
            b = eb.new(f"{limb['name']}_{k + 1}")
            b.head, b.tail = rinv @ joints[k], rinv @ joints[k + 1]
            b.parent = prev
            b.use_connect = k > 0
            prev = b
            names.append(b.name)
        chains[limb["name"]] = names
    bpy.ops.object.mode_set(mode="OBJECT")
    report = {}
    for limb in cfg["limbs"]:
        idx = _select(pts, limb["select"])
        bones = chains[limb["name"]]
        weights, unweighted = _heat_weights(rig, body, idx, bones, pts)
        if unweighted > max(1, len(idx) * 0.01):
            raise RuntimeError(f"{limb['name']}: heat weights missing on {unweighted} of {len(idx)} vertices; nothing saved")
        groups = {n: (body.vertex_groups.get(n) or body.vertex_groups.new(name=n)) for n in bones}
        names = {g.index: g.name for g in body.vertex_groups}
        old = {i: [(names[g.group], g.weight) for g in body.data.vertices[i].groups] for i in range(len(pts))}
        new = {i: [(n, w / sum(x for _, x in ws)) for n, w in ws] for i, ws in weights.items()}
        feather = limb.get("feather", 0.0)
        if feather > 0:
            # Blend across the selection edge so the appendage does not tear from the body where
            # the old weights end: 50/50 at the seam, fading to pure new (inside) or pure old
            # (outside) over the feather distance.
            inside = set(new)
            outside = [i for i in range(len(pts)) if i not in inside]
            kd_in = mathutils.kdtree.KDTree(len(inside))
            for i in inside:
                kd_in.insert(pts[i], i)
            kd_in.balance()
            kd_out = mathutils.kdtree.KDTree(len(outside))
            for i in outside:
                kd_out.insert(pts[i], i)
            kd_out.balance()
            blended = {}
            for i in inside:
                _, j, d = kd_out.find(pts[i])
                if j is not None and d < feather and old[i]:
                    a = 0.5 * (1 - d / feather)
                    blended[i] = [(n, w * (1 - a)) for n, w in new[i]] + [(n, w * a) for n, w in old[i]]
            for i in outside:
                _, j, d = kd_in.find(pts[i])
                if j is not None and d < feather:
                    a = 0.5 * (1 - d / feather)
                    blended[i] = [(n, w * (1 - a)) for n, w in old[i]] + [(n, w * a) for n, w in new[j]]
            new.update(blended)
        others = list(body.vertex_groups)
        for i, ws in new.items():
            for g in others:
                g.remove([i])
            merged = {}
            for n, w in ws:
                merged[n] = merged.get(n, 0.0) + w
            tot = sum(merged.values())
            for n, w in merged.items():
                if w / tot > 0.001:
                    (body.vertex_groups.get(n) or body.vertex_groups.new(name=n)).add([i], w / tot, "REPLACE")
        report[limb["name"]] = {"bones": bones, "vertices": len(idx), "weighted": len(weights), "unweighted": unweighted,
                                "feathered": len(new) - len(weights) if feather > 0 else 0}
    rig.data.pose_position = "POSE"
    bpy.ops.wm.save_as_mainfile(filepath=cfg["out"])
    print("LIMBS", json.dumps(report))
    return report


def _floor_chains(cfg, rig, bind_action):
    """Measured floor correction for authored limb chains (the chain analogue of lab_items'
    floor_items). cfg["floor"] = {"actions": [...], "chains": {"TentFrontL": ["TentFrontL_1", ...]},
    "clearance": 0.004}. On every frame where a vertex weighted mainly to a chain sinks below
    the clearance (rest-world units), the chain's first bone is re-keyed, turned about its head in
    the vertical plane through that vertex until it rests on the floor. Frames above the floor are
    untouched. Returns {action: {chain: fixed frame count}}."""
    body = bpy.data.objects[cfg.get("body", "char1.001")]
    opts = cfg["floor"]
    clearance = opts.get("clearance", 0.004)
    names = {g.index: g.name for g in body.vertex_groups}
    owner = {}
    for v in body.data.vertices:
        if v.groups:
            g = max(v.groups, key=lambda g: g.weight)
            owner[v.index] = names[g.group]
    members = {c: [i for i, b in owner.items() if b in set(bones)] for c, bones in opts["chains"].items()}
    mw = rig.matrix_world
    r_world = mw.to_3x3().normalized()
    out = {}
    for name in opts["actions"]:
        act = bpy.data.actions[name]
        bind_action(rig, act)
        f0, f1 = map(int, act.frame_range)
        fixed = {c: 0 for c in opts["chains"]}
        for f in range(f0, f1 + 1):
            bpy.context.scene.frame_set(f)
            for chain, bones in opts["chains"].items():
                pb = rig.pose.bones[bones[0]]
                turned = False
                for _ in range(4):
                    dg = bpy.context.evaluated_depsgraph_get()
                    ev = body.evaluated_get(dg)
                    bw = ev.matrix_world
                    low = min((bw @ ev.data.vertices[i].co for i in members[chain]), key=lambda p: p.z)
                    if low.z >= clearance - 1e-4:
                        break
                    pivot = mw @ pb.head
                    d = low - pivot
                    horiz = Vector((d.x, d.y, 0.0))
                    if d.length < 1e-6 or horiz.length < 1e-6:
                        break
                    s = max(-1.0, min(1.0, (clearance - pivot.z) / d.length))
                    goal = horiz.normalized() * math.sqrt(1 - s * s) + Vector((0, 0, s))
                    rot = r_world.inverted() @ d.normalized().rotation_difference(goal).to_matrix() @ r_world
                    h = pb.head.copy()
                    pb.rotation_mode = "QUATERNION"
                    pb.matrix = Matrix.Translation(h) @ rot.to_4x4() @ Matrix.Translation(-h) @ pb.matrix
                    bpy.context.view_layer.update()
                    pb.keyframe_insert("rotation_quaternion", frame=f)
                    turned = True
                fixed[chain] += int(turned)
        out[name] = fixed
    return out


def key_limbs(cfg):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from lab_actions import bind_action, fcurves
    bpy.ops.wm.open_mainfile(filepath=cfg["blend"])
    rig = bpy.data.objects[cfg.get("armature", "Armature.001")]
    mw = rig.matrix_world
    r_world = mw.to_3x3().normalized()
    carry_name = cfg.get("carry_bone", "Spine")
    carry_rest = (mw @ rig.data.bones[carry_name].matrix_local).to_3x3().normalized()
    tips = cfg.get("tips", {})

    for action, (f0, f1) in cfg.get("create", {}).items():
        act = bpy.data.actions.get(action) or bpy.data.actions.new(action)
        act.use_fake_user = True
        rig.animation_data_create()
        rig.animation_data.action = act
        root = rig.pose.bones[rig.data.bones[0].name]
        root.rotation_mode = "QUATERNION"
        for f in (f0, f1):
            root.keyframe_insert("location", frame=f)
            root.keyframe_insert("rotation_quaternion", frame=f)
        if act.slots:
            act.slots[0].name_display = rig.name

    def head(bone, pose):
        return mw @ (rig.pose.bones[bone].head if pose else rig.data.bones[bone].head_local)

    def tip(bone, pose):
        t = tips.get(bone)
        if isinstance(t, list):
            if not pose:
                return Vector(t)
            # A fixed rest-world tip travels rigidly with its bone.
            local = (mw @ rig.data.bones[bone].matrix_local).inverted() @ Vector(t)
            return mw @ rig.pose.bones[bone].matrix @ local
        b = rig.pose.bones[bone] if pose else rig.data.bones[bone]
        child = t or (b.children[0].name if len(b.children) == 1 else None)
        if child:
            return head(child, pose)
        return mw @ (b.tail if pose else b.tail_local)

    def seg(bone, pose):
        return (tip(bone, pose) - head(bone, pose)).normalized()

    report = {}
    for action, frames in cfg["keys"].items():
        act = bpy.data.actions[action]
        bones = sorted({b for f in frames.values() for b in f})
        fcs = fcurves(act)
        for fc in list(fcs):
            if any(f'"{b}"' in fc.data_path for b in bones):
                fcs.remove(fc)
        bind_action(rig, act)
        for frame in sorted(frames, key=int):
            f = int(frame)
            bpy.context.scene.frame_set(f)
            # Parents first, so a child's current direction already includes its parent's new key.
            for bone in sorted(frames[frame], key=lambda n: len(rig.pose.bones[n].parent_recursive)):
                value = frames[frame][bone]
                spec = value if isinstance(value, dict) else {"dir": value}
                pb = rig.pose.bones[bone]
                pb.rotation_mode = "QUATERNION"
                if "loc" in spec:
                    target = head(bone, False) + Vector(spec["loc"])
                    delta = mw.inverted().to_3x3() @ (target - head(bone, True))
                    pb.matrix = Matrix.Translation(delta) @ pb.matrix
                    bpy.context.view_layer.update()
                    pb.keyframe_insert("location", frame=f)
                if "dir" in spec:
                    swing, lift = spec["dir"]
                    goal = Quaternion(Vector((0, 0, 1)), math.radians(swing)) @ seg(bone, False)
                    goal = Quaternion(Vector((1, 0, 0)), math.radians(lift)) @ goal
                    if bone != carry_name:
                        carry = (mw @ rig.pose.bones[carry_name].matrix).to_3x3().normalized() @ carry_rest.inverted()
                        goal = carry @ goal
                    rot = r_world.inverted() @ seg(bone, True).rotation_difference(goal.normalized()).to_matrix() @ r_world
                    h = pb.head.copy()
                    pb.matrix = Matrix.Translation(h) @ rot.to_4x4() @ Matrix.Translation(-h) @ pb.matrix
                    bpy.context.view_layer.update()
                    pb.keyframe_insert("rotation_quaternion", frame=f)
        report[action] = {"bones": bones, "frames": sorted(int(f) for f in frames)}
    if cfg.get("floor"):
        report["floor_fixed_frames"] = _floor_chains(cfg, rig, bind_action)
    for o in bpy.data.objects:
        if o.animation_data:
            for t in list(o.animation_data.nla_tracks):
                o.animation_data.nla_tracks.remove(t)
    bpy.ops.wm.save_as_mainfile(filepath=cfg["out"])
    print("KEYS", json.dumps(report))
    return report


def run(config_path=None):
    cfg = json.load(open(config_path, encoding="utf-8")) if config_path else _cfg()
    return {"survey": survey, "rig": rig_limbs, "skeleton": build_skeleton, "keys": key_limbs}[cfg["mode"]](cfg)


if __name__ == "__main__" and "--" in sys.argv:
    run()
