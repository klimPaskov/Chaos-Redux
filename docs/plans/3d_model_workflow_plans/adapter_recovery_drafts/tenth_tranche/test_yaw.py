import sys,unittest,copy
from pathlib import Path
sys.path.insert(0,str(Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche').resolve()));sys.path.insert(1,str(Path('.tools/3d_pipeline/adapter').resolve()))
from assembly_yaw import validate_yaw
class T(unittest.TestCase):
 def setUp(self):self.p={'yaw_degrees':90,'object_names':['Rig','Body'],'action_names':['Idle','Move'],'target_armature_name':'Rig'}
 def test_exact_cardinal_yaw(self):self.assertEqual(validate_yaw(self.p),90)
 def test_unbounded_noncardinal_rejected(self):
  for angle in [True,float('nan'),360,45,0]:
   p=copy.deepcopy(self.p);p['yaw_degrees']=angle
   with self.assertRaises(ValueError):validate_yaw(p)
 def test_explicit_rig_and_unique_objects_required(self):
  for objects in [['Body'],['Rig','Rig'],[]]:
   p=copy.deepcopy(self.p);p['object_names']=objects
   with self.assertRaises(ValueError):validate_yaw(p)
unittest.main()
