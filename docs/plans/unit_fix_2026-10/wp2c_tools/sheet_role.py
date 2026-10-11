import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf; importlib.reload(uf)
from uf import *
import holdtools as H
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects[CFG.get('body','char1.001')]
items=[bpy.data.objects[n] for n in CFG.get('items',[])]
uf.setup()
for o in bpy.data.objects:
    if o.type=='MESH' and o not in [body]+items: o.hide_render=True
act=bpy.data.actions[CFG['prefix']+'_'+CFG['role']]; z.set_action(arm,act); f0,f1=int(act.frame_range[0]),int(act.frame_range[1])
frames=CFG.get('frames') or [int(round(f0+(f1-f0)*k/(CFG.get('n',10)-1))) for k in range(CFG.get('n',10))]
P=R+".tmp/unitfix2/pv/"; paths=[]
for v in CFG.get('views',['left']):
    for f in frames:
        bpy.context.scene.frame_set(f); c=H.head(arm,'Hips')
        paths.append(uf.snap(P+"sr_%s_%d.png"%(v,f),[body]+items,v,(c.x,c.y,c.z+CFG.get('up',0.5)),CFG.get('size',9.0),(CFG.get('res',220),CFG.get('res',220))))
z.sheet(paths,P+CFG['out'],cols=len(frames))
result={'frames':frames}
