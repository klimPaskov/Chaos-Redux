from pathlib import Path
import sys,json
root=Path.cwd();sys.path.insert(0,str(root/'.tools/3d_pipeline'))
from blender_client import BlenderAdapterClient
p=root/'docs/testing/live_qa/20260913_main_menu_startup/model_evidence';args=json.loads((p/'alias_request_args.json').read_text())
r=BlenderAdapterClient(root).call('chaosx_blender_hoi4_collapse_identity_leaf_joints',args)
(p/'alias_operation_result.json').write_bytes((json.dumps(r,indent=2)+'\n').encode())
print(json.dumps({k:r[k] for k in ['status','bones_before','bones_after','maximum_alias_skin_matrix_error','evaluated_action_proofs','checkpoint','checkpoint_sha256','adapter']}))