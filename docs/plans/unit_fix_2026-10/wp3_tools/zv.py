import bpy, math, os, json
from mathutils import Vector, Matrix, Quaternion, Euler

def body_objs():
    return [o for o in bpy.data.objects if o.type=='MESH' and any(m.type=='ARMATURE' for m in o.modifiers)]

def setup_world():
    sc=bpy.context.scene
    sc.render.engine='BLENDER_WORKBENCH'
    sh=sc.display.shading
    sh.light='STUDIO'; sh.color_type='TEXTURE'; sh.show_cavity=False
    sc.render.resolution_x=640; sc.render.resolution_y=800
    sc.render.film_transparent=False
    w=bpy.data.worlds[0] if bpy.data.worlds else bpy.data.worlds.new('w')
    sc.world=w
    w.color=(0.35,0.37,0.4)

def preview_material(obj, diffuse_path):
    """Temp preview material per slot using the given diffuse image (render only)."""
    img=bpy.data.images.load(diffuse_path, check_existing=True)
    mat=bpy.data.materials.get('PREVIEW_TMP') or bpy.data.materials.new('PREVIEW_TMP')
    mat.use_nodes=True
    nt=mat.node_tree
    for n in list(nt.nodes): nt.nodes.remove(n)
    out=nt.nodes.new('ShaderNodeOutputMaterial'); bsdf=nt.nodes.new('ShaderNodeBsdfPrincipled'); tex=nt.nodes.new('ShaderNodeTexImage')
    tex.image=img; nt.links.new(tex.outputs['Color'],bsdf.inputs['Base Color']); nt.links.new(bsdf.outputs['BSDF'],out.inputs['Surface'])
    nt.nodes.active=tex
    saved=[]
    for i,s in enumerate(obj.material_slots):
        saved.append(s.material); s.material=mat
    return saved

def restore_material(obj, saved):
    for s,m in zip(obj.material_slots,saved): s.material=m

def bounds(objs):
    mn=Vector((1e9,)*3); mx=Vector((-1e9,)*3)
    dg=bpy.context.evaluated_depsgraph_get()
    for o in objs:
        eo=o.evaluated_get(dg); me=eo.to_mesh()
        for v in me.vertices:
            w=o.matrix_world@v.co
            mn=Vector((min(mn[i],w[i]) for i in range(3))); mx=Vector((max(mx[i],w[i]) for i in range(3)))
        eo.to_mesh_clear()
    return mn,mx

def shot(path, objs, view='front', center=None, dist=None, size=None, ortho=True):
    sc=bpy.context.scene
    cam=bpy.data.objects.get('PV_CAM')
    if not cam:
        cd=bpy.data.cameras.new('PV_CAM'); cam=bpy.data.objects.new('PV_CAM',cd); sc.collection.objects.link(cam)
    sc.camera=cam
    mn,mx=bounds(objs)
    c=center or (mn+mx)/2
    h=max(mx.z-mn.z,0.1) if size is None else size
    cam.data.type='ORTHO'; cam.data.ortho_scale=h*1.15
    d=20.0
    dirs={'front':(0,-1,0),'back':(0,1,0),'left':(-1,0,0),'right':(1,0,0),'quarter':(-0.7,-0.7,0.35),'top':(0,-0.01,1)}
    v=Vector(dirs[view]).normalized()
    cam.location=c+v*d
    cam.rotation_euler=(-v).to_track_quat('-Z','Y').to_euler()
    cam.data.clip_end=200
    sc.render.filepath=path
    bpy.ops.render.render(write_still=True)
    return path

def sheet(paths, out, cols=None):
    import numpy as np
    ims=[bpy.data.images.load(p,check_existing=False) for p in paths]
    w,h=ims[0].size
    cols=cols or len(ims)
    rows=(len(ims)+cols-1)//cols
    big=np.zeros((h*rows,w*cols,4),dtype=np.float32)
    for k,im in enumerate(ims):
        a=np.array(im.pixels[:],dtype=np.float32).reshape(h,w,4)
        r,c=divmod(k,cols)
        big[(rows-1-r)*h:(rows-r)*h, c*w:(c+1)*w]=a
    o=bpy.data.images.new('sheet_tmp',w*cols,h*rows,alpha=True)
    o.pixels=big.ravel().tolist(); o.filepath_raw=out; o.file_format='PNG'; o.save()
    for im in ims: bpy.data.images.remove(im)
    bpy.data.images.remove(o)
    return out

# ---------------- action review ----------------
import numpy as np
def set_action(arm, act):
    arm.animation_data_create(); arm.animation_data.action = act
    if act.slots:
        for sl in act.slots:
            if sl.identifier == 'OB'+arm.name: arm.animation_data.action_slot = sl; break
        else: arm.animation_data.action_slot = act.slots[0]

def joint_track(arm, act, frames=None, step=1):
    set_action(arm, act)
    f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    frames = frames or list(range(f0, f1+1, step))
    names = [b.name for b in arm.pose.bones]
    out = np.zeros((len(frames), len(names), 3)); Q = np.zeros((len(frames), len(names), 4))
    for i, f in enumerate(frames):
        bpy.context.scene.frame_set(f)
        for j, pb in enumerate(arm.pose.bones):
            m = arm.matrix_world @ pb.matrix
            out[i, j] = m.translation; q = m.to_quaternion(); Q[i, j] = (q.w, q.x, q.y, q.z)
    global LAST_Q
    LAST_Q = Q
    return frames, names, out

def mesh_floor(body, frames):
    dg = bpy.context.evaluated_depsgraph_get(); res = []
    for f in frames:
        bpy.context.scene.frame_set(f); dg.update()
        eo = body.evaluated_get(dg); me = eo.to_mesh()
        co = np.empty(len(me.vertices)*3); me.vertices.foreach_get('co', co); co = co.reshape(-1,3)
        w = np.array(body.matrix_world)[:3,:3]; t = np.array(body.matrix_world)[:3,3]
        wc = co@w.T+t
        res.append((wc[:,2].min(), wc[:,2].max(), wc[:,0].min(), wc[:,0].max(), wc[:,1].min(), wc[:,1].max()))
        eo.to_mesh_clear()
    return np.array(res)

def action_summary(arm, body, act, step=1):
    fr, names, J = joint_track(arm, act, step=step)
    d = np.linalg.norm(np.diff(J, axis=0), axis=2)   # (n-1, bones)
    i, j = np.unravel_index(d.argmax(), d.shape)
    hips = names.index('Hips') if 'Hips' in names else 0
    return dict(action=act.name, frames=len(fr), max_step=float(d.max()), at=(fr[i+1], names[j]),
                hips_travel_xy=float(np.linalg.norm(J[:,hips,:2]-J[0,hips,:2],axis=1).max()), hips_z=(float(J[:,hips,2].min()), float(J[:,hips,2].max())),
                seam=float(np.linalg.norm(J[-1]-J[0],axis=1).max()), steps_gt_041=int((d>0.41).sum()))

def action_sheet(path, arm, body, act, nframes=8, views=('front','right'), size=None, frames=None, tex=None):
    f0, f1 = int(act.frame_range[0]), int(act.frame_range[1])
    frames = frames or [int(round(f0 + (f1-f0)*k/(nframes-1))) for k in range(nframes)]
    set_action(arm, act)
    tmp = []
    mn, mx = bounds([body]) if False else (None, None)
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y = 300, 375
    for v in views:
        for k, f in enumerate(frames):
            sc.frame_set(f)
            p = path.replace('.png', f'_{v}_{k}.png')
            shot(p, [body], v, center=Vector((0, 0, 3.6)), size=size or 8.0)
            tmp.append(p)
    return sheet(tmp, path, cols=len(frames))
