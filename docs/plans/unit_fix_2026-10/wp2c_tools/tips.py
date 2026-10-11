import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import uf, regrip as RG
from uf import *
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; it=bpy.data.objects[CFG['item']]
arm.animation_data_create(); arm.animation_data.action=None; arm.data.pose_position='REST'; bpy.context.view_layer.update()
w=RG.item_world(it); mu=w.mean(0); u,s,vt=np.linalg.svd(w-mu,full_matrices=False); a=vt[0]; t=(w-mu)@a
ends={'pos':int(np.argmax(t)),'neg':int(np.argmin(t))}
arm.data.pose_position='POSE'; out={}
for role in CFG['roles']:
    act=bpy.data.actions[CFG['job']+'_'+role]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); res={}
    for nm,k in ends.items():
        P=[]
        for f in range(f0,f1+1):
            bpy.context.scene.frame_set(f); dg=bpy.context.evaluated_depsgraph_get(); eo=it.evaluated_get(dg); me=eo.to_mesh(); P.append(np.array(eo.matrix_world@me.vertices[k].co)); eo.to_mesh_clear()
        P=np.array(P); sp=np.linalg.norm(np.diff(P,axis=0),axis=1)
        pk=[(round((f0+i+1-1)/30.0,2),round(float(sp[i]),2)) for i in range(1,len(sp)-1) if sp[i]>=sp[i-1] and sp[i]>=sp[i+1] and sp[i]>CFG.get('thr',0.35)]
        res[nm]=pk[:8]
    out[role]=res
result=out
