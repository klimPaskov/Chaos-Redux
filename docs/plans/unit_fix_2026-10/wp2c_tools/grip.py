"""Lab library: hand skinning in numpy, contact-based finger curl around a cylinder, hand-frame helpers."""
import sys
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import bpy, numpy as np, math
from mathutils import Vector, Matrix, Quaternion
import holdtools as H
import fingers as F

def zero_pose(arm):
    for pb in arm.pose.bones:
        pb.rotation_mode = 'QUATERNION'; pb.rotation_quaternion = (1, 0, 0, 0); pb.location = (0, 0, 0); pb.scale = (1, 1, 1)
    bpy.context.view_layer.update()

def hand_data(arm, body, side, vmask_bones=None):
    """vertices influenced by the hand bone or any finger bone of the side, with their weights per bone and rest world positions."""
    hb = side + 'Hand'; me = body.data
    gmap = {g.index: g.name for g in body.vertex_groups if g.name.startswith(hb)}
    idx = []; wts = []
    for v in me.vertices:
        w = {gmap[g.group]: g.weight for g in v.groups if g.group in gmap and g.weight > 1e-4}
        if w and sum(w.values()) > 0.15: idx.append(v.index); wts.append(w)
    M = np.array(body.matrix_world)
    rest = np.array([M[:3, :3] @ np.array(me.vertices[i].co) + M[:3, 3] for i in idx])
    bones = sorted({b for w in wts for b in w})
    W = np.zeros((len(idx), len(bones)))
    for r, w in enumerate(wts):
        for b, x in w.items(): W[r, bones.index(b)] = x
    return dict(idx=np.array(idx), rest=rest, bones=bones, W=W, side=side)

def skin_matrices(arm, bones):
    """armature-space skinning matrices (pose * rest^-1) as 4x4 numpy for the named bones (current pose, view layer must be updated)"""
    out = []
    for b in bones:
        pb = arm.pose.bones[b]; rest = arm.data.bones[b].matrix_local
        out.append(np.array(pb.matrix @ rest.inverted()))
    return out

def pose_positions(arm, hd):
    Mw = np.array(arm.matrix_world); Mi = np.linalg.inv(Mw)
    mats = skin_matrices(arm, hd['bones'])
    vloc = (Mi[:3, :3] @ hd['rest'].T).T + Mi[:3, 3]
    out = np.zeros_like(vloc)
    for k, m in enumerate(mats):
        p = (m[:3, :3] @ vloc.T).T + m[:3, 3]
        out += hd['W'][:, [k]] * p
    return (Mw[:3, :3] @ out.T).T + Mw[:3, 3]

def cyl_dist(P, c, a, r):
    """signed distance of points to a cylinder surface (infinite, axis through c with unit dir a, radius r)"""
    d = P - c; t = d @ a; perp = d - np.outer(t, a)
    return np.linalg.norm(perp, axis=1) - r

LIMITS = {'Index': (90, 100, 80), 'Middle': (90, 100, 80), 'Ring': (90, 100), 'Pinky': (90, 100), 'Thumb': (60, 70)}

def set_bend(arm, side, nm, b, deg, axis=(1, 0, 0)):
    pb = arm.pose.bones['%sHand%s%d' % (side, nm, b + 1)]; pb.rotation_mode = 'QUATERNION'
    pb.rotation_quaternion = Quaternion(axis, math.radians(deg))

def curl_solve(arm, body, hd, side, c_world, a_world, r, eps=0.010, step=2.0, backoff=0.25):
    """Four fingers: rotate each segment (proximal first) about its local X until it touches the cylinder; a proximal or middle segment that is stopped by a
    distal contact backs off by `backoff` so the following segments can wrap. Thumb: first moved off the shaft if it intersects, then curled to contact."""
    ang = {}
    for nm in F.FINGER_NAMES:
        for b in range(F.NSEG[nm]): set_bend(arm, side, nm, b, 0.0)
    bpy.context.view_layer.update()
    for nm in F.FINGER_NAMES[:4]:
        segs = F.NSEG[nm]; lim = LIMITS[nm]
        bone_names = ['%sHand%s%d' % (side, nm, b + 1) for b in range(segs)]
        cols = [hd['bones'].index(n) for n in bone_names]
        for b in range(segs):
            sel = np.nonzero(hd['W'][:, cols[b:]].sum(1) > 0.5)[0]
            own = np.nonzero(hd['W'][:, cols[b]] > 0.45)[0]
            th = 0.0; why = None
            while th < lim[b]:
                set_bend(arm, side, nm, b, th + step); bpy.context.view_layer.update()
                P = pose_positions(arm, hd); th += step
                if len(own) and cyl_dist(P[own], c_world, a_world, r).min() < eps: why = 'own'; break
                if len(sel) and cyl_dist(P[sel], c_world, a_world, r).min() < 0.5 * eps: why = 'chain'; break
            if why == 'chain' and b < segs - 1: th = max(th * (1.0 - backoff) - step, 0.0)
            set_bend(arm, side, nm, b, th); bpy.context.view_layer.update(); ang[bone_names[b]] = th
    # thumb
    t1, t2 = '%sHandThumb1' % side, '%sHandThumb2' % side
    cols = [hd['bones'].index(t1), hd['bones'].index(t2)]
    sel = np.nonzero(hd['W'][:, cols].sum(1) > 0.5)[0]
    def pen(): 
        P = pose_positions(arm, hd); return cyl_dist(P[sel], c_world, a_world, r).min()
    best = None
    for ax in ((1, 0, 0), (0, 0, 1), (0, 1, 0)):
        for sg in (1, -1):
            for th in np.arange(0.0, 70.0, 4.0):
                set_bend(arm, side, 'Thumb', 0, sg * th, ax); bpy.context.view_layer.update()
                if pen() > 0.004: break
            else: th = 99
            if best is None or th < best[0]: best = (th, ax, sg)
    th, ax, sg = best
    set_bend(arm, side, 'Thumb', 0, sg * (th if th < 99 else 0.0), ax); bpy.context.view_layer.update()
    ang[t1] = (sg * th, ax)
    own = np.nonzero(hd['W'][:, cols[1]] > 0.45)[0]; t2a = 0.0
    while t2a < 60.0:
        set_bend(arm, side, 'Thumb', 1, sg * (t2a + step), ax); bpy.context.view_layer.update(); t2a += step
        if len(own) and cyl_dist(pose_positions(arm, hd)[own], c_world, a_world, r).min() < eps: break
    ang[t2] = (sg * t2a, ax)
    return ang

def finger_report(arm, hd, side, c, a, r):
    P = pose_positions(arm, hd); rep = {}
    for nm in F.FINGER_NAMES:
        segs = F.NSEG[nm]; cols = [hd['bones'].index('%sHand%s%d' % (side, nm, b + 1)) for b in range(segs)]
        sel = np.nonzero(hd['W'][:, cols].sum(1) > 0.5)[0]
        d = cyl_dist(P[sel], c, a, r); rep[nm] = (round(float(d.min()), 3), round(float(np.percentile(d, 25)), 3))
    return rep
