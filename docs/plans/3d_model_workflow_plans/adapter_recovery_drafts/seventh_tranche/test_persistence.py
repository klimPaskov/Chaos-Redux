from pathlib import Path
import sys,tempfile,types,unittest,hashlib
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/seventh_tranche').resolve();sys.path.insert(0,str(p));sys.path.insert(1,str(Path('.tools/3d_pipeline/adapter').resolve()));import mesh_vertex_material_repair as m
class Test(unittest.TestCase):
 def run_case(self,drift):
  with tempfile.TemporaryDirectory() as td:
   job=Path(td);src=job/'a.blend';src.write_bytes(b'source');out=job/'b.blend';state={'updated':False,'reopened':False}
   def update():state['updated']=True
   def opening(**kw):state['reopened']=True
   def fingerprint(*args,**kw):
    value='fresh' if state['updated'] else 'stale'
    if drift and state['reopened']:value='changed'
    return {'sha256':{'objects':value},'sections':{'objects':{'Mesh':{'dimensions':value}},'images':{}}}
   h={'bpy':types.SimpleNamespace(context=types.SimpleNamespace(view_layer=types.SimpleNamespace(update=update)),ops=types.SimpleNamespace(wm=types.SimpleNamespace(open_mainfile=opening))),'_promotion_fingerprint':fingerprint,'save_blend':lambda p:p.write_bytes(b'fixture'),'file_sha256':lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()}
   return m.finish_verified({'payload':{'expected_source_sha256':h['file_sha256'](src)}},h,job,src,out,{})
 def test_lazy_bounds_flushed_before_persistence(self):self.assertTrue(self.run_case(False)['save_reopen_proof']['passed'])
 def test_real_object_drift_rejected_with_field(self):
  with self.assertRaisesRegex(RuntimeError,'dimensions'):self.run_case(True)
unittest.main()
