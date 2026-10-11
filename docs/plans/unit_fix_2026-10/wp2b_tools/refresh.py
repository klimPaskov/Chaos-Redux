# Lab: final off-hand contact refresh. For every frame the off arm is reached onto the shaft point nearest its current palm (projection along the item axis, clamped), then keys are written.
# CFG: job, src, out, prefix, roles, main, off, upper_off, fore_off, axis_local, s_min, s_max
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy, numpy as np
from mathutils import Vector
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
main,off=CFG['main'],CFG['off']; al=Vector(CFG['axis_local']).normalized()
arm.animation_data_create(); arm.animation_data.action=None; H.set_rest(arm,True)
pm_off=list(H.hand_centroid(arm,body,main)[1]); po_off=list(H.hand_centroid(arm,body,off)[1]); H.set_rest(arm,False)
def palm(b,o): return H.head(arm,b)+H.rot3(arm,b)@Vector(o)
out={}
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); worst=[]
    for f in range(f0,f1+1):
        bpy.context.scene.frame_set(f)
        Pm=palm(main,pm_off); Po=palm(off,po_off); ac=(H.rot3(arm,main)@al).normalized()
        s=min(max((Po-Pm).dot(ac),CFG['s_min']),CFG['s_max'])
        r=H.solve_arm(arm,CFG['upper_off'],CFG['fore_off'],off,Pm+ac*s,po_off,iters=6); worst.append(r)
        for n in (CFG['upper_off'],CFG['fore_off']): arm.pose.bones[n].keyframe_insert('rotation_quaternion',frame=f)
    A.normalize_signs(act); a=A.audit(arm,body,act,role)
    out[role]=dict(reach_resid_max=round(max(worst),3),over=a['over'],local_over=a['local_over'],ang_max=a['ang_max'],local_max=a['local_max'],seam=a['seam'],local_seam=a['local_seam'][0])
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=out
