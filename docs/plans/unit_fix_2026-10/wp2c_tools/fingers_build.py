import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, fingers as F; importlib.reload(uf); importlib.reload(F)
from uf import *
import holdtools as H
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); saved=arm.animation_data.action; arm.animation_data.action=None; H.set_rest(arm,True)
rep={}
for side in ('Right','Left'):
    A=F.analyse(arm,body,side); A=F.segment(A); ch=F.build_chains(A); W=F.weights_for(A,ch)
    names=F.create_bones(arm,A,ch,side); F.apply_weights(body,A,W,side)
    rep[side]=dict(bones=names,N=[round(float(x),2) for x in A['N']],D=[round(float(x),2) for x in A['D']],
        curl={nm:[round(float(x),2) for x in c['curl']] for nm,c in ch.items()},tips={nm:[round(float(x),2) for x in c['pts'][-1]] for nm,c in ch.items()})
H.set_rest(arm,False); arm.animation_data.action=saved
# influence stats
from collections import Counter
cnt=Counter(len([g for g in v.groups if g.weight>1e-4]) for v in body.data.vertices); rep['influences']=dict(cnt)
rep['bone_count']=len(arm.data.bones)
uf.save_ck(CFG['job'],CFG['out'])
result=rep
