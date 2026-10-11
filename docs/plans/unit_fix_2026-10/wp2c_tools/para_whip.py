import sys, json, time; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf; importlib.reload(uf)
from uf import *
from mathutils import Quaternion, Matrix
import holdtools as H, acttools as A
t0=time.time()
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
prefix=CFG['prefix']; K=CFG.get('k',8); loops=set(CFG['loops'])
chains={j:['ParasiteT%d_%d'%(j+1,b+1) for b in range(3)] for j in range(K)}
parents={j:arm.data.bones[chains[j][0]].parent.name for j in range(K)}
LAG=CFG.get('alpha',[0.5,0.32,0.22]); GAMMA=CFG.get('gamma',1.5)
AMP=[8,10,9,11,8,10,9,11]; CYC=[1,2,2,1,2,1,2,1]
def qpow(a,b,g):
    dq=a.inverted()@b
    if dq.w<0: dq=Quaternion((-dq.w,-dq.x,-dq.y,-dq.z))
    ax,ang=dq.to_axis_angle()
    return a@Quaternion(ax,ang*g)
def zero(): 
    for pb in arm.pose.bones: pb.rotation_mode='QUATERNION'
    for j in chains:
        for n in chains[j]:
            pb=arm.pose.bones[n]; pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
    bpy.context.view_layer.update()
def rot_about(pb, piv, q):
    world=arm.matrix_world@pb.matrix
    turned=Matrix.Translation(piv)@q.to_matrix().to_4x4()@Matrix.Translation(-piv)@world
    pb.matrix=arm.matrix_world.inverted()@turned; pb.scale=(1,1,1); bpy.context.view_layer.update()
out={}
for role in CFG['roles']:
    act=bpy.data.actions[prefix+'_'+role]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); n=f1-f0+1
    zero()
    # parent world rotations per frame
    Q={}
    for p in set(parents.values()):
        Q[p]=[]
    for f in range(f0,f1+1):
        bpy.context.scene.frame_set(f); zero()
        for p in Q: Q[p].append((arm.matrix_world@arm.pose.bones[p].matrix).to_quaternion())
    O={}
    for j in range(K):
        seq=Q[parents[j]]; layers=[seq]
        for m in range(3):
            a=LAG[m]; filt=[None]*n; cur=seq[-1].copy() if role in loops else seq[0].copy()
            for rep in range(2 if role in loops else 1):
                for t in range(n):
                    cur=cur.slerp(seq[t],a); filt[t]=cur.copy()
            layers.append([qpow(seq[t],filt[t],GAMMA) for t in range(n)])
        O[j]=layers
    # writhe key lists (explicit values at every 8th frame, interpolated)
    amp_scale=1.0 if role=='idle' else 0.5
    def writhe(j,m,t):
        cyc=CYC[j]*(1 if role in ('idle','move','retreat','training','defend') else 1)
        ph=(j*0.7+m*0.55)
        return AMP[j]*amp_scale*(0.6+0.4*m)*math.sin(2*math.pi*cyc*t/max(n-1,1)+ph)
    for k,f in enumerate(range(f0,f1+1)):
        bpy.context.scene.frame_set(f); zero()
        for j in range(K):
            for m in range(1,4):
                pb=arm.pose.bones[chains[j][m-1]]
                d=O[j][m][k]@O[j][m-1][k].inverted()
                head=arm.matrix_world@pb.head
                tail=arm.matrix_world@pb.tail; axis=(tail-head).cross(Vector((0,0,1)))
                if axis.length<1e-6: axis=Vector((1,0,0))
                w=Quaternion(axis.normalized(),math.radians(writhe(j,m,k)))
                rot_about(pb,arm.matrix_world@pb.head,w@d)
                pb.keyframe_insert('rotation_quaternion',frame=f)
    A.normalize_signs(act)
    for _r in ('attack','defend','support_attack','training','death'): A.LIM[_r]=0.409; A.ANG[_r]=29.9
    for _r in ('move','retreat'): A.LIM[_r]=0.356; A.ANG[_r]=24.8
    A.LIM['idle']=0.099; A.ANG['idle']=9.9
    a=A.audit(arm,body,act,role); h=[]
    if a['over'] or a['ang_over'] or a['local_over']: h=A.deglitch2(arm,body,act,role,rounds=10); A.normalize_signs(act)
    out[role]=dict(frames=n,t=round(time.time()-t0),hist=h)
uf.save_ck(CFG['job'],CFG['out'])
result=out
