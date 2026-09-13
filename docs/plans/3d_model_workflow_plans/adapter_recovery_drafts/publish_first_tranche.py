from pathlib import Path
import ast
import hashlib
import json

root=Path(__file__).resolve().parent
repo=root.parents[3]
base=repo/'.tools/3d_pipeline/adapter'
baseline=json.loads((root/'baseline_hashes.json').read_text())
for file,expected in baseline.items():
    if hashlib.sha256((base/file).read_bytes()).hexdigest().upper()!=expected:
        raise SystemExit('Concurrent baseline change: '+file)
    ast.parse((root/file).read_text())
config_path=repo/'.tools/3d_pipeline/config/blender_hoi4_adapter.json'
config=json.loads(config_path.read_text())
if config['adapter_version']!='1.10.23': raise SystemExit('Unexpected release baseline')
for operation in ('repair_explicit_mesh_winding','ground_existing_action'):
    if operation in config['operations']: raise SystemExit('Operation collision: '+operation)
    config['operations'].append(operation)
config['adapter_version']='1.10.24'
for file in baseline:
    (base/file).write_bytes((root/file).read_bytes())
config_path.write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
changed=[base/file for file in baseline]+[config_path]
result={path.relative_to(repo).as_posix():hashlib.sha256(path.read_bytes()).hexdigest().upper() for path in changed}
(root/'published_hashes.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
