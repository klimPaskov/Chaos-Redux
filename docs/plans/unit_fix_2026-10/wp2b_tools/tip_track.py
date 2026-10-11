# Lab: world speed of an item's head tip per frame; reports speed peaks (local maxima above a threshold) as candidate swing/impact frames. CFG: job, blend, item, tip_axis_sign, roles
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z; importlib.reload(z)
import bpy, numpy as np
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['blend'])
arm=bpy.data.objects['Armature.001']; it=bpy.data.objects[CFG['item']]
me=it.data
co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
# head tip = the vertex farthest from the grip along the item axis in the rest pose, picked per end (cfg end: 'far' = max distance from centroid)
arm.animation_data_create(); arm.animation_data.action=None; arm.data.pose_position='REST'; bpy.context.view_layer.update()
M=np.array(it.matrix_world); w=co@M[:3,:3].T+M[:3,3]
cen=w.mean(0); d=np.linalg.norm(w-cen,axis=1)
ends=np.argsort(-d)[:50]
# choose the end cluster nearest to the item's head side: cfg tip_dir (world rest direction) 
tdir=np.array(CFG['tip_dir_world']); k=ends[np.argmax((w[ends]-cen)@tdir)]
arm.data.pose_position='POSE'
res={}
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['job']}_{role}"]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
    P=[]
    for f in range(f0,f1+1):
        bpy.context.scene.frame_set(f); dg=bpy.context.evaluated_depsgraph_get(); eo=it.evaluated_get(dg); m2=eo.to_mesh()
        v=m2.vertices[k].co; P.append(np.array(eo.matrix_world@v)); eo.to_mesh_clear()
    P=np.array(P); sp=np.linalg.norm(np.diff(P,axis=0),axis=1)
    peaks=[(f0+i+1,round(float(sp[i]),2)) for i in range(1,len(sp)-1) if sp[i]>=sp[i-1] and sp[i]>=sp[i+1] and sp[i]>CFG.get('thr',0.35)]
    fwd=P[:,1]
    res[role]=dict(frames=[f0,f1],peaks=peaks[:10],speed_max=round(float(sp.max()),2),y_min_frame=int(f0+np.argmin(fwd)),y_range=[round(float(fwd.min()),2),round(float(fwd.max()),2)])
result=res
