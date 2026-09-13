import ast,sys,unittest,types,math,hashlib,json,tempfile
from pathlib import Path
p=Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/third_tranche').resolve();sys.path.insert(0,str(p));sys.path.insert(1,str(p.parent));sys.path.insert(2,str(Path('.tools/3d_pipeline/tests').resolve()))
import mesh_vertex_material_repair as m
import test_vertex_repair as vr
import test_mesh_patch_repair as mp
import test_manual_creature_rig_contract as mr
import test_reimport_promotion_contract as pr
pr.WORKER=p/'blender_worker.py'
tree=ast.parse((p/'blender_worker.py').read_text());node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_promotion_image_record')
ns={'Path':Path,'hashlib':hashlib,'math':math,'_promotion_value':lambda x:x,'_promotion_properties':lambda x:{},'file_sha256':lambda p:hashlib.sha256(p.read_bytes()).hexdigest(),'bpy':types.SimpleNamespace(path=types.SimpleNamespace(abspath=lambda x:x))};exec(compile(ast.Module(body=[node],type_ignores=[]),'fixture','exec'),ns)
class Extra(unittest.TestCase):
 def image(self,**kw):
  args=dict(packed_files=[],filepath='',source='GENERATED',has_data=True,size=[1,1],channels=4,pixels=[.2,.3,.4,1],alpha_mode='STRAIGHT',colorspace_settings=types.SimpleNamespace(name='sRGB'));args.update(kw);return types.SimpleNamespace(**args)
 def test_pixel_hash_and_settings(self):
  a=ns['_promotion_image_record'](Path('.').resolve(),self.image());b=ns['_promotion_image_record'](Path('.').resolve(),self.image(pixels=[.3,.3,.4,1]));self.assertNotEqual(a['pixel_sha256'],b['pixel_sha256']);self.assertEqual(a['source'],'GENERATED')
 def test_empty_invalid_pixels_rejected(self):
  for kw in ({'pixels':[float('nan'),0,0,1]},{'has_data':False},{'source':'MOVIE'},{'size':[5000,5000]},{'pixels':[]}):
   with self.assertRaises(ValueError):ns['_promotion_image_record'](Path('.').resolve(),self.image(**kw))
 def test_nonempty_external_and_missing_paths_rejected(self):
  for path in ('C:/outside.png',str(Path('.').resolve()/'missing.png')):
   with self.assertRaises(ValueError):ns['_promotion_image_record'](Path('.').resolve(),self.image(filepath=path))
 def test_requested_readback(self):
  row={'world_position':[1,2,3],'weights':[{'bone':'Hand','weight':1}]};m.verify_requested_vertex(row,[1+1e-7,2,3],{'Hand':1-1e-8})
  for pos,w in (([2,2,3],{'Hand':1}),([1,2,3],{'Hand':.9}),([1,2,3],{'Hand':1,'Root':0})):
   with self.assertRaises(RuntimeError):m.verify_requested_vertex(row,pos,w)
 def test_non_deform_excluded(self):
  with self.assertRaises(ValueError):m.validate_vertex_edits([{'index':0,'weights':[{'bone':'Control','weight':1}]}],1,{'Hand'},{'Control','Hand'})
suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromModule(x) for x in [vr,mp,mr,pr]);suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Extra));result=unittest.TextTestRunner(verbosity=1).run(suite);sys.exit(not result.wasSuccessful())
