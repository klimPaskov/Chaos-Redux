import sys, json, time; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, fingers as F, grip as Gp, regrip as RG; importlib.reload(uf); importlib.reload(F); importlib.reload(Gp); importlib.reload(RG)
from uf import *
import holdtools as H, acttools as A
t0=time.time()
import acttools as _A
for _r in ('attack','defend','support_attack','training','death'): _A.LIM[_r]=0.409; _A.ANG[_r]=29.9
for _r in ('move','retreat'): _A.LIM[_r]=0.356; _A.ANG[_r]=24.8
_A.LIM['idle']=0.099; _A.ANG['idle']=9.9
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']; item=bpy.data.objects[CFG['item']]
tg=None; aux=json.load(open(R+".tmp/unitfix2/"+CFG['aux']))
main,off=CFG['main'],CFG.get('off'); sideM='Right' if main.startswith('Right') else 'Left'; sideO=('Left' if sideM=='Right' else 'Right') if off else None
prefix=CFG['job']; roles=CFG['roles']; loops=CFG['loops']
arm.animation_data_create(); saved=arm.animation_data.action; arm.animation_data.action=None; Gp.zero_pose(arm)
frM=None; frO=RG.hand_base(arm,body,sideO,CFG['beta'],CFG['dsh'],CFG['tt']) if off else None
arm.animation_data.action=saved
cfg=dict(main=main,off=off,up_m=sideM+'Arm',fo_m=sideM+'ForeArm',G_R=aux['G_R'],a_gR=aux['a_gR'],s_min=CFG['s_min'],s_max=CFG['s_max'])
if off: cfg.update(up_o=sideO+'Arm',fo_o=sideO+'ForeArm',a_gL=frO['a'],N_L=frO['N'],baseL=frO['base'])
sL=aux['sL']; out={}
NO_ALIGN=set(CFG.get('no_align',[]))
for role in roles:
    cfg['no_align']=role in NO_ALIGN
    act=bpy.data.actions[prefix+'_'+role]; rows=None; rl=np.array(aux['rleft'][role]) if off else None
    log=[]
    # 1 smooth over-limit windows
    a0=A.audit(arm,body,act,role); h=[]; changed=bool(off)
    if a0['over'] or a0['ang_over'] or a0['local_over']:
        h=A.deglitch2(arm,body,act,role,rounds=14); changed=True
    A.normalize_signs(act)
    # 2 loop seal (whole body), then floor guard + left refresh, then close the refreshed arms onto frame 1
    sealed=False; slog=[('start',A.local_seam(act))]
    if role in loops:
        for n in (8,12,16,22,30):
            sm=A.local_seam(act)
            if sm[0]<CFG.get('seam_deg',2.0): break
            A.ease_seam(act,n); changed=True; sealed=True
        A.normalize_signs(act)
    slog.append(('sealed',A.local_seam(act),changed))
    def floor_pass(changed):
        if off and CFG.get('floor_mode')=='tilt_first':
            nfix,mzmin=RG.tilt_fix(arm,item,act,main,CFG['clear'],rounds=CFG.get('tilt_rounds',6),sigma=CFG.get('tilt_sigma',2.0)); slog.append(('tilt_first',nfix,round(mzmin,3)))
            if nfix: changed=True
            if changed:
                z0=np.zeros(len(RG.item_min_z(arm,item,act))); RG.solve_frames(arm,cfg,act,aux['s_used'][role],z0,rl,(sL.get(role,1.0) if isinstance(sL,dict) else sL),from_current=True); A.normalize_signs(act)
            return changed
        if off:
            for rnd in range(3):
                mz=RG.item_min_z(arm,item,act); need=np.maximum(0.0,CFG['clear']-mz); dz=RG.smooth_dz(need,rad=6,sigma=2.5); dz=np.maximum(dz,need)
                if need.max()<1e-4 and (rnd>0 or not changed): break
                changed=True
                RG.solve_frames(arm,cfg,act,aux['s_used'][role],dz,rl,(sL.get(role,1.0) if isinstance(sL,dict) else sL),from_current=True)
                A.normalize_signs(act)
            mzc=RG.item_min_z(arm,item,act); slog.append(('mzc',round(float(mzc.min()),3)))
            if mzc.min()<CFG['clear']-0.01:      # arms cannot lift it clear: turn the item about the wrist, then re-reach the off hand
                nfix,mzmin=RG.tilt_fix(arm,item,act,main,CFG['clear']); changed=True; slog.append(('tilt',nfix,round(mzmin,3)))
                z0=np.zeros(len(mzc)); RG.solve_frames(arm,cfg,act,aux['s_used'][role],z0,rl,(sL.get(role,1.0) if isinstance(sL,dict) else sL),from_current=True); A.normalize_signs(act)
        else:
            nfix,mzmin=RG.tilt_fix(arm,item,act,main,CFG['clear'])
            if nfix: changed=True
            slog.append(('tilt',nfix,round(mzmin,3)))
            if mzmin<CFG['clear']-0.01:
                for rnd in range(3):
                    mz=RG.item_min_z(arm,item,act); need=np.maximum(0.0,CFG['clear']-mz); dz=RG.smooth_dz(need,rad=6,sigma=2.5); dz=np.maximum(dz,need)
                    if need.max()<1e-4: break
                    changed=True; RG.solve_frames(arm,cfg,act,aux['s_used'][role],dz,rl,1.0,from_current=True); A.normalize_signs(act)
        return changed
    changed=floor_pass(changed)
    _a=A.audit(arm,body,act,role); slog.append(('diag_after_floor',_a['over'],_a['ang_over'],_a['local_over'],_a['worst'][:3],_a['local_worst'][:3]))
    slog.append(('refreshed',A.local_seam(act),changed))
    if role in loops and changed:
        solved=[cfg['up_m'],cfg['fo_m'],main]+([cfg['up_o'],cfg['fo_o'],off] if off else [])
        for n in (6,10,14,20):
            sm=A.local_seam(act)
            if sm[0]<CFG.get('seam_deg',2.0): break
            A.ease_seam(act,n,bones=solved)
        A.normalize_signs(act)
    slog.append(('final',A.local_seam(act)))
    a1=A.audit(arm,body,act,role)
    if a1['over'] or a1['ang_over'] or a1['local_over']:
        h+=A.deglitch2(arm,body,act,role,rounds=12); A.normalize_signs(act)
        for _k in range(2):
            if RG.item_min_z(arm,item,act).min()>=CFG['clear']-0.01: break
            floor_pass(True); A.normalize_signs(act)
        if role in loops:
            for n in (6,10,14,20):
                if A.local_seam(act)[0]<CFG.get('seam_deg',2.0): break
                A.ease_seam(act,n)
            A.normalize_signs(act)
    mz=RG.item_min_z(arm,item,act)
    a1=A.audit(arm,body,act,role)
    out[role]=dict(slog=[str(x) for x in slog],hist=h,floor_min=round(float(mz.min()),3),below=int((mz<0).sum()),over=a1['over'],worst=a1['worst'][:2],ang_over=a1['ang_over'],local_over=a1['local_over'],local_max=a1['local_max'],seam=a1['seam'],local_seam=a1['local_seam'][0],t=round(time.time()-t0))
uf.save_ck(CFG['job'],CFG['out'])
result=out
