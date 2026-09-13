"""Release evidence: operation parity, immutable locked bytes, and local import closure."""
from pathlib import Path
import ast,hashlib,json,sys,sysconfig,unittest
ROOT=Path(__file__).resolve().parents[5]
LOCK=ROOT/'.tools/3d_pipeline/config/dependencies.lock.json'
class ReleaseConsistency(unittest.TestCase):
 def setUp(self):
  self.route=json.loads(LOCK.read_text())['routes']['blender_hoi4_adapter'];self.config=json.loads((ROOT/self.route['config']).read_text())
 def test_version_and_exact_operation_list(self):
  self.assertEqual(self.route['version'],self.config['adapter_version']);self.assertEqual(self.route['operations'],self.config['operations']);self.assertEqual(len(self.route['operations']),len(set(self.route['operations'])))
 def test_every_locked_source_hash(self):
  for rel,expected in self.route['source_sha256'].items():
   with self.subTest(path=rel):
    path=ROOT/rel;self.assertTrue(path.is_file());self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest().upper(),expected.upper())
 def test_local_import_closure_is_locked(self):
  folder=ROOT/'.tools/3d_pipeline/adapter';stdlib=Path(sysconfig.get_paths()['stdlib']);external={'bpy','bmesh','mathutils','mcp','io_pdx_mesh','io_anim_bvh'}
  for rel in self.route['source_sha256']:
   path=ROOT/rel
   if path.parent!=folder or path.suffix!='.py':continue
   for node in ast.walk(ast.parse(path.read_text())):
    modules=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module] if isinstance(node,ast.ImportFrom) and node.module else []
    for module in modules:
     module=module.split('.')[0];local=folder/(module+'.py')
     if local.is_file():self.assertIn(local.relative_to(ROOT).as_posix(),self.route['source_sha256'])
     else:self.assertTrue(module in external or module in sys.builtin_module_names or (stdlib/(module+'.py')).exists() or (stdlib/module).exists(),f'Missing/unclassified import {module} in {rel}')
if __name__=='__main__':unittest.main()
