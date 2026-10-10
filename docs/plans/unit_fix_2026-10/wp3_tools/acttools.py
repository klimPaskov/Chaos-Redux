import bpy, numpy as np, math
from mathutils import Quaternion, Vector, Euler
import sys; sys.path.insert(0, r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.tools/3d_pipeline/adapter")
import zv as z

LIM = {'idle': 0.092, 'move': 0.33, 'retreat': 0.33}   # 8% inside the gate limits (0.10 / 0.36 / 0.41 u per frame)
ANG = {'idle': 9.0, 'move': 23.0, 'retreat': 23.0}

def cbag(act):
    return act.layers[0].strips[0].channelbag(act.slots[0])

def sign_flips(act):
    n = 0
    cb = cbag(act)
    groups = {}
    for fc in cb.fcurves:
        if fc.data_path.endswith('rotation_quaternion'):
            groups.setdefault(fc.data_path, {})[fc.array_index] = fc
    for dp, g in groups.items():
        if len(g) < 4: continue
        keys = [[kp.co[0] for kp in g[i].keyframe_points] for i in range(4)]
        vals = np.array([[kp.co[1] for kp in g[i].keyframe_points] for i in range(4)]).T
        for k in range(len(vals) - 1):
            if np.dot(vals[k], vals[k+1]) < 0: n += 1
    return n

def normalize_signs(act):
    """Negate whole quaternion keys (values + handles) when the dot with the previous key is negative; no key added or removed."""
    cb = cbag(act); groups = {}
    for fc in cb.fcurves:
        if fc.data_path.endswith('rotation_quaternion'):
            groups.setdefault(fc.data_path, {})[fc.array_index] = fc
    changed = 0
    for dp, g in groups.items():
        if len(g) < 4: continue
        npts = len(g[0].keyframe_points)
        prev = None
        for k in range(npts):
            q = np.array([g[i].keyframe_points[k].co[1] for i in range(4)])
            if prev is not None and np.dot(prev, q) < 0:
                for i in range(4):
                    kp = g[i].keyframe_points[k]
                    kp.co[1] = -kp.co[1]; kp.handle_left[1] = -kp.handle_left[1]; kp.handle_right[1] = -kp.handle_right[1]
                q = -q; changed += 1
            prev = q
    for fc in cb.fcurves: fc.update()
    return changed

def audit(arm, body, act, role, step=1):
    fr, names, J = z.joint_track(arm, act, step=step)
    d = np.linalg.norm(np.diff(J, axis=0), axis=2)
    lim = LIM.get(role, 0.375)
    Q = z.LAST_Q; dots = np.abs((Q[1:] * Q[:-1]).sum(2)).clip(0, 1); ang = np.degrees(2 * np.arccos(dots))
    alim = ANG.get(role, 27.5); ang_over = int((ang > alim).sum())
    over = np.argwhere(d > lim)
    worst = sorted([(float(d[i, j]), fr[i+1], names[j]) for i, j in over], reverse=True)[:4]
    return dict(role=role, frames=len(fr), sec=round(len(fr)/30, 2), flips=sign_flips(act), over=len(over), ang_over=ang_over, ang_max=round(float(ang.max()),1), worst=[(round(a,2), b, c) for a,b,c in worst],
                seam=round(float(np.linalg.norm(J[-1]-J[0], axis=1).max()), 3), hips_z=(round(float(J[:, 0, 2].min()), 2), round(float(J[:, 0, 2].max()), 2)))

ROLES = ['idle','move','attack','defend','support_attack','retreat','training','death']
def audit_all(arm, body, prefix):
    out = {}
    for r in ROLES:
        nm = [a.name for a in bpy.data.actions if a.name in (f'{prefix}_{r}', f'{prefix}_{r}_shamble')]
        if nm: out[r] = audit(arm, body, bpy.data.actions[nm[0]], r)
    return out


# ---------- deliberate pose-ease edits on existing per-frame keys ----------
def _curves(act, bone):
    cb = cbag(act); d = {}
    for fc in cb.fcurves:
        if fc.data_path == f'pose.bones["{bone}"].location': d.setdefault('loc', {})[fc.array_index] = fc
        elif fc.data_path == f'pose.bones["{bone}"].rotation_quaternion': d.setdefault('rot', {})[fc.array_index] = fc
    return d

def _kp(fc, frame):
    for kp in fc.keyframe_points:
        if abs(kp.co[0] - frame) < 1e-4: return kp
    return None

def _pose(act, bone, frame):
    c = _curves(act, bone)
    loc = np.array([c['loc'][i].evaluate(frame) for i in range(3)]) if 'loc' in c else None
    rot = np.array([c['rot'][i].evaluate(frame) for i in range(4)]) if 'rot' in c else None
    return loc, rot

def _slerp(q0, q1, t):
    q0 = q0 / np.linalg.norm(q0); q1 = q1 / np.linalg.norm(q1)
    d = np.dot(q0, q1)
    if d < 0: q1 = -q1; d = -d
    if d > 0.9995:
        r = q0 + t * (q1 - q0); return r / np.linalg.norm(r)
    th = math.acos(d); s = math.sin(th)
    return (math.sin((1 - t) * th) * q0 + math.sin(t * th) * q1) / s

def _write(act, bone, frame, loc=None, rot=None):
    c = _curves(act, bone)
    if loc is not None and 'loc' in c:
        for i in range(3):
            kp = _kp(c['loc'][i], frame)
            if kp: kp.co[1] = float(loc[i]); kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'
    if rot is not None and 'rot' in c:
        for i in range(4):
            kp = _kp(c['rot'][i], frame)
            if kp: kp.co[1] = float(rot[i]); kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'

def ease_range(act, bones, fa, fb, ease='smooth'):
    """Replace the per-frame poses strictly between fa and fb by an eased blend of the poses at fa and fb (plan: 're-ease over N frames')."""
    for b in bones:
        l0, r0 = _pose(act, b, fa); l1, r1 = _pose(act, b, fb)
        for f in range(fa + 1, fb):
            t = (f - fa) / (fb - fa)
            s = t * t * (3 - 2 * t) if ease == 'smooth' else t
            loc = (l0 * (1 - s) + l1 * s) if l0 is not None else None
            rot = _slerp(r0, r1, s) if r0 is not None else None
            _write(act, b, f, loc, rot)
    for fc in cbag(act).fcurves: fc.update()

def ease_seam(act, n, bones=None):
    """Blend the last n frames toward the first-frame pose (smoothstep) so a self-chaining state closes its loop."""
    f0 = int(act.frame_range[0]); f1 = int(act.frame_range[1])
    names = sorted({fc.data_path.split('"')[1] for fc in cbag(act).fcurves if 'pose.bones' in fc.data_path})
    for b in (bones or names):
        l0, r0 = _pose(act, b, f0)
        for f in range(f1 - n + 1, f1 + 1):
            t = (f - (f1 - n)) / n; s = t * t * (3 - 2 * t)
            l, r = _pose(act, b, f)
            _write(act, b, f, (l * (1 - s) + l0 * s) if l is not None else None, _slerp(r, r0, s) if r is not None else None)
    for fc in cbag(act).fcurves: fc.update()

def chain(arm, bone, up=0):
    b = arm.data.bones[bone]; names = [bone]
    for _ in range(up):
        b = b.parent
        if not b: break
        names.append(b.name)
    return names

def deglitch(arm, body, act, role, rounds=6, halfwin=3, up=0, verbose=False):
    """Iteratively ease the poses around each over-limit joint step (bone + 'up' ancestors) between the frames either side."""
    f0 = int(act.frame_range[0]); f1 = int(act.frame_range[1])
    lim = LIM.get(role, 0.375); hist = []
    for r in range(rounds):
        fr, names, J = z.joint_track(arm, act)
        d = np.linalg.norm(np.diff(J, axis=0), axis=2)
        over = np.argwhere(d > lim)
        hist.append(len(over))
        if not len(over): break
        seen = set()
        for i, j in sorted(over.tolist(), key=lambda p: -d[p[0], p[1]]):
            frame = fr[i + 1]; key = (names[j], frame // (2 * halfwin))
            if key in seen: continue
            seen.add(key)
            fa = max(f0, frame - halfwin - 1); fb = min(f1, frame + halfwin)
            if fb - fa < 3: continue
            ease_range(act, chain(arm, names[j], up), fa, fb)
    return hist


def generic_pass(arm, body, prefix, roles=None, seam_n=8, up=1, loop_roles=('idle','move','attack','defend','support_attack','retreat','training'), do_seam=True):
    res = {}
    for r in (roles or ROLES):
        nm = [a.name for a in bpy.data.actions if a.name in (f'{prefix}_{r}', f'{prefix}_{r}_shamble')]
        if not nm: continue
        act = bpy.data.actions[nm[0]]
        s = normalize_signs(act)
        h = deglitch2(arm, body, act, r)
        if do_seam and r in loop_roles:
            for attempt in range(5):
                a = audit(arm, body, act, r)
                if a['seam'] < 0.03 and a['over'] == 0 and a['ang_over'] == 0: break
                ease_seam(act, 10 + 8 * attempt + (12 if r == 'idle' else 0))
                h += deglitch2(arm, body, act, r, rounds=8)
        res[r] = dict(sign_fixed=s, hist=h, **audit(arm, body, act, r))
    return res


def _all_bones(act):
    return sorted({fc.data_path.split('"')[1] for fc in cbag(act).fcurves if 'pose.bones' in fc.data_path})

def smooth_window(act, f0, f1, sigma=1.5, bones=None, taper=3):
    """Gaussian-smooth the existing per-frame keys of the given bones over [f0,f1], tapering the weight to zero at both ends."""
    fa = int(act.frame_range[0]); fb = int(act.frame_range[1])
    lo = max(fa, f0 - taper); hi = min(fb, f1 + taper)
    rad = int(math.ceil(3 * sigma))
    for b in (bones or _all_bones(act)):
        c = _curves(act, b)
        data = {}
        for kind, n in (('loc', 3), ('rot', 4)):
            if kind in c:
                data[kind] = np.array([[fc.evaluate(f) for fc in (c[kind][i] for i in range(n))] for f in range(fa - rad, fb + rad + 1)])
                # clamp-extend at ends
        for kind, arr in data.items():
            full = arr
            for f in range(lo, hi + 1):
                w = 1.0
                if f < f0: w = (f - lo + 1) / (taper + 1)
                elif f > f1: w = (hi - f + 1) / (taper + 1)
                idx = f - (fa - rad)
                acc = np.zeros(full.shape[1]); ws = 0
                for k in range(-rad, rad + 1):
                    j = idx + k
                    if 0 <= j < len(full):
                        g = math.exp(-0.5 * (k / sigma) ** 2); acc += g * full[j]; ws += g
                sm = acc / ws
                if kind == 'rot': sm = sm / np.linalg.norm(sm)
                cur = full[idx]
                val = cur * (1 - w) + sm * w
                if kind == 'rot': val = val / np.linalg.norm(val)
                _write(act, b, f, loc=val if kind == 'loc' else None, rot=val if kind == 'rot' else None)
    for fc in cbag(act).fcurves: fc.update()

def deglitch2(arm, body, act, role, rounds=16, sigma=None, halfwin=None):
    sigma = sigma or (2.5 if role == 'idle' else 1.2); halfwin = halfwin or (6 if role == 'idle' else 3)
    f0 = int(act.frame_range[0]); f1 = int(act.frame_range[1]); lim = LIM.get(role, 0.375); hist = []
    for r in range(rounds):
        fr, names, J = z.joint_track(arm, act)
        d = np.linalg.norm(np.diff(J, axis=0), axis=2)
        Q = z.LAST_Q; dots = np.abs((Q[1:] * Q[:-1]).sum(2)).clip(0, 1); ang = np.degrees(2 * np.arccos(dots))
        over = np.argwhere(d > lim); aover = np.argwhere(ang > ANG.get(role, 27.5)); hist.append(len(over) + len(aover))
        if not len(over) and not len(aover): break
        frames = sorted({fr[i + 1] for i, j in over} | {fr[i + 1] for i, j in aover})
        # merge nearby frames into windows
        wins = []
        for f in frames:
            if wins and f - wins[-1][1] <= halfwin: wins[-1][1] = f
            else: wins.append([f, f])
        for a, b in wins:
            smooth_window(act, max(f0, a - halfwin), min(f1, b + halfwin), sigma=sigma + 0.4 * r)
    return hist


def add_offsets(act, bone, axis, keys):
    """Additive authored layer: keys = [(frame, degrees)...] on one bone-local axis; consecutive keys blend with smoothstep. Existing keys stay; the offset is post-multiplied."""
    ax = {'x': (1,0,0), 'y': (0,1,0), 'z': (0,0,1)}[axis]
    ks = sorted(keys); f0 = int(act.frame_range[0]); f1 = int(act.frame_range[1])
    for f in range(f0, f1 + 1):
        ang = 0.0
        for (fa, da), (fb, db) in zip(ks, ks[1:]):
            if fa <= f <= fb:
                t = (f - fa) / max(fb - fa, 1); s = t * t * (3 - 2 * t); ang = da + (db - da) * s; break
        if f < ks[0][0]: ang = ks[0][1]
        if f > ks[-1][0]: ang = ks[-1][1]
        if abs(ang) < 1e-6: continue
        l, r = _pose(act, bone, f)
        q = Quaternion(r.tolist()); off = Quaternion(ax, math.radians(ang))
        n = q @ off
        if np.dot(np.array(n), r) < 0: n = Quaternion([-v for v in n])
        _write(act, bone, f, None, np.array(n))
    for fc in cbag(act).fcurves: fc.update()


def sole_plants(arm, body, act, contact=0.05, stationary=0.03, min_frames=2, band=0.025):
    """Approximate the gate's sole measurement: lowest foot/toe-weighted vertices per side, ground distance and tangent step per frame."""
    f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    regions = {}
    for side in ('left', 'right'):
        gs = {g.index for g in body.vertex_groups if side in g.name.casefold() and ('foot' in g.name.casefold() or 'toe' in g.name.casefold())}
        regions[side] = [v.index for v in body.data.vertices if sum(g.weight for g in v.groups if g.group in gs) > 0.5]
    z.set_action(arm, act)
    dg = bpy.context.evaluated_depsgraph_get()
    tr = {s: [] for s in regions}
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f); dg.update()
        eo = body.evaluated_get(dg); me = eo.to_mesh()
        co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
        M = np.array(body.matrix_world); co = co @ M[:3, :3].T + M[:3, 3]
        eo.to_mesh_clear()
        for s, idx in regions.items():
            pts = co[idx]; zmin = pts[:, 2].min(); low = pts[pts[:, 2] <= zmin + band]
            tr[s].append((zmin, low[:, :2].mean(0)))
    out = {}
    for s, rows in tr.items():
        flags = []
        for i, (zm, xy) in enumerate(rows):
            step = np.linalg.norm(xy - rows[i - 1][1]) if i else 9
            nxt = np.linalg.norm(rows[i + 1][1] - xy) if i + 1 < len(rows) else 9
            flags.append(zm < contact and min(step, nxt) < stationary)
        runs = []; i = 0
        while i < len(flags):
            if flags[i]:
                j = i
                while j + 1 < len(flags) and flags[j + 1]: j += 1
                if j - i + 1 >= min_frames: runs.append((f0 + i, f0 + j))
                i = j + 1
            else: i += 1
        out[s] = runs
    return out


def hold_extend(act, total, src_frame=None):
    """Re-key every channel to the pose it has at src_frame (default: first frame) for frames 1..total. The authored layers then supply all motion."""
    f0 = int(act.frame_range[0]) if src_frame is None else src_frame
    for fc in cbag(act).fcurves:
        v = fc.evaluate(f0)
        while len(fc.keyframe_points): fc.keyframe_points.remove(fc.keyframe_points[0])
        fc.keyframe_points.add(total)
        for i in range(total):
            kp = fc.keyframe_points[i]; kp.co = (1 + i, v); kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'; kp.interpolation = 'BEZIER'
        fc.update()
    act.frame_start = 1; act.frame_end = total


def thigh_angle(arm, bone):
    """Signed forward angle (deg) of the thigh from straight down in world space (forward = -Y)."""
    pb = arm.pose.bones[bone]
    d = (arm.matrix_world @ pb.tail) - (arm.matrix_world @ pb.head); d = np.array(d) / np.linalg.norm(d)
    return math.degrees(math.atan2(-d[1], -d[2]))

def clamp_thigh(arm, act, bone, floor_deg, f_a, f_b, sign=-1.0, iters=4, pad=4, gain=2.5):
    """Measured corrective offsets on the bone's local x so the thigh never trails behind floor_deg inside [f_a,f_b]. Returns residual min."""
    z.set_action(arm, act)
    for it in range(iters):
        keys = []
        for f in range(f_a, f_b + 1):
            bpy.context.scene.frame_set(f); a = thigh_angle(arm, bone)
            keys.append((f, sign * gain * max(0.0, floor_deg - a)))
        ks = [(max(f_a - pad, int(act.frame_range[0])), 0.0)] + keys + [(min(f_b + pad, int(act.frame_range[1])), 0.0)]
        add_offsets(act, bone, 'x', ks)
    res = []
    for f in range(f_a, f_b + 1):
        bpy.context.scene.frame_set(f); res.append(thigh_angle(arm, bone))
    return round(min(res), 1)


def resample(act, src_frames, new_total):
    """Re-key every channel at integer frames 1..new_total by evaluating the existing curves at src_frames[k] (floats). Used for trims and time-scales of authored motion."""
    cb = cbag(act)
    # normalise quaternion signs first so interpolation between keys is continuous
    normalize_signs(act)
    data = {}
    for fc in cb.fcurves:
        data[(fc.data_path, fc.array_index)] = [fc.evaluate(f) for f in src_frames]
    for fc in cb.fcurves:
        vals = data[(fc.data_path, fc.array_index)]
        while len(fc.keyframe_points): fc.keyframe_points.remove(fc.keyframe_points[0])
        fc.keyframe_points.add(new_total)
        for i in range(new_total):
            kp = fc.keyframe_points[i]; kp.co = (1 + i, vals[i]); kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'; kp.interpolation = 'BEZIER'
        fc.update()
    # renormalise quaternions after component-wise interpolation
    groups = {}
    for fc in cb.fcurves:
        if fc.data_path.endswith('rotation_quaternion'): groups.setdefault(fc.data_path, {})[fc.array_index] = fc
    for dp, g in groups.items():
        if len(g) < 4: continue
        for k in range(new_total):
            q = np.array([g[i].keyframe_points[k].co[1] for i in range(4)]); q = q / np.linalg.norm(q)
            for i in range(4): g[i].keyframe_points[k].co[1] = float(q[i])
        for i in range(4): g[i].update()
    act.frame_start = 1; act.frame_end = new_total

def trim_scale(act, f_start, f_end, new_total):
    """Keep source frames f_start..f_end and spread them evenly over new_total frames (new_total < span speeds the motion up, > slows it down)."""
    src = [f_start + (f_end - f_start) * k / (new_total - 1) for k in range(new_total)]
    resample(act, src, new_total)


def axis_effect(arm, act, bone, frame, deg=20.0):
    """For +deg about the bone-local x/y/z, the world displacement of the farthest descendant tip (or bone tail), as rounded unit-scale vectors (X=right, Y=back(+)/forward(-), Z=up)."""
    z.set_action(arm, act); bpy.context.scene.frame_set(frame)
    pb = arm.pose.bones[bone]
    desc = [c for c in pb.children_recursive] or [pb]
    base = {c.name: np.array(arm.matrix_world @ c.tail) for c in desc}
    out = {}
    orig = pb.rotation_quaternion.copy()
    for ax, v in (('x', (1, 0, 0)), ('y', (0, 1, 0)), ('z', (0, 0, 1))):
        pb.rotation_quaternion = orig @ Quaternion(v, math.radians(deg))
        bpy.context.view_layer.update()
        far = max(desc, key=lambda c: np.linalg.norm(base[c.name] - np.array(arm.matrix_world @ pb.head)))
        d = np.array(arm.matrix_world @ far.tail) - base[far.name]
        out[ax] = tuple(round(float(x), 2) for x in d)
    pb.rotation_quaternion = orig; bpy.context.view_layer.update()
    return out


def add_loc_offsets(act, bone, axis_idx, keys):
    """Additive authored translation layer on one bone-local location channel (rig-local units); smoothstep between explicit keys."""
    ks = sorted(keys)
    fc = None
    for c in cbag(act).fcurves:
        if c.data_path == f'pose.bones["{bone}"].location' and c.array_index == axis_idx: fc = c
    f0 = int(act.frame_range[0]); f1 = int(act.frame_range[1])
    for f in range(f0, f1 + 1):
        off = 0.0
        for (fa, da), (fb, db) in zip(ks, ks[1:]):
            if fa <= f <= fb:
                t = (f - fa) / max(fb - fa, 1); s = t * t * (3 - 2 * t); off = da + (db - da) * s; break
        if f < ks[0][0]: off = ks[0][1]
        if f > ks[-1][0]: off = ks[-1][1]
        kp = _kp(fc, f)
        if kp: kp.co[1] = kp.co[1] + off; kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'
    fc.update()

def ground_in_place(arm, body, act, root='Hips', target=0.004, frames=None, both=False):
    """Lift the root on frames where the lowest vertex is below target (never lowers): removes floor penetration without flattening authored airtime."""
    z.set_action(arm, act)
    f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    scale = arm.matrix_world.to_scale().z
    fix = {}
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f)
        dg = bpy.context.evaluated_depsgraph_get(); eo = body.evaluated_get(dg); me = eo.to_mesh()
        co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
        M = np.array(body.matrix_world); low = (co @ M[:3, :3].T + M[:3, 3])[:, 2].min(); eo.to_mesh_clear()
        if low < target or (both and low > target + 0.003): fix[f] = target - low
    pb = arm.pose.bones[root]
    for f, dz in fix.items():
        bpy.context.scene.frame_set(f)
        m = pb.matrix.copy(); m.translation.z += dz / scale; pb.matrix = m
        bpy.context.view_layer.update(); pb.keyframe_insert('location', frame=f)
    return len(fix), max(fix.values()) if fix else 0.0
