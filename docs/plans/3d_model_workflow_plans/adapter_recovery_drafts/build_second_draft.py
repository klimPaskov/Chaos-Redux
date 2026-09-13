from pathlib import Path
import ast
import difflib
import hashlib
import json

root=Path(__file__).resolve().parent; repo=root.parents[3]; base=repo/'.tools/3d_pipeline/adapter'
files={f:(base/f).read_text(encoding='utf-8-sig') for f in ['blender_worker.py','chaosx_blender_hoi4_mcp.py','manual_creature_rig.py']}
original=dict(files)
old='    if operation in {"inspect_mesh_winding", "repair_mesh_winding"}:'
new='''    if operation == "repair_explicit_mesh_patch":
        from mesh_patch_repair import repair_explicit_mesh_patch
        return repair_explicit_mesh_patch(req, globals())
'''+old
assert files['blender_worker.py'].count(old)==1
files['blender_worker.py']=files['blender_worker.py'].replace(old,new)
tool='''
@mcp.tool()
def chaosx_blender_hoi4_repair_explicit_mesh_patch(job_id: str, blend_rel: str, checkpoint_rel: str, expected_source_sha256: str, patch_spec: Dict[str, Any]) -> Dict[str, Any]:
    """Apply an exact reviewed local face/vertex patch; no inferred fill, rig replacement or source overwrite."""
    return _run(job_id,"repair_explicit_mesh_patch",{"blend_rel":blend_rel,"checkpoint_rel":checkpoint_rel,"expected_source_sha256":expected_source_sha256,"patch_spec":patch_spec})

'''
assert 'def chaosx_blender_hoi4_repair_explicit_mesh_patch(' not in files['chaosx_blender_hoi4_mcp.py']
files['chaosx_blender_hoi4_mcp.py']=files['chaosx_blender_hoi4_mcp.py'].replace('\ndef main() -> None:',tool+'\ndef main() -> None:')
old='"triangles":[list(f.vertices) for f in obj.data.polygons],"materials":[m.name if m else None for m in obj.data.materials]'
new='''"triangles":[list(f.vertices) for f in obj.data.polygons],"materials":[m.name if m else None for m in obj.data.materials],"vertex_groups":[g.name for g in obj.vertex_groups],"vertex_weights":[[{"group":g.group,"bone":obj.vertex_groups[g.group].name,"weight":g.weight} for g in v.groups] for v in obj.data.vertices],"triangle_material_indices":[f.material_index for f in obj.data.polygons],"triangle_loop_uvs":{u.name:[[list(u.data[i].uv) for i in f.loop_indices] for f in obj.data.polygons] for u in obj.data.uv_layers},"triangle_normals_local":[list(f.normal) for f in obj.data.polygons],"triangle_corner_normals_local":[[list(obj.data.corner_normals[i].vector) for i in f.loop_indices] for f in obj.data.polygons],"normal_local_to_world":[list(r) for r in obj.matrix_world.inverted().transposed().to_3x3()]'''
assert files['manual_creature_rig.py'].count(old)==1
files['manual_creature_rig.py']=files['manual_creature_rig.py'].replace(old,new)
draft=root/'second_tranche'; draft.mkdir(exist_ok=True)
diff=[]
for filename,text in files.items():
    ast.parse(text); (draft/filename).write_text(text,encoding='utf-8')
    diff.extend(difflib.unified_diff(original[filename].splitlines(True),text.splitlines(True),fromfile='a/.tools/3d_pipeline/adapter/'+filename,tofile='b/.tools/3d_pipeline/adapter/'+filename))
module=(root/'mesh_patch_repair.py').read_text(); ast.parse(module)
(draft/'mesh_patch_repair.py').write_text(module,encoding='utf-8')
diff.extend(difflib.unified_diff([],module.splitlines(True),fromfile='/dev/null',tofile='b/.tools/3d_pipeline/adapter/mesh_patch_repair.py'))
(draft/'second.patch').write_text(''.join(diff),encoding='utf-8')
(draft/'baseline_hashes.json').write_text(json.dumps({f:hashlib.sha256((base/f).read_bytes()).hexdigest().upper() for f in files},indent=2)+'\n',encoding='utf-8')
print('Second-tranche patch is draft-only; exact geometry patch + additive read-only authoritative inventory.')
