# Lab: measure per-frame lowest point of each item and the body (world z), and item-vs-body clearance is reviewed visually.
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z; importlib.reload(z)
import bpy, numpy as np
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
if CFG.get('open',True): bpy.ops.wm.open_mainfile(filepath=J+CFG['blend'])
arm=bpy.data.objects['Armature.001']; objs=[bpy.data.objects[n] for n in CFG['objs']]
out={}
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['job']}_{role}"]; z.set_action(arm,act)
    f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); rows={o.name:[] for o in objs}
    for f in range(f0,f1+1):
        bpy.context.scene.frame_set(f); dg=bpy.context.evaluated_depsgraph_get()
        for o in objs:
            eo=o.evaluated_get(dg); me=eo.to_mesh(); co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
            M=np.array(o.matrix_world); rows[o.name].append(float((co@M[:3,:3].T+M[:3,3])[:,2].min())); eo.to_mesh_clear()
    out[role]={k:dict(min=round(min(v),3),below0=[f0+i for i,x in enumerate(v) if x<0.0][:12],n_below=sum(1 for x in v if x<0.0)) for k,v in rows.items()}
result=out
