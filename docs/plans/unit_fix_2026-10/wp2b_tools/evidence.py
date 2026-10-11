# Lab: per-frame contact/floor/motion evidence of the final checkpoint -> job validation/wp2b_contact_evidence.json
import sys, json; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy, numpy as np
from mathutils import Vector
R=r"<mod root>/"
JR=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/"
bpy.ops.wm.open_mainfile(filepath=JR+"blender/checkpoints/"+CFG['blend'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); arm.animation_data.action=None; H.set_rest(arm,True)
offs={}
for b in ('LeftHand','RightHand'): offs[b]=list(H.hand_centroid(arm,body,b)[1])
H.set_rest(arm,False)
def palm(b): return H.head(arm,b)+H.rot3(arm,b)@Vector(offs[b])
items=CFG['items']  # [{item, main, off?, axis_local, shaft?}]
out={'checkpoint':CFG['blend'],'items':[i['item'] for i in items],'roles':{}}
for role in ["idle","move","attack","defend","support_attack","retreat","training","death"]:
    act=bpy.data.actions[f"{CFG['job']}_{role}"]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
    a=A.audit(arm,body,act,role)
    row={'frames':[f0,f1],'world_step_over':a['over'],'local_over':a['local_over'],'local_max_deg':a['local_max'],'seam':a['seam'],'items':{}}
    for it in items:
        obj=bpy.data.objects['ITEM_'+it['item']]; low=[]; d=[]
        al=Vector(it['axis_local']).normalized()
        for f in range(f0,f1+1):
            bpy.context.scene.frame_set(f); dg=bpy.context.evaluated_depsgraph_get(); eo=obj.evaluated_get(dg); me=eo.to_mesh()
            co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3); M=np.array(obj.matrix_world); low.append(float((co@M[:3,:3].T+M[:3,3])[:,2].min())); eo.to_mesh_clear()
            if it.get('off'):
                Pm=palm(it['main']); Po=palm(it['off']); ac=(H.rot3(arm,it['main'])@al).normalized(); t=min(max((Po-Pm).dot(ac),-it['shaft'][0]),it['shaft'][1]); d.append(round((Pm+ac*t-Po).length,3))
        r={'floor_min_z':round(min(low),3),'frames_below_floor':sum(1 for x in low if x<0)}
        if d: r['off_hand_to_shaft']={'max':max(d),'mean':round(float(np.mean(d)),3),'per_frame':d}
        row['items'][it['item']]=r
    out['roles'][role]=row
import os
os.makedirs(JR+'validation',exist_ok=True)
json.dump(out,open(JR+'validation/wp2b_contact_evidence.json','w'),indent=1)
result={k:{'items':{i:{x:y for x,y in v.items() if x!='per_frame'} if isinstance(v,dict) else v for i,v in r['items'].items()}} for k,r in out['roles'].items()}
