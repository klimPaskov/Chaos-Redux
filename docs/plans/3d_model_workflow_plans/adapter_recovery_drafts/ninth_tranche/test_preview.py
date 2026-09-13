from pathlib import Path
import ast,math,unittest
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/ninth_tranche');tree=ast.parse((p/'blender_worker.py').read_text());n=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='validate_preview_region');ns={'math':math};exec(compile(ast.Module(body=[n],type_ignores=[]),'fixture','exec'),ns)
class T(unittest.TestCase):
 def test_exact_roi(self):self.assertEqual(ns['validate_preview_region']({'min':[-1,-2,4],'max':[1,1,7]},1024)['max'],[1,1,7])
 def test_invalid_bounds_and_resolution(self):
  for region,res in [({'min':[0,0,0],'max':[0,1,1]},1024),({'min':[0,0,float('nan')],'max':[1,1,1]},1024),(None,4096),(None,True),({'min':[0,0,0],'max':[1,1,1],'code':'x'},512)]:
   with self.assertRaises(ValueError):ns['validate_preview_region'](region,res)
 def test_horizontal_sphere_inside_actual_fov(self):
  radius=math.sqrt(10**2+2**2+1**2)/2;angle=math.radians(35);distance=radius/(math.sin(angle/2)*.78);self.assertLess(math.asin(radius/distance),angle/2)
 def test_stage_sources_parse(self):
  for name in ['blender_worker.py','chaosx_blender_hoi4_mcp.py','manual_creature_rig.py','mesh_winding_repair.py','blender_client.py']:ast.parse((p/name).read_text())
unittest.main()
