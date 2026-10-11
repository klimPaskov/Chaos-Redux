# Lab: final loop closure. For looped roles, ease the last n frames onto the first-frame pose until every local bone seam is below the gate (3 deg), then report contacts.
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
out={}
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]; log=[]
    for n in CFG.get('ns',[8,12,16,22]):
        sm=A.local_seam(act); log.append(sm)
        if sm[0]<CFG.get('seam_deg',2.0): break
        A.ease_seam(act,n)
    A.normalize_signs(act); a=A.audit(arm,body,act,role)
    out[role]=dict(seam_log=log,final=a['local_seam'],over=a['over'],local_over=a['local_over'],ang_max=a['ang_max'],world_seam=a['seam'])
gr={}
for role in CFG.get('ground_roles',[]):
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]; gr[role]=A.ground_in_place(arm,body,act); A.normalize_signs(act)
out['_grounded']=gr
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=out
