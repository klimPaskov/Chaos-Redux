import copy
import sys
from pathlib import Path
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
from mesh_patch_repair import validate_patch

class PatchContracts(unittest.TestCase):
    def setUp(self):
        self.vertices=[[0,0,0],[1,0,0],[0,1,0],[0,0,1]]
        self.faces=[[0,1,3],[1,2,3],[2,0,3]]
        self.spec={'mesh_name':'body','target_armature_name':'rig','remove_face_indices':[], 'boundary_loops':[{'name':'base','vertex_indices':[0,1,2]}], 'added_vertices':[{'name':'center','world_position':[1/3,1/3,0],'weights':[{'bone':'root','weight':1}]}], 'replacement_triangles':[{'vertices':v,'material_index':0,'loop_uvs':{'UVMap':[[0,0],[1,0],[.5,.5]]}} for v in [[1,0,'center'],[2,1,'center'],[0,2,'center']]],'triangle_ceiling':10}
    def valid(self,spec): return validate_patch(spec,self.vertices,self.faces,1,['UVMap'],{'root'})
    def test_explicit_fan_closes_named_loop(self):
        result=self.valid(self.spec); self.assertEqual(result['added_triangles'],3)
    def test_reversed_boundary_winding_is_rejected(self):
        spec=copy.deepcopy(self.spec); spec['replacement_triangles'][0]['vertices'].reverse()
        with self.assertRaises(ValueError): self.valid(spec)
    def test_unnormalized_new_weights_are_rejected(self):
        spec=copy.deepcopy(self.spec); spec['added_vertices'][0]['weights'][0]['weight']=.7
        with self.assertRaises(ValueError): self.valid(spec)
    def test_missing_uv_and_unused_new_vertex_are_rejected(self):
        spec=copy.deepcopy(self.spec); spec['replacement_triangles'][0]['loop_uvs']={}
        with self.assertRaises(ValueError): self.valid(spec)
        spec=copy.deepcopy(self.spec); spec['added_vertices'].append({'name':'unused','world_position':[0,0,.2],'weights':[{'bone':'root','weight':1}]})
        with self.assertRaises(ValueError): self.valid(spec)
    def test_unrigged_static_source_uses_empty_weights(self):
        spec=copy.deepcopy(self.spec); spec['target_armature_name']=''; spec['added_vertices'][0]['weights']=[]
        validate_patch(spec,self.vertices,self.faces,1,['UVMap'],set())
    def test_undeclared_boundary_vertex_is_rejected(self):
        spec=copy.deepcopy(self.spec); spec['replacement_triangles'][0]['vertices'][0]=3
        with self.assertRaises(ValueError): self.valid(spec)

if __name__=='__main__': unittest.main()
