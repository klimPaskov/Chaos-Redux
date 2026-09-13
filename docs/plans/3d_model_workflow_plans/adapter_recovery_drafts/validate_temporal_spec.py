import json
from pathlib import Path
from mesh_patch_repair import validate_patch

root=Path(__file__).resolve().parent; repo=root.parents[3]
evidence=repo/'docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/evidence/20260906_repair'
inventory=json.loads((evidence/'base_landmarks.json').read_text())
patch=json.loads((evidence/'inner_thigh_patch_spec.json').read_text())
flips=json.loads((evidence/'proposed_winding_flips.json').read_text())['flip_face_indices']
mesh=inventory['meshes'][patch['mesh_name']]
faces=[list(tri) for tri in mesh['triangles']]
for index in flips: faces[index].reverse()
bones={b['name'] for b in inventory['rigs'][patch['target_armature_name']]}
result=validate_patch(patch,[v['world'] for v in mesh['vertices']],faces,len(mesh['materials']),list(patch['replacement_triangles'][0]['loop_uvs']),bones)
print(json.dumps({'source_sha256':inventory['source_sha256'],'explicit_flips_required_first':len(flips),'removed_triangles':result['removed_triangles'],'added_triangles':result['added_triangles'],'new_vertices':len(result['new_vertices']),'status':'numeric_contract_pass_only_no_Blender_mutation'}))
