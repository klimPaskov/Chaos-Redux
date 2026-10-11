import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import uf
from uf import *
J=uf.jroot(CFG['job'])+"blender/checkpoints/"
bpy.ops.wm.open_mainfile(filepath=J+CFG['base'])
for o in bpy.data.objects:
    o['chaosx_working']=True; o['chaosx_export_approved']=True
arm=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]; body=[o for o in bpy.data.objects if o.type=='MESH' and o.name.startswith(CFG.get('body_prefix','char1'))][0]
bpy.context.scene.render.fps=CFG.get('fps',30)
arm.name='Armature.001'
got={}
for role,fn in CFG['roles'].items():
    with bpy.data.libraries.load(J+fn) as (src,dst): dst.actions=list(src.actions)
    a=dst.actions[0]; a.name='%s_%s'%(CFG['prefix'],role); a.use_fake_user=True; got[role]=[int(a.frame_range[0]),int(a.frame_range[1])]
bpy.ops.wm.save_as_mainfile(filepath=J+CFG['out'])
result={'actions':got,'arm':arm.name,'body':body.name}
