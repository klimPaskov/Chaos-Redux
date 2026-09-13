"""Pure tiny-seam contract and retained Temporal canonical-byte regression.

These tests do not import Blender or modify any model. Native RNA preservation
and saved/reopened deformation evidence are separate required acceptance gates.
"""
import ast
import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[3]
MODULE = ROOT/".tools/3d_pipeline/adapter/mesh_winding_seam.py"
SPEC = importlib.util.spec_from_file_location("mesh_winding_seam", MODULE)
repair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repair)
POSITIONS = [(0.,0.,0.), (1.,0.,0.), (0.,1.,0.), (0.,0.,1.)]
FACES = [(0,2,1), (0,1,3), (0,3,2), (1,2,3)]


class SeamContract(unittest.TestCase):
    def test_volume_bound_for_closed_tetrahedron(self):
        flips, normals, proof = repair._orient_component(POSITIONS, FACES, list(range(4)))
        self.assertFalse(any(flips.values()))
        self.assertEqual(proof["cap_volume_absolute_upper_bound"], 0.)
        self.assertAlmostEqual(proof["closed_volume_interval"][0], 1/6)

    def test_orientation_corrects_all_corruption_patterns(self):
        for mask in range(16):
            faces = [tuple(reversed(f)) if mask & (1 << i) else f for i, f in enumerate(FACES)]
            flips, normals, proof = repair._orient_component(POSITIONS, faces, list(range(4)))
            inverted = proof["closed_volume_interval"][1] < 0
            self.assertEqual(sorted(i for i, f in flips.items() if f != inverted), [i for i in range(4) if mask & (1 << i)])

    def test_large_open_body_rejected(self):
        with self.assertRaisesRegex(ValueError, "0.5 percent"):
            repair.plan_seam_winding(POSITIONS, FACES, [3], [0,1,2])

    def test_bad_indices_and_reference_overlap_rejected(self):
        for selected, neighbors in (([3,3],[0]), ([True],[0]), ([4],[0]), ([3],[3])):
            with self.assertRaises(ValueError):
                repair.plan_seam_winding(POSITIONS, FACES, selected, neighbors)

    def test_nonfinite_and_invalid_vertex_indices_rejected(self):
        with self.assertRaises(ValueError):
            repair.plan_seam_winding([(float("nan"),0,0)]+POSITIONS[1:], FACES, [3], [0])
        with self.assertRaises(ValueError):
            repair.plan_seam_winding(POSITIONS, [(0,1,99)]+FACES[1:], [3], [0])

    def test_native_route_has_no_weld_caps_new_mesh_or_culling_shortcut(self):
        source = MODULE.read_text(encoding="utf-8")
        calls = [ast.unparse(n.func) for n in ast.walk(ast.parse(source)) if isinstance(n,ast.Call)]
        for forbidden in ("bmesh", "from_pydata", "remove_doubles", "bpy.data.meshes.new", "mesh.polygons.add", "mesh.vertices.remove"):
            self.assertFalse(any(forbidden in call for call in calls))
        self.assertIn("mesh.vertices.add", calls)
        self.assertIn("mesh.edges.add", calls)
        self.assertIn("mesh.polygons[index].flip", calls)
        self.assertNotIn("use_backface_culling = False", source)
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Call) and ast.unparse(node.func) == "bpy.ops.wm.open_mainfile":
                self.assertTrue(any(k.arg == "use_scripts" and isinstance(k.value, ast.Constant) and k.value.value is False for k in node.keywords))


class TemporalExactSourceRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT/"docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/export/mesh/chaosx_temporal_guard.txt"
        if not path.exists():
            raise unittest.SkipTest("Retained non-shipping Temporal fixture absent; native acceptance remains required.")
        raw = path.read_text(encoding="utf-8")
        def array(name, kind, count, stride):
            flat = json.loads(re.search(r"(?m)^\s*"+name+r" \("+kind+r", "+str(count)+r"\):\s*(\[[^\r\n]+\])", raw).group(1))
            return [tuple(flat[i:i+stride]) for i in range(0,count,stride)]
        cls.positions = [(x,z,y) for x,y,z in array("p","float",116718,3)]
        cls.faces = [tuple(reversed(f)) for f in array("tri","int",90000,3)]
        cls.streams = {"uv": array("u0","float",77812,2), "weights": array("w","float",155624,4), "joints": array("ix","int",155624,4)}
        cls.selected, cls.neighbors = [18842,18855,19083], [18604,18679,18777,19254]
        cls.plan = repair.plan_seam_winding(cls.positions, cls.faces, cls.selected, cls.neighbors)

    def test_exact_parent_approved_duplicate_and_flip_plan(self):
        self.assertEqual(self.plan["duplicate_vertex_indices"], [24472,24525,24527,24632,25082])
        self.assertEqual(len(self.plan["flip_face_indices"]), 12195)
        self.assertEqual(self.plan["flip_face_indices_sha256"], "8917252F7EE785DBF65B9ACB9BB9727EC55CECA3EBDDF2B5E395AD463946DCCD")

    def test_robust_body_volume_and_explicit_patch_alignment(self):
        self.assertAlmostEqual(self.plan["body"]["closed_volume_interval"][0], 8.44893564595355)
        self.assertAlmostEqual(self.plan["body"]["cap_area_bound_ratio"], .002001139696371477)
        self.assertAlmostEqual(self.plan["patch"]["area_weighted_reference_alignment"], .9870052804325493)
        self.assertGreater(min(self.plan["patch"]["per_face_reference_alignment"].values()), .58)

    def test_every_original_corner_position_uv_and_weight_exact(self):
        mapping = self.plan["duplicate_vertex_map"]
        faces = [tuple(mapping.get(v,v) for v in f) if i in self.selected else f for i,f in enumerate(self.faces)]
        for stream in [self.positions]+list(self.streams.values()):
            values = stream+[stream[i] for i in self.plan["duplicate_vertex_indices"]]
            for before, after in zip(self.faces, faces):
                self.assertEqual([stream[i] for i in before], [values[i] for i in after])

    def test_repaired_surface_is_outward_without_remaining_shared_seam(self):
        mapping = self.plan["duplicate_vertex_map"]
        positions = self.positions+[self.positions[i] for i in self.plan["duplicate_vertex_indices"]]
        flipped = set(self.plan["flip_face_indices"])
        faces = [tuple(mapping.get(v,v) for v in f) if i in self.selected else f for i,f in enumerate(self.faces)]
        faces = [tuple(reversed(f)) if i in flipped else f for i,f in enumerate(faces)]
        result = repair.plan_seam_winding(positions, faces, self.selected, self.neighbors)
        self.assertEqual(result["duplicate_vertex_indices"], [])
        self.assertEqual(result["flip_face_indices"], [])
        self.assertEqual(len(faces),30000)
        self.assertEqual(len(set(positions)),14997)


if __name__ == "__main__":
    unittest.main()
