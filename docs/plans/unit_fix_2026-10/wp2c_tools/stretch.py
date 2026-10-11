"""Lab library: edge-growth measurement in posed frames and region-limited weight smoothing."""
import sys
sys.path.insert(0, r"<mod root>/.tmp/wp2b")
import bpy, numpy as np, math
import zv as z

def rest_coords(body):
    co = np.empty(len(body.data.vertices) * 3); body.data.vertices.foreach_get('co', co); return co.reshape(-1, 3)

def edges_arr(body):
    e = np.empty(len(body.data.edges) * 2, dtype=np.int64); body.data.edges.foreach_get('vertices', e); return e.reshape(-1, 2)

def posed_coords(body):
    dg = bpy.context.evaluated_depsgraph_get(); eo = body.evaluated_get(dg); me = eo.to_mesh()
    co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); eo.to_mesh_clear(); return co.reshape(-1, 3)

def growth(body, arm, act, frame, scale=None):
    """absolute edge growth (mesh units scaled by body matrix) at (action, frame) relative to the rest pose"""
    E = edges_arr(body); R0 = rest_coords(body); s = body.matrix_world.to_scale()[0] if scale is None else scale
    z.set_action(arm, act); bpy.context.scene.frame_set(frame); P = posed_coords(body)
    l0 = np.linalg.norm(R0[E[:, 0]] - R0[E[:, 1]], axis=1); l1 = np.linalg.norm(P[E[:, 0]] - P[E[:, 1]], axis=1)
    return (l1 - l0) * s, E

def count_over(body, arm, act, frame, thr=0.3):
    g, E = growth(body, arm, act, frame); return int((g > thr).sum())

def vertex_adjacency(body):
    n = len(body.data.vertices); adj = [[] for _ in range(n)]
    for a, b in edges_arr(body): a = int(a); b = int(b); adj[a].append(b); adj[b].append(a)
    return adj

def smooth_weights(body, verts, groups, adj, iters=1, lam=0.5, keep_max=4):
    """Laplacian smoothing of the named group weights over `verts` (set of vertex indices), blended with factor lam; keeps at most keep_max influences and renormalises over ALL groups."""
    gidx = {g.name: g.index for g in body.vertex_groups}; gi = [gidx[n] for n in groups]
    me = body.data
    def getw(v):
        return {g.group: g.weight for g in me.vertices[v].groups}
    W = {int(v): getw(int(v)) for v in set(verts)}
    cache = {}
    for it in range(iters):
        new = {}
        for v in W:
            nb = [u for u in adj[v]]
            base = W[v]; acc = {}; cnt = 0
            for u in nb:
                wu = W.get(u) or cache.setdefault(u, getw(u)); cnt += 1
                for g, x in wu.items():
                    if g in gi: acc[g] = acc.get(g, 0.0) + x
            nw = dict(base)
            tot_g = sum(base.get(g, 0.0) for g in gi)
            if cnt and tot_g > 0:
                avg = {g: acc.get(g, 0.0) / cnt for g in gi}; sa = sum(avg.values())
                if sa > 0:
                    for g in gi: nw[g] = (1 - lam) * base.get(g, 0.0) + lam * avg[g] * (tot_g / sa)
            new[v] = nw
        W = new
    for v, w in W.items():
        items = sorted(w.items(), key=lambda kv: -kv[1])[:keep_max]; s = sum(x for _, x in items) or 1.0
        keep = {g: x / s for g, x in items}
        for g in [g for g in w if g not in keep]:
            body.vertex_groups[g].remove([v])
        for g, x in keep.items(): body.vertex_groups[g].add([v], x, 'REPLACE')

def ring_expand(adj, verts, rings):
    cur = set(verts)
    for _ in range(rings):
        nxt = set(cur)
        for v in cur: nxt.update(adj[v])
        cur = nxt
    return cur
