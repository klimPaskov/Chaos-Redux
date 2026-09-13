import copy
import unittest
from mesh_vertex_material_repair import validate_vertex_edits

class VertexContracts(unittest.TestCase):
    def setUp(self): self.rows=[{'index':1,'weights':[{'bone':'Hand','weight':1}]}]
    def check(self,rows): return validate_vertex_edits(rows,5,{'Hand','Root'},{'Hand','Root'})
    def test_explicit_weights_only_and_position_only(self):
        self.assertEqual(self.check(self.rows),{1})
        self.assertEqual(self.check([{'index':2,'world_position':[1,2,3]}]),{2})
    def test_unknown_or_duplicate_vertices_rejected(self):
        for rows in ([{'index':5,'world_position':[0,0,0]}],self.rows*2):
            with self.assertRaises(ValueError): self.check(rows)
    def test_nonfinite_positions_and_unapproved_bones_rejected(self):
        for rows in ([{'index':1,'world_position':[float('nan'),0,0]}],[{'index':1,'weights':[{'bone':'NewRig','weight':1}]}]):
            with self.assertRaises(ValueError): self.check(rows)
    def test_weights_must_be_explicitly_normalized(self):
        for weight in (0,-1,.75,2,float('inf')):
            with self.assertRaises(ValueError): self.check([{'index':1,'weights':[{'bone':'Hand','weight':weight}]}])

if __name__=='__main__': unittest.main()
