import sys; sys.path.insert(0, r"<mod root>/.tmp/unitfix2")
import importlib, uf; importlib.reload(uf)
from uf import *
import holdtools as H
uf.open_ck(CFG['job'], CFG['src'])
arm=bpy.data.objects['Armature.001']; body=bpy.data.objects[CFG.get('body','char1.001')]
items=[bpy.data.objects[n] for n in CFG['items']]
uf.setup()
for o in bpy.data.objects:
    if o.type=='MESH' and o not in [body]+items: o.hide_render=True
P=R+".tmp/unitfix2/pv/"; paths=[]
for role,f in CFG['shots']:
    act=bpy.data.actions[CFG['job']+'_'+role]; z.set_action(arm,act); bpy.context.scene.frame_set(f)
    c=H.head(arm,'Hips'); 
    for v in CFG['views']:
        ctr=(c.x,c.y,c.z+CFG.get('up',0.8))
        if CFG.get('focus'):
            fh=H.head(arm,CFG['focus']); ctr=(fh.x,fh.y,fh.z)
        paths.append(uf.snap(P+"vp_%s_%d_%s.png"%(role,f,v),[body]+items,v,ctr,CFG.get('size',9.0),(CFG.get('res',360),CFG.get('res',360))))
z.sheet(paths,P+CFG['out'],cols=len(CFG['views']))
result={}
