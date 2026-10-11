"""Lab script: apply authored ops, then the gate pass (sign continuity, deglitch to the gate limits, loop seal, floor) to every role.
CFG: job, src, out, prefix, roles, loops, ops:[{role,op,...}], skip_generic:[roles], body, floor_roles"""
import sys, json, time; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, regrip as RG; importlib.reload(uf); importlib.reload(RG)
from uf import *
import acttools as A, holdtools as H
t0=time.time()
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects[CFG.get('body','char1.001')]
for _r in ('attack','defend','support_attack','training','death'): A.LIM[_r]=0.409; A.ANG[_r]=29.9
for _r in ('move','retreat'): A.LIM[_r]=0.356; A.ANG[_r]=24.8
A.LIM['idle']=0.099; A.ANG['idle']=9.9
P=CFG['prefix']; loops=set(CFG['loops'])
def act_of(role): return bpy.data.actions[P+'_'+role]
log=[]
for op in CFG.get('ops',[]):
    act=act_of(op['role']); k=op['op']
    if k=='limit_rel': RG.limit_rel(act,op['bone'],op['ref'],op['f0'],op['f1'],op['max'])
    elif k=='ease_range': A.ease_range(act,op['bones'],op['fa'],op['fb'])
    elif k=='offsets':
        for b,ax,keys in op['layers']: A.add_offsets(act,b,ax,[tuple(x) for x in keys])
    elif k=='loc_offsets':
        for b,ix,keys in op['layers']: A.add_loc_offsets(act,b,ix,[tuple(x) for x in keys])
    elif k=='hold_extend': A.hold_extend(act,op['total'],op.get('src'))
    elif k=='trim_scale': A.trim_scale(act,op['fa'],op['fb'],op['total'])
    elif k=='cut_stride':
        pl=A.sole_plants(arm,body,act,contact=op.get('contact',0.12),stationary=op.get('stationary',0.06),min_frames=op.get('min_frames',2))
        L=[r[0] for r in pl['left']]; Rr=[r[0] for r in pl['right']]; best=None
        for i in range(len(L)-1):
            l1,l2=L[i],L[i+1]; n=l2-l1
            if op.get('lo',26)<=n<=op.get('hi',46) and any(l1<r<l2 for r in Rr):
                best=(l1,l2); 
                if op.get('prefer_mid') and l1<op['prefer_mid']: continue
                break
        log.append(('stride',pl['left'][:12],pl['right'][:12],best))
        if best: A.trim_scale(act,best[0],best[1],best[1]-best[0]+1)
    elif k=='ease_seam': A.ease_seam(act,op['n'],op.get('bones'))
    A.normalize_signs(act); log.append((op['role'],k))
out={}; FM={}
for role in CFG['roles']:
    act=act_of(role); A.normalize_signs(act)
    h=[]; 
    a0=A.audit(arm,body,act,role); fmap=None
    if (a0['over'] or a0['ang_over']) and role in CFG.get('retime_roles',[]):
        fmap=RG.speed_retime(arm,body,act,role,0.92*A.LIM[role],0.92*A.ANG[role],max_sub=CFG.get('max_sub',24)); A.normalize_signs(act)
        a0=A.audit(arm,body,act,role)
    if a0['over'] or a0['ang_over'] or a0['local_over']:
        h=A.deglitch2(arm,body,act,role,rounds=20); A.normalize_signs(act)
    if role in loops:
        for n in (8,12,16,22,30,40):
            sm=A.local_seam(act); ws=A.audit(arm,body,act,role)['seam']
            if sm[0]<2.0 and ws<0.045: break
            A.ease_seam(act,n); h+=A.deglitch2(arm,body,act,role,rounds=10); A.normalize_signs(act)
    if role in CFG.get('floor_roles',CFG['roles']):
        A.ground_in_place(arm,body,act,root=CFG.get('root','Hips')); A.normalize_signs(act)
    if fmap is not None: FM[role]={str(int(k)):float(v) for k,v in fmap.items()}
    a=A.audit(arm,body,act,role)
    mz=z.mesh_floor(body,list(range(int(act.frame_range[0]),int(act.frame_range[1])+1)))[:,0]
    out[role]=dict(frames=int(act.frame_range[1]),fmap=(None if fmap is None else {str(k):v for k,v in list(fmap.items())[::4]}),h=h[:4],over=a['over'],worst=a['worst'][:2],ang_over=a['ang_over'],local_over=a['local_over'],local_max=a['local_max'],seam=a['seam'],lseam=a['local_seam'][0],floor_min=round(float(mz.min()),3),t=round(time.time()-t0))
uf.save_ck(CFG['job'],CFG['out'])
if CFG.get('fmap_out'): json.dump(FM,open(R+'.tmp/unitfix2/'+CFG['fmap_out'],'w'))
result=out
