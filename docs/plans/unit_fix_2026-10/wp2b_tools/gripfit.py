import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z; importlib.reload(z)
import bpy, numpy as np
from mathutils import Matrix, Vector
bpy.ops.wm.open_mainfile(filepath=CFG['blend'])
arm=bpy.data.objects['Armature.001']
main=CFG['main']; off=CFG['off']
res={}
rest={}
for b in (main,off):
    bone=arm.data.bones[b]; rest[b]=dict(head=list((arm.matrix_world@bone.head_local)), tail=list((arm.matrix_world@bone.tail_local)), x=list((arm.matrix_world.to_3x3()@bone.matrix_local.to_3x3()).col[0]), y=list((arm.matrix_world.to_3x3()@bone.matrix_local.to_3x3()).col[1]), z=list((arm.matrix_world.to_3x3()@bone.matrix_local.to_3x3()).col[2]))
res['rest']=rest
for r in CFG['roles']:
    act=bpy.data.actions[f"{CFG['prefix']}_{r}"]; z.set_action(arm,act)
    f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); dirs=[];gaps=[]
    for f in range(f0,f1+1,2):
        bpy.context.scene.frame_set(f)
        M=arm.matrix_world@arm.pose.bones[main].matrix
        pm=M.translation; po=(arm.matrix_world@arm.pose.bones[off].matrix).translation
        d=M.to_3x3().inverted()@(po-pm); gaps.append(d.length); dirs.append(d.normalized())
    D=np.array([list(v) for v in dirs]); m=D.mean(0); 
    res[r]=dict(mean_dir_local=[round(float(x),2) for x in m/np.linalg.norm(m)], dir_spread=round(float(np.degrees(np.arccos(np.clip(D@(m/np.linalg.norm(m)),-1,1))).mean()),1), gap=[round(min(gaps),2),round(float(np.mean(gaps)),2),round(max(gaps),2)])
result=res
