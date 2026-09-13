from pathlib import Path
import hashlib,json,os
root=Path.cwd(); draft=root/'docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/motion_retarget'
lockpath=root/'.tools/3d_pipeline/config/dependencies.lock.json'; lock=json.loads(lockpath.read_text(encoding='utf-8-sig'))
meshy=json.dumps(lock['routes']['meshy_mcp'],sort_keys=True)
for name in ('blender_worker.py','chaosx_blender_hoi4_mcp.py','retarget_root_motion.py'):
    data=(draft/name).read_text(encoding='utf-8-sig'); compile(data,name,'exec')
    (root/'.tools/3d_pipeline/adapter'/name).write_bytes(data.encode('utf-8'))
(root/'.tools/3d_pipeline/tests/test_animation_retarget.py').write_bytes((draft/'test_animation_retarget.py').read_text(encoding='utf-8-sig').encode('utf-8'))
cp=root/'.tools/3d_pipeline/config/blender_hoi4_adapter.json'; config=json.loads(cp.read_text(encoding='utf-8-sig'))
config['adapter_version']='1.10.41'
if 'inspect_animation_source' not in config['operations']:config['operations'].append('inspect_animation_source')
cp.write_bytes((json.dumps(config,indent=2)+'\n').encode('utf-8'))
# Re-read the latest lock, preserving the independently committed Meshy branch.
lock=json.loads(lockpath.read_text(encoding='utf-8-sig'))
assert json.dumps(lock['routes']['meshy_mcp'],sort_keys=True)==meshy
route=lock['routes']['blender_hoi4_adapter']; route['version']='1.10.41'; route['operations']=config['operations']
route['source_sha256']['.tools/3d_pipeline/adapter/retarget_root_motion.py']=''
for rel in route['source_sha256']:route['source_sha256'][rel]=hashlib.sha256((root/rel).read_bytes()).hexdigest().upper()
tmp=lockpath.with_suffix('.json.adapter_tmp'); tmp.write_bytes((json.dumps(lock,indent=2)+'\n').encode('utf-8')); os.replace(str(tmp),str(lockpath))
print('Published',route['version'],len(route['operations']),'operations; lock',hashlib.sha256(lockpath.read_bytes()).hexdigest().upper())
