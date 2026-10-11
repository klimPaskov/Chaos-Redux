# Lab: after the hold pass, smooth any remaining over-limit joint steps and re-measure contact/floor. CFG: job, src, out, prefix, items:[{item, main, off, axis_local, pm_off?}], roles
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy, numpy as np
from mathutils import Vector
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); arm.animation_data.action=None; H.set_rest(arm,True)
offs={}
for it in CFG['items']:
    for b in (it['main'],it.get('off')):
        if b and b not in offs: offs[b]=list(H.hand_centroid(arm,body,b)[1])
H.set_rest(arm,False)
def palm(b): return H.head(arm,b)+H.rot3(arm,b)@Vector(offs[b])
out={}
for role,(fa,fb,nt) in CFG.get('trim',{}).items():
    A.trim_scale(bpy.data.actions[f"{CFG['prefix']}_{role}"],fa,fb,nt)
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]
    a0=A.audit(arm,body,act,role); hist=None
    if a0['over'] or a0['ang_over']:
        hist=A.deglitch2(arm,body,act,role,rounds=12)
    A.normalize_signs(act)
    a1=A.audit(arm,body,act,role)
    z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
    row=dict(before=(a0['over'],a0['ang_over']),after=(a1['over'],a1['ang_over'],a1['ang_max']),seam=a1['seam'])
    for it in CFG['items']:
        if not it.get('off'): continue
        al=Vector(it['axis_local']).normalized(); d=[]
        for f in range(f0,f1+1):
            bpy.context.scene.frame_set(f); Pm=palm(it['main']); Po=palm(it['off']); ac=(H.rot3(arm,it['main'])@al).normalized()
            t=min(max((Po-Pm).dot(ac),-it['shaft'][0]),it['shaft'][1]); d.append((Pm+ac*t-Po).length)
        row['contact_'+it['item']]=(round(max(d),3),round(float(np.mean(d)),3))
    out[role]=row
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=out
