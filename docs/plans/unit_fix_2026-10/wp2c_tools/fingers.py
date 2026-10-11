"""Lab library: analyse a rest-pose hand mesh, find finger tips/clusters by geodesic structure, build finger chains + weights."""
import sys
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import bpy, numpy as np, math, heapq
from mathutils import Vector, Matrix
import holdtools as H

def dijkstra(n, adj, sources):
    d = np.full(n, 1e9); pred = np.full(n, -1); pq = []
    for s in sources: d[s] = 0.0; heapq.heappush(pq, (0.0, s))
    while pq:
        du, u = heapq.heappop(pq)
        if du > d[u]: continue
        for v, w in adj[u]:
            nd = du + w
            if nd < d[v]: d[v] = nd; pred[v] = u; heapq.heappush(pq, (nd, v))
    return d, pred

def analyse(arm, body, side, wmin=0.25, ring_y=0.2, tip_radius=0.17):
    """Rest pose must be active. Returns dict with local coords, graph distances, tips, assignment, frame."""
    hb = side + 'Hand'; me = body.data
    gis = {g.index for g in body.vertex_groups if g.name.startswith(hb)}
    Wd = {}
    for v in me.vertices:
        w = sum(g.weight for g in v.groups if g.group in gis)
        if w >= wmin: Wd[v.index] = w
    idx = np.array(sorted(Wd)); pos = {int(i): k for k, i in enumerate(idx)}
    M = np.array(body.matrix_world)
    co_w = np.array([(M[:3, :3] @ np.array(me.vertices[int(i)].co) + M[:3, 3]) for i in idx])
    h = np.array(H.head(arm, hb)); Rm = np.array(H.rot3(arm, hb))
    loc = (co_w - h) @ Rm
    adj = [[] for _ in idx]
    for e in me.edges:
        a, b = e.vertices
        if a in pos and b in pos:
            w = float(np.linalg.norm(co_w[pos[a]] - co_w[pos[b]])); adj[pos[a]].append((pos[b], w)); adj[pos[b]].append((pos[a], w))
    roots = [k for k in range(len(idx)) if loc[k, 1] < ring_y]
    d, pred = dijkstra(len(idx), adj, roots)
    return dict(hb=hb, idx=idx, pos=pos, co_w=co_w, loc=loc, adj=adj, d=d, pred=pred, h=h, Rm=Rm, roots=roots, Wd=Wd)

def find_tips(A, n_tips=5, radius=0.17, min_frac=0.4):
    d = A['d']; co = A['co_w']; n = len(d)
    order = np.argsort(-d); dmax = d[order[0]]; tips = []
    for i in order:
        if d[i] < min_frac * dmax: break
        if all(np.linalg.norm(co[i] - co[t]) > radius for t in tips):
            # local maximum within radius
            near = np.nonzero(np.linalg.norm(co - co[i], axis=1) < radius)[0]
            if d[near].max() <= d[i] + 1e-9: tips.append(int(i))
        if len(tips) >= n_tips: break
    return tips

def path_to_root(A, i):
    p = [i]
    while A['pred'][p[-1]] != -1: p.append(int(A['pred'][p[-1]]))
    return p

def lca_depth(A, a, b):
    pa = set(path_to_root(A, a)); 
    for v in path_to_root(A, b):
        if v in pa: return A['d'][v]
    return 0.0

def classify(A, tips):
    """thumb = tip with the smallest depth of its nearest-sibling branch point; fingers ordered index..pinky from the thumb side."""
    best = {}
    for t in tips:
        best[t] = max(lca_depth(A, t, o) for o in tips if o != t)
    thumb = min(tips, key=lambda t: best[t])
    four = [t for t in tips if t != thumb]
    c4 = np.mean([A['co_w'][t] for t in four], axis=0)
    lat = np.array(A['co_w'][thumb]) - c4
    # order along the direction from thumb to the far side, projected on the plane spanned by the finger spread
    P = np.array([A['co_w'][t] - c4 for t in four])
    u, s, vt = np.linalg.svd(P, full_matrices=False); ax = vt[0]
    if np.dot(ax, lat) < 0: ax = -ax    # towards the thumb
    four.sort(key=lambda t: -np.dot(A['co_w'][t] - c4, ax))
    return thumb, four

def assign(A, tips_by_name, detour_max=0.10):
    n = len(A['d']); G = {}
    for name, t in tips_by_name.items():
        g, _ = dijkstra(n, A['adj'], [t]); G[name] = g
    lab = np.full(n, -1); names = list(tips_by_name)
    det = np.stack([A['d'] + G[nm] - A['d'][tips_by_name[nm]] for nm in names], 1)
    best = det.argmin(1); ok = det.min(1) < detour_max
    lab = np.where(ok, best, -1)
    return names, lab, det, G

# ------------------------------------------------------------------ v2: axis-based segmentation
def frame(A):
    """Hand frame from geometry: D finger axis (away from the wrist ring), wrist ring centroid."""
    loc = A['co_w']; ring = loc[A['roots']].mean(0) if A['roots'] else loc.mean(0)
    P = loc - loc.mean(0); u, s, vt = np.linalg.svd(P, full_matrices=False); D = vt[0]
    if np.dot(loc.mean(0) - ring, D) < 0: D = -D
    A['ring'] = ring; A['D'] = D; A['u'] = (loc - ring) @ D
    return A

def comps_at(A, thr, minsize=8, mask=None):
    u = A['u']; adj = A['adj']; n = len(u)
    keep = [i for i in range(n) if u[i] > thr and (mask is None or mask[i])]; ks = set(keep); seen = set(); comps = []
    for i in keep:
        if i in seen: continue
        st = [i]; seen.add(i); m = []
        while st:
            x = st.pop(); m.append(x)
            for w, _ in adj[x]:
                if w in ks and w not in seen: seen.add(w); st.append(w)
        if len(m) >= minsize: comps.append(m)
    return comps

def segment(A, n_fingers=4, fl_lo=0.55, fl_hi=0.9, grow_r=0.16, base_frac=0.32, thumb_base_frac=0.22):
    A = frame(A); u = A['u']; umax = u.max(); co = A['co_w']; n = len(u)
    seeds = None
    for fr in np.arange(fl_hi, fl_lo, -0.02):
        cs = comps_at(A, fr * umax, minsize=8)
        if len(cs) == n_fingers: seeds = cs; used = fr; break
    if seeds is None:
        best = None
        for fr in np.arange(fl_hi, fl_lo, -0.02):
            cs = comps_at(A, fr * umax, minsize=8)
            if len(cs) > n_fingers: seeds = sorted(cs, key=lambda c: -len(c))[:n_fingers]; used = fr; break
            if best is None or len(cs) > len(best[0]): best = (cs, fr)
        if seeds is None and best is not None and len(best[0]) >= 2:
            cs, used = best; cs = [list(c) for c in cs]
            while len(cs) < n_fingers:     # split the largest component in two along its own principal direction (fingers that touch)
                k = max(range(len(cs)), key=lambda i: len(cs[i])); c = np.array(cs[k]); P = co[c] - co[c].mean(0)
                u_, s_, vt_ = np.linalg.svd(P, full_matrices=False); proj = P @ vt_[1]       # across the spread, not along the finger
                lo = [int(c[i]) for i in range(len(c)) if proj[i] < np.median(proj)]; hi = [int(c[i]) for i in range(len(c)) if proj[i] >= np.median(proj)]
                cs[k:k + 1] = [lo, hi]
            seeds = cs
    if seeds is None: raise RuntimeError('no finger seeds')
    lab = np.full(n, -1)
    # thumb seed: a component that stays separate from every finger seed at a lower threshold
    seedset = set(i for c in seeds for i in c); thumb = []
    for fr in np.arange(0.62, 0.38, -0.02):
        cs = [c for c in comps_at(A, fr * umax, minsize=12) if not (set(c) & seedset)]
        if cs: thumb = max(cs, key=lambda c: len(c)); break
    cen = [co[c].mean(0) for c in seeds]; P = np.array(cen) - np.mean(cen, 0)
    uu, ss, vt = np.linalg.svd(P, full_matrices=False); spread = vt[0]
    if thumb:
        tc = co[thumb].mean(0) - np.mean(cen, 0)
        if np.dot(spread, tc) < 0: spread = -spread       # index (first) on the thumb side
    order = np.argsort(-(P @ spread)); seeds = [seeds[i] for i in order]
    for k, c in enumerate(seeds): lab[c] = k
    for i in thumb: lab[i] = n_fingers
    ymin = base_frac * umax
    def grow(lab, lo, nl_range):
        changed = True
        while changed:
            changed = False
            for i in np.argsort(-u):
                if lab[i] != -1 or u[i] < lo: continue
                nb = [lab[w] for w, _ in A['adj'][i] if lab[w] in nl_range]
                if nb: lab[i] = max(set(nb), key=nb.count); changed = True; continue
                lbl = np.nonzero(np.isin(lab, list(nl_range)))[0]
                if len(lbl):
                    dd = np.linalg.norm(co[lbl] - co[i], axis=1); j = dd.argmin()
                    if dd[j] < grow_r: lab[i] = lab[lbl[j]]; changed = True
        return lab
    lab = grow(lab, min(ymin, thumb_base_frac * umax), set(range(n_fingers + 1)))
    A['lab'] = lab; A['seed_frac'] = used; A['n_fingers'] = n_fingers
    return A

# ------------------------------------------------------------------ chains, bones, weights
FINGER_NAMES = ['Index', 'Middle', 'Ring', 'Pinky', 'Thumb']
NSEG = {'Index': 3, 'Middle': 3, 'Ring': 2, 'Pinky': 2, 'Thumb': 2}
FRAC = {3: (0.0, 0.46, 0.76, 1.0), 2: (0.0, 0.55, 1.0), }

def smooth01(x): x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)

def build_chains(A, mcp_frac=0.36, blend=0.05):
    u = A['u']; co = A['co_w']; lab = A['lab']; umax = u.max(); chains = {}
    for k, nm in enumerate(FINGER_NAMES):
        m = np.nonzero(lab == k)[0]
        if len(m) < 6: raise RuntimeError('finger %s has %d verts' % (nm, len(m)))
        ut = float(np.percentile(u[m], 98))
        if nm == 'Thumb': j0 = float(np.percentile(u[m], 6)) + 0.02
        else: j0 = mcp_frac * umax
        seg = NSEG[nm]; fr = FRAC[seg]
        js = [j0 + f * (ut - j0) for f in fr]
        pts = []
        for ju in js[:-1]:
            w = 0.04
            sel = m[np.abs(u[m] - ju) < w]
            while len(sel) < 3 and w < 0.2: w += 0.02; sel = m[np.abs(u[m] - ju) < w]
            pts.append(co[sel].mean(0))
        tipv = m[u[m] > ut - 0.03]; tip = co[tipv].mean(0)
        pts.append(tip)
        chains[nm] = dict(j=js, pts=[np.array(p) for p in pts], m=m, ut=ut, seg=seg)
    # palm-side (curl) directions
    D = A['D']; curls = []
    for nm, c in chains.items():
        p0, p1, pt = c['pts'][0], c['pts'][1], c['pts'][-1]
        d0 = (p1 - p0); d0 /= np.linalg.norm(d0)
        v = (pt - p0); perp = v - d0 * np.dot(v, d0)
        c['curl'] = perp / np.linalg.norm(perp) if np.linalg.norm(perp) > 0.05 else None
    cs = [c['curl'] for nm, c in chains.items() if nm != 'Thumb' and c['curl'] is not None]
    N = np.mean(cs, 0) if cs else np.cross(D, [0, 0, 1.0]); N = N - D * np.dot(N, D); N /= np.linalg.norm(N)
    A['N'] = N; A['L'] = np.cross(D, N)
    for nm, c in chains.items():
        c['curl_raw'] = c['curl']; c['curl'] = N
    return chains

def weights_for(A, chains, blend=0.05):
    """returns {vertex_local_index: {bone_suffix: share}} shares of the vertex's old hand weight; remaining share stays on Hand"""
    u = A['u']; lab = A['lab']; out = {}
    for k, nm in enumerate(FINGER_NAMES):
        c = chains[nm]; js = c['j']; seg = c['seg']
        for i in np.nonzero(lab == k)[0]:
            x = u[i]; sh = {}
            # hand share: 1 below j0-blend .. 0 above j0+blend
            h = 1.0 - smooth01((x - (js[0] - blend)) / (2 * blend))
            rest = 1.0 - h
            # distribute `rest` over bones with hat transitions at js[1:seg]
            ws = []
            for b in range(seg):
                lo = 1.0 if b == 0 else smooth01((x - (js[b] - blend)) / (2 * blend))
                hi = 0.0 if b == seg - 1 else smooth01((x - (js[b + 1] - blend)) / (2 * blend))
                ws.append(max(lo - hi, 0.0))
            tot = sum(ws) or 1.0
            sh = {'%s%d' % (nm, b + 1): rest * ws[b] / tot for b in range(seg)}
            sh['_hand'] = h
            out[int(i)] = sh
    return out

def create_bones(arm, A, chains, side):
    inv = arm.matrix_world.inverted(); hb = side + 'Hand'
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones; names = []
    for nm, c in chains.items():
        prev = eb[hb]
        for b in range(c['seg']):
            name = '%sHand%s%d' % (side, nm, b + 1)
            if name in eb: eb.remove(eb[name])
            e = eb.new(name); e.head = inv @ Vector(c['pts'][b]); e.tail = inv @ Vector(c['pts'][b + 1])
            e.parent = prev; e.use_connect = False
            ax = np.array(inv.to_3x3() @ Vector(e.tail - e.head)); ax /= np.linalg.norm(ax)
            cl = np.array(inv.to_3x3() @ Vector(c['curl'])); cl = cl - ax * np.dot(cl, ax); cl /= np.linalg.norm(cl)
            e.align_roll(Vector(cl)); prev = e; names.append(name)
    bpy.ops.object.mode_set(mode='OBJECT')
    return names

def apply_weights(body, A, W, side):
    me = body.data; idx = A['idx']
    hb = side + 'Hand'; hg = body.vertex_groups[hb]
    groups = {}
    for i, sh in W.items():
        vi = int(idx[i]); old = None
        for g in me.vertices[vi].groups:
            if g.group == hg.index: old = g.weight
        if old is None: continue
        for bn, s in sh.items():
            if bn == '_hand': continue
            name = '%sHand%s' % (side, bn)
            if s * old < 1e-3: continue
            if name not in body.vertex_groups: body.vertex_groups.new(name=name)
            body.vertex_groups[name].add([vi], s * old, 'REPLACE')
        newh = sh['_hand'] * old
        if newh < 1e-3: hg.remove([vi])
        else: hg.add([vi], newh, 'REPLACE')

# ------------------------------------------------------------------ grip frame
def grip_frame(arm, body, side, beta_deg=25.0, ref_dir_loc=None, wing=0.2):
    """Rest pose must be active. Returns hand-bone-local (v_b coordinates) frame vectors and the palm numbers.
    D (fingers), N (palm normal toward the curl), L (thumb side lateral), palm centre Pc, palm surface offset h, diagonal grip axis a (hand-local)."""
    A = analyse(arm, body, side); A = segment(A); ch = build_chains(A)
    lab = A['lab']; u = A['u']; umax = u.max(); co = A['co_w']
    Rr = np.array(H.rot3(arm, side + 'Hand')); hd = np.array(H.head(arm, side + 'Hand'))
    D, N = A['D'], A['N']
    thumb_c = co[lab == 4].mean(0); four_c = co[(lab >= 0) & (lab < 4)].mean(0)
    L = np.cross(D, N); L /= np.linalg.norm(L)
    s_th = 1.0 if np.dot(thumb_c - four_c, L) > 0 else -1.0
    L_th = s_th * L
    palm = np.nonzero((lab == -1) & (u > 0.18 * umax) & (u < 0.34 * umax))[0]
    Pc = co[palm].mean(0)
    rel = co[palm] - Pc; lat = rel - np.outer(rel @ N, N)
    near = np.linalg.norm(lat, axis=1) < wing
    h = float(np.percentile((rel @ N)[near], 92)) if near.sum() > 3 else float((rel @ N).max())
    b = math.radians(beta_deg)
    a_world = math.cos(b) * L_th + math.sin(b) * D
    to_loc = lambda v: Rr.T @ np.asarray(v)
    out = dict(D=to_loc(D), N=to_loc(N), L=to_loc(L_th), a=to_loc(a_world), Pc=to_loc(Pc - hd), h=h, s_th=s_th, A=A, chains=ch)
    return out
