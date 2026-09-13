from pathlib import Path
import importlib.util,json,hashlib,collections
root=Path.cwd(); p=Path(r'C:\Users\klimp\AppData\Roaming\Blender Foundation\Blender\5.1\extensions\user_default\io_pdx_mesh\pdx_data.py'); s=importlib.util.spec_from_file_location('pdx',p); m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
t=m.read_meshfile(str(root/'gfx/models/units/alien_infantry/alien_infantry.mesh'))
rows=[]
for o in t.find('object'):
 skeleton=o.find('skeleton'); bones=list(skeleton)
 usage=collections.Counter(); weight=collections.Counter()
 for mesh in o.findall('mesh'):
  skin=mesh.find('skin')
  print(o.tag,'skin array fields',{k:len(v) for k,v in skin.attrib.items()})
  for ix,w in zip(skin.attrib['ix'],skin.attrib['w']):
   if w>0:
    usage[ix]+=1;weight[ix]+=w
 row={'object':o.tag,'bones':[{'name':b.tag,'index':i,'parent':b.attrib.get('pa'),'weighted_entries':usage[i],'total_weight':weight[i]} for i,b in enumerate(bones)]};rows.append(row)
output=root/'docs/testing/live_qa/20260913_main_menu_startup/model_evidence/alien_bone_usage.json';output.write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))