import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, acttools as A; importlib.reload(z); importlib.reload(A)
import bpy, json
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG.get('src','wp3_01_geom_uv.blend'))
body=bpy.data.objects["char1.001"]; arm=bpy.data.objects["Armature.001"]; me=body.data
if 'UV_WP3' in me.uv_layers:
    me.uv_layers.remove(me.uv_layers['UVMap']); me.uv_layers['UV_WP3'].name='UVMap'
me.uv_layers.active=me.uv_layers['UVMap']
import uvtools as U; importlib.reload(U)
if CFG.get('snap_wrists'): print('wrist weights changed',U.snap_wrist_weights(body))
pre=CFG['prefix']
for role,(fa,fb,nt) in CFG.get('trim',{}).items():
    a_=bpy.data.actions[f'{pre}_{role}']; A.trim_scale(a_,fa,fb,nt)
for na in CFG.get('new_actions',[]):
    base=bpy.data.actions[f"{pre}_{na['base']}"]; old=bpy.data.actions[f"{pre}_{na['role']}"]
    old.name=f"rejected_{old.name}"; old.use_fake_user=True
    new=base.copy(); new.name=f"{pre}_{na['role']}"; A.normalize_signs(new); A.hold_extend(new,na['total'],src_frame=na.get('src_frame'))
for role,n in CFG.get('extend',{}).items():
    a_=bpy.data.actions[f'{pre}_{role}']; A.normalize_signs(a_)
    if isinstance(n,list): A.hold_extend(a_,n[0],src_frame=n[1])
    else: A.hold_extend(a_,n)
res=A.generic_pass(arm,body,pre,seam_n=CFG.get('seam_n',8))
for role,layers in CFG.get('layers',{}).items():
    act=bpy.data.actions[f'{pre}_{role}']
    for bone,axis,keys in layers: A.add_offsets(act,bone,axis,[tuple(k) for k in keys])
    res[role]=A.audit(arm,body,act,role)
for role,bone,floor,fa,fb in CFG.get('thigh_clamps',[]):
    act=bpy.data.actions[f'{pre}_{role}']; res.setdefault('clamp',{})[bone]=A.clamp_thigh(arm,act,bone,floor,fa,fb)
    A.deglitch2(arm,body,act,role); res[role]=A.audit(arm,body,act,role)
for role,rows in CFG.get('loc_layers',{}).items():
    act=bpy.data.actions[f'{pre}_{role}']
    for bone,idx,keys in rows: A.add_loc_offsets(act,bone,idx,[tuple(k) for k in keys])
for role in CFG.get('ground_roles',[]):
    act=bpy.data.actions[f'{pre}_{role}']; res.setdefault('grounded',{})[role]=A.ground_in_place(arm,body,act,both=CFG.get('ground_both',False))
if CFG.get('lift_all',True):
    for role in ('idle','move','attack','defend','support_attack','retreat','training','death'):
        if role in CFG.get('lift_skip',[]): continue
        act=bpy.data.actions[f'{pre}_{role}']
        n,mx=A.ground_in_place(arm,body,act,both=False)
        if n: res.setdefault('lifted',{})[role]=(n,round(mx,3))
# optional per-role post fixes: deglitch again after layers
for role in set(list(CFG.get('layers',{}))+list(CFG.get('loc_layers',{}))):
    act=bpy.data.actions[f'{pre}_{role}']
    A.deglitch2(arm,body,act,role); res[role]=A.audit(arm,body,act,role)
for role in ('idle','move','attack','defend','support_attack','retreat','training','death'):
    bpy.data.actions[f'{pre}_{role}'].use_fake_user=True
bpy.ops.wm.save_as_mainfile(filepath=J+CFG.get('out','wp3_02_actions.blend'))
result={k:{kk:vv for kk,vv in v.items() if kk in ('over','ang_over','ang_max','seam','flips','worst','frames')} for k,v in res.items()}
