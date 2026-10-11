import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, acttools as A; importlib.reload(z); importlib.reload(A)
import bpy
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
if CFG.get('open',True): bpy.ops.wm.open_mainfile(filepath=J+CFG['blend'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
res=A.audit_all(arm,body,CFG['job'])
result={k:{kk:vv for kk,vv in v.items() if kk in ('frames','over','ang_over','ang_max','local_over','local_max','local_worst','worst','seam','flips')} for k,v in res.items()}
