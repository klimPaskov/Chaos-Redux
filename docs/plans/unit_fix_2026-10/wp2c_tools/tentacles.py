"""Lab library: find tentacle tubes of the parasitic zombie (thin flesh structures), cluster them by tip, build chains and weights."""
import sys, heapq
sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import bpy, numpy as np, math, bmesh
from mathutils import Vector
from mathutils.bvhtree import BVHTree
import fingers as F, stretch as S

def flesh_mask(body, diffuse_path, sat_thr=0.12):
    img = bpy.data.images.load(diffuse_path, check_existing=False); W, Hh = img.size
    im = (np.array(img.pixels[:], dtype=np.float32).reshape(Hh, W, 4)[:, :, :3] * 255.0)[::-1]
    me = body.data; uvl = me.uv_layers['UVMap'].data if 'UVMap' in me.uv_layers else me.uv_layers[0].data
    sat = np.zeros(len(me.polygons))
    for p in me.polygons:
        u = np.mean([uvl[l].uv[0] for l in p.loop_indices]); v = np.mean([uvl[l].uv[1] for l in p.loop_indices])
        x = min(max(int(u * W), 0), W - 1); y = min(max(int((1 - v) * Hh), 0), Hh - 1); c = im[y, x]; sat[p.index] = (c.max() - c.min()) / (c.max() + 1e-6)
    bpy.data.images.remove(img)
    return sat > sat_thr

def tube_vertices(body, face_mask, tmax=6.0, ray=12.0):
    me = body.data; bm = bmesh.new(); bm.from_mesh(me); bm.verts.ensure_lookup_table(); bm.faces.ensure_lookup_table(); bvh = BVHTree.FromBMesh(bm)
    flesh = set()
    for p in me.polygons:
        if face_mask[p.index]: flesh.update(p.vertices)
    tube = np.zeros(len(me.vertices), bool)
    for v in flesh:
        co = me.vertices[v].co; n = me.vertices[v].normal; best = 99.0
        for jit in ((0, 0, 0), (0.3, 0, 0), (0, 0.3, 0)):
            d = (-n + Vector(jit)).normalized(); hit = bvh.ray_cast(co + d * 1e-4, d, ray)
            if hit[0] is not None: best = min(best, hit[3])
        tube[v] = best < tmax
    bm.free(); return tube

def tube_graph(body, tube, minsize=60):
    me = body.data; adj = S.vertex_adjacency(body); M = np.array(body.matrix_world)
    co = np.array([M[:3, :3] @ np.array(v.co) + M[:3, 3] for v in me.vertices])
    seen = np.zeros(len(tube), bool); keep = np.zeros(len(tube), bool)
    for v in np.nonzero(tube)[0]:
        if seen[v]: continue
        st = [int(v)]; seen[v] = True; m = []
        while st:
            u = st.pop(); m.append(u)
            for w in adj[u]:
                if tube[w] and not seen[w]: seen[w] = True; st.append(w)
        if len(m) >= minsize: keep[m] = True
    idx = np.nonzero(keep)[0]; pos = {int(i): k for k, i in enumerate(idx)}
    g = [[] for _ in idx]
    for i in idx:
        for w in adj[i]:
            if keep[w]: g[pos[int(i)]].append((pos[int(w)], float(np.linalg.norm(co[i] - co[w]))))
    roots = [pos[int(i)] for i in idx if any((not keep[w]) for w in adj[i])]
    return dict(idx=idx, pos=pos, g=g, co=co[idx], roots=roots, adj=adj, keep=keep, co_all=co)

def cluster_tips(T, tip_r=0.15, min_d=0.6, max_tips=8, detour=0.3):
    n = len(T['idx']); d, pred = F.dijkstra(n, T['g'], T['roots']); c2 = T['co']
    order = np.argsort(-np.where(d < 1e8, d, -1)); tips = []
    for i in order:
        if d[i] < min_d or d[i] > 1e8: break
        if all(np.linalg.norm(c2[i] - c2[t]) > tip_r for t in tips):
            near = np.nonzero(np.linalg.norm(c2 - c2[i], axis=1) < tip_r)[0]
            if d[near].max() <= d[i] + 1e-9: tips.append(int(i))
    G = []
    for t in tips:
        g_, _ = F.dijkstra(n, T['g'], [t]); G.append(g_)
    det = np.stack([d + G[k] - d[tips[k]] for k in range(len(tips))], 1); best = det.argmin(1); lab = np.where(det.min(1) < detour, best, -1)
    sizes = np.array([(lab == k).sum() for k in range(len(tips))])
    keep_k = list(np.argsort(-sizes)[:max_tips]); remap = {k: j for j, k in enumerate(keep_k)}
    lab2 = np.array([remap.get(int(l), -1) for l in lab])
    T.update(d=d, lab=lab2, tips=[tips[k] for k in keep_k], ntips=len(tips))
    return T

# ---------------------------------------------------------------- angular bundle chains
def bundles(T, k=8, min_r=0.35, seed=3):
    """Cluster all kept tube vertices into k angular bundles around the tube-root hub (k-means on unit directions), returns labels, hub, directions."""
    c2 = T['co']; roots = T['roots']
    hub = c2[roots].mean(0)
    v = c2 - hub; r = np.linalg.norm(v, axis=1); dirs = v / np.maximum(r[:, None], 1e-6)
    sel = r > min_r; X = dirs[sel]
    rng = np.random.RandomState(seed); cen = X[rng.choice(len(X), k, replace=False)]
    for it in range(40):
        lab = np.argmax(X @ cen.T, 1)
        new = np.array([X[lab == j].mean(0) if (lab == j).any() else cen[j] for j in range(k)]); new /= np.linalg.norm(new, axis=1, keepdims=True)
        if np.allclose(new, cen, atol=1e-5): break
        cen = new
    full = np.full(len(c2), -1); full[sel] = np.argmax(X @ cen.T, 1)
    T.update(hub=hub, dirs=dirs, r=r, cen=cen, blab=full, k=k)
    return T

def bundle_chains(T, nseg=3, qs=(0.0, 0.33, 0.66, 1.0)):
    out = []
    for j in range(T['k']):
        m = np.nonzero(T['blab'] == j)[0]
        if len(m) < 30: out.append(None); continue
        r = T['r'][m]; lo, hi = np.percentile(r, 5), np.percentile(r, 97)
        js = [lo + q * (hi - lo) for q in qs]; pts = []
        for jr in js[:-1]:
            w = max(0.06, (hi - lo) * 0.12); sel = m[np.abs(T['r'][m] - jr) < w]
            if len(sel) < 3: sel = m[np.argsort(np.abs(T['r'][m] - jr))[:5]]
            pts.append(T['co'][sel].mean(0))
        tipsel = m[T['r'][m] > hi - max(0.06, (hi - lo) * 0.1)]; pts.append(T['co'][tipsel].mean(0))
        out.append(dict(m=m, js=js, pts=pts, n=len(m)))
    return out

def smooth01(x): x = min(max(x, 0.0), 1.0); return x * x * (3 - 2 * x)

def create_chain_bones(arm, body, T, chains, prefix='ParasiteT'):
    """edit-mode bones: chain j bones 1..3 along the bundle slice centroids; parent = body bone with the largest summed original weight on the chain's root slice"""
    inv = arm.matrix_world.inverted(); vg = {g.index: g.name for g in body.vertex_groups}; me = body.data
    body_bones = {b.name for b in arm.data.bones}
    parents = []
    for j, c in enumerate(chains):
        if c is None: parents.append(None); continue
        root = c['m'][T['r'][c['m']] < c['js'][1]]; acc = {}
        for i in root:
            v = int(T['idx'][i])
            for g in me.vertices[v].groups:
                n = vg[g.group]
                if n in body_bones and not n.startswith(prefix): acc[n] = acc.get(n, 0.0) + g.weight
        parents.append(max(acc, key=acc.get) if acc else 'Spine02')
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT'); eb = arm.data.edit_bones; names = {}
    for j, c in enumerate(chains):
        if c is None: continue
        prev = eb[parents[j]]; names[j] = []
        for b in range(3):
            nm = '%s%d_%d' % (prefix, j + 1, b + 1)
            if nm in eb: eb.remove(eb[nm])
            e = eb.new(nm); e.head = inv @ Vector(c['pts'][b]); e.tail = inv @ Vector(c['pts'][b + 1])
            if (e.tail - e.head).length < 1e-3: e.tail = e.head + Vector((0, 0, 0.05))
            e.parent = prev; e.use_connect = False; prev = e; names[j].append(nm)
    bpy.ops.object.mode_set(mode='OBJECT')
    return names, parents

def chain_weights(body, arm, T, chains, names, temp=0.08, blend=0.12, keep_max=4):
    """new weights for every vertex of the kept tube set: the original weights fade out along the first segment while the chain bones of the two nearest bundles take over"""
    me = body.data; idx = T['idx']; r = T['r']; dirs = T['dirs']; cen = T['cen']; k = T['k']
    cosm = dirs @ cen.T
    valid = [j for j in range(k) if chains[j] is not None]
    vgi = {g.name: g.index for g in body.vertex_groups}
    for n in sum(names.values(), []):
        if n not in vgi: body.vertex_groups.new(name=n)
    vgi = {g.name: g.index for g in body.vertex_groups}
    done = 0
    for q in range(len(idx)):
        v = int(idx[q]); cs = np.array([cosm[q, j] if j in valid else -9 for j in range(k)])
        o = np.argsort(-cs)[:2]; ws = np.exp((cs[o] - cs[o[0]]) / temp); ws /= ws.sum()
        orig = {g.group: g.weight for g in me.vertices[v].groups}
        chain_w = {}; s_tot = 0.0
        for wj, j in zip(ws, o):
            c = chains[j]; js = c['js']; rr = r[q]
            s = smooth01((rr - js[0]) / max(js[1] - js[0], 1e-6))
            bw = []
            for b in range(3):
                lo = 1.0 if b == 0 else smooth01((rr - (js[b] - blend * (js[3] - js[0]))) / (2 * blend * (js[3] - js[0])))
                hi = 0.0 if b == 2 else smooth01((rr - (js[b + 1] - blend * (js[3] - js[0]))) / (2 * blend * (js[3] - js[0])))
                bw.append(max(lo - hi, 0.0))
            tot = sum(bw) or 1.0
            for b in range(3): chain_w[vgi[names[j][b]]] = chain_w.get(vgi[names[j][b]], 0.0) + wj * s * bw[b] / tot
            s_tot += wj * s
        new = {g: w * (1.0 - s_tot) for g, w in orig.items()}
        for g, w in chain_w.items(): new[g] = new.get(g, 0.0) + w
        items = sorted(new.items(), key=lambda kv: -kv[1])[:keep_max]; sm = sum(x for _, x in items) or 1.0
        for g in list(orig):
            if g not in dict(items): body.vertex_groups[g].remove([v])
        for g, x in items: body.vertex_groups[g].add([v], x / sm, 'REPLACE')
        done += 1
    return done
