import sys, json; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, stretch as S; importlib.reload(uf); importlib.reload(S)
from uf import *
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
arm.animation_data_create(); arm.animation_data.action=None
for pb in arm.pose.bones: pb.rotation_mode='QUATERNION'; pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
adj=S.vertex_adjacency(body); vg={g.index:g.name for g in body.vertex_groups}
poses=CFG['poses']; thr=CFG.get('thr',0.3); rings=CFG.get('rings',2); lam=CFG.get('lam',0.5); iters=CFG.get('iters',3)
def measure():
    res=[]; E=None
    for act,fr in poses:
        a=bpy.data.actions[CFG['prefix']+'_'+act]; g,E=S.growth(body,arm,a,fr); res.append((act,fr,int((g>thr).sum()),g))
    return res,E
log=[]
res,E=measure(); log.append([(a,f,n) for a,f,n,_ in res])
for rd in range(CFG.get('rounds',8)):
    targets=CFG.get('targets',{})
    bad=set()
    for act,fr,n,g in res:
        lim=targets.get(f'{act}{fr}',CFG.get('target',40))
        if n>lim:
            idx=np.nonzero(g>CFG.get('region_thr',0.15))[0]
            for i in idx: bad.update((int(E[i,0]),int(E[i,1])))
    if not bad: break
    region=S.ring_expand(adj,bad,rings)
    gnames=sorted({vg[g.group] for v in region for g in body.data.vertices[v].groups})
    S.smooth_weights(body,region,gnames,adj,iters=iters,lam=lam)
    res,E=measure(); log.append([(a,f,n) for a,f,n,_ in res]+[('region',len(region))])
cnt={}
for v in body.data.vertices:
    k=len([g for g in v.groups if g.weight>1e-4]); cnt[k]=cnt.get(k,0)+1
uf.save_ck(CFG['job'],CFG['out'])
result={'log':log,'influences':cnt}
