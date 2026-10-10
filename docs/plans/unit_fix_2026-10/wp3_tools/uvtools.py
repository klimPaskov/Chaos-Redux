"""Lab-side UV tools: part labelling by dominant bone, per-part smart unwrap, pack, island count."""
import bpy, bmesh, numpy as np, math

PARTS = {
 'head': ['Head','neck','head_end','headfront'],
 'torso': ['Hips','Spine02','Spine01','Spine','LeftShoulder','RightShoulder'],
 'l_arm': ['LeftArm','LeftForeArm'], 'r_arm': ['RightArm','RightForeArm'],
 'l_hand': ['LeftHand'], 'r_hand': ['RightHand'],
 'l_leg': ['LeftUpLeg','LeftLeg'], 'r_leg': ['RightUpLeg','RightLeg'],
 'l_foot': ['LeftFoot','LeftToeBase'], 'r_foot': ['RightFoot','RightToeBase'],
}

def face_parts(obj, parts=None):
    parts = parts or PARTS
    me = obj.data; names = [g.name for g in obj.vertex_groups]
    bone2part = {b:p for p,bs in parts.items() for b in bs}
    gpart = [bone2part.get(n,'torso') for n in names]
    pl = sorted(set(gpart)); pid = {p:i for i,p in enumerate(pl)}
    nv = len(me.vertices); S = np.zeros((nv, len(pl)), dtype=np.float32)
    for v in me.vertices:
        for g in v.groups: S[v.index, pid[gpart[g.group]]] += g.weight
    nf = len(me.polygons)
    fv = np.array([p.vertices[:] for p in me.polygons])
    fs = S[fv].sum(1)
    lab = fs.argmax(1)
    return lab, pl

def reassign_small(me, lab, min_faces=40):
    """Merge tiny connected same-label components into the neighbouring label with the longest shared border."""
    import collections
    nf = len(me.polygons)
    bm = bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
    changed = True
    seen = np.full(nf, -1); comps = []
    for s in range(nf):
        if seen[s] >= 0: continue
        stack = [s]; seen[s] = len(comps); cur = [s]
        while stack:
            f = bm.faces[stack.pop()]
            for e in f.edges:
                for g in e.link_faces:
                    if g.index != f.index and seen[g.index] < 0 and lab[g.index] == lab[s]:
                        seen[g.index] = len(comps); stack.append(g.index); cur.append(g.index)
        comps.append(cur)
    moved = 0
    for cur in sorted(comps, key=len):
        if len(cur) >= min_faces: continue
        cnt = collections.Counter()
        for fi in cur:
            for e in bm.faces[fi].edges:
                for g in e.link_faces:
                    if lab[g.index] != lab[fi]: cnt[lab[g.index]] += 1
        if cnt:
            tgt = cnt.most_common(1)[0][0]
            for fi in cur: lab[fi] = tgt
            moved += len(cur)
    bm.free()
    return lab, moved

def smart_unwrap_parts(obj, lab, pl, angle=1.15, margin=0.003, layer_name='UV_WP3'):
    me = obj.data
    if layer_name in me.uv_layers: me.uv_layers.remove(me.uv_layers[layer_name])
    layer = me.uv_layers.new(name=layer_name); me.uv_layers.active = layer
    bpy.context.view_layer.objects.active = obj
    for o in bpy.context.selected_objects: o.select_set(False)
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(me)
    bm.faces.ensure_lookup_table()
    # unwrap each part separately, then everything is packed together afterwards
    for pi, p in enumerate(pl):
        for f in bm.faces: f.select_set(False)
        for f in bm.faces:
            if lab[f.index] == pi: f.select_set(True)
        bm.select_flush(True)
        bmesh.update_edit_mesh(me)
        bpy.ops.uv.smart_project(angle_limit=angle, island_margin=margin, area_weight=0.0, correct_aspect=True, scale_to_bounds=False)
    for f in bm.faces: f.select_set(True)
    bmesh.update_edit_mesh(me)
    bpy.ops.uv.select_all(action='SELECT')
    bpy.ops.uv.average_islands_scale()
    bpy.ops.uv.pack_islands(margin=margin*2, rotate=True)
    bpy.ops.object.mode_set(mode='OBJECT')
    return layer_name

def island_count(me, layer_name, nd=5):
    """Count UV islands (connected via shared UV corner coords across shared edges)."""
    layer = me.uv_layers[layer_name]
    uv = np.empty(len(me.loops)*2); layer.data.foreach_get('uv', uv); uv = uv.reshape(-1,2)
    parent = {}
    def find(a):
        while parent.setdefault(a,a) != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    keys = {}
    for p in me.polygons:
        ids = []
        for li in p.loop_indices:
            k = (me.loops[li].vertex_index, round(float(uv[li][0]),nd), round(float(uv[li][1]),nd))
            find(k); ids.append(k)
        for a in ids[1:]:
            ra, rb = find(ids[0]), find(a)
            if ra != rb: parent[ra] = rb
    return len({find(k) for k in list(parent)}) if False else len({find(ids) for ids in list(parent)})

def uv_area_stats(me, layer_name):
    layer = me.uv_layers[layer_name]
    uv = np.empty(len(me.loops)*2); layer.data.foreach_get('uv', uv); uv = uv.reshape(-1,2)
    tot = 0.0
    for p in me.polygons:
        pts = uv[list(p.loop_indices)]
        tot += 0.5*abs(np.cross(pts[1]-pts[0], pts[2]-pts[0])) if len(pts)==3 else 0
    return tot, uv.min(0), uv.max(0)

def topo(obj_or_me, label=''):
    me = obj_or_me.data if hasattr(obj_or_me,'data') else obj_or_me
    bm = bmesh.new(); bm.from_mesh(me)
    bnd = sum(1 for e in bm.edges if len(e.link_faces)==1)
    nm = sum(1 for e in bm.edges if len(e.link_faces)>2)
    loose = sum(1 for v in bm.verts if not v.link_faces)
    # components
    seen=set(); comps=0; sizes=[]
    for f in bm.faces:
        if f.index in seen: continue
        comps+=1; st=[f]; seen.add(f.index); n=0
        while st:
            c=st.pop(); n+=1
            for e in c.edges:
                for g in e.link_faces:
                    if g.index not in seen: seen.add(g.index); st.append(g)
        sizes.append(n)
    r = dict(verts=len(bm.verts), faces=len(bm.faces), boundary=bnd, nonmanifold=nm, loose=loose, comps=comps, big=sorted(sizes)[-5:], small=sum(1 for s in sizes if s<50))
    bm.free()
    return r

def weld(obj, dist_local):
    me = obj.data
    bm = bmesh.new(); bm.from_mesh(me)
    before = len(bm.verts)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=dist_local)
    bm.to_mesh(me); bm.free(); me.update()
    return before, len(me.vertices)

def nm_report(me, scale=1.0, limit=12):
    bm = bmesh.new(); bm.from_mesh(me); bm.edges.ensure_lookup_table(); bm.faces.ensure_lookup_table()
    out=[]
    import collections
    cnt=collections.Counter()
    for e in bm.edges:
        n=len(e.link_faces)
        if n>2:
            cnt[n]+=1
            if len(out)<limit:
                out.append({'edge':e.index,'nf':n,'len':round(e.calc_length()*scale,4),'faces':[(f.index, round(f.calc_area()*scale*scale,5)) for f in e.link_faces]})
    # dup faces
    seen={}; dup=0
    for f in bm.faces:
        k=tuple(sorted(v.index for v in f.verts))
        if k in seen: dup+=1
        seen[k]=f.index
    bm.free()
    return dict(nm_counts=dict(cnt), dup_faces=dup, sample=out)

def repair(obj, max_hole_sides=8):
    me=obj.data
    bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
    log={}
    # 1 duplicate faces (same vertex set): keep first
    seen={}; kill=[]
    for f in bm.faces:
        k=tuple(sorted(v.index for v in f.verts))
        if k in seen: kill.append(f)
        else: seen[k]=f
    log['dup_removed']=len(kill)
    bmesh.ops.delete(bm, geom=kill, context='FACES')
    bm.to_mesh(me); bm.free(); me.update()
    return log

def fix_manifold(obj, max_sides=8, iters=6, verbose=True):
    """Drop the smallest face on every >2-face edge, then close simple boundary loops (<= max_sides) with new-chord triangles."""
    me=obj.data; log=[]
    for it in range(iters):
        bm=bmesh.new(); bm.from_mesh(me); bm.edges.ensure_lookup_table(); bm.faces.ensure_lookup_table()
        kill=set()
        for e in bm.edges:
            if len(e.link_faces)>2:
                grpA=[l.face for l in e.link_loops if l.vert==e.verts[0]]
                grpB=[l.face for l in e.link_loops if l.vert!=e.verts[0]]
                keep=set()
                if grpA and grpB:
                    keep.add(max(grpA,key=lambda f:f.calc_area())); keep.add(max(grpB,key=lambda f:f.calc_area()))
                else:
                    for f in sorted(e.link_faces,key=lambda f:-f.calc_area())[:1]: keep.add(f)
                for f in e.link_faces:
                    if f not in keep: kill.add(f.index)
        if kill:
            bmesh.ops.delete(bm, geom=[bm.faces[i] for i in kill], context='FACES')
            bmesh.ops.delete(bm, geom=[e for e in bm.edges if not e.link_faces], context='EDGES')
            bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_edges], context='VERTS')
        bm.to_mesh(me); bm.free(); me.update()
        filled=fill_boundary_loops(obj, max_len=max_sides)
        t=topo(me); log.append(dict(it=it, killed=len(kill), filled=filled, **t))
        if verbose: print(log[-1])
        if not kill and not filled[0]: break
    return log

def components(me):
    bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table(); bm.verts.ensure_lookup_table()
    seen=set(); comps=[]
    for f in bm.faces:
        if f.index in seen: continue
        st=[f]; seen.add(f.index); cur=[f.index]
        while st:
            c=st.pop()
            for e in c.edges:
                for g in e.link_faces:
                    if g.index not in seen: seen.add(g.index); st.append(g); cur.append(g.index)
        comps.append(cur)
    out=[]
    for cur in comps:
        vs={v.index for i in cur for v in bm.faces[i].verts}
        pts=np.array([bm.verts[i].co[:] for i in vs])
        nb=sum(1 for i in cur for e in bm.faces[i].edges if len(e.link_faces)==1)
        out.append(dict(nf=len(cur),bnd=nb,c=pts.mean(0),mn=pts.min(0),mx=pts.max(0),faces=cur))
    bm.free()
    return out

def drop_open_flecks(obj, max_faces=10):
    me=obj.data
    cs=components(me)
    kill=[i for c in cs if c['bnd']>0 and c['nf']<=max_faces for i in c['faces']]
    bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
    bmesh.ops.delete(bm, geom=[bm.faces[i] for i in kill], context='FACES')
    bmesh.ops.delete(bm, geom=[e for e in bm.edges if not e.link_faces], context='EDGES')
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_edges], context='VERTS')
    bm.to_mesh(me); bm.free(); me.update()
    return len(kill)

def fill_boundary_loops(obj, max_len=12, grow_rounds=3):
    """Close simple boundary loops (every vertex valence 2) up to max_len edges with triangle fans whose chords are new edges.
    A loop that cannot be fanned without duplicating an existing edge is grown (its adjacent faces are removed) and retried.
    Face winding follows the adjacent face. Returns (filled loops, skipped loop sizes)."""
    me=obj.data
    bm=bmesh.new(); bm.from_mesh(me); bm.edges.ensure_lookup_table(); bm.verts.ensure_lookup_table(); bm.faces.ensure_lookup_table()
    import collections
    filled=0; skipped=[]; grown=0
    for rnd in range(4+grow_rounds):
        b=[e for e in bm.edges if e.is_valid and len(e.link_faces)==1]
        adj=collections.defaultdict(list)
        for e in b:
            adj[e.verts[0]].append(e.verts[1]); adj[e.verts[1]].append(e.verts[0])
        progress=False; skipped=[]; to_grow=[]
        # boundary graph components -> edge-disjoint simple cycles (handles pinched figure-8 loops)
        comp_seen=set(); cycles=[]
        for v0 in list(adj):
            if v0 in comp_seen or not v0.is_valid: continue
            st=[v0]; comp=[]; comp_seen.add(v0)
            while st:
                x=st.pop(); comp.append(x)
                for y in adj[x]:
                    if y not in comp_seen: comp_seen.add(y); st.append(y)
            found=set(); out=[]
            for start in comp:
                stack=[(start,[start])]
                while stack:
                    cur,path=stack.pop()
                    for nx in adj[cur]:
                        if nx==start and len(path)>=3:
                            key=frozenset(frozenset((a,b)) for a,b in zip(path,path[1:]+path[:1]))
                            if key not in found: found.add(key); out.append(list(path))
                        elif nx not in path and len(path)<max_len:
                            stack.append((nx,path+[nx]))
            out.sort(key=len)
            used=set()
            for cyc in out:
                es=[frozenset((a,b)) for a,b in zip(cyc,cyc[1:]+cyc[:1])]
                if any(e in used for e in es): continue
                used.update(es); cycles.append(cyc)
        covered={frozenset((a,b)) for cyc in cycles for a,b in zip(cyc,cyc[1:]+cyc[:1])}
        skipped=[1 for e in b if frozenset(e.verts) not in covered]
        for order in cycles:
            e0=bm.edges.get((order[0],order[1]))
            lp=[l for l in e0.link_loops][0]
            fwd = (lp.vert==order[0] and lp.link_loop_next.vert==order[1])
            ring=order[::-1] if fwd else order[:]
            n=len(ring); done=False
            for apex in range(n):
                tri=[(ring[apex],ring[(apex+k)%n],ring[(apex+k+1)%n]) for k in range(1,n-1)]
                chords=[(ring[apex],ring[(apex+k)%n]) for k in range(2,n-1)]
                if any(bm.edges.get(c) for c in chords): continue
                try:
                    for t in tri: bm.faces.new(t)
                    done=True; break
                except ValueError:
                    continue
            if done: filled+=1; progress=True
            else: to_grow.append(ring)
        if not progress and to_grow and grown<grow_rounds:
            kill=set()
            for ring in to_grow:
                for a,bv in zip(ring,ring[1:]+ring[:1]):
                    e=bm.edges.get((a,bv))
                    if e:
                        for f in e.link_faces: kill.add(f)
            if kill:
                bmesh.ops.delete(bm,geom=list(kill),context='FACES')
                bmesh.ops.delete(bm, geom=[e for e in bm.edges if not e.link_faces], context='EDGES')
                bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_edges], context='VERTS')
                grown+=1; progress=True
                bm.edges.ensure_lookup_table(); bm.verts.ensure_lookup_table(); bm.faces.ensure_lookup_table()
        elif not progress:
            skipped += [len(r) for r in to_grow]
            break
        bm.edges.ensure_lookup_table()
    bm.normal_update()
    bm.to_mesh(me); bm.free(); me.update()
    return filled, skipped, grown

def triangulate(obj):
    me=obj.data; bm=bmesh.new(); bm.from_mesh(me)
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts)>3])
    bm.to_mesh(me); bm.free(); me.update()


# ---------------- planar-cluster ("box") unwrap with deterministic shelf packing ----------------
def _arrays(me):
    nv=len(me.vertices); co=np.empty(nv*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
    fv=np.empty(len(me.polygons)*3,dtype=np.int64); me.polygons.foreach_get('vertices',fv); fv=fv.reshape(-1,3)
    return co,fv

def face_adjacency(fv):
    import collections
    ed=collections.defaultdict(list)
    for i,(a,b,c) in enumerate(fv):
        for u,v in ((a,b),(b,c),(c,a)):
            ed[(min(u,v),max(u,v))].append(i)
    nb=[[] for _ in range(len(fv))]
    for k,fs in ed.items():
        for x in fs:
            for y in fs:
                if x!=y: nb[x].append(y)
    return nb

AXES=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=np.float64)

def box_uv(obj, lab, pl, density_boost=None, gutter_px=10, size_px=1024, smooth_iters=5, min_comp=30, layer_name='UV_WP3', seed_axes=None):
    me=obj.data; co,fv=_arrays(me)
    sc=obj.matrix_world.to_scale()[0]
    P=co*sc
    n=np.cross(P[fv[:,1]]-P[fv[:,0]],P[fv[:,2]]-P[fv[:,0]]); area=np.linalg.norm(n,axis=1)/2; n/= (np.linalg.norm(n,axis=1,keepdims=True)+1e-12)
    cen=P[fv].mean(1)
    nb=face_adjacency(fv)
    dots=n@AXES.T
    ax=dots.argmax(1)
    for it in range(smooth_iters):
        new=ax.copy()
        for f in range(len(fv)):
            votes=np.zeros(6); votes[ax[f]]+=area[f]*1.0
            for g in nb[f]:
                if lab[g]==lab[f]: votes[ax[g]]+=area[g]
            c=votes.argmax()
            if dots[f,c]>0.25: new[f]=c
        ax=new
    key=lab*6+ax
    # connected components of equal key
    comp=np.full(len(fv),-1); comps=[]
    for s in range(len(fv)):
        if comp[s]>=0: continue
        st=[s]; comp[s]=len(comps); cur=[s]
        while st:
            f=st.pop()
            for g in nb[f]:
                if comp[g]<0 and key[g]==key[s]:
                    comp[g]=len(comps); st.append(g); cur.append(g)
        comps.append(cur)
    # merge tiny comps into the neighbouring comp sharing most edges (adopts its projection)
    changed=True; guard=0
    while changed and guard<6:
        changed=False; guard+=1
        sizes=np.array([len(c) for c in comps])
        for ci in np.argsort(sizes):
            cur=comps[ci]
            if not cur or len(cur)>=min_comp: continue
            cnt={}
            for f in cur:
                for g in nb[f]:
                    if comp[g]!=ci: cnt[comp[g]]=cnt.get(comp[g],0)+1
            if not cnt: continue
            tgt=max(cnt,key=cnt.get)
            for f in cur: comp[f]=tgt; key[f]=key[comps[tgt][0]]; ax[f]=ax[comps[tgt][0]]
            comps[tgt]=comps[tgt]+cur; comps[ci]=[]; changed=True
    islands=[c for c in comps if c]
    # per-island planar projection with PCA-aligned orientation
    isl=[]
    for c in islands:
        a=ax[c[0]]; axis=AXES[a]
        # basis perpendicular to axis
        up=np.array([0,0,1.0]) if abs(axis[2])<0.9 else np.array([0,1.0,0])
        e1=np.cross(up,axis); e1/=np.linalg.norm(e1); e2=np.cross(axis,e1)
        verts=np.unique(fv[c].ravel())
        q=np.stack([P[verts]@e1,P[verts]@e2],1)
        ctr=q.mean(0); u,s_,vt=np.linalg.svd(q-ctr,full_matrices=False)
        R=vt  # rows: principal axes
        isl.append(dict(faces=c,verts=verts,e1=e1,e2=e2,R=R,ctr=ctr,part=lab[c[0]],axis=a))
    return co,fv,P,isl,area,nb

def pack_islands(P,fv,isl,pl,density_boost=None,gutter_px=10,size_px=1024):
    """Shelf-pack oriented-bbox islands into the unit square at uniform texel density (boosts per part). Returns loop UVs (nf,3,2) and metrics."""
    density_boost=density_boost or {}
    # island local coords
    for it in isl:
        verts=it['verts']
        q=np.stack([P[verts]@it['e1'],P[verts]@it['e2']],1)
        qq=(q-it['ctr'])@it['R'].T
        mn=qq.min(0); mx=qq.max(0)
        it['mn']=mn; it['size']=mx-mn
        it['boost']=density_boost.get(pl[it['part']],1.0)
    g=gutter_px/size_px
    def attempt(scale):
        rects=[]
        for k,it in enumerate(isl):
            w=it['size'][0]*scale*it['boost']+g; h=it['size'][1]*scale*it['boost']+g
            rects.append((k,w,h))
        rects.sort(key=lambda r:-r[2])
        x=y=0; rowh=0; pos={}
        for k,w,h in rects:
            if x+w>1.0:
                x=0; y+=rowh; rowh=0
            pos[k]=(x,y,w,h); x+=w; rowh=max(rowh,h)
        return y+rowh, pos
    lo,hi=0.001,2.0
    for _ in range(40):
        mid=(lo+hi)/2
        used,pos=attempt(mid)
        if used<=1.0: lo=mid
        else: hi=mid
    used,pos=attempt(lo)
    scale=lo
    uvs=np.zeros((len(fv),3,2)); 
    vert_uv={}
    for k,it in enumerate(isl):
        x,y,w,h=pos[k]
        verts=it['verts']
        q=np.stack([P[verts]@it['e1'],P[verts]@it['e2']],1)
        qq=((q-it['ctr'])@it['R'].T-it['mn'])*scale*it['boost']
        qq[:,0]+=x+g/2; qq[:,1]+=y+g/2
        m={int(v):qq[i] for i,v in enumerate(verts)}
        for f in it['faces']:
            for j in range(3): uvs[f,j]=m[int(fv[f,j])]
    cover=sum(it['size'][0]*it['size'][1]*(scale*it['boost'])**2 for it in isl)
    return uvs, dict(scale=scale, rows_used=used, coverage=cover, islands=len(isl))

def write_uv(obj, uvs, layer_name='UV_WP3'):
    me=obj.data
    if layer_name in me.uv_layers: me.uv_layers.remove(me.uv_layers[layer_name])
    layer=me.uv_layers.new(name=layer_name)
    arr=np.zeros((len(me.loops),2))
    for p in me.polygons:
        for j,li in enumerate(p.loop_indices):
            arr[li]=uvs[p.index,j]
    layer.data.foreach_set('uv',arr.ravel())
    me.uv_layers.active=layer
    return layer_name

def geom_prep(obj, tol_world=0.0005, verbose=True):
    s=obj.matrix_world.to_scale()[0]
    log={'weld':weld(obj,tol_world/s)}
    log['manifold']=clean_manifold(obj,verbose=False)
    triangulate(obj)
    log['conflict_fix']=fix_conflict_faces(obj)
    log['settle']=settle(obj)
    log['outward_flips']=fix_component_outward(obj)
    log['topo']=topo(obj)
    return log

def export_bake_arrays(obj, old_layer, new_layer, labels, path):
    me=obj.data; s=obj.matrix_world.to_scale()[0]
    co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)*s
    def tri_uv(name):
        l=me.uv_layers[name]; a=np.empty(len(me.loops)*2); l.data.foreach_get('uv',a); a=a.reshape(-1,2)
        return np.array([a[list(p.loop_indices)] for p in me.polygons])
    fv=np.array([list(p.vertices) for p in me.polygons])
    np.savez_compressed(path, pos=co[fv], uv_old=tri_uv(old_layer), uv_new=tri_uv(new_layer), labels=np.asarray(labels), fv=fv)
    return path

def blender_pack(obj, layer_name, margin=0.006, shape='CONCAVE', rotate=True):
    me=obj.data
    me.uv_layers.active=me.uv_layers[layer_name]
    bpy.context.view_layer.objects.active=obj
    for o in bpy.context.selected_objects: o.select_set(False)
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bm=bmesh.from_edit_mesh(me)
    for f in bm.faces: f.select_set(True)
    bmesh.update_edit_mesh(me)
    ts=bpy.context.scene.tool_settings; ts.use_uv_select_sync=False
    bpy.ops.uv.select_all(action='SELECT')
    bpy.ops.uv.pack_islands(udim_source='CLOSEST_UDIM', rotate=rotate, margin_method='FRACTION', margin=margin, shape_method=shape, scale=True)
    bpy.ops.object.mode_set(mode='OBJECT')


def clean_manifold(obj, tols_world=(0.002,0.005,0.01,0.02), max_sides=8, verbose=True):
    """Iterate until the welded mesh has no boundary and no >2-face edges: sliver-face drop, boundary-vertex merge (growing tolerance), degenerate cleanup, loop fill."""
    me=obj.data; s=obj.matrix_world.to_scale()[0]; log=[]
    for tol in list(tols_world)+[tols_world[-1]]*2:
        # 1 non-manifold edges
        fix_manifold(obj,max_sides=max_sides,verbose=False)
        bm=bmesh.new(); bm.from_mesh(me)
        bverts=[v for v in bm.verts if any(len(e.link_faces)==1 for e in v.link_edges)]
        if bverts:
            bmesh.ops.remove_doubles(bm, verts=bverts, dist=tol/s)
            bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-9)
        # drop zero-area faces and duplicate faces
        seen=set(); kill=[]
        for f in bm.faces:
            k=tuple(sorted(v.index for v in f.verts))
            if f.calc_area()<1e-12 or k in seen or len(set(k))<3: kill.append(f)
            seen.add(k)
        if kill: bmesh.ops.delete(bm,geom=kill,context='FACES')
        bmesh.ops.delete(bm, geom=[e for e in bm.edges if not e.link_faces], context='EDGES')
        bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_edges], context='VERTS')
        bm.to_mesh(me); bm.free(); me.update()
        drop_open_flecks(obj)
        fill_boundary_loops(obj, max_len=max_sides)
        t=topo(me); log.append((tol,t['boundary'],t['nonmanifold'],t['faces']))
        if verbose: print(log[-1])
        if t['boundary']==0 and t['nonmanifold']==0: break
    return log


def fix_winding(obj):
    """Make every closed component consistently outward-facing (bmesh recalc), re-seating custom corner normals only on the flipped faces."""
    me = obj.data
    old_n = np.empty(len(me.loops) * 3); me.corner_normals.foreach_get('vector', old_n) if hasattr(me.corner_normals, 'foreach_get') else None
    try:
        cn = np.array([tuple(n.vector) for n in me.corner_normals]).reshape(-1, 3)
    except Exception:
        cn = None
    fn_before = np.array([tuple(p.normal) for p in me.polygons])
    bm = bmesh.new(); bm.from_mesh(me)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free(); me.update()
    fn_after = np.array([tuple(p.normal) for p in me.polygons])
    flipped = np.where((fn_before * fn_after).sum(1) < 0)[0]
    if cn is not None and len(flipped):
        arr = cn.copy()
        for fi in flipped:
            p = me.polygons[int(fi)]
            for li in p.loop_indices: arr[li] = fn_after[fi]
        me.normals_split_custom_set(arr.tolist())
    return int(len(flipped))


def orientation_conflicts(me):
    bm=bmesh.new(); bm.from_mesh(me); n=0
    for e in bm.edges:
        if len(e.link_faces)==2:
            l1,l2=e.link_loops
            if l1.vert==l2.vert: n+=1
    bm.free(); return n

def fix_conflict_faces(obj, rounds=6):
    """Flip faces whose majority of manifold edges disagree with their neighbours' winding (isolated mis-wound slivers)."""
    me=obj.data; log=[]
    for r in range(rounds):
        bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
        flip=set()
        for f in bm.faces:
            bad=0; tot=0
            for l in f.loops:
                e=l.edge
                if len(e.link_faces)==2:
                    tot+=1
                    o=[x for x in e.link_loops if x!=l][0]
                    if o.vert==l.vert: bad+=1
            if tot and bad*2>tot: flip.add(f)
        log.append(len(flip))
        if not flip: bm.free(); break
        bmesh.ops.reverse_faces(bm, faces=list(flip))
        bm.to_mesh(me); bm.free(); me.update()
    return log, orientation_conflicts(me)


def fix_component_outward(obj):
    """Flip an entire closed component when its signed volume is negative (inside-out)."""
    me=obj.data; bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
    seen=set(); flipped=[]
    for f in bm.faces:
        if f.index in seen: continue
        st=[f]; seen.add(f.index); comp=[f]
        while st:
            c=st.pop()
            for e in c.edges:
                for g in e.link_faces:
                    if g.index not in seen: seen.add(g.index); st.append(g); comp.append(g)
        vol=0.0
        for t in comp:
            a,b,c3=[v.co for v in t.verts]; vol+=a.dot(b.cross(c3))/6.0
        if vol<0:
            bmesh.ops.reverse_faces(bm,faces=comp); flipped.append(len(comp))
    bm.to_mesh(me); bm.free(); me.update()
    return flipped


def snap_wrist_weights(obj, snap=0.75):
    """Deliberate clean-up of existing provider weights at the wrist: hand-dominated vertices keep only Hand/ForeArm, forearm-dominated vertices keep only ForeArm/Hand/Arm; a vertex with >= snap on its top bone takes 1.0. Weights are never created from nothing."""
    me = obj.data; names = {g.index: g.name for g in obj.vertex_groups}
    changed = 0
    for side in ('Left', 'Right'):
        hand, fore, uparm = f'{side}Hand', f'{side}ForeArm', f'{side}Arm'
        gi = {n: obj.vertex_groups.get(n) for n in (hand, fore, uparm)}
        if not gi[hand] or not gi[fore]: continue
        for v in me.vertices:
            w = {names[g.group]: g.weight for g in v.groups}
            if not w: continue
            top = max(w, key=w.get)
            if top == hand: keep = {hand, fore}
            elif top == fore: keep = {fore, hand, uparm}
            else: continue
            nw = {k: val for k, val in w.items() if k in keep}
            tot = sum(nw.values())
            if tot <= 0: continue
            nw = {k: val / tot for k, val in nw.items()}
            tb = max(nw, key=nw.get)
            if nw[tb] >= snap: nw = {tb: 1.0}
            if nw != w:
                for k in w:
                    if k not in nw: obj.vertex_groups[k].remove([v.index])
                for k, val in nw.items(): obj.vertex_groups[k].add([v.index], val, 'REPLACE')
                changed += 1
    return changed


def pos_conflicts(me, nd=6, return_faces=False):
    """Orientation conflicts measured the way the adapter does: edges identified by exact positions, regardless of vertex identity."""
    co = np.empty(len(me.vertices) * 3); me.vertices.foreach_get('co', co); co = co.reshape(-1, 3)
    key = {}
    pid = np.empty(len(me.vertices), dtype=np.int64)
    for i, c in enumerate(np.round(co, nd)):
        pid[i] = key.setdefault(tuple(c), len(key))
    edges = {}
    for p in me.polygons:
        v = [pid[x] for x in p.vertices]
        for a, b in zip(v, v[1:] + v[:1]):
            edges.setdefault((min(a, b), max(a, b)), []).append((p.index, a < b))
    bad = []; multi = 0
    for e, fs in edges.items():
        if len(fs) == 2:
            if fs[0][1] == fs[1][1]: bad.append((fs[0][0], fs[1][0]))
        elif len(fs) > 2: multi += 1
    if return_faces: return bad, multi
    return len(bad), multi

def fix_pos_conflicts(obj, rounds=8):
    me = obj.data; log = []
    for r in range(rounds):
        bad, multi = pos_conflicts(me, return_faces=True)
        log.append((len(bad), multi))
        if not bad: break
        cnt = {}
        for a, b in bad:
            cnt[a] = cnt.get(a, 0) + 1; cnt[b] = cnt.get(b, 0) + 1
        flip = [f for f, n in cnt.items() if n >= 2] or [min(cnt, key=lambda f: me.polygons[f].area)]
        bm = bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
        bmesh.ops.reverse_faces(bm, faces=[bm.faces[f] for f in flip]); bm.to_mesh(me); bm.free(); me.update()
    return log


def resolve_conflicts_by_cut(obj, rounds=4):
    """For stubborn same-direction edges: delete the smaller face of each pair, refill the hole with correctly wound triangles."""
    me = obj.data; log = []
    for r in range(rounds):
        bad, multi = pos_conflicts(me, return_faces=True)
        log.append(len(bad))
        if not bad: break
        kill = {min(a, b, key=lambda f: me.polygons[f].area) if False else (a if me.polygons[a].area < me.polygons[b].area else b) for a, b in bad}
        bm = bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table()
        bmesh.ops.delete(bm, geom=[bm.faces[f] for f in kill], context='FACES')
        bmesh.ops.delete(bm, geom=[e for e in bm.edges if not e.link_faces], context='EDGES')
        bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_edges], context='VERTS')
        bm.to_mesh(me); bm.free(); me.update()
        fill_boundary_loops(obj, max_len=16)
    log.append(pos_conflicts(me)[0])
    return log


def collapse_conflict_edges(obj, rounds=6):
    """Collapse each orientation-conflict edge (merge its two vertices, drop the two degenerate faces); keeps the surface closed."""
    me = obj.data; log = []
    for r in range(rounds):
        bm = bmesh.new(); bm.from_mesh(me); bm.edges.ensure_lookup_table()
        pairs = []
        for e in bm.edges:
            if len(e.link_faces) == 2:
                l1, l2 = e.link_loops
                if l1.vert == l2.vert: pairs.append(e)
        log.append(len(pairs))
        if not pairs: bm.free(); break
        verts = {}
        for e in pairs[:1]:
            bmesh.ops.pointmerge(bm, verts=list(e.verts), merge_co=(e.verts[0].co + e.verts[1].co) / 2)
        bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-9)
        bm.to_mesh(me); bm.free(); me.update()
    return log, orientation_conflicts(me)


def settle(obj, rounds=14):
    """Alternate non-manifold repair, mis-wound face flips, and conflict-edge collapse until the welded mesh is closed, manifold and orientable."""
    me = obj.data; log = []
    for r in range(rounds):
        t = topo(me); pc, multi = pos_conflicts(me)
        log.append((t['boundary'], t['nonmanifold'], pc, multi))
        if t['boundary'] == 0 and t['nonmanifold'] == 0 and pc == 0 and multi == 0: break
        if t['nonmanifold'] or t['boundary'] or multi:
            fix_manifold(obj, verbose=False)
            fill_boundary_loops(obj, max_len=24)
        fix_conflict_faces(obj)
        if pos_conflicts(me)[0]:
            collapse_conflict_edges(obj, rounds=2)
    return log
