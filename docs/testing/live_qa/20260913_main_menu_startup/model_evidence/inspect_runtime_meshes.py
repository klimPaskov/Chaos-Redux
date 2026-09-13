from pathlib import Path
import importlib.util, json, hashlib
root=Path.cwd()
module_path=Path(r'C:\Users\klimp\AppData\Roaming\Blender Foundation\Blender\5.1\extensions\user_default\io_pdx_mesh\pdx_data.py')
spec=importlib.util.spec_from_file_location('locked_pdx_data',module_path)
pdx=importlib.util.module_from_spec(spec); spec.loader.exec_module(pdx)
files=[root/'gfx/models/units'/folder/name for folder,name in [('autonomous_robot','autonomous_robot.mesh'),('alien_infantry','alien_infantry.mesh'),('012_africa_plague_carriers','chaosx_plague_carriers.mesh'),('chaosx_demonic_zombies','chaosx_demonic_zombies.mesh'),('xenobiological_assault_organism','xenobiological_assault_organism.mesh')]]
report=[]
for path in files:
 tree=pdx.read_meshfile(str(path)); objects=[]
 for group in tree:
  if group.tag!='object': continue
  for obj in group:
   bones=[]; streams=[]
   for child in obj:
    if child.tag=='skeleton':
     bones=[{'name':b.tag,'attrs':b.attrib} for b in child]
    if child.tag=='mesh':
     mat=child.find('material'); skin=child.find('skin')
     streams.append({'vertices':len(child.attrib.get('p',[]))//3,'triangles':len(child.attrib.get('tri',[]))//3,'material':mat.attrib if mat is not None else None,'skin_keys':list(skin.attrib) if skin is not None else None})
   objects.append({'name':obj.tag,'streams':streams,'bones':bones})
 report.append({'path':path.relative_to(root).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest().upper(),'objects':objects,'skeleton_nodes':sum(len(o['bones']) for o in objects),'stream_count':sum(len(o['streams']) for o in objects),'vertices':sum(s['vertices'] for o in objects for s in o['streams']),'triangles':sum(s['triangles'] for o in objects for s in o['streams'])})
output=root/'docs/testing/live_qa/20260913_main_menu_startup/model_evidence/baseline_mesh_structure.json'; output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k!='objects'} for r in report],indent=2))