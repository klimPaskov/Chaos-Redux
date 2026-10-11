# Lab script. CFG: job, blend (job/blender/checkpoints rel) | open:false to use the open scene, tex {object: diffuse path}, shots:[{action,frame,view,center?,size?}], out, cols, res
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z; importlib.reload(z)
import bpy, os
from mathutils import Vector
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
if CFG.get('open',True): bpy.ops.wm.open_mainfile(filepath=J+CFG['blend'])
arm=bpy.data.objects['Armature.001']
objs=[o for o in bpy.data.objects if o.type=='MESH' and o.name in CFG['tex']]
for o in bpy.data.objects:
    if o.type=='MESH' and o not in objs: o.hide_render=True
    if o.type=='ARMATURE': o.hide_render=True
for o in objs:
    me=o.data
    if 'UV_WP3' in me.uv_layers and 'UVMap' not in me.uv_layers: me.uv_layers['UV_WP3'].name='UVMap'
    me.uv_layers.active=me.uv_layers['UVMap']; me.uv_layers['UVMap'].active_render=True
z.setup_world(); sc=bpy.context.scene; sc.render.resolution_x,sc.render.resolution_y=CFG.get('res',[300,375])
saved={}
for o in objs:
    saved[o.name]=z.preview_material(o,R+CFG['tex'][o.name]) if False else None
mats={}
for o in objs:
    img=bpy.data.images.load(R+CFG['tex'][o.name],check_existing=True)
    m=bpy.data.materials.new('PV_'+o.name); m.use_nodes=True; nt=m.node_tree
    for n in list(nt.nodes): nt.nodes.remove(n)
    out=nt.nodes.new('ShaderNodeOutputMaterial'); bs=nt.nodes.new('ShaderNodeBsdfPrincipled'); tx=nt.nodes.new('ShaderNodeTexImage'); tx.image=img
    nt.links.new(tx.outputs['Color'],bs.inputs['Base Color']); nt.links.new(bs.outputs['BSDF'],out.inputs['Surface'])
    saved[o.name]=[s.material for s in o.material_slots]
    for s in o.material_slots: s.material=m
paths=[]
for i,sh in enumerate(CFG['shots']):
    if sh.get('action'): z.set_action(arm,bpy.data.actions[sh['action']]); sc.frame_set(sh['frame'])
    else:
        arm.animation_data_create(); arm.animation_data.action=None; arm.data.pose_position='REST'
    c=Vector(sh['center']) if sh.get('center') else Vector((0,0,3.6))
    p=R+".tmp/wp2b/pv/_s%d.png"%i
    z.shot(p,objs,sh.get('view','front'),center=c,size=sh.get('size',8.0)); paths.append(p)
    if not sh.get('action'): arm.data.pose_position='POSE'
res=z.sheet(paths,R+CFG['out'],cols=CFG.get('cols',len(paths)))
for p in paths: os.remove(p)
for o in objs:
    for s,m in zip(o.material_slots,saved[o.name]): s.material=m
result={"sheet":res}
