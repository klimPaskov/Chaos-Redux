# Lab: item floor fix (+ left-hand refresh) and body grounding, alternating with smoothing until motion limits and floor both hold.
# CFG: job, src, out, prefix, roles, item, main, off(optional), upper_off, fore_off, axis_local, s_min, s_max, gap_default, floor_clear, rounds
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H, acttools as A; importlib.reload(z); importlib.reload(H); importlib.reload(A)
import bpy, numpy as np, math
from mathutils import Vector
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']; it=bpy.data.objects[CFG['item']]
main=CFG['main']; off=CFG.get('off'); al=Vector(CFG['axis_local']).normalized()
arm.animation_data_create(); arm.animation_data.action=None; H.set_rest(arm,True)
pm_off=list(H.hand_centroid(arm,body,main)[1]); po_off=list(H.hand_centroid(arm,body,off)[1]) if off else None
H.set_rest(arm,False)
def palm(b,o): return H.head(arm,b)+H.rot3(arm,b)@Vector(o)
def item_low():
    dg=bpy.context.evaluated_depsgraph_get(); eo=it.evaluated_get(dg); me=eo.to_mesh(); co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
    M=np.array(it.matrix_world); wc=co@M[:3,:3].T+M[:3,3]; eo.to_mesh_clear(); k=int(wc[:,2].argmin()); return Vector(wc[k])
def floor_fix(act):
    """Per frame: turn the item about the wrist toward clearing the floor by the largest fraction of the turn (1, .75, .5, .35, .2) for which the off hand can still
    be reached onto the shaft within the hold tolerance. The remaining shortfall stays and is reported by the floor measurement."""
    clear=CFG.get('floor_clear',0.02); tol=CFG.get('hold_tol',0.3); f0,f1=int(act.frame_range[0]),int(act.frame_range[1]); z.set_action(arm,act); fixed=[]
    side='Right' if main.startswith('Right') else 'Left'
    order=[side+'Arm',side+'ForeArm',main]+([CFG['upper_off'],CFG['fore_off']] if off else [])
    def snap(): return {n:arm.pose.bones[n].matrix.copy() for n in order}
    def setpose(sn):
        for n in order:
            arm.pose.bones[n].matrix=sn[n]; bpy.context.view_layer.update()
    def left_refresh(gap):
        if not off: return 0.0
        ac=(H.rot3(arm,main)@al).normalized(); Pm=palm(main,pm_off); s_=min(max(gap,CFG['s_min']),CFG['s_max'])
        return H.solve_arm(arm,CFG['upper_off'],CFG['fore_off'],off,Pm+ac*s_,po_off)
    for f in range(f0,f1+1):
        bpy.context.scene.frame_set(f)
        low=item_low()
        if low.z>=clear-1e-4: continue
        gap=(palm(off,po_off)-palm(main,pm_off)).length if off else 0
        base=snap(); piv=H.head(arm,main); d=low-piv; r=d.length; hz=Vector((d.x,d.y,0))
        if hz.length<1e-6: hz=H.rot3(arm,main)@Vector((1,0,0)); hz.z=0
        ts=max(-1.0,min(1.0,(clear-piv.z)/r)); nd=hz.normalized()*math.sqrt(1-ts*ts)+Vector((0,0,ts))
        chosen=None
        for t in (1.0,0.75,0.5,0.35,0.2):
            setpose(base)
            gd=d.normalized().lerp(nd,t).normalized()
            H.rot_bone(arm,main,piv,d,gd)
            if left_refresh(gap)<=tol: chosen=t; break
        if chosen is None: setpose(base)
        for n in order: arm.pose.bones[n].keyframe_insert('rotation_quaternion',frame=f)
        fixed.append(f)
    A.ground_in_place(arm,body,act); A.normalize_signs(act); return len(fixed)
out={}
for role in CFG['roles']:
    act=bpy.data.actions[f"{CFG['prefix']}_{role}"]; log=[]
    for r in range(CFG.get('rounds',4)):
        n=floor_fix(act); a=A.audit(arm,body,act,role); log.append((n,a['over'],a['ang_over'],a['local_over']))
        if not (a['over'] or a['ang_over'] or a['local_over']): break
        A.deglitch2(arm,body,act,role,rounds=10)
    n=floor_fix(act); a=A.audit(arm,body,act,role)
    out[role]=dict(log=log,final_floor_fixed=n,over=a['over'],ang_over=a['ang_over'],local_over=a['local_over'],local_max=a['local_max'],ang_max=a['ang_max'],seam=a['seam'])
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=out
