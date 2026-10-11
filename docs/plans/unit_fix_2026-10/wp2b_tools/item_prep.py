# Lab script. CFG: job, name, glb, npz, min_comp. Imports a Meshy item GLB into an empty scene, welds and repairs it, unwraps it
# into planar islands and exports bake arrays; saves <job>/blender/checkpoints/items/item_<name>_geom.blend
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, uvtools as U; importlib.reload(U)
import bpy, numpy as np, json, os
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/"
bpy.ops.wm.read_homefile(use_empty=True, use_factory_startup=True)
bpy.ops.import_scene.gltf(filepath=J+CFG['glb'])
parts=[o for o in bpy.data.objects if o.type=='MESH']
for o in bpy.data.objects:
    if o.type!='MESH': bpy.data.objects.remove(o)
bpy.ops.object.select_all(action='DESELECT')
for o in parts: o.select_set(True)
bpy.context.view_layer.objects.active=parts[0]
if len(parts)>1: bpy.ops.object.join()
w=bpy.context.view_layer.objects.active
w.parent=None; w.data.transform(w.matrix_world); w.matrix_world=__import__('mathutils').Matrix.Identity(4)
w.name='ITEM_'+CFG['name']
log={'before':U.topo(w)}
log.update(U.geom_prep(w))
me=w.data
lab=np.zeros(len(me.polygons),dtype=int); pl=['item']
co,fv,P,isl,area,nb=U.box_uv(w,lab,pl,min_comp=CFG.get('min_comp',60))
uvs,m=U.pack_islands(P,fv,isl,pl,density_boost={})
U.write_uv(w,uvs)
U.blender_pack(w,'UV_WP3',margin=CFG.get('margin',0.008))
log['uv']=dict(islands=len(isl),pack=str(m))
U.export_bake_arrays(w,'UVMap','UV_WP3',lab,CFG['npz'])
os.makedirs(J+"blender/checkpoints/items",exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=J+"blender/checkpoints/items/item_%s_geom.blend"%CFG['name'])
result=log
