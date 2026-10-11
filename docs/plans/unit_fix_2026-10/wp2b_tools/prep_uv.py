# Lab script. Requires CFG = dict(job=..., src=checkpoint rel, body='char1.001', out='wp3_01_geom_uv.blend', npz=path, boost={...}, min_comp=120)
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, uvtools as U; importlib.reload(U)
import bpy, numpy as np, json
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
w=bpy.data.objects[CFG.get('body','char1.001')]; me=w.data
log={'before':U.topo(w)}
log.update(U.geom_prep(w))
lab,pl=U.face_parts(w, CFG.get('parts')); lab,moved=U.reassign_small(me,lab)
if CFG.get('tentacle_max'):
    cs=U.components(me); pl=list(pl); pl.append('tentacle'); tid=len(pl)-1; n_t=0
    for c in cs:
        if c['nf']<CFG['tentacle_max']:
            for f in c['faces']: lab[f]=tid
            n_t+=len(c['faces'])
    log['tentacle_faces']=n_t
if CFG.get('tentacle_head_r'):
    import numpy as _np
    arm_=[o for o in bpy.data.objects if o.type=='ARMATURE' and o.name=='Armature.001'][0]
    hc=_np.array(arm_.matrix_world@arm_.data.bones['Head'].head_local)
    sc_=w.matrix_world.to_scale()[0]
    cof=_np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',cof); cof=cof.reshape(-1,3)*sc_
    fvv=_np.array([list(p.vertices) for p in me.polygons]); cen=cof[fvv].mean(1)
    dist=_np.linalg.norm(cen-hc,axis=1)
    if 'tentacle' not in pl: pl=list(pl); pl.append('tentacle')
    tid=pl.index('tentacle'); m=((lab==pl.index('head'))|(lab==pl.index('torso'))|(lab==pl.index('l_arm'))|(lab==pl.index('r_arm')))&(dist>CFG['tentacle_head_r'])&(cen[:,2]>CFG.get('tentacle_zmin',5.0))
    lab[m]=tid; log['tentacle_faces_head']=int(m.sum()); log['head_center']=hc.tolist()
co,fv,P,isl,area,nb=U.box_uv(w,lab,pl,min_comp=CFG.get('min_comp',120))
uvs,m=U.pack_islands(P,fv,isl,pl,density_boost=CFG.get('boost',{}))
U.write_uv(w,uvs)
U.blender_pack(w,'UV_WP3',margin=CFG.get('margin',0.008))
log['uv']=dict(islands=len(isl),pack=str(m))
U.export_bake_arrays(w,'UVMap','UV_WP3',lab,CFG['npz'])
log['parts']=pl
bpy.ops.wm.save_as_mainfile(filepath=J+"blender/checkpoints/"+CFG['out'])
result=log
