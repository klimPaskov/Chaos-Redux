import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, stretch as S; importlib.reload(uf); importlib.reload(S)
from uf import *
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); arm.animation_data.action=None; arm.data.pose_position='POSE'
for pb in arm.pose.bones: pb.rotation_mode='QUATERNION'; pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
out={}
for a in bpy.data.actions:
    if not a.name.startswith(CFG.get('prefix',CFG['job'])+'_') or '_ungrounded' in a.name or a.name.startswith('provider'): continue
    f0,f1=int(a.frame_range[0]),int(a.frame_range[1]); rows=[]
    for f in range(f0,f1+1,CFG.get('step',3)):
        g,E=S.growth(body,arm,a,f); rows.append((f,int((g>0.3).sum()),round(float(g.max()),2)))
    top=sorted(rows,key=lambda r:-r[1])[:3]
    out[a.name.replace(CFG.get('prefix',CFG['job'])+'_','')]=top
result=out
