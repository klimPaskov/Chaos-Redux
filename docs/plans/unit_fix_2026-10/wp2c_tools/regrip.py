"""Lab library: re-grip an item onto a hand frame, solve both arms per frame, curl fingers, key the fingers."""
import sys
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import bpy, numpy as np, math, json
from mathutils import Vector, Matrix, Quaternion
import holdtools as H, acttools as A, zv as z
import fingers as F, grip as Gp

def _rot_bone(arm, name, pivot, cur, goal):
    q = cur.normalized().rotation_difference(goal.normalized())
    pb = arm.pose.bones[name]; world = arm.matrix_world @ pb.matrix
    turned = Matrix.Translation(pivot) @ q.to_matrix().to_4x4() @ Matrix.Translation(-pivot) @ world
    pb.matrix = arm.matrix_world.inverted() @ turned
    pb.scale = (1.0, 1.0, 1.0)
    bpy.context.view_layer.update()
H.rot_bone = _rot_bone

def reset_scales(arm):
    for pb in arm.pose.bones: pb.scale = (1.0, 1.0, 1.0)
    bpy.context.view_layer.update()

def set_world_rot(arm, bone, Rdes):
    Rc = np.array(H.rot3(arm, bone)); dR = Rdes @ Rc.T
    q = Matrix(dR.tolist()).to_quaternion(); piv = H.head(arm, bone)
    pb = arm.pose.bones[bone]; world = arm.matrix_world @ pb.matrix
    turned = Matrix.Translation(piv) @ q.to_matrix().to_4x4() @ Matrix.Translation(-piv) @ world
    pb.matrix = arm.matrix_world.inverted() @ turned
    pb.scale = (1.0, 1.0, 1.0)
    bpy.context.view_layer.update()

def item_world(item):
    co = np.empty(len(item.data.vertices) * 3); item.data.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
    M = np.array(item.matrix_world); return co @ M[:3, :3].T + M[:3, 3]

def set_item_world(item, w):
    Mi = np.linalg.inv(np.array(item.matrix_world)); loc = w @ Mi[:3, :3].T + Mi[:3, 3]
    item.data.vertices.foreach_set('co', loc.ravel()); item.data.update()

def hand_base(arm, body, side, beta=20.0, dsh=0.12, tt=0.0, ref=None):
    """rest pose active: hand-local grip frame; G(r) = base + N*r"""
    g = F.grip_frame(arm, body, side, beta_deg=beta)
    base = g['Pc'] + g['N'] * (g['h'] + tt) + g['D'] * dsh
    a = g['a'] / np.linalg.norm(g['a'])
    if ref is not None and float(np.dot(a, np.asarray(ref) / np.linalg.norm(ref))) < 0: a = -a
    return dict(a=a, N=g['N'], D=g['D'], base=base, Pc=g['Pc'], h=g['h'])

def stageA(arm, body, item, side, fr, al_old, pm_old, r_item, actions):
    """Move the item into the palm grip (rigid, one bone) and counter-rotate the hand keys so the item keeps its world orientation."""
    hb = side + 'Hand'
    Rr = np.array(H.rot3(arm, hb)); hd = np.array(H.head(arm, hb))
    a_g = fr['a']; G = fr['base'] + fr['N'] * r_item
    al = np.array(al_old) / np.linalg.norm(al_old)
    q = Vector(al).rotation_difference(Vector(a_g)); Rot = np.array(q.to_matrix())
    w = item_world(item); x = (w - hd) @ Rr
    x2 = (Rot @ x.T).T + (G - Rot @ np.array(pm_old))
    set_item_world(item, hd + x2 @ Rr.T)
    qi = q.inverted()
    for act in actions:
        f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
        for f in range(f0, f1 + 1):
            l, r = A._pose(act, hb, f); qq = Quaternion(r.tolist()) @ qi
            if np.dot(np.array(qq), r) < 0: qq = Quaternion([-v for v in qq])
            A._write(act, hb, f, None, np.array(qq))
        for fc in A.cbag(act).fcurves: fc.update()
    ang = math.degrees(q.angle)
    return dict(rot_deg=round(ang, 1), G=G.round(3).tolist())

def radius_profile(item, c0, a0, sgrid, width=0.25, pct=40):
    """shaft radius around the axis through c0 (world) with direction a0, at stations sgrid measured from c0"""
    w = item_world(item); d = w - c0; t = d @ a0; perp = np.linalg.norm(d - np.outer(t, a0), axis=1); out = []
    for s in sgrid:
        m = np.abs(t - s) < width
        out.append(float(np.percentile(perp[m], pct)) if m.sum() > 6 else np.nan)
    out = np.array(out); ok = ~np.isnan(out)
    if ok.sum(): out = np.interp(np.arange(len(out)), np.nonzero(ok)[0], out[ok])
    return out

def smooth_dz(need, rad=12, sigma=4.0):
    n = len(need); d = np.array([need[max(0, i - rad):i + rad + 1].max() for i in range(n)])
    k = int(3 * sigma); g = np.exp(-0.5 * (np.arange(-k, k + 1) / sigma) ** 2); g /= g.sum()
    pad = np.pad(d, k, mode='edge'); return np.convolve(pad, g, mode='valid')

def compute_poles(arm, act, up, fo, hand, thr=0.12, sigma=1.5, max_step_deg=25.0):
    """Elbow-pole field from the present pose: the actual bend direction where the arm is bent, interpolated through straight stretches, lightly smoothed,
    and limited to max_step_deg of change per frame so the elbow never flips."""
    z.set_action(arm, act); f0, f1 = int(act.frame_range[0]), int(act.frame_range[1]); V = []; ok = []
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f)
        S = H.head(arm, up); E = H.head(arm, fo); W = H.head(arm, hand); u = (W - S).normalized(); n = (E - S) - u * (E - S).dot(u)
        if n.length > thr: V.append(np.array(n.normalized())); ok.append(True)
        else: V.append(np.zeros(3)); ok.append(False)
    V = np.array(V); ok = np.array(ok); n = len(V)
    idx = np.nonzero(ok)[0]
    if len(idx) == 0: V[:] = np.array([0.0, 0.3, -1.0]) / np.linalg.norm([0.0, 0.3, -1.0])
    else:
        for c in range(3): V[:, c] = np.interp(np.arange(n), idx, V[idx, c])
    k = int(3 * sigma); g = np.exp(-0.5 * (np.arange(-k, k + 1) / sigma) ** 2); g /= g.sum()
    Vs = np.stack([np.convolve(np.pad(V[:, c], k, mode='edge'), g, mode='valid') for c in range(3)], 1)
    out = np.zeros_like(Vs); prev = None; mx = math.radians(max_step_deg)
    for i in range(n):
        v = Vs[i] / max(np.linalg.norm(Vs[i]), 1e-9)
        if prev is not None:
            ang = math.acos(max(-1.0, min(1.0, float(np.dot(prev, v)))))
            if ang > mx:
                t = mx / ang; v = prev * (1 - t) + v * t; v /= max(np.linalg.norm(v), 1e-9)
        out[i] = v; prev = v
    return out

def solve_frames(arm, cfg, act, rows, dz, rleft, sL_sign, from_current=False):
    """per frame hold solve. cfg: main, off, up_m, fo_m, up_o, fo_o, G_R (hand-local), a_gR, a_gL, N_L, baseL.
    from_current: targets are read from the present pose (right grip point + dz, right shaft axis); the right arm is only re-solved where dz > 0."""
    z.set_action(arm, act); f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    main, off = cfg['main'], cfg.get('off'); res = []
    pole_m = compute_poles(arm, act, cfg['up_m'], cfg['fo_m'], main)
    pole_o = compute_poles(arm, act, cfg['up_o'], cfg['fo_o'], off) if off else None
    for k, f in enumerate(range(f0, f1 + 1)):
        bpy.context.scene.frame_set(f); reset_scales(arm)
        R_des_R = np.array(H.rot3(arm, main))
        if from_current:
            G_Rw = H.head(arm, main) + H.rot3(arm, main) @ Vector(list(cfg['G_R']))
            aT = (H.rot3(arm, main) @ Vector(list(cfg['a_gR']))).normalized(); P_T = G_Rw + Vector((0, 0, float(dz[k])))
            do_right = dz[k] > 1e-6
            s = rows[k] if rows else None
        else:
            row = rows[k]; P = Vector(row[1]); aT = Vector(row[2]).normalized(); P_T = P + Vector((0, 0, float(dz[k]))); do_right = True; s = row[3]
        if off:
            Rcur = np.array(H.rot3(arm, off)); v = Rcur @ cfg['a_gL']; goal = aT * sL_sign
            if cfg.get('no_align'): R_des_L = Rcur
            else:
                qd = Vector(v.tolist()).rotation_difference(goal); R_des_L = np.array(qd.to_matrix()) @ Rcur
            G_L = cfg['baseL'] + cfg['N_L'] * float(rleft[k]); s = min(max(s, cfg['s_min']), cfg['s_max'])
            T_L = P_T + aT * s
        def left_iter(T_L_, n_it):
            for it in range(n_it):
                H.solve_arm(arm, cfg['up_o'], cfg['fo_o'], off, T_L_, list(G_L), iters=5, pole=Vector(pole_o[k].tolist()))
                set_world_rot(arm, off, R_des_L)
            return (H.head(arm, off) + H.rot3(arm, off) @ Vector(list(G_L)) - T_L_).length
        for it in range(4):
            if do_right:
                H.solve_arm(arm, cfg['up_m'], cfg['fo_m'], main, P_T, list(cfg['G_R']), iters=5, pole=Vector(pole_m[k].tolist()))
                set_world_rot(arm, main, R_des_R)
            if off:
                H.solve_arm(arm, cfg['up_o'], cfg['fo_o'], off, T_L, list(G_L), iters=5, pole=Vector(pole_o[k].tolist()))
                set_world_rot(arm, off, R_des_L)
        s_used = s
        if off:
            best = ((H.head(arm, off) + H.rot3(arm, off) @ Vector(list(G_L)) - T_L).length, s)
            if best[0] > cfg.get('tol', 0.04):
                snap = {n: arm.pose.bones[n].matrix.copy() for n in (cfg['up_o'], cfg['fo_o'], off)}
                for ds in (0.4, -0.4, 0.8, -0.8, 1.2, -1.2, 1.6, -1.6, 2.0, -2.0):
                    st = min(max(s + ds, cfg['s_min']), cfg['s_max'])
                    if abs(st - s) < 1e-6: continue
                    r_try = left_iter(P_T + aT * st, 3)
                    if r_try < best[0] - 0.01: best = (r_try, st)
                    if r_try < cfg.get('tol', 0.04) * 0.75: break
                s_used = best[1]; T_L = P_T + aT * s_used; left_iter(T_L, 3)
        pr = (H.head(arm, main) + H.rot3(arm, main) @ Vector(list(cfg['G_R'])) - P_T).length if do_right else 0.0
        pl = (H.head(arm, off) + H.rot3(arm, off) @ Vector(list(G_L)) - T_L).length if off else 0.0
        res.append((pr, pl, s_used))
        names = ([cfg['up_m'], cfg['fo_m'], main] if do_right else []) + ([cfg['up_o'], cfg['fo_o'], off] if off else [])
        for n in names: arm.pose.bones[n].keyframe_insert('rotation_quaternion', frame=f)
    return res

def item_min_z(arm, item, act):
    z.set_action(arm, act); f0, f1 = int(act.frame_range[0]), int(act.frame_range[1]); out = []
    for f in range(f0, f1 + 1):
        bpy.context.scene.frame_set(f)
        dg = bpy.context.evaluated_depsgraph_get(); eo = item.evaluated_get(dg); me = eo.to_mesh()
        co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
        M = np.array(item.matrix_world); out.append(float((co @ M[:3, :3].T + M[:3, 3])[:, 2].min())); eo.to_mesh_clear()
    return np.array(out)

def key_fingers(arm, act, side, qmap, frames=None):
    z.set_action(arm, act); f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    for f in (frames or range(f0, f1 + 1)):
        for name, q in qmap.items():
            pb = arm.pose.bones[name]; pb.rotation_mode = 'QUATERNION'; pb.rotation_quaternion = q; pb.keyframe_insert('rotation_quaternion', frame=f)


def hand_centroid_all(arm, body, side, thr=0.5):
    """hand-local centroid of the vertices whose summed weight on the hand bone and its finger bones is >= thr (same as the pre-finger Hand-only centroid)"""
    hb = side + 'Hand'; gis = {g.index for g in body.vertex_groups if g.name.startswith(hb)}
    idx = [v.index for v in body.data.vertices if sum(g.weight for g in v.groups if g.group in gis) >= thr]
    M = np.array(body.matrix_world); me = body.data
    wc = np.array([M[:3, :3] @ np.array(me.vertices[i].co) + M[:3, 3] for i in idx])
    h = np.array(H.head(arm, hb)); R = np.array(H.rot3(arm, hb))
    return (wc.mean(0) - h) @ R

def tilt_fix(arm, item, act, hand, clear, rounds=5, sigma=2.0):
    """Floor clearance by turning the item (with the hand, about the wrist) so its lowest vertex reaches `clear`; the correction is smoothed over time on the hand keys. Returns (frames_fixed_first_round, min_z_after)."""
    import acttools as A
    z.set_action(arm, act); f0, f1 = int(act.frame_range[0]), int(act.frame_range[1]); first = None
    for rd in range(rounds):
        fixed = []
        for f in range(f0, f1 + 1):
            bpy.context.scene.frame_set(f); reset_scales(arm)
            dg = bpy.context.evaluated_depsgraph_get(); eo = item.evaluated_get(dg); me = eo.to_mesh()
            co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3); M = np.array(item.matrix_world)
            wc = co @ M[:3, :3].T + M[:3, 3]; eo.to_mesh_clear(); k = int(wc[:, 2].argmin()); low = Vector(wc[k])
            if low.z >= clear - 1e-4: continue
            piv = H.head(arm, hand); d = low - piv; r = d.length
            hz = Vector((d.x, d.y, 0.0))
            if hz.length < 1e-6: hz = Vector((1, 0, 0))
            ts = max(-1.0, min(1.0, (clear + 0.01 - piv.z) / r)); nd = hz.normalized() * math.sqrt(1 - ts * ts) + Vector((0, 0, ts))
            H.rot_bone(arm, hand, piv, d, nd); arm.pose.bones[hand].keyframe_insert('rotation_quaternion', frame=f); fixed.append(f)
        if first is None: first = len(fixed)
        if not fixed: break
        a, b = min(fixed), max(fixed)
        A.normalize_signs(act)
        if sigma > 0: A.smooth_window(act, a, b, sigma=sigma, bones=[hand], taper=4); A.normalize_signs(act)
    mz = item_min_z(arm, item, act)
    return first, float(mz.min())

def limit_rel(act, bone, ref, f0, f1, max_deg, taper=0):
    """Soft-saturate the rotation of `bone` relative to its pose at frame `ref` over [f0, f1]: angle -> max*tanh(angle/max) (axis kept)."""
    import acttools as A
    q0 = Quaternion(A._pose(act, bone, ref)[1].tolist()); mx = math.radians(max_deg)
    for f in range(f0, f1 + 1):
        l, r = A._pose(act, bone, f); q = Quaternion(r.tolist()); rel = q0.inverted() @ q
        if rel.w < 0: rel = Quaternion((-rel.w, -rel.x, -rel.y, -rel.z))
        ax, ang = rel.to_axis_angle()
        if ang < 1e-6: continue
        a2 = mx * math.tanh(ang / mx); new = q0 @ Quaternion(ax, a2)
        if np.dot(np.array(new), r) < 0: new = Quaternion([-v for v in new])
        A._write(act, bone, f, None, np.array(new))
    for fc in A.cbag(act).fcurves: fc.update()


def speed_retime(arm, body, act, role, lw, la, max_sub=26, min_dur=0.6, max_total=None):
    """Re-time an action on a continuous time axis: every source interval gets a duration in output frames of max(world step/lw, joint rotation step/la) clipped to [min_dur, max_sub]
    (intervals that already respect the limits keep one frame, very slow intervals may shrink to min_dur); the action is re-keyed at integer output frames by evaluating the existing curves at the
    inverse-mapped fractional source frames. Returns the old->new frame map."""
    import acttools as A
    fr, names, J = z.joint_track(arm, act); Q = z.LAST_Q
    d = np.linalg.norm(np.diff(J, axis=0), axis=2).max(1)
    dots = np.abs((Q[1:] * Q[:-1]).sum(2)).clip(0, 1); ang = np.degrees(2 * np.arccos(dots)).max(1)
    need = np.maximum(d / lw, ang / la)
    dur = np.clip(np.where(need > 1.0, need, np.maximum(1.0 - 0.0 * need, 1.0)), 1.0, max_sub)
    if min_dur < 1.0: dur = np.where(need < 0.35, np.maximum(min_dur, need / 0.35 * 1.0 * (1.0 - min_dur) + min_dur), dur)
    T = np.concatenate([[0.0], np.cumsum(dur)]); total = int(math.ceil(T[-1])) + 1
    src = []
    for k in range(total):
        t = min(k, T[-1]); i = int(np.searchsorted(T, t, side='right')) - 1; i = min(max(i, 0), len(dur) - 1)
        src.append(fr[i] + (t - T[i]) / dur[i] * (fr[i + 1] - fr[i]))
    src[-1] = float(fr[-1])
    if max_total and total > max_total: return None
    newidx = {fr[i]: float(T[i]) + 1 for i in range(len(fr))}
    A.resample(act, src, total)
    return newidx
