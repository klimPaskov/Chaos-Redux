"""Stage A without arm re-solve: move the item onto the palm-side grip, counter-rotate the hand keys (item keeps its world orientation), write the aux file
(left-hand stations, shaft radii, grip frames) for the post step. CFG: job, src, out, item, main, off?, al, roles, loops, s_min, s_max, beta, dsh, tt, aux_out"""
import sys, json, time; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, fingers as F, grip as Gp, regrip as RG; importlib.reload(uf); importlib.reload(F); importlib.reload(Gp); importlib.reload(RG)
from uf import *
import holdtools as H, acttools as A
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']; item=bpy.data.objects[CFG['item']]
main,off=CFG['main'],CFG.get('off'); sideM='Right' if main.startswith('Right') else 'Left'; sideO=('Left' if sideM=='Right' else 'Right') if off else None
prefix=CFG['job']; roles=CFG['roles']; loops=CFG.get('loops',[])
arm.animation_data_create(); saved=arm.animation_data.action
al=np.array(CFG['al'],float); al/=np.linalg.norm(al)
if off:   # orient the item axis (butt->head convention) toward the off hand using the idle pose
    z.set_action(arm,bpy.data.actions[prefix+'_idle']); bpy.context.scene.frame_set(1)
    pmw=H.head(arm,main)+H.rot3(arm,main)@Vector(RG.hand_centroid_all(arm,body,sideM).tolist()); pow_=H.head(arm,off)+H.rot3(arm,off)@Vector(RG.hand_centroid_all(arm,body,sideO).tolist())
    if float(np.dot(np.array(pow_-pmw),np.array(H.rot3(arm,main))@al))<0: al=-al
arm.animation_data.action=None; H.set_rest(arm,True); Gp.zero_pose(arm)
frM=RG.hand_base(arm,body,sideM,CFG['beta'],CFG['dsh'],CFG['tt'],ref=al); frO=RG.hand_base(arm,body,sideO,CFG['beta'],CFG['dsh'],CFG['tt']) if off else None
pm_old=[float(x) for x in RG.hand_centroid_all(arm,body,sideM)]; po_old=[float(x) for x in RG.hand_centroid_all(arm,body,sideO)] if off else None
Rr=np.array(H.rot3(arm,main)); hd=np.array(H.head(arm,main))
sgrid=np.arange(-0.5,CFG.get('s_max',5.7)+0.01,0.05)
c0=hd+Rr@np.array(pm_old); prof=RG.radius_profile(item,c0,Rr@al,sgrid)
r_item=float(prof[np.argmin(np.abs(sgrid-0.0))]); r_item=min(max(r_item,0.06),0.3)
acts=[bpy.data.actions[prefix+'_'+r] for r in roles]
repA=RG.stageA(arm,body,item,sideM,frM,al,pm_old,r_item,acts)
# profile again around the new axis (same geometry, different origin station): axis through G_R in the hand frame
G_R=[float(x) for x in (frM['base']+frM['N']*r_item)]
H.set_rest(arm,False); arm.animation_data.action=saved
rep={'stageA':repA,'r_item':round(r_item,3),'G_R':G_R}
s_all={}; rl_all={}; sLd={}
for role in roles:
    act=bpy.data.actions[prefix+'_'+role]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); n=f1-f0+1
    if off:
        sraw=[]; sm=0.0
        for k,f in enumerate(range(f0,f1+1)):
            bpy.context.scene.frame_set(f)
            P=H.head(arm,main)+H.rot3(arm,main)@Vector(G_R); a=(H.rot3(arm,main)@Vector(list(frM['a']))).normalized()
            Po=H.head(arm,off)+H.rot3(arm,off)@Vector(po_old); sraw.append(float((Po-P).dot(a)))
            sm+=float(np.sign(np.dot(np.array(H.rot3(arm,off))@frO['a'],np.array(a))))
        sLd[role]=1.0 if sm>=0 else -1.0
        sb=np.clip(np.array(sraw),CFG['s_min'],CFG['s_max']); loop=role in loops
        pad=9; sg=3.0; gk=np.exp(-0.5*(np.arange(-pad,pad+1)/sg)**2); gk/=gk.sum()
        sp=np.concatenate([sb[-pad:],sb,sb[:pad]]) if loop else np.pad(sb,pad,mode='edge'); ss=np.convolve(sp,gk,mode='valid')
        s_all[role]=[round(float(x),3) for x in ss]
        rl=np.clip(np.interp(ss,sgrid,prof),0.12,0.32); rl=np.convolve(np.pad(rl,3,mode='edge'),np.ones(7)/7,mode='valid'); rl_all[role]=[round(float(x),4) for x in rl]
    else:
        s_all[role]=[0.0]*n
rep['sL']=sLd
json.dump({'s_used':s_all,'rleft':rl_all,'r_item':r_item,'G_R':G_R,'a_gR':[float(x) for x in frM['a']],'sL':sLd},open(R+'.tmp/unitfix2/'+CFG['aux_out'],'w'))
uf.save_ck(CFG['job'],CFG['out'])
result=rep
