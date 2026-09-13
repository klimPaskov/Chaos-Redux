from pathlib import Path
import json,sys,hashlib,subprocess,ast
root=Path.cwd();base=root/'.tools/3d_pipeline';sys.path.insert(0,str(base))
from lib.mcp_stdio import call_stdio
from blender_client import BlenderAdapterClient
lock=json.loads((base/'config/dependencies.lock.json').read_text());cfg=json.loads((base/'config/blender_hoi4_adapter.json').read_text());route=lock['routes']['blender_hoi4_adapter']
assert cfg['adapter_version']==route['version']=='1.10.49' and cfg['operations']==route['operations']
checks=[]
for rel,expected in route['source_sha256'].items():
 path=root/rel;actual=hashlib.sha256(path.read_bytes()).hexdigest().upper()
 raw=subprocess.check_output(['git','hash-object','--no-filters',str(path)],cwd=root).strip().decode();canonical=subprocess.check_output(['git','hash-object','--path='+rel,str(path)],cwd=root).strip().decode()
 checks.append({'path':rel,'expected':expected,'actual':actual,'matches':expected==actual,'canonical_bytes_match':raw==canonical})
assert all(c['matches'] and c['canonical_bytes_match'] for c in checks)
wrapper=base/'wrappers/run_blender_hoi4_adapter.cmd';schema=call_stdio(['cmd.exe','/d','/c','call',str(wrapper)],list_tools=True,cwd=root,timeout_seconds=60)
assert len(schema['tools'])==52 and any(t['name']=='chaosx_blender_hoi4_collapse_identity_leaf_joints' for t in schema['tools'])
client=BlenderAdapterClient(root);health=client.health('alien_infantry');assert health['adapter']['version']=='1.10.49'
evidence=root/'docs/testing/live_qa/20260913_main_menu_startup/model_evidence'
(evidence/'adapter_1_10_49_preflight.json').write_bytes((json.dumps({'version':route['version'],'checks':checks,'schema':schema,'health':health},indent=2)+'\n').encode())
args=json.loads((evidence/'alias_request_args.json').read_text());args['bone_aliases']={'RightLittle3':'RightLittle2'};args['checkpoint_rel']=args['checkpoint_rel'].replace('33_startup_identity_leaf_alias','rejected_nonidentity_leaf_probe')
try:
 client.call('chaosx_blender_hoi4_collapse_identity_leaf_joints',args)
 raise AssertionError('Nonidentity leaf was incorrectly accepted.')
except RuntimeError as exc:
 rejection=str(exc)
 assert 'Blender worker failed' in rejection,rejection
(evidence/'nonidentity_leaf_rejection.json').write_bytes((json.dumps({'expected_rejection':rejection,'source_sha256':hashlib.sha256((root/'docs/assets/016_brilliant_scientist/models_3d/alien_infantry'/args['blend_rel']).read_bytes()).hexdigest().upper()},indent=2)+'\n').encode())
print(json.dumps({'preflight':'pass','version':route['version'],'operation_count':len(schema['tools']),'negative_probe':rejection}))