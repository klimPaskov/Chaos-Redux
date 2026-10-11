# Lab script: two-hand hold pass. For every frame of every listed role the main hand is aimed (about the wrist) so the item axis follows the
# measured hand-to-hand line (fallback: its own provider orientation when the hands are close), then the off-hand arm is reached onto the shaft.
# CFG: job, src, out, prefix, main, off, upper_off, fore_off, axis_local, item, roles:{role:{aim:true,hold:true}}, s_min, g_min_gap, g_full_gap, sigma, shaft:[butt_to_main(world), main_to_head(world)]
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy, numpy as np, math, json
from mathutils import Matrix, Vector, Quaternion
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
main,off=CFG['main'],CFG['off']; up_o,fo_o=CFG['upper_off'],CFG['fore_off']
al=Vector(CFG['axis_local']).normalized()
arm.animation_data_create(); arm.animation_data.action=None; H.set_rest(arm,True)
_,pm_off,_=H.hand_centroid(arm,body,main); _,po_off,_=H.hand_centroid(arm,body,off)
H.set_rest(arm,False)
def palm(bone,offv): return H.head(arm,bone)+H.rot3(arm,bone)@Vector(offv)
def smooth_dirs(D,sigma,loop=False):
    n=len(D); out=[]
    rad=int(math.ceil(3*sigma))
    for i in range(n):
        acc=Vector((0,0,0)); ws=0
        for k in range(-rad,rad+1):
            j=(i+k)%(n-1) if loop and n>1 else min(max(i+k,0),n-1)
            if loop and n>1 and (i+k)>=n-1: j=(i+k-(n-1))
            w=math.exp(-0.5*(k/sigma)**2); acc+=D[j]*w; ws+=w
        out.append((acc/ws).normalized())
    return out
res={}
for role,mode in CFG['roles'].items():
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]; z.set_action(arm,act)
    if mode.get('ease_seam'): A.ease_seam(act,mode['ease_seam'])
    f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
    frames=list(range(f0,f1+1))
    want=[]; gaps=[]
    for f in frames:
        bpy.context.scene.frame_set(f)
        Pm=palm(main,pm_off); Po=palm(off,po_off); d=Po-Pm; gap=d.length
        ac=(H.rot3(arm,main)@al).normalized()
        if gap>1e-4:
            w=min(max((gap-CFG['g_min_gap'])/(CFG['g_full_gap']-CFG['g_min_gap']),0.0),1.0); w=w*w*(3-2*w)
        else: w=0.0
        ad=d.normalized() if gap>1e-4 else ac
        v=ac.lerp(ad,w) if mode.get('aim',True) else ac
        want.append(v.normalized()); gaps.append(gap)
    ws=smooth_dirs(want,CFG.get('sigma',1.5),loop=mode.get('loop',False)) if mode.get('aim',True) else want
    aim_err=[];reach=[];keyed=[]
    for f,wv,gap in zip(frames,ws,gaps):
        bpy.context.scene.frame_set(f)
        if mode.get('aim',True):
            for it in range(3):
                ac=(H.rot3(arm,main)@al).normalized()
                H.rot_bone(arm,main,H.head(arm,main),ac,wv)
            aim_err.append(math.degrees((H.rot3(arm,main)@al).angle(wv)))
            arm.pose.bones[main].keyframe_insert('rotation_quaternion',frame=f)
        if mode.get('hold',True):
            ac=(H.rot3(arm,main)@al).normalized(); Pm=palm(main,pm_off)
            s=min(max(gap,CFG['s_min']),CFG['s_max'])
            T=Pm+ac*s
            r=H.solve_arm(arm,up_o,fo_o,off,T,po_off)
            reach.append(r)
            for n in (up_o,fo_o): arm.pose.bones[n].keyframe_insert('rotation_quaternion',frame=f)
    if mode.get('floor'):
        clear=CFG.get('floor_clear',0.02); it=bpy.data.objects[CFG['item']]; fixed=[]
        for f,gap in zip(frames,gaps):
            bpy.context.scene.frame_set(f); touched=False
            for _ in range(5):
                dg=bpy.context.evaluated_depsgraph_get(); eo=it.evaluated_get(dg); me=eo.to_mesh(); co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
                Mi=np.array(it.matrix_world); wc=co@Mi[:3,:3].T+Mi[:3,3]; eo.to_mesh_clear(); k=int(wc[:,2].argmin()); low=Vector(wc[k])
                if low.z>=clear-1e-4: break
                touched=True; piv=H.head(arm,main); d=low-piv; r=d.length
                hz=Vector((d.x,d.y,0)); 
                if hz.length<1e-6: hz=H.rot3(arm,main)@Vector((1,0,0)); hz.z=0
                ts=max(-1.0,min(1.0,(clear-piv.z)/r)); nd=hz.normalized()*math.sqrt(1-ts*ts)+Vector((0,0,ts))
                H.rot_bone(arm,main,piv,d,nd)
            if touched:
                fixed.append(f); arm.pose.bones[main].keyframe_insert('rotation_quaternion',frame=f)
                if mode.get('hold',True):
                    ac=(H.rot3(arm,main)@al).normalized(); Pm=palm(main,pm_off); s_=min(max(gap,CFG['s_min']),CFG['s_max'])
                    H.solve_arm(arm,up_o,fo_o,off,Pm+ac*s_,po_off)
                    for n in (up_o,fo_o): arm.pose.bones[n].keyframe_insert('rotation_quaternion',frame=f)
        mode['_floor_fixed']=len(fixed)
        A.ground_in_place(arm,body,act)
    A.normalize_signs(act)
    # re-measure contact: distance of the off palm to the shaft segment per frame
    dist=[]
    for f in frames:
        bpy.context.scene.frame_set(f)
        Pm=palm(main,pm_off); Po=palm(off,po_off); ac=(H.rot3(arm,main)@al).normalized()
        t=(Po-Pm).dot(ac); t=min(max(t,-CFG['shaft'][0]),CFG['shaft'][1]); dist.append((Pm+ac*t-Po).length)
    res[role]=dict(frames=len(frames),gap=[round(min(gaps),2),round(max(gaps),2)],aim_err_max=round(max(aim_err),2) if aim_err else None,reach_resid_max=round(max(reach),3) if reach else None,
                   contact_dist_max=round(max(dist),3),contact_dist_mean=round(float(np.mean(dist)),3),floor_fixed=mode.get('_floor_fixed'))
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=res
