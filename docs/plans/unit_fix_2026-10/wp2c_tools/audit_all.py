import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import uf
from uf import *
import acttools as A
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects[CFG.get('body','char1.001')]
for _r in ('attack','defend','support_attack','training','death'): A.LIM[_r]=0.409; A.ANG[_r]=29.9
for _r in ('move','retreat'): A.LIM[_r]=0.356; A.ANG[_r]=24.8
A.LIM['idle']=0.099; A.ANG['idle']=9.9
out={}
for role in CFG['roles']:
    act=bpy.data.actions[CFG.get('prefix',CFG['job'])+'_'+role]; a=A.audit(arm,body,act,role)
    out[role]=dict(over=a['over'],worst=a['worst'][:2],ang_over=a['ang_over'],local_over=a['local_over'],local_max=a['local_max'],seam=a['seam'],local_seam=a['local_seam'])
result=out
