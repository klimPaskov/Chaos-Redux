from pathlib import Path
import ast,math,types,unittest
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/eighth_tranche');tree=ast.parse((p/'mesh_winding_repair.py').read_text());ns={'math':math};exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='_verify_normal_signs'],type_ignores=[]),'fixture','exec'),ns)
class T(unittest.TestCase):
 def run_case(self,wanted,actual,selected=False):
  ns['_corner_normals']=lambda m:{(1,1):actual};return ns['_verify_normal_signs'](None,{(1,1):tuple(-x if selected else x for x in wanted)},{1} if selected else set())
 def test_native_reported_quantization(self):
  for a,b in [((.1399991214,.9833890796,-.1155265346),(.1364198178,.9838997126,-.1154608130)),((-.735597848892,-.672088742256,.0848090648651),(-.735637545586,-.672343671322,.0824100002646))]:self.assertLess(self.run_case(a,b)['maximum_angle_degrees'],.25)
 def test_direction_mismatch_rejected(self):
  with self.assertRaises(RuntimeError):self.run_case((1,0,0),(0,1,0))
 def test_nonunit_source_direction(self):self.assertEqual(self.run_case((.02,0,0),(1,0,0))['source_nonunit_normal_count'],1)
 def test_zero_source_rejected(self):
  with self.assertRaises(RuntimeError):self.run_case((0,0,0),(1,0,0))
 def test_selected_flip(self):self.assertEqual(self.run_case((0,0,-1),(0,0,-1),True)['maximum_angle_degrees'],0)
unittest.main()
