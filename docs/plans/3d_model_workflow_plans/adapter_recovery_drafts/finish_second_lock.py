from pathlib import Path
import hashlib,json,os
root=Path(__file__).resolve().parent; repo=root.parents[3]; base=repo/'.tools/3d_pipeline/adapter'; draft=root/'second_tranche'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest().upper()
config_path=repo/'.tools/3d_pipeline/config/blender_hoi4_adapter.json'; lock_path=repo/'.tools/3d_pipeline/config/dependencies.lock.json'
old=lock_path.read_bytes(); lock=json.loads(old); config=json.loads(config_path.read_text()); route=lock['routes']['blender_hoi4_adapter']
assert route['version']=='1.10.24' and config['adapter_version']=='1.10.25'
changed={'.tools/3d_pipeline/adapter/'+f for f in ['blender_worker.py','chaosx_blender_hoi4_mcp.py','manual_creature_rig.py','mesh_patch_repair.py']}
for rel,expected in route['source_sha256'].items():
    if rel not in changed and rel!='.tools/3d_pipeline/config/blender_hoi4_adapter.json' and sha(repo/rel)!=expected.upper(): raise SystemExit('Concurrent unrelated change: '+rel)
for rel in changed:
    if sha(repo/rel)!=sha(draft/Path(rel).name): raise SystemExit('Published source differs from reviewed draft: '+rel)
route['version']='1.10.25'; route['operations']=config['operations']; route['source_sha256']['.tools/3d_pipeline/adapter/mesh_patch_repair.py']=sha(base/'mesh_patch_repair.py')
for rel in route['source_sha256']: route['source_sha256'][rel]=sha(repo/rel)
temp=lock_path.with_name('dependencies.recovery_1_10_25.tmp')
with temp.open('x',encoding='utf-8',newline='\n') as handle: handle.write(json.dumps(lock,indent=2)+'\n')
if lock_path.read_bytes()!=old: raise SystemExit('Lock changed before atomic publication')
os.replace(temp,lock_path)
result={rel:sha(repo/rel) for rel in sorted(changed|{config_path.relative_to(repo).as_posix(),lock_path.relative_to(repo).as_posix()})}
(draft/'published_hashes.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'version':route['version'],'operations':len(route['operations']),'hashes':result},indent=2))
