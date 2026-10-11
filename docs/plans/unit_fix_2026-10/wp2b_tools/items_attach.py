# Lab script. CFG: job, src (blend rel to job blender/checkpoints), out, items:[{name, geo (items/item_<name>_geom.blend), tex (dir with diffuse/specular/normal png),
#   bone, length (world units), grip_along, axis_local:[x,y,z] (hand frame, butt->head), roll_deg, offset_local:[x,y,z], main_off:{bone, ...}}]
import sys; sys.path.insert(0,r"<mod root>/.tmp/wp2b")
import importlib, zv as z, holdtools as H; importlib.reload(z); importlib.reload(H)
import bpy, numpy as np, json, math, os
from mathutils import Matrix, Vector, Quaternion
R=r"<mod root>/"
J=R+"docs/assets/014_cannibalism/models_3d/"+CFG['job']+"/blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects['char1.001']
for a in bpy.data.actions: a.use_fake_user=True
arm.animation_data_create(); saved_action=arm.animation_data.action; arm.animation_data.action=None
H.set_rest(arm,True)
rep={}
for spec in CFG['items']:
    name=spec['name']
    with bpy.data.libraries.load(J+spec['geo']) as (src,dst):
        dst.objects=[o for o in src.objects if o.startswith('ITEM_')]
    it=dst.objects[0]
    for c in body.users_collection: c.objects.link(it)
    me=it.data
    if 'UV_WP3' in me.uv_layers:
        me.uv_layers.remove(me.uv_layers['UVMap']); me.uv_layers['UV_WP3'].name='UVMap'
    me.uv_layers.active=me.uv_layers['UVMap']
    if spec.get('mirror_x'):
        for v in me.vertices: v.co.x=-v.co.x
        import bmesh
        bm=bmesh.new(); bm.from_mesh(me); bmesh.ops.reverse_faces(bm,faces=bm.faces[:]); bm.to_mesh(me); bm.free(); me.update()
    co=np.empty(len(me.vertices)*3); me.vertices.foreach_get('co',co); co=co.reshape(-1,3)
    ax=spec.get('long_axis',1)   # item-local long axis index (Meshy item GLBs run along Y, head at +Y)
    lo,hi=co[:,ax].min(),co[:,ax].max(); L=hi-lo; s=spec['length']/L
    gy=lo+spec['grip_along']*L
    band=co[np.abs(co[:,ax]-gy)<0.02*L]; g=band.mean(0) if len(band) else co.mean(0); g[ax]=gy
    cen,cen_local,_=H.hand_centroid(arm,body,spec['bone'])
    Rh=H.rot3(arm,spec['bone']); hh=H.head(arm,spec['bone'])
    axis_w=(Rh@Vector(spec['axis_local'])).normalized()
    e=Vector([1 if i==ax else 0 for i in range(3)])
    q=e.rotation_difference(axis_w)
    if spec.get('roll_deg'): q=Quaternion(axis_w,math.radians(spec['roll_deg']))@q
    Rq=q.to_matrix()
    G0=cen+Rh@Vector(spec.get('offset_local',[0,0,0]))
    w=np.array([list(G0+Rq@(Vector((v-g))*s)) for v in co])
    inv=np.array(body.matrix_world.inverted())
    loc=w@inv[:3,:3].T+inv[:3,3]
    me.vertices.foreach_set('co',loc.ravel()); me.update()
    me.calc_loop_triangles()
    it.name='ITEM_'+name; me.name='ITEM_'+name
    it['chaosx_working']=True; it['chaosx_export_approved']=True; it['chaosx_item']=name; it['chaosx_item_bone']=spec['bone']
    it.parent=arm; it.parent_type='OBJECT'; it.matrix_parent_inverse=body.matrix_parent_inverse.copy(); it.matrix_basis=body.matrix_basis.copy()
    vg=it.vertex_groups.new(name=spec['bone']); vg.add(list(range(len(me.vertices))),1.0,'REPLACE')
    for m in list(it.modifiers): it.modifiers.remove(m)
    md=it.modifiers.new('Armature','ARMATURE'); md.object=arm
    # material: clone of the body PDX material with the item's own packed maps
    base=body.material_slots[0].material
    mat=base.copy(); mat.name='Material_'+name
    imgs={}
    for key in ('diffuse','specular','normal'):
        img=bpy.data.images.load(R+CFG['tex_root'].format(name=spec.get('tex_name',name))+'/'+key+'.png',check_existing=False); img.name=f'{CFG["job"]}_{name}_{key}'; img.pack(); imgs[key]=img
    order=[n for n in mat.node_tree.nodes if n.type=='TEX_IMAGE']
    for n,key in zip(sorted(order,key=lambda n:n.name),('diffuse','specular','normal')):
        n.image=imgs[key]
    it.data.materials.clear(); it.data.materials.append(mat)
    rep[name]=dict(scale=s,length_world=spec['length'],hand_centroid=list(cen),palm_off=list(cen_local),axis_world=list(axis_w),verts=len(me.vertices),tris=len(me.polygons),
                   bbox=[list(w.min(0)),list(w.max(0))])
H.set_rest(arm,False); arm.animation_data.action=saved_action
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result=rep
