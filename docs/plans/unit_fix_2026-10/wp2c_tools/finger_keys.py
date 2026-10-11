import sys, json; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf, fingers as F, grip as Gp, regrip as RG; importlib.reload(uf); importlib.reload(F); importlib.reload(Gp); importlib.reload(RG)
from uf import *
import holdtools as H, acttools as A
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
aux=json.load(open(R+".tmp/unitfix2/"+CFG['aux']))
prefix=CFG['job']; roles=CFG['roles']
arm.animation_data_create(); saved=arm.animation_data.action; arm.animation_data.action=None; H.set_rest(arm,False); Gp.zero_pose(arm)
def qdict(ang):
    out={}
    for b,v in ang.items():
        if isinstance(v,tuple): out[b]=Quaternion(v[1],math.radians(v[0]))
        else: out[b]=Quaternion((1,0,0),math.radians(v))
    return out
sol={}
def solve_side(side, base, N, a_g, r):
    Rr=np.array(H.rot3(arm,side+'Hand')); hd0=np.array(H.head(arm,side+'Hand')); hd=Gp.hand_data(arm,body,side)
    G=base+N*r; c=hd0+Rr@G; a=Rr@a_g; a/=np.linalg.norm(a)
    Gp.zero_pose(arm); ang=Gp.curl_solve(arm,body,hd,side,c,a,r); rep=Gp.finger_report(arm,hd,side,c,a,r); Gp.zero_pose(arm)
    return ang,rep
rep={}
main=CFG['main']; sideM='Right' if main.startswith('Right') else 'Left'; off=CFG.get('off'); sideO=('Left' if sideM=='Right' else 'Right') if off else None
frM=RG.hand_base(arm,body,sideM,CFG['beta'],CFG['dsh'],CFG['tt']); frM['a']=np.array(aux['a_gR'])
angR,repR=solve_side(sideM,frM['base'],frM['N'],frM['a'],aux['r_item']); rep['main']={'ang':{k:(round(v,1) if not isinstance(v,tuple) else (round(v[0],1),v[1])) for k,v in angR.items()},'gap':repR}
grid=[0.12,0.16,0.20,0.24,0.28,0.32]; angL={}
if off:
    frO=RG.hand_base(arm,body,sideO,CFG['beta'],CFG['dsh'],CFG['tt'])
    for r in grid:
        angL[r],rl=solve_side(sideO,frO['base'],frO['N'],frO['a'],r)
    rep['off']={str(r):{k:(round(v,1) if not isinstance(v,tuple) else round(v[0],1)) for k,v in angL[r].items()} for r in grid}
arm.animation_data.action=saved
def lerp_ang(r):
    r=min(max(r,grid[0]),grid[-1]); i=max(0,min(len(grid)-2,int(np.searchsorted(grid,r))-1)); t=(r-grid[i])/(grid[i+1]-grid[i]); out={}
    for b in angL[grid[i]]:
        a0,a1=angL[grid[i]][b],angL[grid[i+1]][b]
        if isinstance(a0,tuple): out[b]=(a0[0]*(1-t)+a1[0]*t,a0[1])
        else: out[b]=a0*(1-t)+a1*t
    return out
qM=qdict(angR)
for role in roles:
    act=bpy.data.actions[prefix+'_'+role]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
    rl=aux['rleft'][role] if off else None
    for k,f in enumerate(range(f0,f1+1)):
        qs=dict(qM)
        if off: qs.update(qdict(lerp_ang(rl[k])))
        for n,q in qs.items():
            pb=arm.pose.bones[n]; pb.rotation_mode='QUATERNION'; pb.rotation_quaternion=q; pb.keyframe_insert('rotation_quaternion',frame=f)
uf.save_ck(CFG['job'],CFG['out'])
result=rep
