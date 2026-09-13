from pathlib import Path
import sys,unittest,copy,ast
sys.path.insert(0,str(Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche').resolve()));sys.path.insert(1,str(Path('.tools/3d_pipeline/adapter').resolve()));from explicit_vertex_remap import validate_remap
class T(unittest.TestCase):
 def setUp(self):
  self.positions=[[0,0,0],[1,0,0],[1,1,0],[0,1,0]];self.weights=[[(0,1.0)]]*4;self.faces=[[0,1,2],[0,2,3]];self.spec={'mesh_name':'Body','target_armature_name':'Rig','split_vertices':[{'name':'fan','source_vertex':0}],'corner_remaps':[{'face_index':0,'source_vertex':0,'target_vertex':'fan'}],'remove_unused_vertices':[],'triangle_ceiling':100}
 def test_exact_split(self):self.assertEqual(validate_remap(self.spec,self.positions,self.weights,self.faces)[1][0],['fan',1,2])
 def test_exact_coincident_alias(self):
  self.positions.append([0,0,0]);self.weights.append([(0,1.0)]);self.faces[0][0]=4;self.spec.update(split_vertices=[],corner_remaps=[{'face_index':0,'source_vertex':4,'target_vertex':0}],remove_unused_vertices=[4]);self.assertEqual(validate_remap(self.spec,self.positions,self.weights,self.faces)[2],{4})
 def test_noncoincident_and_weight_drift_rejected(self):
  for positions,weights in [(self.positions,self.weights),([self.positions[0]]+self.positions[1:],self.weights)]:
   s=copy.deepcopy(self.spec);s['split_vertices']=[];s['corner_remaps'][0]['target_vertex']=3
   with self.assertRaises(ValueError):validate_remap(s,positions,weights,self.faces)
 def test_unknown_duplicate_corner_unused_removal_rejected(self):
  for change in ({'corner_remaps':self.spec['corner_remaps']*2},{'remove_unused_vertices':[1]},{'split_vertices':self.spec['split_vertices']*2}):
   s=copy.deepcopy(self.spec);s.update(change)
   with self.assertRaises(ValueError):validate_remap(s,self.positions,self.weights,self.faces)
 def test_source_modules_parse(self):
  for p in Path('docs/plans/3d_model_workflow_plans/adapter_recovery_drafts/tenth_tranche').glob('*.py'):ast.parse(p.read_text())
unittest.main()
