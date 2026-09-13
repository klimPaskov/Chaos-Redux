from pathlib import Path
import ast,math,struct,unittest
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche')
ns={'math':math}
for file,name in [('mesh_winding_repair.py','_verify_normal_signs'),('manual_creature_rig.py','validate_component_dds')]:
 tree=ast.parse((p/file).read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name==name],type_ignores=[]),'fixture','exec'),ns)
class T(unittest.TestCase):
 def test_actual_gorilla_default_reject_explicit_pass(self):
  ns['_corner_normals']=lambda mesh:{(1565,913):(.57549489,.81774521,.00991349)}
  original={(1565,913):(.57055509,.82110113,.01611498)}
  with self.assertRaises(RuntimeError):ns['_verify_normal_signs'](None,original,set())
  proof=ns['_verify_normal_signs'](None,original,set(),angular_tolerance_degrees=.5)
  self.assertGreater(proof['maximum_angle_degrees'],.49);self.assertFalse(proof['worst_corner']['selected_face'])
 def test_actual_robot_remap_encoding(self):
  ns['_corner_normals']=lambda mesh:{(25653,7901):(.15955687,.65305221,-.74031383)}
  source={(25653,7901):(.16119699,.65631938,-.73706198)}
  with self.assertRaises(RuntimeError):ns['_verify_normal_signs'](None,source,set())
  self.assertLess(ns['_verify_normal_signs'](None,source,set(),angular_tolerance_degrees=.5)['maximum_angle_degrees'],.3)
 def test_dds_2048_only_explicit_budget(self):
  h=bytearray(128);h[:4]=b'DDS ';struct.pack_into('<I',h,4,124);struct.pack_into('<II',h,12,2048,2048);struct.pack_into('<I',h,76,32);struct.pack_into('<I4sIIIII',h,80,0x41,b'\0'*4,32,0x00ff0000,0x0000ff00,0x000000ff,0xff000000)
  with self.assertRaises(ValueError):ns['validate_component_dds'](h,128+2048*2048*4)
  self.assertEqual(ns['validate_component_dds'](h,128+2048*2048*4,max_dimension=2048),(2048,2048))
  with self.assertRaises(ValueError):ns['validate_component_dds'](h,128+2048*2048*4-1,max_dimension=2048)
 def test_modules_parse(self):
  for f in p.glob('*.py'):ast.parse(f.read_text())
unittest.main()
