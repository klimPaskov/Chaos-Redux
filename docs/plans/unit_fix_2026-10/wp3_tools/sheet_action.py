import sys; sys.path.insert(0,r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.tmp/wp3_zombies")
import importlib, zv as z; importlib.reload(z)
import bpy
R=r"C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/"
J=R+"docs/assets/002_zombie_outbreak/models_3d/"+CFG['job']+"/blender/checkpoints/"
if CFG.get('open',True): bpy.ops.wm.open_mainfile(filepath=J+CFG.get('blend','wp3_02_actions.blend'))
body=bpy.data.objects["char1.001"]; arm=bpy.data.objects["Armature.001"]; me=body.data
name='UV_WP3' if 'UV_WP3' in me.uv_layers else 'UVMap'
me.uv_layers.active=me.uv_layers[name]; me.uv_layers[name].active_render=True
z.setup_world()
for o in bpy.data.objects:
    if o.name not in ('char1.001','Armature.001'): o.hide_render=True
z.preview_material(body, R+CFG['diffuse'])
act=bpy.data.actions[CFG['action']]
z.action_sheet(R+CFG['out'],arm,body,act,nframes=len(CFG['frames']),views=tuple(CFG.get('views',('front','right'))),frames=CFG['frames'])
