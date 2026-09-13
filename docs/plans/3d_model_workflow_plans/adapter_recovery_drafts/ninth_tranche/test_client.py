from pathlib import Path
import sys,importlib.util,unittest
sys.path.insert(0,str(Path('.tools/3d_pipeline').resolve()));p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/ninth_tranche/blender_client.py');spec=importlib.util.spec_from_file_location('candidate_client',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class T(unittest.TestCase):
 def client(self):
  x=m.BlenderAdapterClient.__new__(m.BlenderAdapterClient);x.repo_root=Path('.');x.wrapper=Path('unused.cmd');x._matching_mutation_receipts=lambda t,a:[{'request_id':'saved_first'}];return x
 def test_uncertain_mutation_never_replayed(self):
  calls=[]
  def call(*a,**kw):calls.append(kw);raise m.MCPRouteError('response_lost')
  m.call_stdio=call
  with self.assertRaisesRegex(m.MCPRouteError,'saved_first'):self.client().call('chaosx_blender_hoi4_bind_existing_pdx_material',{'job_id':'fixture'})
  self.assertEqual(len(calls),1)
 def test_read_only_retry_allowed(self):
  calls=[]
  def call(*a,**kw):
   calls.append(kw)
   if len(calls)==1:raise m.MCPRouteError('read_lost')
   return {'structuredContent':{'ok':True}}
  m.call_stdio=call;self.assertEqual(self.client().call('chaosx_blender_hoi4_health',{'job_id':'fixture'}),{'ok':True});self.assertEqual(len(calls),2)
unittest.main()
