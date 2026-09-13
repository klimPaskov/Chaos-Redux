import ast, math, types, unittest
from pathlib import Path
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/sixth_tranche')
tree=ast.parse(Path('.tools/3d_pipeline/adapter/mesh_winding_repair.py').read_text());nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in {'_corner_normals','_verify_normal_signs'}];ns={'math':math};exec(compile(ast.Module(body=nodes,type_ignores=[]),'fixture','exec'),ns)
class Tests(unittest.TestCase):
 def mesh(self,normals):return types.SimpleNamespace(polygons=[types.SimpleNamespace(index=0,loop_indices=[0,1,2]),types.SimpleNamespace(index=1,loop_indices=[3,4,5])],loops=[types.SimpleNamespace(vertex_index=i) for i in [2,1,0,3,4,5]],corner_normals=[types.SimpleNamespace(vector=n) for n in normals])
 def test_selected_sign_and_unaffected_preserved(self):
  original={(0,i):(0,0,1) for i in [0,1,2]};original.update({(1,i):(0,1,0) for i in [3,4,5]});proof=ns['_verify_normal_signs'](self.mesh([(0,0,-1)]*3+[(0,1,0)]*3),original,{0});self.assertEqual(proof['maximum_vector_error'],0)
  for normals in ([(0,0,1)]*3+[(0,1,0)]*3,[(0,0,-1)]*3+[(0,0,1)]*3):
   with self.assertRaises(RuntimeError):ns['_verify_normal_signs'](self.mesh(normals),original,{0})
 def test_staged_contract(self):
  s=(p/'manual_creature_rig.py').read_text();ast.parse(s);f=s[s.index('def repair_explicit_mesh_winding'):s.index('def _root_vertical_contact')];self.assertNotIn('[(0,0,0)]*len(mesh.loops)',f);self.assertIn('reopened_normal_sign_proof',f);self.assertIn('corners[u.name][f.index][mesh.loops[i].vertex_index]',f)
unittest.main()
