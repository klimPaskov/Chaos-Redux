import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, uvtools as U; importlib.reload(U)
import bpy
J=r"<mod root>/docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
res={}
for n in CFG['items']:
    o=bpy.data.objects[n]
    before=U.topo(o)
    log=U.geom_prep(o,tol_world=CFG.get('tol',0.002))
    import bmesh
    me=o.data; bm=bmesh.new(); bm.from_mesh(me); bm.faces.ensure_lookup_table(); seen=set(); comps=[]
    for f in bm.faces:
        if f.index in seen: continue
        st=[f]; seen.add(f.index); cur=[f]
        while st:
            c=st.pop()
            for e in c.edges:
                for g in e.link_faces:
                    if g.index not in seen: seen.add(g.index); st.append(g); cur.append(g)
        comps.append(cur)
    drop=[f for c in comps if len(c)<40 for f in c]
    if drop: bmesh.ops.delete(bm,geom=drop,context='FACES')
    bm.to_mesh(me); bm.free(); me.update()
    res[n]=dict(before=before,after=U.topo(o),dropped_faces=len(drop),settle=log['settle'][-1])
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=res
