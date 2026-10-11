import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, tentacles as TT, fingers as F, stretch as S; importlib.reload(uf); importlib.reload(F); importlib.reload(S); importlib.reload(TT)
from uf import *
import holdtools as H
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); saved=arm.animation_data.action; arm.animation_data.action=None
for pb in arm.pose.bones: pb.rotation_mode='QUATERNION'; pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
fm=TT.flesh_mask(body,R+CFG['diffuse']); tube=TT.tube_vertices(body,fm,CFG.get('tmax',6.0))
T=TT.tube_graph(body,tube,CFG.get('minsize',60)); T=TT.bundles(T,CFG.get('k',8)); ch=TT.bundle_chains(T)
names,parents=TT.create_chain_bones(arm,body,T,ch)
n=TT.chain_weights(body,arm,T,ch,names)
from collections import Counter
inf=Counter(len([g for g in v.groups if g.weight>1e-4]) for v in body.data.vertices)
arm.animation_data.action=saved
uf.save_ck(CFG['job'],CFG['out'])
result={'bones':len(arm.data.bones),'chains':{str(j):names[j] for j in names},'parents':parents,'verts':n,'influences':dict(inf),'sizes':[c['n'] if c else 0 for c in ch]}
