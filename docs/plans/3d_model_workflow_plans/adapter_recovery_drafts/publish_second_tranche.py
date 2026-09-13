from pathlib import Path
import ast
import hashlib
import json

root=Path(__file__).resolve().parent; repo=root.parents[3]; draft=root/'second_tranche'; base=repo/'.tools/3d_pipeline/adapter'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest().upper()
baseline=json.loads((draft/'baseline_hashes.json').read_text())
config_path=repo/'.tools/3d_pipeline/config/blender_hoi4_adapter.json'; lock_path=repo/'.tools/3d_pipeline/config/dependencies.lock.json'
config=json.loads(config_path.read_text()); lock=json.loads(lock_path.read_text()); route=lock['routes']['blender_hoi4_adapter']
if config['adapter_version']!='1.10.24' or route['version']!='1.10.24': raise SystemExit('Unexpected release version')
for rel,expected in route['source_sha256'].items():
    if sha(repo/rel)!=expected.upper(): raise SystemExit('Unreviewed dependency change: '+rel)
for file,expected in baseline.items():
    if sha(base/file)!=expected: raise SystemExit('Concurrent draft baseline change: '+file)
    ast.parse((draft/file).read_text())
if (base/'mesh_patch_repair.py').exists(): raise SystemExit('New module collision')
ast.parse((draft/'mesh_patch_repair.py').read_text())
if 'repair_explicit_mesh_patch' in config['operations']: raise SystemExit('Operation collision')
config['operations'].append('repair_explicit_mesh_patch'); config['adapter_version']='1.10.25'
for file in [*baseline,'mesh_patch_repair.py']: (base/file).write_bytes((draft/file).read_bytes())
config_path.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
route['version']='1.10.25'; route['operations']=list(config['operations'])
route['source_sha256']['.tools/3d_pipeline/adapter/mesh_patch_repair.py']=sha(base/'mesh_patch_repair.py')
for rel in route['source_sha256']: route['source_sha256'][rel]=sha(repo/rel)
lock_path.write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
result={path.relative_to(repo).as_posix():sha(path) for path in [*(base/f for f in [*baseline,'mesh_patch_repair.py']),config_path,lock_path]}
(draft/'published_hashes.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'version':route['version'],'operations':len(route['operations']),'hashes':result},indent=2))
