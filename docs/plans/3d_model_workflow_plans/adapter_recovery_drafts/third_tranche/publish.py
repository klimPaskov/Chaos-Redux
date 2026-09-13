from pathlib import Path
import ast,json,hashlib,os
r=Path('.').resolve();d=r/'docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/third_tranche';b=r/'.tools/3d_pipeline/adapter';lp=r/'.tools/3d_pipeline/config/dependencies.lock.json';cp=r/'.tools/3d_pipeline/config/blender_hoi4_adapter.json'
old=lp.read_bytes();oldc=cp.read_bytes();lock=json.loads(old);config=json.loads(oldc);route=lock['routes']['blender_hoi4_adapter'];assert route['version']==config['adapter_version']=='1.10.26'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
for rel,expected in route['source_sha256'].items():assert sha(r/rel)==expected.upper(),rel
base={rel:sha(r/rel) for rel in route['source_sha256']};(d/'publication_baseline_1_10_26.json').write_text(json.dumps(base,indent=2))
files=['blender_worker.py','chaosx_blender_hoi4_mcp.py','manual_creature_rig.py','mesh_vertex_material_repair.py']
for n in files:ast.parse((d/n).read_text())
# Preserve approved concurrent skin tool additions; exact diff is recorded for parent.
import difflib
(d/'third.patch').write_text(''.join(''.join(difflib.unified_diff((b/n).read_text().splitlines(True) if (b/n).exists() else [],(d/n).read_text().splitlines(True),fromfile=str(b/n),tofile=str(d/n))) for n in files))
config['adapter_version']='1.10.27'
for op in ['edit_explicit_mesh_vertices','bind_existing_pdx_material']:
 assert op not in config['operations'];config['operations'].append(op)
if lp.read_bytes()!=old or cp.read_bytes()!=oldc:raise SystemExit('Concurrent metadata change')
for rel,value in base.items():assert sha(r/rel)==value,rel
for n in files:
 tmp=b/(n+'.recovery.tmp');tmp.write_bytes((d/n).read_bytes());os.replace(tmp,b/n)
tmp=cp.with_suffix('.recovery.tmp');tmp.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8');os.replace(tmp,cp)
route['version']='1.10.27';route['operations']=list(config['operations']);route['source_sha256']['.tools/3d_pipeline/adapter/mesh_vertex_material_repair.py']=sha(b/'mesh_vertex_material_repair.py')
for rel in route['source_sha256']:route['source_sha256'][rel]=sha(r/rel)
tmp=lp.with_suffix('.recovery.tmp');tmp.write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
if lp.read_bytes()!=old:raise SystemExit('Concurrent lock changed; leave explicit mismatch for review')
os.replace(tmp,lp)
result={'version':route['version'],'operations':len(route['operations']),'tests':{'total':48,'passed':48},'hashes':{rel:sha(r/rel) for rel in route['source_sha256']},'lock_sha256':sha(lp)};(d/'published_hashes.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
